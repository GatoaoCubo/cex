# CEX Crew Runner -- Builder Execution
**Builder**: `session-state-builder`
**Function**: INJECT
**Intent**: reconstroi agent-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:20.324811

## Intent Context
- **Verb**: reconstroi
- **Object**: agent-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_session_state.md
---
id: session-state-builder
kind: type_builder
parent: null
pillar: P10
domain: session_state
llm_function: INJECT
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: CODEX
tags: [kind-builder, session-state, P10, memory, specialist]
---

# session-state-builder
## Identity
Especialista em construir `session_state` de P10: snapshots efemeros de sessao
que capturam estado momentaneo de um agente durante execucao.
## Capabilities
- Produzir session_state YAML com campos minimos e naming P10 corretos
- Distinguir session_state de runtime_state e learning_record sem sobreposicao
- Modelar contexto efemero com checkpoints e recovery sem persistencia entre sessoes
- Validar snapshots contra gates duros de naming, campos obrigatorios e tamanho
## Routing
keywords: [session, snapshot, state, checkpoint, ephemeral, context_window, tokens]
triggers: "captura estado da sessao", "snapshot de contexto atual", "registra checkpoint"
## Crew Role
In a crew, I handle EPHEMERAL STATE CAPTURE.
I answer: "what is the agent's current session state right now?"
I do NOT handle: persistent state, accumulated learning, search indexes, workflows.

### bld_instruction_session_state.md
---
id: p03_ins_session_state_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Session State Builder Instructions
target: session-state-builder agent
phases_count: 3
prerequisites:
  - Agent or satellite name is known (non-empty string)
  - Session identifier is available (unique per execution context)
  - Current session status is known (active, paused, completed, or aborted)
  - Session start timestamp is available in ISO 8601 format
validation_method: checklist
domain: session_state
quality: null
tags: [instruction, session-state, memory, ephemeral, P10]
idempotent: false
atomic: true
rollback: "null — session_state is ephemeral; discard and recapture if invalid"
dependencies: []
logging: true
tldr: Capture an agent's ephemeral session snapshot with context, resource usage, and checkpoints — under 3072 bytes, no persistence across sessions.
density_score: 0.87
---

