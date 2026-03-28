---
kind: schema
id: bld_schema_validator_builder_codex
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for validator - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
---

# Schema: validator

## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P06` |
| Kind | literal `validator` |
| Layer | `governance` |
| Machine format | `yaml` |
| Naming | `p06_val_{rule}.yaml` |
| Max bytes | `3072` |

## Required Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string, regex `^p06_val_[a-z][a-z0-9_]+$` | YES | - | must equal filename stem |
| kind | literal `validator` | YES | - | type integrity |
| pillar | literal `P06` | YES | - | pillar assignment |
| version | semver string | YES | `1.0.0` | artifact version |
| created | date `YYYY-MM-DD` | YES | - | creation date |
| updated | date `YYYY-MM-DD` | YES | - | last update |
| author | string | YES | - | producer identity |
| title | string | YES | - | human label of the rule |
| trigger | enum `pre_commit|post_generate|pre_pool|on_signal` | YES | - | when it runs |
| severity | enum `block|warn|info` | YES | - | failure impact |
| quality | null | YES | null | never self-score |
| tags | list[string], len >= 3 | YES | - | searchability |
| tldr | string, <= 160 chars | YES | - | dense summary |

## Recommended Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| threshold | number or null | REC | null | numeric boundary when applicable |
| target | string | REC | omitted | file glob or field path |
| action_on_fail | enum `reject|warn|log` | REC | `reject` | runtime handling |
| density_score | number, `0.80-1.00` | REC | omitted | density target |
| linked_artifacts | object `{source, related}` | REC | omitted | provenance and neighbors |

## Rule Object
```yaml
condition: string
```
Rule: `condition` MUST be deterministic and machine-checkable.

## Body Structure
1. `## Rule` - canonical target, condition, threshold, action
2. `## Checks` - concrete sub-checks with expressions and failure action
3. `## Error Messages` - failure text plus fix hints
4. `## Pass Example` - realistic passing input
5. `## Fail Example` - realistic failing input with resulting message

## Boundary Rules
`validator` IS:
- post-generation validation logic
- technical policy with explicit failure semantics
- reusable across hooks, pipelines, and artifact families

`validator` IS NOT:
- `quality_gate` with weighted scores and publish thresholds
- `scoring_rubric` with subjective dimensions
- `grammar` that constrains decoder tokens during generation

## Constraints
- max_bytes: `3072`
- naming: `p06_val_{rule}.yaml`
- id == filename stem
- compiled YAML must preserve all frontmatter fields
- at least 3 checks must be listed
- examples must include one PASS and one FAIL
- no subjective language such as "good enough" or "high quality"
