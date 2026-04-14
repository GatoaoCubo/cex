---
id: p11_qg_interface
kind: quality_gate
pillar: P11
title: "Gate: Interface"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "interface — bilateral integration contracts defining methods, I/O schemas, versioning, and compatibility between agents"
quality: 9.0
tags: [quality-gate, interface, contract, bilateral, integration, versioning, compatibility]
tldr: "Gates ensuring interface artifacts define complete bilateral contracts with typed methods, versioning strategy, backward compatibility guarantees, and mock specs."
density_score: 0.92
llm_function: GOVERN
---
# Gate: Interface
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: interface` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem | `id: agent_a_b` in file `agent_b_c.md` |
| H04 | Kind equals literal `interface` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All required fields present | Missing: methods, provider, consumer, or version |
| H07 | Every method has both `input` and `output` defined | Any method with only one side defined |
| H08 | `provider` and `consumer` are distinct identifiers | Same value in both fields |
| H09 | `version` follows semver (`^\d+\.\d+\.\d+$`) | Non-semver version string |
| H10 | At least one method defined | Empty or missing methods list |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Type precision | 1.0 | All method inputs and outputs use typed field definitions | Typed but incomplete coverage | Untyped — described in prose only |
| S02 | Backward compatibility | 1.0 | Compatibility policy stated (breaking vs non-breaking changes defined) | Policy mentioned but vague | No compatibility statement |
| S03 | Versioning strategy | 1.0 | Version bump rules documented (what triggers major/minor/patch) | Semver used but bump rules absent | No versioning guidance |
| S04 | Deprecation path | 0.5 | Deprecated methods marked + migration path to replacement provided | Deprecated methods marked, no migration | No deprecation policy |
| S05 | Error contract | 1.0 | Error responses typed per method (error codes, shapes) | Generic error response defined | No error contract |
| S06 | Mock specification | 1.0 | Mock inputs and expected outputs for at least 2 methods | One method has mock data | No mock spec |
| S07 | Bilaterality enforced | 1.0 | Both provider and consumer roles clearly scoped; no unilateral creep | Mostly bilateral with minor leakage | Reads as a unilateral input schema |
| S08 | Method naming | 0.5 | Method names use verb_noun pattern (e.g., `get_status`, `send_result`) | Names present but inconsistent | Arbitrary names |
| S09 | Timeout and SLA | 0.5 | Expected response time or SLA documented per method | Overall SLA present, not per-method | None |
| S10 | Signal distinction | 0.5 | Interface defines synchronous request-response, not fire-and-forget | Mostly clear | Indistinguishable from a signal |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to pool as golden integration contract |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Prototyping integration between two new agents where final method signatures are not yet known |
| Approver | Both provider and consumer team leads |
