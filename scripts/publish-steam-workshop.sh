#!/usr/bin/env bash

set -euo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly MOD_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

app_id="${STEAM_APP_ID:-}"
published_file_id="${STEAM_PUBLISHED_FILE_ID:-}"
workshop_url=""
notes=""
notes_file=""
steam_username=""
steam_password=""
steam_shared_secret=""
steam_guard_mode=""
env_file="${STEAM_WORKSHOP_ENV_FILE:-${MOD_DIR}/.env}"
assume_yes=false
dry_run=false

usage() {
  cat <<'EOF'
Publish this mod to an existing Steam Workshop item with release notes.

Usage:
  ./scripts/publish-steam-workshop.sh --notes "Release notes" [options]
  ./scripts/publish-steam-workshop.sh --notes-file RELEASE_NOTES.md [options]

Options:
  --notes TEXT          Release notes to attach to this Workshop update.
  --notes-file PATH     Read release notes from a UTF-8 text file.
  --username USERNAME   Override the Steam account configured in the env file.
  --env-file PATH       Configuration file (default: .env).
  --yes                 Skip the final confirmation prompt.
  --dry-run             Build and inspect the upload without publishing it.
  -h, --help            Show this help.

Configuration:
  STEAM_APP_ID and STEAM_PUBLISHED_FILE_ID select the target Workshop item.
  Missing or invalid IDs are requested interactively. Non-interactive runs
  require valid IDs in the environment or configuration file.

Authentication:
  The configuration file accepts STEAM_USERNAME, STEAM_PASSWORD, and
  STEAM_GUARD. STEAM_GUARD accepts auto (default), enabled, or disabled. When
  required, steamguard-cli supplies the code automatically.
  STEAM_SHARED_SECRET remains supported as a fallback.
EOF
}

fail() {
  printf 'Error: %s\n' "$*" >&2
  exit 1
}

resolve_numeric_id() {
  local setting_name="$1"
  local prompt="$2"
  local value="$3"

  while [[ ! "${value}" =~ ^[1-9][0-9]*$ ]]; do
    if [[ -n "${value}" ]]; then
      printf 'Warning: %s must be a positive integer.\n' "${setting_name}" >&2
    fi
    [[ -t 0 ]] \
      || fail "${setting_name} must be a positive integer in ${env_file} or the environment"
    read -r -p "${prompt}: " value \
      || fail "could not read ${setting_name} from the terminal"
  done

  printf '%s' "${value}"
}

vdf_escape() {
  local value="$1"
  value="${value//\\/\\\\}"
  value="${value//\"/\\\"}"
  value="${value//$'\r'/}"
  # Keep physical line breaks: SteamCMD publishes an escaped \n literally.
  printf '%s' "${value}"
}

wait_for_steam_guard_window() {
  local remaining=$((30 - ($(date +%s) % 30)))
  if (( remaining < 15 )); then
    sleep $((remaining + 1))
  fi
}

generate_steam_guard_code_from_cli() {
  local cli_username=""
  local code=""

  cli_username="$(printf '%s' "${steam_username}" | tr '[:upper:]' '[:lower:]')"
  wait_for_steam_guard_window

  code="$(
    steamguard \
      --verbosity error \
      --no-update-check \
      --username "${cli_username}" \
      code --offline
  )" || return 1
  code="${code%$'\r'}"

  [[ "${code}" =~ ^[23456789BCDFGHJKMNPQRTVWXY]{5}$ ]] || return 1
  printf '%s' "${code}"
}

generate_steam_guard_code_from_secret() {
  command -v python3 >/dev/null 2>&1 \
    || fail "python3 is required for automatic Steam Guard codes"

  local code=""
  wait_for_steam_guard_window
  code="$(
    printf '%s' "${steam_shared_secret}" | python3 -c '
import base64
import hashlib
import hmac
import struct
import sys
import time

alphabet = "23456789BCDFGHJKMNPQRTVWXY"
secret = base64.b64decode(sys.stdin.read().strip(), validate=True)

counter = int(time.time()) // 30
digest = hmac.new(secret, struct.pack(">Q", counter), hashlib.sha1).digest()
offset = digest[-1] & 0x0F
value = struct.unpack(">I", digest[offset:offset + 4])[0] & 0x7FFFFFFF

code = ""
for _ in range(5):
    code += alphabet[value % len(alphabet)]
    value //= len(alphabet)

print(code)
'
  )" || fail "STEAM_SHARED_SECRET is not a valid base64 Steam shared_secret"

  [[ "${code}" =~ ^[23456789BCDFGHJKMNPQRTVWXY]{5}$ ]] \
    || fail "failed to generate a valid Steam Guard code"
  printf '%s' "${code}"
}

