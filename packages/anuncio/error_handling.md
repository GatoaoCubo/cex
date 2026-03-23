# ANUNCIO Agent Error Handling

**Version**: 1.0.0 | **Type**: Failure Modes & Recovery | **Quality**: >= 8.5

---

## TOP 5 FAILURE MODES

### 1. Missing Product Data (Input Incomplete)

**Symptom**: Agent receives input with only product_name, missing category/features/benefits

**Root Cause**: User provides minimal data expecting agent to "figure it out"

**Impact**: Low-quality output, generic copy, poor keyword selection, compliance risk

**Detection**:
```python
confidence_score = calculate_input_confidence(input_data)
if confidence_score < 0.40:
    trigger_enrichment_request()
```

**Recovery Steps**:

```yaml
step_1_assess:
  - Calculate confidence score based on field completeness
  - Identify critical missing fields (category, head_terms, features)
  - Determine if can proceed with fallback or must request data

step_2_fallback_strategy:
  if confidence >= 0.40 and confidence < 0.70:
    action: Generate with caveats
    output: Include warning that more data improves quality
    quality_gate: Flag as "needs_review"

  if confidence < 0.40:
    action: Request enrichment
    output: List specific missing fields
    halt: Do not generate until minimum data provided

step_3_enrichment_request:
  message: |
    Para gerar um anuncio de alta qualidade, preciso de mais informacoes:

    CRITICO (obrigatorio):
    - Categoria completa (ex: Suplementos > Proteinas > Whey)
    - Principais beneficios do produto (minimo 3)

    RECOMENDADO (melhora resultado):
    - Especificacoes tecnicas (tamanho, peso, material, etc)
    - Faixa de preco (minimo e maximo)
    - Palavras-chave principais (head terms)
    - Publico-alvo (demografia e dores)

    Com estes dados, posso gerar titulos mais precisos, keywords mais relevantes,
    e copy mais persuasivo.

step_4_partial_generation:
  if user_insists_on_proceeding:
    - Generate with available data
    - Use category inference from product name
    - Apply generic benefit templates
    - Flag output with quality warnings
    - Document assumptions made
```

**Prevention**:
- Validate input schema before processing
- Provide input template/checklist
- Integrate with pesquisa agent for auto-enrichment

---

### 2. Category Mismatch (Wrong Marketplace Category)

**Symptom**: Product placed in wrong category (Air Fryer in "Beleza" instead of "Eletrodomesticos")

**Root Cause**: User error, poor category understanding, ambiguous products

**Impact**: Wrong keywords generated, poor SEO, wrong buyer persona, low conversion

**Detection**:
```python
category_confidence = validate_category_match(product_name, declared_category)
if category_confidence < 0.60:
    trigger_category_review()
```

**Recovery Steps**:

```yaml
step_1_detect:
  - Compare product_name keywords against category taxonomy
  - Check for semantic mismatch (food terms in electronics category)
  - Calculate confidence score for category fit

step_2_suggest_correction:
  if mismatch_detected:
    message: |
      ALERTA: Possivel incompatibilidade de categoria

      Produto: [product_name]
      Categoria declarada: [declared_category]
      Categoria sugerida: [suggested_category]

      Motivo: [explanation]

      Deseja usar a categoria sugerida? (S/N)

      Impacto de categoria errada:
      - Keywords irrelevantes (baixo trafego)
      - Publico errado vendo anuncio (baixa conversao)
      - Possivel rejeicao pelo marketplace

step_3_user_decision:
  if user_accepts_suggestion:
    - Update category to suggested
    - Regenerate keywords for new category
    - Adjust buyer persona assumptions

  if user_rejects_suggestion:
    - Document override in metadata
    - Proceed with declared category
    - Add quality warning to output
    - Flag for manual review

step_4_ambiguous_products:
  examples:
    - "Oleo de Coco" -> Alimentos OU Cosmeticos?
    - "Relogio Inteligente" -> Eletronicos OU Esportes?
    - "Vitamina D" -> Suplementos OU Farmacia?

  resolution:
    - Ask user for intended use case
    - Check marketplace-specific rules
    - Generate separate versions if needed
```

