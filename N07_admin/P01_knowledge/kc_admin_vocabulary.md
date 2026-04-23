---
id: kc_admin_vocabulary
kind: knowledge_card
type: controlled_vocabulary
pillar: P01
title: "Orchestration Domain Vocabulary"
version: 1.0.0
created: 2026-04-21
updated: 2026-04-21
author: n07_orchestrator
domain: orchestration
quality: 7.5
tags: [vocabulary, orchestration, dispatch, n07, controlled-vocabulary]
tldr: "Canonical terms for N07 orchestration domain. Loaded at F2b SPEAK to prevent vocabulary drift."
when_to_use: "Before any N07 artifact generation. Loaded automatically during 8F pipeline."
keywords: [orchestration, dispatch, grid, crew, wave, handoff, signal, consolidate]
density_score: null
related:
  - nucleus_def_n07
  - agent_card_n07
  - kc_orchestration_best_practices
  - spec_metaphor_dictionary
---

# Orchestration Domain Vocabulary

## Canonical Terms

| Term | Definition | N07 Application | Anti-pattern |
|------|-----------|-----------------|-------------|
| dispatch | Send a structured task to a nucleus via handoff file | N07 writes handoff, invokes spawn script | "assign", "delegate" (too vague) |
| handoff | Typed markdown file containing task spec, context refs, and expected output | `.cex/runtime/handoffs/{MISSION}_{nucleus}.md` | "instructions", "todo" |
| signal | JSON completion notification from a nucleus to the orchestrator | `.cex/runtime/signals/signal_{nucleus}_{mission}.json` | "notification", "callback" |
| grid | Parallel dispatch of up to 6 nuclei on independent tasks | `bash _spawn/dispatch.sh grid MISSION` | "batch", "parallel run" |
| wave | Sequential group within a mission; waves execute in order, nuclei within a wave run in parallel | Wave 1 (foundation) -> Wave 2 (content) -> Wave 3 (validation) | "phase", "step" (too generic) |
| consolidate | Post-dispatch verification: check deliverables, kill processes, run doctor, commit | `/consolidate` skill or autonomous lifecycle | "cleanup", "wrap up" |
| crew | Multi-role team with defined topology and handoff protocol for producing one coherent deliverable | `python _tools/cex_crew.py run <name>` | "team" (lacks typed topology) |
| swarm | N parallel builders of the same kind, each producing one independent artifact | `dispatch.sh swarm agent 5` | "batch build" |
| solo | Single-nucleus dispatch for focused task execution | `dispatch.sh solo n03 "task"` | "one-off" |
| mission | End-to-end goal decomposed into waves, dispatched as a grid, consolidated on completion | `/mission <goal>` | "project", "plan" (different CEX concepts) |
| GDP | Guided Decision Protocol: user decides WHAT (subjective), LLM decides HOW (structural) | `decision_manifest.yaml` bridges co-pilot and autonomous modes | "prompting", "configuration" |
| intent resolution | Mapping user natural language to `{kind, pillar, nucleus, verb}` tuple | `cex_intent_resolver.py` + `p03_pc_cex_universal.md` | "parsing", "NLU" (too narrow) |
| 8F pipeline | 8-function reasoning protocol: CONSTRAIN, BECOME, INJECT, REASON, CALL, PRODUCE, GOVERN, COLLABORATE | Every task, every nucleus, no exceptions | "workflow", "checklist" |
| quality gate | F7 GOVERN validation: 7 hard gates + 12-point checklist + 5D scoring | `cex_score.py` assigns score; `quality: null` on creation | "review", "approval" |
| fractal | Convention-over-configuration: every nucleus mirrors the same 12-pillar structure | N00 defines the template; N01-N07 instantiate it | "template", "boilerplate" |
| nucleus | Full 12-pillar AI department with sin lens, identity, and autonomous execution capability | N01-N07 operational; N00 archetype; N08+ community | "agent" (too narrow -- nucleus = department) |

## Cross-Nucleus Shared Terms (DO NOT REDEFINE)

These terms are defined in N00_genesis and must not be redefined:
- **kind**: atomic artifact type from the 293-kind taxonomy
- **pillar**: P01-P12 domain grouping
- **builder**: 12 ISOs teaching 8F how to produce one kind
- **ISO**: individual instruction file within a builder, 1:1 with a pillar
- **artifact**: structured `.md` file with YAML frontmatter + markdown body
- **compiled**: auto-generated `.yaml` from source `.md` via `cex_compile.py`

## Domain-Specific Extensions

| New Term | Definition | Maps to Industry Standard |
|----------|-----------|--------------------------|
| orchestrating sloth | N07's sin lens: never build, always dispatch; laziness = delegation purity | agent orchestration pattern |
| autonomous lifecycle | Post-dispatch loop: work on backlog while polling for nucleus completion | event-driven orchestration |
| depth amplifier | Handoff enrichment pattern: multi-artifact, cross-reference, research phase, quality loop | context engineering |
| session-aware dispatch | PID tracking with session ID to prevent cross-orchestrator process interference | process isolation |
| kill tree | `taskkill /F /PID <pid> /T` to terminate parent + all descendant processes | recursive process termination |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[nucleus_def_n07]] | source | -- |
| [[agent_card_n07]] | source | -- |
| [[kc_orchestration_best_practices]] | upstream | -- |
| [[spec_metaphor_dictionary]] | parent | -- |
