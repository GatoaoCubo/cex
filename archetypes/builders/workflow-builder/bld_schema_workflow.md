---
kind: schema
id: bld_schema_workflow
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for workflow
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: workflow
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p12_wf_{name_slug}) | YES | - | Namespace compliance |
| kind | literal "workflow" | YES | - | Type integrity |
| pillar | literal "P12" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable workflow name |
| steps_count | integer | YES | - | Number of steps in body (must match) |
| execution | enum: sequential, parallel, mixed | YES | - | Step arrangement |
| agent_nodes | list[string] | REC | - | Which agent_nodes participate |
| timeout | integer | REC | - | Total workflow timeout (seconds) |
| retry_policy | enum: none, per_step, global | REC | "none" | Retry strategy |
| depends_on | list[string] | REC | [] | Prerequisite workflows/artifacts |
| signals | list[string] | REC | - | Signal kinds emitted (complete, error) |
| spawn_configs | list[string] | REC | - | Referenced spawn_config ids |
| domain | string | YES | - | Domain this workflow serves |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "workflow" |
| tldr | string <= 160ch | YES | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density |
## ID Pattern
Regex: `^p12_wf_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Purpose` — why this workflow exists, what mission it accomplishes
2. `## Steps` — numbered steps with agent, action, input, output, signal
3. `## Dependencies` — what must exist before workflow runs
4. `## Signals` — what signals are emitted and when (references signal-builder)
## Constraints
- max_bytes: 3072 (body only)
- naming: p12_wf_{name_slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- steps_count MUST match actual count of numbered steps in body
- Each step MUST define agent and action
- Steps with dependencies MUST list them explicitly
- Signals MUST references signal-builder conventions
- quality: null always
