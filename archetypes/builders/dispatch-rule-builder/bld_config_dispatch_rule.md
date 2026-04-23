---
kind: config
id: bld_config_dispatch_rule
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
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
title: "Config Dispatch Rule"
version: "1.0.0"
author: n03_builder
tags: [dispatch_rule, builder, examples]
tldr: "Golden and anti-examples for dispatch rule construction, demonstrating ideal structure and common pitfalls."
domain: "dispatch rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_dispatch_rule
  - bld_config_signal
  - bld_schema_dispatch_rule
  - bld_tools_dispatch_rule
  - bld_config_handoff
  - dispatch-rule-builder
  - p03_sp_dispatch_rule_builder
  - bld_config_memory_scope
  - bld_examples_dispatch_rule
  - p11_qg_dispatch_rule
---
# Config: dispatch_rule Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p12_dr_{scope}.yaml` | `p12_dr_research.yaml` |
| Builder directory | kebab-case | `dispatch-rule-builder/` |
| Frontmatter fields | snake_case | `confidence_threshold`, `load_balance` |
| `id` field | `p12_dr_` prefix + snake_case scope | `p12_dr_build`, `p12_dr_marketing` |
| `agent_group` values | lowercase slug | `edison`, `shaka`, `atlas` |
| `model` values | lowercase enum | `sonnet`, `opus`, `haiku`, `flash` |
| `scope` values | lowercase slug, no spaces | `build`, `research`, `orchestration` |
| `keywords` items | lowercase, no punctuation | `build`, `code`, `implementar` |
Rule: use `.yaml` only for this builder (frontmatter yaml + md body hybrid).
## File Paths
- Output: `cex/P12_orchestration/compiled/p12_dr_{scope}.yaml`
- Human reference: `cex/P12_orchestration/examples/p12_dr_{scope}.md`
- Template: `cex/P12_orchestration/templates/tpl_dispatch_rule.md`
## Size Limits
- Preferred file size: <= 1024 bytes
- Absolute max: 3072 bytes
- Body commentary should remain concise; routing logic is frontmatter only
## Field Restrictions
- `id` MUST match `^p12_dr_[a-z][a-z0-9_]+$`
- `quality` MUST be literal `null` — never a score at authoring time
- `priority` MUST be integer 1-10 (not float, not string)
- `confidence_threshold` MUST be float 0.0-1.0 (not percentage)
- `fallback` MUST differ from `agent_group`
- `keywords` MUST be a list, even for a single keyword
- `model` MUST be one of: `sonnet`, `opus`, `haiku`, `flash`
- `routing_strategy` MUST be one of: `keyword_match`, `semantic`, `hybrid`
## Boundary Restrictions
- No task lists, scope fences, or commit instructions in the file
- No runtime status fields (`status`, `quality_score`, `timestamp`)
- No multi-step workflow graphs or dependency chains
- No hardcoded brand names, product names, or user-specific tokens in keywords
- `conditions` object must use generic keys; no runtime state references

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_dispatch_rule]] | upstream | 0.37 |
| [[bld_config_signal]] | sibling | 0.32 |
| [[bld_schema_dispatch_rule]] | upstream | 0.30 |
| [[bld_tools_dispatch_rule]] | upstream | 0.29 |
| [[bld_config_handoff]] | sibling | 0.29 |
| [[dispatch-rule-builder]] | downstream | 0.29 |
| [[p03_sp_dispatch_rule_builder]] | upstream | 0.28 |
| [[bld_config_memory_scope]] | sibling | 0.27 |
| [[bld_examples_dispatch_rule]] | upstream | 0.27 |
| [[p11_qg_dispatch_rule]] | downstream | 0.26 |
