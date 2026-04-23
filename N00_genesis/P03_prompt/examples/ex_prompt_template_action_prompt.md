---
id: p03_pt_action_prompt
kind: prompt_template
pillar: P03
title: Template Universal de Action Prompt
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
domain: meta
quality: 9.1
tags: [prompt, template, action, universal, meta]
tldr: Template reutilizavel para criar action prompts com variaveis tipadas
when_to_use: Quando precisa criar prompt de acao para qualquer agente
keywords: [action-prompt, prompt-template, prompt-engineering]
long_tails:
  - como criar prompt de acao para agente AI
  - template de prompt reutilizavel com variaveis
axioms:
  - Todo prompt precisa de PURPOSE, INPUT, EXECUTION, OUTPUT, VALIDATION
density_score: 0.95
related:
  - bld_instruction_chain
  - bld_instruction_action_prompt
  - action-prompt-builder
  - bld_examples_chain
  - p03_ch_content_pipeline
  - p02_agent_pesquisa
  - bld_examples_workflow_primitive
  - bld_schema_action_prompt
  - p06_is_quality_audit
  - p03_react_web_research
---

# Template: Action Prompt

## Variables

| Var | Tipo | Descricao | Exemplo |
|-----|------|-----------|---------|
| {{PROMPT_NAME}} | string | Nome do prompt | Analise de Mercado |
| {{PURPOSE}} | string | O que faz (1 linha) | Analisa concorrentes |
| {{INPUT_FIELDS}} | list | Campos de entrada | [url, domain, depth] |
| {{STEPS}} | list | Passos de execucao | [extrair, analisar, reportar] |
| {{OUTPUT_FORMAT}} | string | Formato de saida | markdown table |
| {{VALIDATIONS}} | list | Checklist final | [dados completos, score >= 8] |

## Template Body

```markdown
# {{PROMPT_NAME}}

## PURPOSE
{{PURPOSE}}

## INPUT
You will receive:
{{#each INPUT_FIELDS}}
- **{{name}}** ({{type}}): {{description}}. Example: `{{example}}`
{{/each}}

## EXECUTION

Follow these steps IN ORDER. Each step produces an intermediate output.

{{#each STEPS}}
### Step {{@index}}: {{title}}
- **Action**: {{action}}
- **Output**: {{output_description}}
- **Constraint**: {{constraint}}
{{/each}}

## OUTPUT FORMAT
Return results as: {{OUTPUT_FORMAT}}

Structure:
- **summary**: 2-3 sentence overview of findings
- **data**: structured results from execution steps
- **confidence**: 0.0-1.0 score for result reliability
- **sources**: list of references used

## VALIDATION
Before returning, verify ALL of these:
{{#each VALIDATIONS}}
- [ ] {{this}}
{{/each}}

If ANY validation fails, retry the failed step before returning.
```

### Example 1: Market Analysis Action Prompt

**Input**:
```yaml
PROMPT_NAME: Analise de Concorrentes ML
PURPOSE: Analisar top 5 concorrentes de um produto no Mercado Livre
INPUT_FIELDS:
  - name: product_url
    type: string
    description: URL do produto base no ML
    example: "https://mercadolivre.com.br/MLB-12345"
  - name: depth
    type: integer
    description: Numero de concorrentes a analisar
    example: 5
STEPS:
  - title: Extrair Dados Base
    action: Scrape produto base via Firecrawl
    output_description: JSON com titulo, preco, vendas, reputacao
    constraint: Max 3 credits Firecrawl
  - title: Identificar Concorrentes
    action: Buscar top N vendedores do mesmo catalogo
    output_description: Lista de seller_ids com metricas
    constraint: Apenas sellers com reputacao verde+
  - title: Comparar e Reportar
    action: Gerar tabela comparativa com gaps
    output_description: Markdown table com ranking
    constraint: Incluir preco, frete, reputacao, vendas/mes
VALIDATIONS:
  - Todos os 5 concorrentes tem dados completos
  - Precos em BRL com 2 decimais
  - Score de confianca >= 0.8
OUTPUT_FORMAT: markdown table + YAML summary
```

