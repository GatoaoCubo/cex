---
kind: examples
id: bld_examples_workflow
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of workflow artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: workflow-builder
## Golden Example
INPUT: "Create workflow for research-then-build mission with SHAKA and EDISON"
OUTPUT:
```yaml
id: p12_wf_research_build_mission
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
title: "Research Then Build Mission"
steps_count: 3
execution: mixed
directors: [shaka, edison]
timeout: 5400
retry_policy: per_step
depends_on: []
signals: [complete, error]
spawn_configs: [p12_spawn_shaka_solo_research, p12_spawn_edison_solo_build]
domain: "orchestration"
quality: null
tags: [workflow, research, build, multi-director]
tldr: "3-step mixed workflow: SHAKA researches, EDISON builds from findings, orchestrator consolidates"
density_score: 0.90
```
## Purpose
Orchestrates a research-then-build mission where SHAKA gathers market intelligence,
EDISON implements based on findings, and orchestrator consolidates results. Steps 1-2 are
sequential (build depends on research), step 3 runs after both complete.
## Steps
### Step 1: Market Research [shaka]
- **Agent**: shaka (sonnet)
- **Action**: Research target market and produce knowledge cards
- **Input**: research brief from handoff file
- **Output**: 3-5 knowledge cards committed to records/pool/
- **Signal**: shaka_complete with quality score
- **Depends on**: none (first step)
### Step 2: Implementation [edison]
- **Agent**: edison (opus)
- **Action**: Build feature using research findings from Step 1
- **Input**: knowledge cards produced by SHAKA
- **Output**: implemented feature with tests passing
- **Signal**: edison_complete with quality score
- **Depends on**: Step 1
### Step 3: Consolidation [orchestrator]
- **Agent**: orchestrator (opus)
- **Action**: Review outputs, archive handoffs, push to remote
- **Input**: signals from Steps 1-2, git log
- **Output**: consolidated commit, archived handoffs
- **Signal**: workflow_complete
- **Depends on**: Steps 1, 2
## Dependencies
- Handoff files must exist for SHAKA and EDISON before workflow starts
- spawn_configs referenced must be valid (p12_spawn_shaka_solo_research, p12_spawn_edison_solo_build)
## Signals
- **On step complete**: {sat}_complete signal emitted (see signal-builder)
- **On workflow complete**: workflow_complete signal with aggregate quality
- **On error**: {sat}_error signal, retry per step (max 1), then escalate to orchestrator
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p12_wf_ pattern (H02 pass)
- kind: workflow (H04 pass)
- 20 required fields present (H06 pass)
- body has Purpose + Steps + Dependencies + Signals (H07 pass)
- steps_count: 3 matches actual 3 steps (H08 pass)
- Each step has Agent/Action/Input/Output/Signal/Depends (S03 pass)
- Dependencies section lists prerequisites (S05 pass)
- Signals reference signal-builder conventions (S06 pass)
- No prompt chaining in body (S08 pass)
## Anti-Example
INPUT: "Create a workflow for doing stuff"
BAD OUTPUT:
```yaml
id: my_workflow
kind: flow
steps: 3
quality: 8.5
```
This workflow does research and then builds things. First SHAKA does research,
then EDISON builds. It's a great workflow that produces high quality output.
FAILURES:
1. id: no `p12_wf_` prefix -> H02 FAIL
2. kind: "flow" not "workflow" -> H04 FAIL
3. pillar: missing -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. Missing fields: version, created, updated, author, execution, directors, domain, tags, tldr -> H06 FAIL
6. No ## Steps section with structured steps -> H07 FAIL
7. Body is filler prose ("great workflow", "high quality") -> S10 FAIL
8. Steps lack Agent/Action/Input/Output structure -> S03 FAIL
9. No Dependencies or Signals sections -> S05, S06 FAIL
10. No signal references -> S09 FAIL
