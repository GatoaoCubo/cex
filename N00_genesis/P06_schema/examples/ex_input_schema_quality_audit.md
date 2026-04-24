---
id: p06_is_quality_audit
kind: input_schema
8f: F1_constrain
pillar: P06
title: "Input Schema: Quality Audit Pipeline"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
quality: 9.1
tags: [quality, audit, input, contract]
tldr: "Validates input parameters for the codebase quality audit pipeline (scope, threshold, scan options)"
density_score: 0.90
source: organization-core/records/core/examples/blueprint_quality_audit.yaml
linked_artifacts:
  agent: p02_ag_qa_agent
  output: p05_os_quality_report
related:
  - bld_schema_input_schema
  - bld_schema_optimizer
  - p03_ch_content_pipeline
  - bld_schema_research_pipeline
  - bld_schema_validation_schema
  - p03_ch_kc_to_notebooklm
  - bld_schema_e2e_eval
  - bld_schema_reranker_config
  - bld_schema_unit_eval
  - bld_schema_model_registry
---

# Input Schema: Quality Audit Pipeline

## Fields

| Field | Type | Required | Default | Constraints | Example |
|-------|------|----------|---------|-------------|---------|
| scope | string | yes | none | min_length: 1, must be valid path | `records/agents/` |
| threshold | float | no | 7.0 | min: 0.0, max: 10.0 | `8.0` |
| scan_type | enum | no | `full` | one_of: [full, quick, deep] | `full` |
| exclude_patterns | list[string] | no | `[]` | valid glob patterns | `["*.test.*", "node_modules/"]` |
| output_format | enum | no | `markdown` | one_of: [markdown, json, both] | `both` |

## Step Contracts

### Step 1: scan_files (code)

| Direction | Field | Type | Source |
|-----------|-------|------|--------|
| input | scope | string | blueprint.params.scope |
| output | file_list | list[string] | scan result |
| output | file_stats | object | `{total: int, by_ext: {}}` |
| output | total_lines | int | line count |

### Step 2: analyze_quality (agent: qa-agent)

| Direction | Field | Type | Source |
|-----------|-------|------|--------|
| input | files | list[string] | scan_files.file_list |
| input | stats | object | scan_files.file_stats |
| output | quality_issues | list[Issue] | analysis result |
| output | per_file_scores | object | `{path: float}` |

## Validation Rules

1. If scope is empty or null: `"scope is required: provide directory or file path to audit"`
2. If threshold < 0 or > 10: `"threshold must be between 0.0 and 10.0, got {value}"`
3. If scope path does not exist: `"scope path not found: {scope}"`

## Valid Input Example

```yaml
scope: records/agents/scout-agent/
threshold: 8.0
scan_type: full
exclude_patterns: ["*.test.*"]
output_format: both
```

## Invalid Input Example

```yaml
# FAILS: scope is empty string (required, min_length: 1)
scope: ""
threshold: 15.0  # FAILS: max is 10.0
```

## Upstream/Downstream

| Direction | Component | Protocol |
|-----------|-----------|----------|
| upstream | orchestrator handoff | handoff file (.md) |
| downstream | qa-agent | blueprint step chain |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_input_schema]] | related | 0.30 |
| [[bld_schema_optimizer]] | related | 0.27 |
| [[p03_ch_content_pipeline]] | upstream | 0.25 |
| [[bld_schema_research_pipeline]] | related | 0.25 |
| [[bld_schema_validation_schema]] | related | 0.23 |
| [[p03_ch_kc_to_notebooklm]] | upstream | 0.23 |
| [[bld_schema_e2e_eval]] | related | 0.23 |
| [[bld_schema_reranker_config]] | related | 0.23 |
| [[bld_schema_unit_eval]] | related | 0.23 |
| [[bld_schema_model_registry]] | related | 0.23 |
