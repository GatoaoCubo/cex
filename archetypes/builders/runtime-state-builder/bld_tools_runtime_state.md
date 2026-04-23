---
kind: tools
id: bld_tools_runtime_state
pillar: P04
llm_function: CALL
purpose: Tools available for runtime_state production
quality: 9.0
title: "Tools Runtime State"
version: "1.0.0"
author: n03_builder
tags: [runtime_state, builder, examples]
tldr: "Golden and anti-examples for runtime state construction, demonstrating ideal structure and common pitfalls."
domain: "runtime state construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_golden_test
  - bld_tools_validation_schema
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_response_format
  - bld_tools_prompt_version
  - bld_tools_runtime_rule
  - bld_tools_path_config
  - bld_tools_unit_eval
---

# Tools: runtime-state-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing runtime_states | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions for runtime_state |
| CEX Examples | P10_memory/examples/ | Existing runtime_state artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P10_mental_model seeds (runtime_state equivalent) |
| Agent PRIMEs | records/agent_groups/{name}/PRIME_{NAME}.md | Agent identity for state derivation |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
1. [ ] YAML parses
2. [ ] id matches p10_rs_ prefix
3. [ ] persistence in [session, cross_session]
4. [ ] routing_mode in [keyword, semantic, hybrid, rule_based]
5. [ ] Decision Tree has branches

## Metadata

```yaml
id: bld_tools_runtime_state
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-runtime-state.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_golden_test]] | sibling | 0.62 |
| [[bld_tools_validation_schema]] | sibling | 0.62 |
| [[bld_tools_retriever_config]] | sibling | 0.61 |
| [[bld_tools_memory_scope]] | sibling | 0.60 |
| [[bld_tools_cli_tool]] | sibling | 0.60 |
| [[bld_tools_response_format]] | sibling | 0.59 |
| [[bld_tools_prompt_version]] | sibling | 0.59 |
| [[bld_tools_runtime_rule]] | sibling | 0.58 |
| [[bld_tools_path_config]] | sibling | 0.58 |
| [[bld_tools_unit_eval]] | sibling | 0.58 |
