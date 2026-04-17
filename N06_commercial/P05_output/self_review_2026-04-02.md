---
id: n06_self_review_20260402
kind: context-doc
nucleus: N06
pillar: P09
quality: 9.0
updated: 2026-04-07
date: 2026-04-02
type: self-review
author: n06_commercial
tags: [self-review, N06, brand, commercial, audit]
tldr: "N06 self-assessment: CEX is a product in development. Brand not-bootstrapped is correct product state. Focus on builder quality, tool robustness, onboarding UX."
---

# N06 Self-Review — 2026-04-02

> **Contexto**: CEX é um PRODUTO em desenvolvimento. Este time são os devs que constroem o cérebro X para depois ser adotado por empresas clientes. O estado "brand não bootstrapped" é o estado correto do produto — o cérebro sai em branco, o cliente preenche via `/init`. Auditorias devem focar em qualidade dos builders, robustez das ferramentas, e experiência de onboarding do cliente.

---

## Summary

| Item | Value |
|------|-------|
| Total artifacts (N06_commercial/) | 40 .md source + 13 compiled .yaml = **53** |
| Brand bootstrapped | **NO** — correto para produto em dev |
| `.cex/brand/brand_config.yaml` | Ausente — estado padrão do produto |
| Files com `{{BRAND_*}}` | **30** — templates por design |
| Brand tools funcionais | **2 / 5** (brand_inject, brand_ingest OK; 3 crasham no Windows) |
| Output templates (output/) | **9** — completos, aguardam client bootstrap |
| content-monetization-builder ISOs | **13 / 13** — completo |
| social-publisher-builder ISOs | **13 / 13** — completo, integração N02 indireta |
| Bootstrap paths implementados | **3 / 3** — chat, CLI, auto-detect |

---

## CRITICAL Gaps (must fix)

### 1. Três brand tools crasham no Windows — bug de produto

`brand_validate.py`, `brand_propagate.py`, `brand_audit.py` crasham com UnicodeEncodeError ao tentar imprimir o emoji ❌ no console Windows (cp1252).

```
UnicodeEncodeError: 'charmap' codec can't encode character '\u274c'
```

**Impacto real**: O cliente que adota o CEX no Windows e executa qualquer brand tool pela primeira vez recebe um Python traceback em vez de uma mensagem de erro clara. É o pior momento para crashar — é o onboarding. Os scripts detectam o problema corretamente (exit code 1) mas a mensagem some.

**Fix**: Substituir `\u274c` / `\u2705` por `[FAIL]` / `[OK]` / `[WARN]` em todos os prints das 3 ferramentas. Alternativa: forçar `PYTHONIOENCODING=utf-8` como pré-requisito documentado no README de instalação.

Arquivos afetados:
- `_tools/brand_validate.py` — linha 155
- `_tools/brand_propagate.py` — linha 151
- `_tools/brand_audit.py` — linha 283

---

## WARN Gaps (should fix)

### 2. Sem output templates de funil

`N06_commercial/P05_output/` tem 9 templates — nenhum para:
- **VSL** (Video Sales Letter) — estrutura de 8 seções documentada em `knowledge_card_commercial.md`, mas sem template output
- **Email sequence** — onboarding, upsell, churn prevention documentados nos ISOs do content-monetization-builder, sem template standalone
- **Landing page** (long-form sales page) — ausente
- **Order bump / OTO scripts** — ausente

`workflow_content_monetization.md` descreve pipeline de 9 steps (PARSE→…→ADS→EMAILS→DEPLOY) mas os stages ADS e EMAILS não têm artefatos output correspondentes.

### 3. social-publisher-builder → N02 não documentado diretamente

`bld_collaboration_social_publisher.md` define crews com knowledge-card-builder, prompt-template-builder, cli-tool-builder — mas **não** especifica handoff direto com N02_marketing para geração de captions em brand voice.

O fluxo correto para conteúdo social brand-aligned é: social-publisher-builder (pipeline + schedule) → N02 (captions no brand voice). Esse acoplamento está implícito mas não formalizado no bld_collaboration.

### 4. `output_transformation_arc.md` — conteúdo não verificado

O arquivo existe mas não foi confirmado se cobre o arco BEFORE/AFTER/THROUGH com âncora de pricing. Precisa de revisão para garantir alinhamento com a lógica de precificação por transformação do KC.

### 5. `boot/cex.cmd` auto-detect não verificado

O terceiro caminho de bootstrap (duplo-clique no boot/cex.cmd com auto-detect de estado) não foi testado nesta auditoria.

### 6. `cex_bootstrap.py --from-file` não verificado

O path de ingest via YAML (usado pelo PATH B do `/init`) não foi testado. É o caminho crítico quando o cliente tem materiais de marca existentes.

---

## Brand System Status

