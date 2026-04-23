---
kind: tools
id: bld_tools_permission
pillar: P04
llm_function: CALL
purpose: Tools available for permission production
quality: 9.0
title: "Tools Permission"
version: "1.0.0"
author: n03_builder
tags: [permission, builder, examples]
tldr: "Golden and anti-examples for permission construction, demonstrating ideal structure and common pitfalls."
domain: "permission construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_validation_schema
  - bld_tools_golden_test
  - bld_tools_path_config
  - bld_tools_retriever_config
  - bld_tools_response_format
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_runtime_rule
  - bld_tools_unit_eval
  - bld_tools_input_schema
---

# Tools: permission-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing permissions | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions for permission |
| CEX Examples | P09_config/examples/ | Existing permission artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P09_permission seeds |
| RBAC Patterns | NIST RBAC standard | Role hierarchy best forctices |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
1. [ ] YAML parses
2. [ ] id matches p09_perm_ prefix
3. [ ] read/write/execute in [allow, deny, conditional]
4. [ ] roles is non-empty list
5. [ ] Access Matrix present with roles

## Metadata

```yaml
id: bld_tools_permission
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-permission.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_validation_schema]] | sibling | 0.64 |
| [[bld_tools_golden_test]] | sibling | 0.64 |
| [[bld_tools_path_config]] | sibling | 0.62 |
| [[bld_tools_retriever_config]] | sibling | 0.62 |
| [[bld_tools_response_format]] | sibling | 0.61 |
| [[bld_tools_memory_scope]] | sibling | 0.61 |
| [[bld_tools_cli_tool]] | sibling | 0.61 |
| [[bld_tools_runtime_rule]] | sibling | 0.61 |
| [[bld_tools_unit_eval]] | sibling | 0.60 |
| [[bld_tools_input_schema]] | sibling | 0.60 |
