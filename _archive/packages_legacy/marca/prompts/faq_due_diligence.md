# FAQ DUE DILIGENCE | MARCA AGENT WHITE-LABEL

**Version**: 1.0.0 | **Date**: 2025-12-20
**Prepared for**: Investor Due Diligence
**Confidentiality**: Internal Use Only

---

## CATEGORIA 1: PRODUTO & TECNOLOGIA

### Q1: O que exatamente e o marca_agent?

**R**: Agente especializado em brand strategy para e-commerce brasileiro. Diferente de wrappers de ChatGPT, o marca_agent e treinado com:
- Knowledge bases especificos (brand_archetypes.yaml com 12 arquetipos detalhados)
- Workflows validados (32-block brand strategy)
- Compliance brasileiro (ANVISA, INMETRO, CONAR)
- Quality gates automaticos (score minimo 7.0/10)

### Q2: Qual a diferenca entre marca_agent e usar ChatGPT/Claude direto?

| Aspecto | ChatGPT Direto | marca_agent |
|---------|----------------|-------------|
| Especializacao | Generico | Brand strategy BR especializado |
| Conhecimento | Base geral | Knowledge bases por dominio |
| Consistencia | Varia por prompt | Workflows padronizados (32 blocos) |
| Compliance BR | Nenhum | ANVISA, INMETRO, CONAR |
| White-label | Impossivel | Nativo |
| Treinamento | Usuario faz | Pre-configurado |

### Q3: O marca_agent usa fine-tuning ou RAG?

**R**: Atualmente usa **RAG (Retrieval-Augmented Generation)**:
- Vector stores com knowledge bases (brand_archetypes.yaml, compliance_rules.yaml, etc)
- System instructions especializadas (~1000 tokens)
- Arquitetura LLM-agnostica (Claude, GPT-4, Gemini, Llama)

### Q4: Quais LLMs o marca_agent suporta?

**R**: Arquitetura LLM-agnostica:
- **Tier 1 (Produtivo)**: GPT-4o, GPT-4.1, Claude Sonnet
- **Tier 2 (Custo-beneficio)**: GPT-4.1-mini, Claude Haiku
- **Tier 3 (Roadmap)**: Llama 3, Mistral, modelos locais

### Q5: Como funciona o sistema de qualidade?

**R**: Framework 5D:

```
5D (Dimensoes):
- D1: Coerencia de Identidade (peso 2.0)
- D2: Forca de Posicionamento (peso 2.0)
- D3: Consistencia de Voz (peso 2.0)
- D4: Compliance (peso 2.0)
- D5: Completude (peso 2.0)

Thresholds:
- < 7.0: Rejeitado
- >= 7.0: Experimental
- >= 8.0: Producao
- >= 9.5: Golden (modelo para treinamento)
```

---

## CATEGORIA 2: MODELO DE NEGOCIO

### Q6: Qual o modelo de receita white-label?

**R**: SaaS B2B com revenue share:

```
Estrutura de Preco:
+------------------+-------------+------------------+
| Plano            | MRR Agencia | Margem           |
+------------------+-------------+------------------+
| Starter          | R$ 297      | ~70%             |
| Professional     | R$ 697      | ~72%             |
| Enterprise       | R$ 1.497+   | ~70%             |
+------------------+-------------+------------------+
```

### Q7: Qual o LTV/CAC projetado?

**R**:
- **LTV**: R$ 10.692 (36 meses retencao media, churn 3%)
- **CAC target**: R$ 289 (inside sales + content marketing)
- **LTV/CAC**: 37x
- **Payback**: 1.0 meses

### Q8: Qual o TAM/SAM/SOM?

**R**:
```
TAM: 50.000 agencias de marketing no Brasil = R$300M/ano
SAM: 15.000 agencias digitais = R$90M/ano
SOM (Y3): 1.700 agencias (11% do SAM) = R$10.2M/ano
```

---

## CATEGORIA 3: PRODUTO

### Q9: Quais os 32 blocos gerados?

**R**: 7 secoes completas:
1. Identidade (nomes, taglines, arquetipo, tracos, essencia)
2. Posicionamento (UVP, segmento, diferenciacao, promessa, statement)
3. Tom de Voz (dimensoes, estilo, do's, don'ts, frases)
4. Visual (cores HEX+RGB, tipografia, mood board 9 prompts)
5. Narrativa (origem, missao, visao, valores, manifesto)
6. Diretrizes (do's estendidos, don'ts, compliance, checklist)
7. Validacao (consistency score, uniqueness score, auditoria, integracao)

### Q10: Como funciona o white-label?

**R**: Agencia substitui 6 placeholders no system_instruction_whitelabel.md:
- `{{AGENCY_NAME}}` -> nome da agencia
- `{{AGENT_NAME}}` -> nome do agente (ex: "BrandGenie")
- `{{AGENCY_URL}}` -> site da agencia
- `{{SUPPORT_EMAIL}}` -> email de suporte
- `{{PRIMARY_COLOR}}` -> cor da marca
- `{{SECONDARY_COLOR}}` -> cor secundaria

Deploy em 30 minutos. Cliente final ve apenas a marca da agencia.

---

## CATEGORIA 4: PROPRIEDADE INTELECTUAL

### Q11: O que e proprietario?

**R**:
```
PROPRIETARIO:
- Knowledge bases especializados (brand_archetypes.yaml, compliance_rules.yaml, etc)
- System instructions otimizadas
- Heuristicas de quality gates
- Framework 32-block brand strategy
- Integracao white-label
```

---

## DOCUMENTOS DISPONIVEIS

| Documento | Localizacao |
|-----------|-------------|
| Knowledge bases | data/ directory |
| System instructions | system_instruction*.md |
| Output templates | output_template.md |
| Quality framework | data/quality_dimensions.yaml |
| Deploy guides | upload_kit*.md |

---

**FAQ Due Diligence v1.0.0**
**Status**: Confidencial
**Ultima Atualizacao**: 2025-12-20
