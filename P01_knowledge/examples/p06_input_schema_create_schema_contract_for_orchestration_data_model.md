---
id: p06_is_orchestration_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "input-schema-builder"
title: "Orchestration Pipeline Data Contract"
scope: "orchestration pipeline execution system"
when_to_use: "When N07 dispatches missions to multiple nuclei requiring standardized input validation"
fields:
  - name: "mission_id"
    type: "string"
    required: true
    default: null
    description: "Unique identifier for orchestration mission"
    error_message: "mission_id is required - provide a unique mission identifier"
  - name: "nuclei_config"
    type: "object"
    required: true
    default: null
    description: "Configuration mapping nuclei to their assigned tasks"
    error_message: "nuclei_config is required - specify which nuclei handle which tasks"
  - name: "execution_mode"
    type: "string"
    required: false
    default: "parallel"
    description: "Execution strategy: parallel, sequential, or hybrid"
    error_message: "execution_mode must be: parallel, sequential, or hybrid"
  - name: "timeout_seconds"
    type: "integer"
    required: false
    default: 3600
    description: "Maximum execution time in seconds"
    error_message: "timeout_seconds must be a positive integer"
  - name: "dependencies"
    type: "list"
    required: false
    default: []
    description: "Task dependency graph as list of [prerequisite, dependent] pairs"
    error_message: null
  - name: "priority"
    type: "integer"
    required: false
    default: 5
    description: "Execution priority from 1 (highest) to 10 (lowest)"
    error_message: "priority must be integer between 1 and 10"
  - name: "handoff_strategy"
    type: "string"
    required: false
    default: "file_based"
    description: "How nuclei pass data: file_based, signal_based, or memory_shared"
    error_message: "handoff_strategy must be: file_based, signal_based, or memory_shared"
  - name: "quality_gates"
    type: "object"
    required: false
    default: {"min_score": 8.0, "enforce": true}
    description: "Quality enforcement configuration"
    error_message: null
coercion:
  - from: "string"
    to: "integer"
    rule: "Parse timeout_seconds and priority from string if numeric"
  - from: "string"
    to: "list"
    rule: "Split comma-separated dependency strings into list pairs"
examples:
  - mission_id: "BRAND_LAUNCH_001"
    nuclei_config: {"n02": ["create_landing_copy"], "n03": ["build_brand_guide"]}
    execution_mode: "parallel"
    timeout_seconds: 7200
    priority: 3
  - mission_id: "RESEARCH_SPRINT_042"
    nuclei_config: {"n01": ["analyze_market"], "n04": ["build_knowledge_base"]}
    execution_mode: "sequential"
    dependencies: [["analyze_market", "build_knowledge_base"]]
    handoff_strategy: "signal_based"
domain: "orchestration-pipeline"
quality: 0.0
tags: [input-schema, orchestration, pipeline, nuclei, CEX]
tldr: "Input contract for orchestration pipeline: requires mission_id and nuclei_config, optional execution settings and dependencies."
density_score: 0.92
---

## Contract Definition
The orchestration pipeline receives execution requests from N07 (orchestrator) or mission commands. Callers provide a mission identifier, nucleus-to-task mapping, and optional execution parameters for parallel/sequential dispatch with dependency management.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | mission_id | string | YES | - | Unique identifier for orchestration mission |
| 2 | nuclei_config | object | YES | - | Configuration mapping nuclei to their assigned tasks |
| 3 | execution_mode | string | NO | "parallel" | Execution strategy: parallel, sequential, or hybrid |
| 4 | timeout_seconds | integer | NO | 3600 | Maximum execution time in seconds |
| 5 | dependencies | list | NO | [] | Task dependency graph as [prerequisite, dependent] pairs |
| 6 | priority | integer | NO | 5 | Execution priority from 1 (highest) to 10 (lowest) |
| 7 | handoff_strategy | string | NO | "file_based" | Data passing method between nuclei |
| 8 | quality_gates | object | NO | {"min_score": 8.0} | Quality enforcement configuration |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | integer | Parse timeout_seconds and priority from string if numeric |
| string | list | Split comma-separated dependency strings into list pairs |

## Examples
```json
{
  "mission_id": "BRAND_LAUNCH_001",
  "nuclei_config": {"n02": ["create_landing_copy"], "n03": ["build_brand_guide"]},
  "execution_mode": "parallel",
  "timeout_seconds": 7200,
  "priority": 3
}
```

## References
- CEX Orchestration Protocol: `.claude/rules/n07-orchestrator.md`
- Nucleus Dispatch Rules: `_spawn/dispatch.sh`
- Mission Planning: `.claude/commands/mission.md`