# HOP: Bullet Points | anuncio_agent v4.0.0

**Step**: 4 of 7
**Purpose**: Generate 10 benefit-first bullet points
**Input**: `{parsed_input, titulos, keywords}` from Steps 1+2+3
**Output**: `{bullets[10]}`

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

Generate 10 compelling bullet points with:
- 250-299 characters EACH
- Benefit-first structure
- Natural keyword integration
- Mental triggers incorporated (min 5 across all)

---

## RULES (CRITICAL)

### Character Limits
```yaml
per_bullet:
  minimum: 250
  maximum: 299
  tolerance: 0
  action_if_wrong: auto_adjust
```

### Structure: Benefit-First
```yaml
pattern: "[BENEFICIO]: [Feature/especificacao] que [valor para cliente]"

examples:
  GOOD: "ENERGIA DURADOURA: Formula de liberacao gradual que mantem disposicao por ate 6 horas sem picos ou quedas de energia"
  BAD: "Contem formula de liberacao gradual para energia"

key_principle: "Lead with what the customer GETS, not what the product HAS"
```

### Mental Triggers (min 5 total)
```yaml
required_triggers: 5
available:
  - social_proof: "Mais de X clientes", "Avaliado com X estrelas"
  - authority: "Desenvolvido por especialistas", "Certificado ANVISA"
  - specificity: "27g de proteina", "90% de absorcao"
  - scarcity: "Edicao limitada" (only if REAL)
  - guarantee: "Garantia de satisfacao"
  - reciprocity: "Brinde incluso"
  - urgency: "Promocao valida ate" (only if REAL)
  - exclusivity: "Formula exclusiva"
  - curiosity: "Descubra como"
  - fear_of_loss: "Nao perca ganhos"
```

### Formatting
```yaml
bullet_symbol: "-" or none
emoji: NOT allowed
caps: Only for trigger word (e.g., "ENERGIA DURADOURA:")
paragraph: Single paragraph per bullet
```

---

## EXECUTION

### Step 4.1: Extract Features from Input
```python
features = []

# From parsed_input.features
if parsed_input.features:
    features.extend(parsed_input.features)

# From product_name (extract specs)
specs = extract_specs_from_name(parsed_input.product_name)
features.extend(specs)

# From research notes (if pesquisa_agent source)
if parsed_input.source_type == "pesquisa_agent":
    features.extend(extract_from_research(parsed_input))
```

### Step 4.2: Transform Features to Benefits
```yaml
transformation_rules:
  feature: "27g de proteina por dose"
  benefit: "MAXIMO GANHO MUSCULAR: 27g de proteina isolada por dose que garante a quantidade ideal para hipertrofia"

  feature: "Zero lactose"
  benefit: "CONFORTO DIGESTIVO: Formula sem lactose que evita desconfortos e permite consumo mesmo por intolerantes"

  feature: "Sabor chocolate"
  benefit: "SABOR IRRESISTIVEL: Chocolate suico premium que transforma seu shake em momento de prazer apos treino"
```

### Step 4.3: Assign Mental Triggers
```python
triggers_distribution = {
    "bullet_1": "specificity",      # Lead with numbers
    "bullet_2": "authority",        # Credibility
    "bullet_3": "social_proof",     # Others trust it
    "bullet_4": "specificity",      # More numbers
    "bullet_5": "exclusivity",      # Unique value
    "bullet_6": "guarantee",        # Risk reversal
    "bullet_7": "specificity",      # Technical detail
    "bullet_8": "curiosity",        # Engagement
    "bullet_9": "fear_of_loss",     # Motivation
    "bullet_10": "reciprocity"      # Added value
}
```

### Step 4.4: Integrate Keywords Naturally
```yaml
integration_rules:
  - Place keyword within natural sentence flow
  - Avoid keyword stuffing
  - Use variations when repeating
  - Prioritize readability over SEO

example:
  keywords: ["whey protein", "proteina isolada", "hipertrofia"]
  bullet: "HIPERTROFIA ACELERADA: Proteina isolada de alta pureza que fornece aminoacidos essenciais para maximo ganho de massa muscular"
  keywords_used: ["proteina isolada", "hipertrofia"]
```

### Step 4.5: Validate Character Count
```python
def adjust_bullet(bullet, target_min=250, target_max=299):
    char_count = len(bullet)

    if char_count < target_min:
        # Expand with more detail
        bullet = expand_with_detail(bullet)

    if char_count > target_max:
        # Trim non-essential words
        bullet = trim_to_fit(bullet, target_max)

    return bullet
```

---

## OUTPUT FORMAT

