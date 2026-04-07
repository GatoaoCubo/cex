---
id: mission_content_monetization
kind: workflow
pillar: P12
title: "Mission DAG — Content Monetization Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n07_admin
domain: commercial-monetization
tags: [mission, content-monetization, N06, billing, credits, courses]
tldr: "5-phase mission to distill 4,409 lines of production billing/credits/courses code into a reusable content-monetization-builder. N06 superintends."
quality: 9.0
---

# Mission: Content Monetization Builder

## DAG
```
Phase 1 (N07 scrape) ──→ Phase 2 (N04 KCs) ──→ Phase 3 (N03 ISOs)
                                                       ↓
                         Phase 5 (N07 consolidate) ←── Phase 4 (N06 nucleus)
```

## Status
- [ ] Phase 1: Scrape source systems (N07, 30min)
- [ ] Phase 2: 8 platform KCs (N04, 2h)
- [ ] Phase 3: 14 builder ISOs (N03, 2h)
- [ ] Phase 4: N06 nucleus + templates (N06, 1h)
- [ ] Phase 5: Instance + compile + score (N07, 30min)

## Source
- codexa-core/api/core/ — 6 files, 4,409 lines
- billing_executor (745L), credit_system (711L), cursos_executor (562L)
- erp_connector (1316L), anuncio_validator (619L), email_templates (456L)

## Expected: 31 artifacts
- 8 platform KCs + 14 ISOs + 4 nucleus + 1 template + 3 examples + 1 instance

## Superintendent: N06 (Commercial)
## Spec: `.cex/runtime/handoffs/mission_content_monetization.md`


## Mission Decomposition

This mission breaks down into sequential waves with inter-wave quality gates:

- **Wave 1 (Research)**: N01 gathers context, competitive data, and domain knowledge
- **Wave 2 (Build)**: N03 constructs artifacts using research as input context
- **Wave 3 (Polish)**: N02 applies brand voice and visual consistency to outputs
- **Wave 4 (Validate)**: N05 runs quality checks, scoring, and regression tests

### Resource Allocation

```yaml
# Mission budget allocation
budget:
  total_tokens: 200000
  wave_1_research: 50000
  wave_2_build: 80000
  wave_3_polish: 40000
  wave_4_validate: 30000
  max_duration_minutes: 30
  max_parallel_nuclei: 4
```

| Wave | Nucleus | Input | Output | Quality Gate |
|------|---------|-------|--------|-------------|
| 1 | N01 | Goal statement | Research brief | Completeness >= 8.0 |
| 2 | N03 | Research brief | Artifacts | Structural >= 8.5 |
| 3 | N02 | Raw artifacts | Polished artifacts | Brand compliance |
| 4 | N05 | Final artifacts | Score report | All >= 9.0 |

