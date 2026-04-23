---
id: n00_chain_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Chain -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, chain, p03, n00, archetype, template]
density_score: 0.99
related:
  - bld_schema_chain
  - chain-builder
  - p01_kc_chain
  - bld_collaboration_chain
  - bld_examples_chain
  - p03_sp_chain_builder
  - bld_architecture_chain
  - p10_lr_chain_builder
  - p11_qg_chain
  - bld_schema_action_prompt
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A chain is a chained prompt sequence where the output of step A becomes the input of step B, enabling multi-step reasoning or data transformation pipelines. Each link in the chain is a discrete prompt or tool call, and the chain defines the dependency graph between them. The output is a structured workflow that produces a compounded artifact requiring sequential processing.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `chain` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| steps | list | yes | Ordered list of chain steps with input/output specs |
| topology | string | yes | linear, branching, or conditional |
| stop_condition | string | no | Condition that terminates the chain early |

## When to use
- When a task requires sequential LLM calls where each step depends on the prior output
- When building a multi-stage pipeline (e.g., research -> summarize -> format -> validate)
- When the output of one nucleus must be piped as context into another nucleus's prompt

## Builder
`archetypes/builders/chain-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind chain --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: chain_research_to_brief
kind: chain
pillar: P03
nucleus: n01
title: "Research to Intelligence Brief"
version: 1.0
quality: null
---
topology: linear
steps:
  - step: 1
    prompt: action_prompt/ap_competitor_scan
    output_key: raw_intel
  - step: 2
    prompt: action_prompt/ap_synthesize_brief
    input_key: raw_intel
```

## Related kinds
- `action_prompt` (P03) -- individual links in the chain
- `workflow` (P12) -- higher-level orchestration that may contain chains
- `planning_strategy` (P03) -- strategy that determines chain topology
- `reasoning_trace` (P03) -- captures intermediate chain reasoning

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_chain]] | downstream | 0.51 |
| [[chain-builder]] | related | 0.48 |
| [[p01_kc_chain]] | sibling | 0.46 |
| [[bld_collaboration_chain]] | downstream | 0.46 |
| [[bld_examples_chain]] | downstream | 0.44 |
| [[p03_sp_chain_builder]] | related | 0.43 |
| [[bld_architecture_chain]] | downstream | 0.41 |
| [[p10_lr_chain_builder]] | downstream | 0.41 |
| [[p11_qg_chain]] | downstream | 0.40 |
| [[bld_schema_action_prompt]] | downstream | 0.40 |
