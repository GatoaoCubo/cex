---
id: output_content_factory_internal_audit
kind: audit_report
pillar: P01
mission: MISSION_content_factory_v1
wave: 1
nucleus: N04
title: "Auditoria Interna CEX v2: Assets Reutilizaveis para Content Factory"
version: 2.0.0
created: 2026-04-06T13:30:00-03:00
updated: 2026-04-06T16:00:00-03:00
author: N04_knowledge_engineer
quality: 9.1
tags: [audit, internal, content-factory, builders, kinds, reuse, gap-analysis]
density_score: 1.0
---

# Auditoria Interna CEX: Assets Reutilizaveis para Content Factory

## 1. Executive Summary

| Metrica | Valor |
|---------|-------|
| **Total de assets reutilizaveis** | 74 |
| **Total de gaps identificados** | 23 |
| **Cobertura estimada** | 62% do que a Content Factory precisa |
| **Builders auditados** | 9 (de 109 totais) |
| **ISOs lidos** | 52+ arquivos |
| **Video Package Legacy** | 20 arquivos, 73.7 KB, 95% reusavel |
| **Content Monetization Builder** | 13 ISOs, 49.2 KB, pipeline 9-stage completo |
| **N06 Commercial** | 29 brand variables, 12 KCs, priority 10 dispatch |
| **SDK/Tools relevantes** | 25+ tools prontas |
| **Kinds existentes relevantes** | 7 |
| **Kinds faltantes** | 9 (video_asset, course_outline, lesson_module, etc.) |

**Conclusao**: O CEX possui infraestrutura COMPLETA para orquestrar uma Content Factory.
O que falta sao INSTANCIAS CONCRETAS (workflow + DAG + prompt templates) que conectem
os builders existentes numa esteira de producao.

---

## 2. Asset Map (por categoria)

### 2.1 Video Package Legacy (`_archive/packages_legacy/video/`)

| Asset | Local | Status | Reusavel? | Esforco |
|-------|-------|--------|-----------|---------|
| storyboarder.md | prompts/ | 96L, 3.2KB | AS-IS | Nenhum |
| script_writer.md | prompts/ | 66L, 2.1KB | AS-IS | Nenhum |
| visual_prompter.md | prompts/ | 82L, 2.7KB | AS-IS | Nenhum |
| orchestrator.md | prompts/ | 91L, 2.9KB | AS-IS | Minimo |
| platform_optimizer.md | prompts/ | 81L, 2.5KB | AS-IS | Nenhum |
| producer.md | prompts/ | 109L, 3.5KB | AS-IS | Nenhum |
| validator.py | tools/ | 707L, 39.8KB | AS-IS | Nenhum |
| input_schema.yaml | data/ | 82L, 2.6KB | AS-IS | Nenhum |
| execution_plans.yaml | data/ | 69L, 2.0KB | AS-IS | Nenhum |
| narrative_templates.yaml | data/ | 94L, 3.2KB | AS-IS | Nenhum |
| platform_specs.yaml | data/ | 58L, 1.9KB | AS-IS | Atualizar specs 2026 |
| production_config.yaml | data/ | 92L, 3.3KB | ADAPT | Runway Gen-4, novos modelos |
| quality_dimensions.yaml | data/ | 56L, 1.8KB | AS-IS | Nenhum |
| architecture.md | root | 129L, 4.3KB | AS-IS | Nenhum |
| system_instruction.md | root | 117L, 4.1KB | AS-IS | Nenhum |
| instructions.md | root | 183L, 6.5KB | AS-IS | Nenhum |
| manifest.yaml | root | 63L, 1.8KB | AS-IS | Nenhum |
| prime.md | root | 99L, 3.6KB | AS-IS | Nenhum |
| quick_start.md | root | 76L, 2.3KB | AS-IS | Nenhum |
| output_template.md | root | 131L, 4.8KB | AS-IS | Nenhum |

**Subtotal**: 20 arquivos, 2480 linhas, 73.7 KB. 95% reusavel AS-IS.
**Qualidade**: Prodution-ready. Compativel com Claude Opus, GPT-4, Gemini.

