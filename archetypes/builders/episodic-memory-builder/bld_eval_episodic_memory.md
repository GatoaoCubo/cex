---
kind: quality_gate
id: p10_qg_episodic_memory
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of episodic_memory artifacts
quality: 8.8
title: "Gate: episodic_memory"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, episodic-memory, P10, long-term]
tldr: "Pass/fail gate for episodic_memory: episode_schema with timestamp, retrieval_method, episode_count, decay_policy, owner."
domain: "episodic_memory -- long-term temporally-indexed past interaction store"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_examples_validator
  - p11_qg_chunk_strategy
  - bld_examples_validation_schema
  - p11_qg_memory_scope
  - p11_qg_retriever_config
  - p11_qg_constraint_spec
  - bld_examples_axiom
  - bld_examples_few_shot_example
  - bld_examples_cli_tool
  - p11_qg_handoff_protocol
---

## Quality Gate

# Gate: episodic_memory

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | ID matches `^p10_ep_[a-z][a-z0-9_]+$` | Hyphens, uppercase, or missing prefix |
| H03 | ID equals filename stem | id vs filename mismatch |
| H04 | Kind equals literal `episodic_memory` | `kind: memory` or other |
| H05 | Quality field is null | Non-null value |
| H06 | episode_schema has >= 3 fields | Too few fields |
| H07 | episode_schema includes timestamp field | Missing temporal index |
| H08 | retrieval_method is declared enum value | Missing or invalid |
| H09 | episode_count is numeric integer | Missing or "unlimited" |
| H10 | decay_policy declared with method | Missing or empty |

## SOFT Scoring
| Dimension | Weight | Criteria |
|---|---|---|
| Episode schema completeness | 1.5 | context, task, outcome, retrieval_keys all present |
| Retrieval configuration | 1.5 | retrieval_keys and index_method declared |
| Decay policy detail | 1.0 | Rate/threshold numeric value, not just method name |
| Episode count calibration | 1.0 | Count appropriate for agent complexity |
| Promotion sources | 0.5 | working_memory promotion path declared |
| Boundary clarity | 1.0 | Not entity_memory (no entity_type), not working_memory (no task_id) |
| Owner declaration | 0.5 | nucleus/agent binding declared |
| tldr quality | 0.5 | <= 160 chars, includes owner and episode_count |

## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Reference episodic store spec |
| >= 8.0 | Publish | Deploy for agent integration |
| >= 7.0 | Review | Add decay details or retrieval keys |
| < 7.0 | Reject | Return with gate failures |

## Examples

# Examples: episodic-memory-builder

## Golden Example
INPUT: "Create episodic memory store for N07 orchestration sessions"
OUTPUT:
```yaml
id: p10_ep_n07_orchestration
kind: episodic_memory
pillar: P10
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
owner: "n07"
episode_schema:
  timestamp: "datetime"
  context: "string"
  mission: "string"
  nuclei_dispatched: "list[string]"
  outcome: "string"
  quality_scores: "list[float]"
  retrieval_keys: "list[string]"
  confidence: "float"
retrieval_method: hybrid
episode_count: 200
decay_policy:
  method: time
  rate: "90 days -- orchestration context stays relevant for 3 months"
retrieval_keys: [mission_name, nucleus, kind, outcome]
index_method: hybrid
promotion_sources: [p10_wm_n07_mission_runner]
quality: null
tags: [episodic_memory, n07, orchestration, P10]
tldr: "N07 orchestration episodic store: 200 episodes, 90-day decay, hybrid retrieval by mission/nucleus/kind."
description: "Episodic store for N07 mission orchestration sessions -- enables recall of past dispatch patterns."
```

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches `^p10_ep_` (H02 pass)
- episode_schema has timestamp + 7 fields (H06 pass)
- retrieval_method: hybrid (H07 pass)
- episode_count: 200 (H08 pass)
- decay_policy declared (H09 pass)
- owner: n07 (H10 pass)

## Anti-Example
BAD OUTPUT:
```yaml
id: n07-history
kind: history
owner: n07
episodes: unlimited
decay: none
quality: 8.0
```
FAILURES:
1. id: "n07-history" has hyphen, no `p10_ep_` prefix -> H02 FAIL
2. kind: "history" not "episodic_memory" -> H04 FAIL
3. quality: 8.0 (not null) -> H05 FAIL
4. episode_schema missing entirely -> H06 FAIL
5. episodes: unlimited -- no count limit -> H08 FAIL
6. decay: none -- no policy -> H09 FAIL
7. Missing retrieval_method, tags, tldr, version, pillar -> H multiple FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
