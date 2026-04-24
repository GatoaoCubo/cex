---
id: tpl_outreach_messages
kind: prompt_template
pillar: P03
nucleus: n02
domain: outreach
version: 1.0.0
created: 2026-04-24
quality: null
tags: [seed-intel, outreach, templates, crm]
tldr: "Ready-to-send outreach templates for CEX seeding across tiers, platforms, and regions"
---

# Outreach Message Templates -- CEX Community Seeding

> N02 Creative Lust lens: every template below is designed to feel like a peer
> recommendation, not a marketing pitch. Developers can smell spam from 10 messages
> away. These templates pass the "would I actually read this if someone sent it to me?"
> test. Grounded in influencer directories (global 385 contacts, BR 353 contacts).

---

## 1. Template Matrix

| Template ID | Tier | Platform | Region | Tone | Length |
|-------------|------|----------|--------|------|--------|
| T1-X-EN | T1 (1M+) | Twitter/X DM | Global EN | Respectful, concise, demo-first | 140 words |
| T1-X-BR | T1 (1M+) | Twitter/X DM | Brazil PT-BR | Respectful, concise, demo-first | 140 words |
| T1-EM-EN | T1 (1M+) | Email | Global EN | Professional, value-dense | 200 words |
| T1-EM-BR | T1 (1M+) | Email | Brazil PT-BR | Professional, value-dense | 200 words |
| T1-YT-EN | T1 (1M+) | YouTube collab pitch | Global EN | Collaborative, demo-oriented | 250 words |
| T2-X-EN | T2 (100K-1M) | Twitter/X DM | Global EN | Peer-to-peer, specific | 120 words |
| T2-X-BR | T2 (100K-1M) | Twitter/X DM | Brazil PT-BR | Peer-to-peer, specific | 120 words |
| T2-EM-EN | T2 (100K-1M) | Email | Global EN | Direct, builder-focused | 180 words |
| T2-EM-BR | T2 (100K-1M) | Email | Brazil PT-BR | Direct, builder-focused | 180 words |
| T2-DC-EN | T2 (100K-1M) | Discord message | Global EN | Community-native | 100 words |
| T2-LI-EN | T2 (100K-1M) | LinkedIn message | Global EN | Professional-casual | 120 words |
| T2-LI-BR | T2 (100K-1M) | LinkedIn message | Brazil PT-BR | Professional-casual | 120 words |
| T3-X-EN | T3 (10K-100K) | Twitter/X reply thread | Global EN | Conversational, generous | 80 words |
| T3-RD-EN | T3 (10K-100K) | Reddit comment | Global EN | Community-first, no pitch | 100 words |
| T3-DC-EN | T3 (10K-100K) | Discord community post | Global EN | Show-and-tell format | 150 words |
| T3-BG-EN | T3 (10K-100K) | Blog guest post pitch | Global EN | Value-exchange | 200 words |
| T3-NL-EN | T3 (10K-100K) | Newsletter feature pitch | Global EN | Data-driven | 180 words |
| T4-P2P-EN | T4 (<10K) | Peer-to-peer | Global EN | Casual, genuine | 80 words |
| T4-OSS-EN | T4 (<10K) | Open-source contributor invitation | Global EN | Collaborative, specific | 120 words |
| T4-BLD-EN | T4 (<10K) | "Build with us" pitch | Global EN | Co-creation, ownership | 100 words |
| FU-NR | All | Follow-up: no response | All | Lighter, shorter | 60 words |
| FU-POS | All | Follow-up: positive response | All | Next steps, specific | 80 words |
| FU-TRY | All | Follow-up: after they try CEX | All | Feedback request | 80 words |

---

## 2. T1 Templates (1M+ Followers)

T1 contacts include: Sam Altman, Andrej Karpathy, Andrew Ng, Fireship, sentdex
(global); Leon Martins, Manual do Mundo, Rocketseat, Gustavo Guanabara (BR).

### T1-X-EN: Twitter/X DM (Global EN)