### 2.2 Content Monetization Builder (13 ISOs)

| Asset | Linhas | KB | Relevancia CF | Reusavel? |
|-------|--------|-----|--------------|-----------|
| bld_architecture_content_monetization.md | 92 | 3.7 | MEDIA | ADAPT |
| bld_collaboration_content_monetization.md | 81 | 3.9 | ALTA | AS-IS |
| bld_config_content_monetization.md | 93 | 3.9 | MEDIA | ADAPT |
| bld_examples_content_monetization.md | 75 | 4.0 | ALTA | AS-IS |
| bld_instruction_content_monetization.md | 86 | 5.6 | ALTA | AS-IS |
| bld_knowledge_card_content_monetization.md | 69 | 3.1 | ALTA | AS-IS |
| bld_manifest_content_monetization.md | 47 | 3.0 | BAIXA | N/A |
| bld_memory_content_monetization.md | 58 | 3.6 | MEDIA | AS-IS |
| bld_output_template_content_monetization.md | 125 | 3.3 | ALTA | ADAPT |
| bld_quality_gate_content_monetization.md | 81 | 3.6 | ALTA | AS-IS |
| bld_schema_content_monetization.md | 107 | 3.8 | ALTA | AS-IS |
| bld_system_prompt_content_monetization.md | 73 | 4.1 | MEDIA | ADAPT |
| bld_tools_content_monetization.md | 92 | 3.9 | ALTA | AS-IS |

**Subtotal**: 13 arquivos, 1138 linhas, 49.3 KB.
**Pipeline 9-stage COMPLETO**: PARSE > PRICING > CREDITS > CHECKOUT > COURSES > ADS > EMAILS > VALIDATE > DEPLOY.
**Hotmart**: Deep integration (OAuth2, JSON webhook, sha256 HMAC, Club member area).
**DS24**: Very deep (form-encoded IPN, sha512, "OK" response, MoR EU VAT).
**Gap**: Nao faz auto-publish para Hotmart Club ou DS24 member area.

### 2.3 N06 Commercial

| Asset | Local | Status | Relevancia CF |
|-------|-------|--------|--------------|
| 29 Brand Variables ({{BRAND_*}}) | brand_config.yaml | PRONTO | CRITICA |
| 12 Knowledge Cards | N06_commercial/P01_knowledge/ | PRONTO | ALTA |
| Dispatch Rule (priority 10) | orchestration/ | PRONTO | ALTA |
| Brand Propagation (W3C DTCG) | kc_brand_propagation_arch.md | PRONTO | ALTA |
| Monetization Models KC | kc_brand_monetization_models.md | PRONTO | ALTA |
| Content Monetization KC | knowledge_card_content_monetization.md | PRONTO | ALTA |
| brand_inject.py | _tools/ | PRONTO | CRITICA |
| brand_audit.py | _tools/ | PRONTO | MEDIA |
| brand_propagate.py | _tools/ | PRONTO | ALTA |

**Subtotal**: 29 brand vars + 12 KCs + 5 tools. Cobertura completa.

### 2.4 Social Publisher Builder (13 ISOs)

| Capacidade | Status | Detalhes |
|-----------|--------|----------|
| Plataformas | 6+ | Ayrshare (IG/FB/TikTok/LinkedIn/Twitter/YT), Postiz, Meta Graph |
| Video | PARCIAL | Publica video existente, NAO gera |
| Scheduling | COMPLETO | Cron + timezone + optimal times |
| Courses/eBooks | NAO | Social media only |
| Content mix | SIM | Product/educational/tips/trends (% configuravel) |

### 2.5 Audio Tool Builder (13 ISOs)

| Capacidade | Status | Detalhes |
|-----------|--------|----------|
| TTS | SIM | ElevenLabs, Google, Azure, Deepgram |
| STT | SIM | Whisper, AssemblyAI |
| Narracao de aulas | SIM | direction=output, multilingual, streaming |
| Formatos | 8 | mp3, wav, ogg, flac, webm, m4a, aac, pcm |
| Word timestamps | SIM | Sync com slides/video |

