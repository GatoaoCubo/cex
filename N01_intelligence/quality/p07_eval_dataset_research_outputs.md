---
id: p07_eval_research_outputs
kind: eval_dataset
pillar: P07
title: "Eval Dataset -- N01 Research Output Validation"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n01_intelligence
agent_group: n01-research-analyst
domain: research-quality-evaluation
quality: 9.1
tags: [eval, dataset, research, quality, n01, validation, test-cases]
tldr: "20 test cases for validating N01 research output quality -- covers all 6 output types with expected sources, structure, density, and correctness criteria."
density_score: 0.93
---

## Purpose

This eval dataset provides structured test cases for validating N01 research outputs. Each test case defines an input query, expected output type, minimum quality criteria, and specific assertions that must hold. Without this dataset, research quality assessment is subjective and inconsistent.

## Dataset Overview

| Property | Value |
|----------|-------|
| **Total cases** | 20 |
| **Output types covered** | 6 (competitive_grid, swot, market_snapshot, trend_report, benchmark_report, executive_summary) |
| **Cases per type** | 3-4 |
| **Difficulty levels** | easy (7), medium (8), hard (5) |
| **Evaluation method** | Automated (schema) + manual (correctness) |

## Test Cases

### competitive_grid (4 cases)

| # | Query | Difficulty | Min Sources | Key Assertion |
|---|-------|-----------|-------------|---------------|
| CG-01 | "Compare top 3 LLM agent frameworks: LangChain, CrewAI, AutoGen" | easy | 3 | Grid has >= 5 comparison dimensions (features, pricing, docs, community, maturity) |
| CG-02 | "Pet food subscription services in Brazil -- competitive grid" | medium | 4 | Includes pricing tiers, delivery frequency, geographic coverage |
| CG-03 | "Coding assistants: Cursor vs Windsurf vs GitHub Copilot" | easy | 3 | Feature parity table with at least 8 features compared |
| CG-04 | "Vector database comparison for RAG: Pinecone vs Weaviate vs Chroma vs Qdrant" | hard | 5 | Performance benchmarks cited, not just feature lists |

### swot (3 cases)

| # | Query | Difficulty | Min Sources | Key Assertion |
|---|-------|-----------|-------------|---------------|
| SW-01 | "SWOT analysis for a pet tech startup in Latin America" | medium | 4 | Each quadrant has >= 3 items with evidence |
| SW-02 | "SWOT of CEX knowledge system vs manual prompt engineering" | hard | 3 | Strengths cite specific CEX capabilities; Threats cite real alternatives |
| SW-03 | "SWOT for AI-powered content creation tools market 2026" | medium | 4 | Opportunities and Threats grounded in market data, not speculation |

### market_snapshot (4 cases)

| # | Query | Difficulty | Min Sources | Key Assertion |
|---|-------|-----------|-------------|---------------|
| MS-01 | "Brazilian pet care market size and growth 2024-2028" | medium | 5 | TAM/SAM/SOM with cited sources; growth rate with CAGR |
| MS-02 | "Global LLM market snapshot Q1 2026" | hard | 6 | Revenue figures for top 5 providers with sources |
| MS-03 | "D2C pet food market Latin America" | medium | 4 | Market segmentation by channel, geography, product type |
| MS-04 | "Creator economy tools market 2026" | easy | 3 | Top 10 players by category with estimated revenue ranges |

### trend_report (3 cases)

| # | Query | Difficulty | Min Sources | Key Assertion |
|---|-------|-----------|-------------|---------------|
| TR-01 | "AI agent orchestration trends 2026" | medium | 4 | Each trend has momentum score (rising/stable/declining) and confidence level |
| TR-02 | "Pet humanization trends in Brazil 2025-2026" | easy | 3 | Consumer behavior data cited, not just industry opinion |
| TR-03 | "MCP (Model Context Protocol) adoption trends" | hard | 5 | Adoption metrics: server count, integration count, community growth |

### benchmark_report (3 cases)

| # | Query | Difficulty | Min Sources | Key Assertion |
|---|-------|-----------|-------------|---------------|
| BR-01 | "LLM response quality benchmark: GPT-4o vs Claude 3.5 vs Gemini 2.5" | medium | 4 | Quantitative scores on shared eval dataset, not subjective ratings |
| BR-02 | "RAG pipeline performance: chunking strategies benchmark" | hard | 5 | Latency + accuracy metrics for 3+ chunking approaches |
| BR-03 | "Content generation speed benchmark: human vs AI-assisted" | easy | 3 | Time measurements with sample sizes stated |

### executive_summary (3 cases)

| # | Query | Difficulty | Min Sources | Key Assertion |
|---|-------|-----------|-------------|---------------|
| ES-01 | "Executive summary: CEX system capabilities for investor pitch" | easy | 2 | 1-page format, key metrics highlighted, competitive positioning |
| ES-02 | "Executive summary: pet tech market opportunity for board meeting" | medium | 4 | TAM/SAM cited, competitor count, regulatory landscape |
| ES-03 | "Executive summary: AI tool stack consolidation recommendation" | medium | 3 | Clear recommendation with cost-benefit, risk assessment, timeline |

## Scoring Criteria (per test case)

| Criterion | Weight | Pass Threshold |
|-----------|--------|---------------|
| **Source count** | 20% | >= Min Sources specified |
| **Source authority** | 15% | >= 50% from T1/T2 domains |
| **Source freshness** | 10% | >= 80% within freshness window |
| **Structure compliance** | 20% | Matches expected output template |
| **Density score** | 15% | >= 0.85 |
| **Key assertion** | 20% | Specific assertion passes |
| **TOTAL** | 100% | >= 75% weighted average to pass |

## Execution Protocol

```bash
# Run full eval suite
for i in $(seq 1 20); do
  python _tools/cex_8f_runner.py --execute --nucleus N01 \
    --kind research_brief --query "$(cat eval_queries/$i.txt)" \
    --output "eval_results/case_$i.md"
done

# Score results
python _tools/cex_score.py --eval-dataset p07_eval_research_outputs \
  --results-dir eval_results/ \
  --rubric N01_intelligence/quality/scoring_rubric_intelligence.md

# Generate pass/fail report
python -c "
import yaml
from pathlib import Path
results = list(Path('eval_results').glob('case_*.yaml'))
passed = sum(1 for r in results if yaml.safe_load(r.read_text()).get('pass', False))
print(f'Pass rate: {passed}/{len(results)} ({passed/len(results)*100:.0f}%)')
"
```

## Comparison to Alternative Eval Approaches

| Approach | Coverage | Effort | Objectivity |
|----------|----------|--------|-------------|
| **This dataset (structured)** | 6 output types, 20 cases | Medium (one-time setup) | High (automated + rubric) |
| **Ad-hoc review** | Random | Low | Low (subjective) |
| **LLM-as-judge** | Scalable | Low | Medium (model bias) |
| **Human expert panel** | Deep | Very high | High (but slow) |

**Decision**: Structured dataset + automated scoring is the best trade-off for N01. Supplement with LLM-as-judge for edge cases. Reserve human panel for quarterly quality audits.
