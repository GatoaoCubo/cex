---
id: deck_n02
kind: context_doc
title: N02 Deck -- Available Capabilities
nucleus: N02
sin: Luxuria Criativa
version: 1.0.0
pillar: P01
quality: null
created: 2026-04-07
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus | N02 -- Marketing & Creative |
| Sin | Luxuria Criativa (Creative Lust) |
| Domain | Copywriting, ads, campaigns, brand voice, social media, CTAs, landing pages |
| CLI | Claude (Opus 4.6, 1M context) |
| Mantra | clarity -> desire -> action |
| Standard practice | A/B copy variants on every deliverable |

**Routing rules:**
- Route TO N02: copywriting, ads, headlines, CTAs, landing pages, email sequences, brand voice, social media, campaign copy, visual output
- Route AWAY: research/papers (N01), artifact construction (N03), code/deploy (N05), pricing strategy (N06)

## My Artifacts

| Subdir | Count | Purpose |
|--------|-------|---------|
| agents | 1 | Agent definition for marketing nucleus |
| architecture | 1 | Agent card (N02 capabilities) |
| artifacts | 1 | Email sequence template |
| config | 2 | A/B testing framework, brand override config |
| feedback | 1 | Quality gate for marketing output |
| knowledge | 12 | Design KCs: accessibility, color theory, CSS animation, email HTML, component library, responsive layouts, shadcn/radix, Tailwind, typography, visual hierarchy, marketing KC, social publishing KC |
| memory | 2 | Campaign performance memory, copy optimization insights |
| orchestration | 5 | Cross-nucleus handoffs, dispatch rules (marketing + social), weekly fashion workflow, marketing workflow |
| output | 13 | Templates: CF actions, competitive positioning, dashboard UI, email, monetization launch, README hero, SDK self-audit, social card, style guide, visual report, component, landing page, self-review |
| prompts | 4 | Action prompt, brand voice templates, prompt template, system prompt |
| quality | 1 | Scoring rubric for marketing artifacts |
| schemas | 5 | A11y checklist, design tokens, HTML output schema, responsive breakpoints, Tailwind palette contract |
| tools | 1 | Social publisher tool |
| **Total** | **49** | |

## Kinds I Build

| Kind | Pillar | Domain Fit |
|------|--------|------------|
| prompt_template | P03 | Campaign prompts, ad copy templates, email sequences |
| action_prompt | P03 | Marketing action triggers, CTA prompts |
| system_prompt | P03 | Marketing nucleus persona, brand voice injection |
| tagline | P03 | Brand taglines, slogans, headlines |
| landing_page | P05 | Conversion-optimized landing pages (HTML/Tailwind) |
| social_publisher | P04 | Social media post creation and scheduling |
| content_monetization | P04 | Content packaging for revenue (courses, gated content) |
| knowledge_card | P01 | Marketing domain KCs (patterns, best practices) |
| context_doc | P01 | Marketing context briefs, campaign briefs |
| few_shot_example | P01 | Copy examples for prompt calibration |
| response_format | P05 | Structured output for marketing deliverables |
| scoring_rubric | P07 | Quality criteria for marketing artifacts |
| quality_gate | P11 | Pass/fail gates for marketing output |
| dispatch_rule | P12 | Routing rules for marketing tasks |
| workflow | P12 | Multi-step marketing workflows (campaigns, launches) |
| workflow_primitive | P12 | Reusable marketing workflow steps |

## Tools I Use

| Tool | Purpose |
|------|---------|
| `cex_compile.py` | Compile .md artifacts to .yaml after every save |
| `cex_8f_runner.py` | Execute full 8F pipeline for artifact creation |
| `cex_crew_runner.py` | Compose prompts from ISOs + memory + brand context |
| `cex_score.py` | Peer review scoring (quality assigned by others, never self) |
| `cex_feedback.py` | Track quality metrics, archive feedback |
| `cex_retriever.py` | Find similar artifacts for Template-First approach |
| `cex_prompt_optimizer.py` | Analyze and improve prompt ISOs |
| `cex_memory_select.py` | Inject relevant memories into build context |
| `cex_token_budget.py` | Manage token allocation across long campaigns |
| `cex_notebooklm.py` | Push KCs to NotebookLM for audio/human content |
| `cex_evolve.py` | Auto-improve existing marketing artifacts |
| `cex_quality_monitor.py` | Track quality snapshots and detect regressions |
| `signal_writer.py` | Signal N07 on task completion |

## MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| **markitdown** | `markitdown-mcp` | Convert documents (PDF, DOCX, PPTX) to markdown for content extraction |
| **browser** | `@anthropic-ai/mcp-server-puppeteer` | Browse competitor sites, take screenshots, inspect live landing pages |
| **canva** | `@mcp_factory/canva-mcp-server` | Create and edit designs via Canva API (social cards, banners, presentations) |
| **notebooklm** | `notebooklm-mcp@latest` | Push KCs to Google NotebookLM for podcast/audio content generation |

## My Strengths

1. **Visual output depth**: 13 output templates covering the full marketing stack -- from social cards to dashboard UIs to landing pages
2. **Design knowledge**: 12 specialized KCs covering Tailwind, typography, color theory, accessibility, responsive layouts, CSS animation, visual hierarchy -- deep frontend/design expertise
3. **Schema rigor**: 5 schema contracts (design tokens, responsive breakpoints, Tailwind palette, HTML output, a11y) ensure consistent visual output
4. **Orchestration maturity**: 5 orchestration artifacts including cross-nucleus handoffs, dispatch rules, and a full weekly content workflow
5. **Memory-driven optimization**: Campaign performance memory + copy optimization insights allow learning from past results
6. **Full MCP stack**: Browser for competitive research, Canva for design, markitdown for content ingestion, NotebookLM for human-consumable content

## My Gaps

| Area | Status | What's Missing |
|------|--------|----------------|
| artifacts/ | 1 file | Only email template -- needs ad copy templates, social post templates, campaign brief templates |
| tools/ | 1 file | Only social publisher -- needs A/B test runner, copy analyzer, headline scorer |
| feedback/ | 1 file | Only quality gate -- needs copy performance feedback loops, conversion tracking |
| config/ | 2 files | Missing: social platform configs, email provider config, analytics integration |
| architecture/ | 1 file | Agent card only -- needs N02 architecture diagram, integration map |
| Landing pages | 0 dedicated | Template exists in output/ but no pre-built landing page artifacts |
| Ad copy | 0 files | No dedicated ad copy artifacts despite being core domain |
| Campaign briefs | 0 files | No structured campaign planning documents |

## Cards in My Deck

| Category | Count |
|----------|-------|
| Artifacts (all .md in N02_marketing/) | 49 |
| Kinds I build | 16 |
| Tools I use | 13 |
| MCP servers | 4 |
| Builder agents available | 16 |
| Knowledge cards (local) | 12 |
| **Total cards in deck** | **110** |
