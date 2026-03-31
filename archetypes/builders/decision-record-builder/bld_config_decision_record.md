---
kind: config
id: bld_config_decision_record
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
---
# Config: decision_record Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p08_adr_{decision_slug}.md` | `p08_adr_artifact_store_database.md` |
| Builder directory | kebab-case | `decision-record-builder/` |
| Frontmatter fields | snake_case | `superseded_by`, `date_decided`, `related_to` |
| Decision slug | snake_case, lowercase, no hyphens | `artifact_store_database`, `api_versioning_strategy` |
| Status values | lowercase enum | `proposed`, `accepted`, `deprecated`, `superseded` |
Rule: id MUST equal filename stem. Hyphens in slug = HARD FAIL.
Rule: slug must describe the decision topic, not the outcome. Prefer `artifact_store_database` over `chose_postgresql`.
## File Paths
- Output: `cex/P08_architecture/adrs/p08_adr_{decision_slug}.md`
- Compiled: `cex/P08_architecture/compiled/p08_adr_{decision_slug}.yaml`
- Index: `cex/P08_architecture/adrs/ADR_INDEX.md` (list of all ADRs with status)
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~6000 bytes
- Density: >= 0.75 (ADRs need prose — lower density floor than tool specs)
## Status Enum
| Value | Meaning | Terminal? |
|-------|---------|-----------|
| proposed | Under consideration, not yet ratified | No |
| accepted | In effect, binding for the system | No |
| deprecated | No longer valid; context changed or abandoned | Yes |
| superseded | Replaced by a newer ADR; superseded_by required | Yes |
Rule: terminal statuses (deprecated, superseded) cannot transition to proposed or accepted.
Rule: if status == superseded, superseded_by MUST be populated with a valid p08_adr_ id.
## Slug Conventions
| Decision Type | Slug Pattern | Example |
|---------------|-------------|---------|
| Technology choice | `{component}_{technology}` | `api_gateway_kong` |
| Structural pattern | `{layer}_{pattern}` | `service_layer_pattern` |
| Process rule | `{process}_{rule}` | `deployment_approval_process` |
| Migration decision | `{from}_to_{to}` | `rest_to_graphql` |
| Reject/defer | `{topic}_deferred` | `event_sourcing_deferred` |
## Context Field Guidelines
- context frontmatter field: one sentence summary (used in indexes and search)
- ## Context body section: 2-5 sentences with full force and constraint description
- NEVER state the decision in the context section — only the situation
## Consequences Field Guidelines
- consequences frontmatter field: one sentence summary of key tradeoffs
- ## Consequences body section: bulleted Positive / Negative / Neutral lists
- ALWAYS include at least one negative consequence — ADRs with only positive consequences are rejected
