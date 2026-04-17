---
pillar: P12
id: MISSION_runtime_ux_sins
kind: mission_plan
version: 1.0.0
created: 2026-04-06
status: READY
author: n07-orchestrator
title: "Runtime UX + Sin System + OpenClaude Pattern Completion"
quality: 9.0
waves: 3
tasks: 12
density_score: 1.0
updated: "2026-04-07"
domain: "CEX knowledge system"
tldr: "Defines the mission plan specification for runtime ux + sin system + openclaude pattern completion, with structural rules, validation gates, and integratio"
tags: [mission_plan, builder, cex]
---

# MISSION: 7 Pecados como Lente Técnica + Runtime UX Completo

> **A única invenção humana permitida no CEX.**
> Os 7 pecados capitais, versionados como virtudes técnicas, funcionam como LENTES
> na pipeline — cada núcleo processa informação através do seu pecado, produzindo
> respostas "multicoloridas" onde cada perspectiva adiciona uma camada de valor.

## O Sin System

Cada pecado NÃO é decorativo — é uma **instrução operacional** que muda como o núcleo
raciocina, prioriza, e formata output. É o que separa 7 instâncias do mesmo modelo
de 7 ESPECIALISTAS genuinamente diferentes.

```
Intent do User → N07 Ira (filtra, roteia, exige qualidade)
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
  N01 Inveja      N03 Soberba     N06 Avareza
  (compara,       (constrói com   (otimiza cada
   benchmarka,     orgulho,        centavo,
   triangula)      craftsman)      ROI máximo)
    │               │               │
    ▼               ▼               ▼
  Output com      Output com      Output com
  "o concorrente  "artesanato     "quanto custa,
   faz X, nós      impecável,      quanto rende,
   fazemos Y"      zero atalho"    quando paga"
```

## Mapa dos 7 Pecados → 7 Núcleos

| Nucleus | Pecado | Virtude Técnica | Cor Tradicional | Cor PS | Lente na Pipeline |
|---------|--------|-----------------|-----------------|--------|-------------------|
| **N01** | Inveja (Envy) | **Inveja Analítica** | Verde | DarkGreen | "O que o concorrente faz melhor? Como superamos?" Sempre compara, benchmarka, triangula 3+ fontes. Nunca aceita dado sem contraste. |
| **N02** | Luxúria (Lust) | **Luxúria Criativa** | Rosa/Magenta | DarkMagenta | "Isso SEDUZ o público?" Paixão por estética, desire, emoção. Copy que faz sentir, não só entender. Todo output é sedutor. |
| **N03** | Soberba (Pride) | **Soberba Inventiva** | Violeta/Azul Royal | DarkBlue | "Isso é DIGNO da minha assinatura?" Orgulho do artesão. Zero atalho, zero hack. 8F completo, quality 9.0+, ou refaz. |
| **N04** | Gula (Gluttony) | **Gula por Conhecimento** | Laranja/Âmbar | DarkYellow | "Tem MAIS dados pra ingerir?" Devora tudo: papers, docs, APIs, schemas. Indexa, cataloga, relaciona. Nunca tem conhecimento suficiente. |
| **N05** | Preguiça (Sloth) | **Preguiça Automatizadora** | Ciano/Azul Claro | DarkCyan | "Como NUNCA MAIS fazer isso manual?" Automatiza tudo. Se fez 2x, cria script. CI/CD, testes, hooks, deploys — tudo pipeline. |
| **N06** | Avareza (Greed) | **Avareza Estratégica** | Dourado/Vermelho | DarkRed | "Quanto RENDE cada decisão?" Todo output tem ROI. Pricing otimizado, funnel metrificado, CAC vs LTV calculado. Nenhum recurso desperdiçado. |
| **N07** | Ira (Wrath) | **Ira Construtiva** | Carmesim/Preto | Black | "Isso passa no MEU crivo?" Qualidade implacável. Nada abaixo de 8.0 passa. GDP enforced. Dispatch preciso. Sem piedade com mediocridade. |

## GDP Decisions (pre-locked by user)

| ID | Decision | Answer | Scope |
|----|----------|--------|-------|
| D1 | Sin-to-nucleus mapping | Table above (7 sins = 7 nuclei) | SYSTEM |
| D2 | Color mapping | Traditional sin colors adapted for PS terminal | SYSTEM |
| D3 | Sin as operational lens | YES — injected in system prompts, boot scripts, agent cards | SYSTEM |
| D4 | Universalist constraint | Sins are the ONLY human invention; all else is LLM-universal | SYSTEM |