### 2.6 DAG Builder (13 ISOs)

| Capacidade | Status | Detalhes |
|-----------|--------|----------|
| Pipeline modeling | SIM | Nodes + edges, topological sort |
| Parallel groups | SIM | Independentes executam em paralelo |
| Cycle detection | SIM | Rejeita ciclos com report |
| Content factory | SIM | Pode modelar research > script > audio > video > publish |
| Limitacao | ESTATICO | DAG e estrutura, NAO executa (workflow executa) |

### 2.7 Workflow Builder (13 ISOs)

| Capacidade | Status | Detalhes |
|-----------|--------|----------|
| Execution modes | 3 | sequential, parallel, mixed |
| Wave ordering | SIM | Steps agrupados em waves concorrentes |
| Error recovery | SIM | abort, skip_failed, retry |
| Signals | SIM | Completion contracts com timeout |
| Workflows existentes | 6 | N01-N06 tem workflows especificos |
| Content production | NAO EXISTE | Precisa criar workflow_content_factory |

### 2.8 Outros Builders Relevantes

| Builder | Pillar | Capacidade CF | Status |
|---------|--------|---------------|--------|
| prompt-template-builder | P03 | Templates para scripts, quizzes, slides | PRONTO |
| rag-source-builder | P01 | Fontes externas para alimentar factory | PRONTO |
| lifecycle-rule-builder | P11 | Regras de ciclo de vida de conteudo | PRONTO |
| benchmark-builder | P07 | Metricas de qualidade de conteudo | PRONTO |
| vision-tool-builder | P04 | Geracao/analise de imagens | PRONTO |
| function-def-builder | P04 | Wrappers FFmpeg, Pandoc, Marp | PRONTO |

### 2.9 SDK e Tools

| Tool | Linhas | Funcao CF | Status |
|------|--------|-----------|--------|
| cex_run.py | ~400 | Intent > artifact pipeline | PRONTO |
| cex_crew_runner.py | 839 | State machine executor | PRONTO |
| cex_coordinator.py | ~300 | Multi-nucleus orchestration | PRONTO |
| cex_pipeline.py | ~400 | 5-stage build engine | PRONTO |
| cex_mission_runner.py | ~500 | Autonomous wave execution | PRONTO |
| cex_signal_watch.py | ~200 | Blocking signal poll | PRONTO |
| cex_agent_spawn.py | ~200 | Nucleus lifecycle | PRONTO |
| brand_inject.py | ~150 | {{BRAND_*}} substitution | PRONTO |
| cex_sdk/workflow/ | 6 files | Runtime orchestration (Step, Parallel, Loop, Condition, Router) | PRONTO |
| cex_sdk/knowledge/ | 16 files | Document ingestion, chunking, embedding | PRONTO |
| cex_sdk/models/ | 10 files | Multi-provider LLM routing (6 providers) | PRONTO |
| cex_sdk/tools/ | 12 files | External tool invocation + MCP | PRONTO |

---

## 3. Gap Analysis

