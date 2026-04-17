---
id: p10_ms_n04_knowledge
kind: memory_summary
pillar: P10
nucleus: n04
title: "Memory Summary -- N04 Knowledge Nucleus Session Compression Protocol"
version: "1.0.0"
quality: null
tags: [memory_summary, compression, episodic, session, n04, P10]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "Protocol for compressing N04 session transcripts and episodic memory into dense summaries. Defines summary schema, extraction heuristics, compression ratio targets, and injection format for future context windows."
density_score: null
---

# Memory Summary: N04 Session Compression Protocol

## Purpose

200K context window is large but not infinite. Long sessions, complex missions, and
multi-wave orchestrations accumulate thousands of tokens of context that become stale.
This protocol converts that raw context into dense, retrievable summaries.

Reference: LangMem (Google) for compression primitives; MemGPT/Letta for hierarchical paging.

---

## Summary Schema

```yaml
id: "ms_{nucleus}_{YYYYMMDD}_{session_hash}"
kind: memory_summary
source_session_id: "uuid"
nucleus: "n04"
date: "ISO 8601"
compression_ratio: 0.12          # compressed_tokens / original_tokens
original_tokens: 45000
compressed_tokens: 5400
extraction_method: "llm"         # "llm" | "heuristic" | "hybrid"
quality_signal: 0.82             # 0.0-1.0, confidence in summary completeness

task_summary: "one-sentence description of what was accomplished"

key_decisions:
  - "decision 1 with rationale"
  - "decision 2 with rationale"

facts_extracted:
  - id: "fact_uuid"
    claim: "statement"
    confidence: 0.9
    source: "path or session turn"

entities_encountered:
  - name: "entity name"
    type: "nucleus | kind | tool | concept | person"
    status: "new | updated | confirmed"

artifacts_produced:
  - path: "N04_knowledge/P10_memory/memory_architecture_n04.md"
    kind: "memory_architecture"
    quality: null

procedures_learned:
  - "description of new procedure or updated SOP"

gaps_identified:
  - "what was missing, unresolved, or needs follow-up"

signal_sent: true
commit_hash: "short hash if applicable"
```

---

## Extraction Heuristics (Fast Mode)

When LLM compression is too expensive, apply these rules:

| Signal | Extract? | Why |
|--------|----------|-----|
| Tool call with Write result | YES | Artifact created -- preserve path + kind |
| User decision statement | YES | GDP decision -- permanent value |
| Error message + resolution | YES | Debugging pattern -- procedural value |
| File read operation | NO | Content is in the corpus, not the summary |
| Repeated identical content | NO | Deduplicate |
| Casual clarification | NO | Low signal |
| Test output success | MAYBE | Only if new capability proven |
| N07 dispatch command | YES | Mission state change |
| Signal written | YES | Completion event |

---

## Compression Targets

| Session Type | Target Ratio | Max Compressed Tokens |
|-------------|-------------|----------------------|
| Quick task (< 10 min) | 0.20 | 1000 |
| Standard mission (30 min) | 0.12 | 3000 |
| Full grid (90+ min) | 0.06 | 8000 |
| Multi-wave overnight | 0.04 | 12000 |

---

## Injection Format (for Future Context Windows)

When a session summary is loaded into a new context window as prior context:

```
=== PRIOR SESSION SUMMARY (N04, {date}) ===
Task: {task_summary}
Artifacts: {artifact list}
Key decisions: {decision list}
Facts to remember: {top 5 facts by confidence}
Gaps: {gap list}
=== END PRIOR SESSION ===
```

This format is:
- Consistent (always same structure for easy parsing)
- Dense (target < 500 tokens per summary injection)
- Actionable (gaps tell the nucleus what to do next)

---

## Multi-Session Compression

When >= 3 session summaries exist on the same topic, compress them further:

1. Load all N session summaries for the topic
2. Extract: unique facts (deduplicate across sessions)
3. Merge: decisions from multiple sessions into chronological timeline
4. Synthesize: write a "domain summary" KC in P01_knowledge/
5. Retire: mark individual session summaries as `archived: true`

This is the knowledge distillation step: raw episodic memory -> permanent semantic knowledge.

---

## Trigger Matrix

| When | Action |
|------|--------|
| Context > 80% full | Compress oldest 30% of context |
| Session ends normally | Full session compression to summary |
| `/consolidate` called | Compress all unarchived session summaries |
| Weekly cron | Compress sessions older than 30 days |
| Mission complete | Compress mission-scope context |
