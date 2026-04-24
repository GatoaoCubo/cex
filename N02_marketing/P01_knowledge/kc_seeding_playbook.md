---
id: kc_seeding_playbook
kind: knowledge_card
pillar: P01
nucleus: n02
domain: community-seeding
version: 1.0.0
created: 2026-04-24
quality: null
tags: [seed-intel, playbook, community, growth]
tldr: "Step-by-step playbook for seeding CEX into AI agent communities -- which channels, what content, when, and what NOT to do"
---

# Community Seeding Playbook: CEX Open-Source Launch

## 1. Executive Summary

This playbook provides the week-by-week tactical plan for launching CEX into the open-source AI agent community, covering 88+ global channels and 123 Brazilian channels. It synthesizes data from OpenClaw (9K to 335K stars in 60 days), Hermes Agent (0 to 95K in 7 weeks), CrewAI (0 to 49.8K via organic content), and LangChain (0 to 124K via education partnerships) to extract what is replicable at zero budget. Expected outcome: 500-2,000 GitHub stars in 12 weeks, Discord community of 200+ members, and pipeline of 3-5 newsletter features.

---

## 2. Lessons from Competitors (Extracted from Case Studies)

| Competitor | What Worked | What Failed | Replicable for CEX? |
|------------|-------------|-------------|---------------------|
| **OpenClaw** (335K stars, 60 days) | "Replace $20/mo tools" economic framing; MIT license + self-hosting trust signal; multi-provider architecture positioning; ClawHub marketplace (13,729 skills) creating ecosystem lock-in | 20% of ClawHub skills contained malicious payloads -- no vetting infrastructure; press-dependent J-curve that plateaued without new catalysts | Economic framing: YES. Marketplace: YES (CEX kind registry). MIT: YES. Trademark drama: NO. Founder celebrity ($800M exit): NO |
| **Hermes Agent** (95K stars, 7 weeks) | Release cadence as events (v0.8.0 = +6,400 stars in 24h); self-improving architecture narrative ("handles ambiguous goals"); multi-platform community (Discord/Telegram/Slack/Weibo); community infrastructure built BEFORE launch | Dependent on Nous Research pre-existing Web3 community (10K+ members mobilized instantly) | Release cadence: YES. Self-improvement narrative: YES. Multi-platform presence: YES. Pre-existing org community: NO |
| **CrewAI** (49.8K stars, 18 months) | Intuitive role/goal/backstory API -- any dev can demo in 15 min; social proof escalation ladder (4K -> "Fortune 500" -> "$18M" -> "100K certified"); certification program creating investment lock-in; 40% faster time-to-prototype claim | Enterprise claims require actual enterprise adoption first; $18M funding press cannot be manufactured | Easy-to-demo API: YES (CEX `/build`). Social proof ladder: YES (plan milestones ahead). Certification: YES (8F pipeline as curriculum). Funding press: NO |
| **LangChain** (124K stars, 24 months) | Andrew Ng / DeepLearning.AI course partnership -- institutional distribution to millions; 700+ integrations = 700 natural referral communities; founder personally responded to GitHub issues in first 6 months; weekly webinars as community heartbeat | Complex API required expert tutorials, limiting community content creation; over-reliance on one distribution deal (Andrew Ng) | Founder issue responses: YES. Weekly webinars: YES. Integration network: YES (slow). Institutional distribution deal: PARTIAL (requires relationship). Content complexity: AVOID |

### Key Replicable Patterns (Zero Budget Required)

| Pattern | Source | CEX Application |
|---------|--------|-----------------|
| Economic displacement framing | OpenClaw | "Replace 3-5 paid AI tools with one self-hosted brain" |
| Release cadence as events | Hermes Agent | Every version bump = announcement + demo + community post |
| "15-minute first demo" path | CrewAI | `/build landing_page` produces artifact in under 5 minutes |
| Social proof escalation ladder | CrewAI | Plan milestones: 100 stars -> 500 -> 1K -> 5K (each triggers press angle) |
| Founder issue response | LangChain | Respond to every GitHub issue within 4 hours for first 6 months |
| Community infrastructure pre-launch | Hermes Agent | Discord + README + demo GIF ready BEFORE first public post |

### Non-Replicable Patterns (Do Not Plan For)

