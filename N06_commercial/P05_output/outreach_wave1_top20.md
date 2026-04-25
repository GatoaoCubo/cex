---
id: outreach_wave1_top20
kind: knowledge_card
pillar: P05
nucleus: n06
domain: influencer-outreach
version: 1.0.0
created: 2026-04-25
quality: null
tags: [seed-intel, outreach, wave1, top20, crm]
tldr: "Personalized outreach brief for the top 20 influencer targets in CEX's first seeding wave, ordered by recommended contact sequence"
---

# Wave 1 Outreach Brief: Top 20 Influencer Targets

> N02 Creative Lust lens applied. Every message below passes the "would I read this
> if a stranger sent it to me?" test. Peer-to-peer technical tone. Zero marketing-speak.
>
> Source data: kc_influencer_crm_unified.md (738 contacts, frozen 2026-04-24)
> Templates: tpl_outreach_messages.md (22 template IDs)
> Positioning: kc_cex_positioning_statement.md
> Playbook: kc_seeding_playbook.md

---

## Selection Criteria

Contacts selected from CRM with `priority_score >= 8`. Ties broken by:
1. `relevance_to_cex = HIGH` preferred over MEDIUM
2. `engagement_estimate = HIGH` preferred over MEDIUM
3. Platform fit for developer tooling (GitHub > Twitter > YouTube > Newsletter)

Total contacts scoring >= 8 in CRM: 42. Narrowed to 20 for Wave 1 based on
likelihood of response (individuals > orgs, builders > commentators, active
posters > irregular).

---

## Top 20 Contacts by Recommended Outreach Sequence

Sequencing logic: lead with builders who already work in the agent/CLI/OSS space
(highest response probability + amplification among exactly our target audience),
then expand to educators and content amplifiers.

---

### #1. Danilo Gato

| Field | Value |
|-------|-------|
| CRM # | 111 |
| Region | BR |
| Tier | T2 (100K+) |
| Platform | Twitter/X (primary), YouTube, Instagram, LinkedIn, Podcast, Newsletter |
| Handle | @odanilogato |
| Followers | 100K+ (X), 50K+ (IG), 15K+ (LI), YouTube, Podcast "Papo de IA" |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 10 (highest in entire CRM) |
| Content Type | AI content, tools, daily posts |
| Posting Frequency | daily |

**Why he matters for CEX:** #1 AI content creator in Brazil per Favikon ranking. Founder of CPDF. FGV professor. Multi-platform presence means a single positive take from him cascades across Twitter, YouTube, Instagram, LinkedIn, and his podcast "Papo de IA" (ranked #1 tech on Spotify BR). His audience is exactly the AI-curious Brazilian developer who would adopt CEX.

**Template to use:** T2-X-BR (Twitter/X DM, PT-BR, peer-to-peer)

**Personalization notes:** Reference his daily AI tool coverage. Connect CEX's typed knowledge approach to the tool fatigue his audience experiences -- he reviews new AI tools constantly, and CEX is architecturally different from everything he has covered. His "Papo de IA" podcast is a natural fit for a deep-dive episode.

**Recommended message:**

```
Oi Danilo -- vi sua cobertura diaria de ferramentas de IA e achei muito relevante
pro que estamos construindo.

Acabamos de lancar o CEX em open-source -- um cerebro de IA tipado com 300 tipos
de artefatos, pontuacao de qualidade obrigatoria, e suporte a 4 runtimes
(Claude/Gemini/Codex/Ollama).

O pipeline de raciocinio 8F e a parte que acho que voce ia curtir mais -- e
obrigatorio (nao opt-in), com gate de qualidade e trace visivel. Nenhum outro
framework faz isso.

Acho que seria um topico forte pro Papo de IA -- "cerebro de IA que acumula
inteligencia" vs. agentes descartaveis. Posso compartilhar acesso antecipado
ou uma demo rapida. Interessa?

github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM (primary), LinkedIn message (backup)

**Timing:** Weekday morning (he posts daily -- catch him during content prep). Tuesday-Thursday optimal.

**Risk/anti-pattern:** None significant. He actively reviews tools. Approach as peer sharing, not pitch. His multi-platform presence means a positive response amplifies everywhere.

---

### #2. Simon Willison

| Field | Value |
|-------|-------|
| CRM # | 151 / 210 / 267 |
| Region | GLOBAL |
| Tier | T3 (Twitter), T3 (GitHub), T3 (Blog) |
| Platform | Twitter/X, GitHub, Blog (all HIGH relevance) |
| Handle | @simonw (Twitter), simonw (GitHub) |
| Followers | 40K+ (X), 15K+ stars (llm/Datasette), 100K+ (blog readers) |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 9 (consistent across all 3 platform entries) |
| Content Type | CLI LLM tools, OSS, AI commentary |
| Posting Frequency | daily |

**Why he matters for CEX:** Creator of `llm` CLI tool and Datasette. He is the single most influential voice in the "CLI tools for LLMs" space -- exactly where CEX lives. His blog posts routinely reach Hacker News front page. A mention from Simon is worth 500-2,000 GitHub stars based on historical patterns. He is a typed-systems advocate who would immediately understand CEX's architecture.

**Template to use:** T3-X-EN (Twitter/X reply thread) for initial contact, then T2-EM-EN (email) for follow-up

**Personalization notes:** Reference his `llm` tool and how CEX's 300 typed artifact kinds extend the concept of structured LLM output that he has been advocating. His Datasette work shows he values typed data -- CEX applies the same principle to AI artifacts. Do NOT position as competitor to his tools; position as complementary.

**Recommended message (Twitter reply to one of his threads):**

```
This is genuinely interesting -- your point about structured LLM output resonates
with something we have been building.

We took the typed-output idea to its logical extreme: 300 artifact kinds, each
with a schema, quality gates (9.0 target), and a mandatory 8-step reasoning
pipeline. Runs on Claude, Gemini, Codex, or Ollama. MIT licensed.

Think of it as convention-over-configuration applied to LLM artifacts -- similar
philosophy to how Datasette treats data.

Repo: github.com/gato3/cex

