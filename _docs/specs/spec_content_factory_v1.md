---
id: spec_content_factory_v1
kind: constraint_spec
pillar: P06
title: "Spec Content Factory v1 — Esteira Autonoma de Producao de Conteudo Digital"
version: 1.0.0
created: 2026-04-06
author: n07_orchestrator
domain: content-factory
quality_target: 9.0
status: READY
scope: ALL_NUCLEI
depends_on:
  - MISSION_content_factory_v1 (Wave 1 research — DONE)
  - MISSION_content_factory_wave2 (Wave 2 build — DONE)
tags: [spec, content-factory, video, course, ebook, presentation, podcast, canva, notebooklm, pipeline]
tldr: "Spec completa para Content Factory autonoma. Input: {{BRAND}} + brief. Output: videos, cursos, ebooks, apresentacoes, podcasts, posts. Zero kinds novos. Stack $0: Claude + NotebookLM + Canva Business + open-source tools."
density_score: 0.97
---

# Spec Content Factory v1 — A Maquina que Cria Conteudo

## VISAO

```
USER: "Quero um curso sobre CEX explicando 8F, 12 pillars e nuclei"
           |
           v
    CONTENT FACTORY (autonomo)
           |
           v
    7+ outputs prontos para publicar:
    - Curso (8 modulos com quiz)
    - Video demo 90s (Reels/TikTok)
    - Podcast (Audio Overview)
    - Apresentacao (slides PPTX/PDF)
    - eBook (PDF/EPUB)
    - Social posts (IG, LinkedIn, X, YouTube)
    - Landing page + checkout
```

**USER NAO FAZ NADA.** Nuclei fazem tudo de criacao a publicacao.

---

## PRINCIPIOS

1. **ZERO kinds novos.** 115 kinds existentes cobrem 100%. "Curso" = workflow + prompt_templates.
2. **Stack $0.** Claude (motor) + NotebookLM (gratis) + Canva Business (assinatura existente) + open-source.
3. **{{BRAND}} injection.** Todo output recebe identidade da marca automaticamente.
4. **8F em cada artefato.** Qualidade garantida pelo pipeline existente.
5. **Nuclei fazem tudo.** De research a publicacao, zero intervencao humana.

---

## STACK VALIDADA (todas testadas 2026-04-06)

### Ferramentas com API/Credenciais Confirmadas

| Ferramenta | Tipo | Status | Credencial | Custo |
|-----------|------|--------|-----------|-------|
| **Claude** | Motor LLM (nuclei) | FUNCIONAL | ANTHROPIC_API_KEY | Assinatura existente |
| **Canva Business** | Design/Slides/Export | FUNCIONAL | CANVA_CLIENT_ID + SECRET + ACCESS_TOKEN | Assinatura existente |
| **NotebookLM** | Podcast/Video/Quiz/Flashcards/Slides | FUNCIONAL | Google account (Playwright) | Gratis (conta PRO) |
| **ElevenLabs** | TTS narracao PT-BR | CONFIGURADO | ELEVENLABS_API_KEY | Assinatura existente |
| **Runway** | Video AI generation | CONFIGURADO | RUNWAY_API_KEY | Creditos |
| **Pika** | Video AI alternativo | CONFIGURADO | PIKA_API_KEY | Creditos |
| **Kling** | Video AI budget | CONFIGURADO | KLING_API_KEY | Creditos |
| **Hailuo** | Video AI | CONFIGURADO | HAILUO_API_KEY | Creditos |
| **YouTube** | Video publish | CONFIGURADO | YOUTUBE_API_KEY | Gratis |
| **Ayrshare** | Social multi-publish | CONFIGURADO | AYRSHARE_API_KEY | Assinatura existente |
| **Hotmart** | Curso/checkout BR | CONFIGURADO | MCP wired N06 | Comissao |
| **Stripe** | Pagamento INT | CONFIGURADO | STRIPE_SECRET_KEY | Comissao |
| **MercadoPago** | Pagamento BR | CONFIGURADO | MERCADOPAGO_* | Comissao |
| **Supabase** | Database/Storage | CONFIGURADO | SUPABASE_* | Gratis tier |
| **GitHub** | Repo/Deploy | CONFIGURADO | GITHUB_PAT | Gratis |

