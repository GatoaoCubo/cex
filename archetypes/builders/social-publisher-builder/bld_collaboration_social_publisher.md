---
kind: collaboration
id: bld_collaboration_social_publisher
pillar: P12
llm_function: COLLABORATE
purpose: How social-publisher-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Social Publisher"
version: "1.0.0"
author: n03_builder
tags: [social_publisher, builder, examples]
tldr: "Golden and anti-examples for social publisher construction, demonstrating ideal structure and common pitfalls."
domain: "social publisher construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Collaboration: social-publisher-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how does automated social posting work for this company, and what config do they need?"
I do not write captions. I do not implement API clients. I do not deploy servers.
I produce pipeline architecture + config schema so downstream builders can implement and deploy.

## Crew Compositions

### Crew: "Social Publishing End-to-End"
```
1. knowledge-card-builder  → "domain knowledge about the business niche and audience"
2. social-publisher-builder → "pipeline architecture + config schema + quality gates"
3. prompt-template-builder  → "caption generation prompts for each content type"
4. cli-tool-builder         → "Python runtime that reads config and executes pipeline"
5. spawn-config-builder     → "cron/scheduler deployment for automated execution"
```

### Crew: "Marketing Automation Suite"
```
1. social-publisher-builder → "auto-posting pipeline and config"
2. workflow-builder         → "content approval workflow before publishing"
3. quality-gate-builder     → "post quality validation rules"
4. scoring-rubric-builder   → "engagement scoring dimensions"
```

## Handoff Protocol
| I receive from | Data | Format |
|---------------|------|--------|
| knowledge-card-builder | Niche knowledge, audience profile | KC artifact |
| User/N07 | Business requirements, platforms, schedule | Mission handoff .md |

| I send to | Data | Format |
|----------|------|--------|
| prompt-template-builder | Content types, tone, persona, platform constraints | Config YAML |
| cli-tool-builder | Full pipeline spec, config schema, API endpoints | Architecture .md |
| spawn-config-builder | Scheduling requirements, retry policy | Config section |
| N05_operations | Deploy request for cron + monitoring | Signal |

## Nucleus Routing
| Phase | Nucleus | Why |
|-------|---------|-----|
| Pipeline design | N03 (engineering) | Architecture and schema work |
| Content strategy | N02 (marketing) | Brand, tone, calendar decisions |
| Implementation | N03 → N05 | Code → deploy |
| Instance config | N02 | Company-specific marketing config |
