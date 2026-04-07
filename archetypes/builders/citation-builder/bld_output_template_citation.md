---
kind: output_template
id: bld_output_template_citation
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for citation production
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
- **Author**: {{author_name}}
- **Title**: {{full_title}}
- **Publisher/Venue**: {{publisher_or_venue}}
- **Date**: {{publication_date}}
- **Type**: {{source_type}} ({{reliability_tier}})

## Excerpt
> {{Key passage from source, 1-3 sentences}}

## Relevance
- Supports: {{what claims or artifacts this citation grounds}}
- Scope: {{which domains or kinds benefit from this source}}

## Verification
- URL: {{source_url}}
- Accessed: {{date_accessed}}
- Freshness policy: {{days until re-verification needed}}
- DOI/ISBN: {{if applicable}}

## Related
- Citations: {{related_citation_ids}}
- Knowledge cards: {{supported_kc_ids}}
- Context docs: {{supported_ctx_ids}}
```
