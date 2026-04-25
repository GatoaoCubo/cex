---
id: bld_config_default
kind: builder_default
pillar: P09
source: shared
title: "Config Default: Standard Builder Tunables"
llm_function: CONSTRAIN
version: 1.1.0
quality: 7.8
tags: [config, tunables, P09, shared, default]
tldr: "_Shared config: naming conventions, output paths, and production limits"
related:
  - bld_architecture_kind
  - kind-builder
  - bld_collaboration_kind
  - bld_instruction_kind
  - p06_is_builder_nucleus
  - ex_env_config_default
  - p02_bc_builder_nucleus
  - p12_sc_builder_nucleus
  - agent_card_engineering_nucleus
  - bld_schema_kind
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-22"
---

# P09 Config — Standard Builder Tunables

## Default Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `max_bytes` | 6144 | Maximum artifact file size in bytes |
| `density_target` | 0.85 | Minimum content density (content lines / total) |
| `quality_floor` | 8.0 | Minimum acceptable quality score |
| `quality_target` | 9.0 | Target quality score |
| `max_retries` | 2 | Maximum F6->F7 retry cycles |
| `compile_after_save` | true | Run cex_compile.py after F8 save |
| `signal_on_complete` | true | Write completion signal after F8 |
| `model_hint` | inherit | LLM tier: opus, sonnet, haiku, or inherit from nucleus |

## Override Instructions

To customize for a specific kind, create `bld_config_{kind}.md` with only the
parameters that differ from this default. The loader merges kind-specific
config over this shared default.

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `CEX_MAX_BYTES` | Override max_bytes globally |
| `CEX_QUALITY_FLOOR` | Override minimum quality floor |
| `CEX_NUCLEUS` | Active nucleus identifier (n01-n07) |
| `CEX_DRY_RUN` | When set, skip file writes and git operations |

## Pillar Subdirectory (save target)

Each kind belongs to a pillar. The builder saves output to:
`N{nucleus}_{domain}/P{pillar_number}_{pillar_name}/{artifact_filename}`

The `kind` frontmatter field determines the correct pillar via kinds_meta.json.

## Hard Gates (H01-H07) -- ALL must pass

| Gate | Check | Fail Action |
|------|-------|-------------|
| H01 | Frontmatter present and valid YAML | Return to F6, add frontmatter |
| H02 | `quality: null` in frontmatter (never self-score) | Remove score, set null |
| H03 | Required fields: id, kind, 8f, pillar, title | Add missing fields |
| H04 | Body density >= 0.85 (content lines / total lines) | Add structured data, remove filler |
| H05 | No hallucinated sources (cited paths must exist) | Remove or verify citations |
| H06 | ASCII-only in any generated code blocks | Replace non-ASCII per cex_sanitize rules |
| H07 | Output matches pillar schema constraints | Restructure to match schema |

## Scoring Dimensions (5D)

| Dimension | Weight | Criteria |
|-----------|--------|---------|
| D1 Structural | 30% | Frontmatter complete, naming correct, file in right pillar dir |
| D2 Content | 25% | Density >= 0.85, no filler, tables preferred over prose |
| D3 Accuracy | 20% | No hallucination, sources verified, constraints respected |
| D4 Usefulness | 15% | Actionable, implementable, unambiguous |
| D5 CEX fit | 10% | Kind/pillar/nucleus alignment, 8F stage correctness |

## Configuration Checklist

- Verify all required fields are present in frontmatter before saving
- Validate config values against schema constraints (type, range, enum)
- Cross-reference with related configs to avoid contradictions
- Test config loading in target runtime before committing

## Validation

```yaml
# Required config validation
fields_present: true
types_valid: true
ranges_checked: true
cross_refs_verified: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | upstream | 0.28 |
| [[kind-builder]] | upstream | 0.24 |
| [[bld_collaboration_kind]] | downstream | 0.24 |
| [[bld_instruction_kind]] | upstream | 0.23 |
| [[p06_is_builder_nucleus]] | upstream | 0.23 |
| [[ex_env_config_default]] | related | 0.23 |
| [[p02_bc_builder_nucleus]] | upstream | 0.22 |
| [[p12_sc_builder_nucleus]] | downstream | 0.21 |
| [[agent_card_engineering_nucleus]] | upstream | 0.20 |
| [[bld_schema_kind]] | upstream | 0.20 |
