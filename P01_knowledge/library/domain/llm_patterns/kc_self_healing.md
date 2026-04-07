---
id: p01_kc_self_healing
kind: knowledge_card
type: domain
pillar: P01
title: "Self-Healing Patterns"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: llm_patterns
quality: 9.0
tags: [self-healing, error-recovery, retry, resilience]
tldr: "LLM detects own errors, retries with corrections, learns from failures. Generate → validate → fix → retry (max N)."
when_to_use: "Building autonomous agents that must recover from errors without human intervention"
keywords: [self-healing, auto-fix, retry, error-correction, validation-loop]
density_score: 0.92
updated: "2026-04-07"
---

# Self-Healing Patterns

## The Loop
```
GENERATE → VALIDATE → [PASS] → DONE
                    → [FAIL] → DIAGNOSE → FIX → RETRY (max 3)
                                                      → [FAIL] → ESCALATE
```

## Validation Types

| Type | Checks | Tool |
|------|--------|------|
| Schema | JSON/YAML structure | JSON Schema validator |
| Syntax | Code compiles/parses | Language parser |
| Semantic | Content makes sense | Second LLM pass |
| Constraint | Length, format, required fields | Regex, assertions |
| Test | Code passes tests | Test runner |

## Strategies

| Strategy | How | When |
|----------|-----|------|
| Retry with error | Feed error back, ask to fix | Schema/syntax |
| Retry with example | Show correct format | Format errors |
| Decompose | Smaller parts, fix each | Complex failures |
| Fallback | Simpler approach | Repeated failures |
| Escalate | Ask user | Max retries exhausted |

## CEX Integration
1. 8F F7→F6 loop = validation + retry (max 2)
2. `wf_auto_debug.md` = error diagnosis workflow
3. `cex_compile.py` = YAML validation
4. `cex_doctor.py` = builder integrity check
