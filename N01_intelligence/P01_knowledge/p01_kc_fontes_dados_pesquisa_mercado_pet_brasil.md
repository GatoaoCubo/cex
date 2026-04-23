---
id: p01_kc_fontes_dados_pesquisa_mercado_pet_brasil
kind: knowledge_card
pillar: P01
title: "Principais Fontes de Dados para Pesquisa de Mercado Pet no Brasil"
version: "1.0.0"
created: "2024-12-28"
updated: "2024-12-28"
author: "knowledge-card-builder"
domain: market_research
quality: 9.1
tags: [pesquisa_mercado, pet, brasil, fontes_dados, custos, rate_limits]
tldr: "Fontes primárias de dados para pesquisa do mercado pet brasileiro com custos específicos e limitações de acesso"
when_to_use: "Quando precisar identificar e acessar dados confiáveis sobre mercado pet nacional"
keywords: [abinpet, ibge, euromonitor, mercado_pet, dados_setoriais]
long_tails:
  - Como acessar dados da Abinpet sobre faturamento do setor pet brasileiro
  - Custos de relatórios Euromonitor para mercado pet Brasil
  - Rate limits das APIs de e-commerce pet nacionais
axioms:
  - SEMPRE verifique data de publicação dos relatórios setoriais antes de citar
  - NUNCA use apenas uma fonte para validar tamanho de mercado
  - SEMPRE combine fontes governamentais gratuitas com privadas pagas
linked_artifacts:
  primary: null
  related: [p01_kc_amazon_ads_benchmarks_brasil]
density_score: 0.85
data_source: "https://abinpet.org.br/mercado/"
related:
  - p02_agent_petshop_crm
  - p02_agent_web_researcher
  - p02_agent_pesquisa
  - e2e_gold_petshop_marketing
  - p03_pv_pesquisa_system_v2
  - n01_output_monetization_research
  - p02_agent_pet_shop_crm
  - lp_petshop_crm_001
---

# Principais Fontes de Dados para Pesquisa de Mercado Pet no Brasil

## Quick Reference
```yaml
topic: fontes_dados_mercado_pet_brasil
scope: IBGE, Abinpet, Euromonitor, APIs e-commerce, institutos privados
owner: knowledge-card-builder
criticality: high
```

## Fontes Governamentais (Gratuitas)

### IBGE (Instituto Brasileiro de Geografia e Estatística)
- **POF (Pesquisa de Orçamentos Familiares)**: gastos com animais domésticos
- **Censo Demográfico**: população urbana/rural (correlação posse pets)
- **PNAD Contínua**: renda familiar (poder de compra pet)
- **Frequência**: POF a cada 5-6 anos; Censo 10 anos; PNAD trimestral
- **Acesso**: https://sidra.ibge.gov.br (gratuito, sem rate limit)

### Ministério da Agricultura (MAPA)
- **Registro de produtos veterinários**: base completa fabricantes
- **Fiscalização de rações**: marcas ativas no mercado
- **Dados de exportação/importação**: NCM 2309 (alimentos animais)
- **Acesso**: https://sistemasweb.agricultura.gov.br

## Associações Setoriais (Mistas)

### Abinpet (Associação Brasileira da Indústria de Produtos para Animais)
- **Censo Pet**: faturamento setorial anual R$ 64,2 bi (2023)
- **Custos**: relatórios básicos gratuitos; dados granulares R$ 2.500-15.000
- **Rate limit**: contato comercial, sem API pública
- **Cobertura**: alimentos, acessórios, higiene, medicamentos
- **URL**: https://abinpet.org.br/mercado/

### Comac (Sindicato Nacional da Indústria de Alimentação Animal)
- **Foco**: produção de rações (toneladas/faturamento)
- **Custo**: associados gratuito; não-associados R$ 800-3.000/relatório
- **Frequência**: trimestral (produção), anual (mercado)

## Institutos de Pesquisa Privados

### Euromonitor International
- **Relatório Pet Care Brasil**: US$ 8.500-12.000 (single user)
- **Cobertura**: market size, forecast 5 anos, share marcas
- **Atualização**: anual (Q1)
- **Limitações**: 1 usuário, sem redistribuição, PDF watermark

### Kantar (ex-TNS)
- **WorldPanel Brasil**: painel consumo familiar pet
- **Custo**: acesso custom R$ 25.000-80.000/ano
- **Granularidade**: marcas, categorias, regiões, classes sociais
- **Rate limit**: dashboard web, exportação limitada

### Nielsen/NielsenIQ
- **Retail Measurement**: vendas no varejo (hiper, pet shops)
- **Investimento**: R$ 15.000-40.000 setup + mensalidade
- **Cobertura**: 85% mercado formal pet food nacional

## E-commerce APIs (Rate Limits Críticos)

| Plataforma | Rate Limit | Custo Acesso | Dados Disponíveis |
|------------|-----------|--------------|-------------------|
| Mercado Livre | 10.000 calls/dia | Gratuito | Preços, vendas, reviews |
| Amazon Brasil | 100 calls/h | Selling Partner API | Rankings, preços, estoque |
| Petlove | Sem API pública | Scraping (legal risk) | Catálogo, promocões |
| Cobasi | 500 calls/dia | Parceria B2B | Preços, disponibilidade |

## Fontes Acadêmicas

### Repositórios Universitários
- **USP/ESALQ**: pesquisas agronegócio pet food
- **UFMG Veterinária**: comportamento consumidor pet
- **FGV EAESP**: estudos mercado consumo
- **Acesso**: gratuito via Scielo, CAPES, repositórios institucionais

### Revistas Especializadas
- **RBMV (Revista Brasileira de Medicina Veterinária)**: trends clínicos
- **Pet South America**: dados indústria (revista trade)
- **Custo**: assinatura R$ 200-800/ano

## Comparativo Custo-Benefício

| Fonte | Custo Anual | Confiabilidade | Granularidade | Frequência |
|-------|-------------|----------------|---------------|------------|
| IBGE | R$ 0 | 9/10 | Macro | Baixa |
| Abinpet | R$ 0-15.000 | 8/10 | Setorial | Alta |
| Euromonitor | R$ 45.000 | 9/10 | Mercado | Média |
| APIs E-commerce | R$ 0-5.000 | 7/10 | SKU/Marca | Tempo real |
| Nielsen | R$ 180.000+ | 9/10 | Total | Alta |

## Golden Rules
- COMBINE sempre governamental (IBGE) + setorial (Abinpet) + privado
- VALIDE dados de uma fonte com pelo menos duas outras independentes
- MONITORE rate limits de APIs antes de automação em escala
- NEGOCIE acesso institucional para reduzir custos Euromonitor/Nielsen

## References
- Fonte primária: https://abinpet.org.br/mercado/
- IBGE Sidra: https://sidra.ibge.gov.br
- Euromonitor: https://www.euromonitor.com/pet-care-in-brazil

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_petshop_crm]] | downstream | 0.24 |
| [[p02_agent_web_researcher]] | downstream | 0.20 |
| [[p02_agent_pesquisa]] | downstream | 0.19 |
| [[e2e_gold_petshop_marketing]] | related | 0.18 |
| [[p03_pv_pesquisa_system_v2]] | downstream | 0.18 |
| [[n01_output_monetization_research]] | downstream | 0.17 |
| [[p02_agent_pet_shop_crm]] | downstream | 0.16 |
| [[lp_petshop_crm_001]] | downstream | 0.15 |
