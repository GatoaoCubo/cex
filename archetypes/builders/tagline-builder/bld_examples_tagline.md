---
id: bld_examples_tagline
kind: examples
pillar: P01
builder: tagline-builder
version: 1.0.0
quality: 9.1
title: "Examples Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: GOVERN
---
# Examples: Tagline Builder

## Example 1: SaaS Developer Tool

**Input**: Brand=CodeForge, Industry=developer-tools, Audience=senior devs, Tone=confident-technical, USP="AI that writes tests before you write code"

**Output**:
```yaml
recommended:
  text: "Tests First. Code Fearless."
  reasoning: "Captures TDD philosophy in brand language. 4 words. Impossible for competitors (they don't do test-first AI). Billboard-ready."
  contexts:
    site_hero: "Tests First. Code Fearless."
    social_bio: "AI that writes your tests before you write code. Tests First."
    ad_headline: "Still writing tests after code? There's a better way."
    email_subject: "What if your tests existed before your code?"
```

## Example 2: Pet Shop Premium (PT-BR)

**Input**: Brand=PetRoyal, Industry=pet-care, Audience=classe A/B donas de pets, Tone=carinhoso-premium, USP="spa e nutricionista for seu pet"

**Output**:
```yaml
recommended:
  text: "Seu pet merece o melhor. Nos sabemos qual."
  reasoning: "Emocional + functional. Implica expertise sem ser arrogante. 9 palavras, tom carinhoso-premium."
variants:
  short:
    - text: "Realeza tem quatro patas."
      approach: aspirational
    - text: "Amor com ciencia."
      approach: functional
  provocative:
    - text: "Raction de supermercado? Seu pet discorda."
      approach: provocative
```

## Anti-Example (what NOT to produce)
```yaml
# BAD: Generic, fits any brand
1. "Inovaction que transforma"        # could be any company
2. "Excelencia em each detalhe"     # zero differentiation
3. "Seu parceiro de confianca"      # meaningless
# BAD: Too long
- "A plataforma complete que integra todas as suas necessidades em um so lugar"  # 13 words, not memorable
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P01 |
| Domain | tagline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
