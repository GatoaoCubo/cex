---
id: p01_kc_confidence_scoring
kind: knowledge_card
type: domain
pillar: P01
title: "Confidence Scoring"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n01_research
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, confidence, scoring, threshold, certainty, decision]
tldr: "Assign confidence to LLM outputs on 0-1 scale. High 0.90+: act autonomously. Medium 0.70-0.89: act + flag. Low <0.70: ask user."
when_to_use: "Before any autonomous action, before publishing, before architectural decisions, and at merge gates in query decomposition."
keywords: [confidence, scoring, threshold, certainty, calibration, decision-gate]
density_score: 0.95
related:
  - p11_qg_intelligence
  - p01_kc_source_triangulation
  - p03_sp_reasoning_trace_builder
  - bld_knowledge_card_reasoning_trace
  - p11_qg_reasoning_trace
  - bld_examples_reasoning_trace
  - bld_memory_reasoning_trace
  - bld_collaboration_reasoning_trace
  - bld_schema_reasoning_trace
  - bld_knowledge_card_hitl_config
---

# Confidence Scoring

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | Quantify certainty before acting; gate actions by threshold |
| Trigger | Every autonomous decision, every publish gate, every merge step |
| Benefit | Prevents confident-but-wrong outputs from propagating |
| Risk if skipped | Silent hallucinations, uncalibrated autonomy |

## Threshold Actions

| Score | Label | Action | Example |
|-------|-------|--------|---------|
| >= 0.95 | Very High | Act + no flag | Well-documented API call |
| 0.90–0.94 | High | Act autonomously | Schema-validated output |
| 0.70–0.89 | Medium | Act + flag for review | Inferred pattern, partial evidence |
| 0.50–0.69 | Low | Draft only, ask user | Ambiguous requirement |
| < 0.50 | Very Low | Halt, escalate immediately | Contradictory sources, no evidence |

## Scoring Dimensions

| Dimension | Weight | How to Assess |
|-----------|--------|--------------|
| Source quality | 0.30 | Tier 1-5 per source triangulation taxonomy |
| Evidence count | 0.25 | Number of independent confirmations |
| Recency | 0.15 | How recent is the information (decay over time) |
| Consistency | 0.20 | Do sources agree or contradict? |
| Domain familiarity | 0.10 | Has the agent handled this domain before? |

## Calibration Protocol

| Step | Action |
|------|--------|
| 1 | Score output on each dimension (0.0–1.0) |
| 2 | Apply weights → weighted sum |
| 3 | Check against threshold table |
| 4 | Log score + reasoning in artifact frontmatter or signal |
| 5 | Act according to threshold action |

## Confidence in Practice

| Scenario | Expected Score | Why |
|----------|---------------|-----|
| Copy API endpoint from official docs | 0.98 | Tier 1 source, exact match |
| Infer user preference from 2 past interactions | 0.72 | Limited evidence, reasonable pattern |
| Generate pricing recommendation without market data | 0.35 | No evidence, high-stakes domain |
| Summarize a document the agent just read | 0.90 | Source in context, verifiable |
| Predict future behavior from historical trend | 0.60 | Extrapolation, inherently uncertain |

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| Binary confidence (sure/unsure) | Loses nuance, no gradation for medium-certainty |
| Overconfidence | LLMs default to confident tone even when wrong |
| Score inflation | Always scoring 0.85+ to avoid escalation overhead |
| No logging | Confidence assigned but not recorded → no calibration feedback |
| Ignoring domain risk | 0.80 is fine for draft copy, dangerous for financial data |

## CEX Integration

| Concept | CEX artifact / tool |
|---------|-------------------|
| Score storage | `quality` field in frontmatter |
| Threshold config | `P09_config/` runtime rules |
| Calibration data | `.cex/experiments/results.tsv` |
| Escalation | `signal_writer.py` → `needs_user` signal |
| Memory of past scores | `P10_memory/` learning records |

## Linked Artifacts

- `p01_kc_source_triangulation` — feeds evidence count + source quality dimensions
- `p01_kc_self_healing_skill` — confidence < 0.70 triggers heal-or-escalate
- `p01_kc_gap_detection` — low confidence signals a knowledge gap

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_intelligence]] | downstream | 0.30 |
| [[p01_kc_source_triangulation]] | sibling | 0.28 |
| [[p03_sp_reasoning_trace_builder]] | downstream | 0.27 |
| [[bld_knowledge_card_reasoning_trace]] | sibling | 0.26 |
| [[p11_qg_reasoning_trace]] | downstream | 0.25 |
| [[bld_examples_reasoning_trace]] | downstream | 0.25 |
| [[bld_memory_reasoning_trace]] | downstream | 0.25 |
| [[bld_collaboration_reasoning_trace]] | downstream | 0.23 |
| [[bld_schema_reasoning_trace]] | downstream | 0.22 |
| [[bld_knowledge_card_hitl_config]] | sibling | 0.21 |
