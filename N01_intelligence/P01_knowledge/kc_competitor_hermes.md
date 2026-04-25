---
id: kc_competitor_hermes
kind: knowledge_card
pillar: P01
nucleus: n01
domain: competitive-intelligence
version: 1.0.0
created: 2026-04-24
quality: null
tags: [seed-intel, competitor, hermes, nous-research, gepa, self-improving, mcp]
when_to_use: "When evaluating self-improvement loop architectures; when comparing memory systems (Hermes 3-layer vs. CEX P10); when analyzing MCP bidirectional support; when user asks about fastest-growing agent frameworks of 2026"
axioms:
  - "ALWAYS benchmark CEX's /evolve loop against Hermes GEPA (ICLR 2026 Oral) -- GEPA is the only peer-reviewed self-improvement mechanism in production"
  - "ALWAYS compare 3-layer memory (Hermes: working/episodic/semantic) vs. CEX P10 (6 memory kinds: entity, episodic, procedural, prospective, working, memory_summary)"
  - "NEVER dismiss 115K stars in 60 days as hype -- Hermes has ICLR validation, full MCP bidirectional, and a soul.md personality layer that maps to CEX's nucleus_def"
  - "NEVER ignore assimilation debt -- 9 Hermes-origin kinds were absorbed into CEX (2026-04-18); monitor for upstream divergence"
tldr: "Hermes Agent by Nous Research (115K GitHub stars verified April 24, 2026; fastest-growing framework of 2026) is the only agent with a production-ready self-improvement loop (GEPA, ICLR 2026 Oral), full MCP bidirectional support, and a three-layer memory architecture -- making it the most technically sophisticated direct threat to CEX's compounding intelligence positioning."
---

# Hermes Agent (Nous Research): Competitor Intelligence Profile

> N01 Analytical Envy lens: GEPA mechanism, memory architecture, community growth -- what we must
> match or outmaneuver.

---

## Overview

Hermes Agent is an open-source, self-hosted AI agent framework from Nous Research, released
February 25, 2026. It is the only production-ready agent framework with a built-in self-improvement
loop: agents create skills from experience, improve those skills through use, and build a deepening
model of the user across sessions. The tagline is "The agent that grows with you."

| Field | Value |
|-------|-------|
| Organization | Nous Research |
| Product name | Hermes Agent |
| Tagline | "The agent that grows with you" |
| Launch date | February 25, 2026 |
| License | MIT |
| Primary language | Python (~9,200 lines core) |
| Repository | github.com/NousResearch/hermes-agent |
| Current version | v0.11.0 (as of April 2026) |
| Homepage | hermes-agent.nousresearch.com |

---

## Key Metrics

### GitHub Growth Trajectory

| Date | Stars | Notes |
|------|-------|-------|
| Feb 25, 2026 | ~0 | Launch (quiet tweet: 557 likes) |
| ~Mar 23, 2026 | ~25,000 | v0.4.0 release (200+ bug fixes, 6 messaging adapters, MCP OAuth 2.1) |
| Apr 3, 2026 | ~40,000 | OpenClaw migration tool released ("hermes claw migrate") |
| Apr 8, 2026 | ~50,000 | v0.8.0 merged (209 PRs, 82 issues) |
| Apr 16, 2026 | 57,200 | v0.10.0 release (hermesatlas.com snapshot) |
| Apr 17, 2026 | 95,600 | tokenmix.ai review date |
| Apr 2026 (reported) | 95,600-103,000 | Various sources; DEV.to article: "95.6K Stars" |
| Apr 24, 2026 | 115,038 | LIVE: gh API verified (16,863 forks, 6,791 open issues, 646 contributors) |

**Growth rate (verified April 24):** ~19,438 stars in 8 days (Apr 16-24) = ~2,430 stars/day

**Context:** Launched 3 months after OpenClaw (Feb 2026 vs Nov 2025). Reached 115K in
~8 weeks. 3,202 commits in last 30 days (107/day). OpenClaw had 363K at similar age --
but Hermes is accelerating faster and has zero CVEs vs. OpenClaw's 7+.

### Repository Stats (April 2026)

| Metric | Value |
|--------|-------|
| Stars | 115,038 (gh API, Apr 24) -- up from 57,200 (Apr 16) and 95,600 (Apr 17) |
| Forks | 16,863 (gh API, Apr 24) -- up from 7,572 (Apr 16) |
| Contributors | 646 (gh API, Apr 24) -- up from 274 (Apr 16) |
| Open issues | 6,791 (gh API, Apr 24) |
| 30d commits | 3,202 (gh API, Apr 24) |
| Latest release | v2026.4.23 (Apr 23, 2026) |
| Merged PRs | 1,400+ total |
| PRs in v0.8 alone | 209 |
| Discord community | ~4,000 builders (hermesatlas.com) |
| Ecosystem projects tracked | 80+ (hermesatlas.com) |
| Ecosystem total stars | 90,750 (hermesatlas.com) |

### Ecosystem Breakdown (80+ projects)

| Category | Count | Top project | Top project stars |
|----------|-------|-------------|-------------------|
| Skills & Registries | 17 | Anthropic Cybersecurity Skills | 4,100 |
| Memory & Context | 6 | hindsight | 8,400 |
| Multi-Agent Orchestration | 7 | mission-control | 3,900 |
| Deployment | 7 | llm-agents.nix | 967 |

---

## Technical Architecture

### Core Design Philosophy

Hermes Agent is an autonomous server-based agent, NOT an IDE plugin, NOT an API wrapper, NOT
a framework requiring a developer to write chains. It runs as a persistent server process,
receives commands via messaging platforms (6+), executes tasks autonomously, and -- uniquely --
improves its own performance over time by converting complex task experiences into permanent
skill documents.

### The Five-Step Learning Loop

```
1. RECEIVE   -- message from user or trigger (cron/webhook)
2. RETRIEVE  -- context via persistent memory (FTS5 full-text search, ~10ms latency)
3. REASON    -- LLM planning and tool invocation
4. DOCUMENT  -- outcomes as skill files (threshold: 5+ tool calls to generate skill)
5. PERSIST   -- knowledge to indexed memory
```

This loop runs automatically. After 20+ self-generated skills, repeated research tasks
complete 40% faster than a fresh agent instance (TokenMix benchmark, April 2026). The
improvement is domain-specific (skills are scoped to their originating workflow context).

### GEPA: The Self-Improvement Engine

**GEPA = Genetic-Pareto Algorithm** -- a self-improvement mechanism that uses LLMs to
analyze complete execution traces and propose targeted improvements.

| GEPA Attribute | Details |
|----------------|---------|
| Academic pedigree | ICLR 2026 Oral (top ~5% of submissions) |
| Full name | hermes-agent-self-evolution: Evolutionary self-improvement using DSPy + GEPA |
| Repository | NousResearch/hermes-agent-self-evolution |
| Mechanism | Reads execution traces to understand WHY things fail (not just THAT they failed) |
| What it optimizes | Skills + prompts + code (three artifact types) |
| Tooling | DSPy (Stanford NLP) + Genetic-Pareto optimization |
| Benchmark claim | 40% speedup on repeated research tasks after 20+ self-generated skills |

**How GEPA differs from simple caching/memoization:**
GEPA does not cache outputs. It analyzes the trace of WHY a task succeeded or failed,
identifies the structural bottleneck (wrong tool selection, insufficient context retrieval,
sub-optimal skill decomposition), and generates an improved skill variant that is then
Pareto-ranked against existing skills. Lower-ranked skills are retired.

### Three-Layer Memory Architecture

| Layer | Implementation | Scale | Description |
|-------|---------------|-------|-------------|
| L1: Session memory | Standard context management | In-context | Bounded in-prompt notes (2,200 char limit); forces deliberate consolidation |
| L2: Persistent memory | SQLite FTS5 full-text search | ~100K documents; ~10ms latency | Cross-session storage; survives agent restarts |
| L3: User model | 8 pluggable external providers | Unbounded | Automatic preference profiling; builds deepening model of user across ALL sessions |

