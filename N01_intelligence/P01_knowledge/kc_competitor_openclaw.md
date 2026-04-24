---
id: kc_competitor_openclaw
kind: knowledge_card
pillar: P01
nucleus: n01
domain: competitive-intelligence
version: 1.0.0
created: 2026-04-24
quality: null
tags: [seed-intel, competitor, openclaw, agent-framework, mcp, clawHub]
tldr: "OpenClaw is a viral MIT-licensed self-hosted AI agent gateway (335K+ stars in 60 days) built by Peter Steinberger, now stewarded by a non-profit after its creator joined OpenAI; its 13K+ ClawHub skills ecosystem and MCP-native architecture are both its greatest strength and critical security liability."
---

# OpenClaw: Competitor Intelligence Profile

> N01 Analytical Envy lens: what OpenClaw does that we do NOT, what we do that they CANNOT.

---

## Overview

OpenClaw is an open-source, self-hosted AI agent gateway that connects large language models
(Claude, GPT-4o, Gemini, Llama, local Ollama models) to messaging platforms (WhatsApp, Telegram,
Slack, Discord, Signal, Email) and executes autonomous tasks through a community-built skill
ecosystem called ClawHub.

| Field | Value |
|-------|-------|
| Original name | Clawdbot (Nov 2025) -> Moltbot (Jan 27, 2026) -> OpenClaw (Jan 30, 2026) |
| Creator | Peter Steinberger (Austrian; b. 1986; founder/former CEO of PSPDFKit) |
| Launch date | November 24, 2025 (as Clawdbot) |
| Repository | github.com/openclaw/openclaw |
| License | MIT |
| Primary language | TypeScript + Swift |
| Runtime | Node.js 24+ |
| Foundation status | Non-profit foundation (post-Steinberger departure, Feb 2026) |
| OpenAI backing | OpenAI committed to contribute to and fund the open-source project |

### Origin Story

Steinberger built OpenClaw as a personal automation tool while running PSPDFKit (a PDF SDK
company he founded in 2010 and ran for 13 years). The name changed twice: first from Clawdbot to
Moltbot after Anthropic filed trademark complaints for similarity to "Claude"; then again to OpenClaw
because Steinberger felt "Moltbot never quite rolled off the tongue." On February 14-15, 2026,
OpenAI CEO Sam Altman publicly announced Steinberger was joining OpenAI to "drive the next
generation of personal agents." Altman described him as a "genius with a lot of amazing ideas about
the future of very smart agents interacting with each other." OpenClaw will be maintained through a
non-profit foundation with OpenAI funding support.

---

## Key Metrics

### GitHub Growth Trajectory (record-breaking)

| Date | Stars | Notes |
|------|-------|-------|
| Nov 24, 2025 | ~1K | Launch as Clawdbot |
| Nov 2025 | ~5K | Organic growth phase |
| Jan 30, 2026 | 34,160 | Rebrand to OpenClaw |
| Feb 2, 2026 | 60,000 | Viral acceleration |
| Feb 15, 2026 | 190,000 | Steinberger joins OpenAI announced |
| Mar 2, 2026 | 247,000 | Wikipedia snapshot |
| Mar 3, 2026 | 250,829 | Surpassed React (10-year record) |
| Apr 2026 | 335,000+ | Current (per skywork.ai analysis) |

**Milestone:** Broke React's record as the most-starred GitHub project in ~60 days.
OpenClaw is the fastest-growing open-source project in GitHub history by star acceleration.

### Repository Stats (March 2026 snapshot)

| Metric | Value |
|--------|-------|
| Stars | 335,000+ |
| Forks | 47,700+ |
| Codebase size | ~124,000 lines of code |
| ClawHub skills | 13,729+ |
| Public exposed instances | 135,000+ (security finding) |

### Community Demographics

| Segment | Share |
|---------|-------|
| Developers | 55% |
| Data scientists | 20% |
| IT ops / security | 15% |
| Enthusiasts / non-technical | 10% |

