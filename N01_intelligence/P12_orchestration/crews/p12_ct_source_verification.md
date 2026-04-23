---
id: p12_ct_source_verification.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: source_verification
purpose: "3-role sequential crew that validates external source claims -- harvest sources, cross-check assertions, score confidence per claim"
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "harvester -> cross_checker -> confidence_scorer"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: 0.90
title: "Source Verification Crew Template"
version: "1.0.0"
author: n01_intelligence
tags: [crew_template, source_verification, intelligence, composable, crewai, sequential, validation]
tldr: "3-role sequential crew: source harvesting -> cross-referencing -> confidence scoring"
domain: "source verification orchestration"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_harvester.md
  - p02_ra_cross_checker.md
  - p02_ra_confidence_scorer.md
  - p12_ct_competitive_intelligence.md
  - p12_ct_deep_research.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - p03_sp_crew_template_builder
  - bld_schema_crew_template
---

## Overview
Instantiate when a set of claims or an existing artifact needs independent source
verification before publication or downstream consumption. Producer: N01. Consumers:
any nucleus that needs verified inputs (N04 knowledge cards, N06 pricing data, N02
market claims). This crew is a reusable quality layer -- it can verify output from
other crews (e.g., run source_verification on a competitive_intelligence brief).

Distinct from the `validator` role in competitive_intelligence (which is embedded in
that crew): this crew operates standalone on any input artifact, making it composable
across the entire CEX system.

## Roles
| Role | Role Assignment ID | Reason |
|------|--------------------|--------|
| harvester | p02_ra_harvester.md | Extract all factual claims from input artifact, locate primary sources for each, produce sourced_claims KC |
| cross_checker | p02_ra_cross_checker.md | For each claim-source pair, find >= 1 independent corroborating source; flag contradictions and single-source claims |
| confidence_scorer | p02_ra_confidence_scorer.md | Score each claim 0.0-1.0 based on corroboration depth, source authority, and recency; produce final verification report |

## Process
Topology: `sequential`. Rationale: cross_checker needs the claim-source pairs from
harvester; confidence_scorer needs the corroboration evidence from cross_checker.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| harvester | shared | per-crew-instance (claim extraction is input-specific) |
| cross_checker | shared | per-crew-instance + source cache for reuse |
| confidence_scorer | shared | per-crew-instance + regression_check archive |

## Handoff Protocol
`a2a-task-sequential` -- each role emits `artifact_path` + `quality_score` +
`claim_count`. Confidence_scorer final signal adds `overall_confidence` (0.0-1.0) +
`verdict: verified | partial | unverified` + `low_confidence_claims` list.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] harvester extracts all factual claims from input artifact (>= 5 claims)
- [ ] cross_checker finds >= 1 corroborating source per claim (or flags explicitly)
- [ ] confidence_scorer overall confidence >= 0.70 for `verified` verdict
- [ ] Each claim has a numeric confidence score (not qualitative)
- [ ] Handoff protocol signals present for 3/3 roles

## Instantiation
```bash
python _tools/cex_crew.py run source_verification \
    --charter N01_intelligence/P12_orchestration/crews/team_charter_intelligence_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship |
|----------|-------------|
| [[p02_ra_harvester.md]] | upstream |
| [[p02_ra_cross_checker.md]] | upstream |
| [[p02_ra_confidence_scorer.md]] | upstream |
| [[p12_ct_competitive_intelligence.md]] | sibling |
| [[p12_ct_deep_research.md]] | sibling |
| [[bld_instruction_crew_template]] | upstream |
| [[bld_collaboration_crew_template]] | related |
| [[p11_qg_crew_template]] | upstream |
| [[p03_sp_crew_template_builder]] | upstream |
| [[bld_schema_crew_template]] | upstream |
