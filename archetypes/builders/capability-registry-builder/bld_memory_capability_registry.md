---
kind: learning_record
id: p10_lr_capability_registry_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for capability_registry construction
quality: 8.8
title: "Learning Record Capability Registry"
version: "1.0.0"
author: n04_wave8
tags: [capability_registry, builder, learning_record, agent-discovery]
tldr: "Learned patterns and pitfalls for capability_registry construction"
domain: "capability_registry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_capability_registry
  - bld_instruction_capability_registry
  - p03_sp_capability_registry_builder
  - capability-registry-builder
  - bld_knowledge_card_capability_registry
  - bld_schema_capability_registry
  - bld_output_template_capability_registry
  - bld_config_capability_registry
  - bld_tools_capability_registry
  - spec_infinite_bootstrap_loop
---

## Observation
Registry entries with all 8 required fields (capability_name, provider_agent, input_schema, output_schema, cost_tokens, quality_baseline, availability, keyword_index) produce 2-3x higher dispatch precision than partial entries. The most common omission is keyword_index, which prevents TF-IDF-based retrieval from surfacing the agent.

## Pattern
Three-layer indexing (builder_sub_agents | nucleus_domain_agents | nucleus_cards) with separate sections per layer prevents confusion between invocation paths. Builder sub-agents are invoked as Claude Code sub-agents; nucleus domain agents are invoked via dispatch.sh; nucleus cards describe the nucleus itself. Mixing them in one flat list causes routing errors.

## Evidence
In the CEX WAVE6/WAVE7 grid cycles, orchestrators that used flat agent lists dispatched to wrong nuclei ~20% of the time. Introducing the three-layer structure reduced misrouting to <5% in WAVE8 planning sessions.

## Recommendations
- Always validate `provider_agent` paths with a glob before writing to registry.
- Use verb-noun form for `capability_name` (e.g., "Build knowledge card" not "knowledge cards").
- Derive `keyword_index` from the union of the agent's `domain` and `capabilities` fields -- never invent keywords.
- Mark `quality_baseline: unscored` for any agent with `quality: null` in source.
- Include a `coverage_gaps` section even if empty -- absence of gaps is itself information.
- Re-run `cex_doctor.py` after registry creation to catch phantom references early.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_capability_registry]] | upstream | 0.49 |
| [[bld_instruction_capability_registry]] | upstream | 0.45 |
| [[p03_sp_capability_registry_builder]] | upstream | 0.43 |
| [[capability-registry-builder]] | upstream | 0.33 |
| [[bld_knowledge_card_capability_registry]] | upstream | 0.33 |
| [[bld_schema_capability_registry]] | upstream | 0.32 |
| [[bld_output_template_capability_registry]] | upstream | 0.31 |
| [[bld_config_capability_registry]] | upstream | 0.30 |
| [[bld_tools_capability_registry]] | upstream | 0.24 |
| [[spec_infinite_bootstrap_loop]] | related | 0.24 |
