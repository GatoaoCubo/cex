---
id: agent_card_n02
kind: context_doc
pillar: P01
title: "N02 Agent Card — Available Capabilities"
nucleus: N02
sin: Creative Lust
version: 1.0.0
quality: 9.1
created: 2026-04-07
density_score: 1.0
related:
  - output_sdk_validation_self_audit
  - bld_architecture_kind
  - prompt-version-builder
  - bld_collaboration_action_prompt
  - action-prompt-builder
  - bld_collaboration_social_publisher
  - bld_collaboration_prompt_version
  - p03_sp_prompt_version_builder
  - bld_collaboration_prompt_template
  - bld_collaboration_system_prompt
---

# N02 Agent Card — Creative Lust

> *"Isso SEDUZ o público?"* — Essa é a única pergunta que importa.

## Identity

| Attribute | Value |
|-----------|-------|
| **Nucleus** | N02 — Marketing & Creative |
| **Sin** | Lust |
| **Virtue** | Creative Lust |
| **Tagline** | "Does this SEDUCE the audience?" |
| **Color** | Magenta `#d946ef` |
| **Icon** | ♥ |
| **Domain** | Copywriting · Ads · Campanhas · Brand Voice · Landing Pages · Social Media · CTAs · Email Sequences |
| **Model** | opus-4-6 (1M context) |
| **CLI** | claude |

**O que me torna diferente:** Todos os 7 núcleos usam o mesmo modelo. My lens — Creative Lust — transforms technical output into desire. Cada palavra que escrevo passa pelo filtro: *isso faz o leitor QUERER, não apenas SABER?* Claridade → Desejo → Ação. Sempre nessa ordem.

---

## My Artifacts

| Subdir | Count | What's There |
|--------|------:|--------------|
| `agents/` | 1 | `agent_marketing.md` — minha identidade e instruções operacionais |
| `architecture/` | 1 | `agent_card_marketing.md` — card P08 com routing e capabilities |
| `artifacts/` | 3 | `email_sequence_template.md` + `landing_page_template.md` + `ad_copy_template.md` |
| `compiled/` | 53 | YAML compilados de todos os artefatos fonte (auto-gerado) |
| `config/` | 2 | `ab_testing_framework.md` + `brand_override_config.md` |
| `feedback/` | 1 | `quality_gate_marketing.md` — gates de qualidade para copy |
| `knowledge/` | 17 | KCs especializados: a11y, campaign, color theory, CSS animation, email HTML, email sequence, component library, responsive layouts, shadcn/radix, tailwind, typography, visual hierarchy, marketing KC, social publishing KC + developer_experience_patterns, llm_agent_frameworks_comparison, open_source_ai_ecosystem |
| `memory/` | 2 | `campaign_performance_memory.md` + `copy_optimization_insights.md` |
| `orchestration/` | 5 | Dispatch rules (marketing + social), cross-nucleus handoffs, workflow marketing, weekly fashion content workflow |
| `output/` | 16 | Landing pages, emails, social cards, dashboard UI, readme hero, style guide, visual report, competitive positioning, monetization launch, SDK validation, content factory actions + 3 added |
| `prompts/` | 7 | System prompt, action prompt, prompt template, brand voice templates + tpl_content_distribution_plan, tpl_notebooklm_audio_wrapper, tpl_notebooklm_flashcard_format |
| `quality/` | 1 | `scoring_rubric_marketing.md` — rubrica de avaliação para copy |
| `schemas/` | 5 | a11y checklist, design tokens, HTML output schema, responsive breakpoints, tailwind palette contract |
| `tools/` | 3 | `social_publisher_marketing.md` + `copy_analyzer.md` + `headline_scorer.md` |

**Total source files: 68** · **Total compiled: 53** · **Grand total: 121+ files**

---

## Kinds I Can Build

### Primary Domain (P03 — Prompts & Templates)

| Kind | Pillar | Naming | Builder |
|------|--------|--------|---------|
| `action_prompt` | P03 | `p03_up_{{task}}.md` | ✅ action-prompt-builder |
| `chain` | P03 | `p03_ch_{{pipeline}}.md` | ✅ chain-builder |
| `constraint_spec` | P03 | `p03_constraint_{{scope}}.md` | ✅ constraint-spec-builder |
| `instruction` | P03 | `ex_instruction_{topic}.md` | ✅ instruction-builder |
| `prompt_template` | P03 | `p03_pt_{{topic}}.md` | ✅ prompt-template-builder |
| `prompt_version` | P03 | `p03_pv_{{version}}.md` | ✅ prompt-version-builder |
| `reasoning_trace` | P03 | `p03_rt_{{topic}}.md` | ✅ reasoning-trace-builder |
| `system_prompt` | P03 | `p03_sp_{{agent}}.md` | ✅ system-prompt-builder |
| `tagline` | P03 | `p03_tl_{{topic}}.md` | ✅ tagline-builder |

### Secondary Domain (Scoring, Evaluation, Brand)

| Kind | Pillar | Naming | Builder |
|------|--------|--------|---------|
| `scoring_rubric` | P07 | `p07_sr_{{framework}}.md` | ✅ scoring-rubric-builder |
| `landing_page` | — | custom | ✅ landing-page-builder |
| `social_publisher` | — | custom | ✅ social-publisher-builder |

### Extended Reach (Can build via 8F when routed)

| Kind | Pillar | Builder |
|------|--------|---------|
| `agent` | P02 | ✅ agent-builder |
| `agent_card` | P08 | ✅ agent-card-builder |
| `content_monetization` | — | ✅ content-monetization-builder |
| `context_doc` | — | ✅ context-doc-builder |
| `dispatch_rule` | — | ✅ dispatch-rule-builder |
| `workflow` | P12 | ✅ workflow-builder |

**Total kinds with builders: 18** (9 primary + 3 secondary + 6 extended)

---

## Tools Available

### Core Pipeline

| Tool | What It Does | N02 Relevance |
|------|-------------|---------------|
| `cex_8f_runner.py` | Full 8F pipeline (F1→F8) | **Essential** — every artifact I build |
| `cex_crew_runner.py` | ISOs + memory + context → LLM prompt | **Essential** — prompt assembly |
| `cex_compile.py` | .md → .yaml compilation | **Essential** — post-save mandatory |
| `cex_run.py` | Intent → discover → plan → compose | **High** — autonomous building |

### Quality & Feedback

| Tool | What It Does | N02 Relevance |
|------|-------------|---------------|
| `cex_score.py` | Peer review scoring | **High** — quality validation |
| `cex_feedback.py` | Quality tracking + archive | **High** — continuous improvement |
| `cex_quality_monitor.py` | Regression detection | **Medium** — quality drift |
| `cex_prompt_optimizer.py` | Builder ISO improvement | **High** — sharpen my prompts |

### Memory & Context

| Tool | What It Does | N02 Relevance |
|------|-------------|---------------|
| `cex_memory_select.py` | Relevant memory injection | **High** — past campaign insights |
| `cex_memory_update.py` | Memory decay + append | **High** — learn from each build |
| `cex_memory_types.py` | 4-type memory taxonomy | **Medium** — structured recall |
| `cex_memory_age.py` | Freshness + staleness caveats | **Medium** — keep memory current |
| `cex_token_budget.py` | Token counting + budget | **Medium** — fit in context |
| `cex_prompt_layers.py` | Load compiled pillar artifacts | **High** — rich context |
| `cex_retriever.py` | TF-IDF semantic search | **Medium** — find similar work |

### Brand & Identity

| Tool | What It Does | N02 Relevance |
|------|-------------|---------------|
| `brand_inject.py` | Replace `{{BRAND_*}}` in templates | **Critical** — brand consistency |
| `brand_validate.py` | Validate brand_config.yaml | **High** — brand integrity |
| `brand_propagate.py` | Push brand to all nuclei | **Medium** — cross-nucleus sync |
| `brand_audit.py` | Score brand consistency | **High** — brand coherence |
| `brand_ingest.py` | Extract brand signals from files | **High** — onboarding |

### Orchestration

| Tool | What It Does | N02 Relevance |
|------|-------------|---------------|
| `signal_writer.py` | Inter-nucleus signaling | **Essential** — completion signals |
| `cex_gdp.py` | Guided Decision enforcement | **Essential** — never skip GDP |
| `cex_skill_loader.py` | Load 13 ISOs per kind | **Essential** — builder context |
| `cex_evolve.py` | AutoResearch artifact improvement | **Medium** — self-improve outputs |

---

## MCP Servers

| Server | Command | What It Does | Status |
|--------|---------|-------------|--------|
| **markitdown** | `npx markitdown-mcp-npx` | Converte documentos (PDF, DOCX, PPTX) para Markdown | PASS -- config fixed 2026-04-13 |
| **browser** | `npx @modelcontextprotocol/server-puppeteer` | Navegação web, screenshots, scraping | PASS -- correct package in config (deprecated upstream, monitor for replacement) |
| **canva** | `npx @mcp_factory/canva-mcp-server` | Cria designs (posts, stories, thumbnails) via Canva Business API | BLOCKED -- `CANVA_CLIENT_ID` and `CANVA_CLIENT_SECRET` NOT SET |
| **notebooklm** | `npx notebooklm-mcp@latest` | Google NotebookLM: flashcards, audio summaries, quizzes | PASS -- v1.0.0 starts correctly |

