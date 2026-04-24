---
id: p12_sig_builder_nucleus
kind: signal
8f: F8_collaborate
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
related:
  - p04_fd_builder_toolkit
  - p06_if_builder_nucleus
  - p08_ac_builder_nucleus
  - p03_pt_builder_construction
  - p12_dr_builder_nucleus
  - p12_sig_admin_orchestration
  - p12_ho_builder_nucleus
  - signal-builder
  - p03_ch_builder_pipeline
  - bld_collaboration_signal
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_fd_builder_toolkit]] | upstream | 0.38 |
| [[p06_if_builder_nucleus]] | upstream | 0.37 |
| [[p08_ac_builder_nucleus]] | upstream | 0.32 |
| [[p03_pt_builder_construction]] | upstream | 0.31 |
| [[p12_dr_builder_nucleus]] | related | 0.30 |
| [[p12_sig_admin_orchestration]] | sibling | 0.28 |
| [[p12_ho_builder_nucleus]] | related | 0.27 |
| [[signal-builder]] | related | 0.26 |
| [[p03_ch_builder_pipeline]] | upstream | 0.25 |
| [[bld_collaboration_signal]] | related | 0.25 |