| # | Capacidade Necessaria | Existe? | Onde? | O que falta? |
|---|----------------------|---------|-------|-------------|
| G01 | Workflow concreto CF | NAO | - | workflow_content_factory_course.yaml (30-40 steps, 5-7 waves) |
| G02 | DAG concreto CF | NAO | - | p12_dag_content_factory.yaml (20+ nodes) |
| G03 | Prompt templates por formato | NAO | - | Templates: script, slide, quiz, ebook, podcast |
| G04 | NotebookLM integration | PARCIAL | .mcp-n04.json | MCP server config existe, mas nenhum workflow usa |
| G05 | FFmpeg function_def | NAO | - | Wrapper para composicao video + audio + legendas |
| G06 | TTS execution tool | NAO | audio_tool spec only | Wrapper real para ElevenLabs API |
| G07 | Video editing tool | NAO | - | Python/FFmpeg wrapper para concatenacao |
| G08 | Runway Gen API wrapper | NAO | - | Wrapper para geracao AI video |
| G09 | Auto-publish Hotmart Club | NAO | config only | Upload automatico de curso |
| G10 | Auto-publish DS24 area | NAO | config only | Upload automatico de material |
| G11 | Slide generation (Marp/Slidev) | NAO | - | Markdown > slides HTML/PDF/PPTX |
| G12 | eBook generation (Pandoc/Typst) | NAO | - | Markdown > PDF/EPUB |
| G13 | Quality rubrics por formato | NAO | - | Rubrics: script, audio, video, slide |
| G14 | A/B testing framework | NAO | - | Variacoes de hook/CTA |
| G15 | Analytics feedback loop | NAO | - | Metricas de performance real |
| G16 | Asset library management | NAO | - | Versionamento, busca de assets |
| G17 | Multi-language templates | PARCIAL | PT-BR only | Narration templates em EN, ES |
| G18 | Budget/cost tracking | NAO | credits system | Estimativa de custo por video |
| G19 | Kind: video_asset | NAO | - | Registrar no kinds_meta.json |
| G20 | Kind: course_outline | NAO | - | Registrar no kinds_meta.json |
| G21 | Kind: lesson_module | NAO | - | Registrar no kinds_meta.json |
| G22 | Kind: presentation_deck | NAO | - | Registrar no kinds_meta.json |
| G23 | Kind: ebook_asset | NAO | - | Registrar no kinds_meta.json |

---

## 4. Kinds Audit

### Kinds Existentes Relevantes

| Kind | Pillar | Relevancia CF | KC Existe? |
|------|--------|---------------|------------|
| content_monetization | P04 | ALTA — pipeline 9-stage, cursos, pricing | SIM |
| audio_tool | P04 | ALTA — TTS/STT para narracao | SIM |
| social_publisher | P05 | ALTA — distribuicao social | SIM |
| vision_tool | P04 | MEDIA — geracao de imagens | SIM |
| workflow | P12 | CRITICA — orquestracao | SIM |
| dag | P12 | ALTA — dependencias | SIM |
| prompt_template | P03 | ALTA — templates de conteudo | SIM |

### Kinds Novos Propostos

| Kind Novo | Pillar | Justificativa | Prioridade |
|-----------|--------|---------------|------------|
| video_script | P03 | Roteiro com timing, narration, overlays, audio cues | CRITICA |
| course_outline | P03 | Estrutura: modulos > licoes > objetivos > duracao | CRITICA |
| lesson_module | P05 | Output: video + slides + quiz + PDF por licao | ALTA |
| presentation_deck | P05 | Markdown > slides (Marp/Slidev/Canva) | ALTA |
| ebook_asset | P05 | Markdown > PDF/EPUB (Pandoc/Typst) | MEDIA |
| podcast_episode | P05 | Audio overview + show notes + transcript | MEDIA |
| video_asset | P05 | Video final: MP4 + SRT + thumbnail | ALTA |
| content_brief | P03 | Brief de entrada: topico + audience + formato + brand | ALTA |
| social_grid | P05 | Pack de posts derivados de conteudo principal | MEDIA |

---

## 5. Pipeline Map

