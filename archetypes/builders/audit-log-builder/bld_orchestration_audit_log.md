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
related:
  - bld_knowledge_card_audit_log
  - p03_sp_audit_log_builder
  - bld_collaboration_trace_config
  - bld_collaboration_oauth_app_config
  - audit-log-builder
  - bld_collaboration_sso_config
  - bld_collaboration_sandbox_config
  - kc_audit_log
  - bld_collaboration_action_paradigm
  - bld_collaboration_compliance_framework
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_audit_log]] | upstream | 0.28 |
| [[p03_sp_audit_log_builder]] | upstream | 0.28 |
| [[bld_collaboration_trace_config]] | sibling | 0.24 |
| [[bld_collaboration_oauth_app_config]] | sibling | 0.24 |
| [[audit-log-builder]] | upstream | 0.22 |
| [[bld_collaboration_sso_config]] | sibling | 0.22 |
| [[bld_collaboration_sandbox_config]] | sibling | 0.21 |
| [[kc_audit_log]] | upstream | 0.20 |
| [[bld_collaboration_action_paradigm]] | sibling | 0.20 |
| [[bld_collaboration_compliance_framework]] | sibling | 0.20 |
