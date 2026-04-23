---
kind: schema
id: bld_schema_learning_record
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for learning_record — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
source: P10_memory/_schema.yaml v4.0 + SEED_BANK.yaml + TAXONOMY_LAYERS.yaml + real builder data
quality: 9.1
title: "Schema Learning Record"
version: "1.0.0"
author: n03_builder
tags: [learning_record, builder, examples]
tldr: "Golden and anti-examples for learning record construction, demonstrating ideal structure and common pitfalls."
domain: "learning record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_agent_card
  - bld_schema_axiom
  - bld_schema_handoff_protocol
  - bld_schema_knowledge_card
  - bld_schema_memory_scope
  - bld_schema_output_validator
  - bld_schema_prompt_version
  - bld_schema_unit_eval
  - bld_schema_smoke_eval
---

# Schema: learning_record
## Frontmatter Fields (Required — 10)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_lr_{slug}) | YES | — | H02, H03 |
| kind | literal "learning_record" | YES | — | H04 |
| pillar | literal "P10" | YES | — | H06 |
| version | semver X.Y.Z | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | — | H06 |
| updated | date YYYY-MM-DD | YES | — | H06 |
| author | string | YES | — | H06 |
| observation | string (raw facts, no judgment) | YES | — | Pipeline element 1 |
| pattern | string (reproducible rule or mechanism) | YES | — | Pipeline element 2 |
| evidence | string (metrics, before/after data) | YES | — | Pipeline element 3 |
## Frontmatter Fields (Extended — 12)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| confidence | float 0.0-1.0 | REC | Trust score per confidence scale |
| outcome | enum [SUCCESS, PARTIAL, FAILURE] | REC | Classification of result |
| domain | string | REC | Experience domain |
| tags | list[string], len >= 3 | REC | H07 |
| tldr | string <= 160 chars | REC | S01 |
| impact_score | float 0.0-10.0 | REC | Magnitude of impact |
| decay_rate | float, default 0.03 | REC | Half-life ~23 days at 0.03 |
| agent_group | string | REC | Which agent_group produced this |
| keywords | list[string] | REC | Brain search terms |
| linked_artifacts | object {primary, related} | REC | Cross-references |
| entity_ref | string | REC | Link to entity tracking file |
| semantic_links | list[object {target, relation}] | REC | Knowledge graph connections |
### Confidence Scale
| Score | Meaning | Basis |
|-------|---------|-------|
| 0.9-1.0 | Near-certain | 10+ observations, consistent |
| 0.7-0.8 | High | 5-9 observations |
| 0.5-0.6 | Moderate | 2-4 observations |
| 0.3-0.4 | Low | 1 observation |
| 0.0-0.2 | Speculative | Theoretical only |
### Semantic Link Relations
Valid `relation` values: `depends_on`, `enables`, `contradicts`, `refines`, `caused_by`.
```yaml
semantic_links:
  - {target: "p10_lr_xxx", relation: "caused_by"}
  - {target: "p01_kc_yyy", relation: "refines"}
```
## ID Pattern
Regex: `^p10_lr_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem (H02). Underscores only.
## Linked Artifacts Object
```yaml
linked_artifacts:
  primary: null            # or artifact_id
  related: [p10_lr_xxx]   # list of related ids
```
## Body Structure (7 sections)
1. `## Summary` — dense overview of the experience (2-3 sentences)
2. `## Pattern` — what worked (concrete, reproducible steps)
3. `## Anti-Pattern` — what failed or should be avoided
4. `## Context` — environment, constraints, agent_group, timing
5. `## Impact` — measurable outcomes (time saved, errors avoided)
6. `## Reproducibility` — conditions for repeating this outcome
7. `## References` — related records, artifacts, commits
## Constraints
- max_bytes: 4096 (body) — raised from 3072, real builder files reach 4059B
- density_min: 0.80
- naming: p10_lr_{topic_slug}.md
- id == filename stem
- pattern section: concrete steps, not vague advice
- anti_pattern section: specific failures, not generic warnings

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.59 |
| [[bld_schema_agent_card]] | sibling | 0.59 |
| [[bld_schema_axiom]] | sibling | 0.59 |
| [[bld_schema_handoff_protocol]] | sibling | 0.58 |
| [[bld_schema_knowledge_card]] | sibling | 0.58 |
| [[bld_schema_memory_scope]] | sibling | 0.58 |
| [[bld_schema_output_validator]] | sibling | 0.57 |
| [[bld_schema_prompt_version]] | sibling | 0.57 |
| [[bld_schema_unit_eval]] | sibling | 0.57 |
| [[bld_schema_smoke_eval]] | sibling | 0.57 |
