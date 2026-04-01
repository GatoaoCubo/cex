---
id: p06_is_orchestration_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "input-schema-builder"
scope: "CEX orchestration system input contract for mission execution"
fields:
  - name: "mission"
    type: "string"
    required: true
    default: null
    description: "High-level goal or objective for the orchestration"
    error_message: "mission is required — provide a clear goal description"
  - name: "nuclei"
    type: "list"
    required: true
    default: null
    description: "List of nucleus identifiers (n01-n07) to involve in execution"
    error_message: "nuclei list is required — specify at least one nucleus (n01-n07)"
  - name: "priority"
    type: "string"
    required: false
    default: "normal"
    description: "Execution priority: low, normal, high, urgent"
    error_message: "priority must be: low, normal, high, or urgent"
  - name: "dependencies"
    type: "list"
    required: false
    default: []
    description: "List of prerequisite tasks or artifacts that must complete first"
    error_message: null
  - name: "constraints"
    type: "object"
    required: false
    default: {"max_parallel": 6, "timeout_minutes": 60}
    description: "Execution constraints: max_parallel, timeout_minutes, budget_limit"
    error_message: null
  - name: "context"
    type: "string"
    required: false
    default: null
    description: "Additional context or background information for the mission"
    error_message: null
  - name: "output_format"
    type: "string"
    required: false
    default: "summary"
    description: "Desired output format: summary, detailed, artifacts_only"
    error_message: "output_format must be: summary, detailed, or artifacts_only"
coercion:
  - from: "string"
    to: "list"
    rule: "Split comma-separated nucleus list into array"
  - from: "string"
    to: "integer"
    rule: "Parse numeric strings for timeout and parallel limits"
examples:
  - mission: "Create comprehensive brand identity system"
    nuclei: ["n02", "n06"]
    priority: "high"
    constraints: {"max_parallel": 2, "timeout_minutes": 90}
  - mission: "Research competitive landscape for AI tools"
    nuclei: ["n01"]
    priority: "normal"
    dependencies: ["brand_config_complete"]
    context: "Focus on productivity and automation tools"
    output_format: "detailed"
domain: "orchestration"
quality: 8.9
tags: [input-schema, orchestration, mission, nuclei, cex]
tldr: "Input contract for CEX orchestration: requires mission description and nuclei list, optional priority, dependencies, and execution constraints."
density_score: 0.87
---
## Contract Definition
The CEX orchestration system (N07) receives mission requests from users and other agents. Callers provide a mission description, specify which nuclei to involve, and optionally set priority, dependencies, and execution constraints. This schema ensures consistent orchestration input across all CEX operations.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | mission | string | YES | - | High-level goal or objective for orchestration |
| 2 | nuclei | list | YES | - | Nucleus identifiers (n01-n07) to involve |
| 3 | priority | string | NO | "normal" | Execution priority: low, normal, high, urgent |
| 4 | dependencies | list | NO | [] | Prerequisite tasks or artifacts |
| 5 | constraints | object | NO | {"max_parallel": 6, "timeout_minutes": 60} | Execution limits and timeouts |
| 6 | context | string | NO | null | Additional background information |
| 7 | output_format | string | NO | "summary" | Response format: summary, detailed, artifacts_only |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | list | Split comma-separated nucleus list ("n02,n06" → ["n02", "n06"]) |
| string | integer | Parse numeric strings for timeout and parallel limits |

## Examples
```json
{
  "mission": "Create comprehensive brand identity system",
  "nuclei": ["n02", "n06"],
  "priority": "high",
  "constraints": {"max_parallel": 2, "timeout_minutes": 90}
}
```

```json
{
  "mission": "Research competitive landscape for AI tools",
  "nuclei": ["n01"],
  "priority": "normal",
  "dependencies": ["brand_config_complete"],
  "context": "Focus on productivity and automation tools",
  "output_format": "detailed"
}
```

## References
- CEX Orchestration Rules: `.claude/rules/n07-orchestrator.md`
- Nucleus Routing Table: `CLAUDE.md`
- Mission Command: `.claude/commands/mission.md`