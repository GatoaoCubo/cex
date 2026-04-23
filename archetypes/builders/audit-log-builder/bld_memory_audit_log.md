---
kind: memory
id: p10_mem_audit_log_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for audit_log construction
quality: 8.7
title: "Memory Audit Log"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [audit_log, builder, memory]
tldr: "Learned patterns and pitfalls for audit_log construction"
domain: "audit_log construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_audit_log
  - audit-log-builder
  - p03_sp_audit_log_builder
  - bld_knowledge_card_audit_log
  - p11_qg_audit_log
  - bld_examples_audit_log
  - kc_audit_log
  - p10_lr_workflow_node_builder
  - p10_lr_edit_format_builder
  - p10_mem_github_issue_template_builder
---

## Observation
Common issues include inconsistent event schema, missing required fields (e.g., actor, action, timestamp), and mutable log entries that allow post-creation modifications.

## Pattern
Successful implementations use strict JSON schemas with predefined fields, enforce immutability via cryptographic hashing, and align with SOC2 Type II controls (e.g., CC6.1).

## Evidence
Reviewed artifacts showed reduced compliance risks when using standardized schemas and hash-based immutability checks.

## Recommendations
- Enforce schema validation via tools like JSON Schema or OpenAPI.
- Use cryptographic hashing (e.g., SHA-256) to ensure log immutability.
- Include mandatory fields: `actor`, `action`, `timestamp`, `resource`, `outcome`.
- Automate compliance checks against SOC2 Type II control objectives.
- Document audit log spec in a version-controlled repository.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_audit_log]] | upstream | 0.41 |
| [[audit-log-builder]] | downstream | 0.36 |
| [[p03_sp_audit_log_builder]] | upstream | 0.35 |
| [[bld_knowledge_card_audit_log]] | upstream | 0.30 |
| [[p11_qg_audit_log]] | downstream | 0.26 |
| [[bld_examples_audit_log]] | upstream | 0.24 |
| [[kc_audit_log]] | upstream | 0.20 |
| [[p10_lr_workflow_node_builder]] | related | 0.20 |
| [[p10_lr_edit_format_builder]] | related | 0.19 |
| [[p10_mem_github_issue_template_builder]] | sibling | 0.17 |
