---
id: p03_pt_orchestration_task_dispatch
kind: prompt_template
pillar: P03
title: "Orchestration Task Dispatch Template"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: prompt-template-builder
variables:
  - name: task_description
    type: string
    required: true
    default: null
    description: The main task or goal that needs orchestration across nuclei
  - name: target_nuclei
    type: list
    required: true
    default: null
    description: List of nuclei that should participate in this orchestration
  - name: priority
    type: string
    required: false
    default: "medium"
    description: Task priority level (low, medium, high, urgent)
  - name: deadline
    type: string
    required: false
    default: null
    description: Target completion date in YYYY-MM-DD format
  - name: success_criteria
    type: list
    required: true
    default: null
    description: Measurable outcomes that define successful completion
  - name: dependencies
    type: list
    required: false
    default: []
    description: Other tasks or artifacts this orchestration depends on
  - name: stakeholder
    type: string
    required: true
    default: null
    description: Who requested this orchestration or owns the outcome
  - name: resources
    type: list
    required: false
    default: []
    description: Available resources, constraints, or special requirements
variable_syntax: "mustache"
composable: false
domain: orchestration
quality: 9.0
tags: [orchestration, dispatch, multi-nucleus, coordination, prompt-template]
tldr: "Structures orchestration requests for N07 to dispatch tasks across multiple nuclei with clear success criteria."
keywords: [orchestration, dispatch, nuclei, coordination, multi-agent, task-routing]
density_score: null
---
# Orchestration Task Dispatch Template

## Purpose

Produces structured orchestration requests for N07 (Orchestrator) to dispatch complex tasks across multiple nuclei. Reuse scope: any multi-step goal requiring coordination between different domain specialists (research, marketing, knowledge, operations, commercial). Invoke once per orchestration cycle; vary task parameters to produce distinct coordination plans from the same mold.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| task_description | string | true | null | The main task or goal that needs orchestration across nuclei |
| target_nuclei | list | true | null | List of nuclei that should participate in this orchestration |
| priority | string | false | "medium" | Task priority level (low, medium, high, urgent) |
| deadline | string | false | null | Target completion date in YYYY-MM-DD format |
| success_criteria | list | true | null | Measurable outcomes that define successful completion |
| dependencies | list | false | [] | Other tasks or artifacts this orchestration depends on |
| stakeholder | string | true | null | Who requested this orchestration or owns the outcome |
| resources | list | false | [] | Available resources, constraints, or special requirements |

## Template Body

```
# ORCHESTRATION REQUEST

## Task Overview
**Goal**: {{task_description}}
**Stakeholder**: {{stakeholder}}
**Priority**: {{priority}}
{{#deadline}}**Deadline**: {{deadline}}{{/deadline}}

## Nucleus Coordination
**Target Nuclei**: {{#target_nuclei}}{{.}}, {{/target_nuclei}}

Route this orchestration across the specified nuclei with the following distribution:
- Each nucleus should focus on their domain expertise
- Maintain consistent handoff protocols between nuclei
- Ensure all dependencies are resolved before downstream tasks begin

## Success Definition
The orchestration is complete when ALL of the following criteria are met:
{{#success_criteria}}
- {{.}}
{{/success_criteria}}

## Dependencies & Constraints
{{#dependencies}}
**Dependencies**: 
{{#dependencies}}
- {{.}}
{{/dependencies}}
{{/dependencies}}

{{#resources}}
**Available Resources**:
{{#resources}}
- {{.}}
{{/resources}}
{{/resources}}

## Execution Instructions
1. Parse this request and identify specific sub-tasks for each target nucleus
2. Create handoff files for each nucleus in `.cex/runtime/handoffs/`
3. Execute dispatch via `bash _spawn/dispatch.sh grid ORCHESTRATION_{{priority}}`
4. Monitor progress through signals in `.cex/runtime/signals/`
5. Consolidate results when all nuclei signal completion
6. Validate against success criteria before marking complete

**Guidance for N07**: Apply Guided Decision Protocol (GDP) if any subjective choices need stakeholder input before dispatch.
```

## Quality Gates

| Gate | Status | Notes |
|------|--------|--------|
| H01 | PASS | Frontmatter parses as valid YAML |
| H02 | PASS | ID `p03_pt_orchestration_task_dispatch` matches pattern `^p03_pt_[a-z][a-z0-9_]+$` |
| H03 | PASS | All 8 template variables declared and appear in body |
| H04 | PASS | No undeclared variables used in template body |
| H05 | PASS | File size under 8192 bytes |
| H06 | PASS | Variable syntax consistently uses mustache tier-1 |
| H07 | PASS | All required frontmatter fields present |
| H08 | PASS | Kind field equals `prompt_template` |

## Examples

### Variables
```yaml
task_description: "Launch comprehensive brand identity system for TechFlow SaaS platform"
target_nuclei: ["N02", "N03", "N06"]
priority: "high" 
deadline: "2026-04-15"
success_criteria:
  - "Complete brand guide with logo, colors, typography published"
  - "Landing page deployed with new brand identity"
  - "Pricing strategy aligned with brand positioning"
stakeholder: "CMO Sarah Chen"
dependencies: ["market_research_report", "competitor_analysis"]
resources: ["$15K design budget", "Brand consultant available", "Development team allocated"]
```

### Rendered Output
```
# ORCHESTRATION REQUEST

## Task Overview
**Goal**: Launch comprehensive brand identity system for TechFlow SaaS platform
**Stakeholder**: CMO Sarah Chen
**Priority**: high
**Deadline**: 2026-04-15

## Nucleus Coordination
**Target Nuclei**: N02, N03, N06, 

Route this orchestration across the specified nuclei with the following distribution:
- Each nucleus should focus on their domain expertise
- Maintain consistent handoff protocols between nuclei
- Ensure all dependencies are resolved before downstream tasks begin

## Success Definition
The orchestration is complete when ALL of the following criteria are met:
- Complete brand guide with logo, colors, typography published
- Landing page deployed with new brand identity
- Pricing strategy aligned with brand positioning

## Dependencies & Constraints

**Dependencies**: 
- market_research_report
- competitor_analysis

**Available Resources**:
- $15K design budget
- Brand consultant available
- Development team allocated

## Execution Instructions
1. Parse this request and identify specific sub-tasks for each target nucleus
2. Create handoff files for each nucleus in `.cex/runtime/handoffs/`
3. Execute dispatch via `bash _spawn/dispatch.sh grid ORCHESTRATION_high`
4. Monitor progress through signals in `.cex/runtime/signals/`
5. Consolidate results when all nuclei signal completion
6. Validate against success criteria before marking complete

**Guidance for N07**: Apply Guided Decision Protocol (GDP) if any subjective choices need stakeholder input before dispatch.
```