---
kind: knowledge_card
id: bld_knowledge_card_role_assignment
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for role_assignment production
quality: 9.2
title: "Knowledge Card Role Assignment"
version: "1.0.0"
author: n03_wave8_builder
tags: [role_assignment, builder, knowledge_card, composable, crewai, autogen, swarm]
tldr: "Domain knowledge for role_assignment production"
domain: "role_assignment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
---

## Domain Overview
Role assignments are the atomic role-binding primitive of composable crews: one artifact = one (agent, role, tools, delegation, backstory, goal) tuple. They map directly to the CrewAI Agent class, AutoGen ConversableAgent, and OpenAI Swarm Agent. Crew_template instantiates a team by referencing N role_assignments; supervisor spawns the team at runtime. Decoupling role binding from crew composition enables role reuse (one `peer_reviewer` atom participates in 10+ crews) and agent swap (swap the underlying agent_id without rewriting every crew).

The CrewAI idiom of `role + goal + backstory` (the "persona triad") is the empirical winner for steerability: a clear role-descriptor primes task framing, a measurable goal primes stopping criteria, and a domain-grounded backstory primes tone and depth. AutoGen extends this with `tools` scoping; OpenAI Swarm adds `transfer_to_*` functions that map to CEX delegation_policy. Google A2A standardizes agent_id as a URI, inspiring CEX's `.claude/agents/` and `N0x/agents/` registry paths.

## Key Concepts
| Concept | Definition | Source |
|---------|------------|--------|
| Role Name | snake_case identifier unique within a crew_template | CEX convention |
| Agent ID | Registry path to agent manifest (.claude/agents/ or N0x/agents/) | Google A2A inspiration |
| Responsibilities | 3-5 testable obligations (inputs, outputs, invariants) | CrewAI best-practice |
| Tools Allowed | Least-privilege subset of agent's native toolkit | AutoGen ConversableAgent |
| Delegation Policy | can_delegate_to (role_names) + conditions | CrewAI hierarchical + OpenAI transfer |
| Backstory | 2-3 sentence persona hook grounded in domain | CrewAI Agent API |
| Goal | One-sentence measurable outcome | CrewAI Agent API |
| Persona Triad | role + goal + backstory (empirical steerability winner) | CrewAI research |

## Industry Standards
- CrewAI Agent class (v0.80+): `Agent(role, goal, backstory, tools, allow_delegation)`.
- Microsoft AutoGen ConversableAgent: `name`, `system_message`, `tools`, `is_termination_msg`.
- OpenAI Agents SDK v0.6+: `Agent(name, instructions, handoffs=[transfer_to_X])`.
- Google A2A AgentCard schema: agent_id as URI with optional cryptographic signature.
- LangGraph node naming: convention of snake_case role identifiers.

## Common Patterns
1. **Least-privilege tools**: start from empty set; add only tools the role demonstrably needs.
2. **Persona triad**: role_descriptor + measurable_goal + domain-grounded_backstory; each must be non-generic.
3. **Delegation by role_name**: never leak agent_ids into can_delegate_to (breaks crew portability).
4. **Testable responsibilities**: phrase each bullet as an observable input/output contract.
5. **Runtime notes by process**: document how the role behaves in sequential vs hierarchical vs consensus.

## Pitfalls
- Inlining agent identity in `agent_id` (stringified prompt). Breaks H04, loses registry link.
- Wildcard `tools_allowed: [*]` (phantom tools, over-privilege). Fails H06.
- Activity-goals ("do research") instead of outcome-goals ("produce 8-12 sources with conf >= 0.75").
- Generic backstories ("helpful assistant") lose the steerability gain; always ground in domain.
- `can_delegate_to` listing agent_ids (portability break, fails H07).
- Role reused across crews with incompatible tool requirements -- split into two role_assignments.
