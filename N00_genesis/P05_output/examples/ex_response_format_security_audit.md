---
id: p05_rf_security_audit
kind: response_format
pillar: P05
title: "Output Schema: Access Control Audit Report"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
format: markdown
quality: 9.0
tags: [security, audit, output]
tldr: "Structured security audit report with findings by severity, remediation roadmap, and OWASP compliance mapping"
max_bytes: 8192
density_score: 0.92
source: organization-core/records/agents/access_control_auditor/iso_vectorstore/ISO_operations_agent_007_OUTPUT_TEMPLATE.md
linked_artifacts:
  agent: p02_ag_access_control_auditor
  schema: null
related:
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_sandbox_config
  - bld_schema_safety_policy
  - bld_schema_audit_log
  - bld_schema_benchmark_suite
  - bld_schema_api_reference
---

# Output Schema: Access Control Audit Report

## Fields

| Field | Type | Required | Example |
|-------|------|----------|---------|
| timestamp | string (ISO 8601) | yes | `2026-03-22T14:30:00Z` |
| framework | string | yes | `FastAPI 0.104` |
| total_findings | int | yes | `12` |
| critical_count | int | yes | `2` |
| high_count | int | yes | `3` |
| overall_risk | enum(CRITICAL,HIGH,MEDIUM,LOW) | yes | `HIGH` |
| findings | list[Finding] | yes | see below |
| route_inventory | object | yes | protected/unprotected/public routes |
| cwe_summary | list[CWE] | no | `[{id: "CWE-306", count: 2}]` |

## Nested: Finding

| Field | Type | Required | Example |
|-------|------|----------|---------|
| id | string | yes | `F001` |
| severity | enum(CRITICAL,HIGH,MEDIUM,LOW,INFO) | yes | `CRITICAL` |
| cwe | string | yes | `CWE-306` |
| title | string | yes | `Missing Authentication on User Deletion` |
| file | string | yes | `api/routes/users.js:23` |
| vulnerable_code | string | yes | code snippet |
| remediation_code | string | yes | fixed code snippet |
| impact | string | yes | impact description |

## Constraints

- max_bytes: 8192
- format: markdown (primary) + JSON export
- encoding: utf-8
- Findings grouped by severity (CRITICAL > HIGH > MEDIUM > LOW > INFO)
- Each finding MUST include remediation code, not just description

## Valid Example

```json
{
  "metadata": {"timestamp": "2026-03-22T14:30:00Z", "framework": "FastAPI"},
  "summary": {"total_findings": 3, "by_severity": {"critical": 1, "high": 1, "medium": 1}},
  "findings": [
    {"id": "F001", "severity": "CRITICAL", "cwe": "CWE-306",
     "title": "Missing Auth on DELETE /users/:id",
     "file": "api/routes/users.js:23",
     "remediation_code": "app.delete('/users/:id', authenticate, authorize('admin'), handler)"}
  ]
}
```

## Invalid Example

```json
// FAILS: finding without remediation_code (required field)
{"id": "F001", "severity": "CRITICAL", "title": "Missing Auth", "description": "needs fix"}
```

## Error Handling

| Condition | Action | Return |
|-----------|--------|--------|
| No routes found in codebase | Warn + empty inventory | `{"findings": [], "warning": "no routes detected"}` |
| Scan timeout (>240s) | Return partial results | partial report + `"status": "timeout"` |
| Unrecognized framework | Fallback to generic scan | report with `"confidence": "T3"` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | downstream | 0.55 |
| [[bld_schema_pitch_deck]] | downstream | 0.52 |
| [[bld_schema_reranker_config]] | downstream | 0.52 |
| [[bld_schema_quickstart_guide]] | downstream | 0.51 |
| [[bld_schema_dataset_card]] | downstream | 0.51 |
| [[bld_schema_sandbox_config]] | downstream | 0.51 |
| [[bld_schema_safety_policy]] | downstream | 0.51 |
| [[bld_schema_audit_log]] | downstream | 0.50 |
| [[bld_schema_benchmark_suite]] | downstream | 0.49 |
| [[bld_schema_api_reference]] | downstream | 0.49 |
