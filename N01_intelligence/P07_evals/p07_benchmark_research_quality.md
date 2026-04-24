---
id: p07_bench_research_quality
kind: benchmark
8f: F7_govern
pillar: P07
title: "Benchmark -- N01 Research Output Quality"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n01_intelligence
agent_group: n01-research-analyst
domain: research-quality-measurement
target_system: N01 Intelligence research pipeline
quality: 9.1
tags: [benchmark, research, quality, n01, metrics, evaluation]
tldr: "Quantitative benchmark for N01 research quality -- measures source density, triangulation rate, freshness compliance, output density, and pipeline throughput across research deliverables."
density_score: 0.94
related:
  - bld_config_prompt_optimizer
  - p10_lr_research_sessions
  - bld_instruction_benchmark
  - p07_eval_research_outputs
  - p12_wf_intelligence
  - bld_memory_rag_source
  - bld_knowledge_card_benchmark
  - p10_out_source_dossier
---

## Setup

### Environment

| Component | Requirement |
|-----------|-------------|
| Python | >= 3.11 |
| CEX SDK | `cex_score.py`, `cex_compile.py`, `cex_retriever.py` operational |
| MCP servers | brave-search, firecrawl, markitdown, fetch accessible |
| Corpus | N01_intelligence/P05_output/ contains >= 10 research outputs |
| Scoring rubric | `scoring_rubric_intelligence.md` loaded |
| Source quality contract | `source_quality_contract.md` loaded |

### Fixtures

- Sample research queries: 20 predefined queries covering all 6 output types (competitive_grid, swot, market_snapshot, trend_report, benchmark_report, executive_summary)
- Expected source counts per query type (minimum triangulation targets)
- Known-good reference outputs for quality floor comparison

## Methodology

| Parameter | Value |
|-----------|-------|
| **Iterations** | 10 (run each query type at least 10 times) |
| **Warmup runs** | 1 (first run excluded from statistics) |
| **Percentiles** | p50, p95, p99 |
| **Significance threshold** | p < 0.05 (Mann-Whitney U test vs baseline) |
| **Measurement protocol** | Automated scoring via `cex_score.py --apply` + manual spot-check on 20% sample |

## Metrics

| Metric | Unit | Baseline | Target | Direction |
|--------|------|----------|--------|-----------|
| **Source density** | sources/claim | 1.5 | 3.0 | higher_is_better |
| **Triangulation rate** | % claims with 3+ sources | 45% | 80% | higher_is_better |
| **Freshness compliance** | % sources within freshness window | 70% | 90% | higher_is_better |
| **Output density score** | density (0.0-1.0) | 0.78 | 0.90 | higher_is_better |
| **Quality score (peer-reviewed)** | quality (0.0-10.0) | 7.8 | 9.0 | higher_is_better |
| **Pipeline latency** | minutes per research brief | 45 | 30 | lower_is_better |
| **Factual error rate** | errors per output | 1.2 | 0.1 | lower_is_better |
| **Schema compliance** | % outputs passing schema contracts | 85% | 100% | higher_is_better |
| **Context window utilization** | % of 1M tokens used per session | 60% | 40% | lower_is_better |

## Execution

```bash
# Run full benchmark suite
python _tools/cex_score.py --benchmark N01_intelligence/P05_output/ \
  --rubric N01_intelligence/quality/scoring_rubric_intelligence.md \
  --iterations 10 \
  --output N01_intelligence/P05_output/benchmark_results.yaml

# Run single metric: source density
python -c "
from pathlib import Path
import yaml
outputs = list(Path('N01_intelligence/output').glob('output_*.md'))
for f in outputs:
    content = f.read_text(encoding='utf-8')
    # Count source references (URLs, citations, 'Source:' tags)
    import re
    sources = len(re.findall(r'https?://|Source:|\\[\\d+\\]|\\(\\d{4}\\)', content))
    claims = len(re.findall(r'\\|.*\\|.*\\||^- |^\\d+\\.', content, re.MULTILINE))
    density = sources / max(claims, 1)
    print(f'{f.name}: {sources} sources / {claims} claims = {density:.2f} density')
"

# Run freshness audit
python -c "
from pathlib import Path
import re
from datetime import datetime, timedelta
cutoff = datetime.now() - timedelta(days=90)
outputs = list(Path('N01_intelligence/output').glob('output_*.md'))
for f in outputs:
    content = f.read_text(encoding='utf-8')
    dates = re.findall(r'20[2-3]\\d-[01]\\d-[0-3]\\d', content)
    fresh = sum(1 for d in dates if datetime.strptime(d, '%Y-%m-%d') >= cutoff)
    total = len(dates) if dates else 1
    print(f'{f.name}: {fresh}/{total} dates within 90d ({fresh/total*100:.0f}%)')
"
```

## Results Template

| Metric | p50 | p95 | p99 | vs Baseline | Pass? |
|--------|-----|-----|-----|-------------|-------|
| Source density | ___ | ___ | ___ | ___ | [ ] |
| Triangulation rate | ___ | ___ | ___ | ___ | [ ] |
| Freshness compliance | ___ | ___ | ___ | ___ | [ ] |
| Output density score | ___ | ___ | ___ | ___ | [ ] |
| Quality score | ___ | ___ | ___ | ___ | [ ] |
| Pipeline latency (min) | ___ | ___ | ___ | ___ | [ ] |
| Factual error rate | ___ | ___ | ___ | ___ | [ ] |
| Schema compliance | ___ | ___ | ___ | ___ | [ ] |
| Context utilization | ___ | ___ | ___ | ___ | [ ] |

## Comparison to N05 Benchmarks

| Dimension | N01 Research Benchmark | N05 Operations Benchmark |
|-----------|----------------------|-------------------------|
| What's measured | Research output quality | Infrastructure performance |
| Key metric | Source density (sources/claim) | Deploy latency (seconds) |
| Data source | Research outputs + schema contracts | Logs + health endpoints |
| Iteration count | 10 | 50 (infra needs more samples) |
| Human review | 20% spot-check | Automated only |
| Improvement signal | More sources = better research | Lower latency = better ops |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_prompt_optimizer]] | downstream | 0.41 |
| [[p10_lr_research_sessions]] | downstream | 0.19 |
| [[bld_instruction_benchmark]] | upstream | 0.18 |
| [[p07_eval_research_outputs]] | related | 0.16 |
| [[p12_wf_intelligence]] | downstream | 0.16 |
| [[bld_memory_rag_source]] | downstream | 0.16 |
| [[bld_knowledge_card_benchmark]] | upstream | 0.15 |
| [[p10_out_source_dossier]] | downstream | 0.15 |
