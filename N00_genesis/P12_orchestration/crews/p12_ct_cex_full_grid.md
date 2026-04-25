---
id: p12_ct_cex_full_grid
kind: crew_template
8f: F2_become
pillar: P12
llm_function: CALL
crew_name: cex_full_grid
purpose: "Instantiate the full CEX grid -- N07 as hierarchical manager, N01-N06 as parallel workers. Use for any mission that spans multiple domains."
process: hierarchical
crewai_equivalent: "Process.hierarchical"
autogen_equivalent: "GroupChat.manager + 6 agents"
swarm_equivalent: "n07 orchestrates n01..n06 in parallel"
handoff_protocol_id: a2a-task-hierarchical
quality: 8.8
density_score: 0.88
title: "CEX Full Grid -- All Nuclei Crew"
version: 1.0.0
roles: 7
author: n04_knowledge
nucleus: n07
tags: [crew_template, full_grid, orchestration, composable, cex_universal]
tldr: "Master crew: N07 manages N01-N06 in parallel. Activate for any multi-domain mission."
domain: "full CEX pipeline orchestration"
created: "2026-04-18"
updated: "2026-04-18"
related:
  - p01_kc_orchestration_best_practices
  - p12_wf_admin_orchestration
  - p01_kc_orchestration
  - p03_sp_admin_orchestrator
  - n07_output_orchestration_audit
  - p03_sp_orchestration_nucleus
  - dispatch
  - p02_agent_creation_nucleus
  - p02_agent_admin_orchestrator
  - p12_wf_orchestration_pipeline
---

## Overview

The CEX Full Grid crew instantiates the complete nucleus set (N01-N06) under N07 orchestration.
Use when a mission requires output from 2+ domain nuclei and the deliverables are interdependent.
N07 acts as hierarchical manager: it writes handoffs, dispatches workers, monitors signals,
and consolidates artifacts after all workers complete.

Each worker nucleus follows its own F1..F8 pipeline internally. N07 does not build directly --
it authors handoffs (F6 PRODUCE) that carry the full artifact specification to each nucleus.

## Roles

| Role | Nucleus | Sin Lens | Goal | Primary Tools | Handoff To |
|------|---------|----------|------|---------------|------------|
| orchestrator | N07 | Orchestrating Sloth | dispatch + monitor + consolidate | dispatch.sh, signal_writer, cex_doctor | all workers |
| researcher | N01 | Analytical Envy | produce knowledge_cards + competitive intel | cex_retriever, research_pipeline | N02, N04, N06 |
| copywriter | N02 | Creative Lust | produce campaign copy + landing pages | prompt-template-builder, landing-page-builder | N05, N06 |
| builder | N03 | Inventive Pride | construct all typed artifacts via 8F | all 301 builders, cex_compile | N04, N05 |
| librarian | N04 | Knowledge Gluttony | index + retrieve + taxonomy + RAG | cex_index, cex_retriever, cex_query | all (indexes) |
| operator | N05 | Gating Wrath | test + deploy + quality gate all outputs | cex_doctor, cex_system_test, cex_hooks | N07 (verdicts) |
| monetizer | N06 | Strategic Greed | pricing + funnels + charters | content-monetization-builder, subscription-tier-builder | N02, N07 |

## Process Topology

Topology: `hierarchical`. N07 is the manager. N01-N06 are workers.

```
N07 (manager)
  |
  +-- Wave 1 (parallel): N01 research + N04 index refresh
  |     N01: produce knowledge_cards for domain
  |     N04: refresh capability_registry + retrieval index
  |
  +-- Wave 2 (parallel): N03 build + N06 commercial
  |     N03: construct typed artifacts from handoff spec
  |     N06: produce monetization model + pricing tiers
  |
  +-- Wave 3 (parallel): N02 copy + N05 ops gate
  |     N02: produce campaign copy grounded on N01 + N06 output
  |     N05: run quality gate + CI check on N03 artifacts
  |
  +-- Consolidate (N07):
        verify deliverables, archive signals, commit, report
```

**Rationale for hierarchical process:**
- N01 must complete before N02 (copywriter needs positioning brief)
- N03 must complete before N05 (operator tests what builder produces)
- N06 must complete before N02 (copy needs pricing data)
- N07 manages wave sequencing and can adapt if a nucleus signals early

## Handoff Protocol

`a2a-task-hierarchical` -- N07 writes a `.md` handoff for each nucleus, copies it to
`n0X_task.md` (root), then dispatches. Each nucleus reads its task from the handoff file.
On completion, each nucleus emits a JSON signal and a git commit.

N07 detects completion via:
1. `git log --oneline --since="X minutes ago"` -- commit presence
2. `.cex/runtime/signals/signal_n0X_*.json` -- signal file presence
3. `bash _spawn/dispatch.sh status` -- PID alive check

## Activation

```bash
# Standard grid dispatch (all 6 workers, parallel)
bash _spawn/dispatch.sh grid CEX_FULL_GRID

# Solo dispatch for a single worker
bash _spawn/dispatch.sh solo n03 "task description"

# Using the crew runner (dry-run)
python _tools/cex_crew.py show cex_full_grid

# Using the crew runner (live LLM calls)
python _tools/cex_crew.py run cex_full_grid \
    --charter N07_admin/charters/team_charter_active.md \
    --execute

# Mission runner (blocking, multi-wave, autonomous)
python _tools/cex_mission_runner.py \
    --plan .cex/runtime/plans/plan_MISSION.md \
    --mission MISSION_NAME \
    --timeout 3600
```

## Memory Scope

| Role | Scope | Retention |
|------|-------|-----------|
| orchestrator (N07) | global | persistent (decision manifest, signal archive) |
| researcher (N01) | shared | persistent (KCs saved to P01) |
| copywriter (N02) | shared | per-crew-instance |
| builder (N03) | shared | persistent (artifacts committed to repo) |
| librarian (N04) | shared | persistent (index refreshed in P10) |
| operator (N05) | shared | per-crew-instance + regression_check archive |
| monetizer (N06) | shared | per-crew-instance + pricing KCs |

## Quality Gate

All of the following must be true before N07 consolidates:

- [ ] All 6 workers (N01-N06) have emitted a completion signal
- [ ] All 6 signals carry quality score >= 8.0
- [ ] `python _tools/cex_doctor.py` passes (no new FAILs)
- [ ] Every handoff deliverable listed in `n0X_task.md` exists on disk
- [ ] Git log shows commits from each worker nucleus
- [ ] No orphan processes (verify via `bash _spawn/dispatch.sh status`)

If any gate fails: N07 re-dispatches the failed nucleus (max 1 retry)
or escalates to the user with a failure report.

## Success Criteria

- [ ] All 6 nuclei delivered artifacts within their primary pillar(s)
- [ ] N04 capability_registry refreshed (all 7 nuclei visible)
- [ ] N05 quality gate passed on N03 artifacts
- [ ] N07 consolidation commit exists: `[N07] consolidate: <MISSION_NAME>`
- [ ] `.cex/runtime/signals/` contains 6 completion signal files
- [ ] Decision manifest preserved at `.cex/runtime/decisions/decision_manifest.yaml`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_orchestration_best_practices]] | upstream | 0.46 |
| [[p12_wf_admin_orchestration]] | related | 0.44 |
| [[p01_kc_orchestration]] | upstream | 0.43 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.43 |
| [[n07_output_orchestration_audit]] | related | 0.42 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.42 |
| [[dispatch]] | upstream | 0.42 |
| [[p02_agent_creation_nucleus]] | upstream | 0.42 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.42 |
| [[p12_wf_orchestration_pipeline]] | related | 0.41 |
