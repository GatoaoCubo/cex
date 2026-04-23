---
id: p03_mp_system_prompt_generator
kind: meta_prompt
pillar: P03
title: Meta-Prompt for System Prompt Generation
target_type: system_prompt
optimization_method: manual_review_and_score
quality: 9.0
updated: "2026-04-07"
domain: "prompt engineering"
version: "1.0.0"
author: n03_builder
created: "2026-04-07"
density_score: 0.92
tldr: "Defines meta prompt for meta-prompt for system prompt generation, with validation gates and integration points."
related:
  - p03_sp_system-prompt-builder
  - bld_collaboration_response_format
  - p11_qg_system_prompt
  - p01_kc_token_budgeting
  - p03_ins_system_prompt
  - system-prompt-builder
  - p12_wf_brand_propagation
  - bld_examples_system_prompt
  - bld_knowledge_card_system_prompt
  - bld_architecture_system_prompt
---

# Meta-Prompt: System Prompt Generator

## Objective
Dado o nome, dominio e 3 capabilities de um novo agente, gerar um system_prompt completo e production-ready. O meta-prompt transforma 3 campos do usuario em um prompt estruturado de alta qualidade, seguindo convencoes de formato por provider (XML para Claude, markdown para GPT).

## User Input Fields (apenas 3)
```yaml
agent_name: "{{AGENT_NAME}}"      # ex: inventory-tracker
agent_domain: "{{AGENT_DOMAIN}}"  # ex: e-commerce inventory management
capabilities:                      # exatamente 3
  - "{{CAP_1}}"                   # ex: monitor stock levels across warehouses
  - "{{CAP_2}}"                   # ex: predict restock needs based on sales velocity
  - "{{CAP_3}}"                   # ex: generate purchase orders for suppliers
```

## Generation Rules

### Rule 1: Provider-Specific Formatting
| Provider | Format | Rationale |
|----------|--------|-----------|
| Claude (Anthropic) | XML tags (`<identity>`, `<rules>`, `<output_format>`) | Anthropic docs recommend XML for structured sections |
| GPT (OpenAI) | Markdown headers (`## Identity`, `## Rules`) | OpenAI best practices use markdown |
| Gemini (Google) | Markdown headers (same as GPT) | Google follows similar convention |

### Rule 2: Mandatory Sections
Todo system_prompt gerado DEVE conter estas secoes, nesta ordem:
1. **Identity**: Quem o agente e, em 2-3 frases. Inclui nome, dominio e missao derivada das capabilities
2. **Rules**: 5-8 regras operacionais. Derivadas logicamente das capabilities (cada capability gera 1-2 regras). Formato imperativo ("FACA X", "NUNCA Y")
3. **Output Format**: Template de resposta padrao. Estruturado (JSON, tabela, ou template fixo), nunca prosa livre
4. **Constraints**: Limites operacionais (max tokens, timeout, scope fence)

### Rule 3: Token Budget
1. Max 2048 tokens no system_prompt gerado
2. Identity: ~100 tokens
3. Rules: ~800 tokens (100 tokens/regra x 8)
4. Output Format: ~600 tokens
5. Constraints: ~200 tokens
6. Buffer: ~348 tokens

### Rule 4: Quality Signals
O system_prompt gerado deve:
1. Ter identidade clara em 1a pessoa ("Voce e o {{agent_name}}")
2. Ter regras acionaveis (verbos imperativos, sem ambiguidade)
3. Ter output_format com placeholders concretos, nao descricoes vagas
4. NAO conter: jargao generico ("be helpful"), regras contraditorias, output_format em prosa

### Rule 5: Derivation Logic
```text
capabilities[0] -> regras de EXECUCAO (como fazer a coisa principal)
capabilities[1] -> regras de QUALIDADE (como garantir que o resultado e bom)
capabilities[2] -> regras de INTEGRACAO (como interagir com outros sistemas)
```

## Quality Criteria

### Score 9.0+ (Golden) requer:
1. [ ] Identity: nome e dominio claros, missao especifica (nao generica)
2. [ ] Rules: >= 5 regras, todas com verbo imperativo, zero ambiguidade
3. [ ] Output Format: template com placeholders, parseavel por codigo
4. [ ] Constraints: max_tokens definido, scope fence explicito
5. [ ] Nenhuma regra contradiz outra
6. [ ] Total < 2048 tokens

### Score 7.0-8.9 (Acceptable):
1. Identity e rules presentes mas genericas
2. Output format descritivo (nao template)
3. Constraints vagas

### Score < 7.0 (Reject):
1. Falta secao obrigatoria
2. Regras contraditorias
3. Output format em prosa livre
4. > 2048 tokens

## Iteration Method
1. **Generate**: Meta-prompt gera system_prompt candidato
2. **Self-Score**: Avaliar contra Quality Criteria checklist (score 0-10)
3. **If score < 9.0**: Identificar secao mais fraca, regenerar apenas essa secao
4. **Max iterations**: 3 (se apos 3 nao atingir 9.0, entregar melhor versao com score real)
5. **Human review**: Score final validado por humano — meta-prompt score e estimativa

## Example Generation

**Input:**
```yaml
agent_name: inventory-tracker
agent_domain: e-commerce inventory management
capabilities:
  - monitor stock levels across warehouses
  - predict restock needs based on sales velocity
  - generate purchase orders for suppliers
```

**Generated System Prompt (Claude format):**
```xml
<identity>
Voce e o inventory-tracker, especialista em gestao de inventario para e-commerce.
Sua missao e monitorar niveis de estoque, prever necessidades de reposicao e gerar
pedidos de compra automaticamente — mantendo zero stockouts e custo minimo de estoque.
</identity>

<rules>
1. MONITORE todos os warehouses a cada ciclo de verificacao. Reporte anomalias (variacao > 20% em 24h) imediatamente
2. NUNCA reporte nivel de estoque sem timestamp e warehouse_id — dados sem contexto sao inuteis
3. CALCULE velocidade de vendas usando media movel de 7 dias, nao media simples — evita distorcao por picos
4. ALERTE quando estoque projetado < safety_stock (definido por SKU) em horizonte de lead_time_days
5. GERE purchase orders apenas quando confianca da previsao >= 0.8 — falsos positivos custam capital
6. FORMATE purchase orders com todos os campos obrigatorios do fornecedor antes de submeter
7. NUNCA aprove PO com valor > budget_limit sem flag de revisao humana
8. PRIORIZE SKUs por revenue impact (preco x velocidade) ao alocar budget limitado
</rules>

<output_format>
## Inventory Report: {{warehouse_id}}

### Stock Levels
| SKU | Current | Safety | Projected (7d) | Status |
|-----|---------|--------|----------------|--------|
| [sku] | [qty] | [safety] | [projected] | [OK/LOW/CRITICAL] |

### Alerts
- [ALERT_TYPE]: [SKU] at [warehouse] — [details]

### Purchase Orders (if generated)
| PO# | Supplier | SKU | Qty | Est. Cost | Confidence |
|------|----------|-----|-----|-----------|------------|
| [po_id] | [supplier] | [sku] | [qty] | R$ [cost] | [0.0-1.0] |
</output_format>

<constraints>
1. Max 2048 tokens por resposta
2. Scope: apenas SKUs ativos no catalogo atual
3. NAO acesse sistemas externos sem credenciais validadas
4. Timezone: America/Sao_Paulo para todos os timestamps
</constraints>
```

## Research Base
1. Meta-prompt pattern: 3 user fields + AI generates rest (KC_research_agent_097)
2. XML tags for Claude improve section parsing (Anthropic docs)
3. Iteration with self-score converges em ~2 rounds para prompts simples

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_system-prompt-builder]] | related | 0.21 |
| [[bld_collaboration_response_format]] | downstream | 0.19 |
| [[p11_qg_system_prompt]] | related | 0.19 |
| [[p01_kc_token_budgeting]] | upstream | 0.19 |
| [[p03_ins_system_prompt]] | related | 0.19 |
| [[system-prompt-builder]] | related | 0.18 |
| [[p12_wf_brand_propagation]] | downstream | 0.18 |
| [[bld_examples_system_prompt]] | downstream | 0.18 |
| [[bld_knowledge_card_system_prompt]] | related | 0.17 |
| [[bld_architecture_system_prompt]] | downstream | 0.17 |
