---
kind: architecture
id: bld_architecture_skill
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of skill — inventory, dependencies, and architectural position
quality: 9.2
title: "Architecture Skill"
version: "1.0.0"
author: n03_builder
tags: [skill, builder, examples]
tldr: "Golden and anti-examples for skill construction, demonstrating ideal structure and common pitfalls."
domain: "skill construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - skill-builder
  - bld_collaboration_skill
  - p03_ins_skill_builder
  - bld_system_prompt_skill
  - p11_qg_skill
  - bld_knowledge_card_skill
  - p01_kc_skill
  - procedural-memory-builder
  - bld_memory_skill
  - bld_schema_skill
---

# Architecture: skill in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, trigger, phases_count, etc.) | skill-builder | active |
| trigger_definition | What activates the skill (slash command, keyword, event, or programmatic call) | author | active |
| phase_list | Ordered execution phases with input/output per phase | author | active |
| input_contract | Typed specification of what the skill receives at invocation | author | active |
| output_contract | Typed specification of what the skill produces on completion | author | active |
| user_invocable_flag | Whether the skill is triggered by user (slash command) or agent-only | author | active |
## Dependency Graph
```
agent           --invokes-->    skill  --produces-->     skill_output
trigger_event   --activates-->  skill  --signals-->      completion_signal
skill           --depends-->    knowledge_card
```
| From | To | Type | Data |
|------|----|------|------|
| agent (P02) | skill | consumes | agent invokes skill for reusable capability |
| trigger_event | skill | data_flow | event or command that activates the skill |
| skill | skill_output | produces | structured result from phase execution |
| skill | completion_signal (P12) | signals | emitted when all phases complete |
| knowledge_card (P01) | skill | dependency | domain knowledge injected into skill phases |
| action_prompt (P03) | skill | dependency | individual phases may use action prompts |
## Boundary Table
| skill IS | skill IS NOT |
|----------|--------------|
| A reusable capability with structured phases and trigger | An agent identity with persona and rules (system_prompt P03) |
| Triggered by slash command, keyword, event, or API call | A one-time task prompt (action_prompt P03) |
| Multi-phase with defined input/output per phase | An event interceptor without phases (hook P04) |
| User-invocable or agent-only based on flag | A protocol server exposing tools (mcp_server P04) |
| Produces structured output on completion | A pluggable extension with lifecycle hooks (plugin P04) |
| Scoped to one capability domain | A multi-agent_group orchestration (workflow P12) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Trigger | trigger_definition, user_invocable_flag | Define how and by whom the skill is activated |
| Contract | frontmatter, input_contract, output_contract | Specify typed I/O for the skill |
| Execution | phase_list, action_prompt | Ordered phases with per-phase input/output |
| Context | knowledge_card | Domain knowledge supporting phase execution |
| Output | skill_output, completion_signal | Deliver result and signal completion |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `skill-builder` for pipeline function `CALL`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[skill-builder]] | upstream | 0.70 |
| [[bld_collaboration_skill]] | downstream | 0.68 |
| [[p03_ins_skill_builder]] | upstream | 0.61 |
| [[bld_system_prompt_skill]] | upstream | 0.57 |
| [[p11_qg_skill]] | downstream | 0.55 |
| [[bld_knowledge_card_skill]] | upstream | 0.51 |
| [[p01_kc_skill]] | upstream | 0.50 |
| [[procedural-memory-builder]] | downstream | 0.47 |
| [[bld_memory_skill]] | downstream | 0.46 |
| [[bld_schema_skill]] | upstream | 0.45 |
