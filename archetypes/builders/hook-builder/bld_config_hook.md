---
kind: config
id: bld_config_hook
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
title: "Config Hook"
version: "1.0.0"
author: n03_builder
tags: [hook, builder, examples]
tldr: "Golden and anti-examples for hook construction, demonstrating ideal structure and common pitfalls."
domain: "hook construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_hook_config
  - bld_schema_hook
  - bld_output_template_hook
  - bld_config_prompt_version
  - bld_examples_hook
  - bld_config_memory_scope
  - bld_config_retriever_config
  - bld_config_output_validator
  - bld_config_handoff_protocol
  - bld_config_constraint_spec
---
# Config: hook Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_hook_{slug}.md` | `p04_hook_post_tool_metrics.md` |
| Builder directory | kebab-case | `hook-builder/` |
| Frontmatter fields | snake_case | `trigger_event`, `script_path` |
| Hook slug | snake_case, lowercase | `post_tool_metrics`, `session_start_context` |
| Script files | snake_case with extension | `tool_metrics.sh`, `context_inject.py` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P04_tools/examples/p04_hook_{slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_hook_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2500 bytes
- Density: >= 0.80
## Trigger Event Guide
| Value | When it fires | Typical use |
|-------|---------------|-------------|
| pre_tool_use | Before a tool executes | Permission check, input validation |
| post_tool_use | After a tool complete | Metrics, logging, context update |
| session_start | When session begins | Context loading, env setup |
| session_end | When session ends | Cleanup, state persistence |
| user_prompt_submit | When user sends prompt | Input preprocessing, routing hints |
| stop | When agent stops | Signal emission, summary |
| subagent_stop | When subagent complete | Result collection, cleanup |
| pre_compact | Before context compaction | State preservation |
| permission_request | When permission is requested | Auto-approve, audit |
| notification | When notification is sent | Forwarding, aggregation |
| costm | Custom event | Domain-specific triggers |
## Blocking vs Async Guide
| Blocking | Async | Timeout | Use case |
|----------|-------|---------|----------|
| true | false | <= 10000 | Permission checks, input validation |
| false | true | <= 30000 | Metrics, logging, notifications |
| false | false | <= 5000 | Quick side effects |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_hook_config]] | sibling | 0.33 |
| [[bld_schema_hook]] | upstream | 0.33 |
| [[bld_output_template_hook]] | upstream | 0.32 |
| [[bld_config_prompt_version]] | sibling | 0.31 |
| [[bld_examples_hook]] | upstream | 0.31 |
| [[bld_config_memory_scope]] | sibling | 0.31 |
| [[bld_config_retriever_config]] | sibling | 0.30 |
| [[bld_config_output_validator]] | sibling | 0.29 |
| [[bld_config_handoff_protocol]] | sibling | 0.28 |
| [[bld_config_constraint_spec]] | sibling | 0.28 |
