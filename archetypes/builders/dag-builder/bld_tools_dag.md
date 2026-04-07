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
