---
id: p01_kc_tag_grading_structured_data
type: knowledge_card
lp: P01
title: "TAG Grading: Structured Data Extraction em Paginas CSR"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: SHAKA
domain: research
quality: null
tags: [tag-grading, structured-data, browser-automation, scraping, csr]
tldr: "Certificados TAG exigem browser automation: WebFetch pega scripts, mas JSON-LD, metas e grades vivem no DOM renderizado."
when_to_use: "Extrair dados de paginas de autenticacao ou certificados que renderizam no browser"
keywords: [tag_grading, dynamic_scraping, json_ld, structured_data, playwright]
long_tails:
  - "Como extrair JSON-LD de pagina CSR com browser automation"
  - "Quando WebFetch falha em certificados renderizados por JavaScript"
axioms:
  - "SEMPRE validar se a pagina e CSR antes de concluir scraping"
  - "NUNCA assumir ausencia de schema quando o HTML inicial vem incompleto"
linked_artifacts:
  primary: null
  related: [p01_kc_claude_server_tools]
density_score: null
data_source: "Analise de pagina TAG Grading T9403163 com tentativa blocked em fetch estatico"
---

## Quick Reference

topic: dynamic structured data | scope: TAG Grading certificates | criticality: high
page alvo: T9403163 | status: blocked em fetch estatico | decisao: usar browser

## Conceitos Chave

- WebFetch retornou scripts, nao o certificado completo
- JSON-LD, OG tags e grades podem surgir so apos render
- Cert pages com CSR pedem DOM final, nao HTML inicial
- Browser automation reduz falso negativo de schema

## Comparativo

| Metodo | Captura metas | Captura grade | Risco |
|--------|---------------|---------------|-------|
| Fetch estatico | Baixa | Baixa | Concluir "sem dados" cedo |
| Browser automation | Alta | Alta | Maior custo por execucao |
| Inspecao manual | Media | Alta | Nao escala |

| Sinal | Leitura |
|------|---------|
| So scripts no HTML | Provavel CSR |
| IDs conhecidos sem payload | Dados vem por API/JS |
| OG/JSON-LD ausentes | Esperar render ou network trace |

## Regras de Ouro

- SEMPRE esperar o DOM final antes de extrair schema
- SEMPRE inspecionar Network quando o body vier vazio
- NUNCA marcar pagina como "sem structured data" no 1o fetch
- SEMPRE salvar screenshot e HTML final para auditoria

## Code

<!-- lang: python | purpose: render page before extracting structured data -->
```python
from playwright.sync_api import sync_playwright

def extract_after_render(url: str) -> dict:
    with sync_playwright() as p:
        page = p.chromium.launch().new_page()
        page.goto(url, wait_until="networkidle")
        return {
            "html": page.content(),
            "json_ld": page.locator("script[type='application/ld+json']").all_text_contents(),
            "meta_count": page.locator("meta").count(),
        }
```

## References

- external: https://my.taggrading.com/card/T9403163
- external: https://playwright.dev/python/docs/intro
- external: https://schema.org/
- deepens: p01_kc_claude_server_tools
