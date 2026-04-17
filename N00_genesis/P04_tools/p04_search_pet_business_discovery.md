---
id: p04_search_pet_business_discovery
kind: search_tool
pillar: P04
title: Pet Business Discovery Search Tool
version: 1.0.0
created: 2026-04-03
updated: 2026-04-03
author: builder_agent
domain: crm-research
provider: multi
search_type: web
max_results: 20
result_fields: [title, url, snippet, address, phone]
cost_per_query: "SERPER ~$0.004, FIRECRAWL ~$0.01, EXA ~$0.01"
rate_limits: "SERPER 2500/mo, FIRECRAWL 500/mo, EXA 1000/mo"
tags: [search_tool, pet, business, discovery, crm, SERPER, FIRECRAWL, GATO3]
tldr: "Busca multi-provider otimizada para descoberta de negocios pet por cidade — termos primarios por vertical, long-tail local, negative keywords e variacoes regionais."
quality: 9.1
density_score: null
---

# Pet Business Discovery Search Tool

## Overview
Configuracao de busca multi-provider para descoberta sistematica de businesses pet em cidades brasileiras. Combina SERPER (Google), FIRECRAWL (directories/social), e EXA (semantic) com termos otimizados por vertical pet e regiao.

## Query Strategy

### Termos Primarios por Vertical
```yaml
pet_shop: ["pet shop {cidade}", "loja pet {cidade}", "produtos para gatos {cidade}"]
banho_tosa: ["banho e tosa {cidade}", "banho tosa gatos {cidade}", "grooming felino {cidade}"]
veterinario: ["veterinario {cidade}", "clinica veterinaria {cidade}", "vet gatos {cidade}"]
distribuidor: ["distribuidor pet {cidade}", "atacado pet {cidade}", "fornecedor pet {cidade}"]
hotel_pet: ["hotel pet {cidade}", "hospedagem gatos {cidade}", "creche felina {cidade}"]
adestramento: ["adestrador {cidade}", "comportamento felino {cidade}"]
alimentacao: ["racao premium {cidade}", "alimentacao natural gatos {cidade}"]
acessorios: ["acessorios gatos {cidade}", "arranhador {cidade}", "brinquedos gatos {cidade}"]
daycare: ["daycare pet {cidade}", "creche pet {cidade}"]
farmacia_vet: ["farmacia veterinaria {cidade}", "manipulacao veterinaria {cidade}"]
estetica: ["estetica animal {cidade}", "spa pet {cidade}"]
funeraria: ["cremacao pet {cidade}", "funeraria animal {cidade}"]
```

### Long-Tail Keywords Locais
```yaml
pattern: "{vertical} {bairro} {cidade} {uf}"
examples:
  - "pet shop centro Sao Bernardo do Campo SP"
  - "veterinario 24h Rudge Ramos SBC"
```

### Negative Keywords (filtros)
```yaml
exclude: ["adocao", "ONG", "resgate", "doacao", "perdido", "achado", "castramovil"]
reason: "Filtrar resultados nao-comerciais que poluem CRM B2B"
```

### Variacoes Regionais
```yaml
abc_paulista: {suffix: "ABC", "Grande ABC", alt_names: true}
grande_sp: {suffix: "SP", "Grande Sao Paulo"}
interior_sp: {suffix: "interior SP", include_regiao: true}
```

## Provider Routing
| Provider | Quando Usar | Budget/mo |
|----------|-------------|-----------|
| SERPER | Termos primarios (4 por cidade) | 50 queries/cidade, max 2500 |
| FIRECRAWL | TeleListas, Instagram, Facebook | 20 scrapes/cidade, max 500 |
| EXA | Semantic discovery (long-tail) | 10 searches/cidade, max 1000 |
| FETCH | CNPJ databases, iFood, Rappi | Unlimited |

## Result Structure
```yaml
result:
  title: string
  url: string
  snippet: string
  source: enum[serper, firecrawl, exa, fetch]
  query_term: string
  vertical: string
  cidade: string
```

## Rate Limit Management
- Checkpoint entre verticais (nao entre queries individuais)
- Prioridade: pet_shop > veterinario > banho_tosa > distribuidor > resto
- Fallback: se SERPER esgotado, usar EXA semantic para verticais restantes

## Footer
Provider: multi (SERPER+FIRECRAWL+EXA+FETCH) | Quality: null | Domain: crm-research
