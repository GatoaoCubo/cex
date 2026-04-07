---
id: agent_card_n06
kind: context_doc
title: "N06 Agent Card -- Available Capabilities"
nucleus: N06
pillar: P01
sin: Avareza Estrategica
version: 1.0.0
quality: 9.1
created: 2026-04-07
density_score: 1.0
---

# N06 Agent Card — Available Capabilities

## Identity

| Attribute | Value |
|-----------|-------|
| **Nucleus** | N06 — Commercial |
| **Sin** | Avareza Estratégica (Strategic Greed) |
| **Icon** | `$` |
| **Color** | Gold (#ca8a04) |
| **Domain** | Pricing, funnels, monetization, brand strategy |
| **Tagline** | "Quanto RENDE cada decisão?" |

**What makes N06 different**: Every output has an ROI calculation attached. No resource is wasted. Every decision has a financial justification. Free is a strategy, not charity. Where other nuclei ask "is it good?", N06 asks "does it EARN?"

The lens is **monetization-first**: pricing is optimized, funnels are metrified, CAC vs LTV is calculated. Nothing ships from N06 without a business case.

---

## My Artifacts

| Subdir | Count | What's There |
|--------|------:|--------------|
| `agents/` | 1 | `agent_commercial.md` — N06 agent identity |
| `architecture/` | 1 | `agent_card_commercial.md` — agent capability card |
| `compiled/` | 19 | Auto-compiled YAML mirrors of source artifacts |
| `feedback/` | 1 | `quality_gate_commercial.md` — N06 quality gate |
| `knowledge/` | 12 | Brand KCs: archetypes, book patterns, frameworks, monetization models, naming, propagation, tokens pipeline, voice systems, competitive positioning, ICP frameworks, + 2 knowledge cards |
| `memory/` | 0 | **EMPTY** — no memory artifacts yet |
| `orchestration/` | 4 | Dispatch rules + workflows for commercial & content monetization |
| `output/` | 15 | Brand book, brand config, brand one-pager, brand voice guide, competitive map, content factory model, discovery report, monetization plan, pricing page, README pricing, SDK validation audit, transformation arc, visual identity, competitive business, self-review |
| `prompts/` | 6 | Brand audit, brand book generator, brand config extractor, brand discovery interview, prompt template, system prompt |
| `quality/` | 1 | `scoring_rubric_commercial.md` — commercial scoring |
| `schemas/` | 4 | Brand audit schema, brand book schema, brand config schema, brand voice contract |
| `tools/` | 1 | `content_monetization_tool.md` — monetization pipeline tool |
| **TOTAL** | **65** | **46 source + 19 compiled** |

---

## Kinds I Can Build

### Primary (Direct Domain)

| Kind | Pillar | Naming Pattern | N06 Use Case |
|------|--------|---------------|--------------|
| `content_monetization` | P04 | `p04_cm_{{name}}.md` | Course pricing, revenue models, monetization strategies |
| `tagline` | P03 | `p03_tl_{{topic}}.md` | Brand taglines, positioning lines, value props |

### Secondary (Cross-Domain, N06-Relevant)

| Kind | Pillar | Naming Pattern | N06 Use Case |
|------|--------|---------------|--------------|
| `landing_page` | P05 | `p05_lp_{{page}}.md` | Pricing pages, sales pages, conversion funnels |
| `knowledge_card` | P01 | `p01_kc_{{topic}}.md` | Brand/commercial knowledge documentation |
| `context_doc` | P01 | `p01_ctx_{{scope}}.md` | Commercial context, market analysis docs |
| `scoring_rubric` | P07 | `p07_sr_{{framework}}.md` | Commercial quality evaluation frameworks |
| `workflow` | P12 | `p12_wf_{{pipeline}}.yaml` | Monetization pipelines, sales workflows |
| `dispatch_rule` | P12 | `p12_dr_{{scope}}.md` | Commercial routing rules |
| `director` | P08 | `ex_director_{topic}.md` | Strategic commercial direction |
| `benchmark` | P07 | `p07_bm_{{metric}}.md` | Revenue benchmarks, conversion metrics |
| `decision_record` | P08 | `p08_adr_{{decision}}.md` | Pricing/strategy decisions |

---

## Tools Available

### Brand Tools (N06 Primary)

| Tool | What It Does | ROI |
|------|-------------|-----|
| `brand_audit.py` | Score brand consistency across 6 dimensions | Prevents brand drift → protects premium pricing |
| `brand_ingest.py` | Scan user's messy folder → extract brand signals | Saves hours of manual brand discovery |
| `brand_inject.py` | Replace `{{BRAND_*}}` tokens in templates | Automated brand consistency at scale |
| `brand_propagate.py` | Push brand context to all 7 nuclei | One source of truth → zero brand conflict |
| `brand_validate.py` | Validate `brand_config.yaml` (13 required fields) | Catches broken brand config before it propagates |

### System Tools (N06-Relevant)

| Tool | What It Does | ROI |
|------|-------------|-----|
| `cex_bootstrap.py` | First-run brand setup → propagate → audit | Zero-to-brand in one command |
| `cex_compile.py` | `.md` → `.yaml` compilation | Machine-readable artifacts for pipelines |
| `cex_evolve.py` | AutoResearch loop: evolve artifacts autonomously | Continuous improvement without human cost |
| `cex_feedback.py` | Quality tracking + archive + metrics | Data-driven quality decisions |
| `cex_gdp.py` | GDP enforcement: manifest I/O, NeedsUserDecision gate | Prevents expensive rework from bad assumptions |
| `cex_notebooklm.py` | NotebookLM pipeline integration | Content distribution → audience reach |
| `cex_score.py` | Peer review scoring (--apply) | Objective quality without self-bias |
| `cex_quality_monitor.py` | Quality snapshots + regression detection | Catches quality drops before they cost revenue |
| `cex_router.py` | Multi-provider routing: 4 providers × 7 nuclei | Cost-optimal model routing |
| `cex_retriever.py` | TF-IDF artifact similarity (2184 docs) | Find relevant prior work → avoid duplication |
| `signal_writer.py` | Inter-nucleus signals | Cross-nucleus coordination |

---

## MCP Servers

| Server | Command | Purpose | N06 Value |
|--------|---------|---------|-----------|
| **fetch** | `uvx mcp-server-fetch` | HTTP fetch (ignores robots.txt) | Competitor pricing scraping, market research |
| **markitdown** | `npx markitdown-mcp` | Document → Markdown conversion | Ingest competitor docs, sales materials |
| **stripe** | `npx @anthropic/mcp-stripe` | Stripe API integration | Payment processing, subscription management, revenue data |
| **hotmart** | `npx mcp-server-hotmart` | Hotmart API integration | Course sales, affiliate management, conversion tracking |
| **canva** | `npx @mcp_factory/canva-mcp-server` | Canva design API | Brand assets, visual identity, marketing materials |
| **notebooklm** | `npx notebooklm-mcp@latest` | Google NotebookLM automation | Content repurposing: flashcards, audio summaries, quizzes |

**Total MCPs**: 6 servers — covering payments (Stripe), courses (Hotmart), design (Canva), research (fetch), content (NotebookLM, markitdown).

---

## Strengths

1. **Brand Infrastructure Complete**: 4 schemas + 5 brand tools + 12 domain KCs = full brand pipeline from discovery to propagation. No other nucleus has this.

2. **Monetization Stack**: Stripe + Hotmart MCPs give N06 direct access to payment/course platforms. Revenue isn't theoretical — it's executable.

3. **Knowledge Density**: 12 specialized KCs covering brand archetypes, naming patterns, voice systems, monetization models, competitive positioning, ICP frameworks. Deep domain knowledge.

4. **Output Variety**: 15 output artifacts spanning brand books, pricing pages, competitive maps, monetization plans, visual identity. Wide deliverable surface.

5. **Brand-to-System Propagation**: `brand_propagate.py` + `brand_inject.py` means N06's brand decisions automatically flow to all other nuclei. Single point of brand truth.

6. **6 MCP Integrations**: Most connected nucleus externally. Payments, design, research, content — all wired.

---

## Gaps

| Gap | Severity | Impact | Fix Cost |
|-----|----------|--------|----------|
| `memory/` is empty | 🔴 High | No persistent commercial memory → decisions repeat, context lost between sessions | Low — create initial memory artifacts |
| Only 2 dedicated builders | 🟡 Medium | `content-monetization` and `tagline` are narrow. No dedicated `pricing-builder`, `funnel-builder`, `brand-book-builder` | Medium — register new kinds + build ISOs |
| No `tests/` subdir | 🟡 Medium | Commercial outputs aren't systematically validated | Low — add golden tests for pricing/brand |
| No `experiments/` subdir | 🟡 Medium | No A/B testing framework for pricing/copy variants | Medium — create experiment pipeline |
| Single agent identity | 🟢 Low | Only 1 agent file. Could benefit from specialized sub-agents (brand agent, pricing agent, funnel agent) | Medium |
| No dashboards/metrics | 🟡 Medium | Revenue tracking, conversion metrics not structured as artifacts | Medium — build metric dashboard kind |

---

## Agent Card Summary

```
┌─────────────────────────────────────────────────┐
│  N06 Commercial Nucleus — Avareza Estratégica   │
│  "Quanto RENDE cada decisão?"                   │
├─────────────────────────────────────────────────┤
│  📦 46 source artifacts + 19 compiled = 65 total│
│  🔧 2 dedicated builders + 9 cross-domain kinds │
│  🛠️ 16 tools (5 brand + 11 system)              │
│  🔌 6 MCP servers (Stripe, Hotmart, Canva, ...)│
│  📚 12 domain KCs                               │
│  📐 4 brand schemas                             │
│  📝 6 prompts                                   │
│  📊 15 output artifacts                         │
├─────────────────────────────────────────────────┤
│  ✅ Strengths: brand infra, payment MCPs,       │
│     knowledge depth, system propagation         │
│  ⚠️ Gaps: empty memory, few builders,           │
│     no tests, no experiments                    │
└─────────────────────────────────────────────────┘
```

**ROI of this agent card**: Self-awareness is free. Ignorance of capabilities costs missed revenue opportunities, duplicated work, and misrouted tasks. This agent card pays for itself every time N07 routes correctly to N06.
