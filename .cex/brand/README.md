# .cex/brand/ — The X Variable

This directory holds the single file that makes a CEX instance unique:
**`brand_config.yaml`**.

## What Is This?

CEX = Cérebro Empresarial **X**. The X is a variable.
When you bootstrap CEX for your company, X becomes YOUR brand.

```
Generic CEX          →  bootstrap  →  YOUR CEX
(brain for anyone)                    (brain for YOUR brand)
```

## Files

| File | Purpose |
|------|---------|
| `brand_config.yaml` | **THE file.** 7 sections, 41 variables. Filled by N06 or bootstrap. |
| `brand_config_template.yaml` | Empty template with `{{PLACEHOLDER}}` values. |
| `brand_config_schema.yaml` | JSON Schema spec for validation. |
| `.bootstrapped` | Lock file. Created after successful bootstrap. |

## How It Works

```
User runs CEX for the first time
  │
  ├─ boot/cex.ps1 detects missing .bootstrapped
  │     → offers Quick Bootstrap or Full Discovery
  │
  ├─ Quick Bootstrap (cex_bootstrap.py)
  │     → 13 questions, ~5 min
  │     → fills brand_config.yaml
  │     → validates, propagates, audits
  │
  └─ Full Discovery (N06 Brand Architect)
        → 15 questions, 3 phases
        → generates 32-block Brand Book
        → extracts brand_config.yaml
        → validates, propagates, audits
```

## What Propagation Does

Once `brand_config.yaml` exists:

```
N06 (generates brand_config.yaml)
  │
  ├──→ N01: BRAND_ICP, BRAND_COMPETITORS, BRAND_CATEGORY
  │      Research targets YOUR market
  │
  ├──→ N02: BRAND_VOICE, BRAND_COLORS, BRAND_FONTS
  │      Copy matches YOUR tone, HTML uses YOUR palette
  │
  ├──→ N03: BRAND_COLORS, BRAND_FONTS, BRAND_STYLE
  │      Components use YOUR design tokens
  │
  ├──→ N04: BRAND_NAME, BRAND_CATEGORY, BRAND_CONTENT_PILLARS
  │      Knowledge indexed under YOUR context
  │
  ├──→ N05: BRAND_NAME, BRAND_LOGO_URL
  │      Deploys with YOUR branding
  │
  ├──→ N07: BRAND_NAME
  │      Orchestration uses YOUR identity
  │
  ├──→ CLAUDE.md: Brand Identity section updated
  └──→ boot/*.cmd: Window titles show YOUR brand
```

## Pipeline Auto-Injection

After bootstrap, `brand_config.yaml` is automatically injected into:
- `cex_crew_runner.py compose_prompt()` — every builder prompt
- `cex_forge.py` — every artifact generation prompt

No manual injection needed. Every LLM call knows WHO it's building for.

## Commands

```bash
# First run
python _tools/cex_bootstrap.py

# Check status
python _tools/cex_bootstrap.py --check
python _tools/cex_bootstrap.py --status

# Import existing brand
python _tools/cex_bootstrap.py --from-file my_brand.yaml

# Reset and re-bootstrap
python _tools/cex_bootstrap.py --reset

# Validate
python _tools/brand_validate.py

# Propagate to nuclei
python _tools/brand_propagate.py

# Audit consistency
python _tools/brand_audit.py
```
