---
id: p04_browser_web_scraping
name: web-scraping
description: Pipeline de web scraping com selecao automatica de estrategia (static/dynamic/API/stealth)
version: 1.0.0
pillar: P04
kind: browser_tool
8f: F5_call
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: data_collection
quality: 9.1
tags: [scraping, selenium, playwright, beautifulsoup, data-extraction]
tldr: Skill que roteia automaticamente entre 4 estrategias de scraping baseado na complexidade do alvo e entrega dados estruturados
user_invocable: true
trigger: /scrape [url] [--strategy auto|static|dynamic|api|stealth]
when_to_use: Extrair dados estruturados de paginas web para pesquisa, pricing ou monitoring
when_not_to_use: Dados disponiveis via API publica documentada (use client direto)
phases:
  - Recon
  - Extract
  - Validate
examples:
  - "/scrape https://example.com/products --strategy auto"
  - "/scrape https://marketplace.com/search?q=pet+toys --strategy dynamic --pagination 5"
density_score: 0.88
related:
  - p02_agent_web_researcher
  - bld_examples_browser_tool
  - p02_agent_data_validator
  - p01_kc_web_scraping_ethics
  - p01_kc_browser_tool
  - p04_tool_scraping_config
  - p04_browser_playwright
  - p04_browser_tool_NAME
  - p03_react_web_research
  - bld_instruction_browser_tool
---

# Web Scraping Skill

## Purpose
web-scraping e o **roteador inteligente de extracao web** do organization. Domain: data_collection (research_agent agent_group). Resolve o problema de escolher a estrategia correta de scraping para cada alvo, evitando over-engineering (Selenium onde BeautifulSoup basta) e under-engineering (requests onde JS rendering e necessario).

## Workflow Phases

### Phase 1: Recon
**Input**: URL alvo + parametros do usuario
**Action**: HEAD request + analise de headers (Content-Type, Server, X-Powered-By). Detecta: SSR vs SPA, Cloudflare/Akamai, JSON-LD embutido, robots.txt rules.
**Output**: Strategy recommendation (static|dynamic|api|stealth) + confidence score

### Phase 2: Extract
**Input**: Strategy selecionada + URL + selectors (auto-detected ou user-provided)
**Action**: Executa scraper correspondente:
- **Static**: BeautifulSoup + requests (< 100ms/page)
- **Dynamic**: Playwright headless com wait_for_selector (< 3s/page)
- **API**: Intercepta XHR/fetch calls, chama endpoint direto (< 200ms/call)
- **Stealth**: Fingerprint randomization + proxy rotation + human delays (< 10s/page)
**Output**: Raw HTML/JSON + extracted data fields

### Phase 3: Validate
**Input**: Dados extraidos + schema esperado
**Action**: Verifica completude (campos obrigatorios preenchidos), tipo (string/number/date), e sanidade (precos > 0, datas no futuro = warning). Retry automatico se completude < 80%.
**Output**: Dados validados em JSON + quality report

## Usage

```bash
# Scraping automatico com strategy detection
/scrape https://www.mercadolivre.com.br/produto-123 --strategy auto

# Scraping dinamico com paginacao
/scrape https://shopee.com.br/search?keyword=led --strategy dynamic --pagination 3

# Extracao de dados estruturados (JSON-LD)
/scrape https://example.com/product --strategy api --format jsonld
```

## Input / Output

```yaml
input:
  url: string          # URL alvo (obrigatorio)
  strategy: enum       # auto|static|dynamic|api|stealth (default: auto)
  selectors: dict      # CSS selectors customizados (opcional)
  pagination: int      # Numero de paginas (default: 1)
  timeout: int         # Timeout em segundos (default: 30)

output:
  data: list[dict]     # Dados extraidos estruturados
  strategy_used: str   # Estrategia efetivamente usada
  pages_scraped: int   # Paginas processadas
  quality_score: float # 0.0-1.0 completude dos dados
```

## Anti-Patterns
- **Selenium para HTML statico**: Overhead de 10-50x sem necessidade — use BeautifulSoup
- **Ignorar robots.txt**: Risco de ban permanente + questoes legais
- **Hardcoded selectors**: Quebram com qualquer update do site — prefira JSON-LD ou XPath resiliente
- **Sem rate limiting**: Sobrecarrega servidor alvo, trigga anti-bot mais rapido

## Metrics
| Metrica | Threshold | Acao |
|---------|-----------|------|
| Completude dos dados | >= 80% | Retry com strategy upgrade |
| Tempo por pagina | < 5s (static), < 15s (dynamic) | Escalar ou simplificar selectors |
| Taxa de erro (4xx/5xx) | < 10% | Ativar proxy rotation |
| Ban rate | 0% | Reduzir concorrencia, aumentar delays |

## Cross-References
- scraper-static-agent: Executor para estrategia static (BeautifulSoup)
- scraper-dynamic-agent: Executor para estrategia dynamic (Playwright)
- scraper-stealth-agent: Executor para alvos protegidos (Cloudflare/Akamai)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_web_researcher]] | upstream | 0.29 |
| [[bld_examples_browser_tool]] | downstream | 0.23 |
| [[p02_agent_data_validator]] | upstream | 0.23 |
| [[p01_kc_web_scraping_ethics]] | upstream | 0.21 |
| [[p01_kc_browser_tool]] | related | 0.19 |
| [[p04_tool_scraping_config]] | related | 0.18 |
| [[p04_browser_playwright]] | sibling | 0.18 |
| [[p04_browser_tool_NAME]] | sibling | 0.17 |
| [[p03_react_web_research]] | upstream | 0.17 |
| [[bld_instruction_browser_tool]] | upstream | 0.16 |
