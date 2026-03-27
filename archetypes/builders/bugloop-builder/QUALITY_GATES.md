---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for bugloop artifacts
note: this file IS an instance of what the builder's sibling quality-gate-builder produces
---

# Quality Gates: bugloop

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses without error |
| H02 | id starts with p11_bl_ |
| H03 | id == filename stem |
| H04 | kind == bugloop |
| H05 | pillar == P11 |
| H06 | quality == null |
| H07 | detect object has method, trigger, pattern |
| H08 | fix.max_attempts is integer 1-10 |
| H09 | cycle_count >= fix.max_attempts |
| H10 | escalation.threshold <= cycle_count |
| H11 | confidence is float 0.0-1.0 |
| H12 | auto_fix (root) == fix.auto_fix |
| H13 | verify.assertions list is non-empty |
| H14 | rollback object has enabled + strategy |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items including "bugloop" | 0.5 |
| S03 | detect.pattern is a concrete regex or signature | 1.0 |
| S04 | verify.timeout > 0 | 1.0 |
| S05 | All 5 body sections present | 1.0 |
| S06 | confidence calibrated (>= 0.7 for auto_fix=true) | 1.5 |
| S07 | escalation.target is a named system or role | 0.5 |
| S08 | density >= 0.80 | 1.0 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0

## Invariants
- If auto_fix == true AND confidence < 0.7: HARD fail (unsafe auto-fix)
- If rollback.enabled == false AND fix.strategy == rollback_first: HARD fail (contradiction)
- If escalation.threshold > cycle_count: HARD fail (escalation unreachable)
