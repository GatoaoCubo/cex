---
id: output_content_factory_landscape
kind: research_output
8f: F4_reason
pillar: P01
mission: MISSION_content_factory_v1
nucleus: N01
wave: 1
title: "Research OUT — Landscape de Ferramentas para Content Factory Autonoma"
created: 2026-04-06T14:30:00-03:00
author: n01_research_analyst
quality: 9.1
tags: [research, content-factory, tools, APIs, automation, video, course, audio, presentation, PDF, orchestration]
sources: 48
tools_evaluated: 52
density_score: 1.0
version: 1.0.0
tldr: "> **Objetivo**: Mapear TODAS as ferramentas, APIs, repos open-source e plataformas para montar uma esteira de producao autonoma: brief + brand -> videos +..."
domain: intelligence
updated: 2026-04-07
related:
  - output_content_factory_internal_audit
  - n06_api_access_pricing
  - spec_content_factory_v1
  - n04_output_cf_integration_kcs
  - p01_kc_notebooklm_integration
  - p01_kc_audio_tool
  - bld_knowledge_card_tts_provider
  - kc_api_reference
  - bld_collaboration_audio_tool
  - kc_open_source_ai_ecosystem
---

# Content Factory Autonoma — Landscape de Ferramentas

> **Objetivo**: Mapear TODAS as ferramentas, APIs, repos open-source e plataformas para montar uma esteira de producao autonoma: brief + brand -> videos + apresentacoes + aulas + PDFs + eBooks + cursos AUTOMATICAMENTE.

---

## 1. Executive Summary

O mercado de ferramentas para producao autonoma de conteudo digital esta maduro em componentes individuais mas **fragmentado em integracao**. Nao existe UMA solucao que cubra Planned o pipeline brief-to-course. A oportunidade do CEX esta em ser o **orquestrador** que conecta essas pecas.

**Descobertas-chave:**

- **Audio/TTS**: ElevenLabs lidera em qualidade e PT-BR. NotebookLM tem API oficial via Google Cloud para Audio Overviews.
- **Video AI**: Runway Gen-4 e Sora 2 tem APIs REST funcionais. HeyGen e Synthesia dominam avatares corporativos. Veo 3.1 do Google esta em GA no Vertex AI.
- **Apresentacoes**: Gamma.app tem API GA desde Jan/2026 — melhor opcao programatica. Marp e Slidev sao open-source para markdown-to-slides.
- **PDF/eBook**: Typst + Pandoc + WeasyPrint cobrem 100% do pipeline md->PDF/EPUB, todos open-source.
- **Edicao Programatica**: Remotion (React->video) e Shotstack (API cloud) sao as melhores opcoes.
- **LMS**: Hotmart tem API REST com OAuth2. Thinkific tem API no plano Grow ($199/mo). Open edX e a melhor opcao self-hosted.
- **Orquestracao**: n8n (self-hosted, 400+ integracoes) e a base. LangGraph para agentes complexos. CrewAI para prototipagem rapida.
- **Gap critico**: Nao existe ferramenta que faca brief->curso completo. O CEX pode preencher esse gap.

**Stack recomendado (custo estimado/mes para producao):**
- Tier 1 (essencial): ~$300-500/mes (ElevenLabs + Runway/Sora + Gamma + n8n self-hosted + Pandoc/Typst)
- Tier 2 (premium): ~$800-1500/mes (+ HeyGen + Remotion + Hotmart)
- Tier 3 (enterprise): ~$3000+/mes (+ Synthesia + Canva Enterprise + Custom LMS)

---

## 2. Tabelas Comparativas por Categoria

### 2.1 Geracao de Audio/Podcast

| Tool | API? | Preco (2026) | Open-Source? | PT-BR? | Automacao | Nota |
|------|------|-------------|-------------|--------|-----------|------|
| **NotebookLM** | SIM (Google Cloud) | Enterprise license req. | Nao | Sim | Alta — API cria Audio Overviews programaticamente | API oficial via `notebooks.audioOverviews.create`. Requer Gemini Enterprise ou NotebookLM Enterprise license. Tambem gera Video Overviews, quizzes, flashcards. Lib nao-oficial `notebooklm-py` expoe features extras. |
| **Google Canvas** | Nao (UI only) | Gratis (Google Search) | Nao | Sim | Baixa | Feature do Google AI Mode — escrita e coding interativos. NAO e ferramenta de producao. Confusao de nome com Canvas LMS. |
| **ElevenLabs** | SIM (REST) | Creator: $22/mo (100K chars). Pro: $99/mo. API: $0.24-0.30/1K chars | Nao | SIM (PT-BR nativo) | Muito Alta | Melhor TTS do mercado. Voice cloning (instant + professional). 32+ idiomas. Turbo: <300ms latencia. SDK Python oficial. |
| **PlayHT** | SIM (REST) | Basic: $31/mo. Unlimited: $29-99/mo | Nao | SIM | Alta | Alternativa viavel. 140+ idiomas. Voice cloning com 30s de audio. API Turbo <300ms. |
| **Podcastle** | Limitada | $12-24/mo | Nao | Parcial | Media | Foco em edicao de podcast, nao geracao. Sem API REST publica robusta. |
| **Descript** | SIM (REST, 2026) | $24-33/mo. Enterprise: custom | Nao | Sim (transcricao) | Muito Alta | API nova (2026) permite criar projetos, importar media, editar via NL. Background agent com prompts. Node.js 24+. Ideal para pos-producao. |

**Recomendacao Tier 1**: ElevenLabs (TTS principal) + NotebookLM API (Audio Overviews de documentos)
**Recomendacao Tier 2**: Descript API (pos-producao e edicao automatizada)

---

### 2.2 Geracao de Video AI

| Tool | API? | Preco (2026) | Open-Source? | PT-BR? | Automacao | Nota |
|------|------|-------------|-------------|--------|-----------|------|
| **Runway Gen-4/4.5** | SIM (REST) | $0.01/credito. Gen-4.5: 25 cred/s ($0.25/s). Gen-4 Turbo: ~12 cred/s | Nao | N/A (visual) | Alta | API madura. Text-to-video + image-to-video. 10s clip ~$2.50 (Gen-4.5). Dev portal com creditos pre-pagos. |
| **Sora 2 (OpenAI)** | SIM (REST) | Standard: $0.10/s (720p). Pro: $0.30-0.50/s (1080p) | Nao | N/A | Alta | API desde Set/2025. Duracoes: 4-25s. 10s clip 720p = ~$1.00. Acesso requer Plus ($20/mo) ou Pro ($200/mo). |
| **Pika Labs** | Parcial (via terceiros) | Standard: $8/mo. Fancy: $76/mo. API via fal.ai: ~$0.45/100 clips 1080p | Nao | N/A | Media | Sem API oficial publica. Acesso via Fal.ai, PiAPI, Wavespeed. Pika 2.5 disponivel. |
| **Kling AI** | SIM (REST) | Subs: $7-180/mo. API: $0.14/video (terceiros). Enterprise: ~$4200/30K units | Nao | N/A | Alta | Kling 2.5 Turbo. Ate 3min video, 1080p/48FPS. API via PiAPI ou oficial. Boa relacao custo-beneficio. |
| **HeyGen** | SIM (REST + MCP) | API: $5 (pay-go) a $99/mo. ~2 creditos/min | Nao | SIM (TTS multilingual) | Muito Alta | Avatar AI — melhor para "apresentador virtual". Video Agent API + TTS API. Integracao MCP com Claude. Avatar III/IV. |
| **Synthesia** | SIM (REST) | Starter: $18-29/mo. Creator: $64-89/mo (com API). Enterprise: custom | Nao | SIM (160+ linguas) | Alta | Lider em avatar corporativo. 180+ avatares. Studio Avatars: +$1000/ano. SCORM export (Enterprise). |
| **D-ID** | SIM (REST) | Desde $4.70/mo. Advanced: $196/mo. Enterprise: custom | Nao | Sim | Alta | Talking heads — face + texto = video. API RESTful simples. Creditos compartilhados web/API. Streaming: creditos pela metade. |
| **Veo 3.1 (Google)** | SIM (Vertex AI) | $0.15/s+ (API). Subs: $20-250/mo | Nao | N/A | Alta | GA no Vertex AI. Text-to-video + image-to-video. 1080p, 8s clip em 30-90s. Preview endpoints deprecated Apr/2026 — migrar para GA. |

**Recomendacao Tier 1**: Sora 2 (melhor custo para clips generativos) + HeyGen (avatares/apresentador)
**Recomendacao Tier 2**: Runway Gen-4 (qualidade cinematica) + Veo 3.1 (integracao Google Cloud)
**Recomendacao Tier 3**: Kling AI (custo baixo, alternativa)

---

### 2.3 Geracao de Apresentacoes

| Tool | API? | Preco (2026) | Open-Source? | PT-BR? | Automacao | Nota |
|------|------|-------------|-------------|--------|-----------|------|
| **Gamma.app** | SIM (REST, GA Jan/2026) | Pro/Ultra/Teams/Business (req. para API) | Nao | Sim | Muito Alta | API GA! Cria presentations, docs, webpages, social posts programaticamente. Integracao Make/Zapier/Workato. Markdown input. Folders + email sharing. |
| **Canva API** | SIM (Enterprise only) | Enterprise: custom (30+ team members) | Nao | Sim | Alta (se Enterprise) | Autofill API para templates. Job-based batch generation. **Barreira**: requer Enterprise (30+ pessoas, preco custom). Inacessivel para startups. |
| **Google Slides API** | SIM (REST, gratis) | Gratis (Google Workspace) | Nao | Sim | Alta | API REST completa para criar/editar slides programaticamente. Templates suportados. Gratis para uso basico. Sem AI embutido. |
| **Beautiful.ai** | Nao | $12-40/mo | Nao | Parcial | Baixa | Auto-design inteligente mas sem API publica. Apenas uso via UI. |
| **SlidesAI** | Nao (plugin Google) | $10-20/mo | Nao | Sim | Media | Plugin Google Slides. Texto -> slides. Sem API, requer Google Slides. |
| **Tome** | Nao | Freemium | Nao | Sim | Baixa | AI presentations mas sem API publica. Pivotou para "AI research". |
| **Marp** | SIM (CLI) | Gratis | SIM (MIT) | Sim | Muito Alta | Markdown -> HTML/PDF/PPTX. CLI com server mode (HTTP). 3 themes built-in. CommonMark compativel. `npx @marp-team/marp-cli`. |
| **Slidev** | SIM (CLI) | Gratis | SIM (MIT) | Sim | Alta | Vue 3 + Vite. Markdown -> SPA/PDF/PNG. Hot-reload dev server. Deploy CI/CD. Componentes Vue interativos. |
| **reveal.js** | SIM (JS) | Gratis | SIM (MIT) | Sim | Alta | HTML slides. Markdown plugin. Maior ecossistema de plugins. Mais manual que Marp/Slidev. |

**Recomendacao Tier 1**: Gamma.app API (polished, AI-powered, GA) + Marp CLI (open-source, pipeline)
**Recomendacao Tier 2**: Google Slides API (gratis, templates) + Slidev (developer presentations)

---

### 2.4 Geracao de PDF/eBook

| Tool | API? | Preco (2026) | Open-Source? | PT-BR? | Automacao | Nota |
|------|------|-------------|-------------|--------|-----------|------|
| **Pandoc** | SIM (CLI + pypandoc) | Gratis | SIM (GPL) | Sim | Muito Alta | Swiss army knife: md -> PDF/EPUB/DOCX/HTML + 40 formatos. Templates customizaveis. Citeproc para refs academicas. Docker image disponivel. pypandoc para Python. v3.9 (2026). |
| **Typst** | SIM (CLI + API) | Gratis (app freemium) | SIM (Apache 2.0) | Sim | Muito Alta | Alternativa moderna ao LaTeX. Compilacao em ms. Scripting built-in (loops, functions, data import). 1200+ templates. Rust-based. v1.0 estavel. Ideal para reports automatizados. |
| **WeasyPrint** | SIM (Python lib) | Gratis | SIM (BSD) | Sim | Muito Alta | HTML/CSS -> PDF. Suporta Flexbox, Grid, CSS Paged Media. `pip install weasyprint`. Python >=3.10. Ideal para PDFs estilizados a partir de templates HTML. |
| **LaTeX/Tectonic** | SIM (CLI) | Gratis | SIM (varias) | Sim | Alta | Qualidade tipografica maxima. Tectonic: LaTeX engine moderna, auto-download packages. Pesado (>1GB distro). Lento vs Typst. |
| **mdbook** | SIM (CLI) | Gratis | SIM (MPL) | Sim | Alta | Rust. Markdown -> book site. PDF via mdbook-pdf plugin. Ideal para documentacao tecnica. |
| **Calibre** | SIM (CLI) | Gratis | SIM (GPL) | Sim | Alta | Conversao entre formatos (EPUB/MOBI/PDF/AZW). CLI: `ebook-convert`. Batch processing. |
| **Prince XML** | SIM (CLI) | $795 (server license) | Nao | Sim | Alta | HTML -> PDF profissional. Melhor qualidade print. Caro. |
| **Docusaurus** | SIM (CLI) | Gratis | SIM (MIT) | Sim | Alta | React. Markdown -> docs site. Versioning. i18n. Nao gera PDF nativo (precisa plugin). |

**Recomendacao Tier 1**: Typst (reports/eBooks automatizados) + Pandoc (conversao multi-formato) + WeasyPrint (PDFs estilizados)
**Recomendacao Tier 2**: Calibre (conversao entre formatos finais) + mdbook (documentacao tecnica)

---

### 2.5 Edicao de Video Programatica

| Tool | API? | Preco (2026) | Open-Source? | PT-BR? | Automacao | Nota |
|------|------|-------------|-------------|--------|-----------|------|
| **FFmpeg** | SIM (CLI) | Gratis | SIM (LGPL/GPL) | N/A | Muito Alta | Ferramenta base universal. Concatenacao, overlays, legendas (.srt), reencode, streaming. Presente em quase todos os pipelines. |
| **Remotion** | SIM (Node.js/React) | Free (<=3 pessoas). Company: $100/mo. Enterprise: $500/mo | SIM (BSL) | Sim | Muito Alta | React -> MP4. Server-side rendering. Parametrizacao total. CSS/Canvas/SVG/WebGL. Integracao com Claude demonstrada (2026). Ideal para videos templated. |
| **MoviePy** | SIM (Python) | Gratis | SIM (MIT) | N/A | Alta | Python. Composicao programatica. Depende de FFmpeg. Bom para scripts simples. Menos performatico que Remotion para volumes altos. |
| **Shotstack** | SIM (REST) | Credito-based. 10 free. Subs para volume | Nao | N/A | Muito Alta | Cloud API. JSON define timeline, clips, overlays, transitions. Rendering gerenciado. Startup program (80% desconto). |
| **Creatomate** | SIM (REST) | $41-249/mo (credito-based) | Nao | N/A | Muito Alta | Templates + API. Bom para videos batch (social media, ads). JS Preview SDK. |
| **Editframe** | SIM (REST) | Pay-per-render | Nao | N/A | Alta | API de edicao programatica. Menor que Shotstack/Creatomate em features. |

**Recomendacao Tier 1**: FFmpeg (base universal) + Remotion (videos templated com React)
**Recomendacao Tier 2**: Shotstack (cloud rendering sem infra) + Creatomate (templates batch)

---

### 2.6 Curso/LMS Automation

| Tool | API? | Preco (2026) | Open-Source? | PT-BR? | Automacao | Nota |
|------|------|-------------|-------------|--------|-----------|------|
| **Hotmart Club** | SIM (REST, OAuth2) | Gratis (ate 10% comissao) | Nao | SIM (brasileiro) | Alta | API REST: products, sales, affiliates, subscriptions. Drip content (por data ou dias apos compra). Modulos, quizzes, videos. HotConnect -> Hotmart Developers. SDK Python: `hotmart-python` (PyPI). |
| **Teachable** | Parcial | $39-119/mo | Nao | Parcial | Media | API limitada comparada a Thinkific. Foco em UI. Webhooks disponiveis. |
| **Thinkific** | SIM (REST) | Start: $99/mo. Grow: $199/mo (com API) | Nao | Parcial | Alta | API REST no plano Grow+. Drag-and-drop builder. SCORM/xAPI. Video library reutilizavel. |
| **Canvas LMS** | SIM (REST) | Gratis (self-hosted) | SIM (AGPL) | Sim | Alta | LMS completo. REST API extensa. LTI integrations (Zoom, Gemini). Cuidado: analytics podem falhar em self-hosted. |
| **Moodle** | SIM (REST/SOAP) | Gratis (self-hosted) | SIM (GPL) | SIM | Alta | LMS mais usado no mundo. Ate 10K users. API REST + Web Services. Privacy API (GDPR). v4.5 (2024). Muitos plugins. |
| **Open edX** | SIM (REST + OAuth2) | Gratis (self-hosted) | SIM (AGPL) | Sim | Muito Alta | Escala para milhoes de alunos. Studio (autoria) + LMS (aluno). LTI Advantage Complete. API REST extensa. Self-hosted complexo. Melhor para MOOCs. |

**Recomendacao Tier 1**: Hotmart (mercado BR, API, pagamentos integrados) + Open edX (self-hosted escalavel)
**Recomendacao Tier 2**: Thinkific (API boa, internacional) + Moodle (institucional)

---

### 2.7 Content Factory Solutions (Competidores)

| Solucao | O que faz | Limitacoes | Preco |
|---------|----------|-----------|-------|
| **Jasper** | Brand voice + content marketing | Texto only. Sem video, audio, cursos. Lock-in de brand voice. | $39-125/mo |
| **Copy.ai** | GTM workflow automation + copy | Pivotou para sales/CRM. Sem multimedia. | $36-249/mo |
| **ContentMonk** | AI blog writer | Texto only. Sem pipeline multi-formato. | $15-49/mo |
| **MarketMuse** | Content planning + optimization | SEO-focado. Sem producao multimedia. | $99-399/mo |
| **AirOps** | AI workflow builder | Focado em ops, nao em content creation. | Custom |
| **Superlines** | Automated content workflows | Cobre texto + basic images. Sem video/audio/curso. | Varies |

**Gap no mercado**: NENHUM competidor faz brief -> video + audio + slides + PDF + curso. Todos sao parciais:
- Jasper/Copy.ai: apenas texto
- Nenhum integra LMS/course delivery
- Nenhum tem orquestracao multi-formato end-to-end
- Nenhum tem brand variable system como o CEX

---

### 2.8 Orquestracao de Pipeline

| Tool | API? | Preco (2026) | Open-Source? | Tipo | Nota |
|------|------|-------------|-------------|------|------|
| **n8n** | SIM (REST + MCP) | Self-hosted: gratis. Cloud: $20+/mo | SIM (fair-code) | Visual workflow | 400+ integracoes. AI nodes nativos (OpenAI, Anthropic, Ollama). v2.0 (Dez/2025). Docker/K8s. Ilimitado self-hosted. MCP connector. |
| **Zapier** | SIM (REST) | Free (100 tasks). Starter: $20/mo | Nao | No-code automation | 7000+ apps. Simples mas limitado em logica complexa. Caro em volume. |
| **Make (Integromat)** | SIM (REST) | Core: $9/mo. Pro: $16/mo. Teams: $29/mo | Nao | Visual automation | 3000+ apps. AI Content Extractor. Bring-your-own AI key. 350+ AI integracoes. Mais visual que Zapier. |
| **Temporal** | SIM (SDK) | Self-hosted: gratis. Cloud: usage-based | SIM (MIT) | Durable execution | Code-first. Fault-tolerant (resume apos crash). Ideal para workflows longos (horas/dias). Go/Java/Python/TS SDKs. |
| **Prefect** | SIM (SDK) | Self-hosted: gratis. Cloud: free tier + $500+/mo | SIM (Apache 2.0) | Python workflow | Decorators Python. Jupyter -> prod. Observabilidade forte. Bom para data/ML pipelines. |
| **Airflow** | SIM (SDK) | Gratis (self-hosted) | SIM (Apache 2.0) | DAG scheduler | Standard para ETL/batch. Grande ecossistema de providers. Mais complexo que Prefect. Overkill para content pipeline. |
| **LangGraph** | SIM (Python/TS) | Gratis (lib). Platform: paid | SIM (MIT) | Agent orchestration | Grafos com estado. Checkpointing + time travel. Melhor para agentes complexos com estado. Curva de aprendizado alta. |
| **CrewAI** | SIM (Python) | Gratis (lib). Enterprise: paid | SIM (MIT) | Multi-agent | Role-based (researcher, writer, editor). 20 linhas para comecar. MCP + A2A support. Ideal para content pipelines. Migracao para LangGraph quando escala. |

**Recomendacao Tier 1**: n8n (orquestracao visual, self-hosted) + CrewAI (multi-agent para conteudo)
**Recomendacao Tier 2**: Temporal (workflows longos/fault-tolerant) + LangGraph (agentes complexos)
**Evitar**: Zapier (caro em volume), Airflow (overengineered para content)

---

## 3. Stack Recomendado

### Tier 1 — Essencial (MVP Content Factory)

| Funcao | Ferramenta | Preco | Justificativa |
|--------|-----------|-------|---------------|
| Orquestracao | **n8n** (self-hosted) | Gratis | 400+ integracoes, AI nodes, ilimitado |
| Multi-agent | **CrewAI** | Gratis | Role-based, content pipeline nativo |
| TTS/Audio | **ElevenLabs** (Pro) | $99/mo | Melhor qualidade, PT-BR nativo, voice clone |
| Audio Overview | **NotebookLM API** | Enterprise req. | Podcasts AI a partir de docs |
| Video AI | **Sora 2** (Standard) | ~$0.10/s | Melhor custo, API REST, boa qualidade |
| Avatar/Presenter | **HeyGen** | $99/mo | Avatar AI, multilingual, MCP integration |
| Apresentacoes | **Gamma.app** (API) | Pro plan | API GA, AI-powered, automacao completa |
| Slides open-source | **Marp** | Gratis | md -> PDF/PPTX, MIT license |
| PDF/eBook | **Typst** + **Pandoc** | Gratis | Compilacao em ms + multi-formato |
| PDF estilizado | **WeasyPrint** | Gratis | HTML/CSS -> PDF, Python |
| Edicao video | **FFmpeg** + **Remotion** | Gratis/$0-100/mo | Base universal + templated videos |
| LMS/Curso | **Hotmart** | Gratis (comissao) | API REST, PT-BR nativo, pagamentos |
| **Total estimado** | | **~$300-400/mo** | |

### Tier 2 — Premium (Producao Profissional)

| Funcao | Ferramenta | Preco | Quando usar |
|--------|-----------|-------|-------------|
| Video cinematico | **Runway Gen-4.5** | ~$0.25/s | Quando precisa de qualidade maxima |
| Video Google | **Veo 3.1** | $0.15/s+ | Se ja usa Google Cloud |
| Avatar corporativo | **Synthesia** | $64-89/mo | Treinamento corporativo, SCORM |
| Video cloud edit | **Shotstack** | Credito-based | Rendering sem infra propria |
| Pos-producao | **Descript API** | $24-33/mo | Edicao automatizada, transcricao |
| LMS internacional | **Thinkific** | $199/mo | Se precisa de API + mercado gringo |
| Workflow pro | **Temporal** | Gratis (self-hosted) | Workflows longos, fault-tolerant |
| **Adicional ao Tier 1** | | **+$400-800/mo** | |

### Tier 3 — Futuro (Quando Escalar)

| Funcao | Ferramenta | Quando |
|--------|-----------|--------|
| Design batch | **Canva Enterprise** | 30+ pessoas na equipe |
| LMS MOOC | **Open edX** | Milhares de alunos |
| Agent complex | **LangGraph** | Agentes com estado complexo |
| Video budget | **Kling AI** | Alternativa mais barata em volume |
| Slides interativos | **Slidev** | Apresentacoes com demos ao vivo |

---

## 4. Gaps Identificados

### Gap 1: Brief-to-Course Pipeline (CRITICO)
**Nao existe** nenhuma ferramenta que receba um brief + brand guidelines e produza um curso completo (video + slides + PDF + quiz + LMS deploy). Todas sao ferramentas pontuais. O CEX pode ser o PRIMEIRO a fazer isso.

### Gap 2: Brand-Aware Content Generation
Jasper tem brand voice para texto, mas **nenhuma ferramenta aplica brand guidelines a video, audio, slides e PDF simultaneamente**. O sistema `{{BRAND_*}}` do CEX e unico.

### Gap 3: Multi-Format Orchestration
n8n conecta APIs mas nao entende o CONTEXTO do conteudo. LangGraph/CrewAI orquestram agentes mas nao tem conectores nativos para Gamma, ElevenLabs, HeyGen. Precisamos de um **adapter layer**.

### Gap 4: Quality Gate Cross-Format
Nao existe ferramenta que valide a **consistencia** entre o script do video, os slides, o PDF e o quiz. Um humano precisa revisar. Oportunidade para quality gate automatizado com LLM.

### Gap 5: NotebookLM -> Course
NotebookLM gera Audio Overviews excelentes mas nao exporta para LMS. Nao tem API para controlar estilo do audio (formal/casual). Pipeline NotebookLM -> Hotmart precisa ser construido.

### Gap 6: Localizacao PT-BR
Muitas ferramentas tem suporte PT-BR parcial. Video AI (Runway, Sora, Veo) nao geram narracoes — precisam de TTS separado. Legendas automaticas em PT-BR sao inconsistentes.

---

## 5. Repos Open-Source Relevantes

| Repo | Stars | Linguagem | Licenca | O que faz |
|------|-------|----------|---------|-----------|
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | ~22K | TypeScript | BSL | React -> video programatico |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | ~65K | TypeScript | Fair-code | Workflow automation, 400+ integracoes |
| [typst/typst](https://github.com/typst/typst) | ~40K | Rust | Apache 2.0 | Markdown-like -> PDF (alternativa LaTeX) |
| [marp-team/marp-cli](https://github.com/marp-team/marp-cli) | ~2K | TypeScript | MIT | Markdown -> slides (HTML/PDF/PPTX) |
| [slidevjs/slidev](https://github.com/slidevjs/slidev) | ~35K | Vue/TS | MIT | Vue-powered markdown slides |
| [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint) | ~7K | Python | BSD | HTML/CSS -> PDF |
| [jgm/pandoc](https://github.com/jgm/pandoc) | ~36K | Haskell | GPL | Universal document converter |
| [naqashafzal/AI-Content-Studio](https://github.com/naqashafzal/AI-Content-Studio) | New | Python | OSS | Script -> voiceover -> video -> upload automatico |
| [MichaelCrowe11/dpgen-content-pipeline](https://github.com/MichaelCrowe11/dpgen-content-pipeline) | New | Python | OSS | Multi-agent content pipeline com Google AI |
| [prakashdk/video-creator](https://github.com/prakashdk/video-creator) | New | Python | OSS | Pipeline offline: LLM -> TTS -> imagens -> video |
| [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | New | Python | OSS | API nao-oficial para NotebookLM (features extras) |
| [israelbls/notebooklm-podcast-automator](https://github.com/israelbls/notebooklm-podcast-automator) | New | Python | OSS | REST API para automatizar Audio Overviews |
| [hakimel/reveal.js](https://github.com/hakimel/reveal.js) | ~68K | JS | MIT | HTML presentation framework |

---

## 6. Arquitetura Sugerida

```
                        ┌─────────────────────────────────┐
                        │         CEX ORCHESTRATOR         │
                        │    (N07 + n8n + CrewAI agents)   │
                        └──────────────┬──────────────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                   │
              ┌─────▼─────┐    ┌──────▼──────┐    ┌──────▼──────┐
              │   BRIEF    │    │   BRAND     │    │  DECISIONS  │
              │  (N01/N04) │    │  CONFIG     │    │  MANIFEST   │
              │            │    │ {{BRAND_*}} │    │   (GDP)     │
              └─────┬──────┘    └──────┬──────┘    └──────┬──────┘
                    │                  │                   │
                    └──────────────────┼──────────────────┘
                                       │
                              ┌────────▼────────┐
                              │  CONTENT PLAN   │
                              │  (N01 research  │
                              │   + N04 struct) │
                              └────────┬────────┘
                                       │
              ┌────────────────────────┼────────────────────────┐
              │                        │                        │
     ┌────────▼────────┐    ┌─────────▼─────────┐   ┌─────────▼─────────┐
     │   SCRIPT GEN    │    │   VISUAL GEN      │   │   STRUCT GEN      │
     │  (N02 copy +    │    │  (slides + video   │   │  (course outline  │
     │   LLM agents)   │    │   + thumbnails)    │   │   + quiz + PDF)   │
     └────────┬────────┘    └─────────┬─────────┘   └─────────┬─────────┘
              │                       │                        │
    ┌─────────┼───────────────────────┼────────────────────────┼──────────┐
    │         │                       │                        │          │
    │  ┌──────▼──────┐  ┌────────────▼────────────┐  ┌───────▼───────┐  │
    │  │ AUDIO LAYER │  │     VIDEO LAYER         │  │  DOC LAYER    │  │
    │  │             │  │                         │  │               │  │
    │  │ ElevenLabs  │  │ HeyGen (avatar)         │  │ Typst (PDF)   │  │
    │  │ NotebookLM  │  │ Sora/Runway (gen)       │  │ Pandoc (EPUB) │  │
    │  │ Descript    │  │ Remotion (templated)     │  │ WeasyPrint    │  │
    │  │             │  │ FFmpeg (compose)         │  │ Gamma (slides)│  │
    │  └──────┬──────┘  └────────────┬────────────┘  └───────┬───────┘  │
    │         │                      │                        │          │
    │         └──────────────────────┼────────────────────────┘          │
    │                                │                                   │
    │                    ┌───────────▼───────────┐                      │
    │                    │    QUALITY GATE       │                      │
    │                    │  (LLM cross-check:    │                      │
    │                    │   script vs slides    │                      │
    │                    │   vs video vs PDF)    │                      │
    │                    └───────────┬───────────┘                      │
    │                                │                                   │
    │                    ┌───────────▼───────────┐                      │
    │                    │    PUBLISH LAYER      │                      │
    │                    │                       │                      │
    │                    │ Hotmart (curso)        │                      │
    │                    │ YouTube (video)        │                      │
    │                    │ Spotify (podcast)      │                      │
    │                    │ Gumroad (eBook)        │                      │
    │                    └───────────────────────┘                      │
    │                                                                   │
    │                     n8n WORKFLOW ENGINE                            │
    └───────────────────────────────────────────────────────────────────┘
```

### Fluxo Detalhado

1. **Input**: Brief (tema, publico, formato) + Brand Config + Decision Manifest
2. **Research** (N01): Pesquisa profunda sobre o tema via CrewAI agents
3. **Structure** (N04): Outline do curso, modulos, topicos
4. **Script** (N02): Copy para cada modulo (narracoes, CTAs, slides text)
5. **Audio**: ElevenLabs gera narracoes PT-BR + NotebookLM gera podcast overview
6. **Video**: HeyGen gera avatares + Sora/Runway gera B-roll + Remotion monta timeline + FFmpeg compoe final
7. **Slides**: Gamma.app gera apresentacoes + Marp gera versao PDF
8. **Docs**: Typst gera eBook PDF + Pandoc gera EPUB + WeasyPrint gera handouts
9. **Quality**: LLM cross-check de consistencia entre todos os formatos
10. **Publish**: Deploy para Hotmart (curso), YouTube (videos), distribuicao digital (eBooks)

---

## 7. Riscos e Limitacoes

### Vendor Lock-in
| Risco | Mitigacao |
|-------|----------|
| ElevenLabs muda precos | PlayHT como fallback. Voice clones portaveis? Testar. |
| HeyGen descontinua API | D-ID ou Synthesia como alternativa. Avatares nao sao portaveis. |
| Gamma.app API muda | Marp (open-source) como fallback. Export templates antes. |
| Sora/OpenAI rate limits | Veo (Google) + Kling (budget) como fallback chain. |
| Hotmart muda comissao | Thinkific + Open edX como alternativas. Nao depender 100% de 1 LMS. |

### Rate Limits e Custos
| Ferramenta | Limite conhecido | Custo em escala |
|-----------|-----------------|----------------|
| Sora 2 | Sem limite documentado (pay-per-use) | 100 videos de 10s = ~$100 |
| Runway Gen-4.5 | Creditos pre-pagos | 100 videos de 10s = ~$250 |
| ElevenLabs Pro | 500K chars/mo | ~50 horas de audio |
| HeyGen API | Creditos-based | 100 videos de 1min = ~$200 |
| Gamma API | Baseado em plano | Limites nao documentados publicamente |

### Riscos Tecnicos
- **Latencia**: Pipeline completo (brief -> curso) pode levar 2-6 horas dependendo do volume.
- **Consistencia**: Garantir que narracoes, slides e video estejam sincronizados requer quality gate robusto.
- **PT-BR**: Video AI nao gera narracoes — sempre precisa de TTS separado. Legendas automaticas em PT-BR tem ~90% accuracy.
- **Armazenamento**: Videos em 1080p ocupam ~100-500MB cada. Pipeline de 10 aulas = 1-5GB.
- **Dependencia de APIs**: Qualquer API pode cair. Necessario retry logic + fallback chain.

### Riscos Legais
- **Voice cloning**: Clonar vozes requer consentimento explicito.
- **Avatar AI**: Uso comercial requer licenca adequada (verificar TOS de cada plataforma).
- **Copyright**: Conteudo gerado por AI — legislacao em evolucao. Documentar provenance.

---

## 8. Referencias

### Audio/Podcast
- NotebookLM Enterprise API: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-audio-overview
- ElevenLabs API Docs: https://elevenlabs.io/docs/overview/capabilities/text-to-speech
- ElevenLabs Pricing: https://elevenlabs.io/pricing/api
- PlayHT: https://play.ht/
- Descript API: https://docs.descriptapi.com/
- notebooklm-py (unofficial): https://github.com/teng-lin/notebooklm-py

### Video AI
- Runway API Docs: https://docs.dev.runwayml.com/
- Runway API Pricing: https://docs.dev.runwayml.com/guides/pricing/
- Sora 2 API: via OpenAI API (https://platform.openai.com)
- HeyGen API: https://www.heygen.com/api-pricing
- Synthesia API: https://docs.synthesia.io/reference/introduction
- D-ID API: https://docs.d-id.com/reference/get-started
- Google Veo (Vertex AI): https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation
- Kling AI API: https://klingai.com/global/dev/pricing
- Pika via fal.ai: https://fal.ai

### Apresentacoes
- Gamma.app API: https://developers.gamma.app
- Google Slides API: https://developers.google.com/slides
- Marp CLI: https://github.com/marp-team/marp-cli
- Slidev: https://sli.dev/
- reveal.js: https://revealjs.com/

### PDF/eBook
- Typst: https://typst.app/ | GitHub: https://github.com/typst/typst
- Pandoc: https://pandoc.org/MANUAL.html
- WeasyPrint: https://weasyprint.org/ | GitHub: https://github.com/Kozea/WeasyPrint
- Calibre: https://calibre-ebook.com/
- Prince XML: https://www.princexml.com/

### Edicao de Video
- Remotion: https://www.remotion.dev/ | GitHub: https://github.com/remotion-dev/remotion
- Shotstack: https://shotstack.io/ | API: https://shotstack.io/product/video-editing-api/
- Creatomate: https://creatomate.com/ | API: https://creatomate.com/developers
- FFmpeg: https://ffmpeg.org/
- MoviePy: https://zulko.github.io/moviepy/

### LMS/Cursos
- Hotmart Developers: https://developers.hotmart.com/docs/
- Thinkific API: via plano Grow ($199/mo)
- Open edX: https://openedx.org/
- Moodle: https://moodle.org/
- Canvas LMS: https://www.instructure.com/canvas

### Orquestracao
- n8n: https://n8n.io/ | GitHub: https://github.com/n8n-io/n8n
- CrewAI: https://www.crewai.com/ | GitHub: https://github.com/crewAI/crewAI
- LangGraph: https://langchain-ai.github.io/langgraph/
- Temporal: https://temporal.io/
- Prefect: https://www.prefect.io/
- Make (Integromat): https://www.make.com/

### Competidores
- Jasper: https://www.jasper.ai/
- Copy.ai: https://www.copy.ai/
- Superlines: https://www.superlines.io/

### Repos Open-Source (Content Pipeline)
- dpgen-content-pipeline: https://github.com/MichaelCrowe11/dpgen-content-pipeline
- AI-Content-Studio: https://github.com/naqashafzal/AI-Content-Studio
- video-creator (offline): https://github.com/prakashdk/video-creator
- notebooklm-podcast-automator: https://github.com/israelbls/notebooklm-podcast-automator

---

> **N01 Research Analyst** | MISSION_content_factory_v1 | Wave 1
> 52 ferramentas avaliadas | 48 fontes consultadas | 8 categorias cobertas
> quality: null (peer-review pendente)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[output_content_factory_internal_audit]] | related | 0.33 |
| [[n06_api_access_pricing]] | downstream | 0.28 |
| [[spec_content_factory_v1]] | downstream | 0.24 |
| [[n04_output_cf_integration_kcs]] | related | 0.23 |
| [[p01_kc_notebooklm_integration]] | related | 0.23 |
| [[p01_kc_audio_tool]] | downstream | 0.21 |
| [[bld_knowledge_card_tts_provider]] | related | 0.21 |
| [[kc_api_reference]] | related | 0.19 |
| [[bld_collaboration_audio_tool]] | downstream | 0.17 |
| [[kc_open_source_ai_ecosystem]] | related | 0.17 |
