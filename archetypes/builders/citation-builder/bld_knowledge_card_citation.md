---
kind: knowledge_card
id: bld_knowledge_card_citation
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for citation production — source attribution patterns
sources: kc_citation.md, industry standards, bibliographic best forctices
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
