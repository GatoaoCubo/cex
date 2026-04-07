# Naming Convention — CEX ISO Packages

> Canonical rules for all agent folders, ISO files, prompts, and data files.
> Source of truth: this file. Applies to all files under `packages/` and `decks/`.

---

## Agent Folders

| Rule | Detail |
|------|--------|
| Case | `snake_case` |
| Suffix | No `_agent` suffix (use `anuncio`, not `anuncio_agent`) |
| Max length | 30 characters |
| Separator | Underscore only. No hyphens in new packages |
| Examples | `anuncio`, `knowledge_distiller`, `gateway`, `web_scraper` |

**Exception**: Legacy agents with hyphens (`amazon-ads-agent`, `tool-shed`) are grandfathered.
Do not rename during migration — only normalize on new package creation.

---

## ISO File Names (Canonical)

The canonical ISO Package spec uses human-readable filenames. Legacy agents used
`ISO_{AGENT_GROUP}_{NNN}_{TYPE}.md` — this table maps old to new.

### Conversion Table: OLD → NEW

| OLD (iso_vectorstore/) | NEW (packages/) | pillar | Required |
|------------------------|-----------------|-----|----------|
| `ISO_*_MANIFEST.md` | `manifest.yaml` | P02 | YES |
| `ISO_*_SYSTEM_INSTRUCTION.md` | `system_instruction.md` | P03 | YES |
| `ISO_*_INSTRUCTIONS.md` | `instructions.md` | P03 | YES |
| `ISO_*_ARCHITECTURE.md` | `architecture.md` | P08 | Recommended |
| `ISO_*_OUTPUT_TEMPLATE.md` | `output_template.md` | P05 | Recommended |
| `ISO_*_EXAMPLES.md` | `examples.md` | P07 | Recommended |
| `ISO_*_ERROR_HANDLING.md` | `error_handling.md` | P11 | Recommended |
| `ISO_*_QUICK_START.md` | `quick_start.md` | P01 | Optional |
| `ISO_*_INPUT_SCHEMA.md` | `input_schema.yaml` | P06 | Optional |
| `ISO_*_UPLOAD_KIT.md` | `upload_kit.md` | P04 | Optional |
| `ISO_*_UPLOAD_KIT_WHITELABEL.md` | `upload_kit_whitelabel.md` | P04 | Whitelabel |
| `ISO_*_SYSTEM_INSTRUCTION_WHITELABEL.md` | `system_instruction_whitelabel.md` | P03 | Whitelabel |
| `ISO_*_README.md` | `README.md` | — | Package root |

### File Type Rules

- `manifest.yaml` — YAML only (not .md). Machine-readable identity card.
- `input_schema.yaml` — YAML only. JSON contract for inputs.
- All other files — Markdown (CommonMark), UTF-8, no hardcoded paths.

---

## Sub-Agent Prompts

Agents that spawn sub-agents store their prompt templates under `prompts/`:

```
packages/anuncio/
  prompts/
    headline_writer.md      # Sub-agent: writes ad headlines
    copy_refiner.md         # Sub-agent: refines ad copy
    audience_analyzer.md    # Sub-agent: analyzes target audience
```

| Rule | Detail |
|------|--------|
| Location | `packages/{agent}/prompts/{name}.md` |
| Case | `snake_case` |
| Format | Markdown, must be self-contained (no external imports) |
| Naming | Descriptive verb_noun: `headline_writer`, `copy_refiner` |
| Max size | 2048 tokens per prompt file |

---

## Domain Data Files

Static data, configurations, and lookup tables live under `data/`:

```
packages/pricing/
  data/
    margin_tiers.yaml       # Business rule: margin tiers by category
    platforms.yaml          # Supported platform list
    currency_map.yaml       # Currency code mappings
```

| Rule | Detail |
|------|--------|
| Location | `packages/{agent}/data/{name}.yaml` |
| Case | `snake_case` |
| Format | YAML only (not JSON, not .md) |
| Naming | Descriptive noun: `margin_tiers`, `platforms`, `currency_map` |
| No secrets | Never store API keys, tokens, passwords in data/ |

---

## Full Package Structure

```
packages/{agent_name}/
  manifest.yaml                    # REQUIRED: identity + capabilities
  system_instruction.md            # REQUIRED: system prompt
  instructions.md                  # REQUIRED: usage guide
  architecture.md                  # Recommended: flow diagram
  output_template.md               # Recommended: output format
  examples.md                      # Recommended: input/output pairs
  error_handling.md                # Recommended: error scenarios
  quick_start.md                   # Optional: 5-min setup
  input_schema.yaml                # Optional: input contract
  upload_kit.md                    # Optional: platform guide
  upload_kit_whitelabel.md         # Whitelabel tier
  system_instruction_whitelabel.md # Whitelabel tier
  prompts/                         # Sub-agent prompts (if any)
    {verb_noun}.md
  data/                            # Domain data (if any)
    {noun}.yaml
```

---

## Validation Rules

1. `manifest.yaml` must be valid YAML with fields: `id`, `version`, `type`, `title`, `domain`
2. `id` in manifest must equal the folder name (stem match)
3. `system_instruction.md` must be < 4096 tokens
4. No hardcoded paths in any file (`C:\`, `/home/`, `/Users/`)
5. File names: lowercase, snake_case, ASCII only
6. `prompts/` files: prefix with action verb (`write_`, `analyze_`, `refine_`)
7. `data/` files: plural nouns preferred (`tiers`, `platforms`, `rules`)

---

## Migration Path

Legacy `records/agents/{name}/iso_vectorstore/ISO_*_*.md`
→ New `packages/{name}/{canonical_name}`

Use `_tools/rename_iso.py` for automated conversion:
```bash
python _tools/rename_iso.py \
  --source records/agents/anuncio/iso_vectorstore/ \
  --output packages/anuncio/ \
  --dry-run
```

Remove `--dry-run` to execute. Tool validates portability before writing.

---

*Naming Convention v1.0 | CEX Framework | 2026-03-23*
