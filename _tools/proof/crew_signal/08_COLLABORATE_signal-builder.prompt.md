# CEX Crew Runner -- Builder Execution
**Builder**: `signal-builder`
**Function**: COLLABORATE
**Intent**: reconstroi signal-builder
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:29:34.607519

## Intent Context
- **Verb**: reconstroi
- **Object**: signal-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_signal.md
---
id: signal-builder
kind: type_builder
pillar: P12
domain: signal
llm_function: COLLABORATE
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: CODEX
tags: [kind-builder, signal, P12, orchestration, specialist]
---

# signal-builder
## Identity
Especialista em construir `signal` de P12: eventos atomicos entre agentes.
Produz payloads JSON curtos para complete, error e progress, com semantica
operacional clara e baixo overhead.
## Capabilities
- Produzir signals JSON com campos minimos e naming P12 corretos
- Distinguir signal de handoff e dispatch_rule sem sobreposicao
- Modelar payload minimo e extensoes opcionais sem quebrar consumidores
- Validar sinais contra gates duros de naming, status e timestamp
## Routing
keywords: [signal, completion, progress, error, heartbeat, status]
triggers: "emite signal", "gera completion json", "notifica status do satellite"
## Crew Role
In a crew, I handle ATOMIC STATUS EXCHANGE.
I answer: "what happened, who emitted it, and when?"
I do NOT handle: full instructions, routing policy, workflows, DAGs.

### bld_instruction_signal.md
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
  - Emitting agent or satellite name is identified
  - Event slug is defined (e.g. "build_complete", "research_error")
  - Timestamp is available or can be generated
validation_method: checklist
domain: signal
quality: null
tags: [instruction, signal, orchestration, P12]
idempotent: false
atomic: true
rollback: "null — signals are fire-and-forget; discard and re-emit if invalid"
dependencies: []
logging: true
tldr: Emit an atomic JSON signal payload for complete, error, or progress events — under 4096 bytes, machine-friendly, no routing logic included.
density_score: 0.86
---

## Context
The signal-builder produces `signal` artifacts — minimal JSON payloads representing atomic
status events emitted between agents or satellites. A signal answers exactly three questions:
what happened, who emitted it, and when. Signals are consumed by orchestrators and monitoring
systems; they are not instructions, routing policies, or handoffs.
**Input contract**:
- `{{event_slug}}`: snake_case event name (e.g. `build_complete`, `research_error`)
- `{{emitter}}`: name of the emitting agent or satellite (e.g. `build-sat`, `research-agent`)
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

### bld_knowledge_card_signal.md
---
kind: knowledge_card
id: bld_knowledge_card_signal
pillar: P12
llm_function: INJECT
purpose: Domain knowledge for signal production — atomic searchable facts
sources: signal-builder MANIFEST.md + SCHEMA.md
---

# Domain Knowledge: signal
## Executive Summary
Signals are atomic JSON runtime notifications — the smallest status exchange unit between agents. Each signal answers one question: "what happened, who emitted it, and when?" with exactly 4 required fields. Unlike handoffs (task instructions) or dispatch_rules (routing policy), signals carry only outcome state — no execution content, no routing logic, no workflow steps.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P12 (orchestration) |
| Format | JSON |
| Naming | `p12_sig_{event}.json` |
| Max bytes | 4096 |
| Required fields | 4: satellite, status, quality_score, timestamp |
| Optional fields | 7: task, artifacts, artifacts_count, commit_hash, error_code, message, progress_pct |
| status enum | `complete` / `error` / `progress` |
| quality_score range | 0.0 – 10.0 |
| timestamp format | ISO 8601 datetime |
| Emitter | one signal = one event = one emitter |
## Patterns
| Pattern | Rule |
|---------|------|
| Minimal payload | Emit 4 required fields; add optional only when they reduce consumer ambiguity |
| status=complete | Work concluded successfully enough to advance pipeline |
| status=error | Work failed or blocked; triggers retry/escalation |
| status=progress | Work ongoing; include `progress_pct` (0–100) |
| progress_pct | Valid ONLY when `status=progress` — never on complete/error |
| satellite field | Lowercase slug preferred: `codex`, `edison`, `shaka` |
| quality_score | Reflects event outcome quality (9.0 = clean complete, 5.0 = partial) |
| Immutable once emitted | Never mutate; emit a new signal for updated state |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Task instructions in payload | Signal is not a handoff — no execution content |
| Routing rules or satellite selection | Signal is not a dispatch_rule |
| `progress_pct` on `status=complete` | Schema violation; pct valid only during ongoing work |
| Omitting `timestamp` | Breaks chronological ordering for signal consumers |
| quality_score outside 0.0–10.0 | Hard schema rejection |
| Multiple signals per single event | One signal = one event; consolidate into single emission |
| Payload > 4096 bytes | Exceeds max; trim optional fields |
## Application
1. Identify the event type: completion, failure/block, or ongoing progress
2. Set `status` to `complete`, `error`, or `progress`
3. Set `satellite` to lowercase slug of the emitting agent
4. Set `quality_score` (0.0–10.0) reflecting outcome quality
5. Set `timestamp` to current ISO 8601 datetime
6. If `status=progress`, add `progress_pct` (0–100)
7. Add optional fields (task, artifacts, message) only when they add consumer value
8. Name file `p12_sig_{event}.json`, keep under 4096 bytes
## References
- Schema: signal SCHEMA.md (P06)
- Pillar: P12 (orchestration)
- Boundary: handoff (instructions), dispatch_rule (routing), workflow (step graph) — all distinct from signal

### bld_quality_gate_signal.md
---
id: p11_qg_signal
kind: quality_gate
pillar: P11
title: "Gate: Signal"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: signal
quality: null
density_score: 0.85
tags:
  - quality-gate
  - signal
  - inter-agent
  - p11
tldr: "Gates ensuring signal specs define an exhaustive status enum, emitter identity, timestamp, and minimal payload with no embedded business logic."
---

## Definition
A signal is an atomic event emitted by one agent and consumed by another or a monitor. It carries a status, an emitter identity, a timestamp, and an optional minimal payload. A signal passes this gate when any consumer could parse and act on it without contacting the emitter, the status enum covers all terminal and non-terminal states, and the payload contains no business logic — only status data.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`signal-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `signal` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Status type** field with an explicit enum (e.g., `complete`, `error`, `progress`) and no open-ended string values | Open status strings make consumer logic fragile and non-exhaustive |
| H08 | Spec contains an **Emitter identity field** (the field name and type that identifies which agent emitted the signal) | Consumers and monitors need emitter identity to route, filter, and audit signals |
| H09 | Spec contains a **Timestamp field** (field name, type, and format, e.g., ISO 8601 UTC) | Without timestamps, ordering and deduplication are impossible |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Payload is minimal JSON (only fields required for consumers to act; no verbose metadata) | 1.0 | Large nested payload | Moderate size | Flat structure, <= 10 fields, no nested objects except optional extension |
| 3 | Status enum is exhaustive (covers all reachable states including error sub-types) | 1.0 | Only happy-path statuses | Happy path + generic error | All terminal states + progress states + known error variants |
| 4 | Consumer expectations documented (who reads this signal and what they do per status) | 1.0 | No consumers listed | Consumers named | Consumers named + action per status per consumer |
| 5 | Idempotency considered (spec states whether duplicate signals are safe or must be deduplicated) | 1.0 | No mention | Noted as a concern | Explicit idempotency ruling with dedup key if required |
| 6 | Tags include `signal` | 0.5 | Missing | Present but misspelled | Exactly `signal` in tags list |
| 7 | Extension fields optional not required (future payload fields are opt-in; consumers ignore unknown keys) | 0.5 | Extension fields are required | Marked optional but schema enforces them | Schema allows unknown fields; consumers ignore unknown keys |
| 8 | Backward compatibility policy stated (additive-only field additions, versioning strategy) | 1.0 | No compatibility policy | Semver bump required for any change | Additive-only policy: new optional fields never break consumers |

### bld_schema_signal.md
---
kind: schema
id: bld_schema_signal
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for signal - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
---

# Schema: signal
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P12` |
| Type | literal `signal` |
| Machine format | `json` |
| Naming | `p12_sig_{event}.json` |
| Max bytes | 4096 |
## Required Payload Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| satellite | string, non-empty, lowercase slug preferred | YES | - | emitting agent/satellite |
| status | enum (`complete`, `error`, `progress`) | YES | - | atomic event state |
| quality_score | number, `0.0 <= x <= 10.0` | YES | - | event quality/outcome score |
| timestamp | string, ISO 8601 datetime | YES | - | emission moment |
## Optional Payload Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| task | string | NO | omitted | short task summary |
| artifacts | list[string] | NO | omitted | changed or generated artifacts |
| artifacts_count | integer, `>= 0` | NO | omitted | compact summary count |
| commit_hash | string | NO | omitted | commit reference when applicable |
| error_code | string | NO | omitted | stable error category |
| message | string | NO | omitted | short human-readable note |
| progress_pct | integer, `0-100` | NO | omitted | only for `progress` signals |
## Semantic Rules
1. One signal describes one event from one emitter
2. `status=complete` means work concluded successfully enough to advance
3. `status=error` means work failed or blocked
4. `status=progress` means work is ongoing and not yet terminal
5. `progress_pct` is valid only when `status=progress`
6. Optional fields extend context but never replace the required four fields
## Boundary Rules
`signal` IS:
- atomic runtime notification
- status exchange between agents/supervisors
- lightweight machine-readable event
`signal` IS NOT:
- `handoff`: no task list, no scope fence, no execution instructions
- `dispatch_rule`: no keyword map, no routing policy, no satellite selection rules
- `workflow`: no step graph, no sequencing logic
## Canonical Minimal Example
```json
{
  "satellite": "codex",
  "status": "complete",
  "quality_score": 9.0,
  "timestamp": "2026-03-26T10:30:00-03:00"
}
```

### bld_examples_signal.md
---
kind: examples
id: bld_examples_signal
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of signal artifacts
pattern: few-shot learning for minimal orchestration events
---

# Examples: signal-builder
## Golden Example
INPUT: "Emit completion signal for codex after finishing signal-builder"
OUTPUT (`p12_sig_satellite_complete.json`):
```json
{
  "satellite": "codex",
  "status": "complete",
  "quality_score": 9.2,
  "timestamp": "2026-03-26T10:45:00-03:00",
  "task": "signal-builder",
  "artifacts": [
    "archetypes/builders/signal-builder/MANIFEST.md",
    "archetypes/builders/signal-builder/SCHEMA.md"
  ],
  "artifacts_count": 13,
  "commit_hash": "abc1234",
  "message": "13 ISO files created and validated"
}
```
WHY THIS IS GOLDEN:
- filename follows `p12_sig_{event}.json`
- JSON payload is atomic and machine-readable
- required fields are present and typed correctly
- optional fields are compact and useful for monitors
- no handoff instructions, routing rules, or workflow logic
## Golden Progress Example
OUTPUT (`p12_sig_batch_progress.json`):
```json
{
  "satellite": "edison",
  "status": "progress",
  "quality_score": 8.4,
  "timestamp": "2026-03-26T11:00:00-03:00",
  "task": "wave2_batch",
  "progress_pct": 60,
  "message": "6 of 10 artifacts validated"
}
```
WHY THIS PASSES:
- `progress_pct` only appears with `status=progress`
- message stays short
- payload remains a single event snapshot
## Anti-Example
BAD OUTPUT (`p12_sig_dispatch.yaml`):
```yaml
satellite: codex
status: complete
keywords:
  - orchestration
  - routing
next_steps:
  - edit README
  - commit changes
```
FAILURES:
1. wrong machine format: YAML instead of JSON
2. no `quality_score`
3. no `timestamp`
4. includes routing keywords -> `dispatch_rule` drift
5. includes action list -> `handoff` drift

### bld_config_signal.md
---
kind: config
id: bld_config_signal
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: signal Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p12_sig_{event}.json` | `p12_sig_satellite_complete.json` |
| Builder directory | kebab-case | `signal-builder/` |
| Payload fields | snake_case | `quality_score`, `commit_hash` |
| Status values | lowercase enum | `complete`, `error`, `progress` |
| Satellite values | lowercase slug | `codex`, `edison`, `atlas` |
Rule: use `.json` only for this builder.
## File Paths
- Output: `cex/P12_orchestration/compiled/p12_sig_{event}.json`
- Human reference: `cex/P12_orchestration/examples/p12_sig_{event}.md`
## Size Limits
- Preferred payload size: <= 1024 bytes
- Absolute max: 4096 bytes
- Optional fields should remain sparse and compact
## Payload Restrictions
- Required fields must appear exactly as defined in SCHEMA.md
- Omit optional null/unknown fields instead of writing placeholders
- `progress_pct` allowed only when `status=progress`
- `artifacts_count` should match `artifacts` length when both exist
- `quality_score` must stay numeric; never quote it as text
## Boundary Restrictions
- No markdown, prose sections, or frontmatter inside the JSON payload
- No task lists, scope fences, or commit instructions
- No routing tables, keywords arrays for dispatch, or model selection logic

### bld_output_template_signal.md
---
kind: output_template
id: bld_output_template_signal
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a signal
pattern: every field here exists in SCHEMA.md; template derives, never invents
---

# Output Template: signal
Naming pattern: `p12_sig_{event}.json`
Filename: `p12_sig_{{event}}.json`
```json
{
  "satellite": "{{satellite_slug}}",
  "status": "{{complete|error|progress}}",
  "quality_score": {{0.0_to_10.0}},
  "timestamp": "{{ISO_8601_timestamp}}",
  "task": "{{short_task_label_or_omit}}",
  "artifacts": ["{{artifact_path_1}}"],
  "artifacts_count": {{integer_or_omit}},
  "commit_hash": "{{git_hash_or_omit}}",
  "error_code": "{{short_error_code_or_omit}}",
  "message": "{{short_message_or_omit}}",
  "progress_pct": {{0_to_100_or_omit}}
}
```
## Derivation Notes
- The first four fields are the required minimum contract from SCHEMA.md
- All remaining fields are optional extensions from SCHEMA.md
- Omit absent optional fields instead of filling with placeholder strings
- Keep the payload atomic: no instructions, no routing logic, no nested plans

### bld_architecture_signal.md
---
kind: architecture
id: bld_architecture_signal
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of signal — inventory, dependencies, and architectural position
---

# Architecture: signal in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Minimal metadata (id, kind, pillar, emitter, status, timestamp) | signal-builder | active |
| status_field | Signal type: complete, error, or progress | emitter | active |
| payload | Minimal JSON body with score, message, and optional extensions | emitter | active |
| emitter_id | Identifier of the satellite or agent that produced the signal | emitter | active |
| timestamp | ISO 8601 timestamp of emission | system | active |
| extensions | Optional additional fields without breaking consumer contracts | emitter | active |
## Dependency Graph
```
satellite/agent  --emits-->     signal  --consumed_by-->  orchestrator
signal           --consumed_by-->  monitor  --triggers-->  workflow_step
signal           --signals-->      downstream_action
```
| From | To | Type | Data |
|------|----|------|------|
| satellite/agent (P02) | signal | produces | emitter creates signal on task completion or error |
| signal | orchestrator | consumes | orchestrator reads signals to track satellite status |
| signal | monitor | consumes | monitoring system aggregates signals for dashboards |
| signal | workflow_step (P12) | data_flow | signal triggers next step in multi-step workflow |
| signal | downstream_action | signals | cascading action triggered by signal reception |
| spawn_config (P12) | signal | dependency | spawn config defines expected signal patterns |
## Boundary Table
| signal IS | signal IS NOT |
|-----------|---------------|
| An atomic status event between agents (complete, error, progress) | A full instruction set for a task (handoff P12) |
| Minimal JSON payload with low overhead | A routing policy or dispatch rule (dispatch_rule P12) |
| Emitted once per event — fire and forget | A persistent state that evolves over time |
| Consumed by orchestrators and monitors | A multi-step execution flow (workflow P12) |
| Extensible via optional fields without breaking consumers | A schema-heavy artifact requiring full validation |
| Timestamped and attributed to a specific emitter | An anonymous or unattributed event |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Emission | satellite/agent, emitter_id, timestamp | Identify who emitted the signal and when |
| Payload | status_field, payload, extensions | Carry the signal data with optional extensions |
| Consumption | orchestrator, monitor | Read and react to signals |
| Cascading | workflow_step, downstream_action | Trigger subsequent actions based on signal content |

### bld_collaboration_signal.md
---
kind: collaboration
id: bld_collaboration_signal
pillar: P12
llm_function: COLLABORATE
purpose: How signal-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: signal-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what happened, who emitted it, and when?"
I produce minimal JSON payloads for atomic inter-agent status events: complete, error, and progress. I do NOT carry full task instructions (handoff-builder), define routing policy (dispatch-rule-builder), or model workflows and DAGs.
## Crew Compositions
### Crew: "Task Completion Lifecycle"
```
  1. handoff-builder    -> "delivers full instructions and context to the executing agent"
  2. signal-builder     -> "emits atomic complete/error JSON when the agent finishes or fails"
  3. dispatch-rule-builder -> "reads the completion signal and routes next work to the correct agent"
```
### Crew: "Parallel Agent Coordination"
```
  1. dag-builder        -> "defines which agents run in parallel and their dependency edges"
  2. signal-builder     -> "produces the completion signals that unblock downstream DAG nodes"
  3. chain-builder      -> "consumes signals to advance the execution chain to the next step"
```
### Crew: "Progress Monitoring Pipeline"
```
  1. session-state-builder -> "captures current checkpoint and tokens_used from live execution"
  2. signal-builder        -> "wraps checkpoint data into a progress signal with percentage and ETA"
  3. runtime-state-builder -> "persists signal history for audit and retry decisions"
```
## Handoff Protocol
### I Receive
- seeds: emitter agent ID, signal type (complete/error/progress), quality score or error reason
- optional: payload extensions (percentage, eta, artifact path, retry count)
### I Produce
- signal artifact (JSON, fields: id, type, emitter, timestamp, payload, max 40 lines)
- committed to: `cex/P12/examples/signal-{type}-{emitter}-{timestamp}.json`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- session-state-builder: provides checkpoint and progress data used in progress signal payloads
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| dispatch-rule-builder   | reads completion signals to trigger next routing decision |
| chain-builder           | advances to next chain step only after receiving a complete signal |
| dag-builder             | uses signal semantics to define edge conditions between DAG nodes |
| fallback-chain-builder  | reads error signals to decide which fallback path to activate |
| runtime-state-builder   | persists signal history for audit trails and retry logic |

### bld_memory_signal.md
---
kind: memory
id: bld_memory_signal
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for signal artifact generation
---

# Memory: signal-builder
## Summary
Signals are atomic JSON events exchanged between agents: completion, error, progress, and heartbeat notifications. The critical production lesson is payload minimalism — signals must carry the minimum data needed for the consumer to act. Oversized signals clog event channels and break consumers that expect fixed-size payloads. The second lesson is timestamp precision: signals without ISO 8601 timestamps with timezone are unorderable in distributed systems where agents run on different machines.
## Pattern
- Payload must be minimal: status, source agent, timestamp, and optional score/message — nothing else in core fields
- Timestamps must be ISO 8601 with timezone (e.g., 2026-03-27T14:30:00Z) — timezone-naive timestamps are ambiguous
- Status enum must be strict: complete, error, progress — no custom statuses that consumers do not expect
- Source agent identification must be unambiguous: agent name + session ID, not just agent name
- Extension fields must be in a separate extensions object — never pollute core signal fields
- Signal naming must follow a consistent pattern: {source}_{status}_{timestamp}.json
## Anti-Pattern
- Oversized payloads with full task output embedded — signals are notifications, not data transport
- Timezone-naive timestamps — signals from different sources become unorderable
- Custom status values not in the consumer's enum — consumer silently ignores or crashes on unknown status
- Agent name without session ID — cannot distinguish signals from concurrent sessions of the same agent
- Confusing signal (P12, atomic event) with handoff (P12, full task description) or dispatch_rule (P12, routing policy)
- Signals without timestamps — temporal ordering impossible for debugging and monitoring
## Context
Signals operate in the P12 orchestration layer as the communication primitive between agents. They are consumed by monitors, orchestrators, and other agents that need to react to state changes. In multi-agent systems, signals enable coordination without tight coupling — the emitter does not need to know who consumes the signal, only that it conforms to the expected schema.
## Impact
Minimal payloads kept signal processing latency under 10ms versus 200ms+ for bloated signals. ISO 8601 timestamps with timezone enabled correct ordering across 100% of multi-timezone deployments. Strict status enums eliminated 100% of consumer-side unknown-status crashes.
## Reproducibility
Reliable signal production: (1) use only standard status values (complete, error, progress), (2) include ISO 8601 timestamp with timezone, (3) identify source with agent name + session ID, (4) keep core payload minimal, (5) put extensions in separate object, (6) follow naming convention, (7) validate against naming and status gates.
## References
- signal-builder SCHEMA.md (P12 signal specification)
- P12 orchestration pillar specification
- Event-driven architecture and messaging patterns


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `signal-builder` for pipeline function `COLLABORATE`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