```
Subject: n/a (DM)

Hey {{FIRST_NAME}},

Huge fan of your {{RECENT_CONTENT_REFERENCE}}. It actually connects to something
we just shipped.

We built CEX -- an open-source AI brain with 300 typed knowledge artifacts, a
mandatory reasoning pipeline, and multi-runtime support (Claude, Gemini, Codex,
Ollama). Not another framework. It is a typed knowledge system where 5 words of
input produce governed, scored, production-ready output.

I think your audience would find the architecture genuinely interesting -- the
8-step reasoning trace alone is unlike anything in the agent space right now.

Would you be open to a 10-minute async demo? I can send a 2-minute video or a
live walkthrough -- whatever works for your schedule.

No strings, no ask beyond: try it, break it, tell us what is wrong.

{{SENDER_NAME}}
github.com/{{CEX_REPO}}
```

### T1-X-BR: Twitter/X DM (Brazil PT-BR)

```
Subject: n/a (DM)

Oi {{FIRST_NAME}},

Acompanho seu trabalho ha tempos -- {{RECENT_CONTENT_REFERENCE}} foi exatamente
o tipo de conteudo que me fez querer compartilhar isso com voce.

Lancamos o CEX -- um cerebro de IA open-source com 300 tipos de artefatos,
pipeline de raciocinio obrigatorio de 8 passos, e suporte multi-runtime (Claude,
Gemini, Codex, Ollama). Nao e mais um framework. E um sistema de conhecimento
tipado onde 5 palavras de input produzem saidas governadas e pontuadas.

Acho que sua audiencia iria curtir a arquitetura -- o trace de raciocinio de 8
passos e diferente de qualquer coisa no espaco de agentes agora.

Topa uma demo de 10 minutos? Posso mandar um video de 2 min ou fazer ao vivo
-- o que for mais facil pra voce.

Sem compromisso. So queremos feedback honesto.

{{SENDER_NAME}}
github.com/{{CEX_REPO}}
```

### T1-EM-EN: Email (Global EN)

```
Subject: CEX: typed AI brain -- 300 kinds, 8F pipeline, 4 runtimes (open source)

Hi {{FIRST_NAME}},

I have been following your work on {{TOPIC_AREA}} -- your {{RECENT_CONTENT_REFERENCE}}
was particularly relevant to what we have been building.

CEX is an open-source AI brain (MIT licensed) that takes a different approach from
frameworks like LangChain or CrewAI. Instead of chains and roles, CEX provides:

- 300 typed knowledge artifact kinds (not untyped text output)
- An 8-step mandatory reasoning pipeline (8F) that scores every artifact
- 7 specialized nuclei (each with a domain optimization lens)
- 4-runtime support: Claude, Codex, Gemini, Ollama (your choice, no lock-in)

The practical result: you type "/build landing_page" and CEX produces a complete,
quality-gated, compiled artifact. Every output is scored (9.0 target), indexed,
and version-controlled in your git repo. Intelligence compounds.

I would love to get your take on the architecture. We are pre-launch and looking for
technical eyes, not marketing endorsements. Your honest reaction -- including "this
is wrong because X" -- is exactly what we need.

Would a 15-minute demo work? I can do async (video) or live -- your call.

Best,
{{SENDER_NAME}}
{{SENDER_TITLE}}
github.com/{{CEX_REPO}}
```

### T1-EM-BR: Email (Brazil PT-BR)

```
Subject: CEX: cerebro de IA tipado -- 300 tipos, pipeline 8F, 4 runtimes (open source)

Oi {{FIRST_NAME}},

Acompanho seu trabalho em {{TOPIC_AREA}} -- {{RECENT_CONTENT_REFERENCE}} foi
particularmente relevante para o que estamos construindo.

CEX e um cerebro de IA open-source (licenca MIT) com uma abordagem diferente de
frameworks como LangChain ou CrewAI. Ao inves de chains e roles, CEX oferece:

- 300 tipos de artefatos de conhecimento tipados (nao texto desestruturado)
- Pipeline de raciocinio obrigatorio de 8 passos (8F) que pontua cada artefato
- 7 nucleos especializados (cada um com lente de otimizacao de dominio)
- 4 runtimes: Claude, Codex, Gemini, Ollama (sua escolha, sem lock-in)

O resultado pratico: voce digita "/build landing_page" e CEX produz um artefato
completo, governado, compilado. Cada saida e pontuada (meta 9.0), indexada e
versionada no seu repositorio git. Inteligencia que se acumula.

Gostaria da sua opiniao sobre a arquitetura. Estamos em pre-lancamento e buscamos
olhos tecnicos, nao endorsement de marketing. Sua reacao honesta -- incluindo
"isso esta errado porque X" -- e exatamente o que precisamos.

Uma demo de 15 minutos funciona? Posso mandar video ou fazer ao vivo -- voce
escolhe.

Abraco,
{{SENDER_NAME}}
{{SENDER_TITLE}}
github.com/{{CEX_REPO}}
```

