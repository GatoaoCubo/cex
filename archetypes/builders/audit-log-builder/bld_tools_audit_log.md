---
kind: tools
id: bld_tools_audit_log
pillar: P04
llm_function: CALL
purpose: Tools available for audit_log production
quality: 8.7
title: "Tools Audit Log"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [audit_log, builder, tools]
tldr: "Tools available for audit_log production"
domain: "audit_log construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles audit_log artifact to .yaml | After each save |
| cex_score.py | Scores artifact against 5D quality dimensions | Post-production |
| cex_retriever.py | Retrieves similar audit log specs and KCs | During F3 INJECT |
| cex_doctor.py | Validates builder ISO completeness and structure | During F7 GOVERN |
| cex_hygiene.py | Enforces frontmatter rules and naming conventions | During F7 GOVERN |

## External References
- SOC2 Type II Trust Service Criteria CC6.1, CC7.1, CC7.2
- ISO/IEC 27001:2022 Annex A.8.15 (logging)
- NIST SP 800-92 (Guide to Computer Security Log Management)
- AWS CloudTrail, Datadog Audit Trail, Splunk SIEM (implementation references)
