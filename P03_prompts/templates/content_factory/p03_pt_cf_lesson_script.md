---
id: p03_pt_cf_lesson_script
kind: prompt_template
pillar: P03
title: "Content Factory — Lesson Script Template"
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
    description: "Lesson subject"
  - name: CONTENT_MODULE_TITLE
    type: string
    required: true
    default: null
    description: "Parent module this lesson belongs to"
  - name: CONTENT_LEARNING_OBJECTIVES
    type: list
    required: true
    default: null
    description: "2-4 specific things the student will be able to do after this lesson"
  - name: CONTENT_KEY_CONCEPTS
    type: list
    required: true
    default: null
    description: "Core concepts to teach"
  - name: LESSON_DURATION
    type: string
    required: false
    default: "15min"
    description: "Target lesson length — 5min, 10min, 15min, 30min"
  - name: TARGET_AUDIENCE
    type: string
    required: true
    default: null
    description: "Student persona and prior knowledge level"
  - name: CONTENT_EXERCISES
    type: list
    required: false
    default: null
    description: "Practice exercises or activities to include"
variable_syntax: mustache
composable: true
domain: content_factory
quality: null
tags: [prompt_template, lesson, script, course, content_factory, P03]
tldr: "Reusable mold for generating lesson scripts with objectives, teach, practice, recap structure"
keywords: [lesson script, aula, curso, module, teaching, content factory]
density_score: 0.90
---

# Lesson Script Template

## Purpose
Generates a complete lesson script for a course module. The output follows a pedagogical structure: objectives-teach-practice-recap with clear transitions. Designed to feed into slide deck generation, TTS narration, and video assembly in the Content Factory pipeline.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| BRAND_NAME | string | yes | — | Company or brand name |
| BRAND_VOICE | string | yes | — | Tone descriptor |
| CONTENT_TOPIC | string | yes | — | Lesson subject |
| CONTENT_MODULE_TITLE | string | yes | — | Parent module title |
| CONTENT_LEARNING_OBJECTIVES | list | yes | — | 2-4 outcomes |
| CONTENT_KEY_CONCEPTS | list | yes | — | Core concepts |
| LESSON_DURATION | string | no | 15min | Target length |
| TARGET_AUDIENCE | string | yes | — | Student persona |
| CONTENT_EXERCISES | list | no | — | Practice activities |

## Template Body

```
You are an instructional designer for {{BRAND_NAME}}. Write in a {{BRAND_VOICE}} tone.

MODULE: {{CONTENT_MODULE_TITLE}}
LESSON TOPIC: {{CONTENT_TOPIC}}
AUDIENCE: {{TARGET_AUDIENCE}}
DURATION: {{LESSON_DURATION}}

Create a lesson script teaching these concepts:
{{CONTENT_KEY_CONCEPTS}}

Students should achieve these objectives:
{{CONTENT_LEARNING_OBJECTIVES}}

## OUTPUT FORMAT

### OPENING (10% of duration)
**Hook**: One sentence that connects the topic to a real problem the student faces.
**Preview**: "By the end of this lesson, you will be able to: [restate {{CONTENT_LEARNING_OBJECTIVES}} in plain language]"
**Context**: One sentence connecting this to {{CONTENT_MODULE_TITLE}}.
TIMING: [minutes]

### TEACH (50% of duration)
For EACH concept in {{CONTENT_KEY_CONCEPTS}}:

**[Concept Name]**
- Explain: Define the concept in simple terms (max 3 sentences)
- Illustrate: One concrete example or analogy
- Connect: How it relates to the previous concept
- Visual cue: [Suggested slide or visual]
TIMING: [minutes per concept]

### PRACTICE (25% of duration)
Exercises: {{CONTENT_EXERCISES}}
For each exercise:
- Instructions (what the student does)
- Expected outcome (what success looks like)
- Common mistakes to watch for
TIMING: [minutes]

### RECAP (15% of duration)
- Summarize each objective from {{CONTENT_LEARNING_OBJECTIVES}} in one sentence
- Bridge: "In the next lesson, we will..."
- Quick self-check: 2 yes/no questions the student can answer to verify understanding
TIMING: [minutes]

## CONSTRAINTS
- Total duration MUST match {{LESSON_DURATION}} (+/- 10%)
- One concept per teaching segment — no concept stacking
- Use second person ("you") throughout for engagement
- Include [SLIDE: description] cues for visual pairing
- Match {{BRAND_VOICE}} tone — professional but approachable
- Jargon requires inline definition on first use
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

### Example 1: 15min lesson on API authentication
Variables:
```yaml
BRAND_NAME: "DevAcademy"
BRAND_VOICE: "technical-friendly"
CONTENT_TOPIC: "OAuth 2.0 Authorization Code Flow"
CONTENT_MODULE_TITLE: "Module 3: API Security"
CONTENT_LEARNING_OBJECTIVES:
  - "Explain the 4 steps of Authorization Code Flow"
  - "Implement a token exchange in Python"
  - "Identify when to use Auth Code vs Client Credentials"
CONTENT_KEY_CONCEPTS:
  - "Authorization vs Authentication"
  - "The 4-step OAuth dance"
  - "Token exchange and refresh"
LESSON_DURATION: "15min"
TARGET_AUDIENCE: "Junior developers with basic REST API knowledge"
CONTENT_EXERCISES:
  - "Trace the OAuth flow for a sample app diagram"
  - "Write a Python token exchange using requests library"
```
