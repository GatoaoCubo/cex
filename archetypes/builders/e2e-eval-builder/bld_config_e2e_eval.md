---
kind: config
id: bld_config_e2e_eval
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for e2e_eval production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: e2e_eval Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_e2e_{pipeline_slug}.md | p07_e2e_research_to_kc.md |
| Compiled | p07_e2e_{pipeline_slug}.yaml | p07_e2e_research_to_kc.yaml |
| Builder dir | kebab-case | e2e-eval-builder/ |
| Fields | snake_case | data_fixtures, expected_output |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P07_evals/p07_e2e_{pipeline_slug}.md
- Compiled: cex/P07_evals/compiled/p07_e2e_{pipeline_slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80
- Timeout: default 300s, max 600s for complex pipelines
## Pipeline Policy
- Minimum 2 stages per e2e_eval (otherwise use unit_eval)
- Stages must form connected flow (output_n feeds input_n+1)
- Data fixtures required for reproducibility
- Cleanup mandatory (tests must not pollute state)
