---
kind: schema
id: bld_schema_session_state
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for session_state - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
quality: 9.1
title: "Schema Session State"
version: "1.0.1"
author: n03_builder
tags: [session_state, builder, examples]
tldr: "Golden and anti-examples for session state construction, demonstrating ideal structure and common pitfalls."
domain: "session state construction"
created: "2026-04-07"
updated: "2026-04-18"
last_reviewed: "2026-04-18"
density_score: 0.90
related:
  - bld_schema_handoff
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_dag
  - bld_schema_runtime_state
  - bld_schema_reranker_config
  - bld_schema_agent_profile
  - bld_schema_sandbox_config
  - bld_schema_benchmark_suite
  - bld_schema_input_schema
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
| agent | string | YES | - | Agent or agent_group that owns this state |
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
| search_backend | enum (none, fts5, pgvector, hybrid) | NO | none | Per-session search index backend |
| summarizer_model | string | NO | null | Model used for FTS5 hit summarization |
| summarization_token_budget | int | NO | 2000 | Max tokens for summary injection |
| cross_session_recall | bool | NO | false | If true, history searchable across sessions |
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
- `knowledge_index`: search index configuration (BM25, FAISS)
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_handoff]] | sibling | 0.54 |
| [[bld_schema_usage_report]] | sibling | 0.50 |
| [[bld_schema_dataset_card]] | sibling | 0.48 |
| [[bld_schema_dag]] | sibling | 0.48 |
| [[bld_schema_runtime_state]] | sibling | 0.47 |
| [[bld_schema_reranker_config]] | sibling | 0.47 |
| [[bld_schema_agent_profile]] | sibling | 0.46 |
| [[bld_schema_sandbox_config]] | sibling | 0.46 |
| [[bld_schema_benchmark_suite]] | sibling | 0.46 |
| [[bld_schema_input_schema]] | sibling | 0.45 |
