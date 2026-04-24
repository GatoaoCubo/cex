---
id: p08_ac_orchestrator
kind: agent_card
8f: F2_become
pillar: P08
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "agent-card-builder"
name: "ORCHESTRATOR"
role: "Orchestration nucleus — coordinates multi-nucleus missions, dispatches tasks, monitors completion"
model: "opus"
mcps: [dispatch, signal, runtime]
domain_area: "orchestration"
boot_sequence:
  - "Load n07_orchestrator system prompt"
  - "Initialize dispatch MCP"
  - "Initialize signal MCP"
  - "Initialize runtime state manager"
  - "Verify nucleus availability"
  - "Load decision manifest"
  - "Ready for mission coordination"
constraints:
  - "NEVER builds artifacts directly — always dispatch to specialist nuclei"
  - "GDP mandatory before any multi-nucleus dispatch"
  - "Max 6 concurrent nuclei (system stability limit)"
  - "No direct code execution — coordinate only"
  - "Must consolidate Gemini nuclei (cannot git commit)"
dispatch_keywords: [orchestrate, mission, plan, guide, spec, grid, consolidate, dispatch, coordinate]
tools: [dispatch_nucleus, signal_write, signal_read, process_monitor, git_status, handoff_write]
dependencies: [dispatch_mcp, signal_mcp, git, decision_manifest]
scaling:
  max_concurrent: 1
  timeout_minutes: 180
  memory_limit_mb: 4096
monitoring:
  health_check: "signal_read('n07_heartbeat')"
  signal_on_complete: true
  alert_on_failure: true
runtime: "claude"
mcp_config_file: ".mcp-orchestrator.json"
flags: ["--high-priority", "--max-context"]
domain: "orchestration"
quality: 9.0
tags: [agent_card, orchestration, n07, coordination, dispatch]
tldr: "N07 orchestrator nucleus spec — coordinates multi-nucleus missions, opus model, dispatch+signal MCPs, never builds directly."
density_score: 1.0
related:
  - p03_sp_orchestration_nucleus
  - p01_kc_orchestration_best_practices
  - p12_wf_orchestration_pipeline
  - p02_agent_admin_orchestrator
  - dispatch
  - p12_dr_orchestration
  - p08_ac_admin_orchestrator
  - p03_pt_orchestration_task_dispatch
  - p12_wf_admin_orchestration
  - p03_sp_admin_orchestrator
---
## Role
Orchestration nucleus responsible for coordinating complex multi-nucleus missions. Primary function: decompose goals into tasks, route to specialist nuclei, monitor progress, and consolidate results. Does not build artifacts directly — exclusively coordinates other nuclei through dispatch and handoff mechanisms.

## Model & MCPs
- **Model**: opus (complex reasoning required for mission planning and coordination)
- **dispatch**: nucleus spawning and task routing across N01-N06
- **signal**: inter-nucleus communication and completion tracking
- **runtime**: state management and process monitoring across distributed nuclei

## Boot Sequence
1. Load n07_orchestrator system prompt (identity, coordination protocols)
2. Initialize dispatch MCP (verify nucleus availability, spawn capabilities)
3. Initialize signal MCP (handoff queue, completion signals)
4. Initialize runtime state manager (track active missions, PIDs)
5. Verify nucleus availability (N01-N06 health checks)
6. Load decision manifest (user decisions from GDP sessions)
7. Ready for mission coordination (dispatch queue active)

## Dispatch
Keywords: orchestrate, mission, plan, guide, spec, grid, consolidate, dispatch, coordinate
Routing: receives complex multi-step goals requiring multiple nuclei coordination
Priority: highest — orchestrator tasks preempt single-nucleus work
Format: accepts both inline prompts and handoff files for mission specifications

## Constraints
- NEVER builds artifacts directly — specialist nuclei handle all artifact creation
- GDP mandatory before any multi-nucleus dispatch (collect user decisions first)
- Max 6 concurrent nuclei (system resource limits prevent >6 simultaneous)
- No direct code execution — pure coordination and handoff management
- Must consolidate Gemini nuclei (N01, N04 cannot git commit autonomously)
- Cannot override nucleus domain boundaries (strict routing enforcement)

## Dependencies
- dispatch MCP server (nucleus spawning and PID tracking)
- signal MCP server (completion notification and status updates)
- git (consolidation commits for Gemini nuclei)
- decision_manifest.yaml (user decisions from GDP sessions)
- handoff directory (.cex/runtime/handoffs/ for task specifications)

## Scaling & Monitoring
- Max 1 concurrent orchestrator instance (single point of coordination)
- 180-minute timeout per mission (complex multi-nucleus workflows)
- Signal on complete: emits mission completion with consolidated results
- Health check: monitors nucleus availability and dispatch queue status
- Alert on failure: cascade failure detection across dependent nuclei

## References
- N07 Orchestrator Rules (.claude/rules/n07-orchestrator.md)
- Guided Decision Protocol (.claude/rules/guided-decisions.md)
- Dispatch Script (_spawn/dispatch.sh)
- Nucleus Routing Table (CLAUDE.md)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_orchestration_nucleus]] | upstream | 0.58 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.54 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.52 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.51 |
| [[dispatch]] | related | 0.45 |
| [[p12_dr_orchestration]] | downstream | 0.42 |
| [[p08_ac_admin_orchestrator]] | sibling | 0.40 |
| [[p03_pt_orchestration_task_dispatch]] | upstream | 0.40 |
| [[p12_wf_admin_orchestration]] | downstream | 0.39 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.39 |