**Prevention**:
- Validate category against marketplace taxonomy
- Show category tree for user selection
- Use pesquisa agent to confirm category placement

---

### 3. Character Limits Exceeded (Format Violations)

**Symptom**: Generated title 65 chars (should be 58-60), bullet 310 chars (should be 250-299)

**Root Cause**: Complex product names, verbose descriptions, translation expansions

**Impact**: Marketplace rejects listing, manual editing required, delay in publication

**Detection**:
```python
validation_results = validate_output_format(generated_output)
if validation_results.has_violations:
    trigger_auto_fix()
```

**Recovery Steps**:

```yaml
step_1_validate:
  rules:
    titles: 58-60 chars (strict)
    keywords_block: 115-120 terms (strict)
    bullets: 250-299 chars EACH (strict)
    description: >= 3300 chars (minimum)
    conectores: ZERO in titles (strict)

step_2_auto_fix:
  title_too_long:
    - Remove conectores first (de, para, com, e)
    - Replace long words with abbreviations (Profissional -> Pro)
    - Remove redundant adjectives (Produto -> remove)
    - Reorder to prioritize keywords
    - Regenerate if still exceeds limit

  title_too_short:
    - Add high-value keywords from head_terms
    - Expand product attributes (Preto -> Preto Fosco)
    - Include key specs (5L -> 5 Litros)

  bullet_too_long:
    - Split compound sentences
    - Remove filler words (muito, realmente, verdadeiramente)
    - Condense examples (multiple -> single best example)
    - Remove redundant phrases

  bullet_too_short:
    - Add social proof (50 mil clientes)
    - Include specific numbers (68% reducao)
    - Add benefit amplification (economiza E acelera)
    - Extend with warranty/guarantee info

  keywords_insufficient:
    - Generate longtail variations (whey -> whey protein isolado)
    - Add regional terms (Brasil, brasileiro, nacional)
    - Include use case keywords (pos treino, ganho massa)
    - Add marketplace-specific terms

step_3_validate_again:
  - Run format validation on fixed output
  - Ensure all rules now compliant
  - If still failing, regenerate from scratch
  - Maximum 3 fix attempts before escalation

step_4_quality_check:
  - Verify fixes didn't harm persuasion quality
  - Ensure keywords still relevant
  - Check bullets still benefit-first
  - Confirm StoryBrand structure intact
```

**Prevention**:
- Template generation with char counters
- Real-time length validation during generation
- Pre-validate against marketplace-specific limits

---

### 4. Compliance Issues (Prohibited Claims)

**Symptom**: Copy includes "melhor do mundo", "cura diabetes", "garantido" without proof

**Root Cause**: Aggressive persuasion, translated templates, lack of regulatory awareness

**Impact**: ANVISA violation, marketplace rejection, legal liability, brand damage

**Detection**:
```python
compliance_violations = check_compliance_rules(generated_copy)
if compliance_violations:
    trigger_compliance_fix()
```

**Recovery Steps**:

