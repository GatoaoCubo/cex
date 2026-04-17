---
id: bld_qg_domain_event
kind: quality_gate
pillar: P11
llm_function: GOVERN
version: 1.0.0
quality: null
tags: [domain_event, quality-gate, ddd]
title: "Quality Gate: domain_event"
---
# Quality Gate: domain_event
## HARD Gates (all must pass)
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | id matches `^de_[a-z][a-z0-9_]+$` | Wrong prefix or format |
| H03 | kind == "domain_event" | Wrong kind value |
| H04 | quality == null | Any non-null value |
| H05 | aggregate_root present and non-empty | Missing field |
| H06 | bounded_context present and non-empty | Missing field |
| H07 | occurred_at present and ISO-8601 format | Missing or wrong format |
| H08 | payload section present in body with >= 1 field | Empty or missing payload |
| H09 | Event title/name is past tense | Present or imperative tense |
| H10 | Total file size <= 3072 bytes | Exceeds max_bytes |

## SOFT Scoring
| ID | Dimension | Weight | 10pts | 5pts | 0pts |
|----|-----------|--------|-------|------|------|
| S01 | Causal chain (causation_id + correlation_id) | 1.0 | Both present | One present | Neither |
| S02 | Payload typed and documented | 1.0 | All fields typed | Partial | No types |
| S03 | Consumers documented | 0.8 | >= 1 consumer with reaction | Present, no detail | Absent |
| S04 | Business invariants stated | 0.8 | >= 1 invariant | Vague | Absent |
| S05 | Tags cover aggregate + context | 0.6 | >= 3 distinct tags | 2 tags | < 2 |

## Score Tiers
| Score | Action |
|-------|--------|
| >= 9.0 | Publish to bounded context event catalog |
| >= 7.0 | Use in workflows; flag for invariant improvement |
| < 7.0 | Return: add payload types, consumers, causal chain |
