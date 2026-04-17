---
kind: collaboration
id: bld_collaboration_audit_log
pillar: P12
llm_function: COLLABORATE
purpose: How audit_log-builder works in crews with other builders
quality: 8.9
title: "Collaboration Audit Log"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [audit_log, builder, collaboration]
tldr: "How audit_log-builder works in crews with other builders"
domain: "audit_log construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Collects, formats, and stores system events for compliance, security, and operational auditing. Ensures logs are immutable, searchable, and traceable to specific actions or users.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Application   | User actions          | JSON        |  
| Security      | Authentication events | XML         |  
| System        | Infrastructure alerts | Syslog      |  

## Produces For  
| Builder       | What                  | Format        |  
|---------------|-----------------------|---------------|  
| Compliance    | Audit reports         | Structured log |  
| Security      | Incident investigation  | API endpoint  |  
| Operations    | Log aggregation       | SIEM-compatible |  

## Boundary  
Does NOT handle trace configuration (observability) or regression checks (quality). Trace_config is managed by observability tools; regression_check is handled by QA/Testing teams.
