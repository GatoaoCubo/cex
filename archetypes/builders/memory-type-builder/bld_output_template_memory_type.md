---
kind: output_template
id: bld_output_template_memory_type
pillar: P05
llm_function: PRODUCE
---

# Output Template: memory_type

## Required Frontmatter

| Field | Format | Example |
|-------|--------|---------|
| id | p10_mt_{type} | p10_mt_correction |
| kind | literal | memory_type |
| pillar | literal | P10 |
| version | semver | 1.0.0 |
| created | YYYY-MM-DD | 2026-04-05 |
| updated | YYYY-MM-DD | 2026-04-05 |
| author | string | n07-orchestrator |
| type_name | enum | correction, preference, convention, context |
| decay_rate | float | 0.00, 0.01, 0.02, 0.05 |
| preserve_on_compact | bool | true, false |
| quality | null | null (never self-score) |
| tags | list | [memory_type, p10, {type}] |
| tldr | string<=160 | one-line description |

## Required Body Sections

| Section | Content | Min Length |
|---------|---------|-----------|
| Definition | What observations belong to this type, classification criteria | 2 sentences |
| Decay Policy | Formula, rationale, when pruned | 1 paragraph |
| Storage Rules | Location, naming, update-vs-append, compaction behavior | 3 bullet points |
| Examples | Concrete observations that ARE this type | 3 items |
| Anti-Examples | Observations that SEEM like this type but are NOT, with explanation | 2 items |

## Constraints

- Total body <= 2048 bytes
- One artifact per type (max 4 artifacts in entire system)
- decay_rate must match type: correction=0.00, preference=0.01, convention=0.02, context=0.05