### Common Use Cases (% of deployments)

| Use case | Adoption |
|----------|----------|
| Morning briefings / news digests | 85% |
| Email triage and reply drafting | 72% |
| Calendar sync and scheduling | 65% |
| Code review and PR assistance | 45% |

---

## Technical Architecture

OpenClaw is a local-first autonomous agent runtime, not a framework or SDK. It runs as a persistent
server process on the user's machine or VPS and receives commands via messaging platforms.

### Core Components

| Component | Role |
|-----------|------|
| Local-first gateway | Routes LLM calls and tool invocations; processes tasks autonomously |
| Multi-channel inbox | Unified message bus across WhatsApp, Telegram, Slack, Discord (24+ integrations) |
| ClawHub registry | Skill marketplace; each skill is an MCP server |
| Live Canvas | Real-time visual task execution display |
| Skill directories | Three-scope system: bundled / global / workspace-specific (workspace takes precedence) |

### Skill Architecture

- Skills stored as directories with metadata (YAML) files
- Installable via ClawHub one-click or manual directory placement
- Each skill is an MCP server (see MCP Support below)
- 13,729+ community-submitted skills as of Apr 2026
- Security finding: ~20% of ClawHub skills contained malicious payloads or excessive permissions
  (Cisco AI Security Team, Jan 28, 2026)

### Infrastructure Requirements

| Tier | Spec | Monthly cost |
|------|------|-------------|
| Minimum | 2 vCPUs, 8GB RAM | ~$8 (budget VPS + API costs) |
| Standard | 4 vCPUs, 16GB RAM | ~$25 |
| Power user | 8+ vCPUs, 32GB+ RAM | ~$60 |

### Known Critical Vulnerability

- CVE-2026-25253 (CVSS 8.8): Remote Code Execution via unvalidated skill payloads
- 9 additional CVEs disclosed in 4 days (March 2026) -- highest CVE density of any agent framework
- Root cause: TypeScript gateway trusts skill metadata without sandbox isolation
- Default port 0.0.0.0:18789 exposed to network without auth by default
- Chinese government (March 2026): barred state enterprises from OpenClaw due to data exfiltration
  risks, unauthorized deletion, and energy consumption concerns

---

## Community Strategy

OpenClaw's viral growth was NOT marketing-driven. It was driven by three structural factors:

### Factor 1: Perfect timing in the AI agent hype cycle

Launched November 2025 during peak consumer AI interest. WhatsApp + Telegram integration
resonated with non-US users (where Signal/WhatsApp dominate). The promise: "AI that actually
does things" vs chatbots that just chat.

### Factor 2: MIT license + anti-SaaS narrative

Steinberger positioned OpenClaw explicitly as a way to "bypass expensive SaaS subscriptions."
MIT license meant no legal friction for companies, individuals, or community forks.

### Factor 3: Founder visibility + Sam Altman signal amplification

Steinberger's TED 2026 talk ("The lobster is loose, and it's not going back") generated press
coverage. Sam Altman's public tweet praising Steinberger as a "genius" triggered a second wave of
virality in February 2026. Anthropic trademark threat became PR instead of a blocker.

### Channels

| Channel | Role |
|---------|------|
| GitHub trending | Primary viral vector (Nov 2025) |
| Hacker News | Early tech adopter buzz |
| Twitter/X (Sam Altman endorsement) | Second virality wave (Feb 2026) |
| TED 2026 (Steinberger talk) | Mainstream credibility |
| Chinese developer communities | WeChat / domestic super-app adaptation |
| third-party tutorial sites | openclawlaunch.com, learnopenclaw.com, openclawdesktop.com |
| Fortune / CNBC / TechCrunch coverage | PR amplification of Steinberger-OpenAI move |

---

## Distribution Channels