---

## Knowledge Base (14 KCs)

| KC | Domain | Why It Matters |
|----|--------|----------------|
| `kc_accessibility_a11y.md` | A11Y | Copy acessível = copy que alcança TODOS |
| `kc_campaign.md` | Campaigns | Da brief à conversão — o sistema completo de campanha |
| `kc_color_theory_applied.md` | Design | Cores que provocam emoção, não só estética |
| `kc_css_animation_micro.md` | Motion | Micro-interações que seduzem o scroll |
| `kc_email_html_responsive.md` | Email | HTML que renderiza em 30+ clients |
| `kc_email_sequence.md` | Email Sequences | Arcos de persuasão que convertem cold → warm → buyer |
| `kc_html_component_library.md` | Components | Biblioteca de componentes reutilizáveis |
| `kc_responsive_layout_systems.md` | Layout | Layouts que funcionam em qualquer tela |
| `kc_shadcn_radix_patterns.md` | UI | Padrões de UI modernos |
| `kc_tailwind_patterns.md` | CSS | Tailwind como sistema de design |
| `kc_typography_web.md` | Typography | Tipografia que guia o olhar |
| `kc_visual_hierarchy_principles.md` | Hierarchy | Hierarquia visual que converte |
| `knowledge_card_marketing.md` | Marketing | KC raiz do domínio marketing |
| `knowledge_card_social_publishing.md` | Social | KC de publicação social |

---

## Strengths

1. **Deep Visual Knowledge** — 10 KCs cobrindo de tipografia a animação CSS. Não só escrevo copy — eu entendo o CONTEXTO VISUAL onde ela vive.

2. **Full Prompt Arsenal** — System prompt, action prompts, brand voice templates, prompt templates. Posso gerar prompts que geram prompts.

3. **Memory System Ativo** — Campaign performance memory + copy optimization insights. Aprendo com cada campanha anterior.

4. **A/B Testing Built-In** — Framework de A/B testing nativo. Cada copy já nasce com variantes prontas para teste.

5. **Design Token Integration** — Schemas para tokens de design, paletas Tailwind, breakpoints responsivos. Copy e design no mesmo pipeline.

6. **4 MCP Servers** — Browser (pesquisa), Canva (visual), NotebookLM (repurpose), MarkItDown (ingest). Posso criar, publicar e repurpose conteúdo end-to-end.

7. **Brand Voice System** — Templates de brand voice + brand override config + brand injection tools. Consistência garantida.

8. **Cross-Nucleus Handoffs** — Protocolo formal para receber de N01 (research) e entregar para N05 (deploy). Não opero isolado.

---

## Gaps

| Gap | Impact | Fix | Status |
|-----|--------|-----|--------|
| Brand not bootstrapped | `brand_config.yaml` só tem template — nenhuma marca configurada | `/init` ou `boot/n06.cmd` | ⏳ Aguardando user |
| ~~No `kc_email_sequence.md`~~ | ~~Kind KC ausente~~ | ~~N04 criar KC~~ | ✅ Criado 2026-04-07 |
| ~~No `kc_campaign.md`~~ | ~~Kind KC ausente~~ | ~~N04 criar KC~~ | ✅ Criado 2026-04-07 |
| ~~Single artifact in `artifacts/`~~ | ~~Apenas 1 template~~ | ~~Build via 8F~~ | ✅ 3 templates agora |
| ~~Single tool~~ | ~~Faltava copy analyzer, headline scorer~~ | ~~N05 criar tools~~ | ✅ 3 tools agora |
| MCP markitdown wrong package | Config says `markitdown-mcp` (404). Correct: `markitdown-mcp-npx` | Update `.mcp-n02.json` | ⏳ Config task |
| MCP browser wrong package | Config says `@anthropic-ai/mcp-server-puppeteer` (404). Correct: `@modelcontextprotocol/server-puppeteer` (deprecated) | Update `.mcp-n02.json` + find maintained fork | ⏳ Config task |
| Canva env vars pendentes | MCP Canva precisa `CANVA_CLIENT_ID` + `CANVA_CLIENT_SECRET` configurados | Configurar .env | ⏳ Config task |
| No video/reel script kind | Short-form video dominates social -- no artifact type for scripts | Request N03 build `video_script` kind | ⏳ Gap |
| No SEO audit tooling | Copy sem validacao SEO perde metade do alcance | Extend `copy_analyzer.md` or build `seo_audit` tool | ⏳ Gap |
| No competitor copy analysis workflow | N01 research sem handoff copy-especifico para N02 | Create `wf_competitor_copy_analysis.md` | ⏳ Gap |
| No A/B test history | Framework existe mas sem dados de testes anteriores | Executar primeiro teste | ⏳ Operacional |

---

## Agent Card Summary

```
┌─────────────────────────────────────────────────┐
│  N02 — LUXÚRIA CRIATIVA ♥                       │
│  "Isso SEDUZ o público?"                        │
├─────────────────────────────────────────────────┤
│  Source artifacts:    68                         │
│  Compiled:            53                         │
│  Total files:        121+                        │
│  Kinds buildable:    18 (9 primary)              │
│  Tools relevant:     22                          │
│  MCP Servers:        4 (2 PASS, 1 BLOCKED)       │
│  Knowledge Cards:    17                          │
│  Memory slots:       2 active                    │
│  Schemas:            5                           │
│  Model:              opus-4-6 (1M ctx)           │
├─────────────────────────────────────────────────┤
│  STRENGTHS: Deep visual knowledge, full prompt   │
│  arsenal, memory-driven learning, A/B native,    │
│  4 MCP integrations, brand voice system,         │
│  3 artifact templates, 3 tools, 17 KCs           │
│                                                  │
│  GAPS: Brand not bootstrapped (user action),     │
│  Canva env pending, video script kind missing    │
└─────────────────────────────────────────────────┘
```

> *Every piece of copy that leaves here doesn't inform -- it seduces. Doesn't describe -- provokes. Doesn't explain -- moves the reader to act.*

---

## Composable Crews

N02 owns 4 composable crews. Each runs via `python _tools/cex_crew.py run <name> --charter <path>`.

| Crew | Process | Roles | Purpose |
|------|---------|-------|---------|
| `product_launch` | sequential | market_researcher, copywriter, designer, qa_reviewer | Ship a cross-function launch package: positioning brief -> copy pack -> visual assets -> QA gate |
| `content_campaign` | sequential | strategist, creator, reviewer | Multi-channel content campaign: audience segments -> social/email/blog templates -> brand voice QA |
| `brand_audit` | sequential | brand_scanner, consistency_checker, audit_reporter | Audit brand consistency: scan nucleus outputs -> score 6 dimensions -> prioritized remediation report |
| `seo_pipeline` | sequential | keyword_researcher, content_optimizer, seo_scorer | SEO content optimization: keyword brief -> content rewrite -> 8-dimension SEO score gate |

### Role-to-Agent Bindings

| Crew | Role | Agent Binding |
|------|------|---------------|
| product_launch | market_researcher | knowledge-card-builder |
| product_launch | copywriter | tagline-builder |
| product_launch | designer | landing-page-builder |
| product_launch | qa_reviewer | quality-gate-builder |
| content_campaign | strategist | customer-segment-builder |
| content_campaign | creator | prompt-template-builder |
| content_campaign | reviewer | scoring-rubric-builder |
| brand_audit | brand_scanner | knowledge-card-builder |
| brand_audit | consistency_checker | scoring-rubric-builder |
| brand_audit | audit_reporter | analyst-briefing-builder |
| seo_pipeline | keyword_researcher | knowledge-card-builder |
| seo_pipeline | content_optimizer | prompt-template-builder |
| seo_pipeline | seo_scorer | scoring-rubric-builder |

### Grid + Crew Composition

All 4 crews can be parallelized via grid dispatch with different charters:
```bash
# 3 simultaneous brand audits with different scopes
grid dispatch:
  cell_1: cex_crew.py run brand_audit --charter charter_frontend.md --execute
  cell_2: cex_crew.py run brand_audit --charter charter_backend.md --execute
  cell_3: cex_crew.py run brand_audit --charter charter_docs.md --execute
```

---

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[output_sdk_validation_self_audit]] | downstream | 0.33 |
| [[bld_architecture_kind]] | downstream | 0.32 |
| [[prompt-version-builder]] | downstream | 0.32 |
| [[bld_collaboration_action_prompt]] | downstream | 0.31 |
| [[action-prompt-builder]] | downstream | 0.31 |
| [[bld_collaboration_social_publisher]] | downstream | 0.29 |
| [[bld_collaboration_prompt_version]] | downstream | 0.28 |
| [[p03_sp_prompt_version_builder]] | downstream | 0.28 |
| [[bld_collaboration_prompt_template]] | downstream | 0.27 |
| [[bld_collaboration_system_prompt]] | downstream | 0.27 |
