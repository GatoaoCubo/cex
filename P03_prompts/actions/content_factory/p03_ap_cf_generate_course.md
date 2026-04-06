---
id: p03_ap_cf_generate_course
kind: action_prompt
pillar: P03
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Generate Complete Course from Topic"
action: "Generate a structured online course with modules, lessons, and assessments from a topic and audience definition"
input_required:
  - "topic: string — subject matter for the course"
  - "audience: string — target learner profile (level, goals)"
  - "modules_count: integer — number of modules (default 5)"
  - "brand_config: object — {{BRAND_*}} variables for voice and identity"
output_expected: "Structured course outline with modules, lessons, scripts, quiz questions, and Hotmart-ready metadata"
purpose: "Enable one-command course generation that feeds directly into the Hotmart publish workflow"
steps_count: 5
timeout: "120s"
edge_cases:
  - "Topic too broad (e.g. 'marketing') — narrow by audience and add scope constraint"
  - "modules_count exceeds 12 — split into multi-part course series"
  - "No audience specified — default to 'iniciante, profissional brasileiro 25-40'"
constraints:
  - "Do NOT generate video/audio assets — output is text structure only"
  - "Do NOT set pricing — that is N06 Commercial domain"
  - "All text output in pt-BR unless brand_config.language overrides"
domain: "content_factory"
quality: null
tags: [action_prompt, content_factory, course, education, hotmart]
tldr: "Generate structured course (modules + lessons + quizzes) from topic and audience, ready for Hotmart publish workflow"
density_score: 0.91
---

## Context
Content Factory needs to produce complete online courses autonomously. This action prompt
takes a topic, audience, and module count, then generates the full course structure including
lesson scripts, assessments, and platform metadata.
Purpose: bridge the gap between a course idea and a publish-ready structure for Hotmart.

## Input
| Item | Type | Format | Required |
|------|------|--------|----------|
| topic | string | Free text, 3-100 chars | YES |
| audience | string | Learner profile description | YES |
| modules_count | integer | 3-12 | NO (default 5) |
| brand_config | object | {{BRAND_*}} YAML variables | YES |

## Execution
1. Analyze topic scope and audience level to determine depth and vocabulary
2. Generate module outline with progressive difficulty (beginner → advanced)
3. For each module, produce 3-5 lessons with: title, objective, script (500-800 words), key takeaways
4. Generate 5 quiz questions per module (multiple choice, 4 options each)
5. Compile Hotmart metadata: course title, description, category, tags, prerequisite text

## Output
Format: Markdown + YAML frontmatter
Structure:
```yaml
course:
  title: "{{course_title}}"
  modules:
    - name: "Módulo 1: {{name}}"
      lessons:
        - title: "{{lesson_title}}"
          script: "{{500-800 words}}"
          takeaways: ["{{key1}}", "{{key2}}"]
      quiz: [{question: "...", options: [...], correct: 0}]
  hotmart_meta:
    category: "{{category}}"
    tags: ["{{tag1}}", "{{tag2}}"]
```

## Validation
- All modules present with correct count matching modules_count
- Each lesson has script between 500-800 words
- Each module has exactly 5 quiz questions with valid correct index
- Edge case: broad topic has been narrowed with explicit scope statement
- Brand voice from brand_config applied to all scripts

## References
- wf_cf_publish_hotmart (downstream workflow)
- brand_config.yaml (voice injection)