ask_yes_no() {
  local prompt="$1"
  local answer=""

  [[ -t 0 ]] || return 1
  read -r -p "${prompt} [y/N] " answer
  [[ "${answer}" == "y" || "${answer}" == "Y" ]]
}

offer_steamguard_cli_setup() {
  printf '\nWarning: this account has Steam Guard enabled, but no automatic code is available.\n' >&2

  if ! command -v steamguard >/dev/null 2>&1; then
    if ask_yes_no "Install steamguard-cli now with Cargo?"; then
      command -v cargo >/dev/null 2>&1 \
        || fail "Cargo is required to install steamguard-cli: https://rustup.rs"
      cargo install steamguard-cli --version 0.18.4 --locked \
        || fail "steamguard-cli installation failed"
    else
      printf 'Continuing without steamguard-cli; SteamCMD may request a code interactively.\n' >&2
      return 1
    fi
  fi

  if steam_guard_code="$(generate_steam_guard_code_from_cli)"; then
    return 0
  fi

  printf 'steamguard-cli is installed but has no usable authenticator for %s.\n' "${steam_username}" >&2
  if ask_yes_no "Run 'steamguard setup' now?"; then
    steamguard setup || fail "steamguard-cli setup failed"
    steam_guard_code="$(generate_steam_guard_code_from_cli)" \
      || fail "steamguard-cli still cannot generate a code for ${steam_username}"
    printf 'Consider running steamguard encrypt afterward and storing its passkey in macOS Keychain.\n' >&2
    return 0
  fi

  printf 'Continuing without an automatic code; SteamCMD may request one interactively.\n' >&2
  return 1
}

