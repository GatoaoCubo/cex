# ISO_ANUNCIO_INSTRUCTIONS

**Version**: 1.0.0 | **Quality Target**: 9.0+

## When to Use This Agent

Use anuncio when you need marketplace-ready listing copy for Brazilian e-commerce — titles, keywords, bullets, and descriptions. Handles Mercado Livre, Shopee, Amazon BR, and Magalu formats with ANVISA/INMETRO compliance. Do NOT use for market research (use `pesquisa`), product photography (use `photo`), or paid ad campaigns (use `ads`).

## Execution Steps

1. **Parse product input**: Extract product name, category, key benefits (3-5), technical specifications, and optional research notes from `pesquisa`
2. **Generate 3 title variations**: Each title MUST be:
   - Exactly 58-60 characters (count precisely)
   - Contain 8-10 high-intent keywords
   - ZERO connectors ("de", "para", "com", "e") — they waste characters
3. **Expand keywords into 2 blocks**: Each block MUST have:
   - 115-120 terms (not fewer, not more)
   - Block 2 fully deduplicated from Block 1
   - All lowercase, comma-separated
   - Mix of head terms, long-tail, and regional variations
4. **Write 10 strategic bullets**: Each bullet MUST be:
   - 250-299 characters (not fewer, not more)
   - Structure: Emoji + Benefit + Proof + Mental Trigger
   - Distribute triggers across bullets (scarcity, authority, social proof, urgency, reciprocity)
5. **Write description**: Minimum 3,300 characters using StoryBrand framework:
   - Section 1: Problem (customer pain point)
   - Section 2: Guide (position product as the solution)
   - Section 3: Plan (how to use)
   - Section 4: Benefits (expanded from bullets)
   - Section 5: Specifications (technical details)
   - Section 6: Guarantee (return policy, warranty)
   - Section 7: CTA (clear call-to-action)
6. **Run compliance validation** (11 criteria):
   - Quality (6): title format, keyword count, bullet format, description length, StoryBrand structure, trigger distribution
   - Regulatory (5): no ANVISA-prohibited health claims, no unproven superlatives, INMETRO compliance, marketplace-specific rules, no banned words/phrases
7. **Output as copy-ready markdown**: Single code block format for direct marketplace paste

## Input Requirements

| Field | Type | Required | Example |
|-------|------|----------|---------|
| product_name | string | yes | "Garrafa Termica Inox 500ml" |
| key_benefits | array | yes | ["Mantem temperatura 24h", "Aco inox 304", "Livre de BPA"] |
| specifications | object | no | `{material: "Aco Inox 304", capacity: "500ml", weight: "350g"}` |
| research_notes | markdown | no | Output from pesquisa_agent (22 blocks) |
| context.brand | object | no | Brand guidelines from marca_agent |
| context.marketplace | enum | no | "mercado_livre", "shopee", "amazon_br" |

## Output Format

```markdown
## TITULOS (3 variacoes)
A: Garrafa Termica Inox 500ml Quente Frio 24h Aco 304 BPA Free
B: Garrafa Termica Aco Inox 304 500ml Isolamento 24h Sem BPA
C: Garrafa Inox Termica 500ml 24 Horas Quente Fria Aco 304 BPA

## KEYWORDS BLOCO 1 (115-120 termos)
garrafa termica, garrafa inox, garrafa 500ml, ...

## KEYWORDS BLOCO 2 (115-120 termos)
squeeze termica, copo termico, garrafa agua quente, ...

## BULLETS (10x 250-299 chars)
1. [emoji] Mantem sua bebida na temperatura ideal por 24 horas...
...

## DESCRICAO (3300+ chars)
Voce ja perdeu a paciencia com garrafas que...

## VALIDACAO
- [x] Titulos: 58-60 chars, 0 conectores
- [x] Keywords: 118 + 116 termos
- [x] Bullets: 10x dentro de 250-299 chars
- [x] Descricao: 3,450 chars, StoryBrand completo
- [x] Compliance: ANVISA OK, INMETRO OK
- Quality Score: 8.7/10
```

## Quality Checklist

- [ ] All 3 titles are exactly 58-60 characters (count each one)
- [ ] Zero connectors in titles ("de", "para", "com", "e")
- [ ] Keyword blocks have 115-120 terms each, no overlap between blocks
- [ ] All 10 bullets are 250-299 characters each
- [ ] Description is >= 3,300 characters with all 7 StoryBrand sections
- [ ] No ANVISA-prohibited health claims (e.g., "cura", "trata", "previne")
- [ ] No unproven superlatives without evidence ("melhor do mundo", "unico no mercado")
- [ ] 5D score >= 0.85 overall with all dimensions >= 0.75

## Common Pitfalls

- **Title character count off by 1-2**: Spaces count as characters. Verify with actual char count, not word estimate. "Garrafa Termica" = 17 chars including the space
- **Keyword blocks overlapping**: Block 2 must be 100% deduplicated from Block 1. Use sets to verify zero intersection
- **Bullets too short**: The most common failure. "Feature + benefit" alone = ~150 chars. You need "Emoji + Benefit + Proof + Trigger" to consistently hit 250+
- **Description under 3,300**: Missing the Guarantee or Specifications section is the usual cause. Both are essential for StoryBrand completeness
- **ANVISA violations**: Never claim health benefits for non-health products. "Mantem temperatura" is OK. "Melhora sua saude" is ANVISA violation. When in doubt, use functional language, not health language

## Examples

### Example 1: Complete listing from research
Input: `{product_name: "Whey Protein Isolado 1kg", key_benefits: ["30g proteina por dose", "Baixo lactose", "Sabor chocolate"], research_notes: "pesquisa_output.md"}`
Output: 3 titles (58-60 chars each), 2 keyword blocks (117 + 119 terms), 10 bullets (250-299 chars), description (3,520 chars), compliance 11/11, score 8.9

### Example 2: Quick listing without research
Input: `{product_name: "Fone Bluetooth TWS", key_benefits: ["Cancelamento de ruido", "8h bateria", "IPX5 resistente agua"]}`
Output: 3 titles, 2 keyword blocks, 10 bullets, description (3,380 chars), compliance 10/11 (flagged: needs INMETRO check for electronics), score 8.1
