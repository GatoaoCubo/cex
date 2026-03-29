---
id: p03_pt_research_nucleus
kind: prompt_template
pillar: P03
title: "Research Nucleus Template"
version: "1.0.0"
created: "2023-11-01"
updated: "2023-11-01"
author: "prompt-template-builder"
variables:
  - name: "research_topic"
    type: "string"
    required: true
    default: null
    description: "The central topic for the research inquiry"
  - name: "primary_research_question"
    type: "string"
    required: true
    default: null
    description: "The main question guiding the research"
  - name: "secondary_questions"
    type: "list"
    required: false
    default: []
    description: "Additional questions to complement the primary research question"
  - name: "target_audience"
    type: "string"
    required: false
    default: "general"
    description: "The intended audience for the research outputs"
variable_syntax: "mustache"
composable: false
domain: "research"
quality: null
tags: ["research", "inquiry", "framework"]
tldr: "A template to guide comprehensive research inquiries across different topics."
keywords: ["research", "inquiry", "template", "academic"]
density_score: null
---

# Research Nucleus Template
## Purpose
This template is designed to assist researchers in formulating comprehensive research inquiries tailored to their specific topics and audience. It enables the creation of structured prompts that guide research plans across various disciplines.

## Variables Table
| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| research_topic | string | true | null | The central topic for the research inquiry |
| primary_research_question | string | true | null | The main question guiding the research |
| secondary_questions | list | false | [] | Additional questions to complement the primary research question |
| target_audience | string | false | "general" | The intended audience for the research outputs |

## Template Body
---
This template is designed to assist researchers in formulating comprehensive research inquiries in the domain of {{research_topic}}.

Main Research Question: {{primary_research_question}}

Secondary Questions to Consider: 
{{#secondary_questions}}
- {{.}}
{{/secondary_questions}}

Target Audience: {{target_audience}}

The goal of this research is to explore and provide insights into {{research_topic}}, answering the key question: "{{primary_research_question}}" with the audience {{target_audience}} in mind.
```

## Quality Gates
| Gate | Status | Notes |
|---|---|---|
| H01 id pattern | PASS | `p03_pt_research_nucleus` matches `^p03_pt_[a-z][a-z0-9_]+$` |
| H02 required fields | PASS | All frontmatter required fields are present |
| H03 no undeclared vars | PASS | All `{{vars}}` in body are declared in variables list |
| H04 no unused vars | PASS | All declared variables appear in the template body |
| H05 size <= 8192 bytes | PASS | The template is well within size limits |
| H06 valid syntax tier | PASS | Using Mustache syntax effectively |

## Examples
### Filled Example
**Variables:**
```yaml
research_topic: "climate change"
primary_research_question: "What are the most effective strategies for reducing carbon emissions?"
secondary_questions:
  - "How do these strategies impact economic growth?"
  - "What technologies are essential for this reduction?"
target_audience: "policy makers"
```
**Rendered Output:**
```
This template is designed to assist researchers in formulating comprehensive research inquiries in the domain of climate change.

Main Research Question: What are the most effective strategies for reducing carbon emissions?

Secondary Questions to Consider: 
- How do these strategies impact economic growth?
- What technologies are essential for this reduction?

Target Audience: policy makers

The goal of this research is to explore and provide insights into climate change, answering the key question: "What are the most effective strategies for reducing carbon emissions?" with the audience policy makers in mind.
```