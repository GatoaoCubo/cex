---
id: bld_collaboration_tagline
kind: collaboration
pillar: P12
builder: tagline-builder
version: 1.0.0
quality: 9.0
title: "Collaboration Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: COLLABORATE
related:
  - bld_collaboration_landing_page
  - tagline-builder
  - bld_architecture_tagline
  - bld_tools_tagline
  - bld_memory_tagline
  - bld_config_tagline
  - kc_tagline
  - bld_system_prompt_tagline
  - bld_output_template_tagline
  - bld_quality_gate_tagline
---
# Collaboration: Tagline Builder

## Upstream (receives from)
1. brand_config.yaml → brand identity, tone, audience
2. N01 Research → competitor taglines, market positioning data
3. N06 Commercial → pricing tier names, product positioning

## Downstream (sends to)
1. landing-page-builder → hero headline, sub-headline
2. social-publisher-builder → bio lines, post captions
3. content-monetization-builder → course taglines, product names
4. N02 Marketing → campaign headlines, ad copy
5. N06 Commercial → pitch deck one-liners, brand book messaging

## Crew Behavior
1. In a crew, tagline-builder runs EARLY (provides messaging foundation)
2. Other builders reference tagline output for consistency
3. If brand_config changes, tagline should be regenerated first

## Metadata

```yaml
id: bld_collaboration_tagline
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-collaboration-tagline.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | tagline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_landing_page]] | sibling | 0.51 |
| [[tagline-builder]] | upstream | 0.48 |
| [[bld_architecture_tagline]] | upstream | 0.48 |
| [[bld_tools_tagline]] | upstream | 0.47 |
| [[bld_memory_tagline]] | upstream | 0.42 |
| [[bld_config_tagline]] | upstream | 0.42 |
| [[kc_tagline]] | upstream | 0.39 |
| [[bld_system_prompt_tagline]] | upstream | 0.37 |
| [[bld_output_template_tagline]] | upstream | 0.36 |
| [[bld_quality_gate_tagline]] | upstream | 0.35 |