### T1-YT-EN: YouTube Collab Pitch (Global EN)

```
Subject: Collab idea: "I gave this AI brain 5 words and it built a full app"

Hi {{FIRST_NAME}},

Your {{RECENT_VIDEO_TITLE}} hit {{VIEW_COUNT}} views -- well-deserved. The way you
explained {{SPECIFIC_CONCEPT}} made me think you would genuinely enjoy tearing apart
our architecture.

We built CEX, an open-source AI brain that is fundamentally different from every
agent framework on the market. Here is the hook for a potential video:

**"I gave this AI brain 5 words and it produced a production-ready artifact."**

What makes it demo-able:
1. The 8F reasoning trace runs live -- viewers see each of the 8 steps executing
2. 4-runtime comparison: same command on Claude vs Gemini vs Ollama (side-by-side)
3. 300 typed artifact kinds -- the JSON file alone is visually impressive
4. Quality scoring: the system grades its own output and rejects anything below 8.0

Format options:
- You run it solo, we provide a demo script + support
- We hop on a call and I walk you through it (you edit however you want)
- You roast it live (we genuinely want hard feedback)

Zero editorial control from our side. Your video, your take.

We are MIT licensed, pre-launch, and not selling anything. Just looking for
developer-grade scrutiny.

Would any of these work?

{{SENDER_NAME}}
github.com/{{CEX_REPO}}
```

---

## 3. T2 Templates (100K-1M Followers)

T2 contacts include: Rowan Cheung, Francois Chollet, Yohei Nakajima, Simon
Willison, Swyx, Harrison Chase, Joao Moura, Sebastian Raschka (global);
Filipe Deschamps, Fabio Akita, Danilo Gato, Rafael Milagre, Erick Wendel (BR).

### T2-X-EN: Twitter/X DM (Global EN + PT-BR)

**EN:**
```
Hey {{FIRST_NAME}} -- saw your thread on {{TOPIC}}. Resonated hard.

We just open-sourced CEX -- a typed AI brain with 300 artifact kinds, mandatory
quality scoring, and 4-runtime support (Claude/Gemini/Codex/Ollama).

The 8F reasoning pipeline is the part I think you would find most interesting --
it is mandatory (not opt-in), quality-gated, and produces a visible trace. No
other framework does this.

Happy to share early access or just a quick demo. Interested?

github.com/{{CEX_REPO}}
```

**PT-BR:**
```
Oi {{FIRST_NAME}} -- vi sua thread sobre {{TOPIC}}. Achei muito relevante.

Acabamos de lancar o CEX em open-source -- um cerebro de IA tipado com 300 tipos
de artefatos, pontuacao de qualidade obrigatoria, e suporte a 4 runtimes
(Claude/Gemini/Codex/Ollama).

O pipeline de raciocinio 8F e a parte que acho que voce ia curtir mais -- e
obrigatorio (nao opt-in), com gate de qualidade e trace visivel. Nenhum outro
framework faz isso.

Posso compartilhar acesso antecipado ou uma demo rapida. Interessa?

github.com/{{CEX_REPO}}
```

### T2-EM-EN: Email (Global EN + PT-BR)

**EN:**
```
Subject: CEX: what if AI artifacts were typed like database schemas?

Hi {{FIRST_NAME}},

Quick pitch, honest ask.

CEX is an open-source AI brain where every output is a typed knowledge artifact
-- not unstructured text. Think of it as convention-over-configuration applied to
AI agents: 300 artifact kinds, 12 domain pillars, mandatory 8-step reasoning
with quality scoring.

What makes it different from {{COMPETITOR_THEY_COVER}}:
- Typed knowledge taxonomy ({{COMPETITOR}} has zero)
- Mandatory quality gates (9.0 target, not optional)
- 4-runtime sovereignty: Claude, Codex, Gemini, Ollama

Your {{RECENT_CONTENT}} made me think you would have a strong opinion on whether
this architecture solves a real problem or over-engineers one.

Would love 15 minutes of your time -- demo or just a conversation about the
approach. We are pre-launch and specifically seeking people who will tell us what
is wrong, not what is right.

{{SENDER_NAME}}
github.com/{{CEX_REPO}}
```

