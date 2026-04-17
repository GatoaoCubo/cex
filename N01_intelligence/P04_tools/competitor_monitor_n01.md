---
id: competitor_monitor_n01
kind: daemon
pillar: P04
nucleus: n01
title: "N01 Competitor Monitor Daemon"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: null
tags: [daemon, competitor_monitor, continuous_intelligence, n01, alerts, change_detection]
tldr: "Background daemon for continuous competitor monitoring: pricing changes, product updates, hiring signals, and blog posts. Runs on configurable schedule, writes signals to .cex/runtime/signals/ on change detection."
density_score: 0.88
---

<!-- 8F: F1 constrain=P04/daemon F2 become=daemon-builder F3 inject=search_strategy_n01+browser_tool_n01+api_reference_research_apis+research_pipeline_n01 F4 reason=Analytical Envy is chronic -- not a one-shot -- continuous monitoring closes information gaps before they cost N01 alpha F5 call=cex_compile F6 produce=competitor_monitor_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P04_tools/ -->

## Purpose

Research is not a one-shot event. Competitive landscapes shift daily.
N01 Analytical Envy means monitoring continuously, not querying on demand.

This daemon runs in the background, detecting changes across tracked competitors
and signaling N01 when delta > threshold (new info worth acting on).

## Monitored Signal Categories

| Signal Type | Source | Change Threshold | Priority |
|-------------|--------|-----------------|---------|
| Pricing change | competitor pricing pages | any text change in price fields | P1 |
| New product/feature | product changelog, blog | new post or release note | P1 |
| Hiring surge | LinkedIn job postings | > 5 new roles in 7 days | P1 |
| Funding event | Crunchbase, TechCrunch | new announcement | P1 |
| Partnership / acquisition | press releases, news | keyword match | P2 |
| Leadership change | LinkedIn, press | CxO role change | P2 |
| Pricing page removal | HTTP 404 or redirect | URL change | P2 |
| Review spike (G2/Capterra) | review platform | > 10 new reviews/week | P3 |

## Configuration

```yaml
# competitor_monitor_config.yaml
schedule: "0 8 * * *"  # daily at 08:00
competitors:
  - slug: openai
    pricing_url: "https://openai.com/pricing"
    blog_url: "https://openai.com/blog"
    jobs_query: "OpenAI engineer"
  - slug: anthropic
    pricing_url: "https://www.anthropic.com/pricing"
    blog_url: "https://www.anthropic.com/news"
    jobs_query: "Anthropic engineer"
change_threshold_chars: 50  # min chars changed to trigger alert
signal_output: ".cex/runtime/signals/"
```

## Execution Flow

```
on_schedule():
  for competitor in config.competitors:
    for signal in [pricing, blog, jobs, news]:
      current = fetch(signal.url)
      previous = load_snapshot(competitor, signal.type)
      delta = diff(current, previous)
      if abs(delta) > threshold:
        write_signal(competitor, signal.type, delta)
        save_snapshot(competitor, signal.type, current)
        notify(competitor, signal.type, delta)
```

## Signal Format (output)

Written to `.cex/runtime/signals/monitor_{competitor}_{type}_{timestamp}.json`:

| Field | Type | Description |
|-------|------|-------------|
| `nucleus` | string | `n01` |
| `signal_type` | string | `competitor_change` |
| `competitor` | string | slug |
| `change_type` | string | pricing / feature / hiring / news |
| `delta_summary` | string | what changed (50-200 chars) |
| `confidence` | float | 0-1, change detection confidence |
| `url` | string | source URL |
| `detected_at` | ISO8601 | detection timestamp |
| `priority` | P1/P2/P3 | from signal category table |

## Snapshot Storage

| Location | Format | Retention |
|----------|--------|-----------|
| `.cex/cache/monitor_snapshots/` | {competitor}_{signal}_{date}.json | 30 days |
| N01 compiled outputs | yearly summary | permanent |

## Alert Routing

| Priority | Alert Method | Latency |
|----------|-------------|---------|
| P1 | `.cex/runtime/signals/` write + N07 notification | < 1 min |
| P2 | `.cex/runtime/signals/` write | next N07 check |
| P3 | log only, weekly digest | weekly |

## Performance Targets

| Metric | Target |
|--------|--------|
| Full scan time (10 competitors) | < 5 min |
| False positive rate | < 10% |
| Detection latency (P1 signals) | < 24 hours |
| Uptime | 99.5% (daemon restart on crash) |

## Comparison vs. Alternatives

| Approach | Coverage | Latency | Cost | N01 Fit |
|----------|---------|---------|------|---------|
| Manual monitoring | low | days | high time cost | no scale |
| Google Alerts | medium | hours | free | no structured output |
| This daemon | high | < 24h | compute only | optimal for N01 |
| Commercial CI tools (Crayon, Klue) | very high | hours | $$$  | use as benchmark |
