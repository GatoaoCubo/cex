---
kind: output_template
id: bld_output_template_citation
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for citation production
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Citation"
version: "1.0.0"
author: n03_builder
tags: [citation, builder, examples]
tldr: "Golden and anti-examples for citation construction, demonstrating ideal structure and common pitfalls."
domain: "citation construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_citation
  - bld_instruction_citation
  - p01_kc_citation
  - bld_architecture_citation
  - bld_knowledge_card_citation
  - p03_sp_citation_builder
  - bld_config_citation
  - p11_qg_citation
  - citation-builder
  - bld_examples_citation
---

# Output Template: citation
```yaml
---
id: p01_cit_{{topic_slug}}
kind: citation
pillar: P01
title: "{{Source Title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{builder_name}}"
source_type: {{web|paper|book|internal|api}}
reliability_tier: {{tier_1|tier_2|tier_3}}
url: "{{source_url}}"
date_accessed: "{{YYYY-MM-DD}}"
excerpt: "{{1-3 sentence relevant quote from source}}"
relevance_scope: [{{domain1}}, {{domain2}}]
domain: {{domain_name}}
quality: null
tags: [citation, {{tag1}}, {{tag2}}]
tldr: "{{Dense <=160ch summary of source}}"
---

# {{Source Title}}

## Source
1. **Author**: {{author_name}}
2. **Title**: {{full_title}}
3. **Publisher/Venue**: {{publisher_or_venue}}
4. **Date**: {{publication_date}}
5. **Type**: {{source_type}} ({{reliability_tier}})

## Excerpt
> {{Key passage from source, 1-3 sentences}}

## Relevance
1. Supports: {{what claims or artifacts this citation grounds}}
2. Scope: {{which domains or kinds benefit from this source}}

## Verification
1. URL: {{source_url}}
2. Accessed: {{date_accessed}}
3. Freshness policy: {{days until re-verification needed}}
4. DOI/ISBN: {{if applicable}}

## Related
1. Citations: {{related_citation_ids}}
2. Knowledge cards: {{supported_kc_ids}}
3. Context docs: {{supported_ctx_ids}}
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | citation construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_citation]] | downstream | 0.53 |
| [[bld_instruction_citation]] | upstream | 0.52 |
| [[p01_kc_citation]] | upstream | 0.49 |
| [[bld_architecture_citation]] | downstream | 0.43 |
| [[bld_knowledge_card_citation]] | upstream | 0.41 |
| [[p03_sp_citation_builder]] | upstream | 0.41 |
| [[bld_config_citation]] | downstream | 0.38 |
| [[p11_qg_citation]] | downstream | 0.38 |
| [[citation-builder]] | upstream | 0.36 |
| [[bld_examples_citation]] | downstream | 0.36 |
