---
kind: collaboration
id: bld_collaboration_role_assignment
pillar: P12
llm_function: COLLABORATE
purpose: How role_assignment-builder works in crews with other builders
quality: 8.9
title: "Collaboration Role Assignment"
version: "1.0.0"
author: n03_wave8_builder
tags: [role_assignment, builder, collaboration, composable, crewai]
tldr: "How role_assignment-builder works in crews with other builders"
domain: "role_assignment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_collaboration_crew_template
  - role-assignment-builder
  - bld_architecture_kind
  - bld_collaboration_toolkit
  - bld_collaboration_agent
  - kind-builder
  - bld_collaboration_builder
  - bld_collaboration_system_prompt
  - bld_collaboration_response_format
  - bld_collaboration_quality_gate
---

## Crew Role
Acts as the atomic role-binding unit consumed by crew_template. Upstream from crew-template-builder (composition) and supervisor-builder (runtime instantiation). Sibling to agent-builder (provides identity source) and toolkit-builder (provides native tool set).

## Receives From
| Builder                   | What                              | Format            |
|---------------------------|-----------------------------------|-------------------|
| agent-builder             | agent_id registry path + manifest | .claude/agents/*.md |
| toolkit-builder           | Agent's native toolkit (source)   | yaml tool list    |
| N07 orchestrator          | Role scoping hints (goal, domain) | handoff frontmatter |
| crew-template-builder     | Target crew context (constraints) | p12_ct_*.md       |

## Produces For
| Builder                   | What                             | Format            |
|---------------------------|----------------------------------|-------------------|
| crew-template-builder     | Atomic role_assignment reference | p02_ra_*.md       |
| supervisor-builder        | Runtime-ready role spec          | compiled yaml     |
| workflow-builder          | Role step identity for workflows | artifact ref      |
| agent-package-builder     | Role binding in distributable pkg| bundled artifact  |

## Boundary
Does NOT define agent identity (that is agent-builder's job). Does NOT compose the full crew blueprint (crew-template-builder does). Does NOT execute the role at runtime (supervisor-builder handles spawn). Does NOT provide the underlying toolkit (toolkit-builder owns that). Owns ONLY the binding tuple: (role_name, agent_id, responsibilities, tools_allowed, delegation_policy, backstory, goal).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_crew_template]] | sibling | 0.49 |
| [[role-assignment-builder]] | upstream | 0.44 |
| [[bld_architecture_kind]] | upstream | 0.40 |
| [[bld_collaboration_toolkit]] | sibling | 0.39 |
| [[bld_collaboration_agent]] | sibling | 0.39 |
| [[kind-builder]] | upstream | 0.36 |
| [[bld_collaboration_builder]] | sibling | 0.36 |
| [[bld_collaboration_system_prompt]] | sibling | 0.33 |
| [[bld_collaboration_response_format]] | sibling | 0.33 |
| [[bld_collaboration_quality_gate]] | sibling | 0.33 |
