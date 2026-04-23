---
kind: config
id: bld_config_computer_use
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
title: "Config Computer Use"
version: "1.0.0"
author: n03_builder
tags: [computer_use, builder, examples]
tldr: "Golden and anti-examples for computer use construction, demonstrating ideal structure and common pitfalls."
domain: "computer use construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_computer_use
  - bld_examples_computer_use
  - bld_knowledge_card_computer_use
  - bld_instruction_computer_use
  - bld_output_template_computer_use
  - p03_sp_computer_use_builder
  - bld_config_browser_tool
  - p11_qg_computer_use
  - bld_config_memory_scope
  - computer-use-builder
---
# Config: computer_use Production Rules

This ISO governs computer use: screen capture, mouse, and keyboard actions taken on behalf of the agent.
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_cu_{target_slug}.md` | `p04_cu_browser_control.md` |
| Compiled files | `p04_cu_{target_slug}.yaml` | `p04_cu_browser_control.yaml` |
| Builder directory | kebab-case | `computer_use-builder/` |
| Frontmatter fields | snake_case | `actions_supported`, `screenshot_mode` |
| Target slug | snake_case, lowercase, no hyphens | `browser_control`, `desktop_linux` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_cu_{target_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_cu_{target_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4000 bytes
- Density: >= 0.80 (no filler)
## Action Enum
| Action | Parameters | Description |
|--------|-----------|-------------|
| click | x, y, button | Click at coordinates |
| double_click | x, y | Double-click at coordinates |
| type | text | Type text at cursor/focus |
| scroll | direction, amount | Scroll viewport |
| key_press | key | Press keyboard key |
| drag | x1, y1, x2, y2 | Drag from point to point |
| screenshot | (none) | Capture current screen |
## Resolution Conventions
| Target | Recommended | Notes |
|--------|-------------|-------|
| browser | 1024x768 | Standard viewport, good token/detail balance |
| desktop | 1280x800 | Common laptop resolution |
| mobile | 375x812 | iPhone viewport |
| terminal | 800x600 | Minimal resolution for text |
Rule: resolution MUST be WxH format (e.g., "1024x768").

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_computer_use]] | upstream | 0.41 |
| [[bld_examples_computer_use]] | upstream | 0.40 |
| [[bld_knowledge_card_computer_use]] | upstream | 0.40 |
| [[bld_instruction_computer_use]] | upstream | 0.38 |
| [[bld_output_template_computer_use]] | upstream | 0.37 |
| [[p03_sp_computer_use_builder]] | upstream | 0.35 |
| [[bld_config_browser_tool]] | sibling | 0.35 |
| [[p11_qg_computer_use]] | downstream | 0.34 |
| [[bld_config_memory_scope]] | sibling | 0.30 |
| [[computer-use-builder]] | upstream | 0.29 |