**PT-BR:**
```
Subject: CEX: e se artefatos de IA fossem tipados como schemas de banco?

Oi {{FIRST_NAME}},

Pitch curto, pergunta honesta.

CEX e um cerebro de IA open-source onde cada saida e um artefato de conhecimento
tipado -- nao texto desestruturado. Pense como convencao-sobre-configuracao
aplicada a agentes de IA: 300 tipos de artefatos, 12 pilares de dominio,
raciocinio obrigatorio de 8 passos com pontuacao de qualidade.

O que diferencia do {{COMPETITOR_THEY_COVER}}:
- Taxonomia de conhecimento tipada ({{COMPETITOR}} tem zero)
- Gates de qualidade obrigatorios (meta 9.0, nao opcional)
- Soberania de 4 runtimes: Claude, Codex, Gemini, Ollama

Seu {{RECENT_CONTENT}} me fez pensar que voce teria uma opiniao forte sobre se
essa arquitetura resolve um problema real ou over-engenharia um.

Topa 15 minutos? Demo ou so uma conversa sobre a abordagem. Estamos em
pre-lancamento e buscamos especificamente gente que vai nos dizer o que esta
errado, nao o que esta certo.

{{SENDER_NAME}}
github.com/{{CEX_REPO}}
```

### T2-DC-EN: Discord Message (Global EN)

```
Hey {{USERNAME}} -- I have been lurking in this server for a while and your takes
on {{TOPIC}} are consistently the best here.

We just open-sourced something I think this community would want to tear apart:
CEX -- a typed AI brain with 300 artifact kinds and a mandatory reasoning pipeline.

Not another agent framework. The key difference: every output is quality-scored
(9.0 target) and lives in your git repo as a typed artifact. Runs on
Claude/Gemini/Codex/Ollama.

Would love your honest take: github.com/{{CEX_REPO}}

Happy to answer any architecture questions here in the channel.
```

### T2-LI-EN: LinkedIn Message (Global EN + PT-BR)

**EN:**
```
Hi {{FIRST_NAME}},

Your post on {{TOPIC}} caught my attention -- especially the point about
{{SPECIFIC_INSIGHT}}.

We are building CEX, an open-source typed knowledge system for AI agents. The
core idea: instead of untyped LLM outputs, every artifact is typed (300 kinds),
scored (9.0 quality target), and governed (8-step mandatory reasoning pipeline).
Runs on 4 runtimes -- no vendor lock-in.

I think your perspective on {{THEIR_DOMAIN}} would be valuable as we approach
launch. Would you be open to a quick look?

{{SENDER_NAME}}
```

**PT-BR:**
```
Oi {{FIRST_NAME}},

Seu post sobre {{TOPIC}} chamou minha atencao -- especialmente o ponto sobre
{{SPECIFIC_INSIGHT}}.

Estamos construindo o CEX, um sistema de conhecimento tipado open-source para
agentes de IA. A ideia central: ao inves de saidas de LLM desestruturadas, cada
artefato e tipado (300 tipos), pontuado (meta de qualidade 9.0) e governado
(pipeline de raciocinio obrigatorio de 8 passos). Roda em 4 runtimes -- sem
lock-in de provedor.

Acho que sua perspectiva sobre {{THEIR_DOMAIN}} seria valiosa conforme nos
aproximamos do lancamento. Topa dar uma olhada?

{{SENDER_NAME}}
```

---

## 4. T3 Templates (10K-100K Followers)

T3 contacts are the highest-volume segment (175 global, 265 BR). These are engaged
builders, educators, and community leaders. Outreach should feel like community
participation, not marketing.

### T3-X-EN: Twitter/X Reply Thread Template

```
This is genuinely interesting -- {{BRIEF_REACTION_TO_THEIR_POST}}.

We have been working on something related: a typed knowledge system for AI agents
where every output is a scored artifact (300 kinds, 8-step reasoning pipeline).

Runs on Claude, Gemini, Codex, or Ollama. MIT licensed.

Thread if anyone is curious: [link to CEX overview thread]
Repo: github.com/{{CEX_REPO}}
```

### T3-RD-EN: Reddit Comment Template

```
Interesting discussion. We have been working on a different angle on this problem.

Most agent frameworks produce untyped text output. We built CEX to produce typed
knowledge artifacts -- 300 artifact kinds organized across 12 domain pillars, with
a mandatory 8-step reasoning pipeline that scores every output (9.0 target).

The key difference: intelligence compounds. Every artifact is version-controlled
in git, indexed, and searchable. Run it on Claude, Gemini, Codex, or Ollama.

MIT licensed, pre-launch: github.com/{{CEX_REPO}}

Happy to answer questions about the architecture. We specifically built the
multi-runtime support for this community (looking at you, r/LocalLLaMA).
```

### T3-DC-EN: Discord Community Post Template

```
**Show & Tell: CEX -- a typed AI brain (open source)**

Hey everyone -- I wanted to share something we have been building that takes a
fundamentally different approach from existing agent frameworks.

**What it is:** An AI brain with 300 typed knowledge artifact kinds, organized
across 12 domain pillars, with a mandatory 8-step reasoning pipeline.

**What makes it different:**
- Every output is typed, scored (9.0 target), and compiled
- 7 specialized nuclei with domain optimization lenses
- Runs on Claude, Gemini, Codex, or Ollama (your choice)
- MIT licensed, self-sovereign (your repo, your knowledge)

**Quick demo:** `/build landing_page` -> complete, quality-gated artifact

Repo: github.com/{{CEX_REPO}}
Docs: [link to getting started]

Would love feedback from this community -- especially on the multi-runtime
architecture and the typed knowledge approach. What would you want to test first?
```

### T3-BG-EN: Blog Guest Post Pitch

```
Subject: Guest post pitch: "Convention over Configuration for AI Agents"

Hi {{EDITOR_NAME}},

I would like to pitch a guest post for {{PUBLICATION_NAME}} on a topic I think
your readers would find provocative:

**"Convention over Configuration for AI Agents: What Rails Taught Us About
Building AI Systems"**

The argument: every AI agent framework today makes you build from scratch --
choose your chains, define your roles, wire your tools. CEX applies the Rails
pattern to AI: 300 typed artifact kinds, 12 domain pillars, and a mandatory
reasoning pipeline that handles the HOW while you focus on the WHAT.

The piece would cover:
1. Why "agent framework fatigue" is real (LangChain vs CrewAI vs OpenAI SDK)
2. The typed knowledge gap: 10 competitor analysis showing zero typed taxonomies
3. What convention-over-configuration looks like for AI (with code examples)
4. A live demo walkthrough: 5 words in, professional artifact out

Length: 1,500-2,000 words. I can include benchmarks, architecture diagrams,
and competitive comparisons.

Full transparency: I work on CEX (open source, MIT). The post would focus on
the architectural pattern, not a product pitch. Happy to have your editorial
team review and reshape as needed.

{{SENDER_NAME}}
```

### T3-NL-EN: Newsletter Feature Pitch

```
Subject: For {{NEWSLETTER_NAME}}: typed AI brain with 300 artifact kinds (open source)

Hi {{EDITOR_NAME}},

Quick pitch for {{NEWSLETTER_NAME}}:

CEX is an open-source AI brain that takes a fundamentally different approach from
frameworks like LangChain, CrewAI, and OpenAI Agents SDK. The core innovation:

**Every AI output is a typed knowledge artifact.** 300 kinds. 12 domain pillars.
Mandatory quality scoring (9.0 target). Runs on Claude, Gemini, Codex, or Ollama.

Why your readers would care:
- Zero competitors have typed knowledge taxonomies (data from our 10-framework analysis)
- Self-sovereign: your knowledge stays in YOUR git repo
- Convention-over-configuration: the "Rails of AI agents"
- MIT licensed, no SaaS paywall, no per-operation fees

Stats: 300 kinds, 302 builders, 12 pillars, 8-step reasoning pipeline, 144 tools,
4 runtimes.

Happy to provide a quote, exclusive early access, or a demo for your team.

{{SENDER_NAME}}
github.com/{{CEX_REPO}}
```

---

## 5. T4 Templates (Micro, <10K Followers)

T4 contacts are peers, early-career builders, and open-source contributors. These
are the community's connective tissue. Outreach should feel like an invitation
to build together, not a pitch.

### T4-P2P-EN: Peer-to-Peer Community Message

```
Hey {{FIRST_NAME}} -- saw your {{PROJECT_OR_POST}} and thought you might find
this interesting.

We are building CEX, an open-source AI brain with typed knowledge artifacts (300
kinds, 8-step reasoning, runs on Ollama/Claude/Gemini/Codex).

Pre-launch, looking for early users who want to break things. Interested?

github.com/{{CEX_REPO}}
```

### T4-OSS-EN: Open-Source Contributor Invitation

```
Hi {{FIRST_NAME}},

I noticed your contributions to {{THEIR_PROJECT}} -- especially
{{SPECIFIC_CONTRIBUTION}}. Really solid work.

We are building CEX, an open-source AI brain (MIT licensed) and we are looking
for contributors in {{THEIR_SKILL_AREA}}. Specifically:

- {{SPECIFIC_CONTRIBUTION_OPPORTUNITY_1}}
- {{SPECIFIC_CONTRIBUTION_OPPORTUNITY_2}}

The codebase is Python + YAML + Markdown. 144 tools, 302 builder definitions,
and a typed knowledge system with 300 artifact kinds.

If you are curious: github.com/{{CEX_REPO}}

No pressure -- even a code review or architecture critique would be valuable.

{{SENDER_NAME}}
```

### T4-BLD-EN: "Build With Us" Collaboration Pitch

```
Hey {{FIRST_NAME}},

Your work on {{THEIR_PROJECT}} shows you think deeply about {{DOMAIN}}.

We are building something that might interest you: CEX is a typed AI brain where
300 artifact kinds are organized across 12 pillars. We have 302 builder agents
but we are missing depth in {{THEIR_EXPERTISE_AREA}}.

Would you want to co-build the {{SPECIFIC_KIND}}-builder? Your name on the
builder, full credit, MIT licensed. We handle the infrastructure; you bring the
domain expertise.

github.com/{{CEX_REPO}}
```

---

## 6. Follow-Up Sequences

### FU-NR: After No Response (3-Touch Sequence)

**Touch 1 (Day 5):**
```
Hi {{FIRST_NAME}} -- following up on my message about CEX (typed AI brain,
300 artifact kinds, open source). Totally understand if the timing is not right.

Here is a 90-second demo if you are curious: {{DEMO_LINK}}

No pressure either way. {{SENDER_NAME}}
```

**Touch 2 (Day 12):**
```
Last follow-up, I promise. Just shipped {{NEW_FEATURE_OR_MILESTONE}} on CEX
and thought you might find it relevant to {{THEIR_DOMAIN}}.

Repo: github.com/{{CEX_REPO}}

Either way, keep doing great work on {{THEIR_PLATFORM}}. {{SENDER_NAME}}
```

**Touch 3 (Day 30 -- only if genuinely relevant new development):**
```
Hey {{FIRST_NAME}} -- not following up on my old message (I will take the hint!).

Just wanted to share: CEX just {{MILESTONE}} and {{RELEVANT_DATA_POINT}}. Thought
you would genuinely find it interesting given your work on {{THEIR_FOCUS}}.

No response needed. Just sharing. {{SENDER_NAME}}
```

### FU-POS: After Positive Response (Next Steps)

```
Thanks {{FIRST_NAME}} -- glad it caught your attention.

Here is how to get started:

1. Clone the repo: git clone {{REPO_URL}}
2. Run: /build landing_page (see the 8F pipeline in action)
3. Check the reasoning trace: every step is visible

If you want a guided walkthrough, I am happy to hop on a 15-minute call:
{{CALENDAR_LINK}}

And if you just want to explore solo, the getting started guide is at:
{{DOCS_LINK}}

Let me know which works best for you.

{{SENDER_NAME}}
```

