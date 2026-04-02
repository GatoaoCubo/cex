---
id: p03_pt_creation_tasks
kind: prompt_template
pillar: P03
title: "Creation Task Template"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: prompt-template-builder
variables:
  - name: task_type
    type: string
    required: true
    default: null
    description: The specific type of thing to create (e.g., document, software, design, strategy)
  - name: domain
    type: string
    required: true
    default: null
    description: The field or area of expertise (e.g., marketing, technology, education, finance)
  - name: constraints
    type: list
    required: false
    default: []
    description: Any limitations or restrictions to consider (time, budget, technical, regulatory)
  - name: audience
    type: string
    required: false
    default: "general"
    description: Target audience or user group (beginner, expert, stakeholder, customer)
  - name: output_format
    type: string
    required: false
    default: "structured"
    description: Desired format of the deliverable (structured, visual, narrative, technical)
  - name: requirements
    type: list
    required: false
    default: []
    description: Specific functional or non-functional requirements to fulfill
  - name: success_criteria
    type: list
    required: false
    default: []
    description: Measurable criteria that define successful completion
variable_syntax: "mustache"
composable: false
domain: creation
quality: 9.2
tags: [prompt-template, creation, tasks, reusable, parameterized]
tldr: "Generates structured creation prompts for any deliverable type with configurable domain, constraints, and success criteria."
keywords: [creation, tasks, deliverable, template, structured, requirements]
density_score: 0.89
---
# Creation Task Template

## Purpose

Produces a structured creation prompt for any type of deliverable across different domains. Reuse scope: any situation requiring the creation of new artifacts, documents, software, designs, or strategies. Invoke once per creation task; vary `task_type`, `domain`, and `constraints` to produce distinct creation prompts from the same mold.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| task_type | string | true | null | The specific type of thing to create (e.g., document, software, design, strategy) |
| domain | string | true | null | The field or area of expertise (e.g., marketing, technology, education, finance) |
| constraints | list | false | [] | Any limitations or restrictions to consider (time, budget, technical, regulatory) |
| audience | string | false | "general" | Target audience or user group (beginner, expert, stakeholder, customer) |
| output_format | string | false | "structured" | Desired format of the deliverable (structured, visual, narrative, technical) |
| requirements | list | false | [] | Specific functional or non-functional requirements to fulfill |
| success_criteria | list | false | [] | Measurable criteria that define successful completion |

## Template Body

```
You are an expert {{domain}} professional. Create a {{task_type}} that meets the following specifications.

**Creation Target:**
Type: {{task_type}}
Domain: {{domain}}
Format: {{output_format}}
Audience: {{audience}}

**Constraints:**
{{#constraints}}
- {{.}}
{{/constraints}}
{{^constraints}}
- No specific constraints provided
{{/constraints}}

**Requirements:**
{{#requirements}}
- {{.}}
{{/requirements}}
{{^requirements}}
- Follow industry best practices for {{domain}}
{{/requirements}}

**Success Criteria:**
{{#success_criteria}}
- {{.}}
{{/success_criteria}}
{{^success_criteria}}
- Deliverable is complete, functional, and meets {{audience}} needs
{{/success_criteria}}

**Instructions:**
1. Analyze the requirements and constraints to understand the scope
2. Structure your approach based on {{domain}} best practices
3. Create the {{task_type}} in {{output_format}} format
4. Optimize for the {{audience}} level
5. Validate against success criteria before delivery

Begin creation now:
```

## Quality Gates

| Gate | Status | Notes |
|------|--------|--------|
| H01 | PASS | Frontmatter parses as valid YAML |
| H02 | PASS | `id` matches `p03_pt_creation_tasks` pattern |
| H03 | PASS | `id` equals filename stem |
| H04 | PASS | `kind` equals `prompt_template` |
| H05 | PASS | `quality` is null at authoring time |
| H06 | PASS | All required frontmatter fields present |
| H07 | PASS | Body contains multiple `{{variable}}` placeholders |
| H08 | PASS | All body variables declared in Variables section |
| H09 | PASS | Injection point implied as `user` turn |

## Examples

### Example 1: Software Creation Task

**Variables:**
```yaml
task_type: "REST API"
domain: "software engineering"
constraints: ["Python FastAPI framework", "PostgreSQL database", "Under 2 weeks development"]
audience: "technical team"
output_format: "structured"
requirements: ["Authentication system", "CRUD operations", "API documentation", "Unit tests"]
success_criteria: ["All endpoints functional", "Test coverage >80%", "Documentation complete"]
```

**Rendered Output:**
```
You are an expert software engineering professional. Create a REST API that meets the following specifications.

**Creation Target:**
Type: REST API
Domain: software engineering
Format: structured
Audience: technical team

**Constraints:**
- Python FastAPI framework
- PostgreSQL database
- Under 2 weeks development

**Requirements:**
- Authentication system
- CRUD operations
- API documentation
- Unit tests

**Success Criteria:**
- All endpoints functional
- Test coverage >80%
- Documentation complete

**Instructions:**
1. Analyze the requirements and constraints to understand the scope
2. Structure your approach based on software engineering best practices
3. Create the REST API in structured format
4. Optimize for the technical team level
5. Validate against success criteria before delivery

Begin creation now:
```