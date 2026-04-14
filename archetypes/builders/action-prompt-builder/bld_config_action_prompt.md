---
kind: config
id: bld_config_action_prompt
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
quality: 9.0
title: "Config Action Prompt"
version: "1.0.0"
author: n03_builder
tags: [action_prompt, builder, examples]
tldr: "Golden and anti-examples for action prompt construction, demonstrating ideal structure and common pitfalls."
domain: "action prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: action_prompt Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_ap_{task_slug}.md` | `p03_ap_extract_product_metrics.md` |
| Builder directory | kebab-case | `action-prompt-builder/` |
| Frontmatter fields | snake_case | `input_required`, `output_expected` |
| Task slug | snake_case, lowercase | `extract_product_metrics`, `generate_report` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P03_prompt/examples/p03_ap_{task_slug}.md`
- Compiled: `cex/P03_prompt/compiled/p03_ap_{task_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total (frontmatter + body): ~4500 bytes
- Density: >= 0.80
## Action Verb Patterns
| Pattern | Example | Anti-pattern |
|---------|---------|-------------|
| Extract X from Y | Extract metrics from scrape | Metric extraction |
| Generate X for Y | Generate report for seller | Report generation |
| Validate X against Y | Validate listing against rules | Listing validation |
| Transform X into Y | Transform CSV into JSON | Data transformation |
| Analyze X to determine Y | Analyze reviews to determine sentiment | Review analysis |
## Edge Case Requirements
- Minimum 2 edge cases per action_prompt
- Each edge case: concrete scenario + expected handling
- Common categories: missing data, format variation, timeout, empty input
- Format: "`{{scenario}}` — `{{expected_handling}}`"
