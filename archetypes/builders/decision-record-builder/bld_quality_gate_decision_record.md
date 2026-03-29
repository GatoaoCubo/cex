---
id: p11_qg_decision_record
kind: quality_gate
pillar: P11
title: "Gate: decision_record"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "edison"
domain: "architecture decision record — single significant choice documented with context, options, rationale, and consequences"
quality: null
tags: [quality-gate, decision-record, P08, ADR, architecture, status-lifecycle]
tldr: "Pass/fail gate for decision_record artifacts: context completeness, options coverage, consequence honesty, and status lifecycle integrity."
density_score: 0.90
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
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p08_adr_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens in slug, or missing prefix |
| H03 | ID equals filename stem | `id: p08_adr_foo` but file is `p08_adr_bar.md` |
| H04 | Kind equals literal `decision_record` | `kind: adr` or `kind: record` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | Required fields present: id, title, status, context, decision | Any of these five fields missing or empty |
| H07 | Status is one of: proposed, accepted, deprecated, superseded | `status: active` or unrecognized value |
| H08 | Body contains all 4 required sections | Missing ## Context, ## Options Considered, ## Decision, or ## Consequences |
| H09 | At least 2 options documented in ## Options Considered | Only 1 option or section is empty |
| H10 | If status == superseded: superseded_by field is populated | Status is superseded but superseded_by is null or absent |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Context quality | 1.5 | Context clearly explains the forces and constraints; reader understands why a decision was needed without prior knowledge |
| Options completeness | 1.5 | Each option has name, description, pros, and cons; no option is listed without evaluation |
| Decision clarity | 1.5 | Decision section states the chosen option in the first sentence; rationale is explicit and references the options |
| Consequence honesty | 1.5 | At least one negative consequence documented; consequences are specific (not generic "adds complexity") |
| Status accuracy | 1.0 | Status matches actual state; supersession links are bidirectional and traversable |
| Tradeoff specificity | 1.0 | Tradeoffs name concrete effects (e.g., "increases cold start time by ~200ms") not vague claims |
| Options count | 0.5 | 3+ options considered signals thorough evaluation; 2 is minimum, 1 is a hard fail |
| Deciders documented | 0.5 | deciders field populated so accountability is traceable |
| Related ADRs linked | 0.5 | related_to populated where architectural dependencies exist |
| Boundary clarity | 1.0 | Explicitly not a law (inviolable), not a pattern (reusable), not a diagram — single decision record |
| Domain specificity | 1.0 | Context, decision, and consequences are specific to the declared domain problem — not generic boilerplate |
| Future guidance | 0.5 | Consequences section gives future engineers enough signal to decide whether to revisit this ADR |
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
| conditions | Provisional ADR created under time pressure; author commits to full review within 7 days |
| approver | Author self-certification with expiry date comment in frontmatter |
| audit_trail | Bypass note with expiry date in frontmatter comment |
| expiry | 7d — provisional ADRs must reach >= 7.0 or be deprecated |
| never_bypass | H01 (unparseable YAML breaks tooling), H05 (self-scored gates corrupt quality metrics), H07 (invalid status breaks lifecycle tooling) |
