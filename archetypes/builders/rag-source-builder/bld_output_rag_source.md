---
kind: output_template
id: bld_output_template_rag_source
pillar: P05
llm_function: PRODUCE
derives_from: SCHEMA.md
version: 1.0.0
quality: 9.0
title: "Output Template Rag Source"
author: n03_builder
tags: [rag_source, builder, examples]
tldr: "Golden and anti-examples for rag source construction, demonstrating ideal structure and common pitfalls."
domain: "rag source construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_integration_guide
  - bld_schema_rag_source
  - bld_schema_api_reference
  - bld_schema_reranker_config
  - bld_schema_voice_pipeline
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_schema_bugloop
  - bld_schema_search_strategy
---

# Output Template: rag_source
## Frontmatter Template
```yaml
id: p01_rs_{{source_slug}}
kind: rag_source
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
url: "{{source_url}}"
domain: "{{domain_value}}"
last_checked: "{{YYYY-MM-DD}}"
quality: null
tags: [rag-source, {{domain_tag}}, {{format_tag}}]
tldr: "{{dense_summary_max_160ch}}"
keywords: [{{kw1}}, {{kw2}}, {{kw3}}]
reliability: "{{high|medium|low}}"
format: "{{html|json|api|pdf|csv}}"
extraction_method: "{{crawl|api_call|scrape|download}}"
```
## Body Template
```markdown
## Source Description
{{What this source is, what content it contains, who maintains it, target audience.
2-4 sentences. Dense. No filler.}}
## Freshness Policy
- Re-check interval: {{30|60|90}} days
- Staleness threshold: {{90}} days
- Trigger: {{version release / monthly / on demand}}
- Last verified: {{YYYY-MM-DD}}
## Extraction Notes
- Method: {{crawl / api_call / scrape / download}}
- Format: {{html / json / api / pdf / csv}}
- Auth required: {{yes (API key) / no}}
- Known quirks: {{pagetion / rate limits / JS rendering required / none}}
## References
- Parent domain: {{domain_value}}
- Related sources: {{p01_rs_related_slug if known, else none}}
```
## Variable Reference
| Variable | Required | Constraint |
|----------|----------|-----------|
| source_slug | yes | ^[a-z][a-z0-9_]+$, max 30 chars |
| source_url | yes | valid URL, https:// preferred |
| domain_value | yes | CEX domain taxonomy value |
| YYYY-MM-DD | yes | ISO 8601 date |
| who_produced | yes | agent id or user handle |
| dense_summary | yes | <= 160 chars |
| domain_tag | yes | e.g., llm_providers, benchmarks |
| format_tag | yes | e.g., html, json, api |
## Size Budget
Total body (all sections): <= 1024 bytes. Trim Extraction Notes if needed — Source Description and Freshness Policy take priority.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | downstream | 0.38 |
| [[bld_schema_rag_source]] | downstream | 0.37 |
| [[bld_schema_api_reference]] | downstream | 0.37 |
| [[bld_schema_reranker_config]] | downstream | 0.36 |
| [[bld_schema_voice_pipeline]] | downstream | 0.36 |
| [[bld_schema_quickstart_guide]] | downstream | 0.36 |
| [[bld_schema_usage_report]] | downstream | 0.36 |
| [[bld_schema_pitch_deck]] | downstream | 0.35 |
| [[bld_schema_bugloop]] | downstream | 0.35 |
| [[bld_schema_search_strategy]] | downstream | 0.35 |
