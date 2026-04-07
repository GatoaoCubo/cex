---
id: p04_ct_cex_feedback
kind: cli_tool
pillar: P04
title: "CEX Feedback — Quality tracking, auto-archive, and promotion engine"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, governance, feedback, quality, lifecycle]
cli_command: "python _tools/cex_feedback.py"
cli_args:
  - name: "--archive"
    type: boolean
    required: false
    description: "Move archive candidates to _archived/"
  - name: "--promote"
    type: boolean
    required: false
    description: "List promotion candidates (quality >= 9.0)"
inputs: ["all CEX artifacts across P01-P12, builders, packages, nuclei"]
outputs: ["quality report with metrics", "archive/promote candidate lists", "metrics.jsonl log"]
dependencies: ["pyyaml"]
category: governance
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
---

## Purpose
Scans all CEX artifacts, extracts quality/density metrics from frontmatter, identifies archive candidates (age > 30 days + quality < 7.0) and promotion candidates (quality >= 9.0). Maintains metrics history in .cex/metrics.jsonl.

## Usage
```bash
# Full scan and report
python _tools/cex_feedback.py

# Move archive candidates to _archived/
python _tools/cex_feedback.py --archive

# List promotion candidates
python _tools/cex_feedback.py --promote
```

## Arguments
| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--archive` | flag | no | Execute archive moves |
| `--promote` | flag | no | Show promotion candidates |

No flags = scan + report only.

## Pipeline Position
**8F Function**: GOVERN (F7) + COLLABORATE (F8) — lifecycle governance and quality tracking.
**Stage**: Continuous governance. Runs periodically to maintain artifact health. Downstream of all creation tools.

## Dependencies
- Scans 22+ directories (P01-P12, archetypes/builders, packages, N01-N07)
- Writes to `_archived/` directory and `.cex/metrics.jsonl`
- Thresholds: archive < 7.0 (+ 30 days old), promote >= 9.0
