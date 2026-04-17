---
id: eval_framework_n01
kind: eval_framework
pillar: P07
nucleus: n01
title: "N01 Research Quality Evaluation Framework"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.1
tags: [eval_framework, research_quality, n01, analytical_envy, benchmarking, quality_assessment]
tldr: "5-dimension evaluation framework for N01 research outputs: source quality, analytical depth, comparative coverage, claim confidence, and actionability. Produces weighted score 0-10 with remediation map."
density_score: 0.93
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P07/eval_framework F2 become=eval-framework-builder F3 inject=quality_gate_intelligence+bias_audit_n01+scoring_rubric_intelligence+benchmark_research_quality F4 reason=Analytical Envy demands we MEASURE research quality, not assume it -- what gets measured gets improved F5 call=cex_compile F6 produce=eval_framework_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P07_evals/ -->

## Purpose

N01 Analytical Envy is valueless without a measurement system.
This framework operationalizes "research quality" into 5 scored dimensions,
each grounded in information retrieval (IR) and intelligence tradecraft standards.

Used in:
- F7 GOVERN (mandatory for all N01 outputs)
- self_improvement_loop_n01.md (quality gap identification)
- llm_judge_n01.md (judge prompt grounding)

## Evaluation Architecture

| Component | Role |
|-----------|------|
| D1 Source Quality | evaluates WHERE the evidence came from |
| D2 Analytical Depth | evaluates HOW DEEPLY the evidence was analyzed |
| D3 Comparative Coverage | evaluates WHAT ELSE was considered |
| D4 Claim Confidence | evaluates HOW CERTAIN the findings are |
| D5 Actionability | evaluates WHAT CAN BE DONE with this research |

## D1: Source Quality (weight 25%)

| Score | Criteria |
|-------|----------|
| 10 | Primary sources only: filings, official docs, direct interviews |
| 9 | Mix: primary (> 50%) + peer-reviewed |
| 7-8 | Peer-reviewed papers + Tier-1 news + official reports |
| 5-6 | Tier-2 news + industry blogs + > 1 analyst report |
| 3-4 | Blogs, forums, social media cited as evidence |
| 1-2 | Single source, no corroboration |

Sub-checks:
- Source count >= 5: +1
- All sources < 90 days: +0.5
- No paywalled (unverified) sources: +0.5
- Geographic diversity (non-US sources when relevant): +0.5

## D2: Analytical Depth (weight 25%)

| Score | Criteria |
|-------|----------|
| 10 | First-principles reasoning, novel synthesis, identifies non-obvious pattern |
| 9 | Multi-framework analysis, structural decomposition |
| 7-8 | SWOT or equivalent, identifies root causes, not just symptoms |
| 5-6 | Summary with basic interpretation |
| 3-4 | Mostly summarizes sources, little original analysis |
| 1-2 | Verbatim extraction, zero synthesis |

Sub-checks:
- Causal chain present (X causes Y because Z): +1
- Historical pattern identified: +0.5
- System dynamics modeled: +1
- Counterfactual explored ("what if X didn't happen"): +0.5

## D3: Comparative Coverage (weight 25%)

| Score | Criteria |
|-------|----------|
| 10 | All major alternatives compared, quantified deltas |
| 9 | Primary competitors compared with quantified metrics |
| 7-8 | Vs. 2+ alternatives, some quantification |
| 5-6 | Vs. 1 alternative, qualitative only |
| 3-4 | Single-entity focus, no comparison |
| 1-2 | No comparative context at all |

This dimension is the Analytical Envy dimension. Score < 7 = sin lens violation.

Sub-checks:
- Market share / size context: +1
- Year-over-year trend comparison: +0.5
- Price benchmarking vs. 2+ competitors: +0.5
- NDCG-style ranking of alternatives: +0.5

## D4: Claim Confidence (weight 15%)

| Score | Criteria |
|-------|----------|
| 10 | Every claim has explicit confidence score + evidence grading |
| 9 | Key claims have confidence, qualifiers present |
| 7-8 | Major claims cited, some uncertainty acknowledged |
| 5-6 | Claims made without confidence, sources listed |
| 3-4 | Hedged ("might", "possibly") without evidence |
| 1-2 | Overconfident claims, no uncertainty acknowledgment |

Sub-checks:
- Confidence score on each key finding: +1 per finding (max +3)
- Uncertainty explicitly stated: +1
- Limitation section present: +1

## D5: Actionability (weight 10%)

| Score | Criteria |
|-------|----------|
| 10 | Specific next actions with owners, timelines, success metrics |
| 9 | 3+ concrete recommendations with rationale |
| 7-8 | Recommendations present, somewhat vague |
| 5-6 | Implications noted, no clear actions |
| 3-4 | Findings presented, "reader to decide" |
| 1-2 | Pure description, zero prescription |

## Overall Score Calculation

```
score = (D1 * 0.25) + (D2 * 0.25) + (D3 * 0.25) + (D4 * 0.15) + (D5 * 0.10)
```

| Overall Score | Verdict | Action |
|---------------|---------|--------|
| >= 9.0 | Elite | publish, use as template |
| 8.0 - 8.9 | Publish | minor polish recommended |
| 7.0 - 7.9 | Conditional | specific gaps flagged, fix before use |
| 5.0 - 6.9 | Revise | return to F3/F6 with specific remediation |
| < 5.0 | Reject | restart pipeline |

## Benchmarking vs. Other Evaluation Systems

| System | Dimensions | Automation | Industry Standard | N01 Fit |
|--------|-----------|------------|------------------|---------|
| RAGAS (RAG eval) | faithfulness, relevance, context | high | yes | partial (no comparative D) |
| G-Eval (GPT judge) | coherence, fluency, consistency | high | yes | partial (no actionability) |
| This framework | D1-D5 (N01 domain) | 80% | no (custom) | optimal |
| TREC eval (IR) | precision, recall, NDCG | high | yes | partial (retrieval only) |

N01 advantage: D3 Comparative Coverage is unique to Analytical Envy lens.

## Related Artifacts

| Artifact | Relationship |
|----------|-------------|
| `P07_evals/llm_judge_n01.md` | uses this framework as judge grounding |
| `P11_feedback/quality_gate_intelligence.md` | complementary hard gates |
| `P11_feedback/bias_audit_n01.md` | bias sub-check feeds D1 and D3 |
| `P11_feedback/self_improvement_loop_n01.md` | uses scores for improvement targeting |
