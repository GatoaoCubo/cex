---
id: p12_sm_8f_pipeline
kind: state_machine
pillar: P12
version: "1.0.0"
created: "2026-04-19"
updated: "2026-04-19"
author: "n03_engineering"
entity: "8FPipeline"
initial_state: "IDLE"
final_states: ["COMPLETE", "FAILED"]
states_count: 11
transitions_count: 14
quality: 8.3
tags: [state_machine, 8f_pipeline, P12, cex, fsm]
tldr: "8F pipeline FSM: 11 states (IDLE + F1-F8 + COMPLETE + FAILED), 14 transitions governing artifact construction lifecycle."
related:
  - bld_architecture_kind
  - kind-builder
  - bld_collaboration_kind
  - bld_tools_kind
  - p03_sp_n03_creation_nucleus
  - bld_instruction_kind
  - skill
  - p06_vs_frontmatter
  - bld_config_kind
  - bld_collaboration_quality_gate
density_score: 1.0
---

# State Machine: 8F Pipeline

Formal FSM governing the lifecycle of every artifact construction run in CEX.
Grounded in the 8F Universal Reasoning Protocol (`.claude/rules/8f-reasoning.md`).
Every nucleus (N01-N07) that processes a task transitions through these states in sequence.

## States

| State | Type | Description |
|-------|------|-------------|
| IDLE | initial | No active task. Awaiting TASK_RECEIVED event. |
| F1_CONSTRAIN | intermediate | Resolving kind, pillar, schema from kinds_meta.json. |
| F2_BECOME | intermediate | Loading builder identity: all 13 ISOs from archetypes/builders/{kind}-builder/. |
| F3_INJECT | intermediate | Assembling context: KC, examples, brand config, memory, similar artifacts. |
| F4_REASON | intermediate | Planning: sections, approach, dependency check, GDP gate if subjective. |
| F5_CALL | intermediate | Executing tools: retriever, compiler pre-flight, sub-agent spawn if needed. |
| F6_PRODUCE | intermediate | Generating artifact: frontmatter + body following builder instructions. |
| F7_GOVERN | intermediate | Quality validation: H01-H07 gates, 5D scoring, 12LP checklist. |
| F8_COLLABORATE | intermediate | Persisting: save to pillar dir, compile, commit, signal nucleus complete. |
| COMPLETE | final | Artifact delivered. Signal written. |
| FAILED | final | Unrecoverable error or quality gate exhausted after 2 retries. |

## Transitions

| from_state | event | to_state | guard | action |
|------------|-------|----------|-------|--------|
| IDLE | TASK_RECEIVED | F1_CONSTRAIN | taskValid() | loadKindsMetaJson() |
| F1_CONSTRAIN | KIND_RESOLVED | F2_BECOME | schemaLoaded() | recordKindPillar() |
| F1_CONSTRAIN | KIND_UNKNOWN | FAILED | - | emitError("kind not in kinds_meta") |
| F2_BECOME | BUILDER_LOADED | F3_INJECT | isosLoaded() | loadBuilderISOs() |
| F2_BECOME | BUILDER_MISSING | FAILED | - | emitError("builder ISOs not found") |
| F3_INJECT | CONTEXT_ASSEMBLED | F4_REASON | - | assembleContextSources() |
| F4_REASON | PLAN_READY | F5_CALL | - | writePlanSection() |
| F5_CALL | TOOLS_READY | F6_PRODUCE | - | executePreflightTools() |
| F6_PRODUCE | DRAFT_COMPLETE | F7_GOVERN | - | generateArtifact() |
| F7_GOVERN | SCORE_PASS | F8_COLLABORATE | qualityAbove8() | recordQualityScore() |
| F7_GOVERN | SCORE_FAIL | F6_PRODUCE | retryAllowed() | incrementRetry() |
| F7_GOVERN | SCORE_FAIL | FAILED | retryExhausted() | emitError("quality gate exhausted") |
| F8_COLLABORATE | ARTIFACT_SAVED | COMPLETE | - | saveCompileCommitSignal() |
| F8_COLLABORATE | SAVE_ERROR | FAILED | - | emitError("F8 persistence failed") |

## Guards

| Guard | Expression | Notes |
|-------|-----------|-------|
| taskValid() | intent != null AND kind resolvable | Rejects empty or unresolvable inputs at entry |
| schemaLoaded() | pillar/_schema.yaml exists | Guarantees schema constraints are available for F2 |
| isosLoaded() | count(ISOs in builder dir) == 13 | Enforces complete builder identity before F3 |
| qualityAbove8() | score >= 8.0 | CEX quality floor; artifacts below 8.0 retry or fail |
| retryAllowed() | retry_count < 2 | Max 2 F7->F6 retries per 8F run |
| retryExhausted() | retry_count >= 2 | Triggers terminal FAILED after exhausted retries |

## Actions

| Action | Trigger | Effect |
|--------|---------|--------|
| loadKindsMetaJson() | IDLE -> F1_CONSTRAIN | Opens .cex/kinds_meta.json, resolves kind tuple |
| recordKindPillar() | F1 -> F2 | Writes {kind, pillar, max_bytes, naming} to run context |
| loadBuilderISOs() | F2 -> F3 | Reads all 13 ISOs from archetypes/builders/{kind}-builder/ |
| assembleContextSources() | F3 -> F4 | Pulls KC + examples + brand + memory into context window |
| writePlanSection() | F4 -> F5 | Emits 8F trace header: "F4: Plan -- N sections, approach=X" |
| executePreflightTools() | F5 -> F6 | Runs retriever + similar-artifact scan + sub-agent check |
| generateArtifact() | F6 -> F7 | Produces complete artifact with frontmatter + body |
| recordQualityScore() | F7 pass | Logs score/gates/12LP to run context for F8 |
| incrementRetry() | F7 fail -> F6 | Adds retry_count+1 and annotates which gates failed |
| saveCompileCommitSignal() | F8 -> COMPLETE | Writes file, runs cex_compile.py, git commit, write_signal() |

## References

- Protocol: `.claude/rules/8f-reasoning.md`
- Quality gates: `archetypes/builders/{kind}-builder/bld_quality_gate_{kind}.md`
- Signal writer: `_tools/signal_writer.py`
- Aggregate root governing artifact output: `N03_engineering/P06_schema/aggregate_root_artifact.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | upstream | 0.35 |
| [[kind-builder]] | upstream | 0.33 |
| [[bld_collaboration_kind]] | related | 0.30 |
| [[bld_tools_kind]] | upstream | 0.28 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.28 |
| [[bld_instruction_kind]] | upstream | 0.26 |
| [[skill]] | upstream | 0.26 |
| [[p06_vs_frontmatter]] | upstream | 0.25 |
| [[bld_config_kind]] | upstream | 0.24 |
| [[bld_collaboration_quality_gate]] | upstream | 0.24 |
