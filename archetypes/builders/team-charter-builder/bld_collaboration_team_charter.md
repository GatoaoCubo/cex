---
kind: collaboration
id: bld_collaboration_team_charter
pillar: P12
llm_function: COLLABORATE
purpose: How team_charter-builder works in crews with other builders
quality: 9.1
title: "Collaboration Team Charter"
version: "1.0.0"
author: n06_wave8
tags: [team_charter, builder, collaboration, governance]
tldr: "How team_charter-builder works in crews with other builders"
domain: "team_charter construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role
Authors the governance contract that authorizes a crew instance to execute autonomously, ensuring all budget, quality, and termination constraints are explicit before dispatch begins. Acts as the formal handshake between user intent (GDP) and autonomous execution (nuclei).

## Receives From
| Source              | What                             | Format   |
|---------------------|----------------------------------|----------|
| GDP decision manifest | User's WHAT decisions (tone, scope, budget, audience) | YAML |
| crew_template_ref   | Crew capability profile + nucleus list | Markdown |
| N07 mission plan    | Wave structure, artifact list, deadlines | Markdown |
| N06 (commercial)    | Budget ceiling and ROI targets | YAML/table |

## Produces For
| Consumer            | What                             | Format   |
|---------------------|----------------------------------|----------|
| N07 orchestrator    | Authorized scope + termination criteria | Markdown |
| Nucleus handoffs    | Quality gate thresholds + budget context | reference |
| cex_mission_runner  | Termination criteria for signal polling | structured |
| Audit trail         | Signed governance record for post-mission review | Markdown |

## Boundary
Does NOT produce workflow DAGs (handled by `dag-builder`), dispatch rules (handled by `dispatch-rule-builder`), or nucleus handoffs (authored by N07 directly). Does NOT handle crew_template definitions (handled by `spawn-config-builder`). Legal compliance clauses beyond IP/cost are out of scope -- escalate to user.

## Collaboration Pattern
1. N07 runs GDP with user -> decision manifest written.
2. N07 calls team_charter_builder -> charter authored with manifest as input.
3. Charter is reviewed (N07 validates all required fields).
4. N07 writes handoffs that REFERENCE the charter (not duplicate it).
5. Nuclei operate within charter constraints; N07 enforces termination criteria via cex_mission_runner.
6. On mission complete: charter is archived to `.cex/runtime/decisions/archive/`.