### FU-TRY: After They Try CEX (Feedback Request)

```
Hey {{FIRST_NAME}} -- hope you have had a chance to explore CEX.

Three quick questions (answer any, skip any):

1. What was your first reaction to the 8F reasoning trace?
2. Did anything feel over-engineered or unnecessary?
3. What would make you use this for a real project (vs. just exploring)?

Honest feedback is more valuable to us than a star -- though we would not say no
to one either. :)

If you ran into any issues, drop them as GitHub issues and I will personally
respond within 24 hours.

Thanks for giving it a shot.

{{SENDER_NAME}}
```

---

## 7. Personalization Variables

All `{{VARIABLES}}` used in templates, with data sources for CRM population.

| Variable | Description | Data Source |
|----------|-----------|-------------|
| `{{FIRST_NAME}}` | Contact's first name | CRM contact record (influencer directory) |
| `{{SENDER_NAME}}` | Your name (the person sending) | CRM sender profile |
| `{{SENDER_TITLE}}` | Your title / role | CRM sender profile |
| `{{CEX_REPO}}` | GitHub repository path | Config: repo URL (e.g., `gato3/cex-lab`) |
| `{{RECENT_CONTENT_REFERENCE}}` | Specific recent content they produced | Manual: check their feed before sending |
| `{{RECENT_VIDEO_TITLE}}` | Title of their recent video | YouTube: pull from channel |
| `{{VIEW_COUNT}}` | View count on referenced video | YouTube API or manual check |
| `{{SPECIFIC_CONCEPT}}` | A concept they explained well | Manual: watch/read their content |
| `{{TOPIC_AREA}}` | Their general area of expertise | CRM: tags from influencer directory |
| `{{TOPIC}}` | Specific topic of recent post/thread | Manual: check their recent posts |
| `{{SPECIFIC_INSIGHT}}` | A particular point they made | Manual: read their content |
| `{{THEIR_DOMAIN}}` | Their professional domain | CRM: "Content Type" field from directory |
| `{{COMPETITOR_THEY_COVER}}` | Framework they have reviewed/covered | Manual: search their content history |
| `{{RECENT_CONTENT}}` | Description of recent content | Manual: check before sending |
| `{{USERNAME}}` | Discord/platform username | CRM: platform-specific handle |
| `{{EDITOR_NAME}}` | Newsletter/blog editor name | CRM or masthead lookup |
| `{{PUBLICATION_NAME}}` | Name of newsletter/blog | CRM: "Newsletter" or "Publication" field |
| `{{NEWSLETTER_NAME}}` | Newsletter name | CRM: "Newsletter" field from directory |
| `{{PROJECT_OR_POST}}` | Their project or post reference | Manual: GitHub/social check |
| `{{THEIR_PROJECT}}` | Open-source project they contribute to | GitHub: check their profile |
| `{{SPECIFIC_CONTRIBUTION}}` | A specific commit/PR/feature they built | GitHub: check their contributions |
| `{{THEIR_SKILL_AREA}}` | Technical skill area | CRM: inferred from content type |
| `{{SPECIFIC_CONTRIBUTION_OPPORTUNITY_1}}` | Concrete task they could help with | Internal: check open issues/gaps |
| `{{SPECIFIC_CONTRIBUTION_OPPORTUNITY_2}}` | Second concrete task | Internal: check open issues/gaps |
| `{{THEIR_EXPERTISE_AREA}}` | Domain they are expert in | CRM: "Content Type" + manual |
| `{{SPECIFIC_KIND}}` | CEX artifact kind matching their expertise | Internal: map domain to kinds_meta.json |
| `{{THEIR_PLATFORM}}` | Platform where they are most active | CRM: "Primary Platform" field |
| `{{THEIR_FOCUS}}` | What they focus on professionally | CRM: "Content Type" field |
| `{{NEW_FEATURE_OR_MILESTONE}}` | Recent CEX development | Internal: changelog/commits |
| `{{MILESTONE}}` | CEX milestone (e.g., "hit 1K stars") | Internal: GitHub stats |
| `{{RELEVANT_DATA_POINT}}` | Data relevant to their domain | Internal: analytics |
| `{{DEMO_LINK}}` | Link to demo video | Internal: hosted video URL |
| `{{CALENDAR_LINK}}` | Scheduling link | Internal: Calendly/Cal.com |
| `{{DOCS_LINK}}` | Getting started docs link | Internal: docs URL |
| `{{REPO_URL}}` | Full clone URL | Config: `https://github.com/{{CEX_REPO}}.git` |