### Ferramentas Open-Source (local, $0)

| Ferramenta | Funcao | Instalacao |
|-----------|--------|-----------|
| **Pandoc** | md → PDF/EPUB/DOCX (40+ formatos) | CLI local |
| **Typst** | md → PDF profissional | CLI local |
| **Marp** | md → slides HTML/PDF/PPTX | CLI local |
| **WeasyPrint** | HTML/CSS → PDF | Python lib |
| **FFmpeg** | Video edit/concat/legendas | CLI local |
| **Remotion** | React → video programatico | Node.js |

### MCP Wiring (por nucleo)

| Nucleus | MCPs Disponiveis |
|---------|-----------------|
| N01 Research | notebooklm, firecrawl, brave-search, fetch, markitdown |
| N02 Marketing | canva, notebooklm, browser, markitdown |
| N03 Engineering | canva, github, fetch |
| N04 Knowledge | notebooklm, supabase, postgres, firecrawl, fetch |
| N05 Operations | github, postgres |
| N06 Commercial | canva, notebooklm, hotmart, stripe, fetch, markitdown |

---

## CANVA CONNECT API — Capabilities Testadas

### Endpoints Funcionais

```
POST /v1/designs                    → Criar design (presentation, doc, whiteboard, custom size)
GET  /v1/designs?ownership=owned    → Listar designs (25 encontrados)
GET  /v1/designs/{id}               → Metadata do design
POST /v1/exports                    → Exportar (PDF, PPTX, PNG, JPG, GIF, MP4)
GET  /v1/exports/{id}               → Status + download URL
GET  /v1/users/me                   → User ID + Team ID
```

### Design Types Validados

| Tipo | Preset/Custom | Dimensoes |
|------|--------------|-----------|
| Presentation | preset: `presentation` | Padrao Canva |
| Document | preset: `doc` | Padrao Canva |
| Whiteboard | preset: `whiteboard` | Padrao Canva |
| Instagram Post | custom | 1080x1080 |
| Instagram Story | custom | 1080x1920 |
| YouTube Thumbnail | custom | 1280x720 |
| TikTok | custom | 1080x1920 |
| Facebook Post | custom | 1200x630 |
| LinkedIn Post | custom | 1200x627 |
| Twitter/X Post | custom | 1600x900 |

### Export Validados

| Formato | Status | Uso |
|---------|--------|-----|
| PDF | FUNCIONAL (download URL gerada) | eBooks, handouts, docs |
| PPTX | FUNCIONAL (download URL gerada) | Apresentacoes editaveis |
| PNG | FUNCIONAL (download URL gerada) | Social media, thumbnails |
| JPG | Disponivel | Fotos, banners |
| GIF | Disponivel | Animacoes curtas |
| MP4 | Disponivel | Video de slides |

### Scopes Atuais vs Necessarios

| Scope | Status | Para que |
|-------|--------|---------|
| design:meta:read | ATIVO | Listar designs |
| design:content:read | ATIVO | Ler conteudo |
| design:content:write | ATIVO | Criar designs |
| profile:read | ATIVO | User info |
| asset:read | ATIVO | Listar assets |
| folder:read | ATIVO | Listar pastas |
| asset:write | FALTA | Upload imagens/logos |
| brandtemplate:meta:read | FALTA | Listar brand templates |
| brandtemplate:content:read | FALTA | Ler templates |
| folder:write | FALTA | Criar pastas |

**Acao**: Adicionar scopes faltantes no portal Canva Developer para habilitar brand templates e upload de assets.

### Rate Limits

