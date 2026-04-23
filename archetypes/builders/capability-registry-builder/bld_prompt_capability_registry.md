---
kind: instruction
id: bld_instruction_capability_registry
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for capability_registry
quality: 8.9
title: "Instruction Capability Registry"
version: "1.0.0"
author: n04_wave8
tags: [capability_registry, builder, instruction, agent-discovery]
tldr: "Step-by-step production process for capability_registry"
domain: "capability_registry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_capability_registry_builder
  - bld_examples_capability_registry
  - bld_schema_capability_registry
  - bld_output_template_capability_registry
  - p10_lr_capability_registry_builder
  - capability-registry-builder
  - bld_tools_capability_registry
  - bld_instruction_agent
  - bld_knowledge_card_capability_registry
  - agent-builder
---

## Phase 1: RESEARCH
1. Scan `.claude/agents/` directory -- list all 252 builder sub-agent files.
2. Scan `N01_intelligence/P02_model/`, `N02_marketing/P02_model/`, `N03_engineering/P02_model/`, `N04_knowledge/P02_model/`, `N05_operations/P02_model/`, `N06_commercial/P02_model/` for nucleus domain agents.
3. Read each agent card (`N0x_*/agent_card_n0x.md`) for nucleus-level capabilities.
4. Extract from each agent: id, domain, capabilities list, tools list, input kinds, output kinds.
5. Map each agent to relevant query keywords (from domain + capabilities).
6. Identify quality_baseline from agent frontmatter or defaults (nucleus cards: 9.0+).
7. Check availability: does the agent file exist and have valid frontmatter?
8. Estimate cost_tokens (low/medium/high) based on agent complexity.

## Phase 2: COMPOSE
1. Reference SCHEMA.md for required registry entry fields.
2. Populate OUTPUT_TEMPLATE.md with discovered agents.
3. Group entries by domain: builder_sub_agents | nucleus_domain_agents | nucleus_cards.
4. For each entry, populate: capability_name, provider_agent, input_schema, output_schema, cost_tokens, quality_baseline, availability.
5. Add keyword_index field: comma-separated discovery terms.
6. Sort entries by quality_baseline DESC within each domain group.
7. Add ranked_for cross-reference: which query categories each agent answers best.
8. Validate all paths reference real files (no phantom agents).

## Phase 3: VALIDATE
- [ ] All required fields present (capability_name, provider_agent, input_schema, output_schema, cost_tokens, quality_baseline, availability).
- [ ] No duplicate capability_name entries within a domain group.
- [ ] All provider_agent paths resolve to real files.
- [ ] keyword_index non-empty for each entry.
- [ ] quality_baseline numeric (0.0-10.0) or "unscored".
- [ ] availability enum: active | deprecated | experimental.
- [ ] ranked_for list non-empty for all entries.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_capability_registry_builder]] | related | 0.40 |
| [[bld_examples_capability_registry]] | downstream | 0.38 |
| [[bld_schema_capability_registry]] | downstream | 0.35 |
| [[bld_output_template_capability_registry]] | downstream | 0.34 |
| [[p10_lr_capability_registry_builder]] | downstream | 0.34 |
| [[capability-registry-builder]] | downstream | 0.31 |
| [[bld_tools_capability_registry]] | downstream | 0.30 |
| [[bld_instruction_agent]] | sibling | 0.27 |
| [[bld_knowledge_card_capability_registry]] | upstream | 0.27 |
| [[agent-builder]] | upstream | 0.25 |
