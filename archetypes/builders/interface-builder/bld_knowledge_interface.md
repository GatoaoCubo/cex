---
kind: knowledge_card
id: bld_knowledge_card_interface
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for interface production — bilateral integration contracts
sources: Gamma et al. 1994, OpenAPI 3.x, gRPC/Protobuf, contract-first API design
quality: 9.1
title: "Knowledge Card Interface"
version: "1.0.0"
author: n03_builder
tags: [interface, builder, examples]
tldr: "Golden and anti-examples for interface construction, demonstrating ideal structure and common pitfalls."
domain: "interface construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_interface_builder
  - bld_instruction_interface
  - p11_qg_interface
  - p10_lr_interface_builder
  - interface-builder
  - bld_collaboration_interface
  - bld_architecture_interface
  - bld_collaboration_input_schema
  - bld_schema_interface
  - bld_output_template_interface
---

# Domain Knowledge: interface
## Executive Summary
Interfaces are bilateral contracts where both provider and consumer agree on methods, input shapes, and output shapes. Rooted in interface-based programming (GoF 1994) and API-first design. Interfaces define what CAN happen between two systems — they are static specifications, not runtime events. They differ from input schemas (unilateral), signals (runtime notifications), and connectors (runtime implementations).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P06 (contracts/schema) |
| Frontmatter fields | 20+ |
| Quality gates | 8 HARD + 10 SOFT |
| Direction | Bilateral (both parties agree) |
| Key sections | methods (name, input, output), versioning, deprecation |
| Versioning | semver with backward_compatible flag |
| Mock support | Test doubles derivable from interface |
## Patterns
- **Method-based contracts**: named operations with typed input and output
| Source | Concept | Application |
|--------|---------|-------------|
| OpenAPI 3.x | REST paths, schemas, responses | methods structure |
| gRPC/Protobuf | Typed RPC method definitions | Strongly typed method contracts |
| TypeScript | Structural type contracts | Bilateral type agreement |
| GraphQL | Query/mutation typed fields | Method-level I/O contracts |
| Java interfaces | Abstract method signatures | Method signature pattern |
- **Bilateral agreement**: both provider and consumer acknowledge the contract — unlike unilateral input schemas
- **Versioning with semver**: breaking changes require major version bump; backward_compatible flag explicit
- **Deprecation planning**: every method has planned sunset timeline — no sudden removal
- **Mock derivation**: interfaces generate test doubles automatically — testing does not require real implementation
- **Static specification**: interfaces define what CAN happen, not what DID happen (that is a signal)
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Unilateral contract | That is an input_schema; interfaces require both parties |
| No versioning | Breaking changes break consumers silently |
| No deprecation timeline | Methods removed without warning; consumer breakage |
| Free-text I/O types | Cannot generate mocks or validate compliance |
| Runtime state in interface | Interfaces are static specs; use signals for events |
| No mock specification | Cannot test without real implementation |
## Application
1. Identify parties: who is provider, who is consumer?
2. Define methods: name, typed input, typed output per operation
3. Set version: semver with backward_compatible flag
4. Plan deprecation: sunset timeline for methods to be removed
5. Add mock spec: example inputs and outputs for test doubles
6. Validate: bilateral agreement, all methods typed, version declared
## References
- Gamma et al. 1994: "Design Patterns" — interface segregation principle
- OpenAPI 3.x: REST API contract specification
- gRPC: service definition and typed RPC methods
- Contract-first API design: swagger.io best forctices

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_interface_builder]] | downstream | 0.50 |
| [[bld_instruction_interface]] | downstream | 0.50 |
| [[p11_qg_interface]] | downstream | 0.46 |
| [[p10_lr_interface_builder]] | downstream | 0.45 |
| [[interface-builder]] | downstream | 0.44 |
| [[bld_collaboration_interface]] | downstream | 0.40 |
| [[bld_architecture_interface]] | downstream | 0.40 |
| [[bld_collaboration_input_schema]] | downstream | 0.35 |
| [[bld_schema_interface]] | downstream | 0.34 |
| [[bld_output_template_interface]] | downstream | 0.32 |
