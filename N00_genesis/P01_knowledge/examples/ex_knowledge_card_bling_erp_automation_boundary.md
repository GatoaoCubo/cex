---
id: p01_kc_bling_erp_automation_boundary
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Bling ERP: Fronteira de Automacao para Cadastro de Produto"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: knowledge_agent
domain: execution
quality: 9.1
tags: [bling, automation, boundary, tiering, human-in-the-loop, erp]
tldr: "44 campos Bling em 3 tiers: Tier1 auto via pipeline, Tier2 heuristica com override, Tier3 dados fiscais/fisicos so pelo usuario."
when_to_use: "Definir o que o pipeline pode preencher sozinho vs o que exige confirmacao humana no Bling"
keywords: [automation_boundary, human_override, tier1_tier2_tier3, product_onboarding]
long_tails:
  - "Quais campos do Bling podem ser automatizados sem operador humano"
  - "Como separar fallback do sistema e confirmacao do usuario no cadastro ERP"
axioms:
  - "SEMPRE automatizar apenas o que tem fonte repetivel ou default seguro"
  - "NUNCA empurrar dado fiscal sensivel para automacao cega"
linked_artifacts:
  primary: p01_kc_bling_erp_field_parametrization
  related: [p01_kc_zero_touch_execution]
density_score: 1.0
data_source: "https://developer.bling.com.br/homologacao"
related:
  - p01_kc_bling_erp_field_parametrization
  - bld_tools_subscription_tier
  - kc_subscription_tier
  - p01_kc_llm_benchmark_ecommerce_copy
  - p11_qg_agent_package
  - bld_examples_rate_limit_config
  - p01_kc_tag_grading_structured_data
  - bld_instruction_pricing_page
  - bld_output_template_subscription_tier
  - bld_instruction_subscription_tier
---

## Quick Reference

topic: automation boundary | scope: cadastro de produto no Bling | criticality: high
modelo: Tier 1 automatico | Tier 2 fallback com override | Tier 3 humano

## Conceitos Chave

- Tier 1 cobre campos repetiveis ou derivados por regra simples
- Tier 2 aceita heuristica, mas precisa override facil
- Tier 3 depende de realidade fisica, fiscal ou contratual
- Limite bom de automacao reduz erro sem esconder incerteza

## Comparativo

| Tier | Origem dominante | Exemplo | Acao do sistema |
|------|------------------|---------|-----------------|
| 1 | defaults/pipeline | nome, SKU, imagens | preencher direto |
| 2 | pesquisa/heuristica | preco, marca, NCM | sugerir e permitir editar |
| 3 | operador/empresa | GTIN, PIS, fornecedor | bloquear auto-fill |

| Categoria | Confianca | Campos | Politica |
|-----------|-----------|--------|----------|
| Comercial | alta | titulo, descricao, status | automatizar |
| Operacional | media | peso, dimensoes, estoque | revisar |
| Fiscal | baixa-media | NCM, CEST, aliquotas | confirmar |
| Identificacao unica | baixa | GTIN, lote, validade | usuario define |

## Regras de Ouro

- SEMPRE expor ao usuario tudo que veio de heuristica Tier 2
- SEMPRE manter audit trail do valor defaultado pelo pipeline
- NUNCA autopreencher GTIN, fornecedor ou tributo fixo sem prova
- SEMPRE degradar para rascunho quando o Tier 3 estiver incompleto

## Code

<!-- lang: python | purpose: route fields by automation confidence tier -->
```python
TIER_1 = {"nome", "codigo", "tipo", "situacao", "formato", "imagens"}
TIER_2 = {"preco", "marca", "pesoLiquido", "ncm", "cest"}
TIER_3 = {"gtin", "fornecedores", "pis", "cofins", "validade"}

def classify_field(field: str) -> str:
    if field in TIER_1:
        return "auto"
    if field in TIER_2:
        return "suggest"
    return "require_user"
```

## References

- external: https://developer.bling.com.br/homologacao
- external: https://www.bling.com.br/api-bling
- external: https://developer.bling.com.br/como-testar
- deepens: p01_kc_bling_erp_field_parametrization
- deepens: p01_kc_zero_touch_execution


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_bling_erp_field_parametrization]] | sibling | 0.36 |
| [[bld_tools_subscription_tier]] | downstream | 0.31 |
| [[kc_subscription_tier]] | sibling | 0.19 |
| [[p01_kc_llm_benchmark_ecommerce_copy]] | sibling | 0.19 |
| [[p11_qg_agent_package]] | downstream | 0.17 |
| [[bld_examples_rate_limit_config]] | downstream | 0.17 |
| [[p01_kc_tag_grading_structured_data]] | sibling | 0.16 |
| [[bld_instruction_pricing_page]] | downstream | 0.16 |
| [[bld_output_template_subscription_tier]] | downstream | 0.15 |
| [[bld_instruction_subscription_tier]] | downstream | 0.15 |
