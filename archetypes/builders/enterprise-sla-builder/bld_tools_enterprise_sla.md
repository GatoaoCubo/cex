---
kind: tools
id: bld_tools_enterprise_sla
pillar: P04
llm_function: CALL
purpose: Tools available for enterprise_sla production
quality: 8.9
title: "Tools Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, tools]
tldr: "Tools available for enterprise_sla production"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_white_label_config
  - bld_tools_usage_report
  - enterprise-sla-builder
  - bld_tools_github_issue_template
  - bld_collaboration_enterprise_sla
  - p03_sp_enterprise_sla_builder
  - bld_tools_legal_vertical
  - bld_tools_customer_segment
  - bld_tools_app_directory_entry
  - bld_tools_integration_guide
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile SLA artifact to YAML + register in index | After authoring |
| cex_score.py | Score artifact quality (5D + HARD gates) | After compile |
| cex_retriever.py | Retrieve similar SLA artifacts for template reuse | During F3 INJECT |
| cex_doctor.py | Validate all ISOs in builder for structural health | Post-build audit |
| cex_wave_validator.py | Batch-validate full enterprise-sla-builder (39 ISOs) | CI gate |
| cex_hygiene.py | Enforce 8 hygiene rules (frontmatter, density, IDs) | Pre-commit |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_hooks.py | Pre-commit hook: block non-ASCII + schema violations | On git add |
| cex_sanitize.py | ASCII sanitize .py/.ps1 in builder scope | After code edits |
| cex_feedback.py | Track quality trends + archive low-score artifacts | After scoring |

## External References
- ITIL 4 (Service Level Management framework)
- ISO/IEC 20000-1:2018 (IT Service Management SLA requirements)
- Google SRE Book: Error Budgets and SLO/SLI/SLA distinction
- Prometheus (uptime and latency monitoring reference)
- PagerDuty (incident escalation and SLA breach alerting)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_white_label_config]] | sibling | 0.51 |
| [[bld_tools_usage_report]] | sibling | 0.47 |
| [[enterprise-sla-builder]] | downstream | 0.39 |
| [[bld_tools_github_issue_template]] | sibling | 0.36 |
| [[bld_collaboration_enterprise_sla]] | downstream | 0.33 |
| [[p03_sp_enterprise_sla_builder]] | upstream | 0.32 |
| [[bld_tools_legal_vertical]] | sibling | 0.32 |
| [[bld_tools_customer_segment]] | sibling | 0.32 |
| [[bld_tools_app_directory_entry]] | sibling | 0.31 |
| [[bld_tools_integration_guide]] | sibling | 0.31 |