| Tool | Status | Notas |
|------|--------|-------|
| `brand_validate.py` | PARTIAL | Exit code correto (1), mas crash UnicodeEncodeError no Windows |
| `brand_propagate.py` | PARTIAL | Idem |
| `brand_audit.py` | PARTIAL | Idem |
| `brand_inject.py` | OK | Help carrega, `--check` funciona |
| `brand_ingest.py` | OK | Help carrega, folder scan disponível |
| `cex_bootstrap.py --check` | OK | Imprime "NOT BOOTSTRAPPED" sem emoji — funciona no Windows |
| `.cex/brand/brand_config_template.yaml` | EXISTS | Pronto para preencher |
| `.cex/brand/brand_config_schema.yaml` | EXISTS | Pronto para validar |

---

## Bootstrap Flow Status (produto entregue ao cliente)

| Caminho | Status | Notas |
|---------|--------|-------|
| `/init` chat (conversacional) | FUNCTIONAL | Documentado em `.claude/commands/init.md` — 4 rounds, 3 modos |
| `init.cmd` (double-click) | FUNCTIONAL | Verifica `.bootstrapped`, chama `cex_bootstrap.py` |
| `boot/n06.cmd` (N06 direto) | FUNCTIONAL | Carrega 10 KCs de brand, ativa brand discovery fallback |
| `boot/cex.cmd` (auto-detect) | NOT VERIFIED | Não testado nesta auditoria |
| `cex_bootstrap.py` (CLI interativo) | FUNCTIONAL | 13 perguntas, sem crash no Windows |
| `cex_bootstrap.py --from-file` | NOT VERIFIED | Path de YAML ingest não testado |
| `brand_ingest.py` (folder scan) | FUNCTIONAL | Capability presente |

---

## Monetization Readiness

| Área | Status | Evidência |
|------|--------|-----------|
| Frameworks de pricing | PRONTO (conhecimento) | `knowledge_card_commercial.md` — value-based, anchor, 3-tier, psicológico |
| Template pricing page | TEMPLATE | `output_pricing_page.md` — HTML com `{{BRAND_*}}`, aguarda cliente |
| Funnels (conhecimento) | PRONTO | VSL structure, benchmarks no KC |
| Templates de funil | AUSENTE | Sem VSL, email sequence, landing page |
| Course structure | FRAMEWORK | content-monetization-builder — pipeline 9 stages |
| Template de curso | AUSENTE | Sem course outline template standalone |
| Social publishing | BUILDER PRONTO | social-publisher-builder 13/13 ISOs |
| Social → N02 | INDIRETO | Via crew compositions, sem handoff spec direto |
| Mercado brasileiro | COBERTO | Hotmart, Kiwify, PIX, BRL, parcelamento no KC |
| Upsell architecture | CONHECIMENTO | Documentado no KC, sem template de artefato |

---

## Recommended Actions (priority order)

1. **[CRITICAL] Fix Unicode crash nas 3 brand tools** — Substituir emojis por ASCII nos prints de `brand_validate.py`, `brand_propagate.py`, `brand_audit.py`. Afeta todo cliente Windows no primeiro contato com o produto.

2. **[HIGH] Criar template VSL** — `N06_commercial/P05_output/output_vsl_template.md` com as 8 seções (hook, problem, revelation, proof, offer, CTA, guarantee, scarcity). Conhecimento existe no KC, falta o artefato output.

3. **[HIGH] Criar template email sequence** — `N06_commercial/P05_output/output_email_sequence.md` para onboarding, upsell, churn prevention. Coberto nos ISOs mas sem template standalone.

4. **[MEDIUM] Formalizar handoff social-publisher → N02** — Adicionar N02_marketing como crew partner direto em `bld_collaboration_social_publisher.md` com protocolo explícito: social-publisher-builder produz schedule → N02 escreve captions no brand voice do cliente.

5. **[MEDIUM] Verificar `boot/cex.cmd` auto-detect** — Confirmar que o terceiro caminho de bootstrap funciona conforme documentado no CLAUDE.md.

6. **[MEDIUM] Verificar `cex_bootstrap.py --from-file`** — Testar com um YAML mínimo para garantir que o PATH B do `/init` (cliente com materiais existentes) funciona end-to-end.

7. **[LOW] Revisar `output_transformation_arc.md`** — Confirmar cobertura do arco BEFORE/AFTER/THROUGH com lógica de pricing anchor.

---

## O que está BEM

- **content-monetization-builder**: 13/13 ISOs completos — builder robusto
- **social-publisher-builder**: 13/13 ISOs completos
- **knowledge_card_commercial.md** (q=9.0): pricing frameworks, benchmarks, mercado BR — excelente
- **workflow_content_monetization.md** (q=8.9): pipeline 9-step com retry e mock fallback
- **agent_commercial.md** (q=8.9): dual-role bem definido — Brand Architect + Revenue Engineer
- **Fluxo `/init`**: 3 modos (chat, ingest, reset), edge cases documentados, fluido
- **`cex_bootstrap.py`**: funciona no Windows sem crash — base sólida para onboarding
- **Templates de output (9)**: estrutura correta com `{{BRAND_*}}` — prontos para injeção
- **Brand KCs (10)**: archetypes, voice systems, frameworks, ICP, positioning, tokens — base de conhecimento densa