### CRM Population Priority

| Priority | Variables | Method |
|----------|----------|--------|
| P0 (auto-fill) | `FIRST_NAME`, `SENDER_NAME`, `CEX_REPO`, `REPO_URL` | CRM auto-populate |
| P1 (semi-auto) | `TOPIC_AREA`, `THEIR_DOMAIN`, `THEIR_SKILL_AREA`, `THEIR_PLATFORM` | CRM fields from influencer directory |
| P2 (manual, required) | `RECENT_CONTENT_REFERENCE`, `SPECIFIC_CONCEPT`, `TOPIC` | Research before sending -- 5 min per contact |
| P3 (manual, optional) | `SPECIFIC_CONTRIBUTION`, `COMPETITOR_THEY_COVER` | Deeper research -- 10 min per contact |

### Personalization Rules

1. **Never send a template without filling P0 + P1 + at least one P2 variable.**
   Generic messages get deleted. The {{RECENT_CONTENT_REFERENCE}} is what makes
   the message feel personal.

2. **Research before outreach.** Spend 5 minutes on their profile. Check their
   last 3 posts/videos. Reference something specific. This is not optional.

3. **Match their energy.** If they tweet casually, your DM should be casual. If
   they write formal LinkedIn posts, match that tone. The templates are starting
   points, not scripts.

4. **BR contacts: always use PT-BR templates.** Even if they speak English. The
   local language signals respect and community membership.

5. **Do not batch-send.** Maximum 10 personalized messages per day. Quality over
   quantity. A single genuine conversation with Filipe Deschamps is worth more
   than 50 generic DMs.

---

## Regional Notes

### Brazil-Specific Adjustments

- **CrewAI founder advantage:** Joao Moura is Brazilian. BR devs already have
  cultural affinity with an agent framework founder. Position CEX as architecturally
  deeper (typed vs role-based), not as a replacement. Respect the home-court.

- **Platform priority in BR:** Instagram and YouTube dominate over Twitter/X for
  developer content. Prioritize video-friendly outreach for BR contacts.

- **Community-first culture:** BR tech communities (Data Hackers, He4rt, BrazilJS,
  Telegram groups) are deeply collaborative. Lead with community contribution
  (guest talks, workshops, hackathons), not product pitches.

- **Academic respect:** BR has strong university AI programs (Unicamp, USP, UFMG,
  SENAI CIMATEC). Academic endorsement carries significant weight. Approach
  researchers with the "convention over configuration" angle (Option C from
  positioning analysis) -- it resonates with computer science faculty.

- **Key BR events for seeding:** AI Festival (StartSe, May 13-14), TDC Summit IA
  (Apr 23-24), AI Summit Brasil (Florianopolis), BrazilJS Conference.

### Global Adjustments

- **Hacker News:** Use the "convention over configuration" angle. HN audiences
  value technical depth over marketing polish. No emoji, no hype words.

- **r/LocalLLaMA:** Lead with Ollama support and self-sovereign architecture.
  This community cares about running locally, not about cloud features.

- **r/ClaudeAI:** Lead with Claude Code integration and the 8F pipeline. This
  community already uses Claude and wants to see what CEX adds on top.

- **YouTube:** Demo-ability is everything. Provide a demo script, B-roll footage
  of the 8F trace running, and side-by-side runtime comparison clips.

---

## Sources

- Global influencer directory: `N01_intelligence/P01_knowledge/kc_influencer_directory_global.md` (385 contacts)
- BR influencer directory: `N01_intelligence/P01_knowledge/kc_influencer_directory_br.md` (353 contacts)
- Positioning statement: `N02_marketing/P03_prompt/kc_cex_positioning_statement.md`
- Positioning analysis: `N01_intelligence/P01_knowledge/kc_cex_positioning_analysis.md`
- Competitive matrix: `N01_intelligence/P07_evals/cm_cex_vs_landscape.md`
