---
kind: config
id: bld_config_toolkit
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
quality: 9.1
title: "Config Toolkit"
version: "1.0.0"
author: n03_builder
tags: [toolkit, builder, examples]
tldr: "Golden and anti-examples for toolkit construction, demonstrating ideal structure and common pitfalls."
domain: "toolkit construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_toolkit_builder
  - bld_knowledge_card_toolkit
  - p03_sp_toolkit_builder
  - toolkit-builder
  - bld_collaboration_toolkit
  - bld_tools_toolkit
  - bld_schema_toolkit
  - bld_memory_toolkit
  - p11_qg_toolkit
  - bld_architecture_toolkit
---
# Config: toolkit Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p04_tk_{name}.yaml` | `p04_tk_file_ops.yaml` |
| Builder directory | kebab-case | `toolkit-builder/` |
| Tool names | snake_case | `read_file`, `git_commit`, `web_search` |
| Category values | snake_case | `file_ops`, `git_ops`, `search` |
| Confirmation tiers | lowercase enum | `auto`, `confirm`, `deny` |
Rule: use `.yaml` only for this builder — toolkits are human-reviewed permission documents.
## File Paths
1. Output: `cex/P04_tools/compiled/p04_tk_{name}.yaml`
2. Human reference: `cex/P04_tools/examples/p04_tk_{name}.md`
## Size Limits
1. Preferred toolkit size: <= 2048 bytes
2. Absolute max: 4096 bytes
3. Maximum 15 tools per toolkit — split into sub-toolkits if more are needed
4. Tool descriptions should be one-line: purpose, not usage instructions
## Toolkit Restrictions
1. Required fields must appear exactly as defined in schema
2. Omit optional null/unknown fields instead of writing placeholders
3. `denied_for` is only specified per tool when specific agents are blocked
4. `requires_confirmation` must match risk level: auto for reads, confirm for writes
5. `mcp_endpoint` only present when tool maps to an MCP server
6. Category must match one of: file_ops, git_ops, search, web, system, build, analysis
## Boundary Restrictions
1. No tool implementation code (functions, classes, scripts) inside the toolkit
2. No agent identity, persona, or system prompt content
3. No workflow steps, DAGs, or sequencing logic
4. No routing tables, dispatch rules, or agent selection logic
5. No duplicate tools across toolkits — each tool lives in exactly one toolkit
## Least-Privilege Rules
1. Start with zero tools, add only what the agent demonstrably needs
2. Read operations default to auto confirmation
3. Write operations MUST require confirmation
4. Delete/destructive operations default to deny unless explicitly justified
5. Deny lists override allow lists — if a tool is denied, no allow can override
6. Review toolkit quarterly: remove tools the agent hasn't used in 90 days

## Metadata

```yaml
id: bld_config_toolkit
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-toolkit.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | toolkit construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_toolkit_builder]] | upstream | 0.65 |
| [[bld_knowledge_card_toolkit]] | upstream | 0.63 |
| [[p03_sp_toolkit_builder]] | upstream | 0.60 |
| [[toolkit-builder]] | upstream | 0.59 |
| [[bld_collaboration_toolkit]] | upstream | 0.57 |
| [[bld_tools_toolkit]] | upstream | 0.57 |
| [[bld_schema_toolkit]] | upstream | 0.55 |
| [[bld_memory_toolkit]] | downstream | 0.54 |
| [[p11_qg_toolkit]] | downstream | 0.52 |
| [[bld_architecture_toolkit]] | upstream | 0.52 |
