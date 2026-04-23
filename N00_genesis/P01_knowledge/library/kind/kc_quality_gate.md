---
id: p01_kc_quality_gate
kind: knowledge_card
type: kind
pillar: P11
title: "Quality Gate — Deep Knowledge for quality_gate"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: quality_gate
quality: 9.1
tags: [quality_gate, P11, GOVERN, kind-kc]
tldr: "Binary pass/fail barrier with numeric score threshold that controls artifact promotion and pipeline progression"
when_to_use: "Building, reviewing, or reasoning about quality_gate artifacts"
keywords: [threshold, pass-fail, promotion]
feeds_kinds: [quality_gate]
density_score: null
related:
  - bld_architecture_quality_gate
  - quality-gate-builder
  - p01_kc_reward_signal
  - bld_collaboration_quality_gate
  - p01_kc_artifact_quality_evaluation_methods
  - p01_kc_quality_gates
  - p03_sp_quality_gate_builder
  - p01_kc_validator
  - bld_examples_runtime_rule
  - bld_memory_quality_gate
---

# Quality Gate

## Spec
```yaml
kind: quality_gate
pillar: P11
llm_function: GOVERN
max_bytes: 4096
naming: p11_qg_{{gate}}.yaml
core: true
```

## What It Is
A quality gate is a declarative threshold specification that produces a binary pass/fail verdict with numeric score. It blocks artifact promotion, pipeline progression, or deployment unless the score meets the minimum. It is NOT validator (P06 — technical pass/fail on schema/format without score) nor scoring_rubric (P07 — defines evaluation criteria; quality_gate applies criteria and enforces the threshold).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableLambda` score check + conditional branch | Post-LLM score evaluation gating next chain step |
| LlamaIndex | `ResponseEvaluator` + threshold filter | Faithfulness/relevancy evaluators return score; gate on threshold |
| CrewAI | `Task(guardrail=score_check)` | Guardrail returning (False, "score below threshold") blocks task completion |
| DSPy | `dspy.Assert(metric(pred) >= threshold)` | Assert with metric function as condition; blocks forward() on fail |
| Haystack | `ConditionalRouter` with score branch | Route to retry/reject if score component output < threshold |
| OpenAI | Evals API pass/fail criteria | `pass_threshold` in eval config; graders return pass/fail |
| Anthropic | Custom score check in tool use loop | Tool result score checked before next tool invocation |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| min_score | float | 7.0 | Higher = better quality pool; more rejections and retries |
| on_fail | enum | block | block/retry/escalate — block = hardest gate; retry = tolerant |
| scorer | string | required | LLM judge / rubric / heuristic — defines how score is calculated |
| max_retries | int | 2 | More retries = higher final quality; more latency/cost |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Tiered gates | Different thresholds for different pools | experimental: 7.0, pool: 8.0, golden: 9.5 |
| Retry-with-feedback | Improvable failures (not structural) | on_fail: retry; pass error message to LLM for self-correction |
| Async gate | High-latency scorer (LLM judge) | Gate runs asynchronously; artifact held in pending state |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Gate without scorer definition | Gate passes everything; meaningless threshold | Always define scorer; must be reproducible |
| min_score: 10.0 | Nothing passes; pipeline stalls | Use 9.5 as maximum for golden tier |
| Blocking gate with no retry | Single failure permanently blocks artifact | Define max_retries >= 1; or on_fail: escalate for human review |

## Integration Graph
```
[scoring_rubric] --> [quality_gate] --> [pool / lifecycle_rule]
[reward_signal] -----^          |
                           [bugloop / retry]
```

## Decision Tree
- IF score >= 9.5 THEN pass as golden
- IF score 8.0–9.4 THEN pass as pool artifact
- IF score 7.0–7.9 THEN pass as experimental; flag for improvement
- IF score < 7.0 AND retries remaining THEN retry with scorer feedback
- IF score < 7.0 AND max_retries exhausted THEN block + escalate
- DEFAULT: min_score 7.0 for output gates; 8.0 for pool promotion gates

## Quality Criteria
- GOOD: Has gate name, min_score, scorer, on_fail, max_retries; YAML parseable
- GREAT: Tiered thresholds; scorer is reproducible; feedback passed to retry; async support for slow scorers
- FAIL: No scorer defined; min_score = 10.0 or 0.0; no retry or escalation path; gate never triggered

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_quality_gate]] | upstream | 0.30 |
| [[quality-gate-builder]] | related | 0.30 |
| [[p01_kc_reward_signal]] | sibling | 0.29 |
| [[bld_collaboration_quality_gate]] | related | 0.28 |
| [[p01_kc_artifact_quality_evaluation_methods]] | sibling | 0.28 |
| [[p01_kc_quality_gates]] | sibling | 0.28 |
| [[p03_sp_quality_gate_builder]] | upstream | 0.27 |
| [[p01_kc_validator]] | sibling | 0.26 |
| [[bld_examples_runtime_rule]] | upstream | 0.25 |
| [[bld_memory_quality_gate]] | upstream | 0.25 |
