---
kind: instruction
id: bld_instruction_agent
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for agent
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Agent"
version: "1.0.0"
author: n03_builder
tags: [agent, builder, examples]
tldr: "Golden and anti-examples for agent construction, demonstrating ideal structure and common pitfalls."
domain: "agent construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - agent-builder
  - bld_collaboration_agent
  - bld_instruction_boot_config
  - p03_sp_agent_builder
  - p01_kc_agent
  - p11_qg_agent
  - bld_knowledge_card_agent
  - bld_instruction_golden_test
  - p03_ins_mental_model
  - bld_instruction_action_prompt
---

# Instructions: How to Produce an agent
## Phase 1: RESEARCH
1. Identify the agent's primary domain and the specific function it performs within that domain
2. Define the agent's persona: 2-3 sentences describing who this agent is and how it operates
3. List 4-6 capabilities as action verbs (e.g., "analyzes", "generates", "validates", "routes")
4. Identify constraints: what this agent must never do, what it defers to other agents
5. Determine agent_group assignment: which agent_group owns this agent (or mark agnostic)
6. Search for existing agents in the same domain to avoid duplicate definitions
7. List tools required: MCP servers, scripts, APIs, file system paths this agent needs
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Fill frontmatter: all 10 required fields (quality: null, never self-score)
4. Set llm_function: BECOME (always for agents, never override)
5. Write Identity section: 2-3 sentences on persona, domain, and primary function
6. Write Capabilities section: 4-6 bullets, each a concrete action this agent performs
7. Write Routing section: keywords and triggers that cause this agent to be selected
8. Write Crew Role section: the question this agent answers, and explicit exclusions
9. Write agent_package skeleton: list 10 minimum builder specs with correct naming convention
10. Set capabilities_count to match actual bullets written
11. Check body <= 5120 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. HARD gate: id matches `p02_agent_` pattern
3. HARD gate: kind == agent
4. HARD gate: quality == null
5. HARD gate: agent_package lists >= 10 files
6. HARD gate: capabilities >= 4 bullets in body
7. HARD gate: llm_function == BECOME
8. HARD gate: agent_group field is set (not blank)
9. Cross-check: is persona expressed only in Identity, not scattered across other sections?
10. Cross-check: do capabilities overlap with any agent assigned to the same agent_group?
11. If score < 8.0: revise before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify agent
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | agent construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent-builder]] | upstream | 0.49 |
| [[bld_collaboration_agent]] | downstream | 0.42 |
| [[bld_instruction_boot_config]] | sibling | 0.41 |
| [[p03_sp_agent_builder]] | related | 0.40 |
| [[p01_kc_agent]] | upstream | 0.39 |
| [[p11_qg_agent]] | downstream | 0.38 |
| [[bld_knowledge_card_agent]] | upstream | 0.38 |
| [[bld_instruction_golden_test]] | sibling | 0.37 |
| [[p03_ins_mental_model]] | sibling | 0.37 |
| [[bld_instruction_action_prompt]] | sibling | 0.35 |
