---
id: p03_pt_creation_tasks
kind: prompt_template
pillar: P03
title: "Creation Tasks Prompt Template"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: prompt-template-builder
variables:
  - name: artifact_type
    type: string
    required: true
    default: null
    description: The type of artifact to create (e.g., article, code, design, strategy)
  - name: topic
    type: string
    required: true
    default: null
    description: The specific subject or theme for the creation task
  - name: audience
    type: string
    required: false
    default: "general"
    description: Target audience level (beginner, intermediate, expert, general)
  - name: quality_level
    type: string
    required: false
    default: "professional"
    description: Expected quality standard (draft, professional, expert, publication-ready)
  - name: domain
    type: string
    required: true
    default: null
    description: The knowledge domain or industry context
  - name: constraints
    type: list
    required: false
    default: []
    description: Specific limitations, requirements, or guidelines to follow
  - name: output_format
    type: string
    required: false
    default: "structured"
    description: Desired output structure (structured, narrative, bullet-points, technical)
  - name: length_target
    type: string
    required: false
    default: "medium"
    description: Target length or scope (brief, medium, comprehensive, detailed)
variable_syntax: "mustache"
composable: false
domain: creation
quality: 9.0
tags: [creation, task-generation, prompt-template, reusable, parameterized]
tldr: "Reusable template for generating creation tasks across different domains and artifact types"
keywords: [creation, generation, task, artifact, domain, quality, structured]
density_score: null
---
# Creation Tasks Prompt Template

## Purpose

Generates structured creation tasks for any type of artifact across different domains and quality levels. This template serves as a reusable mold for commissioning creative work, whether writing, coding, designing, or strategic planning. Invoke once per creation request; vary the artifact type, topic, and domain to produce distinct creation briefs from the same template structure.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| artifact_type | string | true | null | The type of artifact to create (e.g., article, code, design, strategy) |
| topic | string | true | null | The specific subject or theme for the creation task |
| audience | string | false | "general" | Target audience level (beginner, intermediate, expert, general) |
| quality_level | string | false | "professional" | Expected quality standard (draft, professional, expert, publication-ready) |
| domain | string | true | null | The knowledge domain or industry context |
| constraints | list | false | [] | Specific limitations, requirements, or guidelines to follow |
| output_format | string | false | "structured" | Desired output structure (structured, narrative, bullet-points, technical) |
| length_target | string | false | "medium" | Target length or scope (brief, medium, comprehensive, detailed) |

## Template Body

```
You are tasked with creating a {{artifact_type}} on the topic of {{topic}}.

**Context & Requirements:**
- Domain: {{domain}}
- Target Audience: {{audience}}
- Quality Standard: {{quality_level}}
- Output Format: {{output_format}}
- Length/Scope: {{length_target}}

**Specific Guidelines:**
{{#constraints}}
- {{.}}
{{/constraints}}

**Deliverable:**
Create a {{quality_level}}-grade {{artifact_type}} that addresses {{topic}} for a {{audience}} audience in the {{domain}} domain. Structure your output in {{output_format}} format, targeting {{length_target}} scope.

**Success Criteria:**
1. Content accuracy and relevance to {{topic}}
2. Appropriate depth for {{audience}} level
3. Adherence to {{quality_level}} standards
4. Clear organization using {{output_format}} structure
5. Scope alignment with {{length_target}} target
{{#constraints}}
6. Compliance with specified constraints
{{/constraints}}

Begin creation now.
```

## Quality Gates

| Gate | Status | Notes |
|------|--------|-------|
| H01 | PASS | Frontmatter parses as valid YAML |
| H02 | PASS | `id` matches `p03_pt_creation_tasks` pattern |
| H03 | PASS | `id` equals filename stem |
| H04 | PASS | `kind` equals `prompt_template` |
| H05 | PASS | `quality` is null at authoring time |
| H06 | PASS | All required frontmatter fields present |
| H07 | PASS | Body contains {{variable}} placeholders |
| H08 | PASS | All body variables declared in Variables section |
| H09 | PASS | Template uses consistent mustache syntax |

## Examples

### Example 1: Technical Article Creation

**Variables:**
```yaml
artifact_type: "technical article"
topic: "microservices architecture patterns"
audience: "intermediate"
quality_level: "professional"
domain: "software engineering"
constraints: 
  - "Include code examples"
  - "Reference current industry standards"
  - "Maximum 3000 words"
output_format: "structured"
length_target: "comprehensive"
```

**Rendered Output:**
```
You are tasked with creating a technical article on the topic of microservices architecture patterns.

**Context & Requirements:**
- Domain: software engineering
- Target Audience: intermediate
- Quality Standard: professional
- Output Format: structured
- Length/Scope: comprehensive

**Specific Guidelines:**
- Include code examples
- Reference current industry standards
- Maximum 3000 words

**Deliverable:**
Create a professional-grade technical article that addresses microservices architecture patterns for an intermediate audience in the software engineering domain. Structure your output in structured format, targeting comprehensive scope.

**Success Criteria:**
1. Content accuracy and relevance to microservices architecture patterns
2. Appropriate depth for intermediate level
3. Adherence to professional standards
4. Clear organization using structured structure
5. Scope alignment with comprehensive target
6. Compliance with specified constraints

Begin creation now.
```

### Example 2: Marketing Strategy Brief

**Variables:**
```yaml
artifact_type: "marketing strategy"
topic: "B2B SaaS customer acquisition"
audience: "expert"
quality_level: "publication-ready"
domain: "digital marketing"
constraints: 
  - "Focus on enterprise clients"
  - "Include budget considerations"
output_format: "bullet-points"
length_target: "medium"
```

**Rendered Output:**
```
You are tasked with creating a marketing strategy on the topic of B2B SaaS customer acquisition.

**Context & Requirements:**
- Domain: digital marketing
- Target Audience: expert
- Quality Standard: publication-ready
- Output Format: bullet-points
- Length/Scope: medium

**Specific Guidelines:**
- Focus on enterprise clients
- Include budget considerations

**Deliverable:**
Create a publication-ready-grade marketing strategy that addresses B2B SaaS customer acquisition for an expert audience in the digital marketing domain. Structure your output in bullet-points format, targeting medium scope.

**Success Criteria:**
1. Content accuracy and relevance to B2B SaaS customer acquisition
2. Appropriate depth for expert level
3. Adherence to publication-ready standards
4. Clear organization using bullet-points structure
5. Scope alignment with medium target
6. Compliance with specified constraints

Begin creation now.
```