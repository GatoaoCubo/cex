---
id: p03_pt_engineering_task_execution
kind: prompt_template
pillar: P03
title: "Engineering Task Execution Template"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: prompt-template-builder
variables:
  - name: task_description
    type: string
    required: true
    default: null
    description: The specific engineering problem or task to be solved
  - name: language_tech
    type: string
    required: true
    default: null
    description: Primary programming language or technology stack to use
  - name: context
    type: string
    required: false
    default: "No additional context provided"
    description: Additional context about the codebase, environment, or project
  - name: output_format
    type: string
    required: false
    default: "code_and_explanation"
    description: Desired response format (code_only, explanation_only, code_and_explanation, step_by_step)
  - name: complexity_level
    type: string
    required: false
    default: "intermediate"
    description: Target complexity level (beginner, intermediate, expert)
  - name: constraints
    type: list
    required: false
    default: []
    description: Specific constraints, requirements, or limitations to consider
  - name: timeframe
    type: string
    required: false
    default: "No time constraints"
    description: Any time-related constraints or deadlines
variable_syntax: "mustache"
composable: false
domain: engineering
quality: 8.9
tags: [engineering, code, development, task-execution, reusable]
tldr: "Structured template for executing engineering tasks with configurable language, complexity, and output format."
keywords: [engineering, development, coding, programming, task, execution, template]
density_score: null
---
# Engineering Task Execution Template

## Purpose

This template produces structured engineering task prompts for software development, debugging, architecture design, and technical problem-solving. Reuse scope: any engineering task requiring code implementation, technical analysis, or development guidance. Invoke once per engineering problem; vary task_description, language_tech, and complexity_level to produce distinct engineering prompts from the same mold.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| task_description | string | true | null | The specific engineering problem or task to be solved |
| language_tech | string | true | null | Primary programming language or technology stack to use |
| context | string | false | "No additional context provided" | Additional context about the codebase, environment, or project |
| output_format | string | false | "code_and_explanation" | Desired response format (code_only, explanation_only, code_and_explanation, step_by_step) |
| complexity_level | string | false | "intermediate" | Target complexity level (beginner, intermediate, expert) |
| constraints | list | false | [] | Specific constraints, requirements, or limitations to consider |
| timeframe | string | false | "No time constraints" | Any time-related constraints or deadlines |

## Template Body

```
You are an expert software engineer. Execute the following engineering task with precision and clarity.

**Task**: {{task_description}}

**Technology Stack**: {{language_tech}}

**Context**: {{context}}

**Complexity Level**: {{complexity_level}}

**Output Format**: {{output_format}}

**Constraints**: 
{{#constraints}}
- {{.}}
{{/constraints}}

**Timeframe**: {{timeframe}}

**Instructions**:
1. Analyze the task requirements thoroughly
2. Consider the specified technology stack and constraints
3. Provide a solution appropriate for {{complexity_level}} level
4. Format your response according to {{output_format}}
5. Include error handling and edge cases where relevant
6. Ensure code follows best practices for {{language_tech}}

**Expected Deliverables**:
- Clean, well-structured code (if applicable)
- Clear explanations of approach and decisions
- Testing considerations or sample tests
- Any setup or deployment instructions needed
- Performance and scalability considerations for {{complexity_level}} level

Focus on practical, production-ready solutions that address the core requirements within the given constraints.
```

## Quality Gates

| Gate | Status | Notes |
|------|--------|-------|
| H01 | PASS | Frontmatter parses as valid YAML with all required fields |
| H02 | PASS | ID `p03_pt_engineering_task_execution` matches namespace `p03_pt_*` |
| H03 | PASS | ID equals filename stem |
| H04 | PASS | Kind equals literal `prompt_template` |
| H05 | PASS | Quality field set to null for authoring |
| H06 | PASS | All required frontmatter fields present |
| H07 | PASS | Body contains {{variable}} placeholders |
| H08 | PASS | All variables in body are declared in Variables section |

## Examples

### Example 1: REST API Development

**Variables**:
```yaml
task_description: "Create a REST API for user management with CRUD operations"
language_tech: "Python FastAPI"
context: "Building a microservice for a larger e-commerce platform"
output_format: "code_and_explanation"
complexity_level: "intermediate"
constraints: ["Must include authentication", "PostgreSQL database", "Docker deployment"]
timeframe: "2-3 hours"
```

**Rendered Output**:
```
You are an expert software engineer. Execute the following engineering task with precision and clarity.

**Task**: Create a REST API for user management with CRUD operations

**Technology Stack**: Python FastAPI

**Context**: Building a microservice for a larger e-commerce platform

**Complexity Level**: intermediate

**Output Format**: code_and_explanation

**Constraints**: 
- Must include authentication
- PostgreSQL database
- Docker deployment

**Timeframe**: 2-3 hours

**Instructions**:
1. Analyze the task requirements thoroughly
2. Consider the specified technology stack and constraints
3. Provide a solution appropriate for intermediate level
4. Format your response according to code_and_explanation
5. Include error handling and edge cases where relevant
6. Ensure code follows best practices for Python FastAPI

**Expected Deliverables**:
- Clean, well-structured code (if applicable)
- Clear explanations of approach and decisions
- Testing considerations or sample tests
- Any setup or deployment instructions needed
- Performance and scalability considerations for intermediate level

Focus on practical, production-ready solutions that address the core requirements within the given constraints.
```