## Context
The session-state-builder produces `session_state` artifacts — ephemeral YAML snapshots
that capture an agent's momentary execution state during a live session. A session_state
records what the agent is currently doing, what resources it has consumed, and where
recovery checkpoints exist if the session is interrupted.
**Input contract**:
- `{{agent_name}}`: the agent or satellite being snapshotted (e.g. `build-sat`, `research-agent`)
- `{{session_id}}`: unique identifier for this execution context (e.g. `sess_20260327_001`)
- `{{session_status}}`: one of `active`, `paused`, `completed`, `aborted`
- `{{started_at}}`: ISO 8601 timestamp of session start
- `{{context_data}}`: optional free-text description of current tasks and state
**Output contract**: A single `session_state` YAML file named `p10_ss_{{session_slug}}.yaml`,
under 3072 bytes, with required frontmatter and three body sections: Active Context,
Resource Usage, and Checkpoints.
**Boundaries**:
- session_state is ephemeral — it captures a moment, not accumulated history.
- Accumulated learning across sessions belongs in a learning_record artifact.
- Persistent runtime state that outlasts a session belongs in a runtime_state artifact.
- Search indexes and knowledge bases are separate artifacts entirely.
- Absent optional fields must be omitted, not filled with placeholder values.
## Phases
### Phase 1: Capture
**Primary action**: Collect all observable facts about the current session state before
writing any YAML.
```
INPUT: agent_name, session_id, session_status, started_at, context_data
1. Derive session_slug for the filename:
   session_slug = session_id.lower().replace(" ", "_").replace("-", "_")
   Verify slug matches pattern: ^[a-z][a-z0-9_]+$
2. Resolve session_status to one of the four valid values:
   active    -> agent is currently executing
   paused    -> agent is waiting for external input or resource
   completed -> agent finished all assigned work
   aborted   -> session terminated before completion
3. Extract current tasks from context_data (if provided):
   current_tasks = list of task descriptions the agent is mid-execution on
   if context_data is empty: current_tasks = []
4. Estimate resource usage from available signals:
   tokens_used: integer or null
   tools_invoked: list of tool names or []
   elapsed_seconds: integer or null
   error_count: integer, default 0
5. Identify recovery checkpoints (if any):
   checkpoint = {
     label: short name (e.g. "after_phase_2"),
     description: what was completed up to this point,
     resumable: true | false
   }
   checkpoints = [] if none exist
OUTPUT: session_slug, session_status, current_tasks[], resource_usage{},
        checkpoints[]
```
Verification: `session_slug` matches naming pattern. `session_status` is one of four
valid values.
### Phase 2: Compose
**Primary action**: Assemble the captured data into a valid session_state YAML artifact
following the schema exactly.
```
INPUT: all outputs from Phase 1, agent_name, session_id, started_at
1. Set filename: p10_ss_{{session_slug}}.yaml
2. Assemble frontmatter (required fields):
   id: p10_ss_{{session_slug}}
   kind: session_state
   pillar: P10
   version: 1.0.0
   agent: {{agent_name}}
   session_id: {{session_id}}
   status: {{session_status}}
   started_at: {{started_at}}
   captured_at: current ISO 8601 timestamp
   quality: null
3. Write Active Context section:
   List current_tasks as bullet items.
   If current_tasks is empty: write "No active tasks — session is {{session_status}}."
4. Write Resource Usage section:
   Emit only fields with known values. Omit fields where value is null unless
   null is the correct documented value (e.g. tokens_used: null is valid when
   token counting is unavailable).
   resource_usage:
     tokens_used: {{tokens_used}}
     tools_invoked: {{tools_invoked}}
     elapsed_seconds: {{elapsed_seconds}}
     error_count: {{error_count}}
5. Write Checkpoints section:
   If checkpoints is non-empty: emit as YAML list with label, description, resumable.
   If checkpoints is empty: write "checkpoints: []"
6. Size check:
   Estimate byte count of assembled YAML.
   If estimate > 3072 bytes:
     Truncate current_tasks to the 3 most recent items.
     Truncate tools_invoked to the 10 most recent entries.
     Re-estimate. If still > 3072: remove optional narrative fields.
OUTPUT: session_state YAML content (assembled, not yet validated)
```
Verification: file is named `p10_ss_{{session_slug}}.yaml`. Estimated size <= 3072 bytes.
### Phase 3: Validate
**Primary action**: Run all quality gates against the assembled artifact and output the
final file only if all HARD gates pass.
```
INPUT: session_state YAML content
1. HARD quality gates (all must pass):
   HARD_1: id matches pattern ^p10_ss_[a-z][a-z0-9_]+$
   HARD_2: kind == "session_state"
   HARD_3: status is one of active/paused/completed/aborted
   HARD_4: started_at is valid ISO 8601 timestamp
   HARD_5: captured_at is valid ISO 8601 timestamp
   HARD_6: quality == null
   HARD_7: artifact size <= 3072 bytes
   HARD_8: no placeholder values present ({{...}}, TBD, N/A as strings)
2. Boundary check:

### bld_knowledge_card_session_state.md
---
kind: knowledge_card
id: bld_knowledge_card_session_state
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for session_state production — atomic searchable facts
sources: session-state-builder MANIFEST.md + SCHEMA.md, P10 schema
---

# Domain Knowledge: session_state
## Executive Summary
Session states are ephemeral snapshots of an agent's execution context — they capture what the agent is doing right now, how far along it is, and where recovery can resume. Each snapshot is a single-point observation (not a time series) consumed by monitors, recovery tools, and post-session extractors. They differ from runtime states (which persist across sessions and drive decisions), learning records (which accumulate experience over time), and axioms (which are immutable truths) by being strictly ephemeral observations lost when the session ends.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (memory) |
| Kind | `session_state` (exact literal) |
| ID pattern | `p10_ss_{session_slug}` |
| Naming | `p10_ss_{agent}_{task}.yaml` |
| Required frontmatter | session_id, agent, status, started_at + standard CEX fields |
| Max body | 3072 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Status values | active, paused, completed, aborted |
| Format | YAML (machine-parseable) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Minimum semantic contract | session_id + agent + status + started_at — always present |
| Status semantics | active (in progress), paused (recoverable), completed (normal end), aborted (abnormal) |
| Optional runtime metrics | active_tasks, context_window_used, tools_called, errors, checkpoints |
| Single-point snapshot | One observation, not a time series; no historical data |
| Graceful degradation | Must work when optional fields are absent |
| Machine-parseable format | YAML for programmatic consumption by monitors |
| Checkpoint for recovery | last_checkpoint enables resume after interruption |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Persistent state in session_state | Session state is ephemeral; use runtime_state for persistence |
| Time series data | Not a log; single snapshot per write |
| Missing session_id | Core identifier; cannot correlate with other session data |
| Missing status field | Consumers cannot determine agent lifecycle phase |
| Body > 3072 bytes | Exceeds max; session states must be compact |
| Routing decisions in session state | Routing belongs in runtime_state or mental_model |
| Optional fields without graceful fallback | Consumers break when optional fields absent |
## Application
1. Set session_id (unique execution context identifier)
2. Set agent (which agent is executing)
3. Set status: active, paused, completed, or aborted
4. Set started_at (ISO 8601 timestamp)
5. Add optional metrics as needed: tasks, context window, tools, errors
6. Add checkpoint data for recovery if applicable
7. Keep body compact (single snapshot); validate <= 3072 bytes
## References
- session-state-builder SCHEMA.md v1.0.0
- P10 memory pillar schema
- Finite state machine (status lifecycle)

### bld_quality_gate_session_state.md
---
id: p11_qg_session-state
kind: quality_gate
pillar: P11
title: "Gate: Session State"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: session_state
quality: null
density_score: 0.85
tags:
  - quality-gate
  - session-state
  - ephemeral
  - p11
tldr: "Gates ensuring session state specs define minimal checkpoint fields, realistic TTL, and a recovery protocol for partial or expired state."
---

## Definition
A session state spec describes an ephemeral snapshot of an in-progress interaction: which fields to capture, how long the snapshot lives, and how to restore a session from it. A spec passes this gate when the captured fields are the minimum necessary to resume work (not a full database dump), the TTL reflects the realistic session length, and partial or expired state has a defined recovery path rather than a hard failure.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`session-state-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `session_state` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains **Checkpoint fields** defined (named list of fields captured at each checkpoint, with type per field) | Without a field list, the snapshot schema is undefined and serialization is non-deterministic |
| H08 | Spec contains an **Expiry / TTL** value (numeric duration + unit, e.g., `ttl: 3600s`) | Without TTL, expired state accumulates and privacy risks cannot be bounded |
| H09 | Spec contains a **Recovery protocol** (what to do when state is absent, partial, or expired at resume time) | Missing recovery causes hard failures instead of graceful degradation |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Fields capture minimal necessary state (no redundant or derivable fields) | 1.0 | Many redundant fields | Some redundancy | Only fields that cannot be recomputed from stable data |
| 3 | TTL realistic for session length (not too short causing premature expiry, not too long accumulating stale state) | 1.0 | TTL not justified | Round-number guess | TTL derived from measured or estimated session duration |
| 4 | Recovery handles partial state (spec addresses incomplete snapshots, not just absent ones) | 1.0 | Only absent state handled | Partial noted, no procedure | Explicit partial-state recovery logic per missing field |
| 5 | No persistent data (all captured data is ephemeral; storage backend is volatile) | 1.0 | Persistent writes present or unclear | Noted as ephemeral | Explicit confirmation + storage backend is volatile (memory or cache) |
| 6 | Tags include `session-state` | 0.5 | Missing | Present but misspelled | Exactly `session-state` in tags list |
| 7 | Token budget tracking noted (LLM context budget included or explicitly excluded with reason) | 0.5 | No mention | Noted as not applicable | Explicitly included or explicitly excluded with reason |
| 8 | Serialization format defined (JSON, msgpack, etc.) with example serialized snapshot | 1.0 | No format stated | Format named only | Format + example snapshot + size estimate |

### bld_schema_session_state.md
---
kind: schema
id: bld_schema_session_state
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for session_state - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
---

# Schema: session_state
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P10` |
| Type | literal `session_state` |
| Machine format | `yaml` |
| Naming | `p10_ss_{session}.yaml` |
| Max bytes | 3072 |
## Required Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (`p10_ss_{slug}`) | YES | - | Unique session state identifier |
| kind | literal "session_state" | YES | - | Type integrity |
| lp | literal "P10" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| session_id | string | YES | - | Unique session identifier |
| agent | string | YES | - | Agent or satellite that owns this state |
| status | enum (`active`, `paused`, `completed`, `aborted`) | YES | - | Current session lifecycle status |
| started_at | string, ISO 8601 | YES | - | Session start timestamp |
| domain | string | YES | - | Domain this artifact belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Searchability |
| tldr | string <= 160ch | YES | - | Dense summary |
## Optional Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| ended_at | string, ISO 8601 | NO | omitted | Session end timestamp |
| duration_seconds | integer >= 0 | NO | omitted | Elapsed time |
| active_tasks | list[string] | NO | omitted | Currently running tasks |
| completed_tasks | list[string] | NO | omitted | Tasks finished this session |
| context_window_used | integer >= 0 | NO | omitted | Tokens consumed so far |
| context_window_max | integer >= 0 | NO | omitted | Max tokens available |
| tools_called | list[string] | NO | omitted | Tools invoked during session |
| tool_call_count | integer >= 0 | NO | omitted | Total tool invocations |
| errors | list[object{code, message}] | NO | omitted | Errors encountered |
| error_count | integer >= 0 | NO | omitted | Total errors |
| checkpoints | list[object{label, timestamp}] | NO | omitted | Recovery points |
| last_checkpoint | string | NO | omitted | Most recent checkpoint label |
| keywords | list[string] | NO | omitted | Brain search terms |
| linked_artifacts | object {primary, related} | NO | omitted | Cross-references |
## Semantic Rules
1. One session_state describes one session of one agent at one moment
2. `status=active` means session is in progress
3. `status=paused` means session is suspended but recoverable
4. `status=completed` means session ended normally
5. `status=aborted` means session ended abnormally
6. Session state is ephemeral: it is NOT accumulated across sessions
7. Optional fields extend the snapshot but never replace required fields
## Boundary Rules
`session_state` IS:
- ephemeral snapshot of current session
- point-in-time capture of agent execution context
- recoverable checkpoint data
`session_state` IS NOT:
- `runtime_state`: persistent state carried across sessions, accumulated routing decisions
- `learning_record`: accumulated learning from outcomes, patterns over time
- `brain_index`: search index configuration (BM25, FAISS)
- `axiom`: immutable fundamental rule
## ID Pattern
Regex: `^p10_ss_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Active Context` — current tasks and execution state
2. `## Resource Usage` — tokens, tools, time consumption
3. `## Checkpoints` — recovery points captured during session
## Constraints
- max_bytes: 3072
- naming: `p10_ss_{session}.yaml`
- id == filename stem
- No persistent state: session_state dies when session ends
- No learning accumulation: use learning_record for that

