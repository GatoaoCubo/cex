---
id: kc_brand_variable_audit
kind: knowledge-card
domain: meta
pillar: P01
version: "1.0"
created: "2026-04-07"
updated: "2026-04-07"
quality: 9.1
tags: [brand, variables, audit, template, injection, N04]
tldr: "Full audit of 44 {{BRAND_*}} template variables across 68 files. 13 gaps fixed."
density_score: 1.0
related:
  - spec_n06_brand_verticalization
  - tpl_brand_context_nucleus
  - bld_knowledge_card_prompt_template
  - bld_memory_prompt_template
  - p01_kc_open_variable
  - n06_output_brand_one_pager
  - n06_output_brand_config
  - p03_ins_prompt_template
  - p02_agent_brand_nucleus
  - kc_instance_variable_registry
---

# Brand Template Variable Audit

## Summary

| Metric | Before | After |
|--------|--------|-------|
| Unique `{{BRAND_*}}` variables in use | 44 | 44 |
| Files referencing brand variables | 68 | 68 |
| Variables with NO config mapping | 13 | 0 |
| Derived variables (computed) | 0 | 3 |
| Alias mappings | 0 | 3 |
| `| default:` syntax supported | No | Yes |

## Gaps Found & Fixed

### Category A: Missing from `brand_config_template.yaml` (added)

| Variable | Uses | Section Added To |
|----------|------|-----------------|
| `BRAND_BIO` | 1 | identity |
| `BRAND_ESSENCE` | 2 | identity |
| `BRAND_MANIFESTO` | 1 | identity |
| `BRAND_PERSON` | 2 | voice |
| `BRAND_ENERGY` | 2 | voice |
| `BRAND_COUNTRY` | 2 | audience |
| `BRAND_HASHTAG` | 1 | positioning |
| `BRAND_TAGS` | 1 | positioning |

### Category B: Derived Variables (computed by `brand_inject.py`)

| Variable | Uses | Derivation |
|----------|------|-----------|
| `BRAND_SLUG` | 4 | `re.sub(r'[^a-z0-9]+', '-', BRAND_NAME.lower())` |
| `BRAND_UPPER` | 1 | `BRAND_NAME.upper()` |
| `BRAND_NAME_SHORT` | 1 | `BRAND_NAME.split()[0]` |

### Category C: Aliases (mapped in `brand_inject.py`)

| Alias | Canonical | Uses |
|-------|-----------|------|
| `BRAND_TONE` | `BRAND_VOICE_TONE` | 5 |
| `BRAND_VOICE` | `BRAND_VOICE_TONE` | 30 |
| `BRAND_NICHE` | `BRAND_CATEGORY` | 2 |

### Category D: Runtime Variables (no fix needed)

| Variable | Uses | Reason |
|----------|------|--------|
| `BRAND_CONTEXT` | 2 | Computed at prompt assembly time by `cex_prompt_layers.py` |

## Files Modified

1. **`_tools/brand_inject.py`** — Added `compute_derived()`, `BRAND_ALIASES`, `_DEFAULT_PATTERN` for `| default:` syntax
2. **`.cex/brand/brand_config_template.yaml`** — Added 8 missing fields across 4 sections
3. **`.cex/brand/brand_config_schema.yaml`** — Added matching schema definitions for all new fields
4. **`_tools/brand_propagate.py`** — Added new vars to nucleus routing, fixed N01 dir name, added N06
5. **`_tools/brand_validate.py`** — Added validation for `BRAND_PERSON` and `BRAND_ENERGY`

## Variable Registry (44 total)

### identity (10)
`BRAND_NAME` · `BRAND_TAGLINE` · `BRAND_SLOGAN` · `BRAND_MISSION` · `BRAND_VISION` · `BRAND_VALUES` · `BRAND_STORY` · `BRAND_BIO` · `BRAND_ESSENCE` · `BRAND_MANIFESTO`

### archetype (2)
`BRAND_ARCHETYPE` · `BRAND_ARCHETYPE_SHADOW`

### voice (11)
`BRAND_VOICE_TONE` · `BRAND_VOICE_FORMALITY` · `BRAND_VOICE_ENTHUSIASM` · `BRAND_VOICE_HUMOR` · `BRAND_VOICE_WARMTH` · `BRAND_VOICE_AUTHORITY` · `BRAND_VOICE_DO` · `BRAND_VOICE_DONT` · `BRAND_LANGUAGE` · `BRAND_PERSON` · `BRAND_ENERGY`

### audience (9)
`BRAND_ICP` · `BRAND_ICP_AGE` · `BRAND_ICP_LOCATION` · `BRAND_ICP_INCOME` · `BRAND_ICP_VALUES` · `BRAND_ICP_FEARS` · `BRAND_ICP_ASPIRATIONS` · `BRAND_TRANSFORMATION` · `BRAND_COUNTRY`

### visual (5)
`BRAND_COLORS` · `BRAND_FONTS` · `BRAND_LOGO_URL` · `BRAND_FAVICON_URL` · `BRAND_STYLE`

### positioning (7)
`BRAND_CATEGORY` · `BRAND_UVP` · `BRAND_DIFFERENTIATOR` · `BRAND_COMPETITORS` · `BRAND_CONTENT_PILLARS` · `BRAND_HASHTAG` · `BRAND_TAGS`

### monetization (5)
`BRAND_PRICING_MODEL` · `BRAND_CURRENCY` · `BRAND_PRICE_ANCHOR` · `BRAND_TIERS` · `BRAND_PAYMENT_PROVIDERS`

### derived (3) — computed, not stored
`BRAND_SLUG` · `BRAND_UPPER` · `BRAND_NAME_SHORT`

### aliases (3) — mapped, not stored
`BRAND_TONE` → `BRAND_VOICE_TONE` · `BRAND_VOICE` → `BRAND_VOICE_TONE` · `BRAND_NICHE` → `BRAND_CATEGORY`

### runtime (1) — injected at prompt assembly
`BRAND_CONTEXT`

## N02 Marketing: `| default:` Syntax

N02's `brand_override_config.md` and `brand_voice_templates.md` use 40+ variables with Jinja-like defaults:
```
{{BRAND_PERSON | default: '2nd_person'}}
{{BRAND_HASHTAG_STRATEGY | default: 'minimal'}}
```
These are now handled by `_DEFAULT_PATTERN` in `brand_inject.py`. When a variable is unset, the default value is used.

## Verification

```bash
python -c "import _tools.brand_inject as bi; print(bi.inject_brand('{{BRAND_SLUG}}', {'identity':{'BRAND_NAME':'Test'}}))"
# Output: test

python -c "import _tools.brand_inject as bi; print(bi.inject_brand('{{BRAND_VOICE}}', {'voice':{'BRAND_VOICE_TONE':'bold'}}))"
# Output: bold

python -c "import _tools.brand_inject as bi; print(bi.inject_brand(\"{{BRAND_X | default: 'fallback'}}\", {}))"
# Output: fallback
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_n06_brand_verticalization]] | downstream | 0.30 |
| [[tpl_brand_context_nucleus]] | downstream | 0.27 |
| [[bld_knowledge_card_prompt_template]] | related | 0.25 |
| [[bld_memory_prompt_template]] | downstream | 0.25 |
| [[p01_kc_open_variable]] | related | 0.24 |
| [[n06_output_brand_one_pager]] | downstream | 0.24 |
| [[n06_output_brand_config]] | downstream | 0.23 |
| [[p03_ins_prompt_template]] | downstream | 0.22 |
| [[p02_agent_brand_nucleus]] | downstream | 0.22 |
| [[kc_instance_variable_registry]] | sibling | 0.21 |
