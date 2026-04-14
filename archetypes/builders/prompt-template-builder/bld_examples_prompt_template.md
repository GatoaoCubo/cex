---
id: examples_prompt_template_builder
kind: examples
pillar: P07
llm_function: GOVERN
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [examples, prompt-template, P03, golden, anti-example]
quality: 9.1
title: "Examples Prompt Template"
tldr: "Golden and anti-examples for prompt template construction, demonstrating ideal structure and common pitfalls."
density_score: 0.90
---

# Examples — prompt-template-builder
## Golden Example
A complete, valid `prompt_template` artifact with 19+ fields.
```yaml
id: p03_pt_knowledge_card_production
kind: prompt_template
pillar: P03
title: "Knowledge Card Production Template"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: knowledge-engine
variables:
  - name: topic
    type: string
    required: true
    default: null
    description: The subject or concept the knowledge card will cover
  - name: domain
    type: string
    required: true
    default: null
    description: The knowledge domain (e.g., machine_learning, finance, biology)
  - name: audience
    type: string
    required: false
    default: "intermediate"
    description: Target reader level (beginner, intermediate, expert)
  - name: max_sections
    type: integer
    required: false
    default: 5
    description: Maximum number of body sections to generate
  - name: include_examples
    type: boolean
    required: false
    default: true
    description: Whether to include concrete examples in each section
  - name: source_refs
    type: list
    required: false
    default: []
    description: List of source URLs or citation keys to incorporate
variable_syntax: "mustache"
composable: false
domain: knowledge
quality: 9.0
tags: [knowledge-card, pytha, production, parameterized]
tldr: "Generates a structured knowledge card for any topic and domain with configurable depth."
keywords: [knowledge, card, synthesis, structured, reusable, topic]
density_score: 0.87
# Knowledge Card Production Template
## Purpose
Produces a structured knowledge card for any topic within a specified domain. Reuse scope: any subject requiring a dense, well-organized reference document. Invoke once per topic; vary `topic`, `domain`, and `audience` to produce distinct cards from the same mold.
## Variables Table
| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| topic | string | true | null | The subject or concept the knowledge card will cover |
| domain | string | true | null | The knowledge domain (e.g., machine_learning, finance) |
| audience | string | false | "intermediate" | Target reader level (beginner, intermediate, expert) |
| max_sections | integer | false | 5 | Maximum number of body sections to generate |
| include_examples | boolean | false | true | Whether to include concrete examples in each section |
| source_refs | list | false | [] | List of source URLs or citation keys to incorporate |
## Template Body
```
You are a knowledge synthesis expert. Produce a knowledge card for the following topic.
Topic: `{{topic}}`
Domain: `{{domain}}`
Audience level: `{{audience}}`
Maximum sections: `{{max_sections}}`
Include examples: `{{include_examples}}`
Source references: `{{source_refs}}`
Structure your output as follows:
1. TLDR (1 sentence)
2. Core Definition (2-3 sentences, precise, domain-apownte)
3. Key Concepts (up to `{{max_sections}}` bullet points)
4. Relationships (how `{{topic}}` connects to adjacent concepts in `{{domain}}`)
5. Common Misconceptions (2-3 items, audience-calibrated for `{{audience}}`)
{{#include_examples}}
6. Concrete Examples (2-3 examples grounded in `{{domain}}`)
{{/include_examples}}
7. References: `{{source_refs}}`
Calibrate terminology and depth for a `{{audience}}`-level reader in `{{domain}}`.
```
## Quality Gates
| Gate | Status | Notes |
|---|---|---|
| H01 id pattern | PASS | `p03_pt_knowledge_card_production` matches `^p03_pt_[a-z][a-z0-9_]+$` |
| H02 required fields | PASS | id, kind, title, variables, quality all present |
| H03 no undeclared vars | PASS | All `{{vars}}` in body declared in variables list |
| H04 no unused vars | PASS | All 6 declared variables appear in template body |
| H05 size <= 8192 bytes | PASS | ~1.8KB |
| H06 valid syntax tier | PASS | variable_syntax: mustache |
