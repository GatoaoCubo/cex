---
kind: examples
id: bld_examples_handoff_protocol
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of handoff_protocol artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: handoff-protocol-builder
## Golden Example
INPUT: "Create handoff protocol for research delegation from STELLA to SHAKA"
OUTPUT:
```yaml
id: p02_handoff_stella_to_shaka
kind: handoff_protocol
pillar: P02
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "EDISON"
name: "STELLA-to-SHAKA Research Delegation"
quality: null
tags: [handoff_protocol, P02, handoff]
tldr: "STELLA-to-SHAKA Research Delegation — production-ready handoff_protocol configuration"
```
## Overview
Handoff protocol for delegating research tasks from STELLA (orchestrator) to SHAKA (research satellite).
STELLA detects research intent, composes context, and dispatches via handoff file.

## Trigger
Condition: task keywords match [research, analyze, investigate, compare, benchmark, scrape].
Confidence threshold: >= 0.7 keyword match score.
Pre-check: verify SHAKA is not already running (signal file check).

## Context Transfer
| Field | Type | Required | Purpose |
|-------|------|----------|---------|
| query | string | YES | Research question in natural language |
| domain | string | YES | Knowledge domain (e-commerce, tech, market) |
| depth | enum: shallow, medium, deep | YES | Research thoroughness level |
| deadline | datetime | NO | When results are needed |
| output_format | enum: kc, report, bullets | YES | Shape of deliverable |
| seeds | list[string] | NO | Seed keywords to guide research |

## Return Contract
```yaml
findings: list[string]    # Key findings, min 3 items
sources: list[url]        # Verified source URLs
confidence: float         # 0.0-1.0 research confidence
summary: string           # 2-3 sentence executive summary
signal_file: path         # Path to completion signal
```
Timeout: 30 minutes. Retry: 1x with simplified query. Escalation: return partial results.
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p02_handoff_ pattern (H02 pass)
- kind: handoff_protocol (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Trigger, Context Transfer, Return Contract (H07 pass)
- Parameters table with value and rationale (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "handoff_protocol" (S02 pass)
## Anti-Example
INPUT: "Create handoff for task delegation"
BAD OUTPUT:
```yaml
id: task-handoff
kind: handoff
quality: 9.0
tags: [handoff]
```
FAILURES:
1. id has hyphens and no p02_handoff_ prefix -> H02 FAIL
2. kind: 'handoff' not 'handoff_protocol' -> H04 FAIL
3. Missing fields: trigger, context_passed, return_contract -> H06 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. No ## Trigger section in body -> H07 FAIL
6. No context transfer table -> S03 FAIL