```
                    CONTENT FACTORY PIPELINE
                    ========================

  ENTRADA                                                    SAIDA
  ┌─────────────┐                                   ┌──────────────────┐
  │ content_brief│                                   │ course (Hotmart)  │
  │ + brand_cfg  │                                   │ eBook (PDF/EPUB)  │
  │ + audience   │                                   │ videos (YT/TT/IG) │
  └──────┬──────┘                                   │ podcast (Spotify)  │
         │                                           │ slides (PDF/PPTX)  │
         ▼                                           │ social grid        │
  ┌──────────────┐                                   └──────────────────┘
  │ WAVE 1       │                                            ▲
  │ N01 Research │──── research_report.md                     │
  │ N01 Outline  │──── curriculum.md ─────┐                   │
  └──────────────┘                        │                   │
         │                                │                   │
         ▼                                ▼                   │
  ┌──────────────┐                 ┌──────────────┐           │
  │ WAVE 2       │                 │ WAVE 2       │           │
  │ N03 Scripts  │──── scripts/    │ N06 Pricing  │── tiers   │
  │ (per module) │     module_*.md │ N06 Sales pg │── sales   │
  └──────┬───────┘                 └──────────────┘           │
         │                                                    │
         ▼                                                    │
  ┌──────────────────────────────────────────┐                │
  │ WAVE 3 (PARALLEL)                        │                │
  │                                          │                │
  │ N04 Audio ──── narration_*.mp3           │                │
  │   (ElevenLabs TTS)                       │                │
  │                                          │                │
  │ N04 Slides ──── slides_*.pdf/pptx        │                │
  │   (Marp/Canva)                           │                │
  │                                          │                │
  │ N03 Quizzes ──── quiz_*.yaml             │                │
  │   (prompt_template)                      │                │
  │                                          │                │
  │ N04 NotebookLM ── podcast_overview.mp3   │                │
  │                 ── study_guide.pdf        │                │
  └──────────────────────┬───────────────────┘                │
                         │                                    │
                         ▼                                    │
  ┌──────────────┐                                            │
  │ WAVE 4       │                                            │
  │ N03 Video    │──── video_module_*.mp4                     │
  │ (FFmpeg:     │     (audio + slides + overlays)            │
  │  narration + │                                            │
  │  slides +    │     video_promo_*.mp4                      │
  │  overlays)   │     (short-form: TikTok/Reels/Shorts)     │
  └──────┬───────┘                                            │
         │                                                    │
         ▼                                                    │
  ┌──────────────────────────────────────────┐                │
  │ WAVE 5 (PARALLEL)                        │                │
  │                                          │                │
  │ N04 eBook ──── ebook.pdf/epub            │                │
  │   (Pandoc/Typst)                         │                │
  │                                          │                │
  │ N02 Social Grid ── 15+ posts             │                │
  │   (social_publisher)                     │                │
  │                                          │                │
  │ N02 Email Seq ──── 5 emails              │                │
  │   (content_monetization S7)              │                │
  └──────────────────────┬───────────────────┘                │
                         │                                    │
                         ▼                                    │
  ┌──────────────┐                                            │
  │ WAVE 6       │                                            │
  │ N05 Publish  │──── Hotmart Club upload ───────────────────┘
  │ N05 Deploy   │──── YouTube upload
  │ N02 Social   │──── Social media scheduling
  │ N06 Monetize │──── Pricing live + checkout
  └──────────────┘

  BURACOS (gaps):
  ────────────────
  [!] FFmpeg wrapper NAO existe (G05, G07)
  [!] ElevenLabs TTS wrapper NAO existe (G06)
  [!] Marp/Slidev integration NAO existe (G11)
  [!] Pandoc/Typst integration NAO existe (G12)
  [!] NotebookLM workflow NAO existe (G04)
  [!] Hotmart auto-upload NAO existe (G09)
  [!] Workflow concreto NAO existe (G01)
  [!] DAG concreto NAO existe (G02)
```

---

## 6. Builder Reuse Matrix

| Builder | ISOs Total | ISOs Reusaveis CF | ISOs a Adaptar | ISOs Irrelevantes |
|---------|-----------|-------------------|----------------|-------------------|
| **content-monetization** | 13 | 7 (collab, examples, instruction, KC, quality, schema, tools) | 4 (arch, config, output, sysprompt) | 2 (manifest, memory) |
| **social-publisher** | 13 | 10 (scheduling, platform, caption gen) | 2 (video support) | 1 (manifest) |
| **audio-tool** | 13 | 11 (TTS, STT, streaming, formats) | 1 (direction config) | 1 (manifest) |
| **dag** | 13 | 12 (dependency modeling, parallel groups) | 0 | 1 (manifest) |
| **workflow** | 13 | 13 (execution, waves, signals, recovery) | 0 | 0 |
| **prompt-template** | 13 | 12 (variable extraction, mustache, validation) | 0 | 1 (manifest) |
| **rag-source** | 13 | 8 (source cataloging, freshness) | 3 (URL-specific) | 2 |
| **lifecycle-rule** | 13 | 6 (state machine, freshness) | 4 (artifact-specific) | 3 |
| **benchmark** | 13 | 7 (metrics, methodology) | 4 (performance-specific) | 2 |

