---
id: n01_pt_intelligence_workflows
kind: prompt_template
pillar: P03
title: "Prompt Templates for N01 Intelligence Workflows"
version: "1.0.0"
created: "2026-03-31"
updated: "2026-03-31"
author: "N01_rebuild_8F"
quality: 9.1
tags: [prompt, template, n01, research, workflow]
tldr: "Provides standardized, machine-readable prompt templates to trigger the N01 agent's core research workflows: Literature Review, Comparative Analysis, and Trend Analysis."
variable_syntax: "handlebars" # {{variable}}
density_score: 0.94
related:
  - bld_schema_multimodal_prompt
  - n06_schema_brand_config
  - bld_schema_benchmark_suite
  - bld_schema_input_schema
  - examples_prompt_template_builder
  - bld_schema_faq_entry
  - bld_schema_prompt_optimizer
  - bld_schema_nps_survey
  - bld_schema_customer_segment
  - bld_schema_model_registry
---

## 1. PURPOSE
This artifact provides standardized, structured prompt templates for initiating the core workflows of the **N01 Research & Intelligence Nucleus**. Using these templates ensures that all necessary parameters are provided to the orchestration engine, allowing it to reliably select the correct workflow and execute the task with high precision.

## 2. TEMPLATE VARIABLES
| Variable               | Type         | Required | Description                                                                                             |
|------------------------|--------------|----------|---------------------------------------------------------------------------------------------------------|
| `research_type`        | String       | **Yes**  | The type of workflow to execute. Must be one of: `LITERATURE_REVIEW`, `COMPARATIVE_ANALYSIS`, `TREND_ANALYSIS`. |
| `primary_question`     | String       | **Yes**  | The central, high-level question the research must answer.                                              |
| `topic`                | String       | Varies   | The main subject or area of interest (for Literature Review, Trend Analysis).                           |
| `subjects`             | String Array | Varies   | A list of two or more items to be compared (for Comparative Analysis).                                  |
| `comparison_criteria`  | String Array | Varies   | The specific, objective criteria to use for comparison.                                                 |
| `time_horizon`         | String       | Varies   | The time period to focus on, e.g., "last 2 years", "2020-2025" (for Trend Analysis).                  |
| `data_sources`         | String Array | No       | A list of preferred data sources or document IDs to be used.                                            |
| `analytical_framework` | String       | No       | A specific framework to apply, e.g., "PESTLE", "Porter's Five Forces".                                  |

---

## 3. TEMPLATES

### **Template A: Literature Review**
Triggers a systematic review of literature on a given topic to answer a specific question.
```prompt
---
research_type: "LITERATURE_REVIEW"
topic: "{{topic}}"
primary_question: "{{primary_question}}"
{{#if data_sources}}
data_sources:
  {{#each data_sources}}- "{{this}}"
  {{/each}}
{{/if}}
---
```
**Example:**
```yaml
---
research_type: "LITERATURE_REVIEW"
topic: "Solid-State Batteries"
primary_question: "What are the primary technical obstacles preventing the mass commercialization of solid-state batteries as of early 2026?"
data_sources:
  - "doc_id:arxiv_2512.01234"
  - "doc_id:ieee_56789"
---
```

### **Template B: Comparative Analysis**
Triggers a head-to-head benchmark of two or more subjects against defined criteria.
```prompt
---
research_type: "COMPARATIVE_ANALYSIS"
primary_question: "How do the following subjects compare on the specified criteria?"
subjects:
  {{#each subjects}}- "{{this}}"
  {{/each}}
comparison_criteria:
  {{#each comparison_criteria}}- "{{this}}"
  {{/each}}
---
```
**Example:**
```yaml
---
research_type: "COMPARATIVE_ANALYSIS"
primary_question: "How do the leading open-source LLMs compare in terms of performance, architecture, and licensing?"
subjects:
  - "Llama 3 70B"
  - "Mistral Large"
  - "Jamba"
comparison_criteria:
  - "Reported MMLU Score"
  - "Model Architecture (e.g., MoE)"
  - "Context Window Size (tokens)"
  - "Commercial Use License Terms"
---
```

### **Template C: Trend Analysis**
Triggers an analysis of patterns, momentum, and future projections for a topic over a specific time horizon.
```prompt
---
research_type: "TREND_ANALYSIS"
topic: "{{topic}}"
primary_question: "{{primary_question}}"
time_horizon: "{{time_horizon}}"
{{#if analytical_framework}}
analytical_framework: "{{analytical_framework}}"
{{/if}}
---
```
**Example:**
```yaml
---
research_type: "TREND_ANALYSIS"
topic: "AI in Drug Discovery"
primary_question: "What is the investment trend and velocity for AI in drug discovery, and which sub-fields are seeing the most momentum?"
time_horizon: "2023-2026"
analytical_framework: "Kinetic Analysis"
---
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_multimodal_prompt]] | downstream | 0.25 |
| [[n06_schema_brand_config]] | downstream | 0.24 |
| [[bld_schema_benchmark_suite]] | downstream | 0.23 |
| [[bld_schema_input_schema]] | downstream | 0.23 |
| [[examples_prompt_template_builder]] | downstream | 0.23 |
| [[bld_schema_faq_entry]] | downstream | 0.23 |
| [[bld_schema_prompt_optimizer]] | downstream | 0.23 |
| [[bld_schema_nps_survey]] | downstream | 0.23 |
| [[bld_schema_customer_segment]] | downstream | 0.22 |
| [[bld_schema_model_registry]] | downstream | 0.22 |
