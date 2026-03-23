# MARCA Agent - Quick Start

> **Time to deploy**: 2 minutes
> **For**: External LLMs (ChatKit, OpenAI, Claude)

---

## What is MARCA Agent?

Brand strategy agent that creates comprehensive Brazilian e-commerce brand identities using the **32-Block Framework**:

- **Section 1**: Brand Identity (names, taglines, archetype, traits, essence)
- **Section 2**: Positioning (UVP, segment, differentiation, promise)
- **Section 3**: Tone of Voice (dimensions, style, do's/don'ts, phrases)
- **Section 4**: Visual Identity (colors, typography, mood board)
- **Section 5**: Brand Narrative (origin, mission, vision, values, manifesto)
- **Section 6**: Brand Guidelines (messaging rules, compliance)
- **Section 7**: Validation (consistency, uniqueness, audit)

---

## Quick Commands

```
/marca {brand_brief}           -> Full 32-block brand strategy
/marca-identity {brief}        -> Section 1 only (blocks 1-5)
/marca-positioning {brief}     -> Section 2 only (blocks 6-10)
/marca-voice {brief}           -> Section 3 only (blocks 11-15)
```

---

## Input Format (Minimal)

```json
{
  "product_name": "Cosmeticos Organicos para Pele Sensivel",
  "category": "Beleza > Cosmeticos Naturais",
  "target_audience": "Mulheres 25-40, conscientes, urbanas",
  "price_range": "Premium (R$ 80-200)"
}
```

---

## Input Format (Full)

```json
{
  "product_name": "Cosmeticos Organicos para Pele Sensivel",
  "category": "Beleza > Cosmeticos Naturais",
  "target_audience": "Mulheres 25-40, conscientes, urbanas",
  "price_range": "Premium (R$ 80-200)",
  "competitors": ["Natura", "Granado", "Simple Organic"],
  "inspirations": ["Aesop", "Glossier"],
  "product_category": "cosmetics"
}
```

---

## Output Summary

```yaml
decision: COMPLETE | PARTIAL
blocks_completed: 32/32
consistency_score: 0.92
uniqueness_score: 8.7/10

sections:
  identity: 5/5 blocks
  positioning: 5/5 blocks
  voice: 5/5 blocks
  visual: 4/4 blocks
  narrative: 5/5 blocks
  guidelines: 4/4 blocks
  validation: 4/4 blocks
```

---

## 12 Brand Archetypes Reference

| Archetype | Core Desire | Example Brands |
|-----------|-------------|----------------|
| Innocent | Simplicidade | Dove, Natura |
| Explorer | Liberdade | Jeep, North Face |
| Sage | Conhecimento | Google, BBC |
| Hero | Maestria | Nike, BMW |
| Outlaw | Libertacao | Harley-Davidson, Virgin |
| Magician | Transformacao | Apple, Tesla |
| Everyman | Pertencimento | IKEA, Havaianas |
| Lover | Intimidade | Chanel, Haagen-Dazs |
| Jester | Diversao | M&Ms, Old Spice |
| Caregiver | Protecao | J&J, Pampers |
| Creator | Inovacao | LEGO, Adobe |
| Ruler | Controle | Rolex, Mercedes |

---

## Quality Thresholds

| Metric | Threshold | Action if Fail |
|--------|-----------|----------------|
| Consistency Score | >= 0.85 | Revise archetype/voice alignment |
| Uniqueness Score | >= 8.0/10 | Strengthen differentiation |
| WCAG Compliance | Level AA | Adjust color contrast |
| Tagline Length | 40-60 chars | Compress/expand tagline |

---

## Example

**Input**:
```
Create brand strategy for: "Garrafa Termica Premium"
Category: Casa > Utensilios
Audience: Profissionais urbanos 25-45
Price: Premium (R$ 150-300)
```

**Output** (summarized):
```
Brand Names:
- Descriptive: ThermoFlow
- Evocative: Constante
- Creative: Hidravita

Tagline: "24 horas de temperatura perfeita para sua rotina" (51 chars)

Archetype: Explorer (primary) + Sage (secondary)
- Justification: Explorer = adventure/outdoor; Sage = tech expertise

Personality: Confiavel, Pratica, Duravel, Aventureira, Sustentavel

Positioning: Para profissionais que nao abrem mao de qualidade,
[BRAND] e a garrafa termica que mantém temperatura por 24h
porque performance constante e o novo padrao de hidratacao.
```

---

## Next Steps

1. Read `instructions.md` for full operation guide
2. Review `output_template.md` for complete 32-block format
3. Check `data/input_schema.yaml` for validation rules

---

*MARCA Agent Quick Start v1.0.0*
