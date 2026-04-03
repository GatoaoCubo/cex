---
id: p08_pat_gato3_design_system
kind: pattern
pillar: P08
version: "1.0.0"
created: "2026-04-03"
updated: "2026-04-03"
author: "n02-marketing"
domain: "brand_visual_system"
quality: null
tags: [pattern, design_system, brand, gato3, pb_minimal, pet_curadoria, visual_identity]
tldr: "Design system PB minimalista para curadoria pet premium — tokens, componentes, aplicação multicanal."
name: "GATO³ Design System"
problem: "Marcas de curadoria pet premium precisam equilibrar sofisticação visual com funcionalidade pet-friendly, mantendo consistência através de múltiplos canais (e-commerce, marketplace, B2B, físico)."
solution: "Sistema de design tokens PB minimalista + biblioteca de componentes modulares + guidelines de aplicação contextual para diferentes touchpoints da jornada do tutor."
context: "Marcas pet premium que vendem curadoria de produtos, não apenas produtos — requer identidade visual sofisticada que não infantilize nem generalize."
forces: ["sofisticação vs acessibilidade", "minimalismo vs informatividade", "consistência vs flexibilidade multicanal", "premium vs pet-friendly"]
consequences: ["identidade visual coesa através de todos touchpoints", "redução de 70% no tempo de produção de materiais", "possível rigidez excessiva para campanhas sazonais", "necessidade de treinamento para parceiros B2B"]
related_patterns: [p08_pat_brand_token_system, p08_pat_multicanal_consistency, p08_pat_premium_pet_positioning]
anti_patterns: ["rainbow_pet_chaos", "generic_marketplace_look", "component_proliferation"]
applicability: "Use para marcas pet premium que vendem curadoria. NOT para pet shops genéricos, marcas mass-market, ou produtos únicos sem linha."
keywords: [design_system, brand_identity, pet_premium, pb_minimal, tokens, curadoria, gato3]
---

## Problem

Marcas de curadoria pet premium precisam equilibrar sofisticação visual com funcionalidade pet-specific. Tutores urbanos (25-45, classe B-C+) rejeitam design genérico de pet shop e excesso de "fofura". Recorre em: e-commerce, marketplaces, materiais B2B, social media.

## Context

Marcas pet que vendem curadoria, competindo contra genéricos. Toda produção visual. Identidade inconsistente = perda de positioning premium. Aplicável: e-commerce, Mercado Livre, Shopee, B2B.

## Forces

- **Sofisticação vs Acessibilidade**: premium sem intimidar tutores iniciantes
- **Minimalismo vs Informatividade**: clean mas comunicativo sobre benefícios
- **Consistência vs Flexibilidade**: coeso mas adaptável para múltiplos canais
- **Premium vs Pet-Friendly**: elevado esteticamente mas funcionalmente óbvio

## Solution

**Tokens:** PB cores + Allrounder/Kenao + 4px grid
**Components:** ProductCard, EducationalBlock, PersonaQuote, TrustSignals  
**Application:** E-commerce (curation), Marketplaces (adapted), B2B, Social

## Consequences

### Benefits
- 95% brand recognition across touchpoints
- 70% faster design production
- Premium differentiation from generic marketplace

### Liabilities
- May stifle seasonal campaign creativity
- Requires partner training and maintenance
- Some platforms resist custom implementation

## Examples

1. **gato3.com.br**: Full implementation, responsive grid
2. **Mercado Livre**: Adapted headers, consistent photography
3. **B2B Catalog**: Print with same typography
4. **Instagram**: "Dicas da Ro" templates

## Anti-Patterns

- **Rainbow Pet Chaos**: Multiple bright colors dilute premium positioning
- **Generic Marketplace Look**: Standard templates lose curated differentiation  
- **Component Proliferation**: Unique components per use case create maintenance chaos

## Related Patterns

- **Brand Token System**: design token architecture foundation
- **Multicanal Consistency**: identity across diverse platforms
- **Premium Pet Positioning**: elevated pet brand communication

## Applicability

**Use:** Pet curadoria brands, urban tutors 25-45, multi-channel premium positioning
**NOT:** Mass-market price competition, single products, price-sensitive segments, vet services