### bld_examples_session_state.md
---
kind: examples
id: bld_examples_session_state
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of session_state artifacts
pattern: few-shot learning for ephemeral session snapshots
---

# Examples: session-state-builder
## Golden Example
INPUT: "Capture session state for edison building wave 19 builders"
OUTPUT (`p10_ss_edison_wave19_build.yaml`):
```yaml
id: p10_ss_edison_wave19_build
kind: session_state
lp: P10
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "codex"
session_id: "edison_20260326_143000"
agent: "edison"
status: "active"
started_at: "2026-03-26T14:30:00-03:00"
domain: "orchestration"
quality: null
tags: [session-state, edison, wave19, build]
tldr: "Edison session building 3 Wave 19 builders, 2 of 3 complete, 67% context used"
ended_at: null
duration_seconds: 1800
active_tasks: ["handoff-builder"]
completed_tasks: ["session-state-builder", "dag-builder"]
context_window_used: 134000
context_window_max: 200000
tools_called: ["Read", "Write", "Glob", "Grep", "Bash"]
tool_call_count: 87
errors:
  - code: "glob_empty"
    message: "no files found for pattern archetypes/builders/dag-builder/"
error_count: 1
checkpoints:
  - label: "session_state_builder_done"
    timestamp: "2026-03-26T14:45:00-03:00"
  - label: "dag_builder_done"
    timestamp: "2026-03-26T15:00:00-03:00"
last_checkpoint: "dag_builder_done"
keywords: [session, snapshot, edison, wave19]
linked_artifacts:
  primary: "archetypes/builders/session-state-builder/"
  related: ["archetypes/builders/dag-builder/", "archetypes/builders/handoff-builder/"]
```
WHY THIS IS GOLDEN (19+ fields present):
- filename follows `p10_ss_{session}.yaml`
- YAML with proper frontmatter delimiters
- all 15 required fields present and typed correctly
- 10 optional fields add meaningful runtime context
- no persistent state, no accumulated learning across sessions
- checkpoints with label + timestamp enable recovery
- error entry has both code and message
- tldr is informative and under 160 characters
- ephemeral: describes this session only, not prior sessions
- tags length >= 3 and descriptive
## Anti-Example
BAD OUTPUT (`p10_ss_runtime.yaml`):
```yaml
id: p10_rs_edison_state
kind: runtime_state
lp: P10
agent: edison
routing_decisions:
  marketing: lily
  research: shaka
  build: edison
accumulated_scores:
  - session: "20260325"
    score: 8.5
  - session: "20260326"
    score: 9.0
learned_patterns:
  - "always read SCHEMA first"
  - "commit after each builder"
```
FAILURES:
1. wrong id prefix: `p10_rs_` instead of `p10_ss_` — violates H01 naming gate
2. wrong kind: `runtime_state` instead of `session_state` — violates H04 type integrity
3. missing `session_id` required field — violates H03 completeness
4. missing `status` required field — violates H03 and H05 lifecycle contract
5. missing `started_at` required field — violates H03 and H09 temporal integrity
6. missing `quality: null` — violates H03 and H06 self-score gate
7. missing `tags` and `tldr` required fields — violates H03 completeness
8. contains `routing_decisions`: persistent cross-session state — violates H08 boundary
9. contains `accumulated_scores`: cross-session accumulation — violates H08 boundary (learning_record drift)
10. contains `learned_patterns`: accumulated learning — violates H08 boundary (learning_record drift)

### bld_config_session_state.md
---
kind: config
id: bld_config_session_state
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: session_state Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p10_ss_{session}.yaml` | `p10_ss_edison_wave19_build.yaml` |
| Builder directory | kebab-case | `session-state-builder/` |
| Frontmatter fields | snake_case | `session_id`, `started_at` |
| Status values | lowercase enum | `active`, `paused`, `completed`, `aborted` |
| Agent values | lowercase slug | `edison`, `atlas`, `codex` |
Rule: use `.yaml` extension only for this builder.
## File Paths
- Output: `cex/P10_memory/compiled/p10_ss_{session}.yaml`
- Human reference: `cex/P10_memory/examples/p10_ss_{session}.md`
## Size Limits
- Preferred snapshot size: <= 2048 bytes
- Absolute max: 3072 bytes
- Optional fields should remain sparse and compact
## Payload Restrictions
- Required fields must appear exactly as defined in SCHEMA.md
- Omit optional null/unknown fields instead of writing placeholders
- `ended_at` and `duration_seconds` only meaningful for completed/aborted sessions
- `checkpoints` should be concise: label + timestamp only
- `errors` entries must have both `code` and `message`
## Boundary Restrictions
- No persistent state: routing decisions, accumulated scores belong in runtime_state
- No learning patterns: accumulated outcomes belong in learning_record
- No search configuration: index settings belong in brain_index
- No immutable rules: fundamental axioms belong in axiom

### bld_output_template_session_state.md
---
kind: output_template
id: bld_output_template_session_state
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a session_state
pattern: every field here exists in SCHEMA.md; template derives, never invents
---

# Output Template: session_state
Naming pattern: `p10_ss_{session}.yaml`
Filename: `p10_ss_{{session_slug}}.yaml`
```yaml
id: p10_ss_{{session_slug}}
kind: session_state
lp: P10
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
session_id: "{{unique_session_id}}"
agent: "{{agent_or_satellite}}"
status: "{{active|paused|completed|aborted}}"
started_at: "{{ISO_8601_timestamp}}"
domain: "{{domain_value}}"
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
ended_at: "{{ISO_8601_or_omit}}"
duration_seconds: {{integer_or_omit}}
active_tasks: [{{task_labels_or_omit}}]
completed_tasks: [{{task_labels_or_omit}}]
context_window_used: {{integer_or_omit}}
context_window_max: {{integer_or_omit}}
tools_called: [{{tool_names_or_omit}}]
tool_call_count: {{integer_or_omit}}
errors:
  - code: "{{error_code_or_omit}}"
    message: "{{error_message_or_omit}}"
