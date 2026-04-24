---
id: p10_rs_n07
kind: runtime_state
8f: F8_collaborate
pillar: P10
title: "Runtime State: N07 Orchestrator"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "runtime-state-builder"
agent: "n07_orchestrator"
persistence: "session"
domain: "multi-nucleus orchestration"
quality: 9.1
tags: [runtime-state, n07, orchestration, routing, mission-control]
tldr: "N07 session-scoped mutable state: active wave, PID registry, provider health, GDP manifest, quality ledger."
routing_mode: "rule_based"
priority_count: 5
update_frequency: "on_trigger"
fallback_agent: "n05_operations"
density_score: 0.88
constraint_count: 6
linked_artifacts:
  primary: "N07_admin/P08_architecture/nucleus_def_n07.md"
  related:
    - ".cex/runtime/decisions/decision_manifest.yaml"
    - ".cex/runtime/pids/spawn_pids.txt"
    - ".cex/runtime/checkpoint.json"
related:
  - p03_sp_orchestration_nucleus
  - p01_kc_orchestration_best_practices
  - auto-accept-handoff
  - bld_collaboration_model_provider
  - p08_ac_orchestrator
  - p12_wf_orchestration_pipeline
  - bld_collaboration_session_state
  - p12_wf_create_orchestration_agent
  - n07_output_orchestration_audit
  - p12_wf_admin_orchestration
---
<!--
F1 CONSTRAIN: kind=runtime_state, pillar=P10, max_bytes=3072, naming=p10_rs_n07.md
F2 BECOME: runtime-state-builder loaded (13 ISOs). Identity: routing/decision-logic state architect
F3 INJECT: bld_schema + bld_examples + bld_memory + n07-orchestrator.md + n07-autonomous-lifecycle.md
F4 REASON: 7 sections, template-first, N07 orchestration domain fully mapped
F5 CALL: compile + doctor ready; no prior artifact exists (new build)
F6 PRODUCE: 124 lines, density=0.88
F7 GOVERN: quality:null enforced; id matches p10_rs_[a-z][a-z0-9_]+ pattern; persistence=session valid
F8 COLLABORATE: written to N07_admin/P10_memory/mem_runtime_state_n07.md; compile follows
-->

## Agent Context

N07 is the orchestrator nucleus running under the "Orchestrating Sloth" sin lens: expend
minimum cognitive overhead per decision, delegate all builds, and act only on high-signal
triggers. Runtime state tracks the mutable variables that change during a live orchestration
session. It does NOT capture N07's identity (nucleus_def) or cross-session learning (learning
records). State expires on N07 process exit; checkpoint.json enables crash recovery.

State is organized into five categories:
- **session**: PID registry, spawn timestamps, session ID
- **mission**: active wave index, nucleus completion flags, handoff paths
- **routing**: provider health scores, quota remaining per provider
- **decisions**: pending GDP items, resolved manifest entries
- **quality**: running score averages per nucleus, gate-fail counts

## Routing Rules

| Rule | Condition | Action | Confidence |
|------|-----------|--------|------------|
| GDP-first | Subjective decision detected before dispatch | Block dispatch; open GDP dialog with user | 1.00 |
| Manifest-carry | GDP manifest exists at `.cex/runtime/decisions/decision_manifest.yaml` | Inject manifest path into every handoff | 1.00 |
| Provider-healthy | Provider health score >= 0.80 | Route nucleus dispatch to that provider | 0.90 |
| Provider-degrade | Provider health score 0.50-0.79 | Use provider with warning; log degraded state | 0.75 |
| Provider-fail | Provider health score < 0.50 | Skip provider; use next in fallback_chain | 0.95 |
| Quota-guard | Quota remaining < 10% | Route to Ollama fallback; skip cloud provider | 0.90 |
| Wave-advance | All nuclei in current wave signaled complete | Close wave; run consolidate; open next wave | 1.00 |
| Timeout-escalate | Nucleus silent for >= 900s with PID alive | Escalate to user; offer kill or wait 10 min | 0.85 |
| Checkpoint-write | 300s elapsed since last checkpoint | Snapshot state to `.cex/runtime/checkpoint.json` | 1.00 |
| Crash-recover | N07 boot detects stale checkpoint (age < 3600s) | Load checkpoint; resume from last known wave | 0.90 |

## Decision Tree