| Pattern | Why Not | Alternative |
|---------|---------|-------------|
| Founder celebrity (OpenClaw's $800M exit) | Requires prior company exit | Build credibility through artifact quality, not biography |
| Trademark drama press cycle | Cannot manufacture involuntary events | Create your own press events via release cadence |
| Pre-existing org community (Hermes/Nous Research) | Requires years of prior reputation | Build community from scratch, seed into existing communities |
| $18M+ VC funding press wave | Funding-dependent | Substitute with production metrics ("X artifacts compiled by community") |
| Andrew Ng partnership | Relationship-dependent | Pitch smaller newsletters first (console.dev, TLDR.tech, Latent.Space) |

---

## 3. Anti-Patterns (CRITICAL -- What NOT to Do)

### Communities That Ban Self-Promotion

| Community | Rule | Consequence of Violation | Correct Approach |
|-----------|------|--------------------------|------------------|
| r/MachineLearning (3M members) | No promotional posts; self-promotion restricted to monthly thread | Post removed + temporary ban; repeat = permanent ban | Contribute technical comments for 2-4 weeks before posting; use monthly self-promotion thread only |
| r/LocalLLaMA (694K members) | No low-effort promotion; requires substantive technical content | Downvoted to oblivion + mod removal | Post benchmarks, architecture analysis, or comparison data -- not "check out my framework" |
| r/ClaudeAI (747K members) | No spam; community expects genuine Claude-related content | Post removed if perceived as advertising | Share CEX as a tool that enhances Claude usage, not as a standalone product pitch |
| Hacker News | No astroturfing (coordinated upvotes); no duplicate submissions | Shadowban on account + domain | ONE Show HN post per major release; respond to every comment; never ask friends to upvote |
| LangChain Discord (30K members) | No competitive framework promotion in #general | Message deleted + possible kick | Only mention CEX when directly answering a user's question about multi-agent orchestration |
| Data Hackers Slack (41K members, BR) | Community rules require relevant, non-spammy content | Kicked from workspace | Post in #show-e-tell or #ferramentas; provide genuine value, not sales pitch |
| MLOps Community Slack (27.9K members) | Professional tone; no product spam | Removed from channel | Contribute to discussions about ML governance, quality gating -- mention CEX only when directly relevant |

### Tactics That Backfire

| Anti-Pattern | Why It Fails | Real Example | What To Do Instead |
|-------------|-------------|-------------|-------------------|
| Cross-posting the same text to 10+ communities | Communities detect copy-paste; moderators coordinate across platforms | Generic "we launched X" posts on Reddit/Discord/HN simultaneously get flagged | Write platform-native content: Reddit gets technical depth, Twitter gets thread format, Discord gets conversation |
| "Star and share!" calls to action | Developer audiences react negatively to explicit star solicitation | Repos with "please star!" in README get mocked on r/programming | Let the product earn stars; CTA should be "try it" not "star it" |
| Bot-generated stars | 4.5M fake stars detected by GitHub (Socket Inc/CMU study, 2025); GitHub's fraud detection can suppress real discovery | Framework X gained 10K stars overnight; all from accounts with no avatar, no repos, no followers -- algorithmic suppression followed | Real stars compound: they fork, contribute, report issues, create tutorials |
| Posting without a polished README | Developers decide in 3 seconds whether to explore further | Repos with no demo GIF, no quick start, no value prop get 60%+ bounce rate | README must have: 1-sentence value prop, demo GIF, 3-line quick start, badge wall |
| Arguing with critics | Public arguments amplify negative coverage and signal insecurity | Framework maintainers defending against "why not just use LangChain" comments created viral negative threads | Acknowledge valid criticism, provide data, move on. "That's fair feedback -- here's what we optimize for differently:" |
| Claiming features you do not have yet | Developer communities verify claims within hours | Frameworks claiming "production-ready" with no test coverage get exposed on HN | Only claim what the repo demonstrates. "300 kinds" is verifiable. "Enterprise-ready" requires proof |
| Spamming WhatsApp/Telegram groups (BR) | BR communities are tight-knit; spam is identified instantly and gets you banned permanently | Automated messages to 20+ Telegram groups = blacklisted across the ecosystem | Engage in 3-5 groups organically for 2+ weeks before sharing anything CEX-related |

### The Credibility Window

Every community gives a new member approximately 3-5 interactions before judging them. This window determines whether you are seen as a contributor or a spammer.

| Interaction # | What To Do | What NOT To Do |
|---------------|-----------|----------------|
| 1-2 | Answer someone else's question; share a useful resource (not yours) | Post about your project |
| 3-4 | Engage in a discussion; offer technical insight | Drop a link to your repo |
| 5+ | Mention CEX naturally when it answers someone's specific question | "Check out CEX" as a standalone message |

---

## 4. Channel Priority Matrix

### Tier 1: Highest CEX Fit (Weeks 1-4)

| # | Channel | Type | Size | CEX Fit | Entry Difficulty | Content Type | Priority |
|---|---------|------|------|---------|------------------|-------------|----------|
| 1 | r/ClaudeAI | Reddit | 747K | **Maximum** -- CEX runs on Claude Code, audience IS the user base | Low | "How I built X with Claude Code + CEX" experience post | P0 |
| 2 | r/LocalLLaMA | Reddit | 694K | **Maximum** -- CEX runs on Ollama, sovereignty messaging resonates | Medium | Benchmark: CEX artifact quality on Ollama vs Claude | P0 |
| 3 | r/LangChain | Reddit | 80K | **High** -- "alternative to LangChain" positioning | Medium | Comparison post: typed knowledge vs untyped chains | P0 |
| 4 | Hacker News (Show HN) | Forum | 10M+ readers | **High** -- AI tools routinely hit front page | High | "Show HN: I built a typed knowledge system for LLM agents" | P0 |
| 5 | Product Hunt | Launch platform | 10M+ | **High** -- CrewAI got #2 product of the day | Medium | Full launch page with demo video + testimonials | P0 |
| 6 | r/AutoGPT | Reddit | 100K | **High** -- autonomous agent enthusiasts | Low | "CEX: 7 autonomous nuclei that govern their own output quality" | P1 |
| 7 | r/PromptEngineering | Reddit | 200K | **High** -- 8F pipeline and prompt compilation are directly relevant | Low | "How CEX's 8F pipeline replaces manual prompt engineering" | P1 |

### Tier 2: High-Value Discord Servers (Weeks 2-6)

| # | Channel | Type | Size | CEX Fit | Entry Difficulty | Content Type | Priority |
|---|---------|------|------|---------|------------------|-------------|----------|
| 8 | LangChain Discord | Discord | 30K | High | Medium (no promotion) | Answer questions about multi-agent orchestration; mention CEX only when relevant | P1 |
| 9 | CrewAI Discord | Discord | 10K | High | Medium | Engage on crew/team composition topics; CEX's WAVE8 primitives are directly relevant | P1 |
| 10 | Hugging Face Discord | Discord | 50K | Medium | Low | Share how CEX integrates with HF models via Ollama | P1 |
| 11 | Learn AI Together Discord | Discord | 30K | Medium | Low | Tutorials and educational content about 8F pipeline | P2 |
| 12 | n8n Discord | Discord | 25K | High | Low | Automation + AI use case overlap with CEX | P2 |
| 13 | OpenRouter Discord | Discord | 8K | High | Low | Multi-model routing audience matches CEX multi-runtime | P2 |
| 14 | AnythingLLM Discord | Discord | 6K | High | Low | Self-hosted LLM audience matches sovereignty messaging | P2 |

### Tier 3: Content Amplification Channels (Weeks 4-8)

| # | Channel | Type | Size | CEX Fit | Entry Difficulty | Content Type | Priority |
|---|---------|------|------|---------|------------------|-------------|----------|
| 15 | Dev.to (AI tag) | Blog | 1M+ | High | Low | "Build your first typed AI artifact in 5 minutes" tutorial | P2 |
| 16 | Hashnode | Blog | 500K+ | Medium | Low | "How We Built CEX" narrative post | P2 |
| 17 | LinkedIn (GenAI.Works / AI groups) | Social | 14M+ (GenAI.Works) | Medium | Low | Enterprise positioning: "typed knowledge governance for AI operations" | P2 |
| 18 | r/MachineLearning | Reddit | 3M | Medium | High (rigorous community) | Technical architecture paper: 8F reasoning pipeline design | P3 |
| 19 | GitHub Awesome Lists | Curated | Various | Medium | Low | Submit to awesome-agents, awesome-llm, awesome-ai-tools | P3 |

### Tier 4: Newsletter and Influencer Outreach (Weeks 6-12)

| # | Channel | Type | Audience | CEX Fit | Approach | Priority |
|---|---------|------|----------|---------|----------|----------|
| 20 | console.dev | Newsletter | Developer tools | High | Pitch: "typed knowledge system -- a new category in AI tooling" | P3 |
| 21 | TLDR.tech | Newsletter | 1M+ devs | Medium | Submit via their open-source feature form | P3 |
| 22 | Latent.Space (swyx) | Newsletter/Podcast | AI engineers | High | Pitch: "convention over configuration for AI agents" angle | P3 |
| 23 | Last Week in AI | Newsletter | Research/practitioner | Medium | Submit after 500+ stars milestone | P3 |
| 24 | GitHub20K | Newsletter | OSS growth | High | Pitch: community seeding strategy + results data | P4 |

---

## 5. Content Calendar (Weeks 1-12)

### Pre-Launch Checklist (Week 0 -- Before ANY Public Post)

| Item | Status | Notes |
|------|--------|-------|
| README has 1-sentence value prop above fold | REQUIRED | "5 words in. Professional artifact out. Intelligence compounds." |
| Demo GIF showing `/build landing_page` (30 seconds) | REQUIRED | Record with asciinema or screen capture; show 8F trace |
| 3-line Quick Start in README | REQUIRED | `pip install cex` -> `cex init` -> `cex build landing_page` |
| Badge wall (license, version, CI) | REQUIRED | MIT badge, Python version, build status |
| Discord server created and structured | REQUIRED | Channels: #general, #showcase, #help, #nuclei-discussion, #pt-br |
| 50-100 seed stars from personal network | REQUIRED | Direct outreach to developer contacts (60% conversion rate per ScrapeGraphAI data) |
| Comparison table vs LangChain/CrewAI in README | REQUIRED | 5-row table: typed knowledge, quality gates, multi-runtime, brand injection, GDP |
| GitHub topics set | REQUIRED | ai-agents, llm, multi-agent, knowledge-management, typed-system, python, claude, ollama |

### Week 1: Soft Launch

| Day | Channel | Content | Format | Who Posts | Goal |
|-----|---------|---------|--------|-----------|------|
| Mon | GitHub | Polish README final version | README update | Core team | Convert visitors to stars |
| Tue | r/ClaudeAI | "I built an AI brain on top of Claude Code -- 300 typed artifact kinds, quality gates, multi-runtime. Here's what I learned." | Experience post (1,500 words) | Founder | 50-100 stars, 20+ comments |
| Wed | r/LocalLLaMA | "CEX runs on Ollama: your knowledge stays local. Here's a typed knowledge system that works offline." | Technical post with benchmarks | Founder | 50-100 stars, sovereignty discussion |
| Thu | Twitter/X | Thread: "Every AI agent forgets. CEX remembers. Here's how:" (5-tweet thread with demo GIF) | Thread | Founder personal | 200+ impressions, 20-50 stars |
| Fri | Discord | Open doors; post welcome message; invite early r/ClaudeAI and r/LocalLLaMA responders | Community launch | Core team | 30-50 Discord members |
| Sat-Sun | All | Respond to every comment/issue from Week 1 posts | Engagement | Founder | Trust building; convert commenters to contributors |

### Week 2: Technical Depth

| Day | Channel | Content | Format | Who Posts | Goal |
|-----|---------|---------|--------|-----------|------|
| Mon | r/LangChain | "Typed knowledge vs. untyped chains: what I built after hitting LangChain's ceiling" | Comparison post (genuine, not hostile) | Founder | 30-80 stars, framework comparison discussion |
| Tue | Dev.to | "Build Your First Typed AI Artifact in 5 Minutes with CEX" | Step-by-step tutorial | Core team | SEO indexing, 20-50 stars |
| Wed | r/PromptEngineering | "How CEX's 8F pipeline eliminates manual prompt engineering -- 8 functions that run automatically on every task" | Technical post | Founder | 20-40 stars, prompt engineering community awareness |
| Thu | Twitter/X | Thread: "CrewAI assigns roles. LangChain chains prompts. CEX types knowledge. Here's the difference:" | Comparison thread with diagrams | Founder personal | 400+ impressions |
| Fri | LangChain Discord | (DO NOT promote) Answer 2-3 questions about multi-agent orchestration from your experience building CEX | Contribution, not promotion | Core team member | Build reputation; plant seed for future organic mentions |

### Week 3: Show HN + Product Hunt

| Day | Channel | Content | Format | Who Posts | Goal |
|-----|---------|---------|--------|-----------|------|
| Mon | Preparation | Prepare Show HN post text and Product Hunt page materials | Internal | Core team | Ensure 50+ stars baseline before launch |
| Tue | Product Hunt | Launch CEX on Product Hunt (aim for Top 5 Product of the Day) | Full product page with demo video, screenshots, testimonials | Core team | 200-800 stars, 1,000-3,000 visits |
| Wed | Hacker News | "Show HN: CEX -- a typed knowledge system for LLM agents (300 kinds, 8F pipeline, 4 runtimes)" | Show HN submission (12-17 UTC) | Founder | 150-2,000 stars (top 10%: 500-2,000) |
| Wed | All | Respond to every HN comment within 3 hours | Aggressive engagement | Founder | HN score boost from engagement |
| Thu | Twitter/X | Amplification thread: "We hit Hacker News front page. Here's the real story behind CEX:" | Behind-the-scenes thread | Founder personal | Capture HN momentum |
| Fri | r/AutoGPT | "7 autonomous nuclei that govern each other's output quality -- here's how CEX rethinks multi-agent" | Technical post | Founder | 20-50 stars from autonomous agent enthusiasts |
| Weekend | GitHub | Respond to every new issue/PR; update README with "Used by X developers" if applicable | Maintenance | Core team | Convert HN/PH traffic to retained users |

### Week 4: Community Consolidation

| Day | Channel | Content | Format | Who Posts | Goal |
|-----|---------|---------|--------|-----------|------|
| Mon | Blog (Medium/Hashnode) | "How We Built CEX: From 5 Words to 300 Typed Knowledge Artifacts" | Long-form narrative (2,500 words) | Founder | Evergreen SEO, 20-200 stars |
| Tue | Discord | First "Office Hours" live session -- demo + Q&A | Live event (1 hour) | Founder + core team | Deepen community engagement; 10-20 new active members |
| Wed | LinkedIn | Article: "Why Your AI Agent Framework Needs Quality Governance" (enterprise angle) | LinkedIn article | Founder | Enterprise visibility, 3-5 inbound inquiries |
| Thu | r/MachineLearning (monthly self-promo thread) | "CEX: typed knowledge system for AI agents -- 300 artifact kinds, 8F pipeline, 4 runtimes" | Self-promotion thread post | Founder | Compliant exposure to 3M subscribers |
| Fri | GitHub Awesome Lists | Submit to: awesome-agents, awesome-llm, awesome-ai-tools, awesome-python | PR submissions | Core team | Long-tail passive discovery (20-200 stars over time) |

### Weeks 5-8: Amplification

| Week | Channel | Content | Format | Goal |
|------|---------|---------|--------|------|
| 5 | Dev.to + Hashnode | "CEX vs LangChain vs CrewAI: A Developer's Honest Comparison" | Comparison article (high SEO value) | 50-500 stars from search intent |
| 5 | Newsletter outreach | Pitch console.dev, TLDR.tech with launch data and star trajectory | Email pitch | Get featured in 1-2 newsletters (100-2,000 stars each) |
| 6 | YouTube | "Build a Complete AI Knowledge System in 15 Minutes with CEX" tutorial | Screen recording (15 min) | 100-800 stars; evergreen monthly return |
| 6 | Twitter/X | Version release announcement thread (v1.1 or v1.2) -- release cadence as event | Release thread | 20-100 stars per release event |
| 7 | Latent.Space pitch | "Convention over configuration for AI agents" -- guest post or podcast pitch | Email to swyx | Pipeline for high-value feature (500-3,000 stars) |
| 7 | Discord | Second Office Hours + "First Contributor" recognition program | Community event | Retain and activate community members |
| 8 | Reddit | Cross-post blog content to r/artificial (700K), r/ArtificialIntelligence (400K) | Adapted posts | Broader audience reach |
| 8 | LinkedIn Groups | Post in "GenAI.Works" (14M), "AI Professionals Network" (500K) | Enterprise content | CTO/enterprise audience |

### Weeks 9-12: Sustaining

| Week | Channel | Content | Format | Goal |
|------|---------|---------|--------|------|
| 9 | YouTube | Series: "8F Pipeline Deep Dive" (4 episodes) | Video series | 200-1,200 stars; establish as educational resource |
| 9 | GitHub | "Good First Issue" labels on 10+ issues; CONTRIBUTING.md | Contributor enablement | Convert users to contributors |
| 10 | Meetup / Conference | Submit talk proposals: "From Rails to AI: Convention over Configuration" | CFP submissions | Pipeline for 500-2,000 stars from talk videos |
| 10 | Community | Launch "CEX-certified AI engineer" pilot program (beta) | Certification | Investment lock-in (CrewAI pattern: 100K certified) |
| 11 | Newsletter | Second wave of newsletter pitches with updated metrics | Email pitch | Target Last Week in AI, GitHub20K |
| 11 | Twitter/X | "1,000 stars in X weeks" milestone thread (social proof escalation) | Milestone thread | Trigger press interest |
| 12 | Blog | "What We Learned Launching an Open-Source AI Brain: Data from 12 Weeks" | Retrospective post | Organic coverage; builds founder credibility |
| 12 | Discord | Third Office Hours; announce next quarter roadmap | Community event | Retention; signal longevity |

---

## 6. Content Templates

### Twitter/X Thread Template

```
Tweet 1:
Every AI agent forgets.
CEX remembers.

I built a typed knowledge system where intelligence compounds.
300 artifact kinds. 8-function reasoning pipeline. 4 runtimes.

Here's what that means for you: [thread]

[Attach: 30-second demo GIF of /build command]

Tweet 2:
Most AI frameworks give you building blocks.
CEX gives you a factory.

You say: "build landing_page"
CEX loads:
- The landing-page builder (12 specialized ISOs)
- Your brand context
- Quality gates (9.0 minimum)
- Compiles to your git repo

5 words in. Production artifact out.

Tweet 3:
The architectural difference:

LangChain: untyped chains (code)
CrewAI: untyped roles (ad hoc)
OpenClaw: untyped skills (13K, 20% compromised)

CEX: 300 TYPED kinds x 12 pillars
Every artifact has: schema, quality score, compilation

Typed knowledge > untyped output.

Tweet 4:
Runs on:
- Claude (via Claude Code)
- Gemini
- Codex
- Ollama (fully local)

Your knowledge stays in YOUR repo.
No vendor lock-in. No telemetry dependency.
No $39/seat/month (looking at you, LangSmith).

Self-sovereign AI infrastructure.

Tweet 5:
MIT license. Self-hosted. Quality-governed.

"5 words in. Professional artifact out.
Intelligence compounds."

Star the repo: [link]
Join Discord: [link]
Read the architecture: [link]

What would YOU build with 300 typed artifact kinds?
```

### Reddit Post Template (r/ClaudeAI)

```
Title: I built an AI brain on top of Claude Code -- 300 typed knowledge artifacts, quality gates, and multi-runtime dispatch

I've been building CEX for [time period] and wanted to share what I learned about
structuring AI output as typed, governed knowledge instead of disposable chat responses.

**The Problem**: Every AI framework produces untyped output. You prompt, you get text,
it evaporates. Next session starts from zero.

**What CEX Does Differently**:

1. **300 typed artifact kinds**: Every output has a kind (knowledge_card, landing_page,
   agent, workflow...), a pillar (P01-P12), and a schema. This means your AI output is
   searchable, compilable, and compounding.

2. **8F mandatory reasoning pipeline**: Every task passes through 8 functions --
   CONSTRAIN, BECOME, INJECT, REASON, CALL, PRODUCE, GOVERN, COLLABORATE. The pipeline
   is mandatory. No shortcuts.

3. **Quality gates**: Nothing ships below 8.0/10. F7 GOVERN runs 7 HARD gates and 5D
   scoring automatically.

4. **4 runtimes**: Claude, Gemini, Codex, Ollama. Your knowledge stays in your git repo
   regardless of which provider you use.

**Quick Start**:
```
/build landing_page
```
That's it. CEX loads the landing-page builder, injects your brand context, reasons
through 8F, produces the artifact, scores it, and compiles it into your repo.

**What I'm NOT claiming**: CEX is not a replacement for LangChain or CrewAI.
They're frameworks for building agent pipelines. CEX is a knowledge system --
it produces governed, typed artifacts that accumulate.

Happy to answer questions about the architecture. MIT license, self-hosted.

[Link to repo]
```

### Discord Introduction Template

```
Hey everyone! I'm [name], builder of CEX -- a typed knowledge system for LLM agents.

Quick context: CEX treats AI output as typed infrastructure, not disposable chat.
300 artifact kinds, 12 domain pillars, mandatory quality gates.

I'm here because [community name] is where the builders are, and I'd love to
learn from this community's experience with [topic].

Not here to spam -- genuinely interested in [community's focus area].
If anyone's curious about typed knowledge systems, happy to discuss.

Repo: [link] | Docs: [link]
```

### YouTube Video Concept Template

```
TITLE: "Build a Complete AI Knowledge System in 15 Minutes | CEX Tutorial"

HOOK (0-15 sec):
"What if your AI agent didn't forget everything after each conversation?
I'm going to show you a typed knowledge system that compounds intelligence --
and you can build your first artifact in under 5 minutes."

STRUCTURE:
0:00 - Hook + problem statement (AI amnesia)
0:30 - What CEX is (30-second overview)
1:30 - Install and init (live terminal)
3:00 - First /build command (live demo with 8F trace visible)
6:00 - Inspect the output (show frontmatter, typed structure, quality score)
8:00 - Brand injection demo (before/after with brand_config.yaml)
10:00 - Multi-runtime: same task on Claude vs Ollama
12:00 - Show compounding: how the second artifact references the first
14:00 - Recap + CTA (star, join Discord, try it yourself)

CTA: "Link in description. MIT license. Your knowledge stays in YOUR repo."
```

### Blog Post Outline Template

```
TITLE: "How We Built CEX: From 5 Words to 300 Typed Knowledge Artifacts"

SECTION 1: The Problem (300 words)
- AI output evaporates between sessions
- No quality governance on agent output
- Vendor lock-in to single providers
- Knowledge doesn't compound

SECTION 2: The Architecture Decision (500 words)
- Why typed knowledge (300 kinds x 12 pillars)
- Why mandatory reasoning (8F pipeline)
- Why multi-runtime (Claude/Gemini/Codex/Ollama)
- Why quality gates (9.0 target, F7 GOVERN)

SECTION 3: Live Demo (500 words + screenshots)
- /build landing_page walkthrough
- Show 8F trace output
- Show resulting artifact (frontmatter, structure, quality score)

SECTION 4: What Surprised Us (300 words)
- Honest reflections: what worked, what didn't
- Architectural pivots along the way
- Community feedback that changed direction

SECTION 5: What's Next (200 words)
- Roadmap highlights
- How to contribute
- CTA: star, join Discord, build your first artifact

TOTAL: ~1,800 words. Cross-post to Dev.to, Hashnode, Medium.
```

### Newsletter Pitch Template

```
Subject: New category in AI tooling: typed knowledge systems (300 kinds, 4 runtimes)

Hi [editor name],

I built CEX -- the first typed knowledge system for LLM agents. Instead of
untyped chains or ad hoc agent outputs, CEX produces typed, quality-gated
knowledge artifacts that compound in your git repo.

Why this matters for [newsletter name]'s audience:
- 300 artifact kinds (from knowledge_card to landing_page to workflow)
- Mandatory 8-function reasoning pipeline (quality floor: 9.0/10)
- Runs on Claude, Gemini, Codex, and Ollama (no vendor lock-in)
- MIT license, self-hosted, zero per-operation fees

We're at [X] stars in [Y] weeks with zero marketing spend.

Happy to provide:
- A 200-word feature blurb ready to publish
- Screenshots / demo GIF
- Technical architecture overview

Repo: [link]

Best,
[name]
```

---

## 7. BR-Specific Strategy

Brazilian communities require a fundamentally different approach from global English-language channels. The platform mix, cultural norms, and communication style differ significantly.

### Platform Priority (BR)

| Platform | Why Dominant in BR | CEX Approach |
|----------|-------------------|--------------|
| Telegram | 45% penetration; dominant for tech communities; groups are conversational and high-trust | Primary channel for organic seeding |
| WhatsApp | 97% smartphone penetration; Communities feature enables 5K-member groups | Bridge from Telegram groups (n8n Brasil has active WA link) |
| Discord | 252K in Rocketseat alone; younger dev audience; educational communities | Secondary channel; Rocketseat + Alura + AI Hub Brasil |
| Instagram | Not a dev platform but influencers cross-post here | Only for visual demos (Reels showing `/build` in action) |
| LinkedIn | Growing for tech content in BR; enterprise-facing | Enterprise positioning in Portuguese |

### BR Channel Priority (Ordered by Impact)

| # | Channel | Platform | Members | Approach | When |
|---|---------|----------|---------|----------|------|
| 1 | Data Hackers | Slack | 41,000+ | Post in #show-e-tell and #ferramentas with genuine value | Week 2 |
| 2 | AI Hub Brasil | Discord | 60,156 | Engage in IA generativa discussions; share CEX when relevant | Week 2 |
| 3 | n8n Brasil | Telegram + WA | 4,446 | Automacao + IA = direct CEX use case; most aligned BR community | Week 1 |
| 4 | Pt-BR Data Science & Python | Telegram | 5,025 | Technical content about CEX Python SDK and 8F pipeline | Week 3 |
| 5 | Python Brasil | Telegram | 25,317 | Channel (broadcast); approach via community content, not direct post | Week 4 |
| 6 | Agentes IA Brasil | Meetup | 67 | **Maximum fit**: new group about IA agents. Become a founding contributor | Week 1 |
| 7 | Rocketseat | Discord | 252,975 | Post technical article in community blog/forum area | Week 5 |
| 8 | Asimov Academy | Discord | 2,681 | Python + agentes IA = core CEX audience; educational approach | Week 4 |
| 9 | AI Professionals SP | Meetup | 8,708 | Present at meetup event; enterprise angle | Week 8 |
| 10 | PyData SP | Meetup | 8,050 | Submit lightning talk proposal | Week 8 |

### Cultural Norms for BR Communities

| Norm | Implication for CEX | Wrong Approach | Right Approach |
|------|---------------------|----------------|----------------|
| Portuguese first | All BR community content must be in Portuguese; English posts are ignored or viewed as elitist | Posting the English README | Write a dedicated PT-BR blog post and community introduction |
| Personal relationships matter | BR communities trust people, not brands | "CEX is a typed knowledge system..." (corporate) | "Oi pessoal, eu construi uma ferramenta que..." (personal) |
| WhatsApp is for relationships | WA groups expect conversational, not broadcast-style posts | Dropping a link without context | Participating in conversations for days before sharing anything |
| "Jeitinho" (creative pragmatism) | BR developers value practical shortcuts over theoretical architecture | Leading with "300 kinds x 12 pillars x 8F pipeline" | Leading with "faz uma landing page com 5 palavras" |
| Community loyalty | Once you earn trust in a BR group, members actively promote you | Spreading thin across 20+ groups | Deep engagement in 5-7 groups |
| Influencer respect | BR tech influencers (Filipe Deschamps, Rocketseat founders) have outsized impact | Ignoring BR influencer ecosystem | Identify 3-5 BR AI influencers and build relationships |

### BR Content Templates (Portuguese)

**Telegram Introduction (n8n Brasil):**
```
Oi pessoal! Eu construi uma ferramenta open-source chamada CEX que complementa
n8n pra quem trabalha com IA.

A ideia: ao inves do output da IA sumir depois de cada conversa, CEX salva tudo
como artefatos tipados no seu repositorio git. Sao 300 tipos de artefato, cada
um com quality gate automatico.

Roda em Claude, Gemini, ou Ollama local. MIT license, self-hosted.

Nao quero spammar o grupo -- so achei que podia ser util pra quem aqui trabalha
com automacao + IA. Se alguem quiser, posso mostrar um demo rapido.

Repo: [link]
```

**LinkedIn Article Title (PT-BR):**
```
"Por que o output do seu agente de IA deveria ser tipado
(e o que acontece quando nao e)"
```

### BR Influencer Targets

| Influencer | Platform | Audience | Why Relevant | Approach |
|------------|----------|----------|-------------|----------|
| Filipe Deschamps | YouTube (1M+) | General dev | Most trusted dev voice in BR | Pitch: "IA que acumula inteligencia" demo |
| Rafaella Ballerini | YouTube (500K+) | Junior devs | Gateway to BR dev community | Pitch: tutorial collaboration |
| Rocketseat team | YouTube + Discord | 252K Discord | Largest BR dev community | Pitch: guest technical post on their blog |
| Meigarom Lopes | YouTube + Telegram | DS community | "Seja um Data Scientist" channel | Pitch: CEX as DS knowledge management tool |
| Asimov Academy | YouTube + Discord | Python + IA | 10K+ students, agentes IA curriculum | Pitch: CEX integration into their agentes IA course |

---

## 8. Metrics and KPIs

### Primary Metrics

| Metric | Week 4 Target | Week 8 Target | Week 12 Target | Source |
|--------|---------------|---------------|----------------|--------|
| GitHub stars | 200-500 | 800-2,000 | 1,500-5,000 | GitHub API |
| GitHub forks | 20-50 | 80-200 | 200-500 | GitHub API |
| GitHub contributors | 3-5 | 10-15 | 20-30 | GitHub insights |
| Discord members | 50-100 | 150-300 | 300-500 | Discord analytics |
| Discord weekly active | 20-40 | 50-100 | 100-200 | Discord analytics |

### Secondary Metrics

| Metric | Week 4 Target | Week 8 Target | Week 12 Target | Source |
|--------|---------------|---------------|----------------|--------|
| Twitter impressions (per thread) | 500-2,000 | 2,000-5,000 | 5,000-10,000 | Twitter analytics |
| Reddit post upvotes (best post) | 20-50 | 50-150 | 100-300 | Reddit |
| Dev.to / blog post views | 500-1,000 | 1,000-3,000 | 3,000-5,000 | Platform analytics |
| Newsletter features | 0 | 1-2 | 3-5 | Tracking spreadsheet |
| YouTube tutorial views | N/A | 500-1,000 | 2,000-5,000 | YouTube analytics |
| Hacker News points (Show HN) | N/A | 30-100 (Week 3) | N/A (one-shot) | HN |

### Production Metrics (Long-Term Credibility)

| Metric | Week 4 Target | Week 8 Target | Week 12 Target | Source |
|--------|---------------|---------------|----------------|--------|
| Total artifacts compiled by community | 100 | 500 | 2,000 | cex_sdk telemetry (opt-in) |
| Total 8F pipeline runs | 200 | 1,000 | 5,000 | cex_sdk telemetry (opt-in) |
| Issues opened (shows real usage) | 10-20 | 30-60 | 60-100 | GitHub issues |
| PRs merged (contributor health) | 2-5 | 10-20 | 20-40 | GitHub PRs |

### Social Proof Escalation Ladder (Pre-Planned)

| Milestone | Press Angle | Channel | When |
|-----------|------------|---------|------|
| 100 stars | "100 developers building typed AI knowledge" | Twitter thread | Week 1-2 |
| 500 stars | "500 stars in X weeks -- here's what we learned" | Blog post + Reddit | Week 4-6 |
| 1,000 stars | "1,000 developers chose typed knowledge over untyped chains" | Newsletter pitch | Week 8-10 |
| 2,000 stars | "2,000 stars: CEX is the fastest-growing typed AI system" | Hacker News update | Week 10-12 |
| 5,000 stars | "5,000 developers compound intelligence with CEX" | Conference talk pitch | Quarter 2 |
| 10,000 stars | "10,000 stars: the typed knowledge revolution" | Media/press outreach | Quarter 3 |

---

## 9. Risk Register

| # | Risk | Probability | Impact | Mitigation |
|---|------|-------------|--------|------------|
| 1 | Hacker News post gets zero traction | Medium | High | Pre-seed 50+ stars before posting; post at 12-17 UTC on Tue-Wed; have engaging comment responses ready. Fallback: resubmit with different angle after 2 weeks |
| 2 | Reddit posts flagged as self-promotion | Medium | Medium | Build 2-4 weeks of genuine participation history before posting; post in self-promotion threads where available; frame as experience sharing, not product launch |
| 3 | "300 kinds is overwhelming" first impression | High | High | README leads with "5 words in, professional artifact out" -- hide complexity behind simplicity. Show 3-5 most useful kinds, not all 300 |
| 4 | Critics compare star count to LangChain/CrewAI | High | Medium | Preempt: "We're pre-launch. Here's what we have that they don't: [typed knowledge, quality gates, multi-runtime]." Position production metrics over vanity metrics |
| 5 | No community tutorials emerge organically | Medium | High | Make CEX trivially demo-able (15-min first artifact path). Create 3 example tutorials yourself. Seed "Good First Issue" labels for contributor onboarding |
| 6 | BR community sees CEX as "gringo tool" | Low | Medium | All BR content in Portuguese. Lead with personal story. Engage in BR communities for 2+ weeks before any CEX mention. Leverage CrewAI's Joao Moura as proof of BR market appetite |
| 7 | Discord server is empty/inactive | Medium | Medium | Do not launch Discord until 50+ people are ready to join (from Reddit/HN/PH response). Seed with 10+ welcome conversations. Schedule weekly office hours from day 1 |
| 8 | Product Hunt launch falls flat | Medium | Medium | Prepare hunter relationship 2 weeks before launch. Have 10+ early supporters ready for launch day engagement. Prepare polished screenshots and demo video in advance |
| 9 | Competitor community bans CEX mentions | Low | Low | Never promote in competitor Discord/Slack channels. Only mention CEX when answering a specific user question. Build reputation first, mention product second |
| 10 | README/docs quality does not match positioning claims | Medium | Critical | Dogfood: use CEX to build CEX docs. Demo GIF must show REAL output, not mocked screenshots. Every claim in README must be verifiable by visiting the repo |
| 11 | Founder burnout from 12-week daily posting schedule | Medium | High | Batch-create content on weekends for the coming week. Automate social media scheduling. Recruit 1-2 community volunteers by Week 4 to share posting load |
| 12 | GitHub's fake star detection flags coordinated seed stars | Low | High | Never use bot accounts. Only ask real developers who genuinely try the tool. Seed stars should come from accounts with real commit history and followers |

---

## Related Artifacts

| Artifact | Relationship |
|----------|-------------|
| [[kc_growth_casestudy_viral]] | Upstream: viral growth patterns informing replicable tactics |
| [[kc_growth_casestudy_organic]] | Upstream: organic growth patterns informing content strategy |
| [[kc_community_directory_global]] | Upstream: 88+ global channel targets |
| [[kc_br_community_directory]] | Upstream: 123 BR community targets |
| [[kc_content_formats_global]] | Upstream: content format effectiveness data |
| [[cm_cex_vs_landscape]] | Upstream: competitive positioning for messaging |
| [[kc_cex_positioning_analysis]] | Upstream: positioning angles for community content |
