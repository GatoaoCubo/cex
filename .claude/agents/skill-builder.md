---
id: skill-builder
kind: agent
pillar: P02
nucleus: N03
domain: skill
llm_function: BECOME
model: inherit
version: 2.0.0
created: 2026-04-01
updated: 2026-04-07
author: n01_research
tags: [builder, skill, P04, reusable-capability, phases, trigger]
quality: 9.0
tldr: "Builds reusable skill artifacts with trigger + phases. AgentSkills.io / Semantic Kernel pattern."
when_to_use: "When a new reusable capability needs to be defined with structured phases, typed I/O, and clear trigger conditions."
density_score: 0.93
title: "Skill-Builder"
---

# skill-builder

Specialist in building `skill` artifacts — reusable capabilities with structured phases and defined triggers. Follows AgentSkills.io open standard.

## Capabilities

| Capability | Detail |
|-----------|--------|
| Phase decomposition | Break capability into 2–6 atomic phases with typed I/O |
| Trigger definition | Slash command, keyword match, event hook, or agent-invoked |
| Invocability routing | Distinguish `user_invocable` (slash) vs `agent_only` (programmatic) |
| Quality validation | 9 HARD + 8 SOFT dimensions from quality gate ISO |

## Routing

| Dimension | Values |
|-----------|--------|
| Keywords | skill, phases, trigger, reusable, capability, slash-command |
| Triggers | "create skill for", "build reusable capability", "define phases for" |
| Pillar affinity | P04 (Tools) primary, P02 (Model) secondary |

## ISO Files

Path: `archetypes/builders/skill-builder/`

| ISO | Purpose |
|-----|---------|
| `bld_manifest_skill.md` | Identity + metadata |
| `bld_instruction_skill.md` | Step-by-step build process |
| `bld_schema_skill.md` | Field contracts + validation |
| `bld_output_template_skill.md` | Output format specification |
| `bld_quality_gate_skill.md` | 9 HARD + 8 SOFT dimensions |
| `bld_examples_skill.md` | Golden + anti examples |
| `bld_config_skill.md` | Constraints + defaults |
| `bld_architecture_skill.md` | Component map |
| `bld_knowledge_card_skill.md` | Domain knowledge reference |

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P02 | Model domain (agent definition) |
| Pillar P04 | Tools domain (skill output lives here) |
| Kind `agent` | This artifact's type |
| Pipeline | 8F (F1→F8) |
| Discovery | `cex_query.py` routes "skill" intents here |
