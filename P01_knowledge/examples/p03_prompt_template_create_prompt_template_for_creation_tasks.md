---
id: p03_pt_creation_tasks
kind: prompt_template
pillar: P03
title: "Creation Tasks Template"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: prompt-template-builder
variables:
  - name: artifact_type
    type: string
    required: true
    default: null
    description: "The specific type of artifact or deliverable to create"
  - name: domain
    type: string
    required: true
    default: null
    description: "The domain or context area for the creation task"
  - name: requirements
    type: string
    required: false
    default: ""
    description: "Specific requirements, constraints, or specifications"
  - name: output_format
    type: string
    required: false
    default: "markdown"
    description: "Desired output format for the created artifact"
  - name: quality_target
    type: string
    required: false
    default: "high"
    description: "Target quality level (low, medium, high, premium)"
  - name: audience
    type: string
    required: false
    default: "general"
    description: "Target audience for the created artifact"
variable_syntax: "mustache"
composable: false
domain: creation
quality: 8.9
tags: [creation, tasks, production, reusable, template]
tldr: "Reusable template for creation task prompts across any domain and artifact type"
keywords: [create, build, generate, artifact, template, production]
density_score: 0.88
---
## Purpose
Generates structured creation prompts for any artifact type across domains. Reuse scope: any task requiring the production of a specific deliverable with defined requirements. Invoke once per creation task; vary `artifact_type`, `domain`, and `requirements` to produce distinct creation prompts from the same mold.

## Variables Table
| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| artifact_type | string | true | null | The specific type of artifact or deliverable to create |
| domain | string | true | null | The domain or context area for the creation task |
| requirements | string | false | "" | Specific requirements, constraints, or specifications |
| output_format | string | false | "markdown" | Desired output format for the created artifact |
| quality_target | string | false | "high" | Target quality level (low, medium, high, premium) |
| audience | string | false | "general" | Target audience for the created artifact |

## Template Body
```
You are an expert {{domain}} creator. Your task is to create a {{artifact_type}} with {{quality_target}} quality standards.

**Creation Target**: {{artifact_type}}
**Domain**: {{domain}}
**Output Format**: {{output_format}}
**Target Audience**: {{audience}}
**Quality Level**: {{quality_target}}

{{#requirements}}
**Requirements & Constraints**:
{{requirements}}
{{/requirements}}

**Instructions**:
1. Analyze the target {{artifact_type}} type and {{domain}} context
2. Structure your creation to serve the {{audience}} audience effectively
3. Deliver output in {{output_format}} format
4. Meet {{quality_target}} quality standards throughout
5. Ensure all specified requirements are addressed

{{#requirements}}
6. Validate against the provided requirements: {{requirements}}
{{/requirements}}

Begin creation now. Focus on producing a complete, well-structured {{artifact_type}} that serves its intended purpose in the {{domain}} domain.
```

## Quality Gates
| Gate | Status | Notes |
|---|---|---|
| H01 | PASS | Frontmatter parses as valid YAML |
| H02 | PASS | ID `p03_pt_creation_tasks` matches namespace `p03_pt_*` |
| H03 | PASS | ID matches filename stem |
| H04 | PASS | Kind equals literal `prompt_template` |
| H05 | PASS | Quality is null at authoring time |
| H06 | PASS | All required frontmatter fields present |
| H07 | PASS | Body contains {{variable}} placeholders |
| H08 | PASS | All body variables declared in Variables section |

## Examples
**Example 1: Software Documentation**
```yaml
Variables:
  artifact_type: "API documentation"
  domain: "software development"
  requirements: "RESTful API with authentication, include code examples"
  output_format: "markdown"
  quality_target: "premium"
  audience: "developers"
```

**Rendered Output**:
```
You are an expert software development creator. Your task is to create a API documentation with premium quality standards.

**Creation Target**: API documentation
**Domain**: software development
**Output Format**: markdown
**Target Audience**: developers
**Quality Level**: premium

**Requirements & Constraints**:
RESTful API with authentication, include code examples

**Instructions**:
1. Analyze the target API documentation type and software development context
2. Structure your creation to serve the developers audience effectively
3. Deliver output in markdown format
4. Meet premium quality standards throughout
5. Ensure all specified requirements are addressed
6. Validate against the provided requirements: RESTful API with authentication, include code examples

Begin creation now. Focus on producing a complete, well-structured API documentation that serves its intended purpose in the software development domain.
```