---
kind: tools
id: bld_tools_audit_log
pillar: P04
llm_function: CALL
purpose: Tools available for audit_log production
quality: null
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
| cex_compile.py | Compiles raw audit events into structured logs | During log ingestion |  
| cex_score.py | Assigns risk scores to audit entries | During real-time monitoring |  
| cex_retriever.py | Fetches historical audit data for analysis | During forensic investigations |  
| cex_doctor.py | Diagnoses inconsistencies in audit trails | During validation phases |  
| cex_formatter.py | Standardizes log formats across systems | During integration with third-party tools |  
| cex_validator.py | Validates audit log completeness and integrity | Before log archival |  

## Validation Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| val_integrity_checker.py | Verifies cryptographic hashes of audit logs | After log compilation |  
| val_compliance_scanner.py | Checks logs against regulatory requirements | During audits |  
| val_anomaly_detector.py | Identifies outliers in audit patterns | During real-time monitoring |  
| val_report_generator.py | Produces summary reports for stakeholders | After validation cycles |  

## External References  
- OpenAudit (framework for audit log management)  
- ELK Stack (Elasticsearch, Logstash, Kibana for log analysis)  
- ISO/IEC 27001 (information security standards for audit trails)