**Output**:
```markdown
## summary
Analisados 5 concorrentes para "Fone Bluetooth TWS". Lider: SellerX (R$89.90, 450 vendas/mes). Gap principal: frete gratis via Full.

## data
| Seller | Preco | Vendas/Mes | Reputacao | Frete | Buy Box |
|--------|-------|------------|-----------|-------|---------|
| SellerX | R$89.90 | 450 | Verde | Full | SIM |
| SellerY | R$94.50 | 320 | Verde | Flex | NAO |
| SellerZ | R$87.00 | 280 | Amarelo | Normal | NAO |
| SellerW | R$92.00 | 210 | Verde | Full | NAO |
| SellerV | R$99.90 | 180 | Verde | Full | NAO |

## confidence: 0.92
## sources: [MLB-12345, MLB-67890, MLB-11223, MLB-44556, MLB-77889]
```

### Example 2: SEO Keyword Action Prompt

**Input**:
```yaml
PROMPT_NAME: Extracao de Keywords SEO
PURPOSE: Extrair keywords de alto volume e baixa concorrencia para listing ML
INPUT_FIELDS:
  - name: seed_keyword
    type: string
    description: Palavra-chave semente
    example: "organizador de maquiagem acrilico"
  - name: max_keywords
    type: integer
    description: Numero maximo de keywords
    example: 20
STEPS:
  - title: Expandir Seeds
    action: Gerar variacoes long-tail da seed keyword
    output_description: Lista de 50+ keywords candidatas
    constraint: Incluir sinonimos BR (nao PT-PT)
  - title: Filtrar por Volume
    action: Estimar volume relativo via SERP analysis
    output_description: Keywords rankeadas por volume estimado
    constraint: Remover keywords com volume < 100/mes estimado
  - title: Classificar Intencao
    action: Categorizar cada keyword por intencao de busca
    output_description: Keywords com tag transactional/informational/navigational
    constraint: Priorizar transactional para listings
VALIDATIONS:
  - Min 15 keywords no output final
  - Cada keyword tem volume estimado e intencao
  - Zero keywords em PT-PT (validar BR)
OUTPUT_FORMAT: YAML list with metadata
```

**Output**:
```yaml
keywords:
  - term: "organizador de maquiagem acrilico grande"
    volume_est: high
    intent: transactional
    competition: low
  - term: "porta maquiagem acrilico com gaveta"
    volume_est: medium
    intent: transactional
    competition: low
  - term: "organizador cosmeticos acrilico transparente"
    volume_est: medium
    intent: transactional
    competition: medium
total: 18
avg_competition: low
recommended_title_keywords: ["organizador", "maquiagem", "acrilico", "grande", "gaveta"]
```

## Quality Gates
- PURPOSE: max 2 linhas, especifico (nao generico)
- INPUT: cada campo com tipo e exemplo
- STEPS: numerados, cada um com output intermediario
- VALIDATION: min 3 criterios mensuraveis

## Semantic Bridge
- Also known as: PromptTemplate, ChatPromptTemplate, SystemMessage
- Keywords: prompt engineering, template variables, instruction following
- LangChain: PromptTemplate | OpenAI: System Prompt | Anthropic: System Message

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_chain]] | related | 0.21 |
| [[bld_instruction_action_prompt]] | related | 0.20 |
| [[action-prompt-builder]] | related | 0.20 |
| [[bld_examples_chain]] | downstream | 0.20 |
| [[p03_ch_content_pipeline]] | related | 0.19 |
| [[p02_agent_pesquisa]] | upstream | 0.19 |
| [[bld_examples_workflow_primitive]] | downstream | 0.19 |
| [[bld_schema_action_prompt]] | downstream | 0.18 |
| [[p06_is_quality_audit]] | downstream | 0.18 |
| [[p03_react_web_research]] | related | 0.18 |
