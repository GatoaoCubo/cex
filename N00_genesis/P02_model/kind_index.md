---
id: n00_p02_kind_index
kind: knowledge_card
8f: F3_inject
pillar: P02
nucleus: n00
title: "P02 Model -- Kind Index"
version: 1.0
quality: 9.0
tags: [index, p02, archetype, n00]
density_score: 1.0
updated: "2026-04-17"
related:
  - kc_intent_resolution_map
  - bld_collaboration_agent
  - p12_dr_software_project
  - bld_architecture_kind
  - bld_collaboration_model_card
  - p12_dr_builder_nucleus
  - kind-builder
  - bld_collaboration_kind
  - p02_nd_n03.md
  - agent-builder
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Master index of all 23 kinds in pillar P02. Reference for /mentor, nucleus builders, and the 8F pipeline.

## Pillar: P02 Model
Defines agent identities, model providers, architectures, and training configurations. The ontological layer that answers: who is this agent, what model runs it, and how was it trained?

## Kinds in P02

| Kind | Purpose | Primary Nucleus | Builder |
|------|---------|-----------------|---------|
| `agent` | Agent definition (persona + capabilities) | N03 | `agent-builder` |
| `agent_package` | Portable AI agent package (ISO format) -- self-contained, LLM-agnostic | N03 | `agent_package-builder` |
| `agent_profile` | Agent persona and identity construction method | N03 | `agent_profile-builder` |
| `agents_md` | AAIF/OpenAI AGENTS.md project-root manifest: setup/test/lint commands, | N03 | `agents_md-builder` |
| `axiom` | Principio fundamental imutavel â€” parte da identidade profunda da ent | N03 | `axiom-builder` |
| `boot_config` | Boot configuration per provider | N03 | `boot_config-builder` |
| `customer_segment` | Customer segment/ICP definition artifact with firmographics and needs | N03 | `customer_segment-builder` |
| `fallback_chain` | Fallback sequence (model A > B > C) | N03 | `fallback_chain-builder` |
| `finetune_config` | Fine-tuning job configuration: dataset, base model, adapter type (LoRA | N03 | `finetune_config-builder` |
| `handoff_protocol` | Agent-to-agent transfer protocol | N03 | `handoff_protocol-builder` |
| `lens` | Perspectiva especializada sobre dominio | N03 | `lens-builder` |
| `memory_scope` | Agent memory configuration | N03 | `memory_scope-builder` |
| `mental_model` | Agent mental model (routing, decisions) | N03 | `mental_model-builder` |
| `model_architecture` | Neural network architecture definition | N03 | `model_architecture-builder` |
| `model_card` | LLM spec in use (pricing, context, capabilities) | N03 | `model_card-builder` |
| `model_provider` | LLM provider adapter (Claude, GPT, Gemini, Ollama, OpenRouter, LiteLLM | N03 | `model_provider-builder` |
| `nucleus_def` | Formal definition of a CEX nucleus (N00-N07). Fields: nucleus_id, role | N07 | `nucleus_def-builder` |
| `personality` | Hot-swappable voice/tone/values persona applied at runtime | N03 | `personality-builder` |
| `rl_algorithm` | Reinforcement learning training algorithm definition | N03 | `rl_algorithm-builder` |
| `role_assignment` | CrewAI Agent-style binding: role -> agent + responsibilities + delegat | N03 | `role_assignment-builder` |
| `router` | Routing rule (task > agent_group) | N03 | `router-builder` |
| `software_project` | Complete software project definition — architecture, dependencies, bui | N03 | `software_project-builder` |
| `training_method` | Model training/adaptation technique definition | N03 | `training_method-builder` |

## Usage
```python
# Build any of these via 8F:
python _tools/cex_8f_runner.py "your intent" --kind {kind} --execute
```

## CoC Hierarchy Note
These 23 kinds follow the convention-over-configuration hierarchy: each instance
(N01-N07) inherits this schema and fills the variables for its sin lens.
N00_genesis holds the canonical archetype; nuclei hold the instantiated versions.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_intent_resolution_map]] | sibling | 0.43 |
| [[bld_collaboration_agent]] | downstream | 0.42 |
| [[p12_dr_software_project]] | downstream | 0.41 |
| [[bld_architecture_kind]] | downstream | 0.39 |
| [[bld_collaboration_model_card]] | related | 0.37 |
| [[p12_dr_builder_nucleus]] | downstream | 0.36 |
| [[kind-builder]] | downstream | 0.36 |
| [[bld_collaboration_kind]] | downstream | 0.35 |
| [[p02_nd_n03.md]] | related | 0.35 |
| [[agent-builder]] | related | 0.35 |
