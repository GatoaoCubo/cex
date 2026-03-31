---
id: mission_geo_discovery
kind: workflow
pillar: P12
title: "Mission DAG — Geo Discovery Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n07_admin
domain: intelligence-discovery
tags: [mission, geo-discovery, N01, entity-resolution, marketplace, grounding]
tldr: "5-phase mission to distill 3,745 lines of production entity-resolution/marketplace-search code into a reusable geo-discovery-builder. N01 superintends."
quality: null
---

# Mission: Geo Discovery Builder

## DAG
```
Phase 1 (N07 scrape) ──→ Phase 2 (N04 KCs) ──→ Phase 3 (N03 ISOs)
                                                       ↓
                         Phase 5 (N07 consolidate) ←── Phase 4 (N01 nucleus)
```

## Status
- [ ] Phase 1: Scrape source systems (N07, 30min)
- [ ] Phase 2: 6 platform KCs (N04, 2h)
- [ ] Phase 3: 14 builder ISOs (N03, 2h)
- [ ] Phase 4: N01 nucleus + templates (N01, 1h)
- [ ] Phase 5: Instance + compile + score (N07, 30min)

## Source
- codexa-core/api/core/ — 6 files, 3,745 lines
- entity_resolver (934L), anuncio_synthesizer (1586L), compliance_checker (410L)
- context_filter (339L), meli_client (303L), gemini_search_client (173L)

## Expected: 29 artifacts
- 6 platform KCs + 14 ISOs + 4 nucleus + 1 template + 3 examples + 1 instance

## Superintendent: N01 (Intelligence)
## Spec: `.cex/runtime/handoffs/mission_geo_discovery.md`
