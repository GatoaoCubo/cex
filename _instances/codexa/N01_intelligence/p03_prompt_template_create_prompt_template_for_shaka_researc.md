---
id: p03_pt_shaka_research_nucleus
kind: prompt_template
pillar: P03
title: "SHaKA Research Nucleus Prompt Template"
version: "1.0.0"
created: "2023-11-02"
updated: "2023-11-02"
author: "prompt-template-builder"
variables:
  - name: "research_question"
    type: "string"
    required: true
    default: null
    description: "The central query or problem statement to guide the research."
  - name: "data_source"
    type: "string"
    required: true
    default: null
    description: "The source or dataset from which data is drawn."
  - name: "methodology"
    type: "string"
    required: true
    default: null
    description: "The planned approach or research methods to be used."
  - name: "expected_outcome"
    type: "string"
    required: false
    default: "Insights and Recommendations"
    description: "Anticipated results or findings expected from the research."
  - name: "constraints"
    type: "list"
    required: false
    default: []
    description: "Important factors or limitations to consider during the research."
variable_syntax: "mustache"
composable: false
domain: "research"
quality: null
tags: [shaka, nucleus, research, prompts, template]
tldr: "Facilitate the creation of research queries in SHaKA Research Nucleus."
keywords: [research, prompt, template, nucleus, shaka, query]
density_score: null
---
# SHaKA Research Nucleus Prompt Template
## Purpose
This template is designed for creating dynamic research queries within the context of SHaKA Research Nucleus. It facilitates the formulation of structured prompts by incorporating variable inputs such as the research question, data source, and methodology, allowing for diverse use cases and adaptability to various research scenarios.
## Variables Table
| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| research_question | string | true | null | The central query or problem statement to guide the research. |
| data_source | string | true | null | The source or dataset from which data is drawn. |
| methodology | string | true | null | The planned approach or research methods to be used. |
| expected_outcome | string | false | Insights and Recommendations | Anticipated results or findings expected from the research. |
| constraints | list | false | [] | Important factors or limitations to consider during the research. |
## Template Body
---
You are conducting research within the SHaKA Research Nucleus. Your task is to formulate a clear and concise research prompt.

Research Question: {{research_question}}
Data Source: {{data_source}}
Methodology: {{methodology}}
Expected Outcome: {{expected_outcome}}
Constraints: {{constraints}}

Please ensure the research prompt addresses all variables and follows a structured approach suitable for a detailed investigation.
```
## Quality Gates
| Gate | Status | Notes |
|---|---|---|
| H01 id pattern | PASS | `p03_pt_shaka_research_nucleus` matches `^p03_pt_[a-z][a-z0-9_]+$` |
| H02 required fields | PASS | All frontmatter required fields are present |
| H03 no undeclared vars | PASS | All `{{vars}}` in the body declared in variables list |
| H04 no unused vars | PASS | All declared variables are used in the template body |
| H05 size <= 8192 bytes | PASS | The file size is well within the limit |
| H06 valid syntax tier | PASS | Uses Mustache syntax |
| H07 var fields complete | PASS | All variable fields are complete |
| H08 body non-empty | PASS | Template body is not empty |
## Examples
### Filled Example
**Variables:**
```yaml
research_question: "What are the impacts of climate change on Arctic biodiversity?"
data_source: "NASA climate datasets"
methodology: "Quantitative analysis"
expected_outcome: "Assessment of species adaptation strategies"
constraints: ["Time constraints", "Resource availability"]
```
**Rendered Output:**
```
You are conducting research within the SHaKA Research Nucleus. Your task is to formulate a clear and concise research prompt.

Research Question: What are the impacts of climate change on Arctic biodiversity?
Data Source: NASA climate datasets
Methodology: Quantitative analysis
Expected Outcome: Assessment of species adaptation strategies
Constraints: [Time constraints, Resource availability]

Please ensure the research prompt addresses all variables and follows a structured approach suitable for a detailed investigation.
```
```