- ~10 creates/minuto (429 depois)
- Exports: sem limite observado
- Reads: sem limite observado

---

## NOTEBOOKLM — Pipeline Validada

### Capacidades Confirmadas (testadas por N04)

| Output | Tipo | Formato | Uso na Content Factory |
|--------|------|---------|----------------------|
| Resumo em Audio | Podcast 2 hosts | .wav/.mp3 | Onboarding, estudo passivo, Spotify |
| Cartoes Didaticos | Flashcards interativos | UI/export | Estudo ativo, curso modulo review |
| Teste (Quiz) | Perguntas + respostas | UI/export | Assessment de curso, certificacao |
| Mapa Mental | Diagrama de conceitos | imagem | Visao geral visual, social post |
| Infografico | Visual estatico | imagem | Social media, ebook insert |
| Apresentacao | Slides | .pptx/.pdf | Reunioes, treinamento, aulas |
| Resumo em Video | Video gerado | .mp4 | Conteudo social, YouTube |
| Relatorios | Doc estruturado | .pdf/.docx | Documentacao formal |
| Tabela de Dados | Dados extraidos | tabela | Analise, comparacao |

### Stack de Automacao

```
KC .md (CEX) → Playwright cola como source → NotebookLM indexa → Estudio gera outputs
```

**Prova de Conceito**: 75 flashcards gerados do kc_8f_pipeline.md (14.6KB)
**Conta**: Gato Ao Cubo PRO (limites 5x maiores)
**Notebook teste**: 940fd258-847f-47c1-b7e6-caca7b730681

### Tools Disponiveis

| Tool | Qtd | Funcao |
|------|-----|--------|
| notebooklm-mcp | 17 tools | Q&A, listar notebooks, criar notebooks |
| claude --chrome | 18 tools | Controlar Chrome real (Named Pipe) |
| Playwright (local) | Script | Browser automation, colar conteudo |

### Limitacoes

- Sem API publica oficial (automacao via browser)
- Auth expira entre sessoes (requer re-login periodico)
- Puppeteer Chrome profile separado do Chrome sistema
- Rate: ~5 notebooks/hora recomendado

---

## ARTEFATOS WAVE 2 — JA CONSTRUIDOS (48 artifacts, 228KB)

### Prompt Templates (7) — `P03_prompts/templates/content_factory/`

| Template | Arquivo | Para gerar |
|----------|---------|-----------|
| Video script | p03_pt_cf_video_script.md | Roteiro com hook/build/benefit/proof/CTA |
| Lesson script | p03_pt_cf_lesson_script.md | Script de aula com objetivos e exercicios |
| Course outline | p03_pt_cf_course_outline.md | Estrutura de curso (modulos, licoes, duracao) |
| eBook chapter | p03_pt_cf_ebook_chapter.md | Capitulo com intro/corpo/exemplos/resumo |
| Slide deck | p03_pt_cf_slide_deck.md | Conteudo de slides com speaker notes |
| Quiz | p03_pt_cf_quiz.md | Multipla escolha sobre conteudo |
| Social post | p03_pt_cf_social_post.md | Post por plataforma (hook, valor, CTA) |

### Action Prompts (7) — `P03_prompts/actions/content_factory/`

| Action | Trigger |
|--------|---------|
| ap_cf_generate_course | "Crie um curso sobre {{TOPIC}}" |
| ap_cf_generate_video | "Crie um video de {{DURATION}}s sobre {{TOPIC}}" |
| ap_cf_generate_ebook | "Crie um ebook sobre {{TOPIC}}" |
| ap_cf_generate_presentation | "Crie apresentacao sobre {{TOPIC}}" |
| ap_cf_generate_podcast | "Crie podcast sobre {{TOPIC}}" |
| ap_cf_generate_campaign | "Promova {{CONTENT}} em {{PLATFORMS}}" |
| ap_cf_publish | "Publique {{CONTENT}} em {{CHANNELS}}" |

### Constraint Specs (6) — `P03_prompts/constraints/content_factory/`

| Spec | Define |
|------|--------|
| cs_cf_video | Duracao, aspect ratio, hook rules, CTA |
| cs_cf_course | Modulos (5-12), licoes (3-8), quiz, certificacao |
| cs_cf_ebook | Capitulos (5-15), palavras/cap (2K-5K), formatacao |
| cs_cf_presentation | Slides (10-30), bullets (3-5), speaker notes |
| cs_cf_podcast | Duracao (10-30min), intro/corpo/outro |
| cs_cf_brief | Campos obrigatorios do brief |

### Function Defs (7) — `P04_tools/functions/content_factory/`

| Tool | O que faz |
|------|-----------|
| fn_cf_canva_create | Criar design no Canva via API |
| fn_cf_canva_export | Exportar design (PDF/PPTX/PNG/MP4) |
| fn_cf_elevenlabs_tts | Gerar narracao via ElevenLabs |
| fn_cf_pdf_generate | Gerar PDF via Typst/Pandoc/WeasyPrint |
| fn_cf_slides_generate | Gerar slides via Marp |
| fn_cf_video_assemble | Montar video via FFmpeg |
| fn_cf_ebook_compile | Compilar ebook via Pandoc |

### DAGs (6) — `P12_orchestration/dags/content_factory/`

| DAG | Pipeline |
|-----|----------|
| dag_cf_master | brief → research → author → produce → validate → publish |
| dag_cf_video | script → storyboard → TTS → video_gen → FFmpeg → export |
| dag_cf_course | outline → modulos → scripts → TTS → slides → quiz → LMS |
| dag_cf_ebook | outline → chapters → review → typeset → PDF/EPUB |
| dag_cf_presentation | outline → slide_content → Canva_create → export |
| dag_cf_social | extract_hooks → posts → schedule → publish |

### Workflows (5) — `P12_orchestration/workflows/content_factory/`

| Workflow | O que faz |
|----------|-----------|
| wf_cf_publish_youtube | Upload → metadata → thumbnail → publish |
| wf_cf_publish_social | Adaptar por plataforma → schedule → Ayrshare |
| wf_cf_publish_hotmart | Upload modulos → config checkout → go live |
| wf_cf_promote | Extract hooks → posts → Canva thumbnails → schedule 7d |
| wf_cf_email_launch | Email sequence 5 dias → automacao |

### Knowledge Cards (10) — `P01_knowledge/library/integration/`

| KC | Conteudo |
|----|---------|
| kc_canva_connect_api | OAuth PKCE, endpoints, export, brand templates |
| kc_elevenlabs_tts | API, modelos, vozes PT-BR, pricing |
| kc_runway_api | Text/image-to-video, precos, rate limits |
| kc_ffmpeg_patterns | Receitas: concat, audio, legendas, thumb |
| kc_marp_cli | md → slides, temas, diretivas |
| kc_typst_patterns | md → PDF profissional, templates |
| kc_pandoc_pipeline | md → PDF/EPUB/DOCX, multi-formato |
| kc_youtube_api | Upload, metadata, playlists |
| kc_ayrshare_api | Multi-rede, scheduling, analytics |
| kc_notebooklm_integration | Capacidades, automacao, MCP tools |

---

## PIPELINE MASTER — dag_cf_master

```
BRIEF + {{BRAND}}
    |
    v
[WAVE 1: RESEARCH] ─── N01
    |  Pesquisa profunda sobre o tema
    |  Output: KCs de dominio + outline
    |
    v
[WAVE 2: AUTHOR] ─── N03 + N02
    |  Gera scripts, outlines, copy (paralelo)
    |  N03: course outline, lesson scripts, ebook chapters
    |  N02: social copy, email sequences, landing page
    |
    v
[WAVE 3: PRODUCE] ─── N03 + N04 (paralelo)
    |  N03 (Claude): 
    |    → Canva API: cria apresentacao + export PPTX/PDF
    |    → Marp: gera slides alternativos
    |    → Typst/Pandoc: gera eBook PDF/EPUB
    |    → ElevenLabs: gera narracoes
    |    → FFmpeg: monta videos
    |
    |  N04 (NotebookLM):
    |    → Cola KCs no NotebookLM
    |    → Gera: Audio Overview (podcast)
    |    → Gera: Flashcards (75+ por KC)
    |    → Gera: Quiz (assessment)
    |    → Gera: Mapa Mental
    |    → Gera: Slides (apresentacao)
    |    → Gera: Video Overview
    |
    v
[WAVE 4: VALIDATE] ─── N07
    |  Quality gates: consistencia entre formatos
    |  Tone check: voz da marca uniforme
    |  Brand check: cores, logo, {{BRAND_*}} aplicados
    |
    v
[WAVE 5: PUBLISH] ─── N05 + N06 (paralelo)
    |  N05: YouTube upload, GitHub release
    |  N06: Hotmart (curso), Stripe/MP (checkout)
    |  N02: Ayrshare (social), email launch
    |
    v
OUTPUT COMPLETO — USER NAO FEZ NADA
```

---

## CASO DE TESTE #1: CEX como {{BRAND}}

### Brand Config (seed by N06, Wave 1)

```yaml
BRAND_NAME: "CEX"
BRAND_TAGLINE: "The typed knowledge system that builds itself"
BRAND_ARCHETYPE: "magician"
BRAND_VOICE_TONE: "tecnico, confiante, direto"
BRAND_STYLE: "dark-terminal-minimal"
BRAND_COLORS: {primary: "#0D1117", accent: "#58A6FF", success: "#3FB950"}
BRAND_FONTS: {heading: "JetBrains Mono", body: "Inter"}
BRAND_ICP: "Devs que querem monetizar conhecimento como infoproduto"
```

### Outputs a Produzir

| # | Output | Formato | Ferramenta | Publish |
|---|--------|---------|-----------|---------|
| 1 | Curso "CEX na Pratica" (8 modulos) | Video + slides + quiz | Claude + Canva + NotebookLM | Hotmart |
| 2 | eBook "CEX em 30 Paginas" | PDF + EPUB | Typst + Pandoc | Gumroad/Hotmart |
| 3 | Video Demo 90s | MP4 9:16 | Claude + FFmpeg | YouTube Shorts, Reels, TikTok |
| 4 | Pitch Deck | PPTX + PDF | Canva API | SlideShare, LinkedIn |
| 5 | Podcast "CEX Explained" | MP3 | NotebookLM Audio Overview | Spotify, YouTube |
| 6 | 75+ Flashcards | Digital | NotebookLM | Curso (material complementar) |
| 7 | Quiz (assessment) | Digital | NotebookLM | Curso (certificacao) |
| 8 | Social Campaign (7 dias) | Posts multi-plataforma | Claude + Canva + Ayrshare | IG, LinkedIn, X, YT |

### Estrutura do Curso (8 Modulos)

| Modulo | Titulo | Conteudo |
|--------|--------|---------|
| M1 | O que e CEX | Visao geral, problema que resolve, a variavel X |
| M2 | 8F Pipeline | CONSTRAIN→BECOME→INJECT→REASON→CALL→PRODUCE→GOVERN→COLLABORATE |
| M3 | 12 Pilares | P01-P12: Knowledge, Identity, Prompts, Tools... |
| M4 | 115 Kinds | Sistema de tipos, kinds universais, como funcionam |
| M5 | 7 Nucleos | N01-N07: Intelligence, Marketing, Engineering... |
| M6 | 109 Builders | ISOs, archetypes, como constroem artefatos |
| M7 | Content Factory | A esteira de producao (este spec!) |
| M8 | Lancamento | Como usar CEX para seu proprio {{BRAND}} |

---

## IMPLEMENTACAO — 4 Waves

### Wave 3: Teste CEX (proximo)

| # | Task | Nucleus | Tempo |
|---|------|---------|-------|
| 1 | Preencher brand_config.yaml com seed CEX | N06 | 30min |
| 2 | Gerar outline do curso (8 modulos) usando ap_cf_generate_course | N03 | 1h |
| 3 | Gerar scripts de cada modulo usando tpl_cf_lesson_script | N03 | 2h |
| 4 | Cola KCs no NotebookLM → gerar podcast + flashcards + quiz | N04 | 1h |
| 5 | Criar apresentacao no Canva via API → export PPTX/PDF | N03 | 1h |
| 6 | Gerar eBook via Typst/Pandoc | N03 | 1h |
| 7 | Gerar video demo 90s | N03 | 1h |
| 8 | Gerar social campaign (7 posts) | N02 | 1h |

### Wave 4: Validate + Publish

| # | Task | Nucleus |
|---|------|---------|
| 1 | Quality gate: review todos os outputs | N07 |
| 2 | Brand consistency check | N06 |
| 3 | Upload curso Hotmart | N06 |
| 4 | Upload video YouTube | N05 |
| 5 | Publish social campaign | N02 |
| 6 | Email launch sequence | N02 |

### Wave 5: Evolve + Scale

| # | Task |
|---|------|
| 1 | /evolve nos artefatos gerados (quality improvement loop) |
| 2 | Segundo {{BRAND}} teste (validar genericidade) |
| 3 | cex_content_factory.py — CLI unificado |
| 4 | n8n workflow visual (opcional) |

---

## GDP — Decisoes Pendentes

| # | Decisao | Opcoes | Status |
|---|---------|--------|--------|
| D1 | NotebookLM: 1 notebook por dominio vs por missao? | Dominio = reutilizavel; Missao = descartavel | OPEN |
| D2 | Quais outputs gerar por padrao? | Todos vs subset (audio + flashcards + quiz) | OPEN |
| D3 | Publicar auto ou aprovar antes? | Auto = rapido; Aprovacao = controle | OPEN |
| D4 | Chrome local vs Firecrawl cloud? | Local = gratis; Cloud = pago, autonomo | OPEN |
| D5 | Conta Google dedicada para automacao? | Gato ao Cubo vs conta nova | OPEN |
| D6 | Canva: adicionar scopes extras? | asset:write, brandtemplate:*, folder:write | OPEN |
| D7 | Pricing do curso CEX | R$497 vs R$997 vs gratis (lead magnet) | OPEN |
| D8 | Plataforma do curso | Hotmart vs YouTube vs self-hosted | OPEN |

---

## METRICAS DE SUCESSO

| Metrica | Target |
|---------|--------|
| Tempo brief → curso completo | < 4 horas (autonomo) |
| Tempo brief → eBook | < 1 hora |
| Tempo brief → video demo | < 30 minutos |
| Custo por brief completo (7 outputs) | < R$15 |
| Quality score medio | >= 8.5 |
| Formatos gerados por brief | >= 7 |
| Intervencao humana | 0 (validate only) |

---

## DONE WHEN

- [ ] brand_config.yaml CEX preenchido
- [ ] Curso 8 modulos gerado (scripts + slides + quiz)
- [ ] eBook PDF/EPUB gerado
- [ ] Video demo 90s gerado
- [ ] Podcast Audio Overview gerado via NotebookLM
- [ ] 75+ flashcards gerados via NotebookLM
- [ ] Apresentacao PPTX/PDF exportada do Canva
- [ ] Social campaign 7 posts gerada
- [ ] Todos os outputs passam quality gate >= 8.5
- [ ] Brand consistency verificada (tom, cores, {{BRAND_*}})
- [ ] Pelo menos 1 output publicado (YouTube, Hotmart, ou social)