```json
{
  "bullets": [
    {
      "number": 1,
      "text": "MAXIMO GANHO MUSCULAR: 27g de proteina isolada por dose que fornece a quantidade exata de aminoacidos para estimular sintese proteica e hipertrofia apos seus treinos mais intensos",
      "chars": 275,
      "trigger": "specificity",
      "keywords_used": ["proteina isolada", "hipertrofia", "aminoacidos"],
      "benefit_focus": "muscle_gain"
    },
    {
      "number": 2,
      "text": "DESENVOLVIDO POR ESPECIALISTAS: Formula criada por nutricionistas esportivos com mais de 15 anos de experiencia em suplementacao para atletas profissionais e amadores",
      "chars": 268,
      "trigger": "authority",
      "keywords_used": ["suplementacao", "atletas"],
      "benefit_focus": "credibility"
    }
  ],
  "metadata": {
    "all_valid": true,
    "triggers_used": ["specificity", "authority", "social_proof", "exclusivity", "guarantee"],
    "triggers_count": 5,
    "keywords_integrated": 18,
    "avg_chars": 270
  }
}
```

---

## BULLET TEMPLATES

### Template 1: Specificity (Numbers)
```
[NUMERO] [UNIDADE] DE [FEATURE]: [Especificacao tecnica] que [resultado mensuravel para cliente] em [tempo ou condicao]
```

### Template 2: Authority
```
[CREDENCIAL]: [Quem desenvolveu/aprovou] com [qualificacao] que [garantia de qualidade]
```

### Template 3: Social Proof
```
[EVIDENCIA SOCIAL]: [Quantidade] de [grupo] que [acao positiva] pela [razao] e [resultado]
```

### Template 4: Benefit-Feature
```
[BENEFICIO EM CAPS]: [Feature especifica] que [transformacao para cliente] permitindo [resultado desejado]
```

### Template 5: Problem-Solution
```
[PROBLEMA RESOLVIDO]: [Solucao oferecida] que [elimina dor do cliente] para [estado desejado]
```

---

## EXAMPLES (COMPLETE)

### 10 Bullets for Whey Protein

```
1. MAXIMO GANHO MUSCULAR: 27g de proteina isolada de alta pureza por dose que fornece aminoacidos essenciais para estimular sintese proteica e acelerar hipertrofia em cada treino (265 chars)

2. DESENVOLVIDO POR ESPECIALISTAS: Formula criada por nutricionistas esportivos certificados com 15 anos de experiencia em suplementacao para atletas que buscam resultados reais (263 chars)

3. MAIS DE 50.000 CLIENTES SATISFEITOS: Avaliado com 4.9 estrelas por praticantes de musculacao que comprovaram ganhos visiveis de massa magra em apenas 30 dias de uso consistente (270 chars)

4. ABSORCAO ULTRA RAPIDA: Tecnologia de hidrolise que permite absorcao em ate 30 minutos pos-treino garantindo que seus musculos recebam nutrientes no momento mais critico (265 chars)

5. EXCLUSIVO SABOR CHOCOLATE SUICO: Formula importada com cacau premium que transforma seu shake em momento de prazer sem abrir mao de zero acucar e apenas 120 calorias por dose (268 chars)

6. GARANTIA TOTAL DE SATISFACAO: Se voce nao sentir diferenca em 30 dias devolvemos seu dinheiro sem perguntas porque confiamos na qualidade superior do nosso whey protein (261 chars)

7. RENDIMENTO DE 33 DOSES POR POTE: Cada pote de 1kg oferece mais de um mes de suplementacao diaria com custo por dose muito abaixo da media do mercado de whey protein importado (267 chars)

8. DESCUBRA O SEGREDO DOS CAMPEOES: A mesma proteina utilizada por atletas profissionais agora acessivel para voce alcancar o fisico dos seus sonhos com dedicacao e consistencia (269 chars)

9. NAO PERCA SEUS GANHOS NOTURNOS: Formula de liberacao gradual que mantem fluxo de aminoacidos durante o sono evitando catabolismo e potencializando recuperacao muscular completa (272 chars)

10. BRINDE EXCLUSIVO NA PRIMEIRA COMPRA: Coqueteleira profissional de 600ml com sistema anti-vazamento inclusa para voce preparar seu shake com praticidade em qualquer lugar (262 chars)
```

---

## VALIDATION CHECKLIST

Before outputting:
- [ ] Exactly 10 bullets
- [ ] All between 250-299 chars
- [ ] All start with benefit (CAPS:)
- [ ] At least 5 different mental triggers
- [ ] Keywords integrated naturally
- [ ] No emojis
- [ ] No prohibited claims (ANVISA)

---

**Next Step**: Pass `{bullets}` to `prompts/descricao_builder.md`