| Channel | Details |
|---------|---------|
| GitHub (primary) | github.com/openclaw/openclaw |
| ClawHub marketplace | skills.openclaw.io (13,729+ skills) |
| Docker Hub | Official container images |
| Tutorial ecosystem | 3+ dedicated tutorial domains |
| openclawlaunch.com | Third-party install+skills portal |
| Tencent / Z.ai | Chinese adaptations for WeChat, DeepSeek |
| Enterprise forks | NanoClaw (security), ZeroClaw (performance), Moltis (multi-tenant) |

### Notable Forks and Spin-offs

| Fork | Stars | Differentiation |
|------|-------|-----------------|
| NanoClaw | 21,500 | Security-first; mandatory Docker/Apple container isolation |
| ZeroClaw | 26,200 | Rust rewrite; 3.4MB binary; <10ms boot |
| Nanobot | 26,800 | Python implementation; 4,000 lines |
| Moltis | 11,600 | Enterprise multi-tenant architecture |
| ZeroClaw (alt) | -- | Rebrand test; merged into NanoClaw |
| Taskade Genesis | (commercial) | Cloud SaaS version; $6/mo; SOC 2; no-code |

---

## MCP Support

OpenClaw has NATIVE, DEEP MCP integration -- it is one of the largest MCP-compatible
platforms in existence.

| Dimension | Details |
|-----------|---------|
| Architecture | Every ClawHub skill IS an MCP server |
| Protocol support | Full MCP spec (adopted by Anthropic, OpenAI, Google DeepMind, Linux Foundation) |
| MCP server count | 13,000+ (via ClawHub) |
| Management tool | McPorter -- visual MCP browser, one-click install, no CLI needed |
| Third-party integration | freema/openclaw-mcp: secure bridge between Claude.ai and self-hosted OpenClaw |
| Auth | MCP connections support OAuth2 |
| Positioning | OpenClaw = "USB-C for AI agents" narrative around MCP |

MCP is OpenClaw's structural moat: 13K MCP skills built by community creates a network
effect that is extremely difficult to replicate. However, the same openness creates security
exposure (see CVEs above).

---

## Pricing Model

| Tier | Cost | Notes |
|------|------|-------|
| OpenClaw software | Free (MIT) | Zero license cost |
| Infrastructure (budget) | ~$8/month | Cheap VPS + API costs |
| Infrastructure (standard) | ~$25/month | Mid-tier VPS |
| Infrastructure (power user) | ~$60/month | 8-core VPS + heavy API usage |
| Taskade Genesis (SaaS fork) | $6/month | Cloud-hosted, no-code, SOC 2 |
| LLM API costs | Variable | External cost; not included above |

Revenue model: OpenClaw itself is non-commercial open-source. The foundation may eventually
pursue commercial support or certification programs, but no announcement as of April 2026.
OpenAI funding provides runway for the foundation.

---

## Strengths

| Strength | Assessment |
|----------|------------|
| GitHub star count | 335K+ = unmatched social proof; de facto reference for "AI agent" |
| Skill ecosystem (13K+) | Network effect moat; most any integration need is covered |
| MCP-native architecture | First-mover in MCP ecosystem; every skill = MCP server |
| Multi-channel breadth | 24+ messaging integrations (WhatsApp, Telegram, Slack, Discord, Signal) |
| MIT license | No restrictions; enables enterprise adoption, forks, commercial wrappers |
| OpenAI foundation backing | Long-term sustainability guarantee; marketing credibility |
| Privacy-first / self-hosted | Resonates with developer and enterprise security concerns |
| Community inertia | 135K+ live instances; ecosystem creates lock-in via skill investment |
| Founder narrative | TED talk + Sam Altman endorsement = mainstream credibility |

---

## Weaknesses