**L3 External Memory Providers (8 supported):**
Honcho, Mem0, Hindsight, Supermemory, RetainDB, ByteRover, OpenViking, Holographic

**Memory opacity caveat:** Cannot easily export human-readable memory files (weak point
flagged by hermesatlas.com watchers as Q2 2026 concern).

### Execution Backends (6)

| Backend | Use case |
|---------|----------|
| Local | Default; runs on host machine |
| Docker | Container isolation |
| SSH | Remote server execution |
| Singularity | HPC / scientific computing |
| Modal | Serverless / cloud bursting |
| Daytona | Cloud development environments |

### Supported LLM Providers

| Provider | Models |
|----------|--------|
| Nous Portal | Hermes 4 70B, Hermes 4 405B |
| OpenRouter | 200+ models |
| Xiaomi | MiMo v2 Pro (free tier) |
| z.ai / GLM | GLM series |
| Kimi / Moonshot | Kimi series |
| MiniMax | M2.7 |
| Hugging Face | Inference API |
| OpenAI | Direct |
| Custom endpoints | Any OpenAI-compatible endpoint |
| TokenMix.ai | 150+ models |

Multi-model routing: cheap models for routine tasks, premium for complex reasoning.
Community reports 40-60% cost reduction via routing (TokenMix benchmark).

### Technical Specs

| Spec | Value |
|------|-------|
| Core codebase size | ~9,200 lines (Python) |
| LLM provider support | 20+ |
| Bundled skills (v0.10.0) | 118 (96 bundled + 22 optional) |
| Skill categories | 26+ |
| Messaging integrations | 6 (Telegram, Discord, Slack, WhatsApp, Signal, CLI) |
| Supported runtimes | Linux, macOS, WSL2, Android (Termux), Docker, SSH, Daytona, Modal |
| Install method | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` |
| Config method | `hermes setup` |

---

## Community Strategy

### Launch Strategy: Quiet + Algorithmic Growth

Nous Research did NOT run a marketing campaign. The February 25, 2026 launch was a simple
tweet that got 557 likes -- modest for a 95K-star project. Growth came from:

1. **Algorithmic GitHub trending:** Hermes appeared on GitHub Trending immediately and stayed
   there for weeks due to commit velocity (208 PRs in v0.8 alone in 8 days).

2. **OpenClaw migration opportunity (April 3):** When Anthropic blocked OpenClaw's access,
   Nous Research released a humorous migration tool: `hermes claw migrate`. This was
   deliberately timed to capture OpenClaw refugees. Generated massive earned media.

3. **Weekly release cadence:** v0.4.0 (Mar 23) -> v0.6.0 -> v0.8.0 (Apr 8) -> v0.10.0 (Apr 16).
   Each release with 100+ PRs signals to the community that the project is actively maintained.
   Release velocity generates repeat GitHub trending appearances.

4. **Strategic partnerships (April 2026):**
   - MiniMax: M2.7 model integration (free for Hermes users)
   - Xiaomi: free MiMo v2 Pro API credits for Hermes users
   - Vercel Labs: joint deployment integration
   - Black Forest Labs: image generation integration

5. **Hackathon activation:** Nous Research Hackathon 2026 resulted in 80+ ecosystem projects.
   Notable: gladiator (runtimenoteslabs): "Two zero-human AI companies battle for GitHub stars
   using Hermes Agent + Paperclip" -- community-built viral projects.

6. **Paradigm Research Lab funding announcement (April 11):** Paradigm + a16z funding
   announcement generated another star spike and press coverage.

### Community Channels

| Channel | Size / Activity |
|---------|-----------------|
| Discord | ~4,000 builders (hermesatlas.com, April 2026) |
| GitHub contributors | 274+ |
| Ecosystem maintainers | 80+ tracked projects |
| awesome-hermes-agent | curated list (0xNyk/awesome-hermes-agent) |
| DataCamp tutorial | "Setup and Tutorial Guide" (official) |
| DEV.to coverage | Multiple in-depth review articles |
| tokenmix.ai | Benchmark coverage + review articles |
| Bitcoin.com News | Mainstream press coverage |

### Top Community Contributors (v0.8 release window)

| Handle | Contribution type |
|--------|------------------|
| @SHL0MS | Core; high PR volume |
| @alt-glitch | Features |
| @benbarclay | Integrations |
| @CharlieKerfoot | Skills |
| @WAXLYY | Memory |
| Teknium | Co-founder; 179 PRs (v0.8) |
| 14 distinct contributors | PRs merged in single release window |

---

## Distribution Channels

| Channel | Details |
|---------|---------|
| GitHub (primary) | github.com/NousResearch/hermes-agent |
| Install script | hermes-agent.nousresearch.com/install.sh |
| Nous Portal | Hosted model access (Hermes 4 70B / 405B) |
| DataCamp tutorial | Structured onboarding content |
| Hermes Atlas | hermesatlas.com -- ecosystem tracker and reports |
| hermesatlas.com reports | Monthly state-of-hermes reports |
| OpenRouter | Model routing marketplace |
| TokenMix.ai | Benchmark review + model routing partner |
| awesome-hermes-agent | Community curation |

---

## MCP Support

Hermes Agent has bidirectional, native, OAuth-secured MCP support -- the most complete
MCP implementation among the three competitors analyzed.

| Dimension | Details |
|-----------|---------|
| MCP client (as tool consumer) | YES -- connect to any MCP server for extended tool capabilities |
| MCP server (as tool provider) | YES -- Hermes can ITSELF act as MCP server (v0.6.0+) |
| OAuth support | YES -- MCP OAuth 2.1 PKCE flow (v0.4.0) |
| Management CLI | YES -- CLI for MCP server management |
| Status | Core feature; bidirectional by v0.6.0 |
| CEX comparison | CEX N07 is MCP gateway (client-only); Hermes is bidirectional |

**Hermes MCP as server (v0.6.0+):** Hermes exposes its conversation interface to other MCP
clients. This means other AI tools (Claude.ai, cursor, etc.) can use Hermes as a tool --
the agent becomes a first-class MCP tool in other workflows. This is a significant
architectural advantage over OpenClaw (which uses MCP only as client) and CEX (which uses
N07 as gateway).

---

## Pricing Model

| Tier | Cost | Notes |
|------|------|-------|
| Framework (MIT) | Free | Zero license cost |
| Infrastructure (optional VPS) | $5-10/month | Not required for local use |
| LLM API (personal assistant, 30 calls/day) | $5-30/month | API cost only |
| LLM API (daily research, 100 calls/day) | $80-150/month | -- |
| LLM API (team support, 500 calls/day) | $200-400/month | -- |
| LLM API (heavy workflows, 2K calls/day) | $800-1,500/month | -- |
| Nous Portal | Subscription (details not published) | Access to Hermes 4 70B/405B |
| Vector DB (scaling >100K memories) | $0-50/month | Optional; only needed at scale |

Funding (April 11, 2026): Paradigm + a16z led round. Valuation not disclosed. Promotional
code AGENTHERMES01 for free tier access during launch period.

**No enterprise tier announced as of April 2026.** Pure MIT + API-cost model.

---

## Strengths

| Strength | Assessment |
|----------|------------|
| GEPA self-improvement | ONLY production-ready agent framework with academic-grade (ICLR 2026 Oral) self-improvement |
| Three-layer memory | Most sophisticated memory architecture in the field; L3 user model is a genuine moat |
| Bidirectional MCP | Both client AND server; more flexible than any competitor |
| Security record | Zero agent-specific CVEs (vs. OpenClaw's 10+); curated 118-skill model vs. 13K unvetted |
| Release velocity | 209 PRs in 8 days (v0.8); demonstrates operational excellence |
| Paradigm + a16z backing | Tier-1 crypto/tech investors signal long-term runway |
| MIT license + no enterprise tier | Zero friction adoption |
| Nous Research model portfolio | Hermes 4 70B/405B available via Nous Portal = end-to-end |
| Community density | 274+ contributors in 2 months = faster than LangChain's early growth |
| Cost efficiency | Multi-model routing cuts LLM bills 40-60% |
| OpenClaw migration tool | Deliberately positioned to capture OpenClaw refugees |
| Strategic partnerships (MiniMax, Xiaomi, Vercel, Black Forest) | Distribution reach without direct marketing budget |

---

## Weaknesses

| Weakness | CEX Exploitability |
|----------|--------------------|
| Self-learning disabled by default (requires manual enablement) | CEX F3b PERSIST + learning_record automatic; no opt-in required |
| Not a code-generation tool (not competing in Cursor/Copilot space) | CEX N05 operations nucleus handles code/test/deploy |
| v0.x API instability (only 2 months old) | CEX versioned artifacts with frontmatter contracts; stable across versions |
| Memory opacity: cannot export human-readable memory files | CEX artifacts are human-readable .md files; transparent knowledge graph |
| Auto-generated skill quality varies (over-generalization on complex multi-phase tasks) | CEX 8F F7 GOVERN: quality gate on every artifact including skills |
| Local model throughput (1-2 tokens/s vs 45 tokens/s native) | CEX routes to appropriate runtime per task |
| 6 messaging integrations (vs OpenClaw's 24+) | CEX does not compete on messaging; N07 dispatch is CLI/API-native |
| No enterprise features (no SSO, no audit trail, no SOC 2) | CEX F8 COLLABORATE: git commit + signal = audit trail built-in |
| No typed knowledge system | CEX 300 kinds x 12 pillars = typed; Hermes skills are untyped Python files |
| No multi-nucleus orchestration (single agent, not 7-nucleus grid) | CEX N07 orchestrates 6 parallel nuclei |
| Ecosystem still maturing (80 projects vs LangChain's 200+ integrations) | CEX's 300 builders compete on depth, not breadth |
| No commercial observability layer (no LangSmith equivalent) | CEX cex_score.py + cex_quality_monitor.py + F7 = built-in |

---

## Key People

| Person | Role | Notes |
|--------|------|-------|
| Teknium | Co-founder; lead contributor | 179 PRs in v0.8 alone; Hermes and Nomos model family creator |
| Jeffrey Quesnelle | Co-founder / CEO | Focus: open-source model development and reinforcement learning |
| @SHL0MS | Core contributor | High PR volume across multiple releases |
| @alt-glitch | Feature contributor | -- |
| @benbarclay | Integration contributor | -- |
| @CharlieKerfoot | Skills contributor | -- |
| @WAXLYY | Memory contributor | -- |

### Nous Research Portfolio (context)

Nous Research produces the Hermes, Nomos, and Psyche model families in addition to Hermes Agent.
This means Hermes Agent has a first-party model provider (Nous Portal) -- giving them an
integrated stack that no other OSS agent framework has.

### Investors (April 11, 2026 round)

| Investor | Type | Known for |
|----------|------|-----------|
| Paradigm | Lead | Crypto-native tech fund; early Coinbase, FTX (pre-collapse), Uniswap |
| a16z (Andreessen Horowitz) | Co-lead | Early OpenAI, GitHub, Coinbase; tier-1 VC |

---

## CEX vs Hermes Agent: Strategic Gap Analysis

| Dimension | Hermes Agent | CEX |
|-----------|-------------|-----|
| Self-improvement | GEPA (ICLR 2026 Oral); 40% speedup | learning_record + memory_update + cex_evolve.py |
| Memory architecture | 3-layer (bounded session + SQLite + 8 external L3 providers) | entity_memory + knowledge_index + learning_record |
| MCP support | Bidirectional (client + server) | N07 MCP gateway (client; Phase 0 preflight) |
| Knowledge system | Untyped Python skill files | 300 typed kinds x 12 pillars x 8F |
| Quality system | None (no quality gates on skills) | F7 GOVERN: 9.0 target; 7 HARD gates; peer review |
| Multi-nucleus | None (single agent) | 8-nucleus grid (N01-N07 + N00) |
| Orchestration | None | N07 orchestrator + dispatch.sh + signal protocol |
| Typed artifacts | No | Yes (frontmatter + schema + kind registry) |
| Human-in-loop | No (autonomous only) | GDP (Guided Decision Protocol) = co-pilot mode |
| Audit trail | None | F8: git commit + signal + compile |
| Sin lens | None | 7 sin lenses (domain-specialized) |
| Stars | 57K-103K | Early stage |
| Funding | Paradigm + a16z | Self-funded / early stage |

**Where Hermes wins vs CEX today:**
1. GEPA is academically validated (ICLR 2026 Oral). CEX's learning loop is operationally sound
   but lacks published benchmarks.
2. Bidirectional MCP (Hermes acts as MCP server) -- CEX is client-only via N07.
3. Star count and community momentum -- 2-month project at 95K stars is extraordinary.

**Where CEX wins vs Hermes today:**
1. Typed infrastructure: 300 kinds vs untyped Python skills.
2. Quality gates: F7 GOVERN + peer review vs no quality enforcement.
3. Multi-nucleus orchestration: N07 grid vs single-agent.
4. GDP (co-pilot mode): subjective decisions resolved with user before dispatch.
5. 4-runtime support: Claude/Codex/Gemini/Ollama vs single-framework.
6. Human-readable, transparent artifact graph vs opaque SQLite memory.

**Q2 2026 watch points (hermesatlas.com):**
1. Skill marketplace maturity (will it challenge OpenClaw's 13K-skill moat?)
2. Enterprise multi-instance story (per-client isolation not yet built)
3. Publishable benchmarks for GEPA self-improvement
4. Nous Portal subscription sustainability
5. Core feature consolidation (v0.x to v1.0 API stability)

**CEX response priority:** Publish benchmark comparison of CEX learning_record improvement
vs Hermes GEPA. Develop bidirectional MCP server capability for N07. Build out typed skill
registry as competitive counter to Hermes skill ecosystem.

---

## Sources Used

- [Hermes Agent -- The Agent That Grows With You | Nous Research](https://hermes-agent.nousresearch.com/)
- [Hermes Agent Review: 95.6K Stars, Self-Improving AI Agent (2026) - TokenMix Blog](https://tokenmix.ai/blog/hermes-agent-review-self-improving-open-source-2026)
- [Hermes Agent Review: 95.6K Stars (April 2026) - DEV Community](https://dev.to/tokenmixai/hermes-agent-review-956k-stars-self-improving-ai-agent-april-2026-11le)
- [The State of Hermes Agent -- April 2026 | Hermes Atlas](https://hermesatlas.com/reports/state-of-hermes-april-2026)
- [GitHub - NousResearch/hermes-agent-self-evolution (GEPA)](https://github.com/NousResearch/hermes-agent-self-evolution)
- [GitHub - 0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)
- [Hermes Agent 2026: First Production-Ready Self-Improving Open-Source AI Agent | Innobu](https://www.innobu.com/en/articles/hermes-agent-self-improvement-open-source-2026.html)
- [GitHub Trending Weekly 2026-04-22 | Shareuhack](https://www.shareuhack.com/en/posts/github-trending-weekly-2026-04-22)
- [Nous Research Hermes Agent: Setup and Tutorial Guide | DataCamp](https://www.datacamp.com/tutorial/hermes-agent)
- [Hermes Agent 2026 Release Tracker | Releasebot](https://releasebot.io/updates/nousresearch/hermes-agent)
- [Earn 40,000 Stars in a Frenzy (36kr English)](https://eu.36kr.com/en/p/3759493153653253)
