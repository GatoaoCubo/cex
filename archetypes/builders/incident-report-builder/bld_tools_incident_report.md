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
