---
kind: config
id: bld_config_validation_schema
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for validation_schema production
pattern: CONFIG restricts SCHEMA, never contradicts
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
# Config: validation_schema Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p06_vs_{scope}.yaml | p06_vs_knowledge_card.yaml |
| Builder dir | kebab-case | validation-schema-builder/ |
| Fields | snake_case | target_kind, on_failure, fields_count |
| Scope slugs | lowercase_underscores | knowledge_card, model_card, signal |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P06_schema/examples/p06_vs_{scope}.yaml
- Compiled: cex/P06_schema/compiled/p06_vs_{scope}.json
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Density: >= 0.80
- Fields: >= 1 (no upper limit, but 5-20 typical)
## Format Policy
- machine_format: json (the schema itself is a JSON-compatible contract)
- Target output may be json or yaml (specified in format field)
- Field types MUST be JSON Schema compatible
- Constraints use simple operators (pattern, enum, min, max, min_length, max_length)
