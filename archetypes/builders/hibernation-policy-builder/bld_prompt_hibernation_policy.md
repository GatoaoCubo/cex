---
kind: instruction
id: bld_instruction_hibernation_policy
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for hibernation_policy
quality: 8.7
title: "Instruction Hibernation Policy"
version: "1.0.0"
author: n03_engineering
tags: [hibernation_policy, builder, instruction]
tldr: "Step-by-step production process for hibernation_policy"
domain: "hibernation_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_instruction_input_schema
  - bld_instruction_kind
  - p03_ins_vector_store
  - bld_instruction_session_backend
  - bld_instruction_instruction
  - p03_ins_mental_model
  - p11_qg_runtime_state
  - bld_instruction_memory_scope
  - bld_instruction_golden_test
  - bld_instruction_agent
---

## Phase 1: RESEARCH (hibernation_policy)
1. Identify the target backend: daytona | modal | singularity | generic.
2. Determine idle trigger type:
   - `no_activity_seconds` for agent-driven workloads (no I/O for N seconds)
   - `no_requests_seconds` for HTTP-serving serverless (no inbound requests)
   - `explicit_signal` for batch jobs with known completion boundaries
3. Choose idle threshold (threshold_seconds):
   - Interactive agent: 1800s (30 min)
   - GPU serverless: 300s (5 min)
   - Batch explicit: 0 (fires immediately on signal)
4. Determine wake conditions: at minimum one of incoming_request, scheduled_cron, explicit_signal.
5. Decide state persistence:
   - keep_memory: true if agent state must survive sleep (long-running workspace)
   - snapshot_disk: true if model weights or filesystem must persist (GPU workloads)
   - checkpoint_cadence_seconds: set to 60 for high-value state, null for ephemeral
6. Set wake_latency_sla_seconds based on user-facing SLA (10s for interactive, 30-60s for batch).
7. Estimate cost_savings_estimate_pct (typical range 60-90% for serverless idle reduction).
8. Identify sibling terminal_backend artifact (same backend slug, e.g. p09_tb_modal for a modal policy).

## Phase 2: COMPOSE
1. Write frontmatter block with all required fields from schema.
2. Set `target_backend` to one of: daytona, modal, singularity, generic.
3. Populate `idle_trigger` block: type + threshold_seconds.
4. Populate `wake_on` list with applicable conditions.
5. Populate `state_persistence` block: keep_memory, snapshot_disk, checkpoint_cadence_seconds.
6. Set `wake_latency_sla_seconds` and `cost_savings_estimate_pct`.
7. Write body: idle trigger table, wake conditions table, state persistence table, SLA table.
8. Add backend-specific notes (e.g., Modal uses container scaling-to-zero, Daytona uses workspace pause API).
9. Add pairing note: reference the sibling terminal_backend artifact.

## Phase 3: VALIDATE
- [ ] `target_backend` is one of: daytona, modal, singularity, generic
- [ ] `idle_trigger.type` is one of: no_activity_seconds, no_requests_seconds, explicit_signal
- [ ] `idle_trigger.threshold_seconds` >= 60 (except explicit_signal where 0 is allowed)
- [ ] `wake_on` list has at least one condition
- [ ] `wake_latency_sla_seconds` > 0
- [ ] ID matches naming pattern: `p09_hp_` + backend slug (e.g. `p09_hp_modal`, `p09_hp_daytona`)
- [ ] H01-H05 HARD gates pass
- [ ] SOFT score >= 8.0 before publish


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_input_schema]] | sibling | 0.21 |
| [[bld_instruction_kind]] | sibling | 0.20 |
| [[p03_ins_vector_store]] | sibling | 0.20 |
| [[bld_instruction_session_backend]] | sibling | 0.20 |
| [[bld_instruction_instruction]] | sibling | 0.19 |
| [[p03_ins_mental_model]] | sibling | 0.19 |
| [[p11_qg_runtime_state]] | downstream | 0.19 |
| [[bld_instruction_memory_scope]] | sibling | 0.19 |
| [[bld_instruction_golden_test]] | sibling | 0.18 |
| [[bld_instruction_agent]] | sibling | 0.18 |
