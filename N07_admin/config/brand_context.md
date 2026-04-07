---
id: brand_context_n07
kind: config
pillar: P09
title: Brand Context for N07
version: 2.0.0
created: 2026-04-01
updated: 2026-04-07
author: n04_knowledge
quality: 9.1
tags: [brand, context, n07, orchestration, admin, dispatch]
tldr: "Brand context for N07 Orchestrator — strategic identity, nucleus routing, mission scoping, brand consistency enforcement, and GDP alignment for GATO³ multi-nucleus coordination."
density_score: 0.95
---

# Brand Context — N07 Orchestrator

> Source: `.cex/brand/brand_config.yaml`
> Nucleus: N07 (Administration/Orchestration)
> Domain: Dispatch, coordination, quality gates, GDP enforcement

## Core Brand Identity

| Field | Value |
|-------|-------|
| **Brand** | GATO³ (Gato ao Cubo) |
| **Tagline** | Educação que acalma, soluções que funcionam, casa que continua elegante. |
| **Slogan** | Cuidado em três dimensões. |
| **Archetype** | Caregiver (Cuidadora + Sábia + Criadora) |
| **Shadow** | Mártir — sacrificar qualidade por crescimento rápido |
| **Language** | pt-BR |

## Strategic Mission Context

### Brand Mission
Harmonizar casa e rotina para que gatos vivam melhor e tutores vivam mais leves — unindo curadoria veterinária, educação acolhedora e design que desaparece no ambiente.

### Brand Vision
Ser a referência nacional em bem-estar felino, onde cada produto, conteúdo e interação eleva a convivência entre gatos, tutores e lares.

### Brand Values (used in GDP decisions)
1. **Amor aos felinos** — Always prioritize cat well-being in content decisions
2. **Educação acolhedora** — Prefer educational over promotional content
3. **Qualidade impecável** — Never publish below quality 8.0
4. **Inovação com propósito** — Technology serves the mission, not the reverse
5. **Comunidade** — Build relationships, not just transactions

## N07 Orchestration Guidelines

### Mission Scoping Rules
When decomposing goals into nucleus tasks:
1. **Brand alignment check**: Every mission must map to at least one Brand Value
2. **ICP validation**: Target audience is always tutores de gatos 25-45 urbanos
3. **Content pillar distribution**: Respect the 40/30/20/10 split across missions
4. **Three dimensions**: Every deliverable should touch at least one of: gato bem-estar, tutor tranquilidade, casa harmonia

### Nucleus Dispatch — Brand Context Injection

| Nucleus | Brand Fields to Inject | Priority |
|---------|----------------------|----------|
| N01 Research | ICP, competitors, category, market context | High |
| N02 Marketing | Voice, tone, personality, content pillars, values | Critical |
| N03 Engineering | Colors, fonts, style, logo, accessibility | Critical |
| N04 Knowledge | Content pillars, language, ICP, category | High |
| N05 Operations | Payment, pricing, channels, geography | Medium |
| N06 Strategy | UVP, differentiator, pricing, tiers, expansion | High |

### GDP Decision Filters
When presenting decisions to user, apply these brand-aligned filters:
- **Tone decisions**: Default to `sofisticado-acolhedor` unless user specifies
- **Visual decisions**: Default to `minimal-pb` unless user specifies
- **Audience decisions**: Default to `ICP: tutores 25-45` unless user specifies
- **Channel decisions**: Respect tier priority: site > ML > Shopee > B2B

### Brand Consistency Enforcement
N07 must verify before consolidation:
- [ ] All N02 outputs use brand voice (no gíria, no CAPS LOCK)
- [ ] All N03 outputs use brand colors/fonts (no off-palette colors)
- [ ] All content is in pt-BR (unless technical docs)
- [ ] No archetype shadow detected (not sacrificing quality for speed)
- [ ] No direct competitor naming (brand_voice_dont)

### Quality Gate — Brand Alignment Score

| Dimension | Weight | Check |
|-----------|--------|-------|
| Voice consistency | 25% | Matches BRAND_VOICE_TONE |
| Visual adherence | 20% | Uses only brand palette/fonts |
| ICP relevance | 20% | Content addresses tutor pain points |
| Value alignment | 20% | Maps to at least 1 Brand Value |
| Pillar balance | 15% | Respects content pillar distribution |

### Competitive Positioning (for strategic dispatch)

| Competitor | Differentiation Angle |
|------------|----------------------|
| CatMyPet | We curate with vet validation; they sell generic |
| Chalesco | We have Ro's education; they have no persona |
| Zee.Dog (gatos) | We are cat-first; they are dog brand with cat line |
| Petlove | We curate; they aggregate everything |

## Cross-References
- GDP protocol → `.claude/rules/guided-decisions.md`
- Dispatch rules → `_spawn/dispatch.sh`
- Brand config (source) → `.cex/brand/brand_config.yaml`
- Brand audit → `python _tools/brand_audit.py`
- Nucleus models → `.cex/config/nucleus_models.yaml`
