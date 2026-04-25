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
tldr: "4-step LLM chain for 8F pipeline: CLASSIFY (F4, temp=0.3, 500tok), BUILD (F6, temp=0.7, 4000tok), VALIDATE (F7, temp=0.0, Haiku, 500tok), RETRY (conditional, temp=0.5). Steps 1-3 and 5 are deterministic; only these 4 are LLM calls."
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

## Token Budget Per Step

| Step | Input Tokens | Output Tokens | Model | Cost Driver |
|------|-------------|---------------|-------|-------------|
| CLASSIFY | ~2000 (constraints+KC summary) | 500 | Opus/Sonnet | Low -- planning only |
| BUILD | ~4000 (plan+full KC+tools) | 4000 | Opus/Sonnet | High -- artifact generation |
| VALIDATE | ~5000 (full artifact text) | 500 | Haiku | Low -- structural check |
| RETRY | ~6000 (artifact+issues) | 4000 | Same as BUILD | Conditional -- only on soft fail |

Total per artifact (no retry): ~12K tokens. With 1 retry: ~22K tokens.

## Step Context Passing

Each step receives the previous step's output as context:
- CLASSIFY output (plan) is injected as `{{construction_plan}}` into BUILD
- BUILD output (artifact text) is injected as `{{artifact_text}}` into VALIDATE
- VALIDATE output (issues list) is injected as `{{issues}}` into RETRY
- No step has access to raw user input -- only the Motor-resolved kind and constraints

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
