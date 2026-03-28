---
kind: schema
id: bld_schema_feature_flag
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for feature_flag
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: feature_flag
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_ff_{feature_slug}) | YES | - | Namespace compliance |
| kind | literal "feature_flag" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| flag_name | string | YES | - | Human-readable flag name |
| default_state | enum: on, off | YES | off | Default state when no targeting matches |
| category | enum: release, experiment, ops, permission | YES | - | Flag category per Fowler |
| rollout_percentage | integer 0-100 | YES | 0 | Current rollout percentage |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "feature_flag" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this flag controls |
| owner | string | REC | - | Team or person responsible |
| expires | date YYYY-MM-DD | REC | - | Stale flag cleanup date |
| targeting | string | REC | - | Targeting strategy summary |
## ID Pattern
Regex: `^p09_ff_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Flag Specification` — what feature, current state, rollout %, kill switch behavior
2. `## Rollout Strategy` — how to ramp: stages, percentage, timeline, cohorts
3. `## Lifecycle` — created, test, ramp, full rollout, retire/cleanup plan
## Constraints
- max_bytes: 1536 (body only — feature_flag is compact)
- naming: p09_ff_{feature_slug}.yaml
- machine_format: json (compiled artifact)
- id == filename stem
- default_state MUST be "on" or "off" (no "maybe", "partial")
- rollout_percentage MUST be integer 0-100
- quality: null always
