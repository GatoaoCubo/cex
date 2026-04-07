---
id: p03_pt_cf_course_outline
kind: prompt_template
pillar: P03
title: "Content Factory — Course Outline Template"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
variables:
  - name: BRAND_NAME
    type: string
    required: true
    default: null
    description: "Company or brand name"
  - name: BRAND_VOICE
    type: string
    required: true
    default: null
    description: "Brand tone descriptor"
  - name: CONTENT_TOPIC
    type: string
    required: true
    default: null
    description: "Broad course subject"
  - name: CONTENT_COURSE_TITLE
    type: string
    required: true
    default: null
    description: "Full course title"
  - name: TARGET_AUDIENCE
    type: string
    required: true
    default: null
    description: "Ideal student persona, level, goals"
  - name: CONTENT_TOTAL_DURATION
    type: string
    required: false
    default: "8h"
    description: "Total course hours — 2h, 4h, 8h, 20h, 40h"
  - name: CONTENT_MODULES_COUNT
    type: integer
    required: false
    default: 6
    description: "Number of modules to generate"
  - name: CONTENT_PREREQUISITES
    type: list
    required: false
    default: null
    description: "What the student must know before starting"
  - name: CONTENT_LEARNING_OUTCOMES
    type: list
    required: true
    default: null
    description: "3-6 high-level outcomes for the entire course"
variable_syntax: mustache
composable: true
domain: content_factory
quality: 9.1
tags: [prompt_template, course, outline, curriculum, content_factory, P03]
tldr: "Reusable mold for generating complete course structures with modules, lessons, dependencies, and duration"
keywords: [course outline, curriculum, modules, lessons, content factory, structure]
density_score: 0.89
---

# Course Outline Template

## Purpose
Generates a complete course structure from a high-level brief. The output maps modules to lessons with dependencies, estimated durations, and learning outcomes. Feeds into the Content Factory pipeline as the master blueprint — each lesson entry becomes an input to `p03_pt_cf_lesson_script` for detailed script generation.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| BRAND_NAME | string | yes | — | Company or brand name |
| BRAND_VOICE | string | yes | — | Tone descriptor |
| CONTENT_TOPIC | string | yes | — | Course subject |
| CONTENT_COURSE_TITLE | string | yes | — | Full course title |
| TARGET_AUDIENCE | string | yes | — | Student persona |
| CONTENT_TOTAL_DURATION | string | no | 8h | Total hours |
| CONTENT_MODULES_COUNT | integer | no | 6 | Module count |
| CONTENT_PREREQUISITES | list | no | — | Prior knowledge |
| CONTENT_LEARNING_OUTCOMES | list | yes | — | 3-6 outcomes |

## Template Body

```
You are a curriculum designer for {{BRAND_NAME}}. Write in a {{BRAND_VOICE}} tone.

COURSE: {{CONTENT_COURSE_TITLE}}
TOPIC: {{CONTENT_TOPIC}}
AUDIENCE: {{TARGET_AUDIENCE}}
TOTAL DURATION: {{CONTENT_TOTAL_DURATION}}
MODULES: {{CONTENT_MODULES_COUNT}}
PREREQUISITES: {{CONTENT_PREREQUISITES}}

Design a course that achieves these outcomes:
{{CONTENT_LEARNING_OUTCOMES}}

## OUTPUT FORMAT

### COURSE METADATA
- Title: {{CONTENT_COURSE_TITLE}}
- Subtitle: [One line value proposition]
- Duration: {{CONTENT_TOTAL_DURATION}}
- Level: [Beginner / Intermediate / Advanced]
- Prerequisites: {{CONTENT_PREREQUISITES}}

### LEARNING PATH
For each of the {{CONTENT_MODULES_COUNT}} modules:

#### Module [N]: [Module Title]
- **Duration**: [hours]
- **Objective**: [One sentence — what the student achieves]
- **Depends on**: [Module N-1 or "none"]
- **Lessons**:
  | # | Lesson Title | Duration | Type | Key Concepts |
  |---|-------------|----------|------|-------------|
  | 1 | [title] | [min] | lecture/demo/lab/quiz | [2-3 concepts] |
  | 2 | [title] | [min] | lecture/demo/lab/quiz | [2-3 concepts] |
- **Assessment**: [Quiz, project, or exercise that validates module objective]

### DEPENDENCY MAP
```text
Module 1 → Module 2 → Module 3
                    ↘ Module 4 → Module 5
Module 6 (capstone, depends on 3+5)
```

### OUTCOMES MAPPING
| Outcome | Covered in Modules | Assessed in |
|---------|-------------------|-------------|
| {{CONTENT_LEARNING_OUTCOMES[0]}} | [M1, M2] | [M2 quiz] |

## CONSTRAINTS
- Total lesson durations MUST sum to {{CONTENT_TOTAL_DURATION}} (+/- 10%)
- Each module has 3-6 lessons (never 1-2, never 7+)
- At least one lab/hands-on lesson per module
- Final module is always capstone/project-based
- Dependencies form a DAG — no circular references
- Match {{BRAND_VOICE}} tone in all descriptions
```

## Quality Gates

| Gate | Status | Notes |
|------|--------|-------|
| H01 | PASS | id matches ^p03_pt_[a-z][a-z0-9_]+$ |
| H02 | PASS | All required frontmatter fields present |
| H03 | PASS | All {{vars}} in body exist in variables list |
| H04 | PASS | All variables in list appear in template body |
| H05 | PASS | File size < 8192 bytes |
| H06 | PASS | variable_syntax is mustache consistently |

## Examples

### Example 1: 8h course on AI agents
Variables:
```yaml
BRAND_NAME: "AgentSchool"
BRAND_VOICE: "technical-casual"
CONTENT_TOPIC: "Building AI agents with LLMs"
CONTENT_COURSE_TITLE: "AI Agents from Zero to Production"
TARGET_AUDIENCE: "Python developers with basic LLM API experience"
CONTENT_TOTAL_DURATION: "8h"
CONTENT_MODULES_COUNT: 5
CONTENT_PREREQUISITES:
  - "Python 3.10+"
  - "Basic REST API usage"
  - "Used ChatGPT or Claude API at least once"
CONTENT_LEARNING_OUTCOMES:
  - "Design a multi-tool agent architecture"
  - "Implement tool calling with structured outputs"
  - "Build a RAG pipeline for agent memory"
  - "Deploy an agent with monitoring and guardrails"
```
