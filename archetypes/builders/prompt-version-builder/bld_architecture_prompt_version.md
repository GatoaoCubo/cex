---
kind: architecture
id: bld_architecture_prompt_version
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of prompt_version — inventory, dependencies, and architectural position
quality: 9.2
title: "Architecture Prompt Version"
version: "1.0.0"
author: n03_builder
tags: [prompt_version, builder, examples]
tldr: "Golden and anti-examples for prompt version construction, demonstrating ideal structure and common pitfalls."
domain: "prompt version construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - prompt-version-builder
  - p03_sp_prompt_version_builder
  - bld_examples_prompt_version
  - bld_output_template_prompt_version
  - p01_kc_prompt_version
  - bld_collaboration_prompt_version
  - bld_instruction_prompt_version
  - p10_lr_prompt_version_builder
  - bld_tools_prompt_version
  - p11_qg_prompt_version
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| prompt_ref | Reference to the prompt_template being versioned | prompt_version | required |
| version | Semantic version of this snapshot | prompt_version | required |
| author | Who created this version | prompt_version | required |
| metrics | Performance metrics for this version | prompt_version | optional |
| ab_group | A/B test group assignment (control, variant_a, variant_b) | prompt_version | optional |
| parent_version | Previous version this evolved from | prompt_version | optional |
| prompt_template | The mutable template this snapshots | P03 | upstream |
| eval | Evaluation results validating this version | P07 | downstream |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| prompt_ref | prompt_version | produces | Reference to the prompt_template being versioned |
| version | prompt_version | produces | Semantic version of this snapshot |
| author | prompt_version | produces | Who created this version |
| metrics | prompt_version | produces | Performance metrics for this version |
| ab_group | prompt_version | produces | A/B test group assignment (control, variant_a, variant_b) |
| parent_version | prompt_version | produces | Previous version this evolved from |
| prompt_template | P03 | depends | The mutable template this snapshots |
| eval | P07 | depends | Evaluation results validating this version |
## Boundary Table
| prompt_version IS | prompt_version IS NOT |
|-------------|----------------|
| Prompt version — immutable snapshot of a prompt at a point in time with metrics and lineage | prompt_template (P03 |
| Not prompt_template | prompt_template (P03 |
| Not mutable template) | mutable template) |
| Not system_prompt | system_prompt (P03 |
| Not agent identity) | agent identity) |
| Not action_prompt | action_prompt (P03 |
| Not task prompt) | task prompt) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | prompt_ref, version, author | Define the artifact's core parameters |
| optional | metrics, ab_group, parent_version | Extend with recommended fields |
| external | prompt_template, eval | Upstream/downstream connections |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_architecture_prompt_version
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-architecture-prompt-version.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[prompt-version-builder]] | upstream | 0.65 |
| [[p03_sp_prompt_version_builder]] | upstream | 0.57 |
| [[bld_examples_prompt_version]] | upstream | 0.48 |
| [[bld_output_template_prompt_version]] | upstream | 0.47 |
| [[p01_kc_prompt_version]] | upstream | 0.46 |
| [[bld_collaboration_prompt_version]] | downstream | 0.43 |
| [[bld_instruction_prompt_version]] | upstream | 0.42 |
| [[p10_lr_prompt_version_builder]] | downstream | 0.42 |
| [[bld_tools_prompt_version]] | upstream | 0.38 |
| [[p11_qg_prompt_version]] | downstream | 0.37 |
