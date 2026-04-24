---
id: "p01_fse_{{TOPIC_SLUG}}"
kind: few_shot_example
8f: F3_inject
pillar: P01
version: 1.0.0
title: Template - Few Shot Example
tags: [template, few-shot, example, prompt, icl]
tldr: Input-output pair for in-context learning. Shows LLM what good output looks like.
quality: 9.0
updated: "2026-04-07"
domain: "knowledge management"
author: n04_knowledge
created: "2026-04-07"
density_score: 0.93
related:
  - few-shot-example-builder
  - p01_kc_few_shot_example
  - bld_collaboration_few_shot_example
  - bld_instruction_few_shot_example
  - bld_knowledge_card_few_shot_example
  - bld_examples_few_shot_example
  - bld_instruction_golden_test
  - p10_lr_few_shot_example_builder
  - p03_sp_few_shot_example_builder
  - bld_output_template_few_shot_example
---

# Few Shot Example: [NAME]

## Purpose
[WHAT this few_shot_example does]
## Schema
```yaml
target_kind: [WHAT_KIND_THIS_EXEMPLIFIES]
input: "[SAMPLE_INPUT]"
output: "[EXPECTED_OUTPUT]"
```
## Example Pair
### Input
```
[NATURAL_LANGUAGE_REQUEST]
```
### Expected Output
```
[COMPLETE_ARTIFACT — full valid output with frontmatter]
```
## Selection Criteria
| Criterion | Requirement |
|-----------|-------------|
| Relevance | Same kind as target |
| Quality | Score >= 8.5 |
| Diversity | Cover different use cases |
| Size | <= 2000 tokens (context budget) |
## Usage in 8F
Injected during F3 (INJECT). 2-3 examples per kind is optimal.
## Quality Gate
1. [ ] Input is natural language
2. [ ] Output is a complete valid artifact
3. [ ] Output passes F7 gates
4. [ ] Example is representative of common use

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `few_shot_example` |
| Pillar | P01 |
| Domain | knowledge management |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[few-shot-example-builder]] | related | 0.34 |
| [[p01_kc_few_shot_example]] | related | 0.29 |
| [[bld_collaboration_few_shot_example]] | downstream | 0.28 |
| [[bld_instruction_few_shot_example]] | downstream | 0.28 |
| [[bld_knowledge_card_few_shot_example]] | related | 0.27 |
| [[bld_examples_few_shot_example]] | downstream | 0.27 |
| [[bld_instruction_golden_test]] | downstream | 0.26 |
| [[p10_lr_few_shot_example_builder]] | downstream | 0.25 |
| [[p03_sp_few_shot_example_builder]] | downstream | 0.25 |
| [[bld_output_template_few_shot_example]] | downstream | 0.23 |
