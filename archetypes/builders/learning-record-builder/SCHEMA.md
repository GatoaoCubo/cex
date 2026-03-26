---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for learning_record — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
source: P10_memory/_schema.yaml v4.0 + SEED_BANK.yaml + TAXONOMY_LAYERS.yaml
---

# Schema: learning_record

## Frontmatter Fields (Required — 15)

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_lr_{slug}) | YES | — | H02, H03 |
| kind | literal "learning_record" | YES | — | H04 |
| pillar | literal "P10" | YES | — | H06 |
| version | semver X.Y.Z | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | — | H06 |
| updated | date YYYY-MM-DD | YES | — | H06 |
| author | string | YES | — | H06 |
| domain | string | YES | — | Experience domain |
| quality | null | YES | null | H05 — never self-score |
| tags | list[string], len >= 3 | YES | — | H07 |
| tldr | string <= 160ch | YES | — | S01 |
| topic | string | YES | — | What was learned (H08) |
| outcome | enum [SUCCESS, PARTIAL, FAILURE] | YES | — | H09 |
| score | float 0.0-10.0 | YES | — | Impact score (H10) |
| context | string | YES | — | When/where this happened |

## Frontmatter Fields (Extended — 7)

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| satellite | string | REC | Which satellite produced this |
| reproducibility | enum [HIGH, MEDIUM, LOW] | REC | Can outcome be repeated? |
| impact | string | REC | Business/system impact description |
| timestamp | ISO 8601 datetime | REC | Precise time of experience |
| dependencies | list[string] | REC | Related learning_records |
| keywords | list[string] | REC | Brain search terms |
| linked_artifacts | object {primary, related} | REC | Cross-references |

## ID Pattern
Regex: `^p10_lr_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem (H02). Underscores only.

## Linked Artifacts Object
```yaml
linked_artifacts:
  primary: null            # or artifact_id
  related: [p10_lr_xxx]   # list of related ids
```

## Body Structure (required sections)
1. `## Summary` — dense overview of the experience (2-3 sentences)
2. `## Pattern` — what worked (concrete, reproducible steps)
3. `## Anti-Pattern` — what failed or should be avoided
4. `## Context` — environment, constraints, satellite, timing
5. `## Impact` — measurable outcomes (time saved, errors avoided)
6. `## Reproducibility` — conditions for repeating this outcome
7. `## References` — related records, artifacts, commits

## Constraints
- max_bytes: 3072 (body)
- density_min: 0.80
- naming: p10_lr_{topic_slug}.md
- id == filename stem
- outcome MUST be enum value (SUCCESS, PARTIAL, FAILURE)
- score MUST be numeric 0.0-10.0 (not null, not string)
- pattern section: concrete steps, not vague advice
- anti_pattern section: specific failures, not generic warnings
