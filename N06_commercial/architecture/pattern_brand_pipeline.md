---
id: p08_pat_brand_pipeline
kind: pattern
pillar: P08
title: "Pattern — Brand Pipeline (Discovery → Propagation)"
nucleus: N06
version: 1.0.0
created: 2026-04-07
author: n06_commercial
domain: brand_infrastructure
quality: 9.0
tags: [pattern, brand, pipeline, N06, architecture, propagation]
tldr: "End-to-end brand pipeline: ingest → discover → configure → validate → propagate → audit. 6 stages, 5 tools, zero manual steps."
density_score: 0.95
---

# Pattern: Brand Pipeline

## Overview

The brand pipeline converts messy user inputs (scattered docs, verbal descriptions, competitor examples) into a validated, propagated brand identity that every nucleus can use.

**ROI**: Without this pipeline, brand setup takes 4+ hours of manual Q&A and file editing. With it: 15 minutes interactive + 5 minutes automated = 20 minutes total. 12:1 time ROI.

---

## Pipeline Stages

```
┌──────────┐    ┌───────────┐    ┌───────────┐    ┌──────────┐    ┌───────────┐    ┌─────────┐
│ INGEST   │───▶│ DISCOVER  │───▶│ CONFIGURE │───▶│ VALIDATE │───▶│ PROPAGATE │───▶│ AUDIT   │
│          │    │           │    │           │    │          │    │           │    │         │
│brand_    │    │brand_     │    │brand_     │    │brand_    │    │brand_     │    │brand_   │
│ingest.py │    │discovery  │    │config     │    │validate  │    │propagate  │    │audit.py │
│          │    │interview  │    │extractor  │    │.py       │    │.py        │    │         │
└──────────┘    └───────────┘    └───────────┘    └──────────┘    └───────────┘    └─────────┘
  Optional        GDP(5-6Q)       Automated       13 fields       7 nuclei        6 dimensions
```

### Stage 1: INGEST (Optional)
**Tool**: `brand_ingest.py`
**Input**: User's messy folder (logos, docs, old websites)
**Output**: Brand signal report (extracted colors, fonts, tone samples)
**GDP**: No — purely analytical
**When to skip**: User can articulate their brand verbally

### Stage 2: DISCOVER
**Tool**: `brand_discovery_interview.md` prompt
**Input**: User conversation (GDP required)
**Output**: Raw brand decisions (tone, audience, values, positioning)
**GDP**: Yes — 5-6 core questions, optional deep dive (15 questions)
**Key questions**:
1. Who is your customer? (ICP)
2. What do you do differently? (positioning)
3. How should your brand feel? (tone)
4. What's your price range? (commercial anchor)
5. What brands do you admire? (style reference)
6. What's your brand name? (identity)

### Stage 3: CONFIGURE
**Tool**: `brand_config_extractor.md` prompt
**Input**: Discovery answers + ingest signals (if any)
**Output**: `.cex/brand/brand_config.yaml` (13 required fields)
**GDP**: No — extraction is mechanical

### Stage 4: VALIDATE
**Tool**: `brand_validate.py`
**Input**: `brand_config.yaml`
**Output**: Pass/Fail + list of missing/invalid fields
**GDP**: No — validation is deterministic
**Required fields**: name, tagline, tone, audience, values, colors_primary, colors_secondary, typography, voice_do, voice_dont, positioning, domain, language

### Stage 5: PROPAGATE
**Tool**: `brand_propagate.py`
**Input**: Validated `brand_config.yaml`
**Output**: Updated brand context in all 7 nucleus directories
**GDP**: No — propagation is atomic
**Critical**: Must be atomic (AX10). All 7 nuclei update or none do.

### Stage 6: AUDIT
**Tool**: `brand_audit.py`
**Input**: Propagated brand state across system
**Output**: Brand Health Index (0-10) across 6 dimensions
**GDP**: No — scoring is deterministic
**Threshold**: BHI ≥ 7.0 = healthy. Below = requires intervention.

---

## Failure Modes

| Stage | Failure | Detection | Recovery |
|-------|---------|-----------|----------|
| INGEST | No usable signals in folder | Empty signal report | Skip to DISCOVER |
| DISCOVER | User abandons mid-interview | Incomplete answers | Save progress, resume later |
| CONFIGURE | Ambiguous answers → wrong config | VALIDATE catches | Re-run DISCOVER for failed fields |
| VALIDATE | Missing required fields | Validation report | Prompt user for missing data |
| PROPAGATE | Partial update (crash mid-way) | Nucleus brand mismatch | Rollback + retry atomic |
| AUDIT | BHI < 7.0 | Score report | Targeted fix on lowest dimension |

---

## Integration Points

| System | How Brand Pipeline Connects |
|--------|---------------------------|
| `cex_bootstrap.py` | Orchestrates full pipeline end-to-end |
| `brand_inject.py` | Post-propagation: replaces `{{BRAND_*}}` tokens |
| `CLAUDE.md` | Brand Identity section auto-populated after Stage 5 |
| `cex_crew_runner.py` | Injects brand context into every prompt |
| `cex_notebooklm.py` | Uses brand voice for content generation |

---

## Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Time to brand (cold start) | < 20 min | Discovery + config + validate + propagate |
| Fields validated | 13/13 | `brand_validate.py` pass rate |
| Propagation coverage | 7/7 nuclei | `brand_propagate.py` success count |
| Brand Health Index | ≥ 7.0 | `brand_audit.py` score |
| Token replacement rate | 100% | `brand_inject.py` zero remaining `{{BRAND_*}}` |
