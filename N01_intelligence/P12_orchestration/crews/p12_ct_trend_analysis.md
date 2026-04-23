---
id: p12_ct_trend_analysis.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: trend_analysis
purpose: "3-role sequential crew that identifies emerging trends in a domain -- signal scanning, pattern clustering, and executive trend brief"
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "scanner -> pattern_detector -> brief_writer"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: 0.91
title: "Trend Analysis Crew Template"
version: "1.0.0"
author: n01_intelligence
tags: [crew_template, trend_analysis, intelligence, composable, crewai, sequential]
tldr: "3-role sequential crew: signal scan -> pattern clustering -> executive trend brief"
domain: "trend analysis orchestration"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_scanner.md
  - p02_ra_pattern_detector.md
  - p02_ra_brief_writer.md
  - p12_ct_competitive_intelligence.md
  - p12_ct_deep_research.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - p03_sp_crew_template_builder
  - bld_schema_crew_template
---

## Overview
Instantiate when a domain needs an emerging-trend report rather than a static competitive
snapshot. Producer: N01. Consumers: N06 (strategic positioning), N02 (content calendar),
N07 (mission planning), N04 (knowledge gap detection). Distinct from `competitive_intelligence`
(point-in-time market scan) and `deep_research` (fact-validated comprehensive report): this
crew optimizes for temporal signal detection -- what is changing, accelerating, or decaying.

## Roles
| Role | Role Assignment ID | Reason |
|------|--------------------|--------|
| scanner | p02_ra_scanner.md | Collect weak and strong signals from multiple source types (news, papers, repos, social); emit raw signal KC with >= 8 data points and timestamps |
| pattern_detector | p02_ra_pattern_detector.md | Cluster signals into named trends, score momentum (accelerating/stable/decaying), identify 2+ cross-domain correlations |
| brief_writer | p02_ra_brief_writer.md | Produce executive trend brief with ranked trends, actionable implications, and confidence tiers |

## Process
Topology: `sequential`. Rationale: pattern_detector needs timestamped signals to cluster;
brief_writer needs named trends with momentum scores. Parallelism would break temporal
grounding.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| scanner | shared | persistent (raw signals KC saved to P01 for longitudinal tracking) |
| pattern_detector | shared | per-crew-instance (trend clusters are instance-specific) |
| brief_writer | shared | per-crew-instance |

## Handoff Protocol
`a2a-task-sequential` -- each role emits `artifact_path` + `quality_score` +
`signal_count` (scanner) or `trend_count` (pattern_detector). Brief_writer
final signal adds `top_trend` + `confidence_tier` for N07 routing.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] scanner raw signals KC contains >= 8 data points with timestamps and source URLs
- [ ] pattern_detector output names >= 3 trends with momentum scores
- [ ] brief_writer output quality >= 9.0 with ranked trends and actionable implications
- [ ] Handoff protocol signals present for 3/3 roles
- [ ] No role produced an artifact without reading upstream output

## Instantiation
```bash
python _tools/cex_crew.py run trend_analysis \
    --charter N01_intelligence/P12_orchestration/crews/team_charter_intelligence_default.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship |
|----------|-------------|
| [[p02_ra_scanner.md]] | upstream |
| [[p02_ra_pattern_detector.md]] | upstream |
| [[p02_ra_brief_writer.md]] | upstream |
| [[p12_ct_competitive_intelligence.md]] | sibling |
| [[p12_ct_deep_research.md]] | sibling |
| [[bld_instruction_crew_template]] | upstream |
| [[bld_collaboration_crew_template]] | related |
| [[p11_qg_crew_template]] | upstream |
| [[p03_sp_crew_template_builder]] | upstream |
| [[bld_schema_crew_template]] | upstream |
