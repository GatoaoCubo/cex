---
id: bld_quality_gate_tagline
kind: quality_gate
pillar: P07
builder: tagline-builder
version: 1.0.0
quality: 9.1
title: "Quality Gate Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: GOVERN
related:
  - bld_examples_tagline
  - bld_instruction_tagline
  - bld_system_prompt_tagline
  - bld_schema_tagline
  - bld_output_template_tagline
  - tagline-builder
  - bld_config_tagline
  - bld_tools_tagline
  - bld_architecture_tagline
  - kc_tagline
---

## Quality Gate

# Quality Gate: Tagline Builder

## HARD gates (must pass or artifact is rejected)
1. H01: Frontmatter has id, kind, title, version, created, quality:null
2. H02: At least 5 variants across 3+ approaches
3. H03: Recommended tagline has reasoning
4. H04: No variant exceeds 15 words
5. H05: Recommended tagline passes competitor-swap test (stated explicitly)

## SOFT gates (warnings, not blockers)
1. S01: Short/medium/long variants present (all 3 lengths)
2. S02: Context adaptations for at least 3 contexts
3. S03: USP extracted and stated
4. S04: Language consistent throughout (no PT/EN mixing unless bilingual brand)
5. S05: Score breakdown present for top variants
6. S06: Emotional + functional approaches both represented

## Scoring Rubric
| Dimension | Weight | 10/10 means |
|-----------|--------|-------------|
| Memorability | 25% | Recalled unprompted after 24h |
| Differentiation | 25% | Could NOT be used by any competitor |
| Clarity | 20% | Understood in 3 seconds (billboard test) |
| Emotional Impact | 15% | Triggers specific feeling in target audience |
| Versatility | 15% | Works across hero, social, email, ad, pitch |

## Scoring Command

```bash
python _tools/cex_score.py --apply --verbose target.md
```

```bash
python _tools/cex_score.py --apply N0*/*.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `quality_gate` |
| Pillar | P07 |
| Domain | tagline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