load_account_env() {
  local line=""
  local line_number=0
  local key=""
  local value=""

  [[ -f "${env_file}" ]] || return 0

  while IFS= read -r line || [[ -n "${line}" ]]; do
    line_number=$((line_number + 1))
    line="${line%$'\r'}"
    case "${line}" in
      ''|'#'*)
        continue
        ;;
    esac

    key="${line%%=*}"
    value="${line#*=}"
    [[ "${line}" == *'='* ]] \
      || fail "invalid assignment in ${env_file} at line ${line_number}"

    case "${key}" in
      STEAM_APP_ID)
        if [[ -n "${value}" && -z "${app_id}" ]]; then
          app_id="${value}"
        fi
        ;;
      STEAM_PUBLISHED_FILE_ID)
        if [[ -n "${value}" && -z "${published_file_id}" ]]; then
          published_file_id="${value}"
        fi
        ;;
      STEAM_USERNAME)
        if [[ -n "${value}" && -z "${steam_username}" ]]; then
          steam_username="${value}"
        fi
        ;;
      STEAM_PASSWORD)
        if [[ -z "${steam_password}" ]]; then
          steam_password="${value}"
        fi
        ;;
      STEAM_GUARD)
        if [[ -z "${steam_guard_mode}" ]]; then
          steam_guard_mode="${value}"
        fi
        ;;
      STEAM_SHARED_SECRET)
        if [[ -z "${steam_shared_secret}" ]]; then
          steam_shared_secret="${value}"
        fi
        ;;
      *)
        fail "unsupported setting in ${env_file}: ${key}"
        ;;
    esac
  done <"${env_file}"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --notes)
      [[ $# -ge 2 ]] || fail "--notes requires a value"
      notes="$2"
      shift 2
      ;;
    --notes-file)
      [[ $# -ge 2 ]] || fail "--notes-file requires a path"
      notes_file="$2"
      shift 2
      ;;
    --username)
      [[ $# -ge 2 ]] || fail "--username requires a value"
      steam_username="$2"
      shift 2
      ;;
    --env-file)
      [[ $# -ge 2 ]] || fail "--env-file requires a path"
      env_file="$2"
      shift 2
      ;;
    --yes)
      assume_yes=true
      shift
      ;;
    --dry-run)
      dry_run=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      fail "unknown option: $1"
      ;;
  esac
done

if [[ -z "${steam_username}" && -n "${STEAM_USERNAME:-}" ]]; then
  steam_username="${STEAM_USERNAME}"
fi
if [[ -n "${STEAM_PASSWORD:-}" ]]; then
  steam_password="${STEAM_PASSWORD}"
  unset STEAM_PASSWORD
fi
if [[ -n "${STEAM_SHARED_SECRET:-}" ]]; then
  steam_shared_secret="${STEAM_SHARED_SECRET}"
  unset STEAM_SHARED_SECRET
fi
if [[ -n "${STEAM_GUARD:-}" ]]; then
  steam_guard_mode="${STEAM_GUARD}"
fi
if [[ -f "${env_file}" ]]; then
  load_account_env
fi
app_id="$(resolve_numeric_id "STEAM_APP_ID" "Steam app ID" "${app_id}")"
published_file_id="$(
  resolve_numeric_id \
    "STEAM_PUBLISHED_FILE_ID" \
    "Steam Workshop item ID" \
    "${published_file_id}"
)"
workshop_url="https://steamcommunity.com/sharedfiles/filedetails/?id=${published_file_id}"
readonly app_id published_file_id workshop_url

steam_guard_mode="${steam_guard_mode:-auto}"
case "${steam_guard_mode}" in
  auto|enabled|disabled)
    ;;
  *)
    fail "STEAM_GUARD must be auto, enabled, or disabled"
    ;;
esac
if [[ ( -n "${steam_password}" || -n "${steam_shared_secret}" ) && -f "${env_file}" ]]; then
  chmod 600 "${env_file}" \
    || fail "could not restrict ${env_file} to owner-only permissions"
fi

[[ -z "${notes}" || -z "${notes_file}" ]] \
  || fail "use either --notes or --notes-file, not both"

if [[ -n "${notes_file}" ]]; then
  [[ -f "${notes_file}" ]] || fail "release-notes file not found: ${notes_file}"
  notes="$(<"${notes_file}")"
fi

[[ -n "${notes}" ]] || fail "release notes are required; use --notes or --notes-file"

readonly DESCRIPTOR="${MOD_DIR}/descriptor.mod"
[[ -f "${DESCRIPTOR}" ]] || fail "descriptor.mod not found in ${MOD_DIR}"
grep -Fq "remote_file_id=\"${published_file_id}\"" "${DESCRIPTOR}" \
  || fail "descriptor.mod is not linked to Workshop item ${published_file_id}"

build_dir="$(mktemp -d "${TMPDIR:-/tmp}/ck3-workshop-content.XXXXXX")"
vdf_file="$(mktemp "${TMPDIR:-/tmp}/ck3-workshop-vdf.XXXXXX")"

cleanup() {
  rm -rf "${build_dir}"
  rm -f "${vdf_file}"
}
trap cleanup EXIT INT TERM

# SteamCMD uploads every file in contentfolder. Stage only the distributable
# mod files so repository metadata, source artwork, and maintainer docs are not
# shipped to subscribers.
rsync -a \
  --exclude '/.git/' \
  --exclude '/.gitignore' \
  --exclude '/.env*' \
  --exclude '/.agents/' \
  --exclude '/.codex/' \
  --exclude '/scripts/' \
  --exclude '/docs/' \
  --exclude '/README.md' \
  --exclude '/WORKSHOP_DESCRIPTION.txt' \
  --exclude '/thumbnail-source.png' \
  --exclude '/ck3-tiger.conf' \
  --exclude '.DS_Store' \
  --exclude '._*' \
  --exclude '*.tmp' \
  --exclude '*.temp' \
  --exclude '*.bak' \
  --exclude '*.old' \
  "${MOD_DIR}/" "${build_dir}/"

