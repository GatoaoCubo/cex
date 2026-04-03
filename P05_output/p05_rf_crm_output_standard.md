---
id: p05_rf_crm_output_standard
kind: response_format
pillar: P05
title: CRM Output Standard Response Format
version: 1.0.0
created: 2026-04-03
updated: 2026-04-03
author: builder_agent
domain: crm-research
task: "Padronizar output de research CRM multi-cidade para pipeline pet business"
format_type: yaml
injection_point: system_prompt
target_kind: agent
sections: [cidade, businesses, summary_stats]
sections_count: 3
llm_function: CONSTRAIN
tags: [response_format, crm, output, multi-city, pet, pipeline, GATO3]
tldr: "Schema padrao de output CRM multi-cidade — estrutura cidade + lista businesses + estatisticas, replicavel cross-city."
quality: null
density_score: null
---

# CRM Output Standard Response Format

## Format Overview
Define a estrutura de output padronizada para toda pipeline CRM de descoberta pet. O LLM DEVE seguir este formato estritamente ao gerar resultados de research por cidade. Output e YAML com 3 secoes: metadados da cidade, lista de businesses, e estatisticas resumo. Modo strict: sim.

## Sections

### S1: Cidade (required)
```yaml
cidade:
  nome: string          # Nome completo (ex: "Sao Bernardo do Campo")
  uf: string            # Sigla estado (ex: "SP")
  ring: int             # Ring geografico 1|2|3|4
  populacao_estimada: int  # Populacao IBGE estimada
  densidade_estimada: float  # Businesses pet / 10k habitantes
  data_research: string    # Data ISO da pesquisa (YYYY-MM-DD)
  fontes_usadas: list      # ["serper", "firecrawl", "exa", "fetch"]
  budget_consumido:
    serper: int          # Queries gastas
    firecrawl: int       # Scrapes gastos
```

### S2: Businesses (repeated, min 1)
```yaml
businesses:
  - nome: string              # Nome comercial
    cnpj: string | null       # 14 digitos sem formatacao
    telefone: string | null   # +55XXXXXXXXXXX
    whatsapp: string | null   # +55XXXXXXXXXXX (pode ser = telefone)
    email: string | null      # email comercial
    website: string | null    # URL com protocolo
    endereco: string          # Endereco completo
    bairro: string | null     # Bairro
    segmento: enum            # pet_shop|banho_tosa|veterinario|distribuidor|hotel_pet|adestramento|alimentacao|acessorios|daycare|farmacia_vet|estetica|funeraria
    potencial: enum           # A|B|C
    completeness_score: int   # 0-4 (campos de contato validados)
    fonte_descoberta: string  # Fonte primaria de descoberta
    fontes_cruzadas: list     # Todas as fontes que confirmaram
    data_discovery: string    # ISO date
    notas: string | null      # Observacoes livres
```

### S3: Summary Stats (required)
```yaml
summary:
  total_businesses: int
  por_segmento:              # Contagem por vertical
    pet_shop: int
    banho_tosa: int
    veterinario: int
    distribuidor: int
    hotel_pet: int
    outros: int
  por_potencial:
    A: int
    B: int
    C: int
  taxa_contato_direto: float   # % com telefone ou whatsapp
  taxa_email: float            # % com email
  taxa_website: float          # % com website
  completeness_media: float    # Media do completeness_score
  tempo_execucao: string       # "1h23m"
```

## Example Output
```yaml
cidade:
  nome: "Sao Bernardo do Campo"
  uf: "SP"
  ring: 1
  populacao_estimada: 844483
  densidade_estimada: 1.8
  data_research: "2026-04-03"
  fontes_usadas: ["serper", "firecrawl", "fetch"]
  budget_consumido:
    serper: 42
    firecrawl: 15

businesses:
  - nome: "Pet House SBC"
    cnpj: "12345678000190"
    telefone: "+5511999887766"
    whatsapp: "+5511999887766"
    email: "contato@pethouse.com.br"
    website: "https://pethouse.com.br"
    endereco: "Rua Marechal Deodoro 500, Centro"
    bairro: "Centro"
    segmento: "pet_shop"
    potencial: "A"
    completeness_score: 4
    fonte_descoberta: "serper"
    fontes_cruzadas: ["serper", "firecrawl", "fetch"]
    data_discovery: "2026-04-03"
    notas: "Loja grande, aceita revenda"

summary:
  total_businesses: 48
  por_segmento:
    pet_shop: 15
    banho_tosa: 12
    veterinario: 10
    distribuidor: 3
    hotel_pet: 5
    outros: 3
  por_potencial:
    A: 12
    B: 20
    C: 16
  taxa_contato_direto: 0.73
  taxa_email: 0.52
  taxa_website: 0.44
  completeness_media: 2.8
  tempo_execucao: "1h47m"
```

## Footer
Format: crm_output_standard | Quality: null | Domain: crm-research
