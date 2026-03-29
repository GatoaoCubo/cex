---
kind: output_template
id: bld_output_template_prompt_version
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a prompt_version artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: prompt_version
```yaml
id: p03_pv_{{slug}}
kind: prompt_version
pillar: P03
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}}}"
prompt_ref: "{{prompt_ref}}}}"
quality: null
tags: [prompt_version, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}}}"
metrics: "{{metrics}}}}"
ab_group: "{{ab_group}}}}"
parent_version: "{{parent_version}}}}"
status: "{{status}}}}"
model_tested: "{{model_tested}}}}"
```
## Overview
{{overview_content}}
## Prompt Snapshot
{{prompt_snapshot_content}}
## Metrics
{{metrics_content}}
## Lineage
{{lineage_content}}

