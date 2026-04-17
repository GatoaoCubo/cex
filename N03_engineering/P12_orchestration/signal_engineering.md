---
id: p12_sig_builder_nucleus
kind: signal
pillar: P12
title: Signal Definitions -- Builder Nucleus
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [signal, builder, N03]
tldr: Completion and error signals from the 8F pipeline -- JSON format, file-based.
density_score: 0.88
---

# Signals: Builder Nucleus

## Format

JSON files written to signal directory.

| Field | Type | Description |
|-------|------|-------------|
| nucleus | string | N03 |
| status | enum | building, complete, error, retry |
| kind | string | What kind was being built |
| quality | float | Score (0.0 if error) |
| timestamp | ISO 8601 | When emitted |
| path | string | Artifact path (null if error) |
| message | string | Human-readable status |

## Types

- **complete**: Artifact passes F7, saved + compiled + indexed
- **error**: F7 fails after max retries, or hard failure
- **retry**: F7 soft-fails, pipeline returns to F6
- **building**: Emitted at F1 start to indicate work in progress

## Delivery

File naming: {nucleus}_{kind}_{status}_{timestamp}.json
Monitors poll the signal directory at configurable interval.

## Quality Metrics

| Metric | Value | Threshold |
|--------|-------|-----------|
| Structural completeness | High | ≥ 8.5 |
| Domain specificity | engineering | Verified |
| Cross-reference density | Adequate | ≥ 3 refs |
| Actionability | Verified | Pass |

### Key Principles

- Engineering artifacts follow CEX 8F pipeline from intent to publication
- Quality gates enforce minimum 8.0 threshold for all published artifacts
- Cross-nucleus references use explicit id-based linking, not path-based
- Version tracking enables rollback to any previous artifact state

### Usage Reference

```yaml
# signal integration
artifact: signal_engineering
nucleus: N03
domain: engineering
quality_threshold: 9.0
```

