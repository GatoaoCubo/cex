---
id: kc_competitor_llamaindex
kind: knowledge_card
pillar: P01
nucleus: n01
domain: competitive-intelligence
version: 1.0.0
created: 2026-04-24
quality: null
tags: [seed-intel, competitor, llamaindex, rag, document-intelligence, llamacloud, jerry-liu]
tldr: "LlamaIndex is the RAG-first framework with 48.9K GitHub stars, $27.5M funding, and 25M+ monthly downloads -- pivoting from data indexing to document-centric AI agents via LlamaCloud, with native MCP support but limited agentic orchestration depth."
---

# Competitor Profile: LlamaIndex

## Overview

LlamaIndex (originally GPT Index) is the dominant Python framework for **Retrieval-Augmented Generation (RAG)**
and document-centric AI applications. Founded by **Jerry Liu** (originally at Stanford NLP and Uber ATG),
it was launched via tweet on November 8, 2022, as a simple tree-index for LLMs. It has since evolved into
a comprehensive platform for connecting LLMs with custom data sources across 300+ integration packages.

As of April 2026, LlamaIndex has **48.9K GitHub stars**, **25M+ monthly downloads**, and a commercial
cloud offering -- **LlamaCloud** -- that provides hosted document parsing, structured extraction, and
agent deployment. The company has raised **$27.5M total** ($19M Series A led by Norwest Venture Partners,
with Greylock participation, March 2025).

The strategic pivot of 2025-2026: LlamaIndex is repositioning from "RAG library" to **"Document Agent Platform"**
-- the official tagline is now "AI Agents for Document OCR + Workflows." This brings it into direct competition
with enterprise IDP (Intelligent Document Processing) vendors like AWS Textract, Azure Form Recognizer,
and commercial OCR platforms, while maintaining developer community through the OSS framework.

**Strategic signal for CEX:** LlamaIndex is the closest framework to CEX in architectural philosophy --
it understands that knowledge infrastructure (indices, retrieval, memory) must underpin agents. However,
it is entirely data-retrieval-focused and has no typed artifact governance, no nuclei specialization,
no quality gates, and no 8F reasoning protocol. CEX's P01_knowledge pillar is architecturally superior
to LlamaIndex: CEX types knowledge into 300 kinds, enforces quality scoring, and compiles knowledge
into searchable artifacts -- LlamaIndex indexes whatever you give it without governance.

---

## Key Metrics

| Metric | Value | Source date |
|--------|-------|-------------|
| GitHub stars | 48,900 | April 2026 |
| GitHub forks | 7,300 | April 2026 |
| GitHub watchers | 272 | April 2026 |
| Open issues | 184 | April 2026 |
| Open PRs | 126 | April 2026 |
| Latest version | v0.14.21 | April 21, 2026 |
| Total releases | 493 | April 2026 |
| License | MIT | GitHub |
| Primary language | Python (71.9%), Jupyter (25.5%) | GitHub |
| Monthly downloads | 25M+ | llamaindex.ai |
| LlamaCloud signups | 300K+ | llamaindex.ai |
| LlamaParse users | 300K+ | llamaindex.ai |
| Documents processed (LlamaParse) | 1B+ | llamaindex.ai |
| 300+ integration packages | LlamaHub | llamahub.ai |
| Contributors | 1,500+ | llamaindex.ai |
| Total funding | $27.5M | Pulse2 / Outpost AI |
| Series A | $19M | March 2025 (Norwest + Greylock) |
| Series A lead | Norwest Venture Partners | March 2025 |
| Company headcount | ~20 | At Series A |

---

## Technical Architecture

LlamaIndex's architecture centers on a **modular, index-first design** -- data is loaded, structured
into indices, and queried through retrieval interfaces. The framework separates data ingestion,
storage, retrieval, and application logic as distinct composable layers.

### Core Stack

| Layer | Components | Function |
|-------|-----------|---------|
| **Data Connectors** | 300+ integrations (APIs, PDFs, SQL, cloud storage) | Ingest from any source |
| **Indices** | VectorStoreIndex, SummaryIndex, KnowledgeGraphIndex, etc. | Structure data for retrieval |
| **Retrieval** | Dense, sparse, hybrid, HyDE, recursive retrieval | Query interface over indexed data |
| **Query Engines** | Sub-question, router, flare, citation | Advanced query decomposition |
| **Chat Engines** | Context-conditioned conversation with memory | Stateful multi-turn |
| **Agents** | OpenAI function-calling, ReAct, custom | Active reasoning with tool use |
| **LlamaCloud Services** | LlamaParse, LlamaExtract, LlamaAgents | Hosted enterprise processing |
| **Workflows** | Event-driven async agent graphs (LlamaIndex Workflows) | Complex multi-step pipelines |

### LlamaCloud Products

| Product | Description | Pricing model |
|---------|-------------|--------------|
| **LlamaParse** | Enterprise document parsing; 50+ file types; complex layouts, tables, images, charts | Credits: $0.003/page; free: 7K pages/month or 10K credits |
| **LiteParser** | Local OSS parsing; no cloud, no LLM costs; major formats, bounding box output | Free (self-hosted) |
| **LlamaExtract** | Schema-based structured extraction from documents (no ML training required) | Credits-based |
| **LlamaAgents** | Deployed document agents with routing to specialized sub-agents | Enterprise |
| **LlamaIndex OSS** | Core Python framework; indexing + retrieval + agent orchestration | Free (MIT) |

### MCP Support

| Aspect | Details |
|--------|---------|
| Support status | Native, production (multiple MCP integrations released 2025) |
| OSS integration | "Use tools exposed by any MCP-compatible server in one line of code" |
| Workflows as MCP servers | LlamaIndex Workflows can be exposed as MCP servers (bidirectional) |
| Documentation search MCP | Native MCP server for LlamaIndex docs (enables coding agents to search docs) |
| 2026 roadmap | MCP servers acting as agents; "fractal" agentic systems via MCP |
| Direction | Both client (consume MCP servers) and server (expose workflows as MCP) |
| Integration depth | First-class; "closely following MCP progress" per official X post |

### LLM Provider Support

| Provider | Status |
|----------|--------|
| OpenAI | Primary reference implementation |
| Anthropic | Supported |
| Cohere | Supported |
| Hugging Face | Supported |
| Ollama | Supported (local) |
| Azure OpenAI | Supported |
| 40+ LLM providers | Via LlamaHub integrations |

---

## Community Strategy

LlamaIndex operates a dual community model: developer OSS community (GitHub, Discord, X) and
an enterprise developer community (LlamaCloud signups, enterprise case studies).

| Channel | Activity level | Size |
|---------|---------------|------|
| GitHub | Very high -- 493 releases, 1,500+ contributors | 48.9K stars |
| X (Twitter) | High -- active announcements, technical threads | Large following |
| Discord | Active | Not publicly disclosed |
| LlamaIndex blog (llamaindex.ai/blog) | High -- weekly posts, release notes | Developer audience |
| LinkedIn | Moderate | company presence |
| YouTube | Moderate -- tutorials, webinars | Not publicly disclosed |
| LlamaHub (integration marketplace) | High -- 300+ integrations | Developer ecosystem |
| Enterprise case studies | Active -- Jeppesen/Boeing, NTT Data, Carlyle | Enterprise credibility |

**Key community differentiator:** LlamaIndex treats documentation and tutorials as a primary
acquisition channel. The Jupyter notebook composition (25.5% of repo) signals that examples
and tutorials are embedded in the codebase itself.

---

## Distribution Channels

| Channel | Description | Reach |
|---------|-------------|-------|
| pip install llama-index | Primary OSS install | 25M+ monthly downloads |
| LlamaHub (llamahub.ai) | 300+ integration packages marketplace | Developer ecosystem |
| GitHub | Discovery | 48.9K stars |
| LlamaCloud (SaaS) | Hosted platform; direct enterprise acquisition | 300K+ signups |
| Enterprise sales | Fortune 500 direct; NTT Data, Carlyle, Boeing case studies | High-value |
| LlamaParse freemium | 7K free pages/month -- developer hook into paid | Credit conversion funnel |
| Norwest / Greylock networks | Investor-facilitated enterprise introductions | Strategic |
| LlamaIndex blog + tutorials | SEO-optimized developer acquisition | High-intent traffic |
| Conference presence (NeurIPS, ICLR, etc.) | Research community credibility | Enterprise AI teams |

---

## Pricing Model

| Tier | Cost | Details |
|------|------|---------|
| LlamaIndex OSS | Free (MIT) | Self-hosted; unlimited; pip install |
| LlamaParse Free | Free | 10,000 credits/month (~1,000 pages) |
| LlamaParse Paid | $0.003/page | Credit system: 1,000 credits = $1 |
| LlamaCloud Enterprise | Custom | HIPAA, GDPR, SOC2; dedicated VPC; SLA |
| LiteParser | Free (open source) | Local parsing; no cloud dependency |

**Credit system details:**
- 1,000 credits = $1.00
- Actions vary by complexity (page parsing vs. structured extraction vs. agent deployment)
- Free tier: 10,000 credits/month (~1,000 pages of LlamaParse)
- Cost unpredictability is a documented criticism from developers

**Enterprise features (LlamaCloud):**
- HIPAA, GDPR, SOC2 compliance
- VPC deployment option
- Dedicated support + mission-critical SLAs
- Granular access controls + enhanced encryption
- 99.9% uptime SLA

---

## Strengths

| Strength | Evidence |
|----------|---------|
| RAG ecosystem dominance | 48.9K stars; 25M+ downloads; category-defining framework |
| 300+ integrations (LlamaHub) | Largest integration ecosystem in the retrieval space |
| Document intelligence depth | LlamaParse benchmarks beat commercial IDP platforms |
| 1B+ documents processed | Production credibility at enterprise scale |
| Native MCP (bidirectional) | Both consumes AND exposes MCP -- most advanced MCP posture of the set |
| $27.5M funding + Norwest/Greylock | Tier-1 investors; operational runway |
| Enterprise compliance | HIPAA, GDPR, SOC2 -- required for healthcare, finance, legal |
| Named enterprise customers | Boeing (Jeppesen), NTT Data, Carlyle -- Fortune 500 proof points |
| Freemium pipeline | 10K free credits = low-friction enterprise trial |
| Active release cadence | v0.14.21 April 2026; 493 total releases |
| Jupyter-embedded tutorials | Lower barrier for data science / ML audience |
| Jerry Liu's credibility | Stanford NLP + Uber ATG = research and production credibility |

---

## Weaknesses (Gaps CEX Could Exploit)

| Weakness | CEX Exploit Angle |
|----------|------------------|
| RAG-only depth, shallow orchestration | CEX has 7 specialized nuclei + 300 kinds; LlamaIndex is great at retrieval, weak at agentic governance |
| No typed artifact taxonomy | LlamaIndex indexes documents; CEX produces typed, compilable, scored artifacts |
| No quality gates | LlamaIndex has no scoring rubric; CEX enforces 9.0 target with 8F pipeline |
| No multi-nucleus governance | LlamaIndex has agents, not specialized nuclei with domain separation |
| Unpredictable credit costs | Credit system creates budgeting anxiety; CEX is self-hosted with no per-operation fee |
| Steep Workflows learning curve | LlamaIndex Workflows complex; CEX 8F pipeline is universal, nucleus-agnostic |
| No GDP protocol | No guided decision framework; CEX separates user decisions from LLM execution |
| No brand injection | No brand awareness; CEX has brand_config.yaml auto-injected |
| No self-improvement loop | No equivalent to cex_evolve.py; LlamaIndex does not improve its own artifacts |
| Document-centric only | CEX covers all 12 pillars; LlamaIndex excels at P01/P10 but not P03/P05/P08/P12 |
| No sin-driven optimization | LlamaIndex has no domain-optimized reasoning lens; CEX nuclei have sin-based bias |
| Commercial lock-in risk | LlamaParse is proprietary; LiteParser is weaker; CEX has no such parsing dependency |
| 184 open issues | Highest issue count of the four frameworks -- quality/maintenance signal |

---

## Key People

| Person | Role | Background | Social |
|--------|------|-----------|--------|
| Jerry Liu | Co-founder & CEO | Stanford NLP PhD dropout; ex-Uber ATG (autonomous vehicles ML); launched LlamaIndex via tweet Nov 2022 | @jerryjliu0 (X); github.com/jerryjliu; LinkedIn |
| Simon Suo | Co-founder & CTO | Co-founded with Liu; engineering and infrastructure | LinkedIn |
| Logan Markewich | Core maintainer | Key open-source contributor; frameworks + integrations | github.com/logan-markewich |
| Laurie Voss | VP of Developer Relations | ex-npm CTO; developer community and evangelism | @seldo (X) |
| Norwest Venture Partners | Series A lead investor | Investment portfolio: Salesforce, Box, Lyft | norwestco.com |
| Greylock | Series A participant | Tier-1 VC (LinkedIn, Airbnb, Facebook early) | greylock.com |

---

## Competitive Position vs CEX

| Dimension | LlamaIndex | CEX |
|-----------|-----------|-----|
| Architecture | Index-centric RAG + document agents | 300 kinds x 12 pillars x 7 nuclei |
| Knowledge model | External document indexing | Typed internal KC library + entity_memory + learning_records |
| Quality system | None | 9.0 target, 7 gates, 5D scoring (cex_score.py) |
| Reasoning protocol | None mandatory (model decides) | Mandatory 8F (F1-F8, every task) |
| Artifact governance | None | Typed artifacts, frontmatter, quality gates, compiler |
| Multi-runtime | Python only | Claude + Codex + Gemini + Ollama |
| Decision framework | None | GDP (Guided Decision Protocol) |
| Brand awareness | None | brand_config.yaml auto-injected |
| Self-improvement | None | AutoResearch loop (cex_evolve.py) |
| MCP posture | Bidirectional (most advanced of set) | Client + server (matching LlamaIndex) |
| Pricing structure | Free OSS + pay-per-credit cloud | Self-sovereign, no per-operation fee |
| Domain coverage | P01/P10 dominant (knowledge + memory) | All 12 pillars, full coverage |
| Star count | 48.9K | Early -- seeding phase |

---

## Sources

- GitHub: https://github.com/run-llama/llama_index
- Official site: https://www.llamaindex.ai/
- Series A announcement: https://pulse2.com/llamaindex-19-million-series-a-raised-for-enterprise-grade-knowledge-agents/
- LlamaCloud launch: https://theoutpost.ai/news-story/llama-index-secures-19-m-funding-and-launches-llama-cloud-for-ai-agent-development-12811/
- MCP OSS docs: https://developers.llamaindex.ai/python/framework/module_guides/mcp/
- MCP announcement (X): https://x.com/llama_index/status/1899848532817035529
- Pricing analysis: https://www.eesel.ai/blog/llamaindex-pricing
- AI Wiki: https://aiwiki.ai/wiki/llamaindex
- 2025 newsletter: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-12-30
- LangChain vs LlamaIndex 2026: https://dev.to/lycore/langchain-vs-llamaindex-in-2026-what-we-actually-use-and-why-52eb
