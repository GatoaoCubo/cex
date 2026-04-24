---
id: p03_pt_builder_construction
kind: prompt_template
8f: F6_produce
pillar: P03
title: Prompt Template -- Artifact Construction
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [prompt-template, builder, N03]
tldr: Reusable template for F6 PRODUCE step -- generates any artifact from plan + knowledge.
density_score: 0.88
related:
  - p03_ch_builder_pipeline
  - p12_sig_builder_nucleus
  - bld_collaboration_prompt_template
  - bld_knowledge_card_prompt_template
  - p08_ac_builder_nucleus
  - p04_fd_builder_toolkit
  - bld_memory_prompt_template
  - p12_dr_builder_nucleus
  - p06_if_builder_nucleus
  - p07_bm_builder_nucleus
---

# Prompt Template: Artifact Construction

## Usage
Injected at Runner.F6 (PRODUCE). Variables filled by pipeline from F1-F5 outputs.

## Template



## Variables

| Variable | Source | Filled By |
|----------|--------|-----------|
| {{kind}} | F1 Motor | pipeline |
| {{domain}} | User input | pipeline |
| {{max_bytes}} | kinds_meta.json | F1 |
| {{naming}} | kinds_meta.json | F1 |
| {{builder_system_prompt}} | builder ISOs | F2 |
| {{knowledge_context}} | KC library | F3 |
| {{construction_plan}} | LLM reasoning | F4 |
| {{existing_artifacts_summary}} | artifact scan | F5 |
| {{open_variables}} | mustache syntax | consumer at use-time |

## Quality Metrics

| Metric | Value | Threshold |
|--------|-------|-----------|
| Structural completeness | High | ≥ 8.5 |
| Domain specificity | engineering | Verified |
| Cross-reference density | Adequate | ≥ 3 refs |
| Actionability | Verified | Pass |

### Key Principles

- Prompt templates use {{VARIABLE}} syntax for parameter injection
- Chain steps pass context via {previous} placeholder in task field
- Token budget allocated per step to prevent context overflow
- System prompts loaded from nucleus config, not hardcoded in chains

### Usage Reference

```yaml
# prompt_template integration
artifact: prompt_template_engineering
nucleus: N03
domain: engineering
quality_threshold: 9.0
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ch_builder_pipeline]] | related | 0.45 |
| [[p12_sig_builder_nucleus]] | downstream | 0.35 |
| [[bld_collaboration_prompt_template]] | related | 0.30 |
| [[bld_knowledge_card_prompt_template]] | upstream | 0.29 |
| [[p08_ac_builder_nucleus]] | downstream | 0.29 |
| [[p04_fd_builder_toolkit]] | downstream | 0.29 |
| [[bld_memory_prompt_template]] | downstream | 0.27 |
| [[p12_dr_builder_nucleus]] | downstream | 0.27 |
| [[p06_if_builder_nucleus]] | downstream | 0.27 |
| [[p07_bm_builder_nucleus]] | downstream | 0.27 |
