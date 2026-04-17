---
kind: schema
id: bld_schema_procedural_memory
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for procedural_memory
quality: 9.2
title: "Schema: procedural_memory"
version: "2.0.0"
author: n06_commercial
tags: [procedural_memory, builder, schema]
tldr: "Schema for LLM agent procedural memory artifacts: skill definitions, namespace, format, storage backend, verification strategy, tier matrix"
domain: "LLM agent procedural memory"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

## Frontmatter Fields

### Required

| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | null | Must match `^p10_pm_[a-z][a-z0-9_]+$` |
| kind | string | yes | "procedural_memory" | Fixed value |
| pillar | string | yes | "P10" | Fixed value |
| title | string | yes | null | Descriptive name for the skill library/store |
| version | string | yes | "1.0.0" | Semver |
| created | string | yes | null | ISO 8601 date |
| updated | string | yes | null | ISO 8601 date |
| author | string | yes | null | Nucleus or person responsible |
| domain | string | yes | null | Agent domain (e.g., "coding-assistant") |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Keywords including skill domain and tier |
| tldr | string | yes | null | One-sentence summary |
| tier | string | yes | null | free, pro, enterprise |
| skill_format | string | yes | null | code, yaml, natural_language, json, mixed |
| skill_count | integer | no | null | Number of skills defined (0 for free tier) |

### Recommended

| Field | Type | Notes |
|---|---|---|
| verification | string | How skills are validated: test_case, unit_test, human_review, none |
| namespace_pattern | string | Key hierarchy pattern (e.g., "domain.task.subtask") |
| storage_backend | string | Backend: redis, postgresql, filesystem, in_memory |
| reflexion_enabled | boolean | Whether Reflexion self-notes are stored alongside skills |

## ID Pattern

```
^p10_pm_[a-z][a-z0-9_]+$
```

Example IDs:
- `p10_pm_coding_assistant_pro`
- `p10_pm_research_agent_enterprise`
- `p10_pm_empty_free_tier`

## Body Structure

1. **Overview** -- agent type, tier, what skill domain is covered, reference system
2. **Skill Definitions** -- table: Skill ID | Name | Format | Storage Key | Verification | Tier
3. **Skill Namespace** -- hierarchy pattern, key examples, lookup method
4. **Storage Backend** -- backend config, encoding, retrieval latency target
5. **Verification Strategy** -- test-case gating, CI pipeline, human review, or none + why
6. **Reflexion Notes** (optional) -- how failure self-notes are stored and retrieved
7. **Commercial Tier Matrix** -- FREE/PRO/ENTERPRISE capability comparison

## Constraints

- `skill_format` must be one of: code, yaml, natural_language, json, mixed.
- `tier: free` artifacts MUST have `skill_count: 0` and state "no procedural memory" in Overview.
- `tier: enterprise` artifacts MUST include skill versioning, rollback, and access control.
- Body MUST include Commercial Tier Matrix.
- quality MUST be null (never self-assign a score).
- No robotics or cognitive neuroscience terminology (motor schemas, basal ganglia, ACT-R).
