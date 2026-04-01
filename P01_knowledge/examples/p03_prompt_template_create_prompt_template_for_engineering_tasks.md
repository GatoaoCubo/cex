---
id: p03_pt_engineering_task_executor
kind: prompt_template
pillar: P03
title: "Engineering Task Executor Template"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: prompt-template-builder
variables:
  - name: task_type
    type: string
    required: true
    default: null
    description: Type of engineering task (code_review, debugging, system_design, refactoring, testing, documentation)
  - name: technology_stack
    type: list
    required: true
    default: null
    description: Technologies, frameworks, and tools involved in the task
  - name: complexity_level
    type: string
    required: false
    default: "intermediate"
    description: Task complexity level (beginner, intermediate, advanced, expert)
  - name: deliverable_format
    type: string
    required: false
    default: "structured_report"
    description: Expected output format (code, documentation, report, checklist, diagram)
  - name: context_description
    type: string
    required: true
    default: null
    description: Background context and specific details about the engineering task
  - name: success_criteria
    type: list
    required: false
    default: ["functional_correctness", "code_quality", "performance"]
    description: Criteria that define successful task completion
  - name: constraints
    type: list
    required: false
    default: []
    description: Technical constraints, limitations, or requirements to consider
variable_syntax: "mustache"
composable: true
domain: engineering
quality: 8.9
tags: [engineering, task-execution, code, development, structured]
tldr: "Executes engineering tasks with specified technology stack, complexity, and deliverables."
keywords: [engineering, development, code, task, execution, technical]
density_score: null
---
## Purpose

This template produces structured engineering task execution prompts for various software development activities. Reuse scope encompasses code reviews, debugging sessions, system design, refactoring, testing, and technical documentation tasks. Invoke once per engineering task by varying the task type, technology stack, and specific requirements to generate focused, actionable prompts.

## Variables Table

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| task_type | string | true | null | Type of engineering task (code_review, debugging, system_design, refactoring, testing, documentation) |
| technology_stack | list | true | null | Technologies, frameworks, and tools involved in the task |
| complexity_level | string | false | "intermediate" | Task complexity level (beginner, intermediate, advanced, expert) |
| deliverable_format | string | false | "structured_report" | Expected output format (code, documentation, report, checklist, diagram) |
| context_description | string | true | null | Background context and specific details about the engineering task |
| success_criteria | list | false | ["functional_correctness", "code_quality", "performance"] | Criteria that define successful task completion |
| constraints | list | false | [] | Technical constraints, limitations, or requirements to consider |

## Template Body

```
You are an expert software engineer with deep expertise in {{technology_stack}}. Execute the following engineering task with precision and attention to detail.

**Task Type**: {{task_type}}
**Complexity Level**: {{complexity_level}}
**Technology Stack**: {{technology_stack}}
**Deliverable Format**: {{deliverable_format}}

**Context & Background**:
{{context_description}}

**Success Criteria**:
{{#success_criteria}}
- {{.}}
{{/success_criteria}}

{{#constraints}}
**Technical Constraints**:
{{#constraints}}
- {{.}}
{{/constraints}}
{{/constraints}}

**Instructions**:
1. Analyze the task requirements thoroughly
2. Consider the technology stack limitations and best practices
3. Apply engineering principles appropriate for {{complexity_level}} level
4. Structure your response as a {{deliverable_format}}
5. Ensure all success criteria are addressed
6. Document any assumptions or decisions made
7. Provide actionable recommendations where applicable

**Output Requirements**:
- Clear, technical language appropriate for {{complexity_level}} audience
- Include code examples, diagrams, or specifications as needed
- Follow best practices for {{technology_stack}}
- Highlight potential risks or trade-offs
- Suggest next steps or follow-up actions

Execute this task systematically and provide a comprehensive response.
```

## Quality Gates

| Gate | Status | Notes |
|---|---|---|
| H01 | PASS | Frontmatter parses as valid YAML |
| H02 | PASS | `id` matches `^p03_pt_[a-z][a-z0-9_]+$` pattern |
| H03 | PASS | `id` equals filename stem |
| H04 | PASS | `kind` equals literal `prompt_template` |
| H05 | PASS | `quality` is null at authoring time |
| H06 | PASS | All required frontmatter fields present |
| H07 | PASS | Body contains `{{variable}}` placeholders |
| H08 | PASS | All body variables declared in Variables section |
| H09 | PASS | Template is composable for embedding in larger workflows |

## Examples

### Example 1: Code Review Task

**Variables**:
```yaml
task_type: "code_review"
technology_stack: ["Python", "FastAPI", "PostgreSQL", "Docker"]
complexity_level: "advanced"
deliverable_format: "checklist"
context_description: "Review a REST API implementation for a user authentication service with JWT tokens, database integration, and containerization"
success_criteria: ["security_compliance", "code_quality", "performance_optimization", "maintainability"]
constraints: ["PCI_DSS_compliance", "sub_200ms_response_time", "horizontal_scaling_support"]
```

**Rendered Output**:
```
You are an expert software engineer with deep expertise in Python, FastAPI, PostgreSQL, Docker. Execute the following engineering task with precision and attention to detail.

**Task Type**: code_review
**Complexity Level**: advanced
**Technology Stack**: Python, FastAPI, PostgreSQL, Docker
**Deliverable Format**: checklist

**Context & Background**:
Review a REST API implementation for a user authentication service with JWT tokens, database integration, and containerization

**Success Criteria**:
- security_compliance
- code_quality
- performance_optimization
- maintainability

**Technical Constraints**:
- PCI_DSS_compliance
- sub_200ms_response_time
- horizontal_scaling_support

[Rest of rendered template...]
```