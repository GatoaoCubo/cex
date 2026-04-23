---
kind: tools
id: bld_tools_dag
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to dag production
quality: 9.0
title: "Tools Dag"
version: "1.0.0"
author: n03_builder
tags: [dag, builder, examples]
tldr: "Golden and anti-examples for dag construction, demonstrating ideal structure and common pitfalls."
domain: "dag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_signal
  - bld_tools_handoff
  - bld_tools_session_state
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_output_validator
  - bld_tools_path_config
  - bld_tools_prompt_version
  - bld_tools_validation_schema
---

# Tools: dag-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| `brain_query` | Search for existing DAGs and pipelines | Phase 1 | CONDITIONAL [MCP] |
| `validate_artifact.py` | Generic artifact validator | Phase 3 | [PLANNED] |
| `toposort` | Topological sort validation | Phase 3 | [PLANNED] |
## Runtime Interfaces
| Interface | Path | Use |
|-----------|------|-----|
| P12 schema | `P12_orchestration/_schema.yaml` | naming, machine format, limits |
| DAG template | `P12_orchestration/templates/tpl_dag.md` | human reference |
| Compiled output | `P12_orchestration/compiled/p12_dag_{pipeline}.yaml` | production target |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Until a generic validator exists, validate manually:
1. filename matches `p12_dag_{pipeline}.yaml`
2. YAML parses
3. required fields present
4. graph is acyclic (trace all paths, no revisits)
5. every edge references existing node ids
6. payload fits `dag`, not `workflow` or `component_map`

## Metadata

```yaml
id: bld_tools_dag
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-dag.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_signal]] | sibling | 0.56 |
| [[bld_tools_handoff]] | sibling | 0.56 |
| [[bld_tools_session_state]] | sibling | 0.53 |
| [[bld_tools_retriever_config]] | sibling | 0.51 |
| [[bld_tools_memory_scope]] | sibling | 0.51 |
| [[bld_tools_cli_tool]] | sibling | 0.50 |
| [[bld_tools_output_validator]] | sibling | 0.50 |
| [[bld_tools_path_config]] | sibling | 0.50 |
| [[bld_tools_prompt_version]] | sibling | 0.49 |
| [[bld_tools_validation_schema]] | sibling | 0.49 |
