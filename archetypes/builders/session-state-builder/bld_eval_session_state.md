---
kind: quality_gate
id: p11_qg_session-state
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of session_state artifacts
pattern: few-shot learning for ephemeral session snapshots
quality: 9.0
title: 'Gate: Session State'
version: 1.0.0
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: Gates ensuring session state specs define minimal checkpoint fields, realistic
  TTL, and a recovery protocol for partial or expired state.
domain: session_state
created: '2026-03-27'
updated: '2026-03-27'
last_reviewed: '2026-04-18'
density_score: 0.85
related:
  - bld_memory_session_state
  - bld_collaboration_session_state
  - session-state-builder
  - p03_sp_session_state_builder
  - bld_memory_runtime_state
  - p11_qg_checkpoint
  - bld_examples_session_state
  - p11_qg_runtime_state
  - bld_knowledge_card_session_state
  - p11_qg_agent-card
---

## Quality Gate

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

## Examples

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

## Golden Example 2 (HERMES — Session with FTS5 Search Backend)
INPUT: "Capture session state for n04 building knowledge index with FTS5 cross-session recall enabled"
OUTPUT (`p10_ss_n04_kc_index_build.yaml`):
```yaml
id: p10_ss_n04_kc_index_build
kind: session_state
lp: P10
version: "1.0.0"
created: "2026-04-18"
updated: "2026-04-18"
author: "n04_knowledge"
session_id: "n04_20260418_110000"
agent: "n04_knowledge"
status: "active"
started_at: "2026-04-18T11:00:00-03:00"
domain: "knowledge_management"
quality: null
tags: [session-state, n04, knowledge-index, fts5, hermes]
tldr: "N04 session building KC index; FTS5 search active, cross-session recall ON, 2k token budget"
active_tasks: ["knowledge-index-builder"]
completed_tasks: []
context_window_used: 42000
context_window_max: 200000
tools_called: ["Read", "Glob", "Grep", "Write"]
tool_call_count: 23
search_backend: fts5
summarizer_model: "claude-haiku-4-5"
summarization_token_budget: 2000
cross_session_recall: true
```
WHY THIS IS GOLDEN (HERMES search fields):
- `search_backend: fts5`: declares per-session FTS5 index for fast KC retrieval within session
- `summarizer_model`: lightweight Haiku handles FTS5 hit summarization to preserve context budget
- `summarization_token_budget: 2000`: explicit cap prevents summary injection from overrunning context
- `cross_session_recall: true`: enables this session's history to be searchable by future sessions

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
