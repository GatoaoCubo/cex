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

---

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

---

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

---

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
   Verify the artifact captures ONLY the current session moment.
   Flag if content describes: accumulated patterns, historical performance,
   knowledge base entries, or persistent configuration — these are NOT session_state.

3. If any HARD gate fails:
   Identify the failing gate. Fix the specific issue. Re-run validation.
   Do not output the artifact until all HARD gates pass.

4. SOFT quality gates (record pass/fail but do not block output):
   SOFT_1: current_tasks is non-empty when status == "active"
   SOFT_2: at least one checkpoint exists when elapsed_seconds > 60
   SOFT_3: error_count is explicitly set (not omitted)
   SOFT_4: tools_invoked list is populated when tools were used
   SOFT_5: captured_at and started_at difference is plausible (captured >= started)

OUTPUT: validated session_state YAML file, gate_results{hard: N/8, soft: N/5}
```

Verification: all 8 HARD gates pass. File written only after validation succeeds.

---

## Output Contract

```yaml
---
id: p10_ss_{{session_slug}}
kind: session_state
pillar: P10
version: 1.0.0
agent: {{agent_name}}
session_id: {{session_id}}
status: {{session_status}}
started_at: {{started_at}}
captured_at: {{captured_at}}
quality: null
---

# Session State: {{agent_name}} / {{session_id}}

## Active Context

{{current_tasks_as_bullet_list_or_status_note}}

## Resource Usage

resource_usage:
  tokens_used: {{tokens_used}}
  tools_invoked: {{tools_invoked_as_list}}
  elapsed_seconds: {{elapsed_seconds}}
  error_count: {{error_count}}

## Checkpoints

{{checkpoints_as_yaml_list_or_empty_list}}
```

---

## Validation

- [ ] HARD: `id` matches pattern `^p10_ss_[a-z][a-z0-9_]+$`
- [ ] HARD: `kind` equals `session_state`
- [ ] HARD: `status` is one of `active`, `paused`, `completed`, `aborted`
- [ ] HARD: `started_at` is a valid ISO 8601 timestamp
- [ ] HARD: `captured_at` is a valid ISO 8601 timestamp
- [ ] HARD: `quality` equals `null`
- [ ] HARD: artifact total size is <= 3072 bytes
- [ ] HARD: no placeholder strings present in output (`{{...}}`, `TBD`, `N/A`)
- [ ] SOFT: `current_tasks` is non-empty when `status` is `active`
- [ ] SOFT: at least one checkpoint defined when `elapsed_seconds` > 60
- [ ] SOFT: `error_count` is explicitly set
- [ ] SOFT: `tools_invoked` is populated when tools were used
- [ ] SOFT: `captured_at` >= `started_at` (temporal consistency)

**Score threshold**: All 8 HARD gates must pass. Artifact is not output until they do.

---

## Metacognition

**Does**:
- Capture an agent's ephemeral execution state at a single point in time
- Record current tasks, resource usage, and recovery checkpoints
- Enforce strict size limit (3072 bytes) to keep snapshots lightweight
- Distinguish ephemeral session capture from persistent state artifacts

**Does NOT**:
- Accumulate learning or patterns across sessions (learning_record artifact)
- Persist state that outlasts the current session (runtime_state artifact)
- Manage search indexes or knowledge bases
- Capture workflow routing logic or execution plans

**Chaining**:
- Before: any active agent execution that needs a mid-run snapshot
- After: a recovery mechanism may read checkpoints to resume from interruption
- After: a monitoring agent may aggregate session_states to detect stalls
- Note: session_state is NOT chained to pool — it is ephemeral and discarded after use
