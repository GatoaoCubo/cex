---
id: p11_qg_decision_record
kind: quality_gate
pillar: P11
title: "Gate: decision_record"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "architecture decision record — single significant choice documented with context, options, rationale, and consequences"
quality: 9.0
tags: [quality-gate, decision-record, P08, ADR, architecture, status-lifecycle]
tldr: "Pass/fail gate for decision_record artifacts: context completeness, options coverage, consequence honesty, and status lifecycle integrity."
density_score: 0.90
llm_function: GOVERN
---
# Gate: decision_record
## Definition
| Field | Value |
|---|---|
| metric | decision_record artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: decision_record` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | ID matches `^p08_adr_[a-z][a-z0-9_]+$` | Uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | ID/filename mismatch |
| H04 | Kind equals literal `decision_record` | Any other value |
| H05 | Quality field is null | Any non-null value |
| H06 | Required fields present: id, title, status, context, decision | Any missing or empty |
| H07 | Status is one of: proposed, accepted, deprecated, superseded | Unrecognized value |
| H08 | Body contains all 4 required sections | Missing Context, Options, Decision, or Consequences |
| H09 | At least 2 options in ## Options Considered | Only 1 or empty |
| H10 | If status == superseded: superseded_by populated | superseded_by null or absent |
## SOFT Scoring
| Dimension | Weight | Criteria |
|---|---|---|
| Context quality | 1.5 | Forces and constraints clear; reader understands why a decision was needed |
| Options completeness | 1.5 | Each option has name, description, pros, cons |
| Decision clarity | 1.5 | Chosen option stated first; rationale references options |
| Consequence honesty | 1.5 | >= 1 negative consequence; consequences are specific |
| Status accuracy | 1.0 | Status matches actual state; supersession links traversable |
| Tradeoff specificity | 1.0 | Concrete effects named, not vague claims |
| Options count | 0.5 | 3+ signals thorough evaluation; 2 is minimum |
| Deciders documented | 0.5 | deciders field populated |
| Related ADRs linked | 0.5 | related_to populated where dependencies exist |
| Boundary clarity | 1.0 | Explicitly not a law, not a pattern, not a diagram |
| Domain specificity | 1.0 | Context/decision/consequences specific to declared domain |
| Future guidance | 0.5 | Consequences give signal to decide whether to revisit |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference ADR |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Provisional ADR under time pressure; full review within 7 days |
| approver | Author self-certification with expiry date in frontmatter comment |
| expiry | 7d — must reach >= 7.0 or be deprecated |
| never_bypass | H01 (breaks tooling), H05 (corrupts metrics), H07 (breaks lifecycle tooling) |
