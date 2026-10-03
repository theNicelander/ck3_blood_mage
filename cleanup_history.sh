#!/usr/bin/env bash
# cleanup_history.sh
set -e

BACKUP_DIR=$(mktemp -d)
echo "Backing up current textures to $BACKUP_DIR..."
rsync -a --prune-empty-dirs --include '*/' --include '*.dds' --include '*.png' --include '*.tga' --exclude '*' gfx/ "$BACKUP_DIR/gfx/"

echo "Purging texture history..."
git filter-repo --invert-paths --force \
  --path-glob '*.dds' \
  --path-glob '*.png' \
  --path-glob '*.tga'

echo "Restoring current textures..."
rsync -a "$BACKUP_DIR/gfx/" gfx/
git add gfx/
git commit -m "chore: snapshot current textures"
rm -rf "$BACKUP_DIR"

echo "Done. Re-add remote if needed and force push."
