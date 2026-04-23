---
kind: tools
id: bld_tools_renewal_workflow
pillar: P04
llm_function: CALL
purpose: Tools available for renewal_workflow production
quality: 9.0
title: "Tools Renewal Workflow"
version: "1.0.0"
author: wave6_n06
tags: [renewal_workflow, builder, tools, renewal, GRR, Gainsight, Salesforce]
tldr: "Tools available for renewal_workflow production"
domain: "renewal_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - renewal-workflow-builder
  - bld_knowledge_card_renewal_workflow
  - p12_sp_renewal_workflow_builder
  - bld_tools_churn_prevention_playbook
  - bld_collaboration_renewal_workflow
  - bld_output_template_renewal_workflow
  - bld_architecture_renewal_workflow
  - bld_instruction_renewal_workflow
  - bld_tools_nps_survey
  - bld_examples_renewal_workflow
---

## Production Tools
| Tool                  | Purpose                                        | When                          |
|-----------------------|------------------------------------------------|-------------------------------|
| cex_compile.py        | Compile .md to .yaml                           | After every save              |
| cex_score.py          | Apply peer-review quality score                | Post-production               |
| cex_retriever.py      | Fetch similar renewal workflow artifacts       | During F3 INJECT              |
| cex_doctor.py         | Diagnose schema and frontmatter issues         | Pre-publish validation        |
| cex_wave_validator.py | Validate domain keywords and ISO completeness  | Post-build CI gate            |

## Validation Tools
| Tool                  | Purpose                                        | When                          |
|-----------------------|------------------------------------------------|-------------------------------|
| cex_schema_hydrate.py | Enforce schema constraints on frontmatter      | Pre-commit                    |
| cex_hooks.py          | Pre-commit ASCII and schema checks             | git commit                    |

## External Integrations
| System             | Purpose                                    | Integration Type                |
|--------------------|--------------------------------------------|---------------------------------|
| Gainsight CS       | Health score, CTA automation, renewal CTAs | REST API + Webhook              |
| Salesforce CPQ     | Renewal Opportunity, contract amendments   | REST API (v58.0+)               |
| DocuSign / Adobe   | Contract signature and amendment execution | eSignature API                  |
| Zuora / Chargebee  | Subscription billing and auto-renewal mgmt | Billing platform API            |
| Clari / Gong       | Renewal forecast and conversation intel    | Revenue intelligence API        |

## External References
- Gainsight Renewal Center: stage-based CTA design documentation
- Salesforce CPQ Renewal Playbook: Opportunity management configuration
- Zuora Subscription Management API v1: auto-renewal and contract amendment
- California ARL (Bus. & Prof. Code Section 17600): auto-renewal notice compliance

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[renewal-workflow-builder]] | downstream | 0.48 |
| [[bld_knowledge_card_renewal_workflow]] | upstream | 0.45 |
| [[p12_sp_renewal_workflow_builder]] | downstream | 0.43 |
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.42 |
| [[bld_collaboration_renewal_workflow]] | downstream | 0.41 |
| [[bld_output_template_renewal_workflow]] | downstream | 0.39 |
| [[bld_architecture_renewal_workflow]] | downstream | 0.37 |
| [[bld_instruction_renewal_workflow]] | upstream | 0.34 |
| [[bld_tools_nps_survey]] | sibling | 0.33 |
| [[bld_examples_renewal_workflow]] | downstream | 0.33 |