error_count: {{integer_or_omit}}
checkpoints:
  - label: "{{checkpoint_label_or_omit}}"
    timestamp: "{{ISO_8601_or_omit}}"
last_checkpoint: "{{label_or_omit}}"
keywords: [{{keyword_1}}, {{keyword_2}}]
linked_artifacts:
  primary: "{{primary_ref_or_omit}}"
  related: [{{related_refs_or_omit}}]
```
## Derivation Notes
- Required fields (id through tldr) form the minimum valid snapshot
- Optional fields capture richer execution context when available
- Omit absent optional fields instead of writing placeholder values
- Keep the snapshot ephemeral: no accumulated history, no persistent routing

### bld_architecture_session_state.md
---
kind: architecture
id: bld_architecture_session_state
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of session_state — inventory, dependencies, and architectural position
---

# Architecture: session_state in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, session_id, agent, timestamp, etc.) | session-state-builder | active |
| context_snapshot | Current context window contents and token usage | agent | active |
| checkpoint_data | Resumable state for crash recovery or context overflow | agent | active |
| active_tasks | List of in-progress tasks with status and progress | agent | active |
| tool_state | Current tool invocations and pending results | agent | active |
| token_budget | Remaining token allocation and compression status | agent | active |
## Dependency Graph
```
agent           --produces-->   session_state  --consumed_by-->  recovery_system
session_state   --feeds-->      learning_record  --signals-->    checkpoint_event
session_state   --consumed_by-->  context_manager
```
| From | To | Type | Data |
|------|----|------|------|
| agent (P02) | session_state | produces | agent dumps current state as ephemeral snapshot |
| session_state | recovery_system | consumes | checkpoint data used for crash recovery |
| session_state | learning_record (P10) | data_flow | session data distilled into persistent learning |
| session_state | context_manager | consumes | context manager reads token budget and usage |
| session_state | checkpoint_event (P12) | signals | emitted when checkpoint is saved |
| runtime_state (P10) | session_state | dependency | runtime state provides initial values for session |
## Boundary Table
| session_state IS | session_state IS NOT |
|------------------|----------------------|
| An ephemeral snapshot of current session context | A persistent record of accumulated experience (learning_record P10) |
| Discarded when session ends — not cross-session | A variable state that persists across sessions (runtime_state P10) |
| Contains token usage, active tasks, and checkpoints | A design-time cognitive map (mental_model P02) |
| Used for crash recovery and context overflow management | A search index or knowledge base (brain_index P01) |
| Scoped to one session of one agent | A shared state across multiple agents |
| Lightweight snapshot with minimal overhead | A comprehensive audit log of all actions |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Source | agent, runtime_state | Agent execution produces session data |
| Snapshot | frontmatter, context_snapshot, token_budget | Capture current context and resource usage |
| Tasks | active_tasks, tool_state | Track in-progress work and pending tool results |
| Recovery | checkpoint_data, recovery_system | Enable crash recovery and context overflow handling |
| Downstream | learning_record, checkpoint_event | Distill persistent learning and signal checkpoints |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `session-state-builder` for pipeline function `INJECT`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