| Weakness | CEX Exploitability |
|----------|--------------------|
| Critical security record: 10 CVEs in March 2026 alone | CEX positions as enterprise-grade, governed, audited |
| Malicious skill problem: ~20% of ClawHub skills compromised | CEX typed knowledge system enforces artifact quality gates |
| No quality gates on community contributions | CEX 8F pipeline + H01-H07 HARD gates = quality insurance |
| Non-technical users cannot self-protect (2 vCPU minimum config complexity) | CEX abstracts complexity behind nucleus dispatch |
| Founder-dependency risk: Steinberger at OpenAI may reprioritize | CEX has 7-nucleus architecture not dependent on single founder |
| No typed knowledge system -- skills are unstructured scripts | CEX is a TYPED infrastructure: 300 kinds, 12 pillars, schemas |
| No compounding intelligence: each agent instance starts fresh | CEX learning_record + memory_update = knowledge compounds |
| No multi-runtime governance (N07 pattern absent) | CEX N07 orchestrates across Claude/Codex/Gemini/Ollama |
| Chinese government ban signals trust problem | CEX audit trail (F8) + governed dispatch = compliance-ready |
| Codebase: 124K LoC TypeScript = high maintenance overhead | CEX modular Python; cex_sdk; 54 system tests |

---

## Key People

| Person | Role | Social |
|--------|------|--------|
| Peter Steinberger | Creator / Founder (now at OpenAI) | steipete.me; @steipete |
| Sam Altman | OpenAI CEO; public OpenClaw champion | @sama (tweet: 2023150230905159801) |
| Shadow (pseudonym) | Core maintainer; issued security warnings | GitHub: @shadow-opensrc |
| Matt Schlicht | Creator of Moltbook (OpenClaw social network for agents) | LinkedIn: matt-schlicht |

### Foundation Governance (post-Steinberger)

OpenClaw is governed by an unnamed non-profit foundation as of February 2026. Membership and
governance structure not yet publicly documented. OpenAI has pledged contributions.

---

## CEX vs OpenClaw: Strategic Gap Analysis

| Dimension | OpenClaw | CEX |
|-----------|----------|-----|
| Architecture | Monolithic TypeScript gateway | Modular 8-nucleus Python system |
| Knowledge system | Untyped scripts (skills) | 300 typed kinds x 12 pillars |
| Quality enforcement | None (community free-for-all) | 8F pipeline + H01-H07 gates + 9.0 target |
| Multi-runtime | Single (Node.js) | 4 runtimes (Claude/Codex/Gemini/Ollama) |
| Security model | Reactive (CVE-disclosed) | Proactive (governance layer + quality gate) |
| Enterprise readiness | Low (security CVEs, no SOC 2) | High (audit trail, governed dispatch) |
| Self-improvement | None (starts fresh every session) | learning_record + memory_update + evolve loop |
| Orchestration | None (single-agent) | N07 + 8-nucleus grid dispatch |
| Stars | 335K | Early stage |
| MCP | First-class (13K servers) | Supported (via N07 MCP gateway) |

**CEX opportunity:** Typed, governed, compounding knowledge architecture vs OpenClaw's viral-but-insecure
untyped skill pile. Enterprise buyers who were burned by OpenClaw CVEs will seek governance alternatives.

---

## Sources Used

- [Comprehensive Analysis: OpenClaw GitHub Stars Count February 2026 & Ecosystem](https://skywork.ai/skypage/en/openclaw-github-stars-ecosystem/2038550906443481088)
- [OpenClaw creator Peter Steinberger joins OpenAI | TechCrunch](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/)
- [OpenClaw - Wikipedia](https://en.wikipedia.org/wiki/OpenClaw)
- [OpenClaw + MCP -- Model Context Protocol Skills Guide](https://openclawlaunch.com/guides/openclaw-mcp)
- [McPorter -- Install & Manage MCP Servers for OpenClaw](https://openclawlaunch.com/guides/openclaw-mcporter)
- [Skills & ClawHub -- Extending OpenClaw](https://learnopenclaw.com/core-concepts/skills)
- [Sam Altman on X (Steinberger announcement)](https://x.com/sama/status/2023150230905159801)
- [Fortune: Who is OpenClaw creator Peter Steinberger?](https://fortune.com/2026/02/19/openclaw-who-is-peter-steinberger-openai-sam-altman-anthropic-moltbook/)