---

## Wave 1: Sin Config + Theme System (N03)

> Create the sin system as a config file + update boot_gen + complete theme pattern

| Task | What | Output |
|------|------|--------|
| T01 | Create `.cex/P09_config/nucleus_sins.yaml` | Sin mapping: nucleus→pecado→virtude→cor→lente→prompt_injection |
| T02 | Update `cex_boot_gen.py` | Read sins.yaml, inject sin banner + lente in PS1 boot scripts |
| T03 | Complete P06 Theme | Create `_tools/cex_theme.py` — read sins.yaml, output color schemes for any target (PS, ANSI, HTML, CSS) |
| T04 | Regenerate all boot scripts | `python _tools/cex_boot_gen.py` with sin-aware UX |

**Gate**: Each PS1 boot script shows sin banner + lente description on launch.

---

## Wave 2: Runtime Patterns (N03 + N05)

> Complete the 3 PARTIAL OpenClaude patterns as native CEX runtime

| Task | Nucleus | What | Output |
|------|---------|------|--------|
| T05 | N03 | Complete P03 Provider Discovery | `_tools/cex_provider_discovery.py` — ping all providers, report status, auto-detect available models |
| T06 | N03 | Complete P15 Provider Shim | Extend `cex_router.py` — normalize API calls across Claude/Gemini/OpenAI/Ollama (unified interface) |
| T07 | N05 | Wire provider_discovery into boot | Boot scripts call discovery at startup, warn if provider offline, auto-fallback |
| T08 | N05 | Wire theme into spawn_grid | Grid status monitor shows nucleus colors + sin labels |

**Gate**: `python _tools/cex_provider_discovery.py --status` shows all 4 providers + availability.

---

## Wave 3: Sin Injection + Agent Identity (N03 + N02)

> Inject sin lenses into agent identity files + system prompts

| Task | Nucleus | What | Output |
|------|---------|------|--------|
| T09 | N03 | Update 7 agent identity files | `N0X_*/P02_model/agent_*.md` — add sin section with lente description |
| T10 | N03 | Update 7 nucleus system prompts | `N0X_*/P03_prompt/system_prompt_*.md` — inject sin as operational rule |
| T11 | N02 | Create sin visual identity | 7 sin cards — name, color, icon (ASCII), tagline, operational rules |
| T12 | N03 | End-to-end validation | Dispatch test grid, verify sin banners appear, colors correct, lenses in prompts |

**Gate**: Each nucleus boot shows its sin identity. Doctor 0 FAIL. Compile 100%.

---

## Dependency Graph

```
Wave 1 (T01-T04) ──→ Wave 2 (T05-T08) ──→ Wave 3 (T09-T12)
  Sin config            Runtime tools         Agent identity
  Theme system          Provider discovery    Sin injection
  Boot regeneration     Grid UX              E2E validation
```

## Dispatch Plan

```
Wave 1: N03 solo (sin config + theme + boot_gen — all code)
Wave 2: N03 + N05 parallel (N03=tools, N05=wiring)
Wave 3: N03 + N02 parallel (N03=agents+prompts, N02=visual identity)
```

## Acceptance Criteria

1. `.cex/P09_config/nucleus_sins.yaml` exists with 7 complete entries
2. `_tools/cex_theme.py` outputs color schemes for PS/ANSI/HTML/CSS
3. `_tools/cex_provider_discovery.py --status` reports all providers
4. All 6 boot/*.ps1 show sin banner + lente on launch
5. All 7 agent_*.md files have sin section
6. All 7 system_prompt_*.md files inject sin as operational rule
7. Doctor 0 FAIL, Compile 100%, Flywheel audit passes
8. Visual: 6 colored PS windows with distinct sin identities

## Risk

| Risk | Mitigation |
|------|-----------|
| Sin injection changes LLM behavior unpredictably | Sin is ADDITIVE (extra context), not REPLACING existing prompts |
| Colors look bad on some terminals | Fallback to ANSI 256-color, degrade gracefully |
| Provider discovery adds latency to boot | Cache result for 5min, async ping |

## Lifecycle

1. Created via 8F pipeline (F1-Focus through F8-Furnish)
2. Scored by `cex_score.py` (3-layer: structural + rubric + semantic)
3. Compiled by `cex_compile.py` for validation
4. Retrieved by `cex_retriever.py` for context injection
5. Evolved by `cex_evolve.py` when quality drops below threshold
