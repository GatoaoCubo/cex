---
kind: architecture
id: bld_architecture_interface
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of interface — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Interface"
version: "1.0.0"
author: n03_builder
tags: [interface, builder, examples]
tldr: "Golden and anti-examples for interface construction, demonstrating ideal structure and common pitfalls."
domain: "interface construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_input_schema
  - p01_kc_interface
  - p03_sp_interface_builder
  - interface-builder
  - bld_knowledge_card_interface
  - p10_lr_interface_builder
  - bld_instruction_interface
  - p11_qg_interface
  - bld_collaboration_interface
  - bld_output_template_interface
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| method_definitions | Named operations both parties agree exist | author | required |
| input_types | Typed input shape per method (may reference input_schema) | author | required |
| output_types | Typed output shape per method | author | required |
| version | Semantic version for backward compatibility tracking | author | required |
| deprecation_policy | How and when old methods are retired | author | recommended |
| mock_spec | Stub responses for testing without live implementation | author | optional |
| error_contract | Named error codes and shapes each method may return | author | recommended |
| compatibility_notes | Breaking vs non-breaking change classification | author | optional |
## Dependency Graph
```
interface     --consumes--> input_schema
connector     --implements--> interface
validator     --checks_against--> interface
system_prompt --references--> interface
interface     --produces--> mock_spec
```
| From | To | Type | Data |
|------|----|------|------|
| interface | input_schema | data_flow | method input shapes formalized as schemas |
| connector | interface | depends | runtime adapter implements the declared contract |
| validator | interface | data_flow | compliance check against method signatures |
| system_prompt | interface | data_flow | documents available methods to agent identity |
| interface | mock_spec | produces | stub responses derived from output_types |
## Boundary Table
| interface IS | interface IS NOT |
|--------------|-----------------|
| Bilateral contract agreed by both parties | Unilateral shape contract for one callee |
| Specifies methods with named input and output | Runtime event or status report |
| Design-time artifact (written before implementation) | Concrete implementation or adapter code |
| Versioned with deprecation and compatibility policy | Routing decision about who receives what |
| Defines what CAN happen between two agents | Validates whether something DID happen correctly |
| Shared reference for both producer and consumer | Orchestration logic or execution recipe |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Contract surface | method_definitions, version | Declare the operations both agents agree on |
| Type system | input_types, output_types | Enforce data shapes for each method direction |
| Safety | error_contract, compatibility_notes | Define failure modes and change impact |
| Lifecycle | deprecation_policy | Govern how the contract evolves over time |
| Testing | mock_spec | Enable development against the contract without live systems |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_input_schema]] | sibling | 0.44 |
| [[p01_kc_interface]] | upstream | 0.44 |
| [[p03_sp_interface_builder]] | upstream | 0.44 |
| [[interface-builder]] | upstream | 0.42 |
| [[bld_knowledge_card_interface]] | upstream | 0.38 |
| [[p10_lr_interface_builder]] | downstream | 0.37 |
| [[bld_instruction_interface]] | upstream | 0.36 |
| [[p11_qg_interface]] | downstream | 0.36 |
| [[bld_collaboration_interface]] | downstream | 0.34 |
| [[bld_output_template_interface]] | upstream | 0.33 |
