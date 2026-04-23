---
kind: output_template
id: bld_output_template_bias_audit
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for bias_audit production
quality: 8.9
title: "Output Template Bias Audit"
version: "1.0.0"
author: wave1_builder_gen
tags: [bias_audit, builder, output_template]
tldr: "Template with vars for bias_audit production"
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_bias_audit
  - bld_instruction_bias_audit
  - p03_sp_bias_audit_builder
  - bias-audit-builder
  - p10_lr_bias_audit_builder
  - kc_bias_audit
  - bld_collaboration_bias_audit
  - bld_knowledge_card_bias_audit
  - bld_tools_bias_audit
  - bld_schema_bias_audit
---

# p07_ba_{{name}}.md

This ISO drives a bias audit: measuring fairness across demographic slices.

```yaml
---
title: {{title}}
description: {{description}}
auditor: {{auditor}}
date: {{date}}
scope: {{scope}}
methodology: {{methodology}}
findings: {{findings}}
recommendations: {{recommendations}}
status: {{status}}
---
```

## Introduction  
`{{introduction_content}}`  

## Scope  
`{{scope_content}}`  

## Methodology  
`{{methodology_content}}`  

## Findings  
`{{findings_content}}`  

## Recommendations  
`{{recommendations_content}}`  

## Conclusion  
`{{conclusion_content}}`

## Validation Checklist
| # | Check | Pass Condition |
|---|-------|---------------|
| 1 | Methodology documented | At least 1 fairness metric defined |
| 2 | Demographic groups specified | Protected attributes listed |
| 3 | Baseline comparison present | Reference model defined |
| 4 | Statistical significance reported | p-value or confidence interval |
| 5 | Disparity metric computed | Demographic parity or equalized odds |
| 6 | Recommendations present | At least 1 actionable recommendation |
| 7 | Data source cited | Dataset name and sample size |
| 8 | Reproducibility check | Methodology reproducible |
| 9 | Trade-offs noted | Fairness vs accuracy addressed |
| 10 | quality: null | Never self-scored |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_bias_audit]] | downstream | 0.43 |
| [[bld_instruction_bias_audit]] | upstream | 0.40 |
| [[p03_sp_bias_audit_builder]] | upstream | 0.33 |
| [[bias-audit-builder]] | downstream | 0.31 |
| [[p10_lr_bias_audit_builder]] | downstream | 0.29 |
| [[kc_bias_audit]] | upstream | 0.27 |
| [[bld_collaboration_bias_audit]] | downstream | 0.25 |
| [[bld_knowledge_card_bias_audit]] | upstream | 0.21 |
| [[bld_tools_bias_audit]] | upstream | 0.21 |
| [[bld_schema_bias_audit]] | downstream | 0.20 |
