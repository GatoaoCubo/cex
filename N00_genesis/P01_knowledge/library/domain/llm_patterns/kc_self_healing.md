---
id: p01_kc_self_healing
kind: knowledge_card
8f: F3_inject
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
related:
  - p01_kc_self_healing_skill
  - p12_wf_auto_debug
  - p01_kc_error_recovery
  - bld_knowledge_card_output_validator
  - p01_kc_llm_output_parsing_validation
  - p01_kc_feedback_loops
  - bld_collaboration_validation_schema
  - bld_examples_runtime_rule
  - p10_lr_bugloop_builder
  - p01_kc_bugloop
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_self_healing_skill]] | sibling | 0.36 |
| [[p12_wf_auto_debug]] | downstream | 0.30 |
| [[p01_kc_error_recovery]] | sibling | 0.29 |
| [[bld_knowledge_card_output_validator]] | sibling | 0.28 |
| [[p01_kc_llm_output_parsing_validation]] | sibling | 0.26 |
| [[p01_kc_feedback_loops]] | sibling | 0.26 |
| [[bld_collaboration_validation_schema]] | downstream | 0.25 |
| [[bld_examples_runtime_rule]] | downstream | 0.25 |
| [[p10_lr_bugloop_builder]] | downstream | 0.23 |
| [[p01_kc_bugloop]] | sibling | 0.23 |
