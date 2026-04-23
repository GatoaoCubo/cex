---
kind: tools
id: bld_tools_incident_report
pillar: P04
llm_function: CALL
purpose: Tools available for incident_report production
quality: 8.9
title: "Tools Incident Report"
version: "1.1.0"
author: n05_ops
tags: [incident_report, builder, tools]
tldr: "Tools available for incident_report production"
domain: "incident_report construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_tools_edit_format
  - incident-report-builder
  - bld_tools_vad_config
  - bld_instruction_incident_report
  - bld_tools_subscription_tier
  - bld_collaboration_incident_report
  - bld_knowledge_card_incident_report
  - bld_tools_faq_entry
  - bld_tools_reasoning_strategy
  - p03_sp_incident_report_builder
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Generates structured incident reports | After data collection |
| cex_score.py | Assigns severity and impact scores | During triage |
| cex_retriever.py | Fetches incident-related data from logs | During investigation |
| cex_doctor.py | Diagnoses report inconsistencies | Before finalization |
| cex_analyzer.py | Identifies root causes | During analysis |
| cex_generator.py | Creates report templates | At report initiation |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| val_checker.py | Validates report syntax | After generation |
| val_formatter.py | Ensures consistent formatting | During editing |
| val_validator.py | Cross-checks data accuracy | Before submission |
| val_scorer.py | Reconfirms severity scores | During review |

## External References
- NIST SP 800-61 Rev. 2: Computer Security Incident Handling Guide (process framework)
- PagerDuty / Opsgenie: Incident alerting and on-call management
- Jira / Linear: Action item tracking with owner + due date
- Grafana / Datadog: Timeline reconstruction from metrics
- Loguru: Structured logging for timeline evidence collection

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_edit_format]] | sibling | 0.34 |
| [[incident-report-builder]] | downstream | 0.29 |
| [[bld_tools_vad_config]] | sibling | 0.28 |
| [[bld_instruction_incident_report]] | upstream | 0.28 |
| [[bld_tools_subscription_tier]] | sibling | 0.27 |
| [[bld_collaboration_incident_report]] | downstream | 0.26 |
| [[bld_knowledge_card_incident_report]] | upstream | 0.26 |
| [[bld_tools_faq_entry]] | sibling | 0.26 |
| [[bld_tools_reasoning_strategy]] | sibling | 0.25 |
| [[p03_sp_incident_report_builder]] | upstream | 0.25 |
