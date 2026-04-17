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
  - name: task_goal
    type: string
    required: true
    default: null
    description: The primary objective or goal to be accomplished through orchestration
  - name: target_nuclei
    type: list
    required: true
    default: null
    description: List of nuclei (N01-N07) that will participate in executing this task
  - name: priority_level
    type: string
    required: false
    default: "medium"
    description: Task priority level (low, medium, high, critical)
  - name: deadline
    type: string
    required: false
    default: null
    description: Target completion date or timeline constraint
  - name: dependencies
    type: list
    required: false
    default: []
    description: List of prerequisite tasks or resources that must be available
  - name: success_criteria
    type: list
    required: true
    default: null
    description: Measurable criteria that define successful task completion
  - name: resource_constraints
    type: object
    required: false
    default: {}
    description: Budget, time, or capacity limitations affecting task execution
  - name: coordination_mode
    type: string
    required: false
    default: "parallel"
    description: Execution mode (parallel, sequential, hybrid)
variable_syntax: "mustache"
composable: false
domain: orchestration
quality: 9.2
tags: [orchestration, task-dispatch, coordination, nuclei]
tldr: "Generates structured orchestration instructions for multi-nucleus task execution with clear goals and coordination."
keywords: [orchestration, dispatch, nuclei, coordination, task, parallel]
density_score: null
---
# Orchestration Task Dispatch Template

## Purpose
Produces structured orchestration instructions for coordinating multi-nucleus task execution within the CEX system. Reuse scope: any complex task requiring coordination between multiple specialized nuclei (N01-N07). Invoke once per orchestration goal; vary task parameters to produce distinct dispatch instructions from the same template structure.

## Variables Table
| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| task_goal | string | true | null | The primary objective or goal to be accomplished through orchestration |
| target_nuclei | list | true | null | List of nuclei (N01-N07) that will participate in executing this task |
| priority_level | string | false | "medium" | Task priority level (low, medium, high, critical) |
| deadline | string | false | null | Target completion date or timeline constraint |
| dependencies | list | false | [] | List of prerequisite tasks or resources that must be available |
| success_criteria | list | true | null | Measurable criteria that define successful task completion |
| resource_constraints | object | false | {} | Budget, time, or capacity limitations affecting task execution |
| coordination_mode | string | false | "parallel" | Execution mode (parallel, sequential, hybrid) |

## Template Body
```
You are the N07 Orchestrator coordinating a multi-nucleus task execution.

TASK GOAL: {{task_goal}}

EXECUTION PARAMETERS:
- Target Nuclei: {{target_nuclei}}
- Priority Level: {{priority_level}}
- Coordination Mode: {{coordination_mode}}
- Deadline: {{deadline}}

DEPENDENCIES:
{{#dependencies}}
- {{.}}
{{/dependencies}}

SUCCESS CRITERIA:
{{#success_criteria}}
- {{.}}
{{/success_criteria}}

RESOURCE CONSTRAINTS:
{{#resource_constraints}}
- {{.}}
{{/resource_constraints}}

ORCHESTRATION INSTRUCTIONS:
1. Validate all dependencies are satisfied before initiating dispatch
2. Create handoff files for each target nucleus in .cex/runtime/handoffs/
3. Execute coordination mode: {{coordination_mode}}
4. Monitor progress via signals in .cex/runtime/signals/
5. Consolidate results when all nuclei complete their assignments
6. Validate against success criteria before marking task complete

HANDOFF STRUCTURE for each nucleus:
- Task context and specific responsibilities
- Input data and parameters
- Expected outputs and quality gates
- Inter-nucleus coordination points
- Success criteria relevant to this nucleus

Monitor completion signals and initiate consolidation when all nuclei report task completion.
```

## Quality Gates
| Gate | Status | Notes |
|------|--------|-------|
| H01 | PASS | Frontmatter parses as valid YAML |
| H02 | PASS | id matches p03_pt_orchestration_task_dispatch pattern |
| H03 | PASS | id equals filename stem |
| H04 | PASS | kind equals literal prompt_template |
| H05 | PASS | quality is null at authoring time |
| H06 | PASS | All required frontmatter fields present |
| H07 | PASS | Body contains {{variable}} placeholders |
| H08 | PASS | All template variables declared in Variables section |

## Examples
### Variables:
```yaml
task_goal: "Create comprehensive brand identity system for new product launch"
target_nuclei: ["N02", "N03", "N06"]
priority_level: "high"
deadline: "2026-04-15"
dependencies: ["Market research completed", "Product specifications finalized"]
success_criteria: ["Brand guidelines documented", "Visual assets created", "Pricing strategy defined"]
resource_constraints: {"budget": 15000, "team_capacity": "3 FTE"}
coordination_mode: "sequential"
```

### Rendered Output:
```
You are the N07 Orchestrator coordinating a multi-nucleus task execution.

TASK GOAL: Create comprehensive brand identity system for new product launch

EXECUTION PARAMETERS:
- Target Nuclei: N02, N03, N06
- Priority Level: high
- Coordination Mode: sequential
- Deadline: 2026-04-15

DEPENDENCIES:
- Market research completed
- Product specifications finalized

SUCCESS CRITERIA:
- Brand guidelines documented
- Visual assets created
- Pricing strategy defined

RESOURCE CONSTRAINTS:
- budget: 15000
- team_capacity: 3 FTE

ORCHESTRATION INSTRUCTIONS:
1. Validate all dependencies are satisfied before initiating dispatch
2. Create handoff files for each target nucleus in .cex/runtime/handoffs/
3. Execute coordination mode: sequential
4. Monitor progress via signals in .cex/runtime/signals/
5. Consolidate results when all nuclei complete their assignments
6. Validate against success criteria before marking task complete

HANDOFF STRUCTURE for each nucleus:
- Task context and specific responsibilities
- Input data and parameters
- Expected outputs and quality gates
- Inter-nucleus coordination points
- Success criteria relevant to this nucleus

Monitor completion signals and initiate consolidation when all nuclei report task completion.
```