```yaml
step_1_detect_violations:
  prohibited_patterns:
    superlatives_unproven:
      - "melhor do mundo"
      - "numero 1"
      - "unico"
      - "milagroso"

    health_claims_anvisa:
      - "cura [doenca]"
      - "trata [condicao]"
      - "previne [doenca]"
      - "elimina [sintoma]"

    false_guarantees:
      - "resultado garantido"
      - "100% eficaz"
      - "nunca falha"

    time_pressure_excessive:
      - "ultima unidade"
      - "nunca mais tera chance"
      - "preco nunca mais"

    comparison_unfair:
      - "melhor que [marca]"
      - "[marca] e inferior"

step_2_auto_fix:
  replace_superlatives:
    before: "o melhor whey do mundo"
    after: "whey premium com alta concentracao de proteina"

    before: "milagroso para pele"
    after: "eficaz para uniformizar tom da pele"

  soften_health_claims:
    before: "cura acne"
    after: "ajuda a reduzir aparencia de acne"

    before: "elimina rugas"
    after: "suaviza visivelmente linhas de expressao"

  add_disclaimers:
    weight_loss: "Associado a dieta equilibrada e exercicios"
    results: "Resultados variam conforme pessoa e uso correto"
    health: "Nao substitui orientacao medica profissional"

  moderate_urgency:
    before: "ultima unidade NUNCA MAIS"
    after: "estoque limitado neste lote promocional"

step_3_compliance_checklist:
  anvisa_rules:
    - No health cure claims for supplements/cosmetics
    - Include disclaimers for weight loss products
    - State "nao substitui alimentacao" for supplements

  inmetro_rules:
    - Include technical specs for electronics
    - Show certification number if required
    - Voltage/power clearly stated

  marketplace_rules:
    mercado_livre:
      - No external links in description
      - Price match claims prohibited
      - Authenticity guarantees required for brands

    shopee:
      - No competitor mentions
      - Influencer claims need proof
      - Free shipping claims must be accurate

  conar_guidelines:
    - No misleading before/after without disclosure
    - Celebrity endorsements need authorization
    - Child-targeted ads have special rules

step_4_escalate_if_unresolvable:
  if violations_persist_after_fixes:
    action: Flag for human review
    message: |
      ALERTA DE COMPLIANCE

      Nao foi possivel gerar copy 100% compliance-compliant com os dados fornecidos.

      Violacoes detectadas:
      [list_violations]

      Opcoes:
      1. Ajustar dados de entrada (remover claims proibidos)
      2. Aceitar output com avisos (revisar manualmente)
      3. Consultar juridico/compliance antes de publicar
```

**Prevention**:
- Pre-validate input against prohibited terms
- Use compliance database updated with regulations
- Flag high-risk categories (health, supplements) for extra review

---

### 5. Quality Below Threshold (Score < 8.0)

**Symptom**: Output generated but 5D validation score is 6.5 (below pool threshold)

**Root Cause**: Poor input data, weak keywords, generic templates, rushed generation

**Impact**: Low conversion, poor SEO, brand damage, customer complaints

**Detection**:
```python
quality_score = calculate_5d_score(output)
if quality_score < 8.0:
    trigger_quality_improvement()
```

**Recovery Steps**:

```yaml
step_1_diagnose:
  dimensions:
    titulo_score:
      if < 7.5:
        issues:
          - Keywords not compelling
          - Length not optimal
          - Conectores present
        fix: Regenerate with stronger head_terms

    keywords_score:
      if < 7.5:
        issues:
          - Insufficient count
          - Low intent keywords
          - Duplicates between blocks
        fix: Expand with longtail + regional variations

    bullets_score:
      if < 7.5:
        issues:
          - Too short or too long
          - Missing mental triggers
          - Weak benefit statements
        fix: Add social proof + specific numbers + urgency

    description_score:
      if < 7.5:
        issues:
          - Too short (< 3300 chars)
          - Missing StoryBrand elements
          - Weak CTA
        fix: Expand sections + strengthen emotional appeal

    compliance_score:
      if < 7.5:
        issues:
          - Prohibited claims present
          - Missing certifications
          - Unclear disclaimers
        fix: Apply compliance fixes + add disclaimers

step_2_iterative_improvement:
  max_iterations: 3
  strategy:
    iteration_1:
      - Fix lowest scoring dimension first
      - Regenerate that section only
      - Validate improvement

    iteration_2:
      - Fix second lowest dimension
      - Ensure fixes don't conflict
      - Re-validate all dimensions

    iteration_3:
      - Global optimization pass
      - Balance all dimensions
      - Final compliance check

step_3_fallback_strategies:
  if_still_below_8_after_iterations:
    option_a_request_better_data:
      message: |
        Qualidade do anuncio esta abaixo do ideal (score: [X.X]).

        Para melhorar, forneca:
        - Diferenciais unicos do produto
        - Provas sociais (numero de clientes, avaliacoes)
        - Especificacoes tecnicas mais detalhadas
        - Certificacoes e garantias

    option_b_flag_for_review:
      message: |
        Anuncio gerado mas requer revisao manual.

        Score atual: [X.X] (ideal: >= 8.0)

        Pontos fracos:
        [list_weak_dimensions]

        Sugestoes de melhoria:
        [specific_recommendations]

    option_c_delegate_to_specialist:
      if category_requires_expertise:
        examples:
          - Suplementos -> Requires nutrition knowledge
          - Eletronicos -> Requires tech specs expertise
          - Cosmeticos -> Requires ingredient knowledge
        action: Suggest consulting specialist or using pesquisa agent

step_4_quality_gates:
  experimental: 7.0 <= score < 8.0
    - Output with warnings
    - Flag for improvement
    - Document known issues

  pool_ready: score >= 8.0
    - Production quality
    - Safe to publish
    - Add to golden examples if >= 9.5

  rejected: score < 7.0
    - Do not output
    - Force regeneration or data enrichment
    - Block publication until fixed
```

