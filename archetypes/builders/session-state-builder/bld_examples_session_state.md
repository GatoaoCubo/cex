---
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
---
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
---
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
---
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
---
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
