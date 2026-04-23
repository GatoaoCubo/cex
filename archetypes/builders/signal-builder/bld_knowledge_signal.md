---
kind: knowledge_card
id: bld_knowledge_card_signal
pillar: P12
llm_function: INJECT
purpose: Domain knowledge for signal production — atomic searchable facts
sources: signal-builder MANIFEST.md + SCHEMA.md
quality: 9.1
title: "Knowledge Card Signal"
version: "1.0.0"
author: n03_builder
tags: [signal, builder, examples]
tldr: "Golden and anti-examples for signal construction, demonstrating ideal structure and common pitfalls."
domain: "signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_signal
  - bld_examples_signal
  - p03_sp_signal_builder
  - p03_ins_signal_builder
  - p12_sig_admin_orchestration
  - signal-builder
  - p01_kc_signal
  - bld_config_signal
  - bld_architecture_signal
  - bld_collaboration_signal
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
| Required fields | 4: agent_group, status, quality_score, timestamp |
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
| agent_group field | Lowercase slug preferred: `codex`, `edison`, `shaka` |
| quality_score | Reflects event outcome quality (9.0 = clean complete, 5.0 = partial) |
| Immutable once emitted | Never mutate; emit a new signal for updated state |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Task instructions in payload | Signal is not a handoff — no execution content |
| Routing rules or agent_group selection | Signal is not a dispatch_rule |
| `progress_pct` on `status=complete` | Schema violation; pct valid only during ongoing work |
| Omitting `timestamp` | Breaks chronological ordering for signal consumers |
| quality_score outside 0.0–10.0 | Hard schema rejection |
| Multiple signals per single event | One signal = one event; consolidate into single emission |
| Payload > 4096 bytes | Exceeds max; trim optional fields |
## Application
1. Identify the event type: completion, failure/block, or ongoing progress
2. Set `status` to `complete`, `error`, or `progress`
3. Set `agent_group` to lowercase slug of the emitting agent
4. Set `quality_score` (0.0–10.0) reflecting outcome quality
5. Set `timestamp` to current ISO 8601 datetime
6. If `status=progress`, add `progress_pct` (0–100)
7. Add optional fields (task, artifacts, message) only when they add consumer value
8. Name file `p12_sig_{event}.json`, keep under 4096 bytes
## References
- Schema: signal SCHEMA.md (P06)
- Pillar: P12 (orchestration)
- Boundary: handoff (instructions), dispatch_rule (routing), workflow (step graph) — all distinct from signal

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_signal]] | upstream | 0.56 |
| [[bld_examples_signal]] | upstream | 0.52 |
| [[p03_sp_signal_builder]] | upstream | 0.52 |
| [[p03_ins_signal_builder]] | upstream | 0.50 |
| [[p12_sig_admin_orchestration]] | related | 0.48 |
| [[signal-builder]] | related | 0.47 |
| [[p01_kc_signal]] | sibling | 0.45 |
| [[bld_config_signal]] | upstream | 0.44 |
| [[bld_architecture_signal]] | upstream | 0.43 |
| [[bld_collaboration_signal]] | related | 0.41 |
