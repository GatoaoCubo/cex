---
id: p01_kc_bugloop
kind: knowledge_card
type: kind
pillar: P11
title: "Bugloop — Deep Knowledge for bugloop"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: bugloop
quality: 9.1
tags: [bugloop, P11, GOVERN, kind-kc]
tldr: "Automated detect-fix-verify cycle with confidence-calibrated fix strategies and escalation on max attempts"
when_to_use: "Building, reviewing, or reasoning about bugloop artifacts"
keywords: [auto-repair, MTTR, retry]
feeds_kinds: [bugloop]
density_score: null
related:
  - bld_knowledge_card_bugloop
  - p10_lr_bugloop_builder
  - p11_qg_bugloop
  - p03_sp_bugloop_builder
  - bugloop-builder
  - bld_instruction_bugloop
  - bld_architecture_bugloop
  - bld_examples_bugloop
  - bld_collaboration_bugloop
  - p01_kc_feedback_loops
---

# Bugloop

## Spec
```yaml
kind: bugloop
pillar: P11
llm_function: GOVERN
max_bytes: 4096
naming: p11_bl_{{scope}}.md + .yaml
core: false
```

## What It Is
A bugloop is a declarative specification for an automated detect→fix→verify→commit/escalate cycle targeting a known failure pattern. It encodes the detection signal, fix strategy, confidence threshold, verification suite, and escalation path. It is NOT unit_eval (P07 — manual test that measures quality passively) nor optimizer (P11 — metric-driven continuous improvement; bugloop targets discrete failures, not ongoing metrics).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableLambda` retry chain + `@tool` error handler | Custom retry wrapper around agent tool calls |
| LlamaIndex | `Workflow` with error event handlers | `@step` error events trigger fix sub-workflows |
| CrewAI | `Task(guardrail=...)` + `max_iter` retry | Task-level guardrail + retry mimics detect-fix-verify |
| DSPy | `dspy.Assert` / `dspy.Suggest` with retry | Assert triggers automatic re-prompting on failure |
| Haystack | `ConditionalRouter` + error branch pipeline | Route failed components to fix pipeline |
| OpenAI | Custom function retry with error feedback | Pass error message back to LLM for self-correction |
| Anthropic | Tool use error loop + system correction | Tool result error → re-invoke with correction instructions |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| confidence | float [0,1] | 0.75 | Higher = less conservative fixes; calibrate to domain risk |
| max_attempts | int | 3 | More attempts = higher recovery rate; longer MTTR |
| fix_strategy | enum | patch_and_retry | patch_and_retry/rollback_first/isolate_then_fix |
| escalation_target | string | human | human/queue/agent_group — depends on urgency |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Confidence-calibrated strategy | Domain has variable risk | style errors: 0.95 patch; data corruption: 0.30 escalate immediately |
| Rollback-first | Unknown root cause, reversible changes | `fix_strategy: rollback_first` → restore known-good state |
| Isolate-then-fix | Modular failure with clear boundary | Disable failing component, fix in isolation, re-integrate |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Confidence 0.95 for non-deterministic failures | Silent bad fixes applied; system worse than before | Cap confidence at 0.55 for runtime/non-deterministic failures |
| No max_attempts limit | Infinite loop on unfixable bug | Always set max_attempts; default 3 |
| Empty verify.assertions | Verification passes trivially; broken fix ships | Require at least 1 test assertion; gate commit on test pass |

## Integration Graph
```
[quality_gate] --> [bugloop] --> [learning_record]
[guardrail] --------^     |
                     [signal: complete/escalate]
```

## Decision Tree
- IF confidence >= 0.75 AND attempts < max_attempts THEN apply fix + verify
- IF verify passes THEN commit + write learning_record
- IF verify fails AND attempts < max_attempts THEN retry with next strategy
- IF attempts == max_attempts THEN escalate to target
- DEFAULT: Always set escalation_target; never loop silently

## Quality Criteria
- GOOD: Has scope, detect signal, fix_strategy, confidence, max_attempts, verify assertions, escalation_target
- GREAT: Confidence calibrated to domain risk table; rollback policy explicit; verify has >= 2 assertions
- FAIL: No max_attempts; confidence not calibrated; empty assertions; no escalation path defined

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_bugloop]] | sibling | 0.57 |
| [[p10_lr_bugloop_builder]] | upstream | 0.44 |
| [[p11_qg_bugloop]] | related | 0.43 |
| [[p03_sp_bugloop_builder]] | related | 0.43 |
| [[bugloop-builder]] | related | 0.43 |
| [[bld_instruction_bugloop]] | upstream | 0.41 |
| [[bld_architecture_bugloop]] | upstream | 0.39 |
| [[bld_examples_bugloop]] | upstream | 0.39 |
| [[bld_collaboration_bugloop]] | downstream | 0.34 |
| [[p01_kc_feedback_loops]] | sibling | 0.34 |
