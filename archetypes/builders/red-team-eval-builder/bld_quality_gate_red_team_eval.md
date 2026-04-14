---
id: p11_qg_red_team_eval
kind: quality_gate
pillar: P11
title: "Gate: red_team_eval"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "adversarial LLM safety evaluation — pre-deployment attack scenario configurations with declared attack_types, specific target, and measurable pass_criteria"
quality: 9.1
tags: [quality-gate, red-team-eval, P07, adversarial, safety, llm-security, owasp]
tldr: "Pass/fail gate for red_team_eval artifacts: attack coverage, target specificity, pass_criteria observability, payload safety, and OWASP traceability."
density_score: 0.90
llm_function: GOVERN
---
# Gate: red_team_eval
## Definition
| Field | Value |
|---|---|
| metric | red_team_eval artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: red_team_eval` |

## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p07_rt_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, hyphens, or missing prefix |
| H03 | ID equals filename stem | `id: p07_rt_foo` but file is `p07_rt_bar.md` |
| H04 | Kind equals literal `red_team_eval` | Any other value |
| H05 | Quality field is null | Any non-null value |
| H06 | All required fields present | Missing `attack_types`, `target`, or `pass_criteria` |
| H07 | attack_types is non-empty list | `attack_types: []` or absent |
| H08 | All attack_type values from approved enum | Non-enum value present |
| H09 | target is specific (not generic) | `target: "the model"` or `target: "the system"` |
| H10 | pass_criteria is observable and measurable | `pass_criteria: "be safe"` |
| H11 | No real PII or working exploit payloads in body | Actual SSNs, emails, or real jailbreak strings present |
| H12 | Body has all 4 required sections | Missing ## Overview, ## Attack Scenarios, ## Pass Criteria, or ## Configuration |

## SOFT Scoring
| Dimension | Weight | Criteria |
|---|---|---|
| Attack type coverage | 1.5 | >= 3 attack_types covering distinct threat vectors; not all from same OWASP category |
| Pass criteria specificity | 1.5 | Each criterion maps to observable model output; automated evaluation is feasible |
| OWASP traceability | 1.0 | Every attack_type has at least one LLM01-LLM10 reference |
| Framework completeness | 1.0 | Framework declared with run command and expected output format |
| Scenario detail | 1.0 | Each attack scenario has placeholder pattern + expected response + OWASP ref |
| Boundary clarity | 1.0 | Explicitly not a guardrail, e2e_eval, unit_eval — adversarial pre-deploy purpose stated |
| Payload safety | 1.0 | Placeholder notation used consistently; no real exploits or PII in spec body |
| Domain specificity | 1.0 | Attack scenarios specific to declared target domain, not generic boilerplate |
| Testability | 1.0 | Each scenario testsble with declared framework; expected output described |
| Severity classification | 0.5 | Severity declared; justification implied by attack types chosen |
| Test count declaration | 0.5 | test_count field present and >= 1 |
| Env var documentation | 0.5 | Environment variables listed with purpose |

## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Bypass
Conditions: exploratory red team spike mapping unknown attack surface only.
Approver: security lead self-certification with exploratory scope comment.
Audit: bypass note in frontmatter comment with expiry date.
Expiry: 7d — promote to >= 7.0 or remove.
Never bypass: H01 (unparseable YAML breaks tooling), H05 (self-scored gates corrupt metrics), H11 (real PII/exploits is a non-negotiable safety violation).
