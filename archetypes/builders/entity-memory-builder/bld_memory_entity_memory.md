---
id: p10_lr_entity_memory_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "Entity memory records without confidence scoring caused downstream agents to treat unverified attributes (scraped from secondary sources) with the same weight as primary-source facts, leading to incorrect grounding in 3 out of 5 test prompts. Records with confidence < 0.5 that lacked expiry dates were re-injected indefinitely, polluting context with stale data in 2 production runs."
pattern: "Assign confidence float to every entity_memory. Set expiry for all volatile entities (tools, services, APIs). Use update_policy: merge for general facts, overwrite for pricing/version data. Minimum 3 attributes — records with 1-2 attributes provided insufficient grounding to be useful."
evidence: "5 grounding test prompts: 3 failed with unscored attributes; 0 failures after confidence scoring added. 2 production runs with stale injection: root cause was missing expiry on versioned tool records."
confidence: 0.85
outcome: SUCCESS
domain: entity_memory
tags: [entity-memory, confidence-scoring, expiry, update-policy, grounding, attributes]
tldr: "Confidence scoring and expiry are load-bearing for entity memory quality. Min 3 attributes. update_policy must match entity volatility."
impact_score: 8.0
decay_rate: 0.03
agent_group: edison
keywords: [entity memory, confidence, expiry, attributes, update policy, grounding, staleness, relationships]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Entity Memory"
density_score: 0.90
llm_function: INJECT
---
## Summary
Entity memory is only as useful as its worst attribute. A single unverified fact injected with the same weight as a primary-source fact degrades the entire grounding block. Three authoring decisions determine whether entity memory is useful or noise: confidence scoring, expiry declaration, and attribute count. Records with >= 3 specific, confidence-scored attributes consistently grounded LLM responses correctly.

## Pattern
**Confidence scoring + expiry + minimum attribute density.**
1. 0.9-1.0: verified from primary source (official docs, direct API response)
2. 0.7-0.89: reliable secondary source (internal MEMORY.md, team knowledge)
3. 0.5-0.69: probable — inferred from multiple consistent mentions
4. 0.0-0.49: uncertain — single mention; consider omitting

Expiry rules:
1. tool/service with versioning: 6-12 months
2. person with role: 12 months
3. stable concept/organization: null
4. API endpoint/pricing: 3-6 months

Update policy matching:
1. pricing, versions, status → overwrite
2. history, timeline, events → append
3. general facts with mixed volatility → merge
4. contracts, decisions → versioned

Attribute count: minimum 3 (identity + status + provenance); target 5-8; split at 12+.

## Anti-Pattern
1. Single attribute — no grounding advantage over the entity name alone
2. confidence: 1.0 for scraped web data — overconfidence poisons merge logic
3. No expiry on versioned API service — stale endpoint causes silent failures after migration
4. update_policy: append on pricing — accumulates outdated prices
5. Attributes containing inferences ("best_tool: true") — opinions corrupt fact maps
6. Mixing entity_memory with learning_record fields (impact_score, decay_rate) — breaks routing

## Builder Context

This ISO operates within the `entity-memory-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_entity_memory_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_entity_memory_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | entity_memory |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
