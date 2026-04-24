---
id: sch_input_schema_n07
kind: input_schema
8f: F1_constrain
pillar: P06
nucleus: n07
title: "Orchestrator Input Contract"
version: 1.0
quality: 8.9
tags: [input-schema, orchestration, dispatch, handoff, validation]
scope: "n07-orchestrator-operations"
domain: "orchestration, dispatch, wave planning, mission control"
author: "input-schema-builder"
created: "2026-04-17"
updated: "2026-04-17"
tldr: "Input contracts for N07 core operations: dispatch, mission, handoff, consolidation. Strict validation prevents costly re-dispatch."
density_score: 0.88
related:
  - bld_schema_validation_schema
  - bld_schema_input_schema
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_sandbox_config
  - bld_schema_nucleus_def
  - bld_schema_prompt_compiler
  - bld_schema_quickstart_guide
---
<!-- 8F: F1=P06/input_schema F2=input-schema-builder F3=nucleus_def_n07 F4=reason F5=call F6=produce F7=govern F8=collaborate -->

## Purpose

N07 (Orchestrating Sloth) enforces strict input validation at every entry point.
Malformed dispatch or handoff data causes wave failures that cost tokens and time.
Catching invalid input at F1 CONSTRAIN is cheaper than re-dispatching a failed wave.

## Schema 1: Dispatch Input

Caller: user or cex_mission_runner.py. Receiver: N07 dispatch layer (_spawn/dispatch.sh).

| # | Field | Type | Required | Default | Validation | Failure Action |
|---|-------|------|----------|---------|------------|----------------|
| 1 | nucleus | enum | YES | - | one of: n01,n02,n03,n04,n05,n06 | reject; log invalid_nucleus |
| 2 | mode | enum | YES | solo | one of: solo,grid,crew,swarm | reject; log invalid_mode |
| 3 | task_description | string | YES | - | len >= 20, len <= 2000 | reject if blank; truncate if >2000 |
| 4 | handoff_path | path | YES | - | must exist or be writable under .cex/runtime/handoffs/ | reject if path escapes repo root |
| 5 | priority | enum | NO | normal | one of: low,normal,high,critical | default normal if absent or invalid |
| 6 | timeout_seconds | integer | NO | 3600 | range [60, 86400] | clamp to range; warn if clamped |

Coercion: nucleus uppercase -> lowercase; mode uppercase -> lowercase; timeout_seconds as string -> cast int.

## Schema 2: Mission Input

Caller: user via /mission or cex_mission_runner.py. Receiver: N07 mission planner.

| # | Field | Type | Required | Default | Validation | Failure Action |
|---|-------|------|----------|---------|------------|----------------|
| 1 | goal | string | YES | - | len >= 10, len <= 1000 | reject if blank |
| 2 | budget_tokens | integer | NO | 500000 | range [10000, 5000000] | clamp; warn if clamped |
| 3 | max_waves | integer | NO | 5 | range [1, 20] | clamp to range |
| 4 | nuclei | list[enum] | NO | [n03] | each item in n01-n06 | strip invalid entries; warn |
| 5 | gdp_required | boolean | NO | true | true or false | default true if unparseable |

Coercion: nuclei as comma-separated string -> split to list; budget_tokens as string -> cast int;
gdp_required as string "true"/"false" -> boolean.

## Schema 3: Handoff Input

Caller: N07 writing to .cex/runtime/handoffs/. Receiver: target nucleus at boot.

| # | Field | Type | Required | Default | Validation | Failure Action |
|---|-------|------|----------|---------|------------|----------------|
| 1 | mission_name | string | YES | - | slug pattern [a-z0-9_], len 3-64 | reject; log invalid_mission_name |
| 2 | nucleus | enum | YES | - | one of: n01,n02,n03,n04,n05,n06 | reject; log invalid_nucleus |
| 3 | wave_id | string | YES | - | pattern wave_[0-9]+, e.g. wave_1 | reject; log invalid_wave_id |
| 4 | deliverables | list[path] | YES | - | len >= 1; each path must be relative, non-empty string | reject if empty list |
| 5 | context_refs | list[path] | NO | [] | each path must exist in repo | strip missing; warn per missing entry |
| 6 | decisions_ref | path | NO | null | must point under .cex/runtime/decisions/ if provided | null if invalid; warn |

Coercion: deliverables/context_refs as newline-separated string -> split to list;
decisions_ref empty string -> null.

