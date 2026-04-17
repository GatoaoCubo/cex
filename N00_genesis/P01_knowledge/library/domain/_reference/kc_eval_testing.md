---
id: p01_kc_eval_testing
kind: knowledge_card
type: domain
pillar: P01
title: Evaluation Testing -- Benchmarks, Evals, Red Team, Regression
version: 1.0.0
created: '2026-03-29'
author: orchestrator
domain: evaluation
origin: manual
quality: 9.0
tags:
- eval
- benchmark
- testing
- red-team
- regression
- braintrust
tldr: 'LLM eval patterns: unit/smoke/E2E, benchmarks, red team adversarial, regression detection'
when_to_use: Setting up evaluation pipelines or regression monitoring
feeds_kinds:
- benchmark
- e2e_eval
- smoke_eval
- unit_eval
- red_team_eval
- regression_check
density_score: 0.85
updated: "2026-04-07"
---

## Quick Reference
| Framework | Eval Type | CEX Kind |
|-----------|-----------|----------|
| Braintrust Scorer | LLM judge | llm_judge |
| DeepEval | Unit eval | unit_eval, golden_test |
| Promptfoo | Regression | regression_check |
| RAGAS | RAG eval | e2e_eval, benchmark |
| Promptfoo redteam | Adversarial | red_team_eval |

## Key Concepts
- **Benchmark**: absolute measurement against fixed dataset
- **Unit Eval**: single input/output pair with assertion
- **E2E Eval**: full pipeline test input to final output
- **Smoke Eval**: quick sanity check (runs? valid JSON?)
- **Red Team Eval**: adversarial attacks (jailbreak, injection)
- **Regression Check**: current vs baseline (detect degradation)

## Patterns
| Trigger | Action |
|---------|--------|
| New model version | Run regression_check |
| Pre-production | Run smoke_eval + unit_eval |
| Security audit | Run red_team_eval |
| Quarterly review | Run full benchmark + e2e |

## Anti-Patterns
- Only testing happy path
- Regression without baseline
- LLM judge without calibration

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_eval_testing`
- **Tags**: 

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_eval_testing`
- **Tags**: 

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |
