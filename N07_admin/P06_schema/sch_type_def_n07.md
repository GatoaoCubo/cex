---
id: sch_type_def_n07
kind: type_def
pillar: P06
nucleus: n07
title: "Orchestrator Type Definitions"
version: 1.0
quality: 8.2
tags: [type-def, orchestration, dispatch, wave, mission]
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_integration_guide
  - bld_schema_pitch_deck
  - bld_schema_multimodal_prompt
  - bld_schema_eval_metric
  - bld_schema_sandbox_config
---
<!-- 8F: F1=P06/type_def F2=type-def-builder F3=nucleus_def_n07 F4=reason F5=call F6=produce F7=govern F8=collaborate -->

## Purpose

N07 orchestrates missions across nuclei. Without typed structures, every handoff
re-describes the same fields in free prose, wasting tokens on re-parsing.
These types define once, reference everywhere -- the sloth lens applied to data.

---

## Enumerations

### NucleusId

| Value | Nucleus |
|-------|---------|
| `n01` | intelligence |
| `n02` | marketing |
| `n03` | engineering |
| `n04` | knowledge |
| `n05` | operations |
| `n06` | commercial |
| `n07` | orchestrator |

### WaveStatus

| Value | Meaning |
|-------|---------|
| `pending` | Not yet dispatched |
| `running` | Nuclei active |
| `complete` | All signals received |
| `failed` | Timeout or crash detected |
| `skipped` | Dependency gate blocked |

### MissionPhase

| Value | Meaning |
|-------|---------|
| `planning` | GDP in progress, waves not locked |
| `dispatching` | Grid dispatch initiated |
| `monitoring` | Polling signals, backlog work active |
| `consolidating` | Final wave done, verifying artifacts |
| `done` | Report committed, processes stopped |

### SignalType

| Value | Meaning |
|-------|---------|
| `complete` | Nucleus finished, quality >= floor |
| `failed` | Nucleus crashed or timed out |
| `partial` | Some deliverables produced, not all |
| `heartbeat` | Alive ping (long-running tasks) |

---

## Type Definitions

### WavePlan

Describes one execution wave: which nuclei run, what they depend on, and when they time out.

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `wave_id` | string | yes | -- | Unique identifier, e.g. `wave_1` |
| `nuclei` | list[NucleusId] | yes | -- | Nuclei dispatched in this wave |
| `dependencies` | list[WaveDep] | no | `[]` | Wave IDs that must be `complete` first |
| `timeout_sec` | int | yes | 2700 | Max seconds before wave declared failed |
| `status` | WaveStatus | yes | `pending` | Current execution state |

WaveDep: `{ wave_id: string, required: boolean }`

### HandoffSpec

Contract written by N07 into `.cex/runtime/handoffs/` before dispatch.

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `mission` | string | yes | -- | Mission name, matches MissionState.name |
| `nucleus` | NucleusId | yes | -- | Target nucleus |
| `deliverables` | list[string] | yes | -- | Expected output file paths |
| `context_refs` | list[string] | no | `[]` | Artifact paths the nucleus must read |
| `decisions_ref` | string or null | no | null | Path to decision_manifest.yaml |

### DispatchResult

Recorded in `.cex/runtime/pids/spawn_pids.txt` after each spawn.

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `pid` | int | yes | -- | Wrapper process ID |
| `nucleus` | NucleusId | yes | -- | Which nucleus was spawned |
| `cli` | string | yes | -- | `claude`, `gemini`, `codex`, or `ollama` |
| `session_id` | string | yes | -- | UUID for this N07 session |
| `start_time` | datetime | yes | -- | ISO 8601 spawn timestamp |
| `worker_pids` | list[int] | no | `[]` | Descendant worker PIDs (post-enrichment) |

### ConsolidationReport

Produced by N07 after the final wave; committed to repo.

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `mission` | string | yes | -- | Mission name |
| `wave_id` | string | yes | -- | Final wave that triggered consolidation |
| `artifacts_verified` | int | yes | -- | Count of deliverables confirmed on disk |
| `artifacts_expected` | int | yes | -- | Count declared in HandoffSpec.deliverables |
| `quality_avg` | float or null | no | null | Mean quality score; null if not yet scored |
| `gaps` | list[string] | no | `[]` | Missing or below-floor artifact paths |

### SignalPayload

JSON written to `.cex/runtime/signals/signal_{nucleus}_{mission}_{ts}.json`.

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `nucleus` | NucleusId | yes | -- | Emitting nucleus |
| `event` | SignalType | yes | -- | Completion category |
| `score` | float or null | no | null | Quality score if available |
| `path` | string or null | no | null | Primary artifact path |
| `timestamp` | datetime | yes | -- | ISO 8601 emit time |

### MissionState

Ephemeral runtime object tracking full mission lifecycle.

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `name` | string | yes | -- | Unique mission name |
| `phase` | MissionPhase | yes | `planning` | Current lifecycle phase |
| `waves` | list[WavePlan] | yes | -- | Ordered wave schedule |
| `decisions_locked` | bool | yes | false | GDP complete and manifest written |
| `start_time` | datetime | yes | -- | ISO 8601 mission start |

---

## Relationships

```
MissionState
  +-- waves: list[WavePlan]
  |     +-- nuclei: list[NucleusId]
  |     +-- status: WaveStatus
  |
  +-- (per nucleus) HandoffSpec
        +-- decisions_ref -> decision_manifest.yaml
        +-- context_refs -> artifact paths

dispatch(HandoffSpec) -> DispatchResult
  +-- pid, worker_pids -> spawn_pids.txt

nucleus emits -> SignalPayload
  +-- event: SignalType
  +-- score -> feeds ConsolidationReport

wave complete -> ConsolidationReport
  +-- gaps -> back to WavePlan (retry or skip)
```

---

## Rationale

| Choice | Reason |
|--------|--------|
| `decisions_locked` bool on MissionState | GDP gate: dispatch is blocked until true |
| `worker_pids` list on DispatchResult | Wrapper PID alone cannot tree-kill claude.exe |
| `quality_avg` nullable on ConsolidationReport | Scoring runs asynchronously after consolidation |
| `decisions_ref` nullable on HandoffSpec | Direct conversational tasks skip manifest |
| `timeout_sec` on WavePlan | Per-wave ceiling; long waves (N01 research) differ from short builds |

---

## Properties

| Property | Value |
|----------|-------|
| Kind | `type_def` |
| Pillar | P06 |
| Nucleus | N07 |
| Domain | orchestration |
| Pipeline | 8F (F1-F8) |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | related | 0.52 |
| [[bld_schema_usage_report]] | related | 0.51 |
| [[bld_schema_benchmark_suite]] | related | 0.50 |
| [[bld_schema_dataset_card]] | related | 0.50 |
| [[bld_schema_quickstart_guide]] | related | 0.49 |
| [[bld_schema_integration_guide]] | related | 0.49 |
| [[bld_schema_pitch_deck]] | related | 0.48 |
| [[bld_schema_multimodal_prompt]] | related | 0.48 |
| [[bld_schema_eval_metric]] | related | 0.47 |
| [[bld_schema_sandbox_config]] | related | 0.47 |
