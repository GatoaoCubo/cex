---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for dag validation
pattern: HARD gates block publish, SOFT gates improve structural quality
---

# Quality Gates: dag

## HARD Gates

| Gate | Check | Why |
|------|-------|-----|
| H01 | filename matches `p12_dag_{pipeline}.yaml` | namespace compliance |
| H02 | payload parses as valid YAML | machine readability |
| H03 | all required fields present: id, kind, lp, version, created, updated, author, pipeline, nodes, edges, domain, quality, tags, tldr | completeness |
| H04 | `kind` is literal `dag` | type integrity |
| H05 | `quality` is null | never self-score |
| H06 | graph is acyclic: no circular dependencies | DAG definition |
| H07 | payload size <= 3072 bytes | schema constraint |
| H08 | no runtime fields: no `on_error`, no `timeout`, no `action`, no `runtime_state` | boundary against workflow |
| H09 | no mutable state fields: no `current_step`, no `retries` | static spec only |
| H10 | every edge `from`/`to` references an existing node id | referential integrity |

## SOFT Gates

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | node ids are lowercase slugs | 0.5 | 10 |
| S02 | `execution_order` is present and topologically valid | 1.0 | 10 |
| S03 | optional fields are omitted when unknown | 0.5 | 10 |
| S04 | node labels are short and descriptive | 0.5 | 10 |
| S05 | `node_count` matches actual nodes length | 0.5 | 10 |
| S06 | `edge_count` matches actual edges length | 0.5 | 10 |
| S07 | payload stays <= 2048 bytes when feasible | 0.5 | 10 |
| S08 | `critical_path` is present and valid | 1.0 | 10 |
| S09 | `parallel_groups` correctly identifies concurrent nodes | 1.0 | 10 |

## Scoring Formula
```text
hard_pass = all 10 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5
PUBLISH: >= 8.0
REVIEW:  >= 7.0
REJECT:  < 7.0 or any HARD fail
```

## Pre-Publish Checklist
- [ ] filename uses `p12_dag_` prefix
- [ ] required fields present
- [ ] graph is acyclic
- [ ] all edge references valid
- [ ] no workflow or runtime drift
