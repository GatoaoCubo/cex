---
kind: instruction
id: bld_instruction_role_assignment
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for role_assignment
quality: 8.9
title: "Instruction Role Assignment"
version: "1.0.0"
author: n03_wave8_builder
tags: [role_assignment, builder, instruction, composable, crewai]
tldr: "Step-by-step production process for role_assignment"
domain: "role_assignment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Phase 1: RESEARCH
1. Identify role_name and the crew(s) that will use it (scope).
2. Select agent_id source: `.claude/agents/{slug}.md` for sub-agents, `N0x/agents/*` for nucleus agents.
3. Confirm the agent exists and read its manifest for native capability + tool list.
4. Draft responsibilities as 3-5 crisp bullet points (inputs consumed, outputs produced, invariants).
5. Identify potential delegate roles in target crew_template; build can_delegate_to list.
6. Review agent toolkit; select tools_allowed subset appropriate to this role (least-privilege).

## Phase 2: COMPOSE
1. Reference SCHEMA.md for required fields (role_name, agent_id, responsibilities, tools_allowed, delegation_policy, backstory, goal).
2. Populate OUTPUT_TEMPLATE.md with binding details.
3. Craft `backstory` as 2-3 sentence persona hook grounded in domain (CrewAI idiom: "You are a...").
4. Craft `goal` as one-sentence measurable outcome ("Produce X such that Y holds").
5. Set `delegation_policy.can_delegate_to` list (role_names, not agent_ids) or null if non-delegating.
6. Set `delegation_policy.conditions`: rule-based triggers (on quality < 8, on keyword match, on timeout).
7. List `tools_allowed` as explicit subset of agent's native toolkit; prefix with `-` to exclude.
8. Proofread: agent_id resolvable, responsibilities checkable, tools subset valid.

## Phase 3: VALIDATE
- [ ] agent_id resolves to an existing .claude/agents/ OR N0x/agents/ artifact.
- [ ] role_name is snake_case, unique within target crew_template.
- [ ] responsibilities list has 3-5 bullets, each testable.
- [ ] tools_allowed is a subset of the agent's native toolkit.
- [ ] delegation_policy.can_delegate_to list references valid role names (not agent_ids).
- [ ] backstory <= 300 chars, goal <= 150 chars.
- [ ] File size <= 3072 bytes.
