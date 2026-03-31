---
kind: config
id: bld_config_response_format
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for response_format production
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
# Config: response_format Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p05_rf_{format_slug}.yaml | p05_rf_knowledge_card.yaml |
| Builder dir | kebab-case | response-format-builder/ |
| Fields | snake_case | format_type, injection_point, sections_count |
| Format slugs | lowercase_underscores | knowledge_card, model_card, signal_json |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P05_output/examples/p05_rf_{format_slug}.yaml
- Compiled: cex/P05_output/compiled/p05_rf_{format_slug}.json
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80
- Sections: >= 1 (recommend 3-7; LLMs struggle above 10)
## Format Policy
- format_type determines output structure the LLM follows
- json: highest compliance rate, best for machine consumption
- yaml: good for config-like output with frontmatter
- markdown: best for human-readable docs, supports headers/tables
- csv: tabular data only, simple extraction
- plaintext: unstructured, use only when no structure needed
