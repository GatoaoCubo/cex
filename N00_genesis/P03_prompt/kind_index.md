---
id: n00_p03_kind_index
kind: knowledge_card
8f: F3_inject
pillar: P03
nucleus: n00
title: "P03 Prompt -- Kind Index"
version: 1.0
quality: 9.0
tags: [index, p03, archetype, n00]
density_score: 1.0
related:
  - kc_intent_resolution_map
  - bld_architecture_kind
  - bld_collaboration_action_prompt
  - bld_collaboration_kind
  - p12_dr_software_project
  - kind-builder
  - p12_dr_builder_nucleus
  - agent_card_n03
  - bld_collaboration_system_prompt
  - p02_agent_creation_nucleus
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Master index of all 21 kinds in pillar P03. Reference for /mentor, nucleus builders, and the 8F pipeline.

## Pillar: P03 Prompt
Prompt engineering artifacts: templates, chains, reasoning strategies, system prompts, and the universal prompt compiler that transmutes user intent into precise builder dispatch.

## Kinds in P03

| Kind | Purpose | Primary Nucleus | Builder |
|------|---------|-----------------|---------|
| `action_prompt` | Task prompt sent by human/orchestrator to the agent | N03 | `action_prompt-builder` |
| `context_file` | Project-scoped instruction file auto-injected into context (HERMES CLAUDE.md/AGENTS.md) | N03 | `context-file-builder` |
| `chain` | Chained prompt sequence (output A -> input B) | N03 | `chain-builder` |
| `churn_prevention_playbook` | Churn prevention playbook: signal detection, intervention triggers, sa | N06 | `churn_prevention_playbook-builder` |
| `constraint_spec` | Constrained generation rules | N03 | `constraint_spec-builder` |
| `context_window_config` | Token budget allocation, priority tiers, and overflow rules for prompt | N03 | `context_window_config-builder` |
| `expansion_play` | Account expansion play: upsell triggers, cross-sell map, NRR mechanics | N06 | `expansion_play-builder` |
| `instruction` | Step-by-step execution instructions for agents or pipelines | N03 | `instruction-builder` |
| `multimodal_prompt` | Cross-modal prompt pattern for vision/audio/text | N03 | `multimodal_prompt-builder` |
| `planning_strategy` | Agent planning approach definition | N03 | `planning_strategy-builder` |
| `prompt_compiler` | Intent-to-artifact transmutation rules. Compiles vague user input into | N07 | `prompt_compiler-builder` |
| `prompt_optimizer` | Automated prompt improvement and compilation tool | N03 | `prompt_optimizer-builder` |
| `prompt_technique` | Specific prompting method or pattern | N03 | `prompt_technique-builder` |
| `prompt_template` | Reusable template with {{vars}} to generate prompts | N03 | `prompt_template-builder` |
| `prompt_version` | Versioned prompt snapshot | N03 | `prompt_version-builder` |
| `reasoning_strategy` | Prompting technique for structured reasoning | N03 | `reasoning_strategy-builder` |
| `reasoning_trace` | Structured chain-of-thought reasoning with confidence scores | N03 | `reasoning_trace-builder` |
| `sales_playbook` | Sales playbook with personas, discovery flow, objection handling, clos | N03 | `sales_playbook-builder` |
| `system_prompt` | System prompt that defines agent identity and rules | N03 | `system_prompt-builder` |
| `tagline` | Short memorable phrase capturing brand essence — taglines, slogans, he | N02 | `tagline-builder` |
| `webinar_script` | Webinar script with intro/agenda/segments/Q&A/CTA + speaker notes + sl | N03 | `webinar_script-builder` |

## Usage
```python
# Build any of these via 8F:
python _tools/cex_8f_runner.py "your intent" --kind {kind} --execute
```

## CoC Hierarchy Note
These 21 kinds follow the convention-over-configuration hierarchy: each instance
(N01-N07) inherits this schema and fills the variables for its sin lens.
N00_genesis holds the canonical archetype; nuclei hold the instantiated versions.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_intent_resolution_map]] | sibling | 0.43 |
| [[bld_architecture_kind]] | downstream | 0.40 |
| [[bld_collaboration_action_prompt]] | downstream | 0.37 |
| [[bld_collaboration_kind]] | downstream | 0.36 |
| [[p12_dr_software_project]] | downstream | 0.36 |
| [[kind-builder]] | downstream | 0.36 |
| [[p12_dr_builder_nucleus]] | downstream | 0.34 |
| [[agent_card_n03]] | upstream | 0.32 |
| [[bld_collaboration_system_prompt]] | related | 0.31 |
| [[p02_agent_creation_nucleus]] | upstream | 0.31 |
