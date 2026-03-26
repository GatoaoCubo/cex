---
lp: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for knowledge_card — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
source: P01_knowledge/_schema.yaml (types.knowledge_card)
---

# Schema: knowledge_card

## Frontmatter Fields

### Required (13 fields)
| Field | Type | Required | Default | Source |
|-------|------|----------|---------|--------|
| id | string (p01_kc_{topic_slug}) | YES | - | CEX naming |
| type | literal "knowledge_card" | YES | - | CEX |
| lp | literal "P01" | YES | - | CEX |
| title | string 5-100 chars | YES | - | CEX |
| version | semver string (X.Y.Z) | YES | "1.0.0" | CEX |
| created | date YYYY-MM-DD | YES | - | CEX |
| updated | date YYYY-MM-DD | YES | - | CEX |
| author | string (not STELLA) | YES | - | CEX |
| domain | string | YES | - | CEX |
| quality | null | YES | null | CEX (never self-score) |
| tags | list[string], len >= 3 | YES | - | CEX |
| tldr | string < 160 chars | YES | - | CEX |
| when_to_use | string | YES | - | CEX |

### CEX Extensions (6 fields, recommended)
| Field | Type | Required | Source |
|-------|------|----------|--------|
| keywords | list[string], len >= 2 | REC | CEX (BM25 search) |
| long_tails | list[string], len >= 1 | REC | CEX (semantic search) |
| axioms | list[string], len >= 1 | REC | CEX (golden rules) |
| linked_artifacts | object {primary, related} | REC | CEX (graph) |
| density_score | float 0.80-1.00 | REC | CEX (quality) |
| data_source | string (URL or description) | REC | CEX (provenance) |

## linked_artifacts Object
```yaml
linked_artifacts:
  primary: p0X_type_name_or_null    # main related artifact
  related: [p0X_type_name, ...]     # other related artifacts
```

## Body Structure: domain_kc
Required sections (in order):
1. `## Quick Reference` — yaml block: topic, scope, owner, criticality
2. `## Key Concepts` — 3+ bullets, max 80 chars each
3. `## Strategy Phases` — 3+ numbered steps with outcomes
4. `## Golden Rules` — 3+ SEMPRE/NUNCA rules
5. `## Flow` — code block with visual pipeline
6. `## Comparativo` — table with Abordagem/Vantagem/Desvantagem
7. `## References` — URLs or artifact references

## Body Structure: meta_kc
Required sections (in order):
1. `## Executive Summary` — 3+ key facts as bullets
2. `## Spec Table` — table with Spec/Value/Notes
3. `## Patterns` — confirmed patterns as bullets
4. `## Anti-Patterns` — anti-patterns with consequences
5. `## Application` — numbered steps
6. `## References` — URLs or artifact references

## Constraints (from _schema.yaml)
- max_bytes: 5120 (total body, excl frontmatter)
- min_bullets: 3
- density_min: 0.80
- quality_min: 7.0 (assigned by evaluator, not self)
- each bullet max 80 chars
- sections with < 3 lines: expand or remove
- id == filename stem
- tags: list of strings (never list-in-string)
- naming: p01_kc_{topic_slug}.md
