---
kind: quality_gate
id: p01_qg_faq_entry
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for faq_entry
quality: 9.0
title: "Quality Gate Faq Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [faq_entry, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for faq_entry"
domain: "faq_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| support_deflection_metric | 20% | > | per entry |
| canonical answer length | <=150 words | <= | answer field |
| required field completeness | 100% | == | all frontmatter fields |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches ^p01_faq_[a-z][a-z0-9_]+.md$ | ID format mismatch |
| H03 | kind field = faq_entry | Kind field incorrect or missing |
| H04 | question field exists and is non-empty | Missing or empty question |
| H05 | answer field exists and is non-empty | Missing or empty canonical answer |
| H06 | related_topics array present and non-empty | Missing related topics list |
| H07 | support_deflection_metric is numeric | Non-numeric value or absent |
| H08 | Schema.org FAQPage snippet present in output | Missing structured data |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Question clarity (imperative verb, user language, specific) | 0.20 | All 3 criteria met = 1.0, 2 = 0.6, <2 = 0 |
| D02 | Answer completeness (resolves root cause, no follow-up needed) | 0.20 | Full resolution = 1.0, partial = 0.5, vague = 0 |
| D03 | Schema.org FAQPage compliance (correct type, acceptedAnswer) | 0.20 | Fully compliant = 1.0, partial = 0.5, absent = 0 |
| D04 | Support deflection metric present and quantified | 0.15 | Numeric with % = 1.0, present unquantified = 0.5, absent = 0 |
| D05 | Related topics coverage (>=2 valid links) | 0.15 | >=2 = 1.0, 1 = 0.5, 0 = 0 |
| D06 | Accessibility (no jargon, plain language, WCAG compliant) | 0.10 | All criteria met = 1.0, partial = 0.5 |

## Actions
| Label | Score | Action |
|-------|-------|--------|
| GOLDEN | >=9.5 | Auto-publish, no review |
| PUBLISH | >=8.0 | Publish after editorial approval |
| REVIEW | >=7.0 | Require editorial review |
| REJECT | <7.0 | Reject, rework required |

## Bypass
| Conditions | Approver | Audit Trail |
|------------|----------|-------------|
| Urgent support fix (<2h deadline) | Senior Editor | Incident ticket ID |
| Legacy entry critical update | Product Manager | Change log entry |
