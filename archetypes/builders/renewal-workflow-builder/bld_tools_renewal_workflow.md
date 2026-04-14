---
kind: tools
id: bld_tools_renewal_workflow
pillar: P04
llm_function: CALL
purpose: Tools available for renewal_workflow production
quality: null
title: "Tools Renewal Workflow"
version: "1.0.0"
author: wave6_n06
tags: [renewal_workflow, builder, tools, renewal, GRR, Gainsight, Salesforce]
tldr: "Tools available for renewal_workflow production"
domain: "renewal_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool               | Purpose                                    | When                            |
|--------------------|--------------------------------------------|---------------------------------|
| cex_compile.py     | Compile renewal workflow YAML artifacts    | After artifact generation       |
| cex_score.py       | Score stage completeness and GRR model     | Post-generation quality check   |
| cex_retriever.py   | Fetch similar renewal workflows            | During F3 INJECT phase          |
| cex_doctor.py      | Diagnose schema compliance issues          | Pre-validation checks           |
| cex_validator.py   | Enforce frontmatter schema rules           | Data ingestion and post-build   |

## Validation Tools
| Tool               | Purpose                                    | When                            |
|--------------------|--------------------------------------------|---------------------------------|
| val_check.py       | Verify stage owner and escalation coverage | Pre-deployment                  |
| val_audit.py       | Cross-reference GRR model scenarios        | Monthly RevOps reviews          |
| val_comparator.py  | Detect duplicate renewal workflows         | Before creating new workflow    |
| val_sanitizer.py   | Clean invalid contract IDs or date formats | Data preprocessing              |

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
