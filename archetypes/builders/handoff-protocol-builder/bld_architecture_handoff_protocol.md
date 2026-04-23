---
kind: architecture
id: bld_architecture_handoff_protocol
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of handoff_protocol — inventory, dependencies, and architectural position
quality: 9.2
title: "Architecture Handoff Protocol"
version: "1.0.0"
author: n03_builder
tags: [handoff_protocol, builder, examples]
tldr: "Golden and anti-examples for handoff protocol construction, demonstrating ideal structure and common pitfalls."
domain: "handoff protocol construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_handoff_protocol_builder
  - handoff-protocol-builder
  - bld_output_template_handoff_protocol
  - p01_kc_handoff_protocol
  - bld_instruction_handoff_protocol
  - bld_collaboration_handoff_protocol
  - p10_lr_handoff_protocol_builder
  - bld_examples_handoff_protocol
  - bld_tools_handoff_protocol
  - p11_qg_handoff_protocol
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| trigger | Condition that initiates the handoff | handoff_protocol | required |
| context_passed | Data fields transferred from source to target | handoff_protocol | required |
| return_contract | Expected shape and fields of the response | handoff_protocol | required |
| timeout | Max wait time before escalation | handoff_protocol | optional |
| retry_policy | Retry count and backoff on failure | handoff_protocol | optional |
| source_agent | Agent initiating the handoff | P02 | upstream |
| target_agent | Agent receiving the handoff | P02 | downstream |
| dispatch_rule | Routing rule that selects the target | P12 | external |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| trigger | handoff_protocol | produces | Condition that initiates the handoff |
| context_passed | handoff_protocol | produces | Data fields transferred from source to target |
| return_contract | handoff_protocol | produces | Expected shape and fields of the response |
| timeout | handoff_protocol | produces | Max wait time before escalation |
| retry_policy | handoff_protocol | produces | Retry count and backoff on failure |
| source_agent | P02 | depends | Agent initiating the handoff |
| target_agent | P02 | depends | Agent receiving the handoff |
| dispatch_rule | P12 | depends | Routing rule that selects the target |
## Boundary Table
| handoff_protocol IS | handoff_protocol IS NOT |
|-------------|----------------|
| Handoff protocol — trigger conditions, context passed, return contract between agents | dispatch_rule (P12 |
| Not dispatch_rule | dispatch_rule (P12 |
| Not keyword routing) | keyword routing) |
| Not workflow | workflow (P12 |
| Not multi-step orchestration) | multi-step orchestration) |
| Not router | router (P02 |
| Not task routing) | task routing) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | trigger, context_passed, return_contract | Define the artifact's core parameters |
| optional | timeout, retry_policy | Extend with recommended fields |
| external | source_agent, target_agent, dispatch_rule | Upstream/downstream connections |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_architecture_handoff_protocol
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-architecture-handoff-protocol.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_handoff_protocol_builder]] | upstream | 0.57 |
| [[handoff-protocol-builder]] | upstream | 0.56 |
| [[bld_output_template_handoff_protocol]] | upstream | 0.50 |
| [[p01_kc_handoff_protocol]] | upstream | 0.43 |
| [[bld_instruction_handoff_protocol]] | upstream | 0.41 |
| [[bld_collaboration_handoff_protocol]] | downstream | 0.40 |
| [[p10_lr_handoff_protocol_builder]] | downstream | 0.39 |
| [[bld_examples_handoff_protocol]] | upstream | 0.38 |
| [[bld_tools_handoff_protocol]] | upstream | 0.37 |
| [[p11_qg_handoff_protocol]] | downstream | 0.36 |