## Schema 4: Consolidation Input

Caller: cex_mission_runner.py or N07 post-wave. Receiver: N07 consolidation step.

| # | Field | Type | Required | Default | Validation | Failure Action |
|---|-------|------|----------|---------|------------|----------------|
| 1 | mission_name | string | YES | - | slug [a-z0-9_], len 3-64 | reject; log invalid_mission_name |
| 2 | wave_id | string | YES | - | pattern wave_[0-9]+ | reject; log invalid_wave_id |
| 3 | expected_signals | list[string] | YES | - | len >= 1; each item in n01-n06 | reject if empty; strip invalid items |
| 4 | timeout_seconds | integer | NO | 3600 | range [60, 86400] | clamp to [60, 86400]; warn |
| 5 | auto_archive | boolean | NO | true | true or false | default true if unparseable |

Coercion: expected_signals as comma-separated string -> split to list;
timeout_seconds as string -> cast int; auto_archive as string -> boolean.

## Validation Rules

| Rule | Applies To | Description |
|------|-----------|-------------|
| R01 | All schemas | All required fields present before processing begins |
| R02 | Dispatch, Handoff | nucleus must resolve to an active nucleus directory (N0X_*/) |
| R03 | Dispatch | handoff_path parent directory must exist and be writable |
| R04 | Handoff | deliverables list must contain at least one non-empty path string |
| R05 | Mission | nuclei list must contain at least one valid nucleus after stripping |
| R06 | Consolidation | expected_signals must match nuclei referenced in the wave handoffs |
| R07 | All schemas | No field value may contain path traversal sequences (../) |
| R08 | All schemas | Coercion failures on required fields raise ValidationError immediately |

## Error Catalog

| Code | Schema | Message |
|------|--------|---------|
| E01 | Dispatch | DispatchError: nucleus '{v}' not in [n01-n06] |
| E02 | Dispatch | DispatchError: task_description too short (min 20 chars) |
| E03 | Dispatch | DispatchError: handoff_path escapes repo root |
| E04 | Mission | MissionError: goal is required and cannot be blank |
| E05 | Mission | MissionError: no valid nuclei after stripping invalid entries |
| E06 | Handoff | HandoffError: deliverables list is empty |
| E07 | Handoff | HandoffError: wave_id does not match pattern wave_[0-9]+ |
| E08 | Consolidation | ConsolidationError: expected_signals is empty |
| E09 | All | ValidationError: path traversal detected in field '{field}' |

## Rationale

Sloth lens: the cheapest validation is the one that runs before dispatch.
A 50ms input check prevents a 30-minute wave failure and a re-dispatch burn.

| Design Choice | Reason |
|---------------|--------|
| strict enums for nucleus/mode | prevents silent routing to wrong target |
| deliverables required non-empty | consolidation step cannot verify an empty list |
| timeout clamped not rejected | prevents lockout from misconfigured callers |
| decisions_ref nullable | GDP is not always required (technical builds skip it) |
| gdp_required defaults true | safe default; operator can override per-mission |

## References

1. `N07_admin/P08_architecture/nucleus_def_n07.md`
2. `N03_engineering/P06_schema/input_schema_build_contract.md`
3. `.cex/runtime/handoffs/` (handoff directory contract)
4. `.claude/rules/guided-decisions.md` (GDP protocol)
5. `_spawn/dispatch.sh` (dispatch CLI contract)

## Properties

| Property | Value |
|----------|-------|
| Kind | input_schema |
| Pillar | P06 |
| Nucleus | N07 |
| Domain | orchestration, dispatch, wave planning, mission control |
| Pipeline | 8F (F1-F8) |
| Compiler | cex_compile.py |
| Quality target | null (peer-scored) |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_validation_schema]] | related | 0.44 |
| [[bld_schema_input_schema]] | related | 0.43 |
| [[bld_schema_reranker_config]] | related | 0.41 |
| [[bld_schema_usage_report]] | related | 0.40 |
| [[bld_schema_dataset_card]] | related | 0.39 |
| [[bld_schema_benchmark_suite]] | related | 0.39 |
| [[bld_schema_sandbox_config]] | related | 0.39 |
| [[bld_schema_nucleus_def]] | related | 0.39 |
| [[bld_schema_prompt_compiler]] | related | 0.39 |
| [[bld_schema_quickstart_guide]] | related | 0.38 |