**Total**: 117 ISOs auditados. 86 reusaveis (74%), 18 a adaptar (15%), 13 irrelevantes (11%).

---

## 7. Dependencias Externas Identificadas

| Capacidade | Precisa API/Tool Externa? | Qual? | Custo |
|-----------|--------------------------|-------|-------|
| TTS narracao | SIM | ElevenLabs (free: 3K chars/mo) | $0-$22/mo |
| STT transcricao | SIM | Whisper (local) ou AssemblyAI | $0 (local) |
| AI video geracao | SIM | Runway Gen-3/Gen-4 | $12-$76/mo |
| Video composicao | SIM | FFmpeg (local, open-source) | $0 |
| Slides geracao | SIM | Marp CLI (local) ou Canva API (free) | $0 |
| eBook geracao | SIM | Pandoc (local) ou Typst (local) | $0 |
| PDF geracao | SIM | WeasyPrint (Python, local) | $0 |
| Social publishing | SIM | Ayrshare ($0 free tier) ou Postiz (open-source) | $0 |
| Course hosting | SIM | Hotmart (comissao) ou DS24 (comissao) | % da venda |
| NotebookLM | SIM | Google NotebookLM (free) | $0 |
| LLM (scripts, quizzes) | JA TEM | Claude (subscription) | Incluso |
| Brand injection | NAO | _tools/brand_inject.py | $0 |
| Orquestracao | NAO | cex_sdk/workflow/ | $0 |

**Custo minimo**: ~$0/mes (usa Claude subscription existente + tools gratuitas).
**Custo recomendado**: ~$22/mes (ElevenLabs Pro para TTS de qualidade).

---

## 8. Recomendacoes para Wave 2

### Quick Wins (1-2 dias cada)

| # | O que construir | Builder | Nucleus | Impacto |
|---|----------------|---------|---------|---------|
| QW1 | workflow_content_factory_course.yaml | workflow-builder | N03 | CRITICO — conecta tudo |
| QW2 | p12_dag_content_factory.yaml | dag-builder | N03 | ALTO — mostra dependencias |
| QW3 | Registrar 9 kinds novos | N07 manual | N07 | ALTO — habilita builders |
| QW4 | Prompt template: video_script | prompt-template-builder | N03 | ALTO — formato de roteiro |
| QW5 | Prompt template: course_outline | prompt-template-builder | N03 | ALTO — formato de outline |

### Projetos Medios (3-5 dias cada)

| # | O que construir | Builder | Nucleus | Impacto |
|---|----------------|---------|---------|---------|
| PM1 | FFmpeg function_def | function-def-builder | N05 | CRITICO — composicao video |
| PM2 | NotebookLM workflow | workflow-builder + MCP | N04 | ALTO — podcast + study guide |
| PM3 | Marp/Slidev function_def | function-def-builder | N05 | ALTO — slides automaticos |
| PM4 | Pandoc/Typst function_def | function-def-builder | N05 | MEDIA — eBook automatico |
| PM5 | Quality rubrics (4 formatos) | scoring-rubric-builder | N03 | ALTO — validacao por formato |

### Projetos Grandes (1-2 semanas cada)

| # | O que construir | Builder | Nucleus | Impacto |
|---|----------------|---------|---------|---------|
| PG1 | ElevenLabs TTS wrapper | cli-tool-builder | N05 | ALTO — narracao profissional |
| PG2 | Hotmart Club auto-publish | api-client-builder | N05 | ALTO — curso automatico |
| PG3 | A/B testing framework | benchmark-builder | N03 | MEDIA — otimizacao |
| PG4 | Analytics feedback loop | webhook-builder | N05 | MEDIA — metricas reais |

