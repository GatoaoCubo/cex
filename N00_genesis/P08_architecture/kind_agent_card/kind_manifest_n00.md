---
id: n00_agent_card_manifest
kind: knowledge_card
pillar: P08
nucleus: n00
title: "Agent Card -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, agent_card, p08, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_nucleus_def
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_kind
  - bld_schema_multimodal_prompt
  - bld_schema_agent_profile
  - bld_schema_integration_guide
  - bld_schema_pitch_deck
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An agent_card is the deployment specification for an autonomous agent: it declares the agent's identity, model tier, tools, boot sequence, and dispatch contract. It is the A2A (agent-to-agent) standard descriptor that allows N07 to discover, configure, and route work to any nucleus or sub-agent without human intervention.

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `agent_card` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable agent name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nucleus | string | yes | Owning nucleus (n01-n07) |
| model | string | yes | Model identifier (e.g. claude-sonnet-4-6) |
| sin_lens | string | yes | Cultural DNA / optimization driver |
| tools | list | yes | Available tool names this agent may call |
| boot_script | string | yes | Path to boot.ps1 or equivalent |
| dispatch_protocol | string | yes | solo \| grid \| crew |
| context_window | integer | no | Max tokens (default 200000) |
| sub_agents | integer | no | Max parallel sub-agent spawns |

## When to use
- Registering a new nucleus or sub-agent so N07 can discover and dispatch it
- Defining capability boundaries for a specialized builder (e.g. landing-page-builder)
- Enabling the capability_registry to index and search spawnable agents

## Builder
`archetypes/builders/agent_card-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind agent_card --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: agent_card_n03
kind: agent_card
pillar: P08
nucleus: n03
title: "N03 Engineering Agent Card"
version: 1.0
quality: null
---
# N03 Engineering
model: claude-opus-4-6
sin_lens: Inventive Pride
tools: [cex_compile, cex_doctor, cex_8f_runner]
boot_script: boot/n03.ps1
dispatch_protocol: grid
```

## Related kinds
- `agent` (P02) -- the agent definition that this card describes for deployment
- `capability_registry` (P08) -- indexes all agent_cards for crew planning
- `nucleus_def` (P02) -- machine-readable nucleus identity this card supplements

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_nucleus_def]] | upstream | 0.47 |
| [[bld_schema_reranker_config]] | upstream | 0.44 |
| [[bld_schema_usage_report]] | upstream | 0.44 |
| [[bld_schema_dataset_card]] | upstream | 0.43 |
| [[bld_schema_benchmark_suite]] | upstream | 0.43 |
| [[bld_schema_kind]] | upstream | 0.43 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.42 |
| [[bld_schema_agent_profile]] | upstream | 0.42 |
| [[bld_schema_integration_guide]] | upstream | 0.42 |
| [[bld_schema_pitch_deck]] | upstream | 0.42 |
