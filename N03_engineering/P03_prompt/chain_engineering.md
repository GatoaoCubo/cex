---
id: p03_ch_builder_pipeline
kind: chain
8f: F6_produce
pillar: P03
title: Prompt Chain -- Builder Pipeline
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [chain, builder, N03]
tldr: 4-step prompt chain -- classify, plan, build, validate.
density_score: 0.88
related:
  - p03_pt_builder_construction
  - p12_wf_builder_8f_pipeline
  - p11_qg_chain
  - p01_kc_chain
  - tpl_instruction
  - p10_lr_chain_builder
  - bld_examples_chain
  - bld_architecture_chain
  - p01_kc_prompt_engineering_best_practices
  - p12_sig_builder_nucleus
---

# Prompt Chain: Builder Pipeline

## Overview

4 LLM calls in the 8F pipeline. Steps 1-3 and 5 are deterministic.

## Step 1: CLASSIFY (F4 REASON)

    Given kind={{kind}}, constraints={{constraints}}, knowledge={{kc_summary}}:
    Plan sections, references, structure.
    Output 100-200 word construction plan.

Temperature: 0.3 | Max tokens: 500

## Step 2: BUILD (F6 PRODUCE)

    Using plan={{plan}}, tools={{tools}}, knowledge={{full_kc}}:
    Produce complete artifact with YAML frontmatter and structured body.
    Follow builder output template for {{kind}}.

Temperature: 0.7 | Max tokens: 4000

## Step 3: VALIDATE (F7 GOVERN)

    Check artifact against gates H01-H07:
    {{artifact_text}}
    Report: pass/fail per gate, overall score, issues list.

Temperature: 0.0 | Max tokens: 500 | Model: haiku

## Step 4: RETRY (if needed)

    Artifact failed these gates: {{issues}}
    Revise to fix specific issues. Keep what passed.

Temperature: 0.5 | Max tokens: 4000

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
# chain integration
artifact: chain_engineering
nucleus: N03
domain: engineering
quality_threshold: 9.0
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_pt_builder_construction]] | related | 0.48 |
| [[p12_wf_builder_8f_pipeline]] | downstream | 0.33 |
| [[p11_qg_chain]] | downstream | 0.32 |
| [[p01_kc_chain]] | related | 0.31 |
| [[tpl_instruction]] | related | 0.30 |
| [[p10_lr_chain_builder]] | downstream | 0.30 |
| [[bld_examples_chain]] | downstream | 0.28 |
| [[bld_architecture_chain]] | downstream | 0.28 |
| [[p01_kc_prompt_engineering_best_practices]] | upstream | 0.28 |
| [[p12_sig_builder_nucleus]] | downstream | 0.28 |
