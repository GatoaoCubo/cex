---
kind: architecture
id: bld_architecture_incident_report
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of incident_report -- inventory, dependencies
quality: null
title: "Architecture Incident Report"
version: "1.0.0"
author: wave1_builder_gen
tags: [incident_report, builder, architecture]
tldr: "Component map of incident_report -- inventory, dependencies"
domain: "incident_report construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
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
Incident_report-builder sits within CEX's risk management layer, integrating with data pipelines, validation systems, and storage to ensure transparent, auditable incident documentation across trading and operations.
