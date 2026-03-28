---
kind: tools
id: bld_tools_dag
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to dag production
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

## Interim Validation
Until a generic validator exists, validate manually:
- filename matches `p12_dag_{pipeline}.yaml`
- YAML parses
- required fields present
- graph is acyclic (trace all paths, no revisits)
- every edge references existing node ids
- payload fits `dag`, not `workflow` or `component_map`
