---
kind: collaboration
id: bld_collaboration_research_pipeline
pillar: P12
llm_function: COLLABORATE
purpose: How research-pipeline-builder works in crews with other builders
pattern: each builder must know its ROLE, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Research Pipeline"
version: "1.0.0"
author: n03_builder
tags: [research_pipeline, builder, examples]
tldr: "Golden and anti-examples for research pipeline construction, demonstrating ideal structure and common pitfalls."
domain: "research pipeline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_social_publisher
  - research-pipeline-builder
  - bld_collaboration_content_monetization
  - n01_dr_research_pipeline
  - p03_sp_research_pipeline_builder
  - n01_tool_research_pipeline
  - bld_architecture_research_pipeline
  - bld_collaboration_knowledge_card
  - p08_ac_intelligence
  - p12_dr_intelligence
---

# Collaboration: research-pipeline-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how do we collect, score, synthesize, and verify market intelligence from multiple sources end-to-end?"
I do not write API clients. I do not generate content. I do not deploy services.
I produce pipeline architecture + config schema so downstream builders implement and deploy.

## Crew Compositions

### Crew: "Market Intelligence End-to-End"
```
1. research-pipeline-builder → "7-stage pipeline architecture + config + quality gates"
2. knowledge-card-builder    → "domain knowledge cards from research output"
3. api-client-builder        → "Python clients for each data source"
4. cli-tool-builder          → "orchestrator CLI that runs the pipeline"
5. formatter-builder         → "HTML/PPTX report templates"
6. spawn-config-builder      → "cron deployment for scheduled research"
```

### Crew: "Research → Content → Publish"
```
1. research-pipeline-builder → "collect market intelligence"
2. prompt-template-builder   → "turn research into content briefs"
3. social-publisher-builder  → "publish content to social platforms"
```

## Handoff Protocol
| I receive from | Data | Format |
|---------------|------|--------|
| User / N07 | Research query + niche requirements | Mission handoff .md |
| knowledge-card-builder | Domain context for STORM perspectives | KC artifact |

| I send to | Data | Format |
|----------|------|--------|
| N02_marketing | Research results for content strategy | JSON + signal |
| N06_commercial | Pricing intelligence, competitor data | JSON + signal |
| N01_intelligence | Verified market report | HTML/PPTX/JSON |
| cli-tool-builder | Pipeline spec for implementation | Architecture .md |
| api-client-builder | Source API specs for client code | Tools .md |

## Nucleus Routing
| Phase | Nucleus | Why |
|-------|---------|-----|
| Pipeline design | N03 (engineering) | Architecture + schema work |
| Research execution | N01 (intelligence) | Domain expertise, source knowledge |
| Content from research | N02 (marketing) | Transform insights into content |
| Pricing from research | N06 (commercial) | Market pricing strategy |
| Deploy pipeline | N05 (operations) | Cron + monitoring |

## Relationship to Social Publisher
```
Research Pipeline (INPUT)        Social Publisher (OUTPUT)
  collect → score → verify  →→→    generate → schedule → publish
  N01_intelligence               N02_marketing
  STORM+CRAG+CRITIC              Calendar + API + Rotation
```
Together they form the cycle: RESEARCH → DECISION → CONTENT → PUBLISH.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_social_publisher]] | sibling | 0.47 |
| [[research-pipeline-builder]] | upstream | 0.40 |
| [[bld_collaboration_content_monetization]] | sibling | 0.36 |
| [[n01_dr_research_pipeline]] | related | 0.34 |
| [[p03_sp_research_pipeline_builder]] | upstream | 0.31 |
| [[n01_tool_research_pipeline]] | upstream | 0.31 |
| [[bld_architecture_research_pipeline]] | upstream | 0.30 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.30 |
| [[p08_ac_intelligence]] | upstream | 0.28 |
| [[p12_dr_intelligence]] | related | 0.28 |