```
incoming_trigger
  |-- GDP_decision_required?
  |     YES -> block_dispatch -> open_gdp_dialog -> write_manifest -> proceed
  |     NO  -> continue
  |
  |-- manifest_present?
  |     NO  -> check_if_technical_task
  |             YES -> proceed_autonomous
  |             NO  -> open_gdp_dialog
  |     YES -> inject_manifest -> proceed_autonomous
  |
  |-- wave_complete? (all nucleus signals received)
  |     YES -> run_consolidate -> quality_gate_pass?
  |             YES -> archive_wave -> dispatch_next_wave (if any)
  |             NO  -> flag_failing_nucleus -> escalate_to_user
  |     NO  -> nucleus_timeout? (>= 900s silent)
  |             YES -> pid_alive?
  |                     YES -> escalate_to_user
  |                     NO  -> mark_crashed -> escalate_to_user
  |             NO  -> continue_monitoring (non-blocking backlog work)
  |
  |-- provider_health_check (pre-dispatch)
        score >= 0.80 -> assign_provider
        score  0.50-0.79 -> assign_with_warning
        score < 0.50 -> next_in_fallback_chain
```

## Priorities

1. **Mission integrity** -- all nuclei in wave complete before advancing; no partial-wave merges
2. **GDP compliance** -- subjective decisions always blocked until user resolves; never assume
3. **Provider health** -- route only to providers scoring >= 0.80; degrade gracefully below that
4. **Non-blocking operation** -- N07 never idles during wave execution; maintain backlog work
5. **Minimal state** -- track only what drives the next decision; discard resolved wave data

## Heuristics

| Heuristic | When | Confidence |
|-----------|------|------------|
| Prefer sequential dispatch over grid when <= 2 nuclei | Small wave; grid overhead exceeds benefit | 0.85 |
| Mark nucleus dead after 2 consecutive timeouts | No signal + PID gone both checks | 0.90 |
| Re-read checkpoint on any unexpected state gap | State field missing or stale vs disk | 0.88 |
| Use cloud provider for N03/N07 tasks; Ollama for N01/N04 | Build tasks need Opus; research tolerates local | 0.80 |
| GDP dialog for tone/audience/style; never for file paths | Structural decisions are autonomous | 0.95 |
| Discard wave state after successful archive | Session memory must not accumulate unbounded | 0.90 |

## Constraints

1. Max 6 nuclei dispatched concurrently per wave (one per N01-N06)
2. GDP dialog MUST complete before any dispatch; zero exceptions
3. Checkpoint interval: exactly 300s; never skip even during active wave
4. Kill only session-owned PIDs via `taskkill /F /PID <pid> /T`; never `Stop-Process`
5. Quota guard triggers at < 10% remaining; never at 0% (too late to reroute cleanly)
6. N07 MUST NOT build artifacts directly; all builds dispatched to N01-N06

## State Transitions

| Trigger | From | To | Condition |
|---------|------|----|-----------|
| `dispatch.sh grid` called | IDLE | DISPATCH | Handoffs written + manifest present |
| All wave signals received | DISPATCH | CONSOLIDATE | Signal count == expected nucleus count |
| Consolidate gate passes | CONSOLIDATE | NEXT_WAVE or ARCHIVE | quality_avg >= 8.0 for all nuclei |
| Consolidate gate fails | CONSOLIDATE | ESCALATE | Any nucleus quality_avg < 8.0 |
| User resolves escalation | ESCALATE | DISPATCH or ARCHIVE | User chooses re-dispatch or accept |
| N07 process exits | any | ARCHIVED | Checkpoint written; PIDs recorded for cleanup |
| Crash detected at boot | IDLE | RECOVER | Checkpoint age < 3600s; resume wave index |
| 300s elapsed | any live state | CHECKPOINT_WRITE | Timer fires; state snapshot persisted |

## Persistence Scope

| State Category | Scope | Storage Path | TTL |
|----------------|-------|-------------|-----|
| session (PIDs, spawn times) | session | `.cex/runtime/pids/spawn_pids.txt` | N07 exit |
| mission (wave, progress) | session + checkpoint | `.cex/runtime/checkpoint.json` | Until archived |
| routing (provider health) | session | in-memory; refreshed each dispatch | N07 exit |
| decisions (GDP manifest) | cross-session | `.cex/runtime/decisions/decision_manifest.yaml` | Until mission archived |
| quality (score ledger) | session | `.cex/runtime/signals/signal_*.json` | Until archived |

## Properties

| Property | Value |
|----------|-------|
| Kind | `runtime_state` |
| Pillar | P10 |
| Nucleus | N07 |
| Domain | multi-nucleus orchestration |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_orchestration_nucleus]] | upstream | 0.35 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.32 |
| [[auto-accept-handoff]] | downstream | 0.32 |
| [[bld_collaboration_model_provider]] | upstream | 0.31 |
| [[p08_ac_orchestrator]] | upstream | 0.31 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.30 |
| [[bld_collaboration_session_state]] | related | 0.30 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.30 |
| [[n07_output_orchestration_audit]] | downstream | 0.29 |
| [[p12_wf_admin_orchestration]] | downstream | 0.29 |
