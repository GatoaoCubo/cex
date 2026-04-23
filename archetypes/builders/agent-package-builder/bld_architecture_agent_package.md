---
kind: architecture
id: bld_architecture_agent_package
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of agent_package — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Agent Package"
version: "1.0.0"
author: n03_builder
tags: [agent_package, builder, examples]
tldr: "Golden and anti-examples for agent package construction, demonstrating ideal structure and common pitfalls."
domain: "agent package construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - agent-builder
  - agent-package-builder
  - p01_kc_agent_package
  - bld_instruction_agent_package
  - bld_architecture_agent
  - p03_sp_agent_package_builder
  - bld_schema_agent_package
  - bld_knowledge_card_agent_package
  - p03_sp_agent_builder
  - p02_iso_organization_agent
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| manifest.yaml | Entry point: identity, tier, file inventory, LP mapping | author | required |
| system_instruction.md | Agent persona and behavioral rules, capped at 4096 tokens | author | required |
| instructions.md | Operational steps the agent follows (P03) | author | required |
| quick_start.md | Minimal usage example for immediate deployment | author | tier >= standard |
| examples.md | Input/output demonstration pairs | author | tier >= standard |
| input_schema.yaml | Typed input contract for the agent (P06) | author | tier >= complete |
| output_schema.yaml | Typed output contract for the agent (P06) | author | tier >= complete |
| knowledge_base/ | Domain knowledge cards bundled for retrieval | author | tier = whitelabel |
| upload_kit.md | Deployment instructions per target platform | author | tier >= standard |
| tier_label | One of: minimal / standard / complete / whitelabel | author | required |
## Dependency Graph
```
agent         --produces--> agent_package
system_prompt --produces--> system_instruction.md
knowledge_card --produces--> knowledge_base/
agent_package   --produces--> upload_kit
agent_package   --consumed_by--> spawn_config
agent_package   --consumed_by--> workflow
```
| From | To | Type | Data |
|------|----|------|------|
| agent | agent_package | data_flow | canonical identity, capabilities, domain |
| system_prompt | agent_package | data_flow | persona text becomes system_instruction.md |
| knowledge_card | agent_package | data_flow | domain facts bundled into knowledge_base/ |
| agent_package | upload_kit | produces | deployment instructions derived from manifest |
| agent_package | spawn_config | data_flow | tier, file paths, model recommendations |
| agent_package | workflow | data_flow | self-contained execution node |
## Boundary Table
| agent_package IS | agent_package IS NOT |
|----------------|-------------------|
| Portable, self-contained multi-file bundle | Canonical agent definition in a repository |
| Tiered completeness: minimal to whitelabel | Boot configuration (model flags, MCP profiles) |
| LLM-agnostic (no hardcoded model names) | Mental model for routing and decision-making |
| Static distributable artifact, not runtime | Spec for the underlying LLM itself |
| manifest.yaml is the required entry point | Single-file artifact |
| system_instruction.md capped at 4096 tokens | Fallback chain or multi-model routing logic |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | manifest.yaml, tier_label | Declare the package and its completeness level |
| Behavior | system_instruction.md, instructions.md | Carry agent persona and operational recipe |
| Contract | input_schema.yaml, output_schema.yaml | Define typed entry and exit data shapes |
| Knowledge | knowledge_base/, examples.md | Bundle domain facts and usage demonstrations |
| Deployment | upload_kit.md, quick_start.md | Enable immediate use on any target platform |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent-builder]] | upstream | 0.46 |
| [[agent-package-builder]] | upstream | 0.44 |
| [[p01_kc_agent_package]] | upstream | 0.43 |
| [[bld_instruction_agent_package]] | upstream | 0.43 |
| [[bld_architecture_agent]] | sibling | 0.43 |
| [[p03_sp_agent_package_builder]] | upstream | 0.41 |
| [[bld_schema_agent_package]] | upstream | 0.37 |
| [[bld_knowledge_card_agent_package]] | upstream | 0.37 |
| [[p03_sp_agent_builder]] | upstream | 0.36 |
| [[p02_iso_organization_agent]] | upstream | 0.34 |
