---
kind: examples
id: bld_examples_bias_audit
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of bias_audit artifacts
quality: 9.1
title: "Examples Bias Audit"
version: "1.0.0"
author: wave1_builder_gen
tags: [bias_audit, builder, examples]
tldr: "Golden and anti-examples of bias_audit artifacts"
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

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
