---
kind: quality_gate
id: p10_qg_prospective_memory
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of prospective_memory artifacts
quality: 8.7
title: "Gate: prospective_memory"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, prospective-memory, P10, future-actions]
tldr: "Gate for prospective_memory: owner, reminders array, trigger_type, action_payload, execution_mechanism."
domain: "prospective_memory -- agent store of future intentions and reminders"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - p11_qg_schedule
  - p11_qg_chunk_strategy
  - p11_qg_constraint_spec
  - p11_qg_quality_gate
  - p11_qg_creation_artifacts
  - p11_qg_memory_scope
  - p11_qg_retriever_config
  - p11_qg_function_def
  - p11_qg_handoff_protocol
  - bld_knowledge_card_quality_gate
---

## Quality Gate

# Gate: prospective_memory

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | ID matches `^p10_pm_[a-z][a-z0-9_]+$` | Wrong format |
| H03 | ID equals filename stem | Mismatch |
| H04 | Kind equals literal `prospective_memory` | Wrong kind |
| H05 | Quality field is null | Non-null value |
| H06 | owner declared and non-empty | Missing owner |
| H07 | reminders array has >= 1 entry | Empty or missing |
| H08 | Each reminder has trigger_type | Missing trigger_type |
| H09 | Each reminder has action_payload | Missing or vague ("something") |
| H10 | execution_mechanism declared | Missing |

## SOFT Scoring
| Dimension | Weight | Criteria |
|---|---|---|
| Action payload executability | 2.0 | Self-contained instructions without external context |
| Trigger specificity | 1.5 | Concrete trigger values (datetime, signal name, condition expression) |
| Priority ordering | 0.5 | Priority integers declared for multi-reminder stores |
| Expiry appropriateness | 0.5 | Time-sensitive reminders have expiry; recurring have null |
| Completion policy | 0.5 | mark_done vs re_schedule matches reminder nature |
| Boundary clarity | 1.0 | Not schedule (no cron workflow config), not session_state |
| tldr quality | 0.5 | Includes owner and reminder count/types |

## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Reference prospective memory spec |
| >= 8.0 | Publish | Deploy for agent integration |
| >= 7.0 | Review | Improve action_payload or trigger values |
| < 7.0 | Reject | Return with failures |

## Examples

# Examples: prospective-memory-builder

## Golden Example
INPUT: "Create prospective memory for N07 with weekly quality check and N01 dispatch on low score"
```yaml
id: p10_pm_n07_quality_ops
kind: prospective_memory
pillar: P10
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
owner: "n07"
execution_mechanism: polling
completion_policy: re_schedule
reminders:
  - id: "weekly_quality_audit"
    trigger_type: time
    trigger_value: "every Monday 09:00 UTC"
    action_payload: "Run cex_doctor.py --full and compile quality report to N07_admin/P11_feedback/"
    priority: 2
    expiry: null
    completion_policy: re_schedule
    recurrence: "0 9 * * 1"
  - id: "low_quality_dispatch"
    trigger_type: condition
    trigger_value: "average quality_score < 7.5 in last 7 days"
    action_payload: "Dispatch N01 to audit and improve lowest-scoring artifacts"
    priority: 1
    expiry: null
    completion_policy: mark_done
    recurrence: null
quality: null
tags: [prospective_memory, n07, quality_ops, P10]
tldr: "N07 quality ops prospective memory: weekly audit (time trigger) + N01 dispatch on low score (condition trigger)."
```

WHY THIS IS GOLDEN: owner declared, reminders array >= 1, trigger_type per reminder, action_payload specific, priority set, quality null, execution_mechanism declared.

## Anti-Example
```yaml
id: n07-reminders
kind: schedule
reminders:
  - do: something later
quality: 8.0
```
FAILURES: hyphened id, wrong kind (schedule != prospective_memory), quality non-null, vague action_payload, missing owner, trigger_type, expiry, tags.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
