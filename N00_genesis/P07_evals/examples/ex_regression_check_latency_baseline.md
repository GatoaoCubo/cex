---
id: p07_regcheck_latency_baseline
kind: regression_check
8f: F7_govern
pillar: P07
name: "Latency Regression Check"
description: "Regression check comparing API response latency against v2.1 baseline with p50/p95/p99 thresholds"
baseline_ref: "v2.1"
threshold: "+10%"
metrics: [p50, p95, p99]
alert_on: slack
version: 1.0.0
created: 2026-03-29
author: builder_agent
quality: 9.0
tags: [regression, latency, performance, baseline, monitoring]
related:
  - p07_regression_check
  - p07_benchmark_api_latency
  - p07_regression_check_operations
  - p11_qg_performance
  - bld_knowledge_card_regression_check
  - p03_ins_optimizer
  - p01_kc_regression_check
  - regression-check-builder
  - bld_collaboration_regression_check
  - bld_examples_regression_check
---

# Regression Check: Latency Baseline

## Purpose

Detects latency regressions in the organization Railway API by comparing current percentile response times against the v2.1 production baseline. Any metric exceeding +10% triggers a Slack alert before deployment proceeds.

## Baseline Reference (v2.1)

Captured 2026-03-15 from 24h production traffic (47,283 requests):

| Endpoint | p50 | p95 | p99 | Sample Size |
|----------|-----|-----|-----|-------------|
| `GET /api/v2/health` | 12ms | 28ms | 45ms | 18,450 |
| `POST /api/v2/chat` | 340ms | 890ms | 1,450ms | 12,100 |
| `POST /api/v2/search` | 85ms | 210ms | 380ms | 8,920 |
| `GET /api/v2/knowledge/:id` | 18ms | 42ms | 78ms | 5,200 |
| `POST /api/v2/evaluate` | 520ms | 1,200ms | 2,100ms | 2,613 |

## Regression Thresholds

| Severity | Threshold | Action |
|----------|-----------|--------|
| **Pass** | <= baseline | No action, deploy proceeds |
| **Warn** | +1% to +10% | Log warning, deploy proceeds with note |
| **Fail** | > +10% | Block deployment, Slack alert, investigate |
| **Critical** | > +25% | Block + page on-call, likely infrastructure issue |

The +10% threshold was calibrated against natural traffic variance. Historical data shows v2.0 -> v2.1 had max 6% variance from day-to-day traffic patterns. Anything above 10% is a real regression, not noise.

## Test Protocol

### Step 1: Collect Current Metrics
```bash
# Run against staging, 1000 requests per endpoint
python scripts/load_test.py \
  --target https://organization-api-staging.railway.app \
  --endpoints health,chat,search,knowledge,evaluate \
  --requests-per-endpoint 1000 \
  --concurrency 10 \
  --output results/latency_current.json
```

### Step 2: Compare Against Baseline
```python
import json
from pathlib import Path

baseline = json.loads(Path("baselines/v2.1_latency.json").read_text())
current = json.loads(Path("results/latency_current.json").read_text())

regressions = []
for endpoint in baseline:
    for metric in ["p50", "p95", "p99"]:
        base_val = baseline[endpoint][metric]
        curr_val = current[endpoint][metric]
        delta_pct = ((curr_val - base_val) / base_val) * 100

        if delta_pct > 10:
            regressions.append({
                "endpoint": endpoint,
                "metric": metric,
                "baseline": base_val,
                "current": curr_val,
                "delta": f"+{delta_pct:.1f}%",
                "severity": "critical" if delta_pct > 25 else "fail"
            })

if regressions:
    send_slack_alert(regressions)
    sys.exit(1)
```

### Step 3: Alert Format
```json
{
  "channel": "#organization-alerts",
  "text": ":warning: Latency regression detected",
  "blocks": [
    {
      "type": "section",
      "text": "POST /api/v2/chat p95: 890ms -> 1,120ms (+25.8%) :red_circle:"
    },
    {
      "type": "section",
      "text": "Baseline: v2.1 (2026-03-15) | Current: v2.2-rc1 | Threshold: +10%"
    }
  ]
}
```

## Regression Investigation Playbook

| Symptom | Likely Cause | First Check |
|---------|-------------|-------------|
| All endpoints +15-25% | Infrastructure (Railway cold start, DB) | `railway logs --recent` |
| Only `/chat` regressed | LLM call or prompt size increased | Check prompt token count delta |
| Only `/search` regressed | BM25/FAISS index issue | Verify index freshness, Ollama status |
| p99 spiked but p50 stable | Tail latency from GC or connection pool | Check connection pool exhaustion |
| All metrics 2x+ | Wrong environment or region | Verify Railway service and region |

## Historical Trend

| Version | Date | p50 /chat | p95 /chat | Status |
|---------|------|-----------|-----------|--------|
| v1.8 | 2026-02-01 | 410ms | 980ms | — |
| v1.9 | 2026-02-15 | 380ms | 940ms | Improved (prompt optimization) |
| v2.0 | 2026-03-01 | 355ms | 910ms | Improved (connection pooling) |
| v2.1 | 2026-03-15 | 340ms | 890ms | **Current baseline** |

## CI Integration

```yaml
# .github/workflows/regression.yml
- name: Latency regression check
  run: |
    python scripts/load_test.py --target $STAGING_URL --output results/current.json
    python scripts/regression_check.py --baseline baselines/v2.1.json --current results/current.json --threshold 10
  env:
    SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
```

## Anti-Patterns
- Comparing against outdated baseline (refresh after each major release)
- Running load test with 10 requests (not statistically significant, need >= 1000)
- Testing against production instead of staging (affects real users)
- Single percentile only (p50 hides tail latency regressions at p99)
- Ignoring cold-start: first 50 requests after deploy are always slower

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_regression_check]] | sibling | 0.43 |
| [[p07_benchmark_api_latency]] | related | 0.41 |
| [[p07_regression_check_operations]] | sibling | 0.32 |
| [[p11_qg_performance]] | downstream | 0.30 |
| [[bld_knowledge_card_regression_check]] | upstream | 0.29 |
| [[p03_ins_optimizer]] | upstream | 0.28 |
| [[p01_kc_regression_check]] | related | 0.28 |
| [[regression-check-builder]] | related | 0.28 |
| [[bld_collaboration_regression_check]] | downstream | 0.26 |
| [[bld_examples_regression_check]] | related | 0.24 |
