---
id: brand_context_n04
kind: config
pillar: P09
title: Brand Context for N04
version: 2.0.0
created: 2026-04-01
updated: 2026-04-07
author: n04_knowledge
quality: 9.1
tags: [brand, context, n04, knowledge, rag, indexing, content-pillars]
tldr: "Brand context for N04 Knowledge — content pillar distribution, knowledge card adaptation rules, RAG chunking guidelines, taxonomy standards, and documentation voice for GATO³ feline wellness knowledge base."
density_score: 0.96
---

# Brand Context — N04 Knowledge

> Source: `.cex/brand/brand_config.yaml`
> Nucleus: N04 (Knowledge/Docs/RAG/Indexing)
> Domain: Knowledge cards, documentation, taxonomy, embeddings, retrieval

## Core Brand Identity

| Field | Value |
|-------|-------|
| **Brand** | GATO³ (Gato ao Cubo) |
| **Category** | Curadoria de bem-estar felino + casa multi-espécie harmonizada |
| **Archetype** | Caregiver (Cuidadora + Sábia + Criadora) |
| **Voice** | Sofisticado-acolhedor, informativo, minimalista |
| **Language** | pt-BR |

## Content Pillar Distribution

All N04 knowledge artifacts must respect these proportions:

| Pillar | Weight | N04 Application | Tag |
|--------|--------|-----------------|-----|
| Produtos (40%) | Dominant | Product selection criteria, compatibility guides, specification cards | `pillar:produto` |
| Educacional (30%) | Strong | Feline science KCs, "Você sabia?" callouts, behavioral insights | `pillar:educacional` |
| Dicas da Ro (20%) | Supporting | Step-by-step guides, troubleshooting, protocols | `pillar:dicas-ro` |
| Tendências (10%) | Minimal | Market trend KCs, design trend summaries | `pillar:tendencia` |

## Knowledge Card Adaptation Rules

### Title Format
- **Pattern**: "Como [ação] para [benefício] do seu gato"
- **Examples**:
  - ✅ "Como escolher a cama ideal para o conforto do seu gato"
  - ✅ "Como reduzir o estresse do seu gato em apartamento"
  - ❌ "Cama para gatos — Guia completo" (generic, no benefit)

### Opening Structure
1. Start with cat owner **pain point**, not product features
2. Acknowledge the feeling ("Sabemos que pode ser frustrante quando...")
3. Preview the solution ("Neste guia, a Ro vai te mostrar...")

### Chunking Strategy
- Break complex topics into **"Você sabia?"** callout boxes
- Maximum 200 words per section before a visual break
- Use Ro's voice for reassurance: "Lembre-se...", "Dica da Ro:", "O mais importante é..."
- Tag each chunk with content pillar for retrieval accuracy

### Documentation Voice for Portuguese Cat Owners
- **Tone**: Sofisticado-acolhedor — blend expertise with warmth
- **Structure**: Lead with practical benefits, support with science
- **Language patterns**: Use "seu gato" (familiar), avoid clinical veterinary terms
- **Examples**: Always use Brazilian household contexts (apartamentos, varandas, kitinets)
- **Pronouns**: "você" (informal, warm), never "senhor/senhora" (too formal)

## RAG & Indexing Guidelines

### Embedding Optimization
- **Chunk size**: 512 tokens (optimized for pt-BR diacritics overhead)
- **Overlap**: 50 tokens between chunks
- **Metadata tags**: Always include `pillar`, `domain`, `icp_segment`, `product_category`
- **Language model**: Use multilingual embeddings (pt-BR native support required)

### Taxonomy Standards

| Level | Example | Purpose |
|-------|---------|---------|
| Domain | `feline-wellness` | Top-level categorization |
| Category | `behavior`, `nutrition`, `products` | Mid-level grouping |
| Topic | `stress-reduction`, `environment-enrichment` | Specific subject |
| Subtopic | `window-perch-selection`, `scratching-post-placement` | Granular retrieval |

### ICP-Aware Retrieval
When building retrieval pipelines, prioritize:
1. Content matching ICP fears (stress, ugly products, uncertainty)
2. Content matching ICP aspirations (harmony, confidence, beauty)
3. Product-related content (40% pillar = most searched)
4. Educational content with scientific backing

## Brand Values in Knowledge Creation

| Value | Knowledge Application |
|-------|----------------------|
| Amor aos felinos | Every KC must prioritize cat well-being over convenience |
| Educação acolhedora | Explain the "why" — accessible science, never jargon |
| Qualidade impecável | No KC published below quality 8.0; target 9.0+ |
| Inovação com propósito | New knowledge structures must serve retrieval, not novelty |
| Comunidade | Cross-reference related KCs to build knowledge networks |

## Anti-Patterns (N04-specific)
- ❌ Clinical veterinary language without Ro's warmth layer
- ❌ Product-first content that ignores educational context
- ❌ Generic pet advice that applies equally to dogs (cat-specific only)
- ❌ Knowledge cards without content pillar tags (breaks retrieval)
- ❌ Orphan KCs with no cross-references (breaks knowledge graph)

## Cross-References
- KC structure contract → `P01_knowledge/library/domain/meta/kc_8f_pipeline.md`
- Template catalog → `P01_knowledge/library/domain/kc_template_catalog.md`
- Variable registry → `P01_knowledge/library/domain/meta/kc_instance_variable_registry.md`
- Brand config → `.cex/brand/brand_config.yaml`
- N02 voice guide → `N02_marketing/config/brand_context.md`
