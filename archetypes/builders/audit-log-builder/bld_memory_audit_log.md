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
