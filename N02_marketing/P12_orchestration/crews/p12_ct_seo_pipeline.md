---
id: p12_ct_seo_pipeline.md
kind: crew_template
8f: F2_become
pillar: P12
llm_function: CALL
crew_name: seo_pipeline
purpose: Coordinate a 3-role crew that optimizes content for search -- keyword research, content optimization, and performance scoring
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "researcher -> optimizer -> scorer"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "SEO Pipeline Crew Template"
version: "1.0.0"
author: n02_marketing
tags: [crew_template, seo_pipeline, marketing, composable, crewai, search_optimization]
tldr: "3-role sequential crew: keyword research -> content optimization -> SEO performance scoring with pass/fail gate"
domain: "search engine optimization pipeline"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_keyword_researcher.md
  - p02_ra_content_optimizer.md
  - p02_ra_seo_scorer.md
  - p12_ct_product_launch.md
  - p12_ct_content_campaign.md
  - p12_ct_brand_audit.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
---

## Overview
Instantiate when existing content needs SEO optimization or when new content
must be search-optimized before publication. The crew runs three roles in strict
sequence: keyword_researcher identifies target keywords with search volume,
difficulty, and intent mapping; content_optimizer rewrites headings, meta
descriptions, internal links, and body copy grounded on the keyword brief;
seo_scorer evaluates the optimized content against 8 SEO dimensions and gates
publication. Producer is N02 (marketing); consumers are N05 (deploy) and growth ops.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| keyword_researcher | p02_ra_keyword_researcher.md | Research target keywords with volume, difficulty, intent classification |
| content_optimizer | p02_ra_content_optimizer.md | Optimize headings, meta, links, body copy grounded on keyword brief |
| seo_scorer | p02_ra_seo_scorer.md | Score optimized content on 8 SEO dimensions, gate publication |

## Process
Topology: `sequential`. Rationale: optimizer cannot rewrite without the keyword
brief (no keywords = blind optimization); scorer cannot evaluate without seeing
both the keyword targets and the optimized content (needs to verify keyword
placement against intent). Parallelism would produce content optimized for
unknown keywords.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| keyword_researcher | shared | persistent (keyword map saved to P01) |
| content_optimizer | shared | per-crew-instance |
| seo_scorer | shared | persistent (scores saved to P11 regression_check) |

## Handoff Protocol
`a2a-task-sequential` -- researcher emits `keyword_brief_id` with target keywords
and intent map. Optimizer reads brief, rewrites content, emits `optimized_content_id`.
Scorer reads both keyword brief and optimized content, produces SEO score card.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] Keyword brief contains >= 5 target keywords with volume + difficulty + intent
- [ ] Optimized content includes primary keyword in title, H1, meta description, first 100 words
- [ ] SEO score card covers all 8 dimensions with composite >= 8.5
- [ ] Handoff protocol signals present for 3/3 roles
- [ ] No keyword stuffing (density <= 2.5% per keyword)

## Instantiation
```bash
python _tools/cex_crew.py run seo_pipeline \
    --charter N02_marketing/P12_orchestration/crews/team_charter_seo_pipeline.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_keyword_researcher.md]] | upstream | 0.52 |
| [[p02_ra_content_optimizer.md]] | upstream | 0.50 |
| [[p02_ra_seo_scorer.md]] | upstream | 0.48 |
| [[p12_ct_product_launch.md]] | sibling | 0.36 |
| [[p12_ct_content_campaign.md]] | sibling | 0.34 |
| [[p12_ct_brand_audit.md]] | sibling | 0.38 |
| [[bld_instruction_crew_template]] | related | 0.31 |
| [[bld_collaboration_crew_template]] | related | 0.29 |