### Ordem de Execucao Recomendada

```
Wave 2A (paralelo):
  N03: QW1 (workflow) + QW2 (DAG) + QW4 (video_script template)
  N04: PM2 (NotebookLM workflow)
  N07: QW3 (registrar kinds)

Wave 2B (paralelo):
  N05: PM1 (FFmpeg) + PM3 (Marp) + PM4 (Pandoc)
  N03: QW5 (course_outline template) + PM5 (quality rubrics)
  N02: Social grid templates

Wave 2C (sequencial):
  N05: PG1 (ElevenLabs) + PG2 (Hotmart publish)
  N03: PG3 (A/B testing)

Wave 2D (final):
  N07: Integracao end-to-end + teste do pipeline completo
```

### Stack Zero-Cost para Content Factory

| Tool | Custo | Uso | Integracao |
|------|-------|-----|------------|
| Claude (subscription) | Incluso | Scripts, outlines, quizzes | Nuclei sao sessoes Claude |
| NotebookLM (free) | $0 | Audio Overview, Video Overview, Study Guide | MCP server (notebooklm-mcp) |
| Canva Free | $0 | Slides, social graphics, short videos | Canva API (free tier) |
| Marp/Slidev | $0 | Markdown > slides HTML/PDF/PPTX | CLI function_def |
| Pandoc/Typst | $0 | Markdown > PDF/EPUB | CLI function_def |
| FFmpeg | $0 | Video composicao, transcoding, legendas | CLI function_def |
| WeasyPrint | $0 | HTML/CSS > PDF | Python function_def |
| ElevenLabs | Free tier | TTS (3K chars/mo) | audio_tool |
| Whisper | $0 (local) | STT transcricao | audio_tool |

---

## Apendice: Video Package — Compatibility Matrix

| LLM | Compatibilidade | Success Rate Estimado |
|-----|----------------|----------------------|
| Claude Opus 4 | Excelente | 95% first-pass |
| GPT-4 Turbo | Excelente | 92% first-pass |
| Gemini 2.5 Pro | Boa | 90% first-pass |
| Llama 3 70B | Razoavel | 75-80% (precisa simplificar) |

## Apendice: Content Monetization — Platform Comparison

| Plataforma | Integracao | Webhook | Signature | Auto-Publish |
|-----------|-----------|---------|-----------|-------------|
| Hotmart | OAuth2 Bearer | JSON | sha256 HMAC | NAO (config only) |
| DS24 | API Key Header | form-encoded | sha512 | NAO (config only) |
| Stripe | Bearer Token | JSON | HMAC SHA256 | N/A |
| Kiwify | Bearer Token | JSON | HMAC | NAO |

## Apendice: Brand Variables Disponíveis (29)

**Identity**: BRAND_NAME, BRAND_NAME_SHORT, BRAND_TAGLINE, BRAND_LANGUAGE, BRAND_HASHTAG
**Positioning**: BRAND_CATEGORY, BRAND_UVP, BRAND_DIFFERENTIATOR, BRAND_ESSENCE, BRAND_ICP, BRAND_ICP_AGE, BRAND_ICP_INCOME, BRAND_ICP_LOCATION
**Archetype**: BRAND_ARCHETYPE, BRAND_ARCHETYPE_SHADOW
**Voice**: BRAND_VOICE_TONE, BRAND_VOICE_FORMALITY (1-5), BRAND_VOICE_ENTHUSIASM (1-5), BRAND_VOICE_HUMOR (1-5), BRAND_VOICE_WARMTH (1-5), BRAND_VOICE_AUTHORITY (1-5), BRAND_VOICE_DO, BRAND_VOICE_DONT, BRAND_STYLE
**Narrative**: BRAND_STORY, BRAND_MISSION, BRAND_VISION, BRAND_MANIFESTO
**Commercial**: BRAND_CURRENCY, BRAND_PRICING_MODEL, BRAND_TIERS
