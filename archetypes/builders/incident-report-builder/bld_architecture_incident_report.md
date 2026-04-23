---
kind: architecture
id: bld_architecture_incident_report
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of incident_report -- inventory, dependencies
quality: 8.9
title: "Architecture Incident Report"
version: "1.1.0"
author: n05_ops
tags: [incident_report, builder, architecture]
tldr: "Component map of incident_report -- inventory, dependencies"
domain: "incident_report construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_architecture_compliance_framework
  - bld_collaboration_incident_report
  - incident-report-builder
  - bld_architecture_formatter
  - bld_architecture_fintech_vertical
  - bld_architecture_ai_rmf_profile
  - bld_architecture_roi_calculator
  - bld_architecture_content_filter
  - bld_architecture_legal_vertical
  - bld_architecture_sandbox_config
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| IncidentReportGenerator | Creates structured reports | DevOps | Active |
| DataCollector | Aggregates incident logs | DataEng | Testing |
| Validator | Ensures data integrity | QA | Draft |
| Formatter | Applies template rules | UI/UX | Active |
| Storage | Persists reports | DB | Active |
| Notifier | Sends alerts on errors | SRE | Active |
| UserInterface | Input for manual entries | Frontend | Active |

## Dependencies
| From | To | Type |
|------|----|------|
| IncidentReportGenerator | DataCollector | Data |
| Validator | DataCollector | Control |
| Formatter | Validator | Data |
| Storage | Formatter | Data |
| Notifier | Validator | Control |
| UserInterface | Formatter | Control |

## Architectural Position
Incident_report-builder sits within CEX's P11 Feedback pillar as the post-incident documentation module. It consumes outputs from monitoring (trace_config), triage (bugloop), and knowledge systems (learning_record). Post-mortem reports feed upstream into compliance_framework (regulatory breach obligations), threat_model (updated threat surfaces from real incidents), and the knowledge library (P01). Follows NIST SP 800-61 incident lifecycle: Preparation -> Detection -> Containment -> Eradication -> Recovery -> Post-Incident.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_compliance_framework]] | sibling | 0.33 |
| [[bld_collaboration_incident_report]] | downstream | 0.33 |
| [[incident-report-builder]] | downstream | 0.31 |
| [[bld_architecture_formatter]] | sibling | 0.30 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.29 |
| [[bld_architecture_ai_rmf_profile]] | sibling | 0.29 |
| [[bld_architecture_roi_calculator]] | sibling | 0.29 |
| [[bld_architecture_content_filter]] | sibling | 0.29 |
| [[bld_architecture_legal_vertical]] | sibling | 0.29 |
| [[bld_architecture_sandbox_config]] | sibling | 0.29 |
