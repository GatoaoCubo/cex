---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for runtime_state artifacts
---

# Quality Gates: runtime_state

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p10_rs_ |
| H03 | id == filename stem |
| H04 | kind == runtime_state |
| H05 | pillar == P10 |
| H06 | quality == null |
| H07 | persistence in [session, cross_session] |
| H08 | agent is non-empty string |
| H09 | routing_mode in [keyword, semantic, hybrid, rule_based] |
| H10 | update_frequency in [per_task, per_session, on_trigger] |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items | 0.5 |
| S03 | Routing Rules has >= 2 rules with conditions and confidence | 1.0 |
| S04 | Decision Tree has >= 2 branches | 1.0 |
| S05 | Priorities has >= 3 ordered items with rationale | 1.0 |
| S06 | Heuristics has >= 2 rules of thumb with confidence | 1.0 |
| S07 | State Transitions has >= 2 triggers | 0.5 |
| S08 | density >= 0.80 | 1.0 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0
