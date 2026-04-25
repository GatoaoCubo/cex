---
id: bld_feedback_inference_config
kind: builder_default
pillar: P11
title: "Inference Config Builder - Feedback ISO"
domain: inference_config
version: 1.0.0
quality: null
tags: [feedback, anti-patterns, P11, inference_config]
related:
  - bld_eval_inference_config
tldr: "Anti-patterns and correction protocol for inference config builders."
author: builder_agent
llm_function: GOVERN
density_score: 0.85
created: "2026-04-23"
updated: "2026-04-23"
---

# Feedback: Inference Config

## Anti-Patterns (NEVER do)

| Rule | Violation | Gate |
|------|-----------|------|
| No self-score | Never assign quality score | H05 |
| No VRAM overcommit | Always calculate memory budget | D3 |
| No missing framework | Always specify serving framework | H04 |
| No vague targets | Use numeric latency/throughput targets | D4 |
| No missing quantization | Always specify quantization level | H07 |

## Common Failure Modes

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| VRAM overcommit | OOM crash at runtime | Recalculate with overhead margin |
| No fallback | Service outage when primary fails | Add fallback serving path |
| Static batching | Low GPU utilization | Switch to continuous batching |
| Missing TTFT target | Interactive use feels slow | Add time-to-first-token target |

## Correction Protocol

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify failed gate | F7 |
| 2 | Return to F6 with fix | F6 |
| 3 | Re-run F7 | F7 |
| 4 | Max 2 retries | F8 |

## Quality Dimensions

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| D1 Structural completeness | 20%% | All required sections present |
| D2 Domain accuracy | 25% | Content matches inference config domain |
| D3 Density | 20%% | >= 0.85 information density |
| D4 Cross-references | 15%% | Valid links to related artifacts |
| D5 Actionability | 20%% | Builder can produce from this alone |

## Common Failures

| Failure | Frequency | Fix |
|---------|-----------|-----|
| Generic content | High | Add domain-specific examples |
| Missing boundary adherence | Medium | Check kinds_meta.json boundary |
| Low density score | Medium | Replace prose with tables |

## Properties

| Property | Value |
|----------|-------|
| Kind | `feedback` |
| Pillar | P11 |
| Domain | inference config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
