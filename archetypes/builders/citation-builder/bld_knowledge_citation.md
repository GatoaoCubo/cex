---
kind: knowledge_card
id: bld_knowledge_card_citation
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for citation production — source attribution patterns
sources: kc_citation.md, industry standards, bibliographic best forctices
quality: 9.0
title: "Knowledge Card Citation"
version: "1.0.0"
author: n03_builder
tags: [citation, builder, examples]
tldr: "Golden and anti-examples for citation construction, demonstrating ideal structure and common pitfalls."
domain: "citation construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_citation
  - p03_sp_citation_builder
  - p10_lr_citation_builder
  - citation-builder
  - bld_instruction_citation
  - bld_output_template_citation
  - p11_qg_citation
  - bld_collaboration_citation
  - bld_schema_citation
  - bld_config_citation
---

# Domain Knowledge: citation
## Executive Summary
Citations are structured source attributions that ground LLM outputs in verifiable evidence. Each citation records source type, reliability tier, URL, access date, and a concrete excerpt. They differ from knowledge_cards (which contain distilled facts), rag_sources (which configure retrieval pipelines), and glossary_entries (which define terms).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (Knowledge) |
| LLM Function | INJECT |
| Max bytes | 2048 |
| Naming | p01_cit_{topic}.md |
| Core | false |
| Source types | web, paper, book, internal, api |
| Reliability tiers | tier_1 (primary), tier_2 (docs), tier_3 (blog) |
## Patterns
- **Inline citation**: Ground a specific claim — `[1] Author, Title (Year)`
- **Citation bundle**: Multiple sources supporting one domain
- **Tiered reliability**: tier_1=peer-reviewed, tier_2=official docs, tier_3=blog
- **Temporal freshness**: date_accessed + freshness_days policy
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| URL-only | No context if URL rots |
| No date_accessed | Cannot assess temporal validity |
| No excerpt | Reader must visit source to verify |
| Single tier for all | Blog weighted same as paper |
## Cross-Framework Map
| Provider | Citation Concept |
|----------|-----------------|
| OpenAI | File search annotations (file_citation objects) |
| Anthropic | Source-grounded citations (2025+) |
| Google | Vertex AI Grounding metadata |
| LangChain | Document.metadata["source"] |
| Perplexity | Inline numbered references |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_citation]] | sibling | 0.66 |
| [[p03_sp_citation_builder]] | downstream | 0.51 |
| [[p10_lr_citation_builder]] | downstream | 0.51 |
| [[citation-builder]] | related | 0.45 |
| [[bld_instruction_citation]] | downstream | 0.44 |
| [[bld_output_template_citation]] | downstream | 0.42 |
| [[p11_qg_citation]] | downstream | 0.41 |
| [[bld_collaboration_citation]] | downstream | 0.41 |
| [[bld_schema_citation]] | downstream | 0.40 |
| [[bld_config_citation]] | downstream | 0.37 |
