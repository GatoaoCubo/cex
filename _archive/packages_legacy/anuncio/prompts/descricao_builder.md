# HOP: Descricao Builder | anuncio_agent v4.0.0

**Step**: 5 of 7
**Purpose**: Build comprehensive product description
**Input**: `{parsed_input, titulos, keywords, bullets}` from ALL previous steps
**Output**: `{descricao}`

---

## WORKFLOW ROUTES (Confidence-Based Behavior)

| Route | Confidence | Behavior |
|-------|------------|----------|
| Full Generation | >=0.80 | Generate without markers |
| With Suggestions | 0.60-0.79 | Add [VERIFICAR] markers |
| Partial | 0.40-0.59 | Add [COMPLETAR] markers |
| Request Enrichment | <0.40 | Stop and request more info |

---

## TASK

Build a comprehensive product description with:
- Minimum 3300 characters
- StoryBrand 7-part framework
- Mobile-first formatting
- Natural keyword integration
- Compliance verified

---

## RULES

### Character Requirements
```yaml
minimum: 3300
maximum: null (no upper limit, but aim for 3500-4500)
quality_threshold: "readable, not padded"
```

### StoryBrand Framework (7 Parts)
```yaml
structure:
  1_hero: "O cliente e o heroi da historia"
  2_problem: "O problema/vilao que ele enfrenta"
  3_guide: "A marca como guia experiente"
  4_plan: "Passos claros para sucesso"
  5_call_to_action: "CTA direto"
  6_success: "Visao do sucesso"
  7_failure: "O que evitar"

flow: "Connect emotionally -> Establish credibility -> Drive action"
```

### Mobile-First Formatting
```yaml
paragraph_max_lines: 4
line_max_chars: 80
use_headers: true
use_bold: true (for emphasis)
use_lists: true (for scannability)
emoji: NOT allowed
html: NOT allowed (plain text)
```

---

## EXECUTION

### Step 5.1: Structure with StoryBrand

#### Section 1: HERO (The Customer)
```markdown
## Voce Merece Resultados Reais

Voce treina duro, se dedica, acorda cedo, faz sacrificios...
Mas os resultados parecem demorar a aparecer?

[Connect with customer's desire and struggle]
[~400-500 chars]
```

#### Section 2: PROBLEM (The Villain)
```markdown
## O Desafio Que Todo Praticante Enfrenta

O mercado esta cheio de suplementos que prometem muito
e entregam pouco. Formulas cheias de aditivos, sabores
artificiais, e proteinas de baixa qualidade que seu corpo
mal consegue absorver.

[Articulate the frustration they feel]
[~400-500 chars]
```

#### Section 3: GUIDE (The Brand)
```markdown
## Nossa Historia

Criado por nutricionistas esportivos com mais de 15 anos
de experiencia, [Produto] nasceu da insatisfacao com o
que existia no mercado brasileiro.

[Establish credibility and empathy]
[~400-500 chars]
```

#### Section 4: PLAN (Clear Steps)
```markdown
## Simples de Usar

1. Adicione 1 scoop (30g) em 200ml de agua ou leite
2. Misture por 30 segundos ate ficar homogeneo
3. Consuma em ate 30 minutos pos-treino

[Clear, actionable steps]
[~300-400 chars]
```

#### Section 5: CALL TO ACTION
```markdown
## Comece Sua Transformacao Hoje

Adicione ao carrinho agora e receba em casa com total
seguranca. Pagamento facilitado em ate 12x sem juros.

[Direct, clear CTA]
[~200-300 chars]
```

#### Section 6: SUCCESS (The Vision)
```markdown
## Imagine Seus Resultados

Em poucas semanas voce vai notar:
- Mais energia durante os treinos
- Recuperacao muscular acelerada
- Ganhos visiveis de massa magra
- Confianca ao olhar no espelho

[Paint the picture of success]
[~400-500 chars]
```

#### Section 7: FAILURE (What to Avoid)
```markdown
## Nao Deixe Para Depois

Cada dia sem suplementacao adequada e um dia de treino
que nao rende o maximo. Seus musculos precisam de
proteina de qualidade para crescer.

[Subtle urgency without manipulation]
[~300-400 chars]
```

### Step 5.2: Integrate Previous Elements

```python
# From titulos
title_keywords = extract_keywords(titulos)

# From keywords
keyword_list = keywords[0].terms + keywords[1].terms

# From bullets
bullet_benefits = [b.benefit_focus for b in bullets]

# Integration strategy
# - Use title keywords in headers
# - Sprinkle keyword_list naturally throughout
# - Reference bullet benefits in relevant sections
```

### Step 5.3: Add Product Details

```markdown
## Informacoes Tecnicas

**Composicao por Dose (30g):**
- Proteina: 27g
- Carboidratos: 2g
- Gorduras: 1g
- Calorias: 120kcal

**Ingredientes:** Proteina isolada do soro do leite,
cacau em po, aroma natural de chocolate, sucralose.

[Technical details for informed buyers]
[~400-500 chars]
```

### Step 5.4: Validate and Format

```python
def format_description(text):
    # Split into paragraphs
    paragraphs = text.split('\n\n')

    # Ensure no paragraph > 4 lines
    formatted = []
    for p in paragraphs:
        if len(p.split('\n')) > 4:
            p = split_long_paragraph(p)
        formatted.append(p)

    return '\n\n'.join(formatted)

def validate_description(text):
    assert len(text) >= 3300, f"Too short: {len(text)} chars"
    assert '##' in text, "Missing headers"
    # Check for prohibited claims
    check_compliance(text)
    return True
```

---

## OUTPUT FORMAT

```json
{
  "descricao": {
    "full_text": "[Complete description text]",
    "char_count": 3450,
    "sections": [
      {"name": "hero", "chars": 450},
      {"name": "problem", "chars": 480},
      {"name": "guide", "chars": 420},
      {"name": "plan", "chars": 350},
      {"name": "cta", "chars": 280},
      {"name": "success", "chars": 470},
      {"name": "failure", "chars": 350},
      {"name": "technical", "chars": 450}
    ],
    "keywords_integrated": 28,
    "compliance": {
      "anvisa_passed": true,
      "inmetro_passed": true,
      "prohibited_terms_found": []
    },
    "formatting": {
      "headers_count": 8,
      "paragraphs_count": 15,
      "avg_paragraph_lines": 3.2,
      "mobile_friendly": true
    }
  }
}
```

---

## COMPLETE EXAMPLE

```markdown
## Voce Merece Resultados de Verdade

Voce acorda cedo, treina pesado, se dedica todos os dias.
Faz dieta, controla macros, dorme bem. Mas parece que os
resultados demoram mais do que deveriam?

Voce nao esta sozinho. Milhares de praticantes de musculacao
enfrentam o mesmo desafio: encontrar um suplemento que
realmente faz diferenca.

---

## O Problema Com a Maioria dos Suplementos

O mercado brasileiro esta inundado de whey proteins que
prometem mundos e fundos. Formulas cheias de maltodextrina,
sabores artificiais, e proteina de baixa biodisponibilidade.

Voce paga caro e seu corpo absorve apenas uma fracao.
O resultado? Frustracao e dinheiro jogado fora.

---

## Por Que Criamos Este Whey Protein

Nossa equipe de nutricionistas esportivos, com mais de 15
anos de experiencia, estava cansada de ver atletas
desapontados.

Decidimos criar o suplemento que gostariamos de usar:
proteina isolada de alta pureza, sem aditivos desnecessarios,
com sabor que da prazer beber.

Cada lote e testado em laboratorio independente para
garantir 27g de proteina real por dose.

---

## Como Usar

E simples:

1. Adicione 1 scoop (30g) em 200ml de agua gelada ou leite
2. Misture vigorosamente por 30 segundos
3. Consuma em ate 30 minutos apos o treino

Para melhores resultados, mantenha consistencia diaria.

---

## Comece Sua Transformacao Hoje

Clique em "Comprar Agora" e receba em casa com toda
seguranca. Pagamento facilitado em ate 12x sem juros
no cartao. Frete gratis para compras acima de R$ 150.

---

## Imagine Seus Proximos 30 Dias

Com suplementacao adequada, voce vai notar:

- Mais disposicao durante treinos intensos
- Recuperacao muscular mais rapida entre sessoes
- Ganhos visiveis de massa magra
- Aquela satisfacao ao ver o progresso no espelho

Nao e magica. E ciencia aplicada com consistencia.

---

## Nao Deixe Para Amanha

Cada treino sem proteina adequada e uma oportunidade
perdida de crescimento. Seus musculos precisam de
aminoacidos de qualidade para reparar e crescer.

Quanto mais cedo comecar, mais rapido vera resultados.

---

## Especificacoes Tecnicas

**Por Dose (30g):**
- Proteina: 27g (90% de pureza)
- Carboidratos: 2g
- Gorduras: 1g
- Calorias: 120kcal

**Ingredientes:** Whey protein isolado, cacau em po,
aroma natural, edulcorante sucralose.

**Porcoes por Embalagem:** 33 doses (1kg)

**Registro:** Produto isento de registro conforme
RDC 27/2010 - ANVISA

---

**Conservacao:** Manter em local fresco e seco.
Apos aberto, consumir em ate 60 dias.
```

---

## VALIDATION CHECKLIST

Before outputting:
- [ ] Minimum 3300 characters
- [ ] All 7 StoryBrand sections present
- [ ] Headers used for structure
- [ ] Paragraphs max 4 lines
- [ ] Keywords integrated naturally
- [ ] No ANVISA violations
- [ ] Mobile-friendly format
- [ ] No emojis or HTML

---

**Next Step**: Pass `{descricao}` to `prompts/qa_validation.md`
