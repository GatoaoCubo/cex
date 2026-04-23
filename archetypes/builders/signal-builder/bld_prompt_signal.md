---
id: p03_ins_signal_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Signal Builder Instructions
target: signal-builder agent
phases_count: 3
prerequisites:
  - Event type is known (complete, error, or progress)
  - Emitting agent or agent_group name is identified
  - Event slug is defined (e.g. "build_complete", "research_error")
  - Timestamp is available or can be generated
validation_method: checklist
domain: signal
quality: 9.0
tags: [instruction, signal, orchestration, P12]
idempotent: false
atomic: true
rollback: "null — signals are fire-and-forget; discard and re-emit if invalid"
dependencies: []
logging: true
tldr: Emit an atomic JSON signal payload for complete, error, or progress events — under 4096 bytes, machine-friendly, no routing logic included.
density_score: 0.86
llm_function: REASON
related:
  - p03_sp_signal_builder
  - bld_knowledge_card_signal
  - bld_architecture_signal
  - signal-builder
  - p11_qg_signal
  - bld_schema_signal
  - bld_collaboration_signal
  - bld_config_signal
  - p01_kc_signal
  - bld_examples_signal
---
## Context
The signal-builder produces `signal` artifacts — minimal JSON payloads representing atomic
status events emitted between agents or agent_groups. A signal answers exactly three questions:
what happened, who emitted it, and when. Signals are consumed by orchestrators and monitoring
systems; they are not instructions, routing policies, or handoffs.
**Input contract**:
- `{{event_slug}}`: snake_case event name (e.g. `build_complete`, `research_error`)
- `{{emitter}}`: name of the emitting agent or agent_group (e.g. `build-sat`, `research-agent`)
- `{{status}}`: one of `complete`, `error`, `progress`
- `{{timestamp}}`: ISO 8601 datetime of the event
- `{{metadata_raw}}`: optional free-text of additional context to include
**Output contract**: A single `signal` JSON file named `p12_sig_{{event_slug}}.json`,
under 4096 bytes, with required fields and optional metadata. No routing logic, no
instructions, no narrative prose.
**Boundaries**:
- A signal is atomic — one event, one payload, one file.
- Full task instructions belong in a handoff artifact.
- Routing policy (which agent handles what) belongs in a dispatch_rule artifact.
- Multi-step workflows and DAGs are not signals.
- Optional metadata must remain compact — no embedded documents.
## Phases
### Phase 1: Classify
**Primary action**: Confirm this is a runtime event and determine the minimum required
payload before writing any JSON.
```
INPUT: event_slug, emitter, status, timestamp, metadata_raw
1. Confirm this is a runtime event, not an instruction or routing rule:
   Is it reporting something that already happened or is happening? -> signal
   Is it telling an agent what to do next?                         -> NOT a signal
   Is it defining how tasks get routed?                            -> NOT a signal
2. Validate event_slug:
   Must match pattern: ^[a-z][a-z0-9_]+$
   Must be descriptive: "{emitter}_{status}" pattern preferred
   Examples: "build_complete", "research_error", "ingest_progress"
3. Validate status value:
   complete  -> terminal success event
   error     -> terminal failure event
   progress  -> non-terminal update (use sparingly — only for long-running ops)
4. Parse metadata_raw into optional_fields:
   Extract only machine-friendly key-value pairs.
   Discard prose, instructions, or routing logic.
   Convert any numeric strings to numbers.
   Keep only fields that help automation (scores, counts, paths, error codes).
   Reject fields that duplicate required fields (emitter, status, timestamp).
5. Compute target_consumer from event context:
   if status == "complete" or "error": consumer is likely an orchestrator
   if status == "progress":            consumer is likely a monitoring system
OUTPUT: validated_slug, validated_status, optional_fields{}, target_consumer
```
Verification: `validated_slug` matches naming pattern. `validated_status` is one of
three valid values. `optional_fields` contains no instructions or routing logic.
### Phase 2: Compose
**Primary action**: Assemble the minimum valid JSON payload with required fields first,
optional fields appended only if compact and relevant.
```
INPUT: validated_slug, emitter, validated_status, timestamp, optional_fields
1. Set filename: p12_sig_{{event_slug}}.json
2. Assemble required fields (always present):
   {
     "id": "p12_sig_{{event_slug}}",
     "kind": "signal",
     "pillar": "P12",
     "emitter": "{{emitter}}",
     "status": "{{validated_status}}",
     "timestamp": "{{timestamp}}",
     "quality": null
   }
3. Append optional fields (only if each meets ALL criteria):
   - Value is machine-friendly (lowercase enum, number, ISO timestamp, or short string)
   - Value adds information not derivable from required fields
   - Adding it does not push total payload over 4096 bytes
   Common valid optional fields:
     "score":       numeric quality indicator (0.0 - 10.0)
     "duration_s":  execution time in seconds (integer)
     "task_id":     identifier of the task that generated this signal
     "error_code":  short string error classifier (e.g. "timeout", "validation_failed")
     "items_count": integer count of processed items
     "artifact_id": identifier of the artifact produced
4. Size check:
   Estimate JSON byte count (minified).
   If > 4096 bytes: remove optional fields one by one (lowest value first)
   until size <= 4096 bytes.
OUTPUT: signal JSON content (assembled, not yet validated)
```
Verification: required fields all present. Estimated minified size <= 4096 bytes.
No field contains prose, instructions, or routing logic.
### Phase 3: Validate
**Primary action**: Run all quality gates against the assembled JSON and output the
final file only if all HARD gates pass.
```
INPUT: signal JSON content
1. HARD quality gates (all must pass):
   HARD_1: id matches pattern ^p12_sig_[a-z][a-z0-9_]+$
   HARD_2: kind == "signal"
   HARD_3: status is one of complete/error/progress
   HARD_4: timestamp is valid ISO 8601 datetime string
   HARD_5: emitter is non-empty string
   HARD_6: quality == null
   HARD_7: total JSON size (minified) <= 4096 bytes
   HARD_8: JSON parses without syntax errors
2. Scope check:
   Verify the signal contains NO routing instructions.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_signal_builder]] | related | 0.51 |
| [[bld_knowledge_card_signal]] | downstream | 0.51 |
| [[bld_architecture_signal]] | downstream | 0.44 |
| [[signal-builder]] | downstream | 0.41 |
| [[p11_qg_signal]] | downstream | 0.41 |
| [[bld_schema_signal]] | downstream | 0.40 |
| [[bld_collaboration_signal]] | downstream | 0.39 |
| [[bld_config_signal]] | downstream | 0.38 |
| [[p01_kc_signal]] | downstream | 0.38 |
| [[bld_examples_signal]] | downstream | 0.37 |
