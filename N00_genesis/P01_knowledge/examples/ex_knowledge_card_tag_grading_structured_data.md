---
id: p01_kc_tag_grading_structured_data
kind: knowledge_card
pillar: P01
title: "TAG Grading: Structured Data Extraction em Paginas CSR"
version: 2.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: research
quality: 9.1
tags: [tag-grading, structured-data, browser-automation, scraping, csr]
tldr: "Certificados TAG exigem browser: WebFetch retorna scripts, mas JSON-LD e grades so existem no DOM renderizado."
when_to_use: "Extrair dados de paginas que renderizam certificados via JavaScript"
keywords: [tag_grading, dynamic_scraping, json_ld, structured_data, playwright]
long_tails:
  - "Como extrair JSON-LD de pagina CSR com browser automation"
  - "Quando WebFetch falha em certificados renderizados por JS"
axioms:
  - "SEMPRE validar se a pagina e CSR antes de fechar scraping"
  - "NUNCA assumir ausencia de schema se HTML inicial vem vazio"
linked_artifacts:
  primary: null
  related: [p01_kc_claude_server_tools]
density_score: 1.0
data_source: "Analise de pagina TAG Grading T9403163 — fetch estatico bloqueado"
---

## Quick Reference

topic: structured data extraction | scope: TAG certificates | criticality: high
page alvo: T9403163 | bloqueio: fetch estatico | decisao: browser automation

## Conceitos Chave

- WebFetch retornou scripts, sem certificado completo
- JSON-LD e grades surgem somente apos render JS
- Paginas CSR pedem DOM final, nao HTML de resposta
- Browser automation elimina falso negativo de schema

## Comparativo

| Metodo | Captura metas | Captura grade | Custo | Escala |
|--------|---------------|---------------|-------|--------|
| Fetch estatico | Baixa | Nula | Minimo | Alta |
| Browser render | Alta | Alta | Medio | Media |
| Inspecao manual | Media | Alta | Alto (h/h) | Nula |
| API discovery | Alta | Alta | Minimo | Alta |
| Network trace | Alta | Media | Baixo | Baixa |

| Sinal no HTML | Diagnostico | Proxima acao |
|---------------|-------------|--------------|
| So scripts/analytics | CSR provavel | Usar browser |
| IDs sem payload | Dados via API/XHR | Network trace |
| OG/JSON-LD ausentes | Render pendente | Esperar DOM |
| 200 OK body vazio | SPA puro | Playwright wait |
| 403 ou captcha | Anti-bot ativo | Headers + proxy |

| Ferramenta | JS render | Setup | Paralelismo |
|------------|-----------|-------|-------------|
| Playwright | Sim | Medio | Alto |
| Puppeteer | Sim | Medio | Alto |
| Selenium | Sim | Alto | Limitado |
| curl/httpx | Nao | Minimo | Alto |
| Firecrawl | Sim | SaaS | Alto |

## Regras de Ouro

- SEMPRE esperar DOM final antes de extrair schema
- SEMPRE inspecionar Network se body vier vazio
- NUNCA marcar pagina como "sem schema" no 1o fetch
- SEMPRE salvar screenshot e HTML para auditoria

## Code

<!-- lang: python | purpose: render page then extract structured data -->
```python
from playwright.sync_api import sync_playwright

def extract_after_render(url: str) -> dict:
    with sync_playwright() as p:
        page = p.chromium.launch().new_page()
        page.goto(url, wait_until="networkidle")
        return {
            "html": page.content(),
            "json_ld": page.locator(
                "script[type='application/ld+json']"
            ).all_text_contents(),
            "meta_count": page.locator("meta").count(),
        }
```

## References

- external: https://my.taggrading.com/card/T9403163
- external: https://playwright.dev/python/docs/intro
- external: https://schema.org/
- deepens: p01_kc_claude_server_tools


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating
