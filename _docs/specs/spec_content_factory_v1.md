---
id: spec_content_factory_v1
kind: constraint_spec
pillar: P06
title: "Spec Content Factory v1 -- Autonomous Digital Content Production Pipeline"
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
tldr: "Complete spec for autonomous Content Factory. Input: {{BRAND}} + brief. Output: videos, courses, ebooks, presentations, podcasts, posts. Zero new kinds. $0 stack: Claude + NotebookLM + Canva Business + open-source tools."
density_score: 0.97
quality: 9.0
updated: "2026-04-07"
---

# Spec Content Factory v1 -- The Machine That Creates Content

## VISION

```
USER: "I want a course about CEX explaining 8F, 12 pillars and nuclei"
           |
           v
    CONTENT FACTORY (autonomous)
           |
           v
    7+ outputs ready to publish:
    - Course (8 modules with quiz)
    - 90s demo video (Reels/TikTok)
    - Podcast (Audio Overview)
    - Presentation (slides PPTX/PDF)
    - eBook (PDF/EPUB)
    - Social posts (IG, LinkedIn, X, YouTube)
    - Landing page + checkout
```

**USER DOES NOTHING.** Nuclei handle everything from creation to publication.

---

## PRINCIPLES

1. **ZERO new kinds.** 115 existing kinds cover 100%. "Course" = workflow + prompt_templates.
2. **$0 stack.** Claude (engine) + NotebookLM (free) + Canva Business (existing subscription) + open-source.
3. **{{BRAND}} injection.** Every output receives brand identity automatically.
4. **8F on every artifact.** Quality guaranteed by the existing pipeline.
5. **Nuclei do everything.** From research to publication, zero human intervention.

---

## VALIDATED STACK (all tested 2026-04-06)

### Tools with Confirmed API/Credentials

| Tool | Type | Status | Credential | Cost |
|------|------|--------|------------|------|
| **Claude** | LLM engine (nuclei) | FUNCTIONAL | ANTHROPIC_API_KEY | Existing subscription |
| **Canva Business** | Design/Slides/Export | FUNCTIONAL | CANVA_CLIENT_ID + SECRET + ACCESS_TOKEN | Existing subscription |
| **NotebookLM** | Podcast/Video/Quiz/Flashcards/Slides | FUNCTIONAL | Google account (Playwright) | Free (PRO account) |
| **ElevenLabs** | TTS narration PT-BR | CONFIGURED | ELEVENLABS_API_KEY | Existing subscription |
| **Runway** | Video AI generation | CONFIGURED | RUNWAY_API_KEY | Credits |
| **Pika** | Alternative video AI | CONFIGURED | PIKA_API_KEY | Credits |
| **Kling** | Budget video AI | CONFIGURED | KLING_API_KEY | Credits |
| **Hailuo** | Video AI | CONFIGURED | HAILUO_API_KEY | Credits |
| **YouTube** | Video publish | CONFIGURED | YOUTUBE_API_KEY | Free |
| **Ayrshare** | Social multi-publish | CONFIGURED | AYRSHARE_API_KEY | Existing subscription |
| **Hotmart** | Course/checkout BR | CONFIGURED | MCP wired N06 | Commission |
| **Stripe** | Payment INT | CONFIGURED | STRIPE_SECRET_KEY | Commission |
| **MercadoPago** | Payment BR | CONFIGURED | MERCADOPAGO_* | Commission |
| **Supabase** | Database/Storage | CONFIGURED | SUPABASE_* | Free tier |
| **GitHub** | Repo/Deploy | CONFIGURED | GITHUB_PAT | Free |

### Open-Source Tools (local, $0)

| Tool | Function | Installation |
|------|----------|-------------|
| **Pandoc** | md -> PDF/EPUB/DOCX (40+ formats) | Local CLI |
| **Typst** | md -> professional PDF | Local CLI |
| **Marp** | md -> slides HTML/PDF/PPTX | Local CLI |
| **WeasyPrint** | HTML/CSS -> PDF | Python lib |
| **FFmpeg** | Video edit/concat/subtitles | Local CLI |
| **Remotion** | React -> programmatic video | Node.js |

### MCP Wiring (per nucleus)

| Nucleus | Available MCPs |
|---------|---------------|
| N01 Research | notebooklm, firecrawl, brave-search, fetch, markitdown |
| N02 Marketing | canva, notebooklm, browser, markitdown |
| N03 Engineering | canva, github, fetch |
| N04 Knowledge | notebooklm, supabase, postgres, firecrawl, fetch |
| N05 Operations | github, postgres |
| N06 Commercial | canva, notebooklm, hotmart, stripe, fetch, markitdown |

---

## CANVA CONNECT API -- Tested Capabilities

### Functional Endpoints

```
POST /v1/designs                    -> Create design (presentation, doc, whiteboard, custom size)
GET  /v1/designs?ownership=owned    -> List designs (25 found)
GET  /v1/designs/{id}               -> Design metadata
POST /v1/exports                    -> Export (PDF, PPTX, PNG, JPG, GIF, MP4)
GET  /v1/exports/{id}               -> Status + download URL
GET  /v1/users/me                   -> User ID + Team ID
```

### Validated Design Types

| Type | Preset/Custom | Dimensions |
|------|--------------|------------|
| Presentation | preset: `presentation` | Canva default |
| Document | preset: `doc` | Canva default |
| Whiteboard | preset: `whiteboard` | Canva default |
| Instagram Post | custom | 1080x1080 |
| Instagram Story | custom | 1080x1920 |
| YouTube Thumbnail | custom | 1280x720 |
| TikTok | custom | 1080x1920 |
| Facebook Post | custom | 1200x630 |
| LinkedIn Post | custom | 1200x627 |
| Twitter/X Post | custom | 1600x900 |

### Validated Exports

| Format | Status | Use |
|--------|--------|-----|
| PDF | FUNCTIONAL (download URL generated) | eBooks, handouts, docs |
| PPTX | FUNCTIONAL (download URL generated) | Editable presentations |
| PNG | FUNCTIONAL (download URL generated) | Social media, thumbnails |
| JPG | Available | Photos, banners |
| GIF | Available | Short animations |
| MP4 | Available | Slide videos |

### Current vs Required Scopes

| Scope | Status | Purpose |
|-------|--------|---------|
| design:meta:read | ACTIVE | List designs |
| design:content:read | ACTIVE | Read content |
| design:content:write | ACTIVE | Create designs |
| profile:read | ACTIVE | User info |
| asset:read | ACTIVE | List assets |
| folder:read | ACTIVE | List folders |
| asset:write | MISSING | Upload images/logos |
| brandtemplate:meta:read | MISSING | List brand templates |
| brandtemplate:content:read | MISSING | Read templates |
| folder:write | MISSING | Create folders |

**Action**: Add missing scopes in the Canva Developer portal to enable brand templates and asset uploads.

### Rate Limits

- ~10 creates/minute (429 after that)
- Exports: no observed limit
- Reads: no observed limit

---

## NOTEBOOKLM -- Validated Pipeline

### Confirmed Capabilities (tested by N04)

| Output | Type | Format | Content Factory Usage |
|--------|------|--------|----------------------|
| Audio Summary | Podcast 2 hosts | .wav/.mp3 | Onboarding, passive study, Spotify |
| Didactic Cards | Interactive flashcards | UI/export | Active study, course module review |
| Test (Quiz) | Questions + answers | UI/export | Course assessment, certification |
| Mind Map | Concept diagram | image | Visual overview, social post |
| Infographic | Static visual | image | Social media, ebook insert |
| Presentation | Slides | .pptx/.pdf | Meetings, training, classes |
| Video Summary | Generated video | .mp4 | Social content, YouTube |
| Reports | Structured doc | .pdf/.docx | Formal documentation |
| Data Table | Extracted data | table | Analysis, comparison |

### Automation Stack

```
KC .md (CEX) -> Playwright pastes as source -> NotebookLM indexes -> Studio generates outputs
```

**Proof of Concept**: 75 flashcards generated from kc_8f_pipeline.md (14.6KB)
**Account**: Gato Ao Cubo PRO (5x higher limits)
**Test notebook**: 940fd258-847f-47c1-b7e6-caca7b730681

### Available Tools

| Tool | Count | Function |
|------|-------|----------|
| notebooklm-mcp | 17 tools | Q&A, list notebooks, create notebooks |
| claude --chrome | 18 tools | Control real Chrome (Named Pipe) |
| Playwright (local) | Script | Browser automation, paste content |

### Limitations

- No official public API (automation via browser)
- Auth expires between sessions (requires periodic re-login)
- Puppeteer Chrome profile separate from system Chrome
- Rate: ~5 notebooks/hour recommended

---

## WAVE 2 ARTIFACTS -- ALREADY BUILT (48 artifacts, 228KB)

### Prompt Templates (7) -- `P03_prompts/templates/content_factory/`

| Template | File | Generates |
|----------|------|-----------|
| Video script | p03_pt_cf_video_script.md | Script with hook/build/benefit/proof/CTA |
| Lesson script | p03_pt_cf_lesson_script.md | Lesson script with objectives and exercises |
| Course outline | p03_pt_cf_course_outline.md | Course structure (modules, lessons, duration) |
| eBook chapter | p03_pt_cf_ebook_chapter.md | Chapter with intro/body/examples/summary |
| Slide deck | p03_pt_cf_slide_deck.md | Slide content with speaker notes |
| Quiz | p03_pt_cf_quiz.md | Multiple choice on content |
| Social post | p03_pt_cf_social_post.md | Post per platform (hook, value, CTA) |

### Action Prompts (7) -- `P03_prompts/actions/content_factory/`

| Action | Trigger |
|--------|---------|
| ap_cf_generate_course | "Create a course about {{TOPIC}}" |
| ap_cf_generate_video | "Create a {{DURATION}}s video about {{TOPIC}}" |
| ap_cf_generate_ebook | "Create an ebook about {{TOPIC}}" |
| ap_cf_generate_presentation | "Create a presentation about {{TOPIC}}" |
| ap_cf_generate_podcast | "Create a podcast about {{TOPIC}}" |
| ap_cf_generate_campaign | "Promote {{CONTENT}} on {{PLATFORMS}}" |
| ap_cf_publish | "Publish {{CONTENT}} on {{CHANNELS}}" |

### Constraint Specs (6) -- `P03_prompts/constraints/content_factory/`

| Spec | Defines |
|------|---------|
| cs_cf_video | Duration, aspect ratio, hook rules, CTA |
| cs_cf_course | Modules (5-12), lessons (3-8), quiz, certification |
| cs_cf_ebook | Chapters (5-15), words/chapter (2K-5K), formatting |
| cs_cf_presentation | Slides (10-30), bullets (3-5), speaker notes |
| cs_cf_podcast | Duration (10-30min), intro/body/outro |
| cs_cf_brief | Required brief fields |

### Function Defs (7) -- `P04_tools/functions/content_factory/`

| Tool | What it does |
|------|-------------|
| fn_cf_canva_create | Create design in Canva via API |
| fn_cf_canva_export | Export design (PDF/PPTX/PNG/MP4) |
| fn_cf_elevenlabs_tts | Generate narration via ElevenLabs |
| fn_cf_pdf_generate | Generate PDF via Typst/Pandoc/WeasyPrint |
| fn_cf_slides_generate | Generate slides via Marp |
| fn_cf_video_assemble | Assemble video via FFmpeg |
| fn_cf_ebook_compile | Compile ebook via Pandoc |

### DAGs (6) -- `P12_orchestration/dags/content_factory/`

| DAG | Pipeline |
|-----|----------|
| dag_cf_master | brief → research → author → produce → validate → publish |
| dag_cf_video | script → storyboard → TTS → video_gen → FFmpeg → export |
| dag_cf_course | outline → modulos → scripts → TTS → slides → quiz → LMS |
| dag_cf_ebook | outline → chapters → review → typeset → PDF/EPUB |
| dag_cf_presentation | outline → slide_content → Canva_create → export |
| dag_cf_social | extract_hooks → posts → schedule → publish |

### Workflows (5) -- `P12_orchestration/workflows/content_factory/`

| Workflow | What it does |
|----------|-------------|
| wf_cf_publish_youtube | Upload -> metadata -> thumbnail -> publish |
| wf_cf_publish_social | Adapt per platform -> schedule -> Ayrshare |
| wf_cf_publish_hotmart | Upload modules -> config checkout -> go live |
| wf_cf_promote | Extract hooks -> posts -> Canva thumbnails -> schedule 7d |
| wf_cf_email_launch | 5-day email sequence -> automation |

### Knowledge Cards (10) -- `P01_knowledge/library/integration/`

| KC | Content |
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

## MASTER PIPELINE -- dag_cf_master

```
BRIEF + {{BRAND}}
    |
    v
[WAVE 1: RESEARCH] --- N01
    |  Deep research on the topic
    |  Output: domain KCs + outline
    |
    v
[WAVE 2: AUTHOR] --- N03 + N02
    |  Generates scripts, outlines, copy (parallel)
    |  N03: course outline, lesson scripts, ebook chapters
    |  N02: social copy, email sequences, landing page
    |
    v
[WAVE 3: PRODUCE] --- N03 + N04 (parallel)
    |  N03 (Claude):
    |    -> Canva API: creates presentation + export PPTX/PDF
    |    -> Marp: generates alternative slides
    |    -> Typst/Pandoc: generates eBook PDF/EPUB
    |    -> ElevenLabs: generates narrations
    |    -> FFmpeg: assembles videos
    |
    |  N04 (NotebookLM):
    |    -> Pastes KCs into NotebookLM
    |    -> Generates: Audio Overview (podcast)
    |    -> Generates: Flashcards (75+ per KC)
    |    -> Generates: Quiz (assessment)
    |    -> Generates: Mind Map
    |    -> Generates: Slides (presentation)
    |    -> Generates: Video Overview
    |
    v
[WAVE 4: VALIDATE] --- N07
    |  Quality gates: cross-format consistency
    |  Tone check: uniform brand voice
    |  Brand check: colors, logo, {{BRAND_*}} applied
    |
    v
[WAVE 5: PUBLISH] --- N05 + N06 (parallel)
    |  N05: YouTube upload, GitHub release
    |  N06: Hotmart (course), Stripe/MP (checkout)
    |  N02: Ayrshare (social), email launch
    |
    v
COMPLETE OUTPUT -- USER DID NOTHING
```

---

## TEST CASE #1: CEX as {{BRAND}}

### Brand Config (seed by N06, Wave 1)

```yaml
BRAND_NAME: "CEX"
BRAND_TAGLINE: "The typed knowledge system that builds itself"
BRAND_ARCHETYPE: "magician"
BRAND_VOICE_TONE: "technical, confident, direct"
BRAND_STYLE: "dark-terminal-minimal"
BRAND_COLORS: {primary: "#0D1117", accent: "#58A6FF", success: "#3FB950"}
BRAND_FONTS: {heading: "JetBrains Mono", body: "Inter"}
BRAND_ICP: "Devs who want to monetize knowledge as info-products"
```

### Outputs to Produce

| # | Output | Format | Tool | Publish |
|---|--------|--------|------|---------|
| 1 | Course "CEX in Practice" (8 modules) | Video + slides + quiz | Claude + Canva + NotebookLM | Hotmart |
| 2 | eBook "CEX in 30 Pages" | PDF + EPUB | Typst + Pandoc | Gumroad/Hotmart |
| 3 | Video Demo 90s | MP4 9:16 | Claude + FFmpeg | YouTube Shorts, Reels, TikTok |
| 4 | Pitch Deck | PPTX + PDF | Canva API | SlideShare, LinkedIn |
| 5 | Podcast "CEX Explained" | MP3 | NotebookLM Audio Overview | Spotify, YouTube |
| 6 | 75+ Flashcards | Digital | NotebookLM | Curso (material complementar) |
| 7 | Quiz (assessment) | Digital | NotebookLM | Curso (certificacao) |
| 8 | Social Campaign (7 days) | Multi-platform posts | Claude + Canva + Ayrshare | IG, LinkedIn, X, YT |

### Course Structure (8 Modules)

| Module | Title | Content |
|--------|-------|---------|
| M1 | What is CEX | Overview, problem it solves, the X variable |
| M2 | 8F Pipeline | CONSTRAIN->BECOME->INJECT->REASON->CALL->PRODUCE->GOVERN->COLLABORATE |
| M3 | 12 Pillars | P01-P12: Knowledge, Identity, Prompts, Tools... |
| M4 | 115 Kinds | Type system, universal kinds, how they work |
| M5 | 7 Nuclei | N01-N07: Intelligence, Marketing, Engineering... |
| M6 | 109 Builders | ISOs, archetypes, how they build artifacts |
| M7 | Content Factory | The production pipeline (this spec!) |
| M8 | Launch | How to use CEX for your own {{BRAND}} |

---

## IMPLEMENTATION -- 4 Waves

### Wave 3: CEX Test (next)

| # | Task | Nucleus | Time |
|---|------|---------|------|
| 1 | Fill brand_config.yaml with CEX seed | N06 | 30min |
| 2 | Generate course outline (8 modules) using ap_cf_generate_course | N03 | 1h |
| 3 | Generate scripts for each module using tpl_cf_lesson_script | N03 | 2h |
| 4 | Paste KCs into NotebookLM -> generate podcast + flashcards + quiz | N04 | 1h |
| 5 | Create presentation in Canva via API -> export PPTX/PDF | N03 | 1h |
| 6 | Generate eBook via Typst/Pandoc | N03 | 1h |
| 7 | Generate 90s demo video | N03 | 1h |
| 8 | Generate social campaign (7 posts) | N02 | 1h |

### Wave 4: Validate + Publish

| # | Task | Nucleus |
|---|------|---------|
| 1 | Quality gate: review all outputs | N07 |
| 2 | Brand consistency check | N06 |
| 3 | Upload course to Hotmart | N06 |
| 4 | Upload video to YouTube | N05 |
| 5 | Publish social campaign | N02 |
| 6 | Email launch sequence | N02 |

### Wave 5: Evolve + Scale

| # | Task |
|---|------|
| 1 | /evolve on generated artifacts (quality improvement loop) |
| 2 | Second {{BRAND}} test (validate genericity) |
| 3 | cex_content_factory.py -- unified CLI |
| 4 | n8n visual workflow (optional) |

---

## GDP -- Pending Decisions

| # | Decision | Options | Status |
|---|----------|---------|--------|
| D1 | NotebookLM: 1 notebook per domain vs per mission? | Domain = reusable; Mission = disposable | OPEN |
| D2 | Which outputs to generate by default? | All vs subset (audio + flashcards + quiz) | OPEN |
| D3 | Auto-publish or approve first? | Auto = fast; Approval = control | OPEN |
| D4 | Local Chrome vs Firecrawl cloud? | Local = free; Cloud = paid, autonomous | OPEN |
| D5 | Dedicated Google account for automation? | Gato ao Cubo vs new account | OPEN |
| D6 | Canva: add extra scopes? | asset:write, brandtemplate:*, folder:write | OPEN |
| D7 | CEX course pricing | R$497 vs R$997 vs free (lead magnet) | OPEN |
| D8 | Course platform | Hotmart vs YouTube vs self-hosted | OPEN |

---

## SUCCESS METRICS

| Metric | Target |
|--------|--------|
| Time brief -> complete course | < 4 hours (autonomous) |
| Time brief -> eBook | < 1 hour |
| Time brief -> demo video | < 30 minutes |
| Cost per complete brief (7 outputs) | < R$15 |
| Average quality score | >= 8.5 |
| Formats generated per brief | >= 7 |
| Human intervention | 0 (validate only) |

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