**Prevention**:
- Validate input quality before generation
- Use high-quality templates from pool
- Integrate with pesquisa agent for better data
- Learn from high-scoring examples (>= 9.5)

---

## COMMON ERROR MESSAGES

| Error Code | Message | Action |
|------------|---------|--------|
| `INPUT_001` | "Dados insuficientes: category obrigatorio" | Provide category |
| `INPUT_002` | "Confianca baixa (< 40%): enriquecer dados" | Add features/benefits |
| `FORMAT_001` | "Titulo excede 60 chars" | Auto-fix or regenerate |
| `FORMAT_002` | "Bullet fora do range 250-299 chars" | Auto-fix length |
| `FORMAT_003` | "Keywords insuficientes (< 115)" | Generate more terms |
| `COMPLIANCE_001` | "Claim proibido detectado: [term]" | Remove/replace term |
| `COMPLIANCE_002` | "Certificacao obrigatoria ausente" | Add ANVISA/INMETRO |
| `QUALITY_001` | "Score abaixo de 8.0 (atual: [X.X])" | Improve or review |
| `CATEGORY_001` | "Mismatch: produto nao pertence a categoria" | Suggest correct category |

---

## ESCALATION MATRIX

| Scenario | Severity | Auto-Fix | Human Review | Specialist |
|----------|----------|----------|--------------|------------|
| Missing product name | CRITICAL | No | Yes | No |
| Missing category | HIGH | Attempt inference | Yes | No |
| Char limit violation | MEDIUM | Yes | No | No |
| Prohibited claim | HIGH | Yes | If persists | Legal |
| Quality < 7.0 | MEDIUM | 3 attempts | Yes | Maybe |
| Quality < 8.0 | LOW | 1 attempt | Optional | No |
| Category mismatch | MEDIUM | Suggest fix | Yes | No |
| Ambiguous product | HIGH | Ask user | Yes | Category expert |

---

## MONITORING & METRICS

Track these metrics to identify patterns:

```yaml
error_metrics:
  input_quality_distribution:
    - Track confidence scores of incoming requests
    - Identify common missing fields
    - Measure enrichment request rate

  format_violation_rate:
    - Count auto-fixes per section
    - Track iteration count to compliance
    - Measure manual intervention rate

  compliance_violation_types:
    - Categorize prohibited claims
    - Track by product category
    - Measure fix success rate

  quality_score_distribution:
    - Track scores by category
    - Identify low-scoring patterns
    - Measure improvement from iteration

  recovery_success_rate:
    - Auto-fix success: target > 85%
    - Manual review required: target < 10%
    - Complete failures: target < 2%
```

---

## LEARNING FROM FAILURES

```yaml
feedback_loop:
  when_error_occurs:
    - Log full context (input + error + recovery)
    - Tag with error_code and category
    - Store in errors database

  weekly_analysis:
    - Review top 10 error patterns
    - Identify root causes
    - Update auto-fix rules
    - Improve validation logic

  monthly_improvement:
    - Update prohibited terms list
    - Refine category taxonomy
    - Enhance quality scoring weights
    - Train on high-quality examples
```

---

**Created**: 2026-02-06 | **LAW 7**: Resilience & Iteration | **Version**: 1.0.0
