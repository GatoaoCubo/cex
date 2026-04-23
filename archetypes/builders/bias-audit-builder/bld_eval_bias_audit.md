---
kind: quality_gate
id: p07_qg_bias_audit
pillar: P07
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for bias_audit
quality: 9.1
title: "Quality Gate Bias Audit"
version: "1.1.0"
author: n06_hybrid_review
tags: [bias_audit, builder, quality_gate]
tldr: "Quality gate for bias_audit -- fixed pillar (P07), corrected ID pattern, added named benchmark and jurisdiction compliance HARD gates."
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
related:
  - bld_examples_bias_audit
  - bld_knowledge_card_bias_audit
  - bld_schema_bias_audit
  - bld_output_template_bias_audit
  - n06_audit_bias_audit_builder
  - bld_instruction_bias_audit
  - bias-audit-builder
  - kc_bias_audit
  - bld_tools_bias_audit
  - p03_sp_bias_audit_builder
---

## Quality Gate

## Definition

This ISO drives a bias audit: measuring fairness across demographic slices.
| metric | threshold | operator | scope | scale |
|--------|-----------|----------|-------|-------|
| disparate_impact_ratio | 0.80 | >= | protected_group / reference_group | 0.0-1.0 (EEOC 4/5 rule) |
| demographic_parity_diff | 0.05 | <= | |P(Y=1\|A=0) - P(Y=1\|A=1)| | 0.0-1.0 |
| equal_opportunity_diff | 0.05 | <= | |TPR_group0 - TPR_group1| | 0.0-1.0 |
| benchmark_coverage | 1 | >= | named benchmarks used (BBQ/WinoBias/StereoSet/BOLD) | count |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match ^p07_ba_[a-zA-Z0-9_]+\.md$ |
| H03 | kind matches | kind is not "bias_audit" |
| H04 | pillar correct | pillar is not "P07" |
| H05 | benchmarks_used present | benchmarks_used list is empty or missing |
| H06 | at least one named benchmark | None of: BBQ, WinoBias, StereoSet, BOLD, HolisticBias, Winogender |
| H07 | affected_groups present | affected_groups list is empty or missing |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Named benchmark coverage | 0.20 | >= 3 named benchmarks = 1.0; 2 = 0.7; 1 = 0.4; 0 = 0.0 |
| D2 | Metric completeness | 0.15 | All 3 metrics (parity diff, opp diff, impact ratio) = 1.0; 2 = 0.7; 1 = 0.4 |
| D3 | Protected attribute coverage | 0.15 | >= 4 attributes = 1.0; 2-3 = 0.7; 1 = 0.4 |
| D4 | Jurisdiction compliance docs | 0.15 | NYC LL144 + Colorado + EU AI Act = 1.0; any 2 = 0.7; 1 = 0.4; 0 = 0.0 |
| D5 | Mitigation strategy | 0.10 | Specific strategy with expected outcome = 1.0; vague = 0.5; absent = 0.0 |
| D6 | Statistical rigor | 0.10 | p-value + effect size reported = 1.0; p-value only = 0.7; absent = 0.0 |
| D7 | Intersectional analysis | 0.10 | Cross-tabulation present = 1.0; absent = 0.0 |
| D8 | Documentation quality | 0.05 | Reproducible methodology = 1.0; partial = 0.5; vague = 0.0 |

## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN -- auto-approve; usable as NYC LL144 public summary template |
| >= 8.0 | PUBLISH -- usable after legal review for compliance submissions |
| >= 7.0 | REVIEW -- escalate to senior auditor; not suitable for regulatory filing |
| < 7.0 | REJECT -- mandatory rewrite; cannot be used as compliance documentation |

## Bypass
| Condition | Approver | Audit Trail Required |
|-----------|----------|----------------------|
| Independent auditor pre-certified (NYC LL144) | Chief Compliance Officer | Auditor certification on file |
| EU conformity assessment completed | Legal + CISO | Annex IV documentation |
| Academic research (no deployment) | Research Ethics Board | IRB approval document |

## Examples

## Golden Example

This ISO drives a bias audit: measuring fairness across demographic slices.
```markdown
---
title: "Gender Bias Audit in Loan Approval Model"
authors: ["Alice Smith", "Bob Johnson"]
date: "2023-10-01"
kind: "bias_audit"
---

**Methodology**:
- Evaluated demographic parity and equalized odds across gender (male/female) using 10,000 loan applications.
- Used SHAP values to analyze feature contributions.
- Compared outcomes against baseline model (no fairness constraints).

**Results**:
- Female applicants had 15% lower approval rates (p < 0.01).
- SHAP analysis revealed "credit score" was the primary driver, but interaction with gender was significant.
- Post-audit model reduced disparity by 70% via reweighting.

**Discussion**:
- Trade-offs between fairness and accuracy (2% drop in overall accuracy).
- Recommendations: Monitor gender-disparity metrics quarterly.
```

## Anti-Example 1: Missing Methodology
```markdown
---
title: "Quick Bias Check"
authors: ["Charlie Brown"]
date: "2023-09-15"
kind: "bias_audit"
---

**Results**:
- "Found bias in age group 30-40."
- "Suggested adding age to fairness constraints."
```
## Why it fails
No explanation of evaluation methodology, metrics, or data sources. Cannot verify claims or reproduce analysis.

## Anti-Example 2: Single Metric Focus
```markdown
---
title: "Accuracy Audit"
authors: ["Dana White"]
date: "2023-08-20"
kind: "bias_audit"
---

**Methodology**:
- Evaluated model accuracy on test set.

**Results**:
- Accuracy: 85%.
```
## Why it fails
Confuses general performance evaluation with fairness audit. Ignores required fairness-specific metrics and analysis.

## Pattern Recognition
| Pattern | Indicator | Correct Action |
|---------|-----------|---------------|
| Missing demographic | No protected attributes listed | Add group definitions |
| Single metric | Only accuracy reported | Add fairness metrics |
| No baseline | No reference model | Define comparison baseline |
| Vague methodology | 'We checked bias' | Specify metric + method |
| No significance test | Raw numbers only | Add statistical significance |
| Single group only | One demographic | Audit all relevant groups |
| No recommendations | Results only | Add actionable steps |
| Self-scored quality | quality: 9.0 | Set to null |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
