---
kind: config
id: bld_config_input_schema
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
# Config: input_schema Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p06_is_{scope_slug}.yaml` | `p06_is_brain_query.yaml` |
| Builder directory | kebab-case | `input-schema-builder/` |
| Frontmatter fields | snake_case | `error_message`, `default` |
| Scope slugs | snake_case, lowercase | `brain_query`, `research_input` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P06_schema/examples/p06_is_{scope_slug}.yaml`
- Compiled: `cex/P06_schema/compiled/p06_is_{scope_slug}.json`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total: ~4000 bytes including frontmatter
- Density: >= 0.80
## Field Type Enum
| Type | JSON equivalent | Example |
|------|----------------|---------|
| string | string | "hello" |
| integer | number (int) | 42 |
| float | number (float) | 3.14 |
| boolean | boolean | true |
| list | array | [1, 2, 3] |
| object | object | {key: value} |
## Required vs Optional Policy
- Required fields: MUST be provided by caller, error_message SHOULD be set
- Optional fields: MUST have default value, caller can omit
- No field can be both required AND have a default (required means caller provides)