[[ -f "${build_dir}/descriptor.mod" ]] || fail "staged upload has no descriptor.mod"

escaped_contentfolder="$(vdf_escape "${build_dir}")"
escaped_notes="$(vdf_escape "${notes}")"

cat >"${vdf_file}" <<EOF
"workshopitem"
{
    "appid" "${app_id}"
    "publishedfileid" "${published_file_id}"
    "contentfolder" "${escaped_contentfolder}"
    "changenote" "${escaped_notes}"
}
EOF

file_count="$(find "${build_dir}" -type f | wc -l | tr -d ' ')"
printf 'Steam Workshop update ready\n'
printf '  App:     %s\n' "${app_id}"
printf '  Item:    %s\n' "${published_file_id}"
printf '  URL:     %s\n' "${workshop_url}"
printf '  Files:   %s\n' "${file_count}"
printf '  Notes:\n%s\n' "${notes}"

if ${dry_run}; then
  printf '\nDry run only; nothing was uploaded.\n'
  exit 0
fi

command -v steamcmd >/dev/null 2>&1 \
  || fail "SteamCMD is not installed. Install it with: brew install --cask steamcmd"

if [[ -z "${steam_username}" ]]; then
  read -r -p 'Steam account name: ' steam_username
fi
[[ -n "${steam_username}" ]] || fail "Steam account name is required"

if ! ${assume_yes}; then
  printf '\nThis will replace the content of Workshop item %s.\n' "${published_file_id}"
  read -r -p 'Publish this update? [y/N] ' confirmation
  [[ "${confirmation}" == "y" || "${confirmation}" == "Y" ]] || fail "upload cancelled"
fi

login_args=(+login "${steam_username}")
if [[ -n "${steam_password}" ]]; then
  login_args+=("${steam_password}")
else
  printf '\nStarting SteamCMD. Enter your password and Steam Guard code when prompted.\n'
fi

steam_guard_code=""
if [[ -n "${steam_password}" && "${steam_guard_mode}" != "disabled" ]]; then
  if command -v steamguard >/dev/null 2>&1 \
    && steam_guard_code="$(generate_steam_guard_code_from_cli)"; then
    :
  elif [[ -n "${steam_shared_secret}" ]]; then
    steam_guard_code="$(generate_steam_guard_code_from_secret)"
  elif [[ "${steam_guard_mode}" == "enabled" ]]; then
    offer_steamguard_cli_setup || true
  elif ask_yes_no "steamguard-cli has no authenticator for this account. Does the Steam account have Steam Guard enabled?"; then
    offer_steamguard_cli_setup || true
  fi
fi

if [[ -n "${steam_guard_code}" ]]; then
  unset steam_shared_secret
  login_args+=("${steam_guard_code}")
  printf '\nStarting SteamCMD with the password from %s and an automatic Steam Guard code.\n' "${env_file}"
elif [[ -n "${steam_shared_secret}" && "${steam_guard_mode}" != "disabled" ]]; then
  [[ -n "${steam_password}" ]] \
    || fail "STEAM_SHARED_SECRET requires STEAM_PASSWORD for unattended login"
  steam_guard_code="$(generate_steam_guard_code_from_secret)"
  unset steam_shared_secret
  login_args+=("${steam_guard_code}")
  printf '\nStarting SteamCMD with password and automatic Steam Guard authentication from %s.\n' "${env_file}"
elif [[ -n "${steam_password}" ]]; then
  printf '\nStarting SteamCMD with the password from %s.\n' "${env_file}"
  if [[ "${steam_guard_mode}" != "disabled" ]]; then
    printf 'Steam Guard may prompt for a code if required.\n'
  fi
fi

steamcmd \
  "${login_args[@]}" \
  +workshop_build_item "${vdf_file}" \
  +quit

grep -Fq "\"publishedfileid\" \"${published_file_id}\"" "${vdf_file}" \
  || fail "SteamCMD changed the Workshop item ID unexpectedly; inspect its output before retrying"

printf '\nPublished Workshop update: %s\n' "${workshop_url}"
