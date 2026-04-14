---
id: p11_qg_guardrail
kind: quality_gate
pillar: P11
title: "Gate: guardrail"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "guardrail — safety boundaries and enforcement policies applied to agents and artifacts"
quality: 9.0
tags: [quality-gate, guardrail, safety, enforcement, security-boundary, P11]
tldr: "Validates guardrail artifacts: enforcement mode specificity, concrete violation examples, severity classification, and bypass policy."
density_score: 0.94
llm_function: GOVERN
---
# Gate: guardrail
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: guardrail` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p11_gr_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `guardrail` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, severity, scope, enforcement, domain, quality, tags, tldr | Any missing field |
| H07 | `severity` is one of: `critical`, `high`, `medium`, `low` | Unlisted value; drives escalation routing |
| H08 | `enforcement` is one of: `block`, `warn`, `log` | Unlisted value; missing causes system no-op |
| H09 | `scope` defines where this guardrail applies (agent, artifact, pipeline, or all) | Scope absent; guardrail cannot be targeted |
| H10 | Rules section has >= 3 concrete, measurable restrictions | Fewer than 3 or rules are subjective |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names protected boundary and enforcement mode | 0.09 | Named=1.0, vague=0.3 |
| S02 | Tags list len >= 3, includes severity level keyword | 0.05 | Met=1.0, partial=0.5 |
| S03 | Violations section has >= 2 specific, concrete examples | 0.13 | 2+=1.0, 1=0.5, 0=0.0 |
| S04 | Enforcement action describes exact system response (not just "block") | 0.12 | Precise=1.0, generic "block"=0.3 |
| S05 | Detection method specified (pattern match, LLM judge, static rule, regex) | 0.11 | Specified=1.0, absent=0.0 |
| S06 | Severity classification justified with written rationale | 0.09 | Justified=1.0, bare label=0.2 |
| S07 | Bypass policy defined: who can override and under what conditions | 0.10 | Explicit=1.0, absent=0.0 |
| S08 | Audit trail requirement documented for violations | 0.09 | Documented=1.0, absent=0.0 |
| S09 | False-positive risk assessed with mitigation strategy | 0.09 | Assessed+mitigated=1.0, absent=0.0 |
| S10 | Boundary from `permission`, `law`, and `quality_gate` stated | 0.08 | All 3=1.0, 2=0.6, 1=0.3, 0=0.0 |
| S11 | No subjective language in rules ("be careful", "apownte", "reasonable") | 0.05 | Clean=1.0, subjective language found=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for guardrail calibration |
| >= 8.0 | PUBLISH — pool-eligible; enforcement, detection, and bypass documented |
| >= 7.0 | REVIEW — usable but detection method or false-positive risk missing |
| < 7.0  | REJECT — redo; likely no concrete violation examples or missing enforcement spec |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Severity is `low` or `medium` only AND guardrail blocks a critical production hotfix path |
| approver | Security lead; written sign-off required before bypass activates |
| audit trail | Required: security lead name, incident ID, timestamp, expected re-enable date |
