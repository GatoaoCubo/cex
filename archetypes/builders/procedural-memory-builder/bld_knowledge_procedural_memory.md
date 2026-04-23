---
kind: knowledge_card
id: bld_knowledge_card_procedural_memory
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for procedural_memory production
quality: 9.2
title: "Knowledge Card: procedural_memory Builder"
version: "2.0.0"
author: n06_commercial
tags: [procedural_memory, builder, knowledge_card, voyager, reflexion, expel, skills]
tldr: "LLM agent procedural memory: skill libraries (Voyager), self-reflection notes (Reflexion/ExpeL), code-as-policies, skill composition, commercial tier gating (free=none, pro=shared library, enterprise=versioned+team)"
domain: "LLM agent procedural memory"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.91
related:
  - procedural-memory-builder
  - bld_collaboration_skill
  - bld_instruction_procedural_memory
  - p03_sp_procedural_memory_builder
  - bld_architecture_skill
  - bld_system_prompt_skill
  - bld_memory_skill
  - skill-builder
  - p10_mem_procedural_memory_builder
  - bld_collaboration_procedural_memory
---

## Domain Overview

Procedural memory in LLM agents stores *how to do things*: task sequences, tool-use
patterns, learned workflows, and skill definitions. Unlike episodic (what happened) or
semantic (what is true) memory, procedural memory is about executable knowledge that
the agent can apply to new situations.

The field was formalized by Voyager (Wang 2023), which introduced a self-expanding
skill library where GPT-4 agents write, verify, and reuse JavaScript skill functions
in Minecraft. ExpeL (Zhao 2023) extended this with cross-task experience transfer via
success/failure extraction from prior trajectories. Reflexion (Shinn 2023) adds
self-notes that persist verbal reasoning about past failures for future guidance.

## Key Concepts

| Concept | Definition | Source |
|---------|-----------|--------|
| Skill Library | Persistent store of reusable skill functions/definitions | Voyager (Wang 2023) |
| Skill Verification | Running generated skills against test cases before storing | Voyager |
| Self-Notes / Reflection | Verbal reasoning about past failures persisted for future use | Reflexion (Shinn 2023) |
| Experience Extraction | Mining success/failure patterns from trajectories into reusable insights | ExpeL (Zhao 2023) |
| Code-as-Policies | Executable code (Python/JS) as the procedural memory unit | Liang 2023 |
| Skill Composition | Combining existing skills to solve novel tasks without retraining | Voyager, Code-as-policies |
| Skill Namespace | Hierarchical key structure for skill lookup (domain.task.subtask) | CEX convention |
| Skill Versioning | Tracking skill evolution with backward-compatible updates | Production systems |
| Generalization | Abstracting from specific episodes to reusable skill templates | ExpeL |
| Skill Retrieval | Finding relevant skills by task description (semantic or exact match) | RAG + exact key |

## Industry References

| System | Architecture | Key Contribution |
|--------|-------------|-----------------|
| Voyager (Wang 2023) | GPT-4 + Minecraft env + JS skill library | First self-expanding LLM skill library |
| ExpeL (Zhao 2023) | Experience pool + LLM extraction | Cross-task procedural knowledge transfer |
| Reflexion (Shinn 2023) | Verbal self-reflection + memory store | Self-notes from failure for future guidance |
| Code-as-Policies (Liang 2023) | Python code as policy representation | Compositional code skills for robot/agent |
| GITM (Zhu 2023) | Goal-item tree + skill decomposition | Hierarchical procedural task planning |
| Ghost in the Minecraft (GITM) | Skill sub-goals with curriculum | Multi-level skill composition |
| LangMem procedural layer | Skill/SOP storage in LangGraph | Production LLM skill memory |

## Skill Storage Formats

| Format | Pros | Cons | Best For |
|--------|------|------|---------|
| Code (Python/JS) | Executable + verifiable | Requires sandbox | Tool-use, API calls |
| YAML definition | Human-readable + editable | Not directly executable | SOP, workflow specs |
| Natural language note | Easy to generate | Not structured | Reflexion self-notes |
| Structured JSON | Parseable by agent | Verbose | Skill metadata + deps |

## Commercial Tier Differentiation

| Feature | Free | PRO | ENTERPRISE |
|---------|------|-----|------------|
| Procedural memory | None | Shared skill library | Versioned + team-scoped |
| Skill count | 0 | Up to 100 per agent | Unlimited |
| Skill verification | N/A | Test-case gated | CI pipeline + rollback |
| Cross-agent sharing | N/A | Within workspace | Cross-organization |
| Skill versioning | N/A | Latest only | Full history + rollback |
| Reflexion notes | None | Per-session | Persistent + searchable |
| Code-as-policy | None | Python sandboxed | Enterprise sandbox + audit |

## Common Patterns

1. **Skill-before-context**: Check skill library before reasoning from scratch.
2. **Verify-before-store**: Run new skills against test cases before persisting.
3. **Fail-extract-store**: After failure, extract a self-note (Reflexion) for next time.
4. **Hierarchical namespace**: `domain.task.subtask` keys for skill lookup scalability.
5. **Skill composition**: Build complex tasks from primitive stored skills (Voyager pattern).

## Pitfalls

- Storing unverified skills causes procedural memory contamination (wrong procedures run).
- No versioning means a skill update silently breaks dependent tasks.
- Flat namespace (all skills in one list) becomes unsearchable at >50 skills.
- No failure extraction (Reflexion pattern) means the agent repeats the same mistakes.
- Free tier conflation: procedural memory is a PRO+ feature; free agents should degrade gracefully.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[procedural-memory-builder]] | downstream | 0.71 |
| [[bld_collaboration_skill]] | downstream | 0.61 |
| [[bld_instruction_procedural_memory]] | downstream | 0.57 |
| [[p03_sp_procedural_memory_builder]] | downstream | 0.55 |
| [[bld_architecture_skill]] | downstream | 0.54 |
| [[bld_system_prompt_skill]] | downstream | 0.51 |
| [[bld_memory_skill]] | downstream | 0.50 |
| [[skill-builder]] | downstream | 0.47 |
| [[p10_mem_procedural_memory_builder]] | downstream | 0.46 |
| [[bld_collaboration_procedural_memory]] | downstream | 0.45 |
