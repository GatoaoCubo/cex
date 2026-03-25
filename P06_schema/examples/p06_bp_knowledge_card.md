---
id: p06_bp_knowledge_card
type: artifact_blueprint
lp: P06
description: "Blueprint for generating knowledge_card artifacts — defines shape, sections, limits"
format: yaml
version: 1.0.0
created: 2026-03-24
author: edison
quality: 9.0
tags: [blueprint, knowledge-card, artifact-generation, meta-template]
---

# Artifact Blueprint: knowledge_card

## Purpose
Defines the SHAPE an LLM must fill when generating a knowledge_card (P01). This is injected into the generation prompt as a CONSTRAIN — the LLM sees this and must conform.

## Shape Definition
```yaml
artifact: knowledge_card
lp: P01
max_bytes: 5120
density_min: 0.8
machine_format: yaml

frontmatter:
  required: [id, type, lp, domain, quality, tags]
  optional: [source, author, version, created]
  
sections:
  - name: Title
    format: "# {descriptive title}"
    required: true
  - name: Body  
    format: "Dense paragraphs, no filler. Every sentence carries information."
    required: true
    min_bytes: 200
  - name: Key Points
    format: "Bullet list of actionable insights"
    required: false
  - name: Sources
    format: "Links or references"
    required: false

constraints:
  - "Density >= 0.8 (information per byte)"
  - "No introductions like 'This document describes...'"
  - "No conclusions like 'In summary...'"
  - "Every sentence must teach something new"
  - "Prefer tables over paragraphs when comparing"
```

## Injection Pattern
```
Generate a knowledge_card following this blueprint:
{blueprint_yaml}

Topic: {{topic}}
Domain: {{domain}}
Sources: {{sources}}
```

## Validation
After generation, validate against P06.validation_schema and P06.validator rules. Blueprint compliance != quality — both gates must pass.

## Difference from prompt_template
A prompt_template (P03) defines HOW TO ASK the LLM.
An artifact_blueprint (P06) defines WHAT THE OUTPUT LOOKS LIKE.
They work together: prompt_template includes the blueprint as a constraint.
