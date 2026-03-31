---
kind: config
id: bld_config_golden_test
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for golden_test production
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
# Config: golden_test Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_gt_{case_slug}.md | p07_gt_kc_prompt_caching.md |
| Builder dir | kebab-case | golden-test-builder/ |
| Fields | snake_case | quality_threshold, target_kind |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P07_evals/examples/p07_gt_{case_slug}.md
- Compiled: cex/P07_evals/compiled/p07_gt_{case_slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80
- Golden output: no truncation (complete artifact required)
## Quality Threshold Policy
- quality_threshold minimum: 9.5 (non-negotiable)
- Reviewer approval required before golden status
- Producer CANNOT self-approve as reviewer
