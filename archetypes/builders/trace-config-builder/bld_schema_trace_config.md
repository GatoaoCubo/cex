---
kind: schema
id: bld_schema_trace_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for trace_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: trace_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_tc_{name}) | YES | - | Namespace compliance |
| kind | literal "trace_config" | YES | - | Type integrity |
| pillar | literal "P07" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| enabled | boolean | YES | - | Master tracing switch |
| sample_rate | float 0.0-1.0 | YES | - | Fraction of requests to trace |
| export_format | enum: otlp, langsmith, console, json_file | YES | - | Trace exporter type |
| export_path | string | YES | - | Endpoint URL or filesystem path |
| capture_prompts | boolean | YES | - | Record full prompt content |
| capture_responses | boolean | YES | - | Record full response content |
| span_attributes | list[string] | YES | - | Custom span attributes |
| retention_days | integer > 0 | YES | - | Trace retention period |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "trace_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this config covers |
| scope | string | REC | - | Agent or system scope |
| environment | enum: development, staging, production, evaluation | REC | - | Target environment |
| error_classification | map[string, string] | REC | - | Error type categorization |
## ID Pattern
Regex: `^p07_tc_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Tracing Specification` — enabled, sample rate, exporter, rationale
2. `## Capture Rules` — what is captured vs excluded, privacy controls
3. `## Span Attributes` — 8F function mapping, custom attributes
4. `## Retention Policy` — hot/warm/cold tiers, days per tier, cleanup
## Constraints
- max_bytes: 4096 (body only)
- naming: p07_tc_{name}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- sample_rate MUST be 0.0-1.0
- capture_prompts and capture_responses MUST be explicit booleans (not omitted)
- retention_days MUST be positive integer
- quality: null always
- NEVER capture prompts/responses in production without explicit privacy assessment
