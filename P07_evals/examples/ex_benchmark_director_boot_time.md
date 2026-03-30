---
id: p07_bm_agent_node_boot_time
kind: benchmark
pillar: P07
description: "Benchmark for agent_node boot times across all providers"
metric: boot_time_seconds
version: 1.0.0
created: 2026-03-24
author: atlas
quality: 9.0
tags: [benchmark, performance, boot, agent_node]
---

# Benchmark: Satellite Boot Time

## Metric
Time from `Start-Process` to first Claude API response (seconds).

## Baselines (measured 2026-03-05)
| Satellite | Model | Boot Time | Status |
|-----------|-------|-----------|--------|
| edison | opus | 5s | PASS |
| shaka | sonnet | 12s | PASS |
| lily | sonnet | 10s | PASS |
| pytha | sonnet | 5s | PASS |
| atlas | opus | 15s | WARN (MCP heavy) |
| york | sonnet | 5s | PASS |
| chrome | sonnet | 10s | PASS |
| minimal | haiku | 2s | PASS |

## Thresholds
| Tier | Max Boot | Action |
|------|----------|--------|
| Fast | < 5s | Ideal for interactive |
| Normal | 5-15s | Acceptable for grid |
| Slow | > 15s | Investigate MCP load |

## How to Run
```bash
powershell -Command "Measure-Command { Start-Process boot\edison.cmd -Wait }"
```
