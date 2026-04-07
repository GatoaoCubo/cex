---
kind: examples
id: bld_examples_signal
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of signal artifacts
pattern: few-shot learning for minimal orchestration events
quality: 9.1
title: "Examples Signal"
version: "1.0.0"
author: n03_builder
tags: [signal, builder, examples]
tldr: "Golden and anti-examples for signal construction, demonstrating ideal structure and common pitfalls."
domain: "signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: signal-builder
## Golden Example
INPUT: "Emit completion signal for codex after finishing signal-builder"
OUTPUT (`p12_sig_agent_group_complete.json`):
```json
{
  "agent_group": "codex",
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
  "message": "13 builder spec files created and validated"
}
```
WHY THIS IS GOLDEN:
1. filename follows `p12_sig_{event}.json`
2. JSON payload is atomic and machine-readable
3. required fields are present and typed correctly
4. optional fields are compact and useful for monitors
5. no handoff instructions, routing rules, or workflow logic
## Golden Progress Example
OUTPUT (`p12_sig_batch_progress.json`):
```json
{
  "agent_group": "edison",
  "status": "progress",

  "quality_score": 8.4,
  "timestamp": "2026-03-26T11:00:00-03:00",
  "task": "wave2_batch",
  "progress_pct": 60,

  "message": "6 of 10 artifacts validated"
}
```
WHY THIS PASSES:
1. `progress_pct` only appears with `status=progress`
2. message stays short
3. payload remains a single event snapshot
## Anti-Example
BAD OUTPUT (`p12_sig_dispatch.yaml`):
```yaml
agent_group: codex
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

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | signal construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
