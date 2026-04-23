---
id: trend_detector_n01
kind: search_tool
pillar: P04
nucleus: n01
title: "N01 Market Trend Detection Tool"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.1
tags: [search_tool, trend_detection, market_signals, n01, analytical_envy, time_series]
tldr: "Trend detection tool for N01: detects rising / falling / plateauing signals across competitor metrics, hiring, search volume, and social velocity. Outputs ranked trend signals with statistical confidence."
density_score: 0.88
updated: "2026-04-17"
related:
  - p06_schema_trend_detection
  - p10_out_trend_report
  - p01_kc_trend_detection_time_series
  - p12_wf_weekly_fashion_content
  - p04_rp_weekly_market_intelligence_brief_output_template
  - p02_card_intelligence
  - bld_schema_experiment_tracker
  - p03_sp_n01_intelligence
  - p01_kc_competitive_intelligence_osint
  - n01_agent_intelligence
---

<!-- 8F: F1 constrain=P04/search_tool F2 become=search-tool-builder F3 inject=competitor_monitor_n01+search_strategy_n01+data_extractor_n01+api_reference_research_apis F4 reason=Analytical Envy demands seeing trends BEFORE competitors do -- trend detection is forward-looking intelligence, not backward-looking reporting F5 call=cex_compile F6 produce=trend_detector_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P04_tools/ -->

## Purpose

Trend detection separates intelligence from reporting.
N01 Analytical Envy: finding a trend AFTER everyone knows it = no competitive advantage.
This tool detects trends in their EARLY stage, before they become obvious.

## Trend Signal Categories

| Category | Data Source | Detection Method | Lead Time |
|----------|------------|-----------------|-----------|
| Hiring surge | LinkedIn job postings | rolling 30d avg vs. 90d baseline | 3-6 months |
| Search volume | Google Trends (unofficial) | week-over-week delta | 1-4 weeks |
| GitHub activity | GitHub API | star/fork/commit velocity | 1-3 months |
| Paper citation | Semantic Scholar | citation growth rate | 6-12 months |
| Funding pace | Crunchbase | deals per month, round size | 3-12 months |
| Social velocity | Twitter/X (keyword) | mention rate per week | 1-4 weeks |

## Trend Detection Algorithm

For each signal:

```
time_series = [v_t0, v_t1, ..., v_tn]  # values over time
baseline = mean(time_series[0:baseline_window])
recent = mean(time_series[-recent_window:])
trend_score = (recent - baseline) / baseline  # relative change

if trend_score > 0.30:
    direction = "RISING"
    confidence = min(1.0, trend_score * 2)
elif trend_score < -0.30:
    direction = "FALLING"
    confidence = min(1.0, abs(trend_score) * 2)
else:
    direction = "STABLE"
    confidence = 1.0 - abs(trend_score)
```

## Trend Output Schema

| Field | Type | Description |
|-------|------|-------------|
| `signal_id` | string | `{category}_{entity}_{date}` |
| `entity` | string | company, topic, or technology |
| `category` | string | hiring / search / github / etc. |
| `direction` | string | RISING / FALLING / STABLE |
| `trend_score` | float | relative change from baseline |
| `confidence` | float | 0-1 statistical confidence |
| `baseline_period` | string | e.g., "90d" |
| `recent_period` | string | e.g., "30d" |
| `data_points` | int | number of time-series points |
| `narrative` | string | 1-sentence human-readable summary |
| `detected_at` | ISO8601 | detection timestamp |

## Early Signal Detection

| Early Signal | Typical Lead Time | How Detected |
|-------------|------------------|-------------|
| Competitor pivot | 2-4 months before announcement | hiring for new skill domains |
| Market entry | 3-6 months before launch | domain registration + job postings |
| Pricing change | 2-4 weeks before implementation | pricing page A/B tests |
| Partnership | 1-2 months before announcement | employee LinkedIn connections cross-company |
| Funding close | 3-6 months | hiring surge + PR activity increase |

## Comparative Trend Analysis

N01 always compares trends across competitors:

```
for entity in [primary_target] + competitors:
    trend = detect_trend(entity, category)
    signals.append(trend)

ranked = sort(signals, by=trend_score, descending=True)
output_comparison_table(ranked)
```

Example output:

```
| Entity | Hiring Trend | Score | Direction | vs. Category |
|--------|-------------|-------|-----------|-------------|
| OpenAI | +82% | 0.82 | RISING | +45% above avg |
| Anthropic | +67% | 0.67 | RISING | +30% above avg |
| Google | +12% | 0.12 | STABLE | category avg |
| Mistral | -8% | -0.08 | STABLE | -21% below avg |
| Category avg | +30% | -- | -- | baseline |
```

## Integration

```
competitor_monitor_n01 (triggered by change event)
  -> trend_detector_n01 (time-series analysis)
    -> write trend signals to entity_memory_n01
    -> if significant trend: alert N07 via .cex/runtime/signals/
```

## Comparison vs. Alternatives

| Tool | Automation | Lead Time | Structured? | N01 Fit |
|------|-----------|-----------|-------------|---------|
| Google Trends | high | 1-4w | no | partial (no competitor compare) |
| Crayon / Klue (commercial) | high | varies | yes | use as benchmark |
| This tool | high | 1-12m by category | yes (typed) | optimal (integrated with N01) |
| Manual signal tracking | none | variable | no | impractical |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_schema_trend_detection]] | downstream | 0.40 |
| [[p10_out_trend_report]] | downstream | 0.27 |
| [[p01_kc_trend_detection_time_series]] | upstream | 0.26 |
| [[p12_wf_weekly_fashion_content]] | downstream | 0.24 |
| [[p04_rp_weekly_market_intelligence_brief_output_template]] | related | 0.19 |
| [[p02_card_intelligence]] | upstream | 0.17 |
| [[bld_schema_experiment_tracker]] | downstream | 0.17 |
| [[p03_sp_n01_intelligence]] | upstream | 0.17 |
| [[p01_kc_competitive_intelligence_osint]] | upstream | 0.17 |
| [[n01_agent_intelligence]] | upstream | 0.17 |