Would genuinely value your architectural critique.
```

**Outreach channel:** Twitter/X public reply (he engages with replies), then DM if he responds

**Timing:** Weekday, during US Pacific business hours. He blogs and tweets actively during workdays.

**Risk/anti-pattern:** Simon is highly opinionated and will publicly critique anything he finds architecturally wrong. This is a feature, not a bug -- his honest feedback is more valuable than uncritical praise. Do NOT oversell. Let the architecture speak. Per seeding playbook: he is the type who will "tell us what is wrong, not what is right."

---

### #3. Yohei Nakajima

| Field | Value |
|-------|-------|
| CRM # | 108 |
| Region | GLOBAL |
| Tier | T2 (100K-1M) |
| Platform | Twitter/X |
| Handle | @yoheinakajima |
| Followers | 108K |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 9 |
| Content Type | AI agents, BabyAGI |
| Posting Frequency | weekly |

**Why he matters for CEX:** Creator of BabyAGI -- one of the earliest autonomous agent frameworks. He understands multi-agent orchestration at a deep level and would immediately grasp CEX's 7-nuclei architecture and the 8F reasoning pipeline. His endorsement signals "the agent space pioneer thinks this matters."

**Template to use:** T2-X-EN (Twitter/X DM, Global EN)

**Personalization notes:** Reference BabyAGI's task decomposition and how CEX's 8F pipeline formalizes the reasoning loop that BabyAGI pioneered informally. Connect to his ongoing interest in agent architectures that self-improve.

**Recommended message:**

```
Hey Yohei -- BabyAGI was the project that first showed task decomposition could
work in autonomous agents. It actually connects to something we just shipped.

We built CEX -- an open-source AI brain with 300 typed knowledge artifacts, a
mandatory 8-step reasoning pipeline, and multi-runtime support (Claude/Gemini/
Codex/Ollama). The 8F pipeline essentially formalizes the reasoning loop --
CONSTRAIN, BECOME, INJECT, REASON, CALL, PRODUCE, GOVERN, COLLABORATE.

The part I think you would find most interesting: every artifact is quality-scored
(9.0 target) and the system self-improves via an evolution loop that re-processes
artifacts below threshold.

Happy to share early access or just a quick demo. Interested?

github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM

**Timing:** He posts weekly -- mid-week (Tue-Thu) when he is actively engaging on Twitter.

**Risk/anti-pattern:** None. He is known for being generous with feedback on agent projects. Just be genuine and reference his specific work.

---

### #4. Harrison Chase

| Field | Value |
|-------|-------|
| CRM # | 148 / 207 |
| Region | GLOBAL |
| Tier | T3 (Twitter), T3 (GitHub) |
| Platform | Twitter/X, GitHub |
| Handle | @hwchase17 (Twitter), hwchase17 (GitHub) |
| Followers | 45K+ (X), LangChain 100K+ stars |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 9 |
| Content Type | LangChain, agent frameworks |
| Posting Frequency | daily |

**Why he matters for CEX:** CEO of LangChain -- the largest agent framework by stars. He IS the competitive landscape. But this is exactly why reaching out matters: if Harrison acknowledges CEX's typed-knowledge approach as solving a real problem LangChain does not address, that is the strongest possible signal to the market. He is not an enemy -- he is the person most qualified to evaluate whether typed knowledge taxonomies matter.

**Template to use:** T2-EM-EN (Email, professional)

**Personalization notes:** Frame as architectural conversation, not competition. Reference the specific gap: LangChain produces untyped output. CEX produces typed, scored, compiled artifacts. This is not "better than LangChain" -- it is a different architectural choice. He is the smartest person to evaluate whether that choice matters.

**Recommended message:**

```
Subject: CEX: what if AI artifacts were typed like database schemas?

Hi Harrison,

Quick pitch, honest ask.

CEX is an open-source AI brain where every output is a typed knowledge artifact
-- not unstructured text. Think of it as convention-over-configuration applied to
AI agents: 300 artifact kinds, 12 domain pillars, mandatory 8-step reasoning
with quality scoring.

What makes it different from LangChain (genuine respect for what you built):
- Typed knowledge taxonomy (LangChain produces graphs/chains; CEX produces typed artifacts)
- Mandatory quality gates (9.0 target, not optional)
- 4-runtime sovereignty: Claude, Codex, Gemini, Ollama

I think you would have the strongest opinion in the industry on whether typed
knowledge taxonomies solve a real problem or over-engineer one.

Would love 15 minutes of your time -- demo or just a conversation about the
approach. We are pre-launch and specifically seeking people who will tell us what
is wrong, not what is right.

Best,
Gato3
github.com/gato3/cex
```

**Outreach channel:** Email (professional channel for competitor-to-competitor). Needs research for email address -- try GitHub profile or LangChain team page.

**Timing:** Mid-week, morning US Eastern time.

**Risk/anti-pattern:** Seeding playbook warns: "Never promote in competitor Discord/Slack channels." This is direct outreach to the founder, which is different -- it is a professional conversation, not community spam. Risk: he ignores it (likely). Upside: he engages (massive signal). Do NOT frame as "better than LangChain." Frame as "different architectural bet -- what do you think?"

---

### #5. Joao Moura

| Field | Value |
|-------|-------|
| CRM # | 159 / 208 |
| Region | GLOBAL (Brazilian) |
| Tier | T3 (Twitter), T3 (GitHub) |
| Platform | Twitter/X, GitHub |
| Handle | @joaomdmoura (Twitter), joaomdmoura (GitHub) |
| Followers | 30K+ (X), CrewAI 25K+ stars |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 9 |
| Content Type | Multi-agent orchestration, CrewAI |
| Posting Frequency | weekly |

**Why he matters for CEX:** Founder of CrewAI and Brazilian. The seeding playbook notes: "BR devs already have cultural affinity with an agent framework founder." Joao understands crews, roles, and multi-agent handoffs -- CEX's WAVE8 composable crew protocol is the closest architectural parallel in the market. His audience is the exact developer who wants structured multi-agent orchestration.

**Template to use:** T2-X-BR (Twitter/X DM, PT-BR -- he is Brazilian, per playbook: "always use PT-BR templates")

**Personalization notes:** Reference CrewAI's role/goal/backstory pattern and how CEX extends it with typed artifacts + mandatory quality gates. Position as architectural dialogue, not competition. Respect the home-court.

**Recommended message:**

```
Oi Joao -- o que voce construiu com CrewAI (role/goal/backstory) abriu a cabeca
de muita gente sobre multi-agent orchestration. Achei muito relevante.

Acabamos de lancar o CEX em open-source -- um cerebro de IA tipado com 300 tipos
de artefatos, pontuacao de qualidade obrigatoria, e suporte a 4 runtimes.

O que e diferente da abordagem do CrewAI: cada saida e um artefato tipado com
schema, nao texto livre. E o pipeline de raciocinio de 8 passos e obrigatorio
(nao opt-in), com gate de qualidade e trace visivel.

Acho que voce teria uma opiniao forte sobre se tipagem de artefatos de IA
resolve um problema real. Topa trocar uma ideia?

github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM (PT-BR)

**Timing:** Mid-week. He engages on Twitter during Brazilian business hours.

**Risk/anti-pattern:** Playbook says "Position CEX as architecturally deeper (typed vs role-based), not as a replacement. Respect the home-court." Never say "better than CrewAI." Say "different architectural choice."

---

### #6. Swyx (Shawn Wang)

| Field | Value |
|-------|-------|
| CRM # | 86 / 146 |
| Region | GLOBAL |
| Tier | T2 (Newsletter), T3 (Twitter) |
| Platform | Newsletter (Latent Space), Twitter/X, Podcast |
| Handle | @swyx (Twitter), Latent Space (Newsletter/Pod) |
| Followers | 200K+ (newsletter), 50K+ (Twitter) |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 9 |
| Content Type | AI engineering |
| Posting Frequency | weekly |

**Why he matters for CEX:** Top 10 US Tech podcast. Coined the term "AI Engineering." Latent Space is the newsletter/podcast that senior AI engineers actually read. A feature on Latent Space would reach the exact audience that would both use and contribute to CEX. The seeding playbook lists him as a Week 7 target for "convention over configuration for AI agents" pitch.

**Template to use:** T2-EM-EN (Email) for newsletter pitch, T3-NL-EN (Newsletter feature pitch) as alternative

**Personalization notes:** Reference his "AI Engineering" framing. CEX IS AI engineering infrastructure -- typed knowledge artifacts are the building blocks. Connect to his recent podcast episodes about agent frameworks. The "convention over configuration" angle resonates with his Rails background.

**Recommended message:**

```
Subject: CEX: convention over configuration for AI agents (typed knowledge system)

Hi Shawn,

Your "AI Engineering" framing changed how the industry thinks about LLM
infrastructure. CEX is an attempt to build the convention-over-configuration
layer that AI engineering has been missing.

Quick version: open-source AI brain where every output is a typed knowledge
artifact. 300 artifact kinds, 12 domain pillars, mandatory 8-step reasoning
with quality scoring (9.0 target). Runs on Claude, Codex, Gemini, Ollama.

What makes it different from LangChain/CrewAI/OpenAI SDK:
- Typed knowledge taxonomy (300 kinds with schemas -- they have zero)
- Mandatory quality gates (not optional)
- 4-runtime sovereignty (no vendor lock-in)

I think the "typed knowledge vs untyped output" thesis would be an interesting
angle for Latent Space -- it is a genuinely new architectural pattern, not
another agent framework.

Would a 15-minute demo work? Happy to do async video or live.

Gato3
github.com/gato3/cex
```

**Outreach channel:** Email via Substack or Latent Space contact form

**Timing:** Weekday, early in the week (Mon-Tue). Newsletter goes out mid-week, so pitches early in the week get reviewed during planning.

**Risk/anti-pattern:** Swyx is discerning -- he will not feature something that does not have real traction. Wait until post-launch (at least 100+ stars) before pitching. Per playbook: "Pitch after 500+ stars milestone" is the conservative target, but a pre-launch technical deep-dive is also viable if the architecture is genuinely novel.

---

### #7. Rocketseat (Diego Fernandes)

| Field | Value |
|-------|-------|
| CRM # | 21 |
| Region | BR |
| Tier | T1 (1M+) |
| Platform | YouTube (primary), Instagram, LinkedIn |
| Handle | Rocketseat / Diego Fernandes |
| Followers | 1M+ (YT), 55K+ students, 252K Discord, 50K+ IG |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 9 |
| Content Type | React, Node, fullstack, AI tooling |
| Posting Frequency | daily |

**Why he matters for CEX:** Co-founder/CTO of Rocketseat -- the largest developer education community in Brazil (252K Discord members). He covers AI tooling. His audience is the Brazilian fullstack developer who is already using AI tools but lacks a structured system. Rocketseat's educational format is ideal for a "build your first artifact in 5 minutes" tutorial.

**Template to use:** T1-X-BR (Twitter/X DM, PT-BR) or T1-YT-EN adapted to PT-BR for YouTube collab

**Personalization notes:** Reference Rocketseat's coverage of AI tooling and developer workflow. Position CEX as the missing infrastructure layer between "I use ChatGPT" and "I have a production AI system." His community would respond to the convention-over-configuration angle -- they already understand it from React/Next.js patterns.

**Recommended message:**

```
Oi Diego,

Acompanho o trabalho da Rocketseat ha tempos -- a cobertura de AI tooling e
exatamente o tipo de conteudo que me fez querer compartilhar isso com voce.

Lancamos o CEX -- um cerebro de IA open-source com 300 tipos de artefatos,
pipeline de raciocinio obrigatorio de 8 passos, e suporte multi-runtime (Claude,
Gemini, Codex, Ollama). Nao e mais um framework. E um sistema de conhecimento
tipado onde 5 palavras de input produzem saidas governadas e pontuadas.

Acho que a comunidade Rocketseat iria curtir a arquitetura -- pense como
convention-over-configuration (que o pessoal ja conhece do Next.js) aplicado a
agentes de IA.

Topa uma demo de 10 minutos? Posso mandar um video de 2 min ou fazer ao vivo
-- o que for mais facil pra voce.

Sem compromisso. So queremos feedback honesto.

Gato3
github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM or LinkedIn message

**Timing:** Weekday, Brazilian business hours. He posts daily -- any weekday morning works.

**Risk/anti-pattern:** Rocketseat is education-first. Frame as educational content opportunity ("tutorial for your community"), not product promotion.

---

### #8. Filipe Deschamps

| Field | Value |
|-------|-------|
| CRM # | 34 |
| Region | BR |
| Tier | T2 (100K-1M) |
| Platform | YouTube (800K+), Newsletter, Twitter, Podcast |
| Handle | Filipe Deschamps |
| Followers | 800K+ (YT), largest BR tech newsletter, TabNews founder |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 9 |
| Content Type | Tech news, OSS, curso.dev |
| Posting Frequency | daily |

**Why he matters for CEX:** Largest Brazilian tech newsletter. TabNews founder (community news platform). He covers open-source developer tools daily, and his audience trusts his judgment. A feature in his newsletter reaches the core Brazilian developer audience at scale.

**Template to use:** T2-EM-BR (Email, PT-BR)

**Personalization notes:** Reference TabNews and his daily tech news coverage. Position CEX as a "Show TabNews" worthy project. His audience would value the MIT license, self-hosting, and Ollama support. He built TabNews (open-source) -- he understands the OSS developer community.

**Recommended message:**

```
Subject: CEX: cerebro de IA tipado -- 300 tipos, pipeline 8F, 4 runtimes (open source)

Oi Filipe,

Acompanho seu trabalho no TabNews e na newsletter -- a cobertura diaria de
ferramentas dev foi particularmente relevante para o que estamos construindo.

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
olhos tecnicos, nao endorsement de marketing.

Uma demo de 15 minutos funciona? Posso mandar video ou fazer ao vivo.

Abraco,
Gato3
github.com/gato3/cex
```

**Outreach channel:** Email (he prefers email for professional outreach)

**Timing:** Early week (Mon-Tue). Newsletter planning happens early in the week.

**Risk/anti-pattern:** Playbook notes: "A single genuine conversation with Filipe Deschamps is worth more than 50 generic DMs." Invest time in personalization. Research his last 3 videos before sending.

---

### #9. Fabio Akita

| Field | Value |
|-------|-------|
| CRM # | 37 |
| Region | BR |
| Tier | T2 (100K-1M) |
| Platform | YouTube (700K+), Twitter, Instagram |
| Handle | Fabio Akita / @AkitaOnRails |
| Followers | 700K+ (YT), 60K+ (X), 15K+ (IG) |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 9 |
| Content Type | CS fundamentals, history, deep technical content |
| Posting Frequency | weekly |

**Why he matters for CEX:** The most technically respected developer content creator in Brazil. His handle is literally "AkitaOnRails" -- he LIVED the Rails convention-over-configuration revolution. The "convention over configuration for AI agents" angle was designed for people exactly like him. His deep CS content style means he would actually understand and articulate the 8F pipeline architecture.

**Template to use:** T2-EM-BR (Email, PT-BR, professional) or T2-X-BR (Twitter DM)

**Personalization notes:** The Rails connection is the hook. His handle tells you everything. CEX applies the exact same architectural principle (opinionated conventions over ad-hoc configuration) that made Rails revolutionary -- but to AI agent output. Reference his CS fundamentals content and how 8F is essentially a formalization of software engineering quality gates applied to AI.

**Recommended message:**

```
Subject: CEX: convencao sobre configuracao -- para agentes de IA

Oi Fabio,

Seu conteudo sobre fundamentos de CS e historia da computacao e exatamente o tipo
de profundidade que falta no espaco de IA. Isso me fez querer sua opiniao.

CEX e um cerebro de IA open-source que aplica o principio que voce viveu com Rails
-- convencao sobre configuracao -- ao mundo de agentes de IA:

- 300 tipos de artefatos tipados (como models e views no Rails, mas para outputs de IA)
- Pipeline de raciocinio obrigatorio de 8 passos (8F) -- nao opt-in
- 12 pilares de dominio (diretorio de convencoes -- voce nunca decide onde um arquivo vai)
- 4 runtimes: Claude, Codex, Gemini, Ollama

O que diferencia de LangChain/CrewAI: eles dao building blocks. CEX da uma fabrica
com convencoes. Voce foca no WHAT, o sistema cuida do HOW.

Acho que voce teria uma opiniao forte -- e provavelmente diria o que esta errado,
que e exatamente o que precisamos.

Topa trocar uma ideia?

Gato3
github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM (@AkitaOnRails) or email

**Timing:** Mid-week. His videos drop weekly -- avoid the day after a new video (he is busy with comments).

**Risk/anti-pattern:** Akita is known for being blunt and critical. This is exactly what CEX needs. Per playbook: "Acknowledge valid criticism, provide data, move on." His honest critique is worth 10 polite compliments.

---

### #10. Rafael Milagre

| Field | Value |
|-------|-------|
| CRM # | 116 |
| Region | BR |
| Tier | T2 (100K-1M) |
| Platform | YouTube (100K+), Instagram, Twitter, LinkedIn, Podcast, Newsletter |
| Handle | Viver de IA / @rafaelmilagre |
| Followers | 100K+ (YT), 40K+ (IG), 15K+ (X), 20K+ (LI) |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 9 |
| Content Type | AI for business, mentoring, ESPM professor |
| Posting Frequency | weekly |

**Why he matters for CEX:** Largest AI education platform in Brazil ("Viver de IA"). ESPM professor. His audience is the Brazilian professional who wants to use AI in their business -- the exact audience for CEX's "5 words in, professional artifact out" value proposition. Multi-platform presence amplifies any mention.

**Template to use:** T2-X-BR (Twitter/X DM, PT-BR)

**Personalization notes:** Reference "Viver de IA" and its focus on making AI practical for business. CEX's GDP (Guided Decision Protocol) is exactly what his audience needs -- it separates "what to build" (user decides) from "how to build" (AI decides). This maps to his teaching approach.

**Recommended message:**

```
Oi Rafael -- vi que o Viver de IA esta cobrindo ferramentas praticas de IA para
negocios. Achei muito relevante.

Acabamos de lancar o CEX em open-source -- um cerebro de IA tipado com 300 tipos
de artefatos, pontuacao de qualidade obrigatoria, e suporte a 4 runtimes.

O que acho que sua audiencia iria curtir: voce digita 5 palavras e sai um artefato
profissional -- pontuado, compilado, versionado. Nao precisa saber prompt engineering.
O sistema cuida da parte tecnica. E o pipeline e visivel -- da pra ver cada passo.

Posso compartilhar acesso antecipado ou uma demo rapida pra voce avaliar?
Interessa?

github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM (@rafaelmilagre)

**Timing:** Weekday, Brazilian business hours.

**Risk/anti-pattern:** His audience is more business-focused than developer-focused. Frame the message around practical outcomes (artifacts, quality scores) rather than architecture (8F, pillars).

---

### #11. Fireship (Jeff Delaney)

| Field | Value |
|-------|-------|
| CRM # | 9 |
| Region | GLOBAL |
| Tier | T1 (1M+) |
| Platform | YouTube |
| Handle | Jeff Delaney / Fireship |
| Followers | 4.06M |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 8 |
| Content Type | Dev tools, 100-sec explainers, Code Report |
| Posting Frequency | daily |

**Why he matters for CEX:** The single largest developer-focused YouTube channel that covers actual dev tools. His "100 seconds of X" and Code Report formats are perfectly suited for CEX demo. The 8F pipeline trace running live is inherently visual and demo-able -- exactly what his format needs.

**Template to use:** T1-YT-EN (YouTube collab pitch)

**Personalization notes:** Reference his Code Report series. Propose the hook: "I gave this AI brain 5 words and it built a full artifact." The 8F trace running live is visual content gold. Side-by-side 4-runtime comparison (same command on Claude vs Ollama) is the kind of content his audience loves.

**Recommended message:**

```
Subject: Collab idea: "I gave this AI brain 5 words and it built a production artifact"

Hi Jeff,

Your Code Report series consistently covers what actually matters in dev tooling.
The way you explained agent frameworks made me think you would genuinely enjoy
tearing apart our architecture.

We built CEX, an open-source AI brain that is fundamentally different from every
agent framework on the market. Here is the hook for a potential video:

"I gave this AI brain 5 words and it produced a quality-scored artifact."

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

MIT licensed, pre-launch, not selling anything.

Gato3
github.com/gato3/cex
```

**Outreach channel:** Email (business email from YouTube about page) or DM

**Timing:** Mid-week. His content schedule is daily -- early week pitch gets considered for the following week.

**Risk/anti-pattern:** T1 contacts are the hardest to reach. Low response probability but extreme upside. Per playbook: "Direct outreach to developer contacts (60% conversion rate)" applies to personal network, not cold outreach. Expect 5-10% response rate. One attempt, then follow-up sequence (FU-NR). Do NOT spam.

---

### #12. sentdex (Harrison Kinsley)

| Field | Value |
|-------|-------|
| CRM # | 19 |
| Region | GLOBAL |
| Tier | T1 (1M+) |
| Platform | YouTube |
| Handle | Harrison Kinsley / sentdex |
| Followers | 1.4M |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 8 |
| Content Type | Python, ML programming |
| Posting Frequency | weekly |

**Why he matters for CEX:** The original Python ML educator on YouTube. His audience is the Python developer who builds ML projects -- the exact technical profile that would adopt CEX. He programs live, shows real code, and values practical tools. CEX's Python SDK and 150 tools are directly relevant to his content style.

**Template to use:** T1-X-EN (Twitter/X DM) or T1-EM-EN (Email)

**Personalization notes:** Reference his Python ML tutorials. Position CEX as a tool a Python developer would actually use -- not a theoretical framework. The 144 Python tools, the CLI interface, and the typed artifact output are all things he can demo live.

**Recommended message:**

```
Hey Harrison,

Your Python ML tutorials are what got half the ML community started. Your recent
work on practical AI tools connects to something we just shipped.

We built CEX -- an open-source AI brain with 300 typed knowledge artifacts, a
mandatory reasoning pipeline, and multi-runtime support (Claude, Gemini, Codex,
Ollama). It is a Python project -- 150 tools, full CLI, typed artifacts that
live in your git repo.

The part I think you would find most interesting: the 8F reasoning pipeline runs
live and produces a visible trace. Every output is quality-scored (9.0 target).
You can literally watch the system reason through each step.

Would you be open to a 10-minute async demo? I can send a 2-minute video or a
live walkthrough.

No strings. Just looking for technical feedback from someone who actually
builds things.

Gato3
github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM or email

**Timing:** Weekday, during US business hours.

**Risk/anti-pattern:** Same T1 caution as Fireship. Low response probability, high upside. One clean attempt, follow-up sequence, then move on.

---

### #13. Amjad Masad

| Field | Value |
|-------|-------|
| CRM # | 29 |
| Region | GLOBAL |
| Tier | T1 (1M+) |
| Platform | Twitter/X |
| Handle | @aabormasad |
| Followers | 150K+ |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 8 |
| Content Type | AI coding, Replit |
| Posting Frequency | daily |

**Why he matters for CEX:** CEO of Replit. He is building AI-native coding infrastructure -- exactly the space CEX inhabits. Replit Agent is a competitor in the "AI builds things" space, but CEX's typed knowledge approach is architecturally distinct. His daily engagement on AI coding topics means he is reachable.

**Template to use:** T2-X-EN (Twitter/X DM)

**Personalization notes:** Reference Replit Agent and how CEX takes a different approach -- typed artifacts vs code generation. Position as architectural conversation between two people building AI infrastructure.

**Recommended message:**

```
Hey Amjad -- what you are building with Replit Agent shows AI can generate real
code. We took a different angle: what if AI generated typed knowledge artifacts
instead?

CEX is an open-source AI brain with 300 artifact kinds, mandatory quality scoring
(9.0 target), and 4-runtime support (Claude/Gemini/Codex/Ollama). Every output
is typed, scored, compiled, and version-controlled.

The 8F reasoning pipeline is the part I think you would find most interesting --
it is mandatory, quality-gated, and produces a visible trace.

Happy to share early access or just a quick demo. Interested?

github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM

**Timing:** He posts daily -- any weekday works. Morning US time.

**Risk/anti-pattern:** He is building a competitor. Frame as architectural conversation, not competition. If he ignores it, do not follow up aggressively.

---

### #14. Rowan Cheung

| Field | Value |
|-------|-------|
| CRM # | 43 |
| Region | GLOBAL |
| Tier | T2 (100K-1M) |
| Platform | Twitter/X |
| Handle | @rowancheung |
| Followers | 567K (X), 2M+ newsletter (The Rundown AI) |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 8 |
| Content Type | AI newsletter, weekly tools coverage |
| Posting Frequency | daily |

**Why he matters for CEX:** The Rundown AI has 2M+ subscribers -- one of the largest AI newsletters. He covers AI tools daily. A feature in The Rundown reaches an audience that actively evaluates new AI tools. His engagement rate is HIGH, meaning his audience actually reads and acts on his recommendations.

**Template to use:** T2-X-EN (Twitter/X DM) or T3-NL-EN (Newsletter feature pitch)

**Personalization notes:** Reference his recent coverage of AI tools/frameworks. Position CEX as a new category ("typed knowledge system") rather than another agent framework -- this gives him a fresh angle for his newsletter.

**Recommended message:**

```
Hey Rowan -- saw your coverage of AI tools in The Rundown. Your audience is
exactly who would care about this.

We just open-sourced CEX -- a typed AI brain with 300 artifact kinds, mandatory
quality scoring, and 4-runtime support (Claude/Gemini/Codex/Ollama).

The key differentiator from every framework you have covered: typed knowledge.
Every output has a schema, a quality score (9.0 target), and lives in your git
repo. Intelligence compounds. No other framework does this.

Happy to provide a 200-word feature blurb, screenshots, or a demo for your team.

github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM (primary), email (backup for newsletter pitch)

**Timing:** Early week (Mon-Tue). Newsletter planning happens early.

**Risk/anti-pattern:** Newsletter features require traction. Wait until post-launch with at least 100+ stars before pitching.

---

### #15. Francois Chollet

| Field | Value |
|-------|-------|
| CRM # | 44 |
| Region | GLOBAL |
| Tier | T2 (100K-1M) |
| Platform | Twitter/X |
| Handle | @fchollet |
| Followers | 566K |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 8 |
| Content Type | Keras, ARC-AGI, typed systems advocacy |
| Posting Frequency | weekly |

**Why he matters for CEX:** Creator of Keras -- the most developer-friendly deep learning library. CRM notes he is a "typed systems advocate." ARC-AGI benchmark creator. He fundamentally cares about structured, typed approaches to AI -- CEX's 300-kind taxonomy is exactly the kind of architectural decision he would have an opinion on.

**Template to use:** T2-X-EN (Twitter/X DM) or GitHub issue/discussion

**Personalization notes:** Reference Keras's design philosophy (developer experience, typed APIs) and how CEX applies the same principle to AI output. His ARC-AGI work on measuring intelligence is connected to CEX's 8F quality governance -- both are about measuring AI output quality.

**Recommended message:**

```
Hey Francois -- Keras showed that typed, developer-friendly APIs can be the
winning abstraction for ML. We applied the same principle to AI agent output.

CEX is an open-source AI brain with 300 typed artifact kinds (schema per kind),
mandatory quality scoring (9.0 target), and an 8-step reasoning pipeline that
governs every output. 4 runtimes: Claude, Gemini, Codex, Ollama.

Your ARC-AGI work on measuring intelligence resonates with our F7 GOVERN step --
both are about structured evaluation of AI output, not vibes.

Would love your take on whether typed knowledge taxonomies solve a real problem.

github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM or GitHub

**Timing:** He posts weekly. Mid-week engagement.

**Risk/anti-pattern:** He is opinionated and may disagree with the approach publicly. Welcome it. His critique will make CEX better and bring attention.

---

### #16. Paul Gauthier (Aider)

| Field | Value |
|-------|-------|
| CRM # | 209 |
| Region | GLOBAL |
| Tier | T3 (GitHub) |
| Platform | GitHub |
| Handle | paul-gauthier |
| Project | Aider (30K+ stars) |
| Relevance | HIGH |
| Priority Score | 9 |
| Content Type | AI pair programming |

**Why he matters for CEX:** Creator of Aider -- the leading AI pair programming tool. CEX and Aider operate in adjacent spaces (AI-assisted development), and his audience understands CLI-based AI tools. A mention or comparison from him reaches the exact developer who values terminal-based AI workflows.

**Template to use:** T4-OSS-EN (Open-source contributor invitation) or T2-EM-EN (Email)

**Personalization notes:** Reference Aider's approach to AI pair programming and how CEX extends the concept from "AI helps you code" to "AI produces governed knowledge artifacts." The git-based workflow (artifacts in your repo) is a shared design philosophy.

**Recommended message:**

```
Hi Paul,

Aider showed that AI pair programming works best as a CLI tool that respects
your git workflow. We built on a similar philosophy.

CEX is an open-source AI brain (MIT) where every output is a typed knowledge
artifact that lives in your git repo. 300 artifact kinds, mandatory quality
scoring (9.0 target), and a reasoning pipeline that produces a visible trace.
Runs on Claude, Codex, Gemini, or Ollama.

The shared design philosophy: git is the source of truth. AI is a tool, not a
platform. The user's repo is sovereign.

Would love your architectural take -- especially on how typed artifacts compare
to Aider's code-generation approach.

Gato3
github.com/gato3/cex
```

**Outreach channel:** GitHub (star + issue/discussion), email

**Timing:** He is active on GitHub. Any weekday.

**Risk/anti-pattern:** None significant. OSS maintainers are generally open to architectural conversations from peer projects.

---

### #17. Zain Kahn

| Field | Value |
|-------|-------|
| CRM # | 124 |
| Region | GLOBAL |
| Tier | T2 (100K-1M) |
| Platform | Twitter/X, LinkedIn, Newsletter |
| Handle | @zainkahn (X), Superhuman AI (Newsletter) |
| Followers | 80K+ (X), 1M+ (LI), 1M+ (newsletter subs) |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 9 |
| Content Type | AI newsletter, business applications |
| Posting Frequency | daily |

**Why he matters for CEX:** Superhuman AI newsletter has 1M+ subscribers. Cross-platform presence (Twitter + LinkedIn + newsletter) means a single positive take cascades. His audience is the professional who uses AI tools for business -- exactly the audience for CEX's "5 words in, professional artifact out" pitch.

**Template to use:** T2-X-EN (Twitter/X DM) combined with T3-NL-EN (Newsletter pitch)

**Personalization notes:** Reference Superhuman AI's tool coverage. Position CEX as a new category worthy of newsletter feature -- typed knowledge system vs yet-another-agent-framework.

**Recommended message:**

```
Hey Zain -- Superhuman AI consistently covers the tools that matter. I think
your audience would find this genuinely different from anything you have featured.

CEX is an open-source AI brain with 300 typed artifact kinds, mandatory quality
scoring (9.0 target), and 4-runtime support. The key difference from every
framework: typed knowledge that compounds in your git repo.

Practical demo: "/build landing_page" produces a complete, quality-gated artifact
in seconds. No prompt engineering needed.

Happy to provide a feature blurb, demo video, or early access for your team.

github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM (primary), LinkedIn message (backup)

**Timing:** Early week (Mon-Tue) for newsletter planning.

**Risk/anti-pattern:** Same as Rowan Cheung -- newsletter features require traction. Wait for post-launch.

---

### #18. Programacao Dinamica

| Field | Value |
|-------|-------|
| CRM # | 94 |
| Region | BR |
| Tier | T2 (100K-1M) |
| Platform | YouTube (150K+), Instagram |
| Handle | Programacao Dinamica |
| Followers | 150K+ (YT), 12K+ (IG) |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 8 |
| Content Type | CS, algorithms, Python |
| Posting Frequency | weekly |

**Why she/they matter for CEX:** Academic-quality CS content. The CRM notes "ideal audience." Their Python + algorithms focus means their audience has the technical depth to actually understand and use CEX's typed knowledge system. The academic rigor aligns with CEX's 8F pipeline formalization.

**Template to use:** T2-X-BR (Twitter/X DM, PT-BR)

**Personalization notes:** Reference their CS fundamentals content. The 8F pipeline can be explained as a formal state machine -- their audience would appreciate the computer science underpinning.

**Recommended message:**

```
Oi -- acompanho o Programacao Dinamica pelo conteudo de CS com profundidade
academica real. Isso me fez pensar que voces teriam uma opiniao forte sobre
o que estamos construindo.

CEX e um cerebro de IA open-source onde cada saida e um artefato tipado -- 300
tipos com schema, pipeline de raciocinio de 8 passos (F1-F8), pontuacao de
qualidade obrigatoria. Roda em Python, MIT license.

A parte CS: o pipeline 8F e essencialmente uma maquina de estados formal aplicada
a geracao de artefatos de IA. Cada passo tem pre-condicoes e pos-condicoes.

Acho que seria um topico interessante pra vocês -- "convencao sobre configuracao
para agentes de IA." Posso compartilhar uma demo?

github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM or YouTube comment

**Timing:** Mid-week. They post weekly.

**Risk/anti-pattern:** Academic audience values rigor. Do not oversell. Let the architecture speak. Be prepared for hard technical questions.

---

### #19. Erick Wendel

| Field | Value |
|-------|-------|
| CRM # | 117 |
| Region | BR |
| Tier | T2 (100K-1M) |
| Platform | YouTube (100K+), Twitter (30K+), Instagram (20K+) |
| Handle | Erick Wendel / @erickwendel_ |
| Followers | 100K+ (YT), 30K+ (X), 20K+ (IG) |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 8 |
| Content Type | Advanced JS, Node.js |
| Posting Frequency | weekly |

**Why he matters for CEX:** Deep technical content creator and conference speaker. His JS/Node audience is the builder audience -- people who write production code. While CEX is Python-based, the architectural concepts (typed systems, quality gates, convention-over-configuration) are language-agnostic and his audience values technical depth.

**Template to use:** T2-X-BR (Twitter/X DM, PT-BR)

**Personalization notes:** Reference his conference talks and deep technical content. Frame CEX's 8F pipeline as an engineering discipline applied to AI -- something his engineering-minded audience would appreciate.

**Recommended message:**

```
Oi Erick -- seu conteudo tecnico avancado e talks em conferencia mostram que voce
se importa com engenharia de software feita direito. Isso me fez querer sua
opiniao.

CEX e um cerebro de IA open-source que aplica disciplina de engenharia a output
de IA: 300 tipos de artefatos tipados, pipeline de raciocinio obrigatorio de 8
passos, pontuacao de qualidade (meta 9.0). Roda em 4 runtimes -- sem lock-in.

A parte que acho que voce ia curtir: quality gates obrigatorios. Nada publica
abaixo de 8.0/10. E uma abordagem de engenharia, nao de prompt.

Topa uma demo? Posso mandar video ou fazer ao vivo.

github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM (@erickwendel_)

**Timing:** Mid-week, Brazilian business hours.

**Risk/anti-pattern:** None significant. He is known for being technically curious and generous with feedback.

---

### #20. Eduardo Mendes (Dunossauro)

| Field | Value |
|-------|-------|
| CRM # | 119 |
| Region | BR |
| Tier | T2 (100K-1M) |
| Platform | YouTube (100K+), Instagram, Twitter |
| Handle | Dunossauro / @dunossauro |
| Followers | 100K+ (YT) |
| Engagement | HIGH |
| Relevance | HIGH |
| Priority Score | 8 |
| Content Type | Python, FastAPI, open-source contribution |
| Posting Frequency | weekly |

**Why he matters for CEX:** Live de Python host. Open-source contributor. His audience is the Brazilian Python developer who contributes to OSS -- the exact profile of a CEX early contributor. "Live de Python" is a live-coding format that would be perfect for a CEX walkthrough.

**Template to use:** T2-X-BR (Twitter/X DM, PT-BR)

**Personalization notes:** Reference "Live de Python" and his OSS contributions. CEX is a Python project (150 tools, full SDK). Position as both a tool to use AND an OSS project to contribute to. Specific contribution opportunity: Python SDK improvements, FastAPI integration for CEX API endpoints.

**Recommended message:**

```
Oi Eduardo -- acompanho o Live de Python e suas contribuicoes open-source.
Exatamente o tipo de pessoa que gostaria de ter olhando nosso projeto.

CEX e um cerebro de IA open-source em Python (150 tools, SDK completo, licenca
MIT) com 300 tipos de artefatos tipados e pipeline de raciocinio de 8 passos.

Alem de usar, estamos buscando contribuidores Python -- especificamente alguem
com experiencia em FastAPI (pra endpoints de API do CEX) e em tooling Python
(cex_sdk tem 100+ modulos).

Se quiser, posso te dar um tour pelo codebase ou ate fazer uma sessao ao vivo
pra sua comunidade. "Live de CEX" -- seria um episodio interessante.

github.com/gato3/cex
```

**Outreach channel:** Twitter/X DM or YouTube comment

**Timing:** Mid-week. He does live streams -- check his schedule and reach out before a stream, not during.

**Risk/anti-pattern:** He is an OSS contributor -- he will look at the code quality, not just the pitch. Make sure the repo is clean, documented, and has "Good First Issue" labels before reaching out.

---

## Honorable Mentions (Priority 8, Not in Top 20)

These contacts also scored 8+ but were deprioritized for Wave 1 due to lower response probability (orgs vs individuals), platform fit, or strategic sequencing. Target for Wave 2.

| CRM # | Name | Score | Why Wave 2 |
|-------|------|-------|------------|
| 52 | Nate Herk | 8 | YouTube focus; needs demo video ready first |
| 67 | Yannic Kilcher | 8 | ML paper reviews; need a "CEX architecture paper" before pitching |
| 78 | Soumith Chintala | 8 | PyTorch co-founder; very high profile, lower response probability |
| 97/128 | Jeremy Howard | 8 | fast.ai founder; needs educational framing, prepare tutorial first |
| 105 | Data Chaz | 8 | Streamlit advocate; prepare Streamlit integration demo first |
| 112 | Matt Wolfe | 8 | futuretools.io; needs launch traction (100+ stars) first |
| 113 | Matthew Berman | 8 | LLM coverage; needs launch traction first |
| 114 | AI Explained | 8 | Signal-over-noise; prepare deep architecture doc first |
| 115 | David Shapiro | 8 | AGI deep dives; prepare autonomous evolution demo first |
| 123 | Theo Browne | 8 | T3 stack creator; prepare TypeScript angle or dismiss as non-fit |
| 166 | Sebastian Raschka | 8 | Lightning AI; prepare research comparison first |
| 170 | Alessio Fanelli | 8 | Latent Space co-host; reach through Swyx (contact #6 above) |
| 171 | Nathan Labenz | 8 | Cognitive Revolution host; prepare podcast pitch deck first |
| 172 | Peter Steinberger | 8 | OpenClaw, now at OpenAI; interesting but complicated affiliation |
| 211+ | GitHub maintainers | 8-9 | Ollama, MCP, Dify, OpenHands etc; target after repo is polished |

---

## Week 1 Action Plan

Five contacts for the first week of outreach. Selected for: highest response probability, builder identity (they make things, not just comment), and amplification potential within the agent/OSS community.

### Day 1 (Monday): Danilo Gato

- **Action:** Send Twitter/X DM in PT-BR (message above)
- **Pre-work:** Check his last 3 tweets/posts. Add specific reference to his most recent AI tool coverage in `{{RECENT_CONTENT_REFERENCE}}`
- **Expected response time:** 1-3 days (daily poster, highly engaged)
- **If no response by Day 5:** Send FU-NR Touch 1 with 90-second demo link

### Day 2 (Tuesday): Simon Willison

- **Action:** Reply to one of his recent Twitter threads with a genuine technical comment that references CEX's typed approach (message above). Do NOT cold DM first -- earn attention via public reply.
- **Pre-work:** Find a thread where he discusses structured LLM output, CLI tools, or agent frameworks. Reply there. If no suitable thread exists within last 7 days, wait and monitor.
- **Expected response time:** 1-2 days if the thread is relevant (he replies to thoughtful comments)
- **If no response by Day 7:** Send a direct DM referencing the public reply

### Day 3 (Wednesday): Yohei Nakajima

- **Action:** Send Twitter/X DM in EN (message above)
- **Pre-work:** Check his recent tweets about agent architectures. Reference specific BabyAGI design decisions.
- **Expected response time:** 3-5 days (weekly poster)
- **If no response by Day 8:** Send FU-NR Touch 1

### Day 4 (Thursday): Fabio Akita

- **Action:** Send Twitter/X DM in PT-BR (message above)
- **Pre-work:** Watch his most recent video. Reference a specific point he made about CS fundamentals or software architecture. The Rails connection is the hook -- but it needs to feel natural, not forced.
- **Expected response time:** 3-7 days (weekly poster)
- **If no response by Day 10:** Send FU-NR Touch 1 with demo link

### Day 5 (Friday): Joao Moura

- **Action:** Send Twitter/X DM in PT-BR (message above)
- **Pre-work:** Check CrewAI's recent releases/tweets. Reference something specific about their crew architecture. Frame as architectural dialogue.
- **Expected response time:** 3-7 days
- **If no response by Day 10:** Send FU-NR Touch 1
- **Special note:** If he responds positively, this unlocks the entire BR agent-framework community. Prioritize this relationship.

### Week 1 Rules

1. **Maximum 1 outreach per day.** Quality over quantity. Per playbook: "Maximum 10 personalized messages per day" -- we are doing 5 per week, which is conservative and sustainable.
2. **5 minutes of research per contact before sending.** Check their last 3 posts. Fill in `{{RECENT_CONTENT_REFERENCE}}` with something specific. Generic messages get deleted.
3. **Respond to any reply within 4 hours.** First response speed is everything. Per LangChain playbook: "Founder personally responded to GitHub issues in first 6 months."
4. **Log every outreach in CRM.** Update `outreach_status` from `not_started` to `contacted` with date and channel.
5. **Do NOT send Week 2 outreach until Week 1 follow-ups are complete.** Build relationships, do not spray.

---

## Outreach Sequence Summary (Weeks 1-4)

| Week | Contacts | Rationale |
|------|----------|-----------|
| 1 | #1 Danilo Gato, #2 Simon Willison, #3 Yohei Nakajima, #9 Fabio Akita, #5 Joao Moura | Builders + BR anchors. Highest response probability. |
| 2 | #6 Swyx, #4 Harrison Chase, #8 Filipe Deschamps, #16 Paul Gauthier, #15 Francois Chollet | Newsletter/framework founders. Needs traction from Week 1. |
| 3 | #7 Rocketseat, #10 Rafael Milagre, #14 Rowan Cheung, #17 Zain Kahn, #18 Prog. Dinamica | Education + newsletters. Needs demo video ready. |
| 4 | #11 Fireship, #12 sentdex, #13 Amjad Masad, #19 Erick Wendel, #20 Eduardo Mendes | T1 YouTube + remaining BR builders. Needs 100+ stars. |

---

## Pre-Outreach Checklist (from Seeding Playbook)

Before sending ANY message from this brief, verify:

| Item | Status | Notes |
|------|--------|-------|
| README has 1-sentence value prop above fold | REQUIRED | "5 words in. Professional artifact out. Intelligence compounds." |
| Demo GIF showing `/build landing_page` (30 sec) | REQUIRED | Record with asciinema; show 8F trace |
| 3-line Quick Start in README | REQUIRED | Clone, init, build |
| Badge wall (license, version, CI) | REQUIRED | MIT, Python, build status |
| Discord server created and structured | REQUIRED | #general, #showcase, #help, #pt-br |
| Comparison table vs LangChain/CrewAI in README | REQUIRED | 5-row table from positioning statement |
| GitHub topics set | REQUIRED | ai-agents, llm, typed-system, python, claude, ollama |
| Repo is public | REQUIRED | Cannot outreach to a private repo |

**Do NOT send outreach until ALL items above are DONE.**

---

## Sources

| Source | Path |
|--------|------|
| CRM | N06_commercial/P01_knowledge/kc_influencer_crm_unified.md |
| Templates | N02_marketing/P03_prompt/tpl_outreach_messages.md |
| Positioning | N02_marketing/P03_prompt/kc_cex_positioning_statement.md |
| Playbook | N02_marketing/P01_knowledge/kc_seeding_playbook.md |
