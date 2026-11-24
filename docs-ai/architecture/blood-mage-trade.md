# CK3 1.21 Trade Modifiers & Mod Budget

## Vanilla 1.21 Baselines (`common/defines/00_defines.txt`, `NTrade`)

- `BASE_MAX_TRADE_GOODS_ON_ROUTE = 1`, hard cap `MAX_TRADE_GOODS_ON_ROUTE_CAP = 6` (vanilla grants `+1` rarely: Wealth perk, Monsoon tradition, Republic laws/contracts, Merchant Company domicile).
- `BASE_MAX_TRADE_ROUTES = 1` (capstone-tier in vanilla: T5 merchant legacy, Republic laws, domicile, duchy office, trade leagues).
- `BASE_MAX_TRADE_MARKETS_ON_ROUTE = 3`, `BASE_TRADE_POST_LIMIT = 2`, `BASE_MAX_TRADE_ROUTE_LENGTH = 10`, `BASE_TRADE_CAPACITY = 35`.

## Blood Mages Trade Budget

- **Do not stack route/goods caps or scatter trade bloat across core Blood Mage modifiers** (follow root `AGENTS.md` modifier priority: all playstyles > landed rulers > niche playstyles):
  - `max_trade_goods_on_route = 1`: **1 source only** (`bm_tradition_verbudir`, mirrors vanilla Monsoon tradition; holds the mod's maritime/fishing trade modifiers).
  - `max_trade_routes = 1`: **1 source only** (`dynasty_blood_fortune_modifier_3`, mirrors T5 merchant legacy; single trade nod on Covenant of Fortune).
- Keep Blessing of Fortune, Fortunate Lifeforce, and Nábrókarstafur focused on all-playstyle and landed economy rather than merchant/trade modifiers.

## Formatting & Allowlist Gotchas (`00_gdp_definitions.txt`, `00_trade_definitions.txt`)

- `trade_category_all_{sell,buy}_price_mult`: `decimals = 2` (`0.005` displays `+0.50%`). Keep values tiny (`0.005`–`0.02`; vanilla max ~`0.03`), as margins compound fast.
- `trade_expertise_growth_mult`: `decimals = 1` (%). `trade_post_limit_add`: `decimals = 0`.
- Register any new vanilla trade modifier via `python3 scripts/check_modifiers.py --add <mod> --scope <character|county|domicile>`.
