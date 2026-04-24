---
id: n00_interface_manifest
kind: knowledge_card
8f: F3_inject
pillar: P06
nucleus: n00
title: "Interface -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, interface, p06, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_integration_guide
  - bld_schema_interface
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_thinking_config
  - bld_schema_multimodal_prompt
  - bld_schema_kind
  - bld_schema_quickstart_guide
  - bld_schema_action_paradigm
---

<!-- 8F: F1=knowledge_card P06 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Interface defines the agent-to-agent (A2A) integration contract specifying how two agents or system components communicate. It covers the message protocol, task schema, capability requirements, trust level, handoff format, and error signaling conventions. Interface artifacts are the formal specification that enables safe, version-controlled agent composition without tight coupling.

## Pillar
P06 -- Schema

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `interface` |
| pillar | string | yes | Always `P06` |
| title | string | yes | "Producer -> Consumer Interface" naming |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| producer | string | yes | Agent or system emitting the message |
| consumer | string | yes | Agent or system receiving the message |
| protocol | enum | yes | a2a_task / json_rpc / rest / grpc / signal |
| message_schema | object | yes | Schema of the message payload |
| capability_requirements | list | no | Producer capabilities consumer depends on |
| versioning_policy | string | yes | How breaking changes are communicated |

## When to use
- Defining the handoff protocol between two nuclei in a multi-agent workflow
- Specifying the A2A task schema for a new crew role pairing
- Documenting the integration contract between CEX and an external agent framework

## Builder
`archetypes/builders/interface-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind interface --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N03 engineering + N07 orchestration define interfaces
- `{{SIN_LENS}}` -- Inventive Pride: minimal surface, maximum composability
- `{{TARGET_AUDIENCE}}` -- agent developers building producers or consumers
- `{{DOMAIN_CONTEXT}}` -- agent types, trust model, message frequency, failure modes

## Example (minimal)
```yaml
---
id: interface_n07_to_n03_handoff
kind: interface
pillar: P06
nucleus: n03
title: "N07 Orchestrator -> N03 Engineering Handoff Interface"
version: 1.0
quality: null
---
producer: n07
consumer: n03
protocol: a2a_task
versioning_policy: "Additive fields only; major version for breaking changes"
```

## Related kinds
- `agent` (P02) -- agents that implement this interface as producer or consumer
- `input_schema` (P06) -- message payload schema referenced by the interface
- `workflow` (P12) -- orchestration artifact that sequences multiple interface calls

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | related | 0.40 |
| [[bld_schema_interface]] | related | 0.40 |
| [[bld_schema_reranker_config]] | related | 0.39 |
| [[bld_schema_usage_report]] | related | 0.39 |
| [[bld_schema_dataset_card]] | related | 0.38 |
| [[bld_schema_thinking_config]] | related | 0.38 |
| [[bld_schema_multimodal_prompt]] | related | 0.37 |
| [[bld_schema_kind]] | related | 0.37 |
| [[bld_schema_quickstart_guide]] | related | 0.37 |
| [[bld_schema_action_paradigm]] | related | 0.37 |
