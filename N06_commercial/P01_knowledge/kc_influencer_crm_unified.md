---
id: kc_influencer_crm_unified
kind: knowledge_card
pillar: P01
nucleus: n06
domain: influencer-crm
version: 1.0.0
created: 2026-04-24
quality: null
tags: [seed-intel, crm, influencer, outreach]
tldr: "Unified CRM of 714 tech/AI influencers (Global + BR) tiered for CEX open-source seeding outreach, deduplicated"
---

# Unified Influencer CRM -- CEX Open-Source Seeding

> 714 contact entries | 2 regions (GLOBAL / BR) | 4 tiers (T1-T4) | 16-field CRM schema
> Merged from: kc_influencer_directory_global.md (385) + kc_influencer_directory_br.md (353), deduplicated 24 cross-platform/cross-section entries
> Relevance scoring informed by: cm_cex_vs_landscape.md + kc_cex_positioning_analysis.md
> Data freeze: 2026-04-24

---

## 1. CRM Schema

Every contact in this CRM follows a 16-field schema. Fields are populated where data is
available; empty fields are marked `--` for future enrichment.

| # | Field | Type | Description |
|---|-------|------|-------------|
| 1 | name | string | Full name or handle (person or org) |
| 2 | region | enum | `GLOBAL` or `BR` |
| 3 | tier | enum | `T1` (1M+), `T2` (100K-1M), `T3` (10K-100K), `T4` (micro <10K) |
| 4 | platform | string | Primary platform (Twitter/X, YouTube, GitHub, LinkedIn, Newsletter, Podcast, Discord, Reddit, Telegram, Instagram, Conference, Academic) |
| 5 | handle | string | Primary handle or URL |
| 6 | followers | string | Approximate follower/subscriber count on primary platform |
| 7 | engagement_estimate | enum | `HIGH` (>3% rate or niche authority), `MEDIUM` (1-3%), `LOW` (<1% or broadcast-only) |
| 8 | content_type | string | Primary content focus |
| 9 | posting_frequency | enum | `daily`, `weekly`, `biweekly`, `irregular`, `--` (unknown) |
| 10 | relevance_to_cex | enum | `HIGH` (typed systems, multi-agent, OSS AI, agent frameworks), `MEDIUM` (AI tools, dev workflows, LLM apps), `LOW` (general AI/tech news) |
| 11 | contact_method | string | Preferred outreach channel |
| 12 | outreach_status | enum | `not_started` (all entries initialized here) |
| 13 | priority_score | int (1-10) | Composite of relevance x reach x engagement x platform_fit for CEX seeding |
| 14 | notes | string | Key context for outreach personalization |
| 15 | last_updated | date | `2026-04-24` (initial load) |
| 16 | cross_ref | string | Other directories or platforms where this contact appears |

### Priority Score Formula

```
priority_score = (relevance_weight x 4) + (tier_weight x 3) + (engagement_weight x 2) + (platform_fit x 1)

relevance_weight:  HIGH=3, MEDIUM=2, LOW=1
tier_weight:       T1=3, T2=2, T3=1, T4=0.5
engagement_weight: HIGH=3, MEDIUM=2, LOW=1
platform_fit:      GitHub=3, Twitter=2.5, YouTube=2, Newsletter=2, Podcast=2, Discord=2, Reddit=1.5, LinkedIn=1.5, Instagram=1, Conference=1.5, Academic=1
```

Score range: 1-10 (normalized). 10 = perfect CEX seeding target.

---

## 2. Tier Summary Dashboard

| Tier | Definition | Global Count | BR Count | Total | Primary Platforms |
|------|-----------|-------------|----------|-------|-------------------|
| T1 | 1M+ followers | 17 | 11 | 28 | YouTube, Twitter/X, Instagram, Podcast |
| T2 | 100K-1M | 76 | 48 | 124 | YouTube, Twitter/X, Newsletter, Instagram, LinkedIn |
| T3 | 10K-100K | 160 | 275 | 435 | Twitter/X, Instagram, LinkedIn, GitHub, YouTube, Telegram, Podcast, Conference, Academic |
| T4 | Micro (<10K) | 120 | 7 | 127 | GitHub, Discord, Reddit, Telegram, Community |
| **TOTAL** | | **373** | **341** | **714** |

### Relevance Distribution

| Relevance | Global | BR | Total | % of Total |
|-----------|--------|-----|-------|------------|
| HIGH | 193 | 223 | 416 | 56.4% |
| MEDIUM | 132 | 107 | 239 | 32.4% |
| LOW | 60 | 23 | 83 | 11.2% |

### Platform Distribution (Primary)

| Platform | Global | BR | Total |
|----------|--------|-----|-------|
| Twitter/X | 100 | 52 | 152 |
| YouTube | 68 | 55 | 123 |
| GitHub | 48 | 0 | 48 |
| Newsletter | 32 | 16 | 48 |
| Podcast | 28 | 22 | 50 |
| Conference/Speaker | 32 | 25 | 57 |
| Blog/Substack | 30 | 0 | 30 |
| Discord | 22 | 2 | 24 |
| Reddit | 18 | 0 | 18 |
| LinkedIn | 7 | 42 | 49 |
| Instagram | 0 | 62 | 62 |
| Telegram | 0 | 32 | 32 |
| Education Platform | 0 | 14 | 14 |
| Community Leader | 0 | 11 | 11 |
| Academic | 0 | 22 | 22 |

---

## 3. T1 Priority Contacts (1M+ followers)

These are the highest-reach targets. Every contact has potential to generate thousands of GitHub stars with a single post or mention.

| # | Name | Region | Tier | Platform | Handle | Followers | Eng. | Content Type | Freq. | Relevance | Contact | Priority | Notes | Updated | Cross-Ref |
|---|------|--------|------|----------|--------|-----------|------|-------------|-------|-----------|---------|----------|-------|---------|-----------|
| 1 | Satya Nadella | GLOBAL | T1 | Twitter/X | @satyanadella | 5M+ | LOW | AI innovation, Microsoft | weekly | LOW | PR | 3 | CEO Microsoft; mentions drive mass awareness | 2026-04-24 | -- |
| 2 | Sam Altman | GLOBAL | T1 | Twitter/X | @sama | 4.2M | MEDIUM | AI leadership, OpenAI | daily | LOW | PR/media | 3 | OpenAI CEO; competitor ecosystem | 2026-04-24 | -- |
| 3 | Lex Fridman | GLOBAL | T1 | YouTube | Lex Fridman | 5.0M | HIGH | AI interviews, deep tech | weekly | LOW | Podcast pitch | 4 | MIT researcher, top AI podcast; also 4.2M on Twitter/X @lexfridman | 2026-04-24 | X #3 |
| 4 | Manual do Mundo | BR | T1 | YouTube | Ibere Thenorio | 15M+ | HIGH | Science, tech, AI demos | weekly | MEDIUM | PR | 5 | Mainstream science; occasional AI content | 2026-04-24 | -- |
| 5 | Leon Martins (Coisa de Nerd) | BR | T1 | YouTube | Leon Martins | 11.1M | HIGH | Tech, science, pop culture | weekly | MEDIUM | PR (AMMA) | 5 | Also 2.2M IG; iBest finalist; wife Nilce co-hosts | 2026-04-24 | IG #57 |
| 6 | 3Blue1Brown | GLOBAL | T1 | YouTube | Grant Sanderson | 8.2M | HIGH | Math/ML visualization | biweekly | MEDIUM | Email | 5 | Best math explainer on YouTube | 2026-04-24 | -- |
| 7 | Thiago Augusto (Jornada Top) | BR | T1 | Instagram | @jornada.top | 8M | HIGH | Tech innovation | daily | MEDIUM | DM | 5 | Also 1.41M YT (Jornada Top channel); iBest finalist; merged from YT #22 | 2026-04-24 | YT #22, IG #56 |
| 8 | Fireship | GLOBAL | T1 | YouTube | Jeff Delaney | 4.06M | HIGH | Dev tools, 100-sec explainers | daily | HIGH | DM/email | 8 | Code Report; fast-paced dev content; ideal for CEX demo | 2026-04-24 | -- |
| 10 | Gesiel Taveira | BR | T1 | YouTube | Gesiel Taveira | 4.36M | HIGH | Tech reviews, innovation | weekly | MEDIUM | DM | 5 | Also 371K IG; 10+ years on YT | 2026-04-24 | IG #62 |
| 11 | TecMundo | BR | T1 | YouTube | TecMundo | 3.8M | HIGH | Tech news, hardware | daily | MEDIUM | PR | 4 | Part of NZN network; since 2005 | 2026-04-24 | NL #271 |
| 12 | Canaltech | BR | T1 | YouTube | Canaltech | 3.57M | HIGH | Tech news, reviews | daily | MEDIUM | PR | 4 | Founded by Felipe Szatkowski; also 529K IG | 2026-04-24 | IG #58, NL #272 |
| 13 | Two Minute Papers | GLOBAL | T1 | YouTube | K. Zsolnai-Feher | 1.77M | HIGH | AI research papers | weekly | MEDIUM | Email | 5 | TU Wien researcher; great for typed-system narrative | 2026-04-24 | -- |
| 14 | Allie K. Miller | GLOBAL | T1 | Twitter/X | @alliekmiller | 1.5M | MEDIUM | AI business applications | daily | MEDIUM | DM/LinkedIn | 5 | #1 AI Business Voice, ex-Amazon/IBM | 2026-04-24 | -- |
| 15 | Corey Schafer | GLOBAL | T1 | YouTube | Corey Schafer | 1.5M | HIGH | Python, dev tutorials | irregular | MEDIUM | Email | 5 | Software dev educator | 2026-04-24 | -- |
| 16 | Andrej Karpathy | GLOBAL | T1 | Twitter/X | @karpathy | 1.4M | HIGH | AI education, neural nets, LLMs | weekly | MEDIUM | DM/email | 6 | Ex-Tesla AI Dir, OpenAI founding team, Eureka Labs | 2026-04-24 | Speaker #300 |
| 17 | Kai-Fu Lee | GLOBAL | T1 | Twitter/X | @kaifulee | 1.4M | LOW | AI strategy, Asia markets | weekly | LOW | PR/media | 3 | CEO 01.ai, ex-Google China | 2026-04-24 | -- |
| 18 | Krish Naik | GLOBAL | T1 | YouTube | Krish Naik | 1.4M | HIGH | ML/DL/CV education | daily | MEDIUM | DM/email | 5 | AI educator India | 2026-04-24 | -- |
| 19 | sentdex | GLOBAL | T1 | YouTube | Harrison Kinsley | 1.4M | HIGH | Python, ML programming | weekly | HIGH | DM/email | 8 | Python ML tutorials; ideal audience for CEX | 2026-04-24 | -- |
| 20 | Gustavo Guanabara (Curso em Video) | BR | T1 | YouTube | Guanabara | 1M+ | HIGH | Free programming courses | weekly | MEDIUM | DM/Email | 5 | 20+ years teaching; massive beginner reach | 2026-04-24 | Edu #335 |
| 21 | Rocketseat (Diego Fernandes) | BR | T1 | YouTube | Rocketseat | 1M+ | HIGH | React, Node, fullstack, AI | daily | HIGH | DM/Email | 9 | Co-founder/CTO; 55K+ students; covers AI tooling | 2026-04-24 | IG #77, LI #174 |
| 23 | John Carmack | GLOBAL | T1 | Twitter/X | @ID_AA_Carmack | 1.1M | MEDIUM | AGI research, engineering | irregular | LOW | Email | 3 | AGI at Keen Technologies | 2026-04-24 | -- |
| 24 | Andrew Ng | GLOBAL | T1 | Twitter/X | @AndrewYNg | 1.1M | MEDIUM | AI education, ML courses | weekly | MEDIUM | Coursera/DeepLearning.AI | 5 | Co-founder Coursera, Stanford | 2026-04-24 | NL #222 |
| 25 | Tina Huang | GLOBAL | T1 | YouTube | Tina Huang | 1.0M+ | HIGH | AI, data science, tech | weekly | MEDIUM | DM/email | 5 | Ex-Meta data scientist | 2026-04-24 | -- |
| 26 | NerdCast | BR | T1 | Podcast | Ottoni + Pazos | 10M+ downloads | HIGH | Nerd culture, tech | weekly | MEDIUM | PR | 5 | Largest podcast in BR | 2026-04-24 | -- |
| 27 | Greg Brockman | GLOBAL | T1 | Twitter/X | @gaborbrockman | 200K+ | LOW | OpenAI, ChatGPT | irregular | LOW | PR | 2 | Co-founder/President OpenAI | 2026-04-24 | -- |
| 28 | Reid Hoffman | GLOBAL | T1 | Twitter/X | @reidhoffman | 200K+ | LOW | AI strategy, investing | weekly | LOW | PR | 2 | LinkedIn founder | 2026-04-24 | Pod #263 |
| 29 | Amjad Masad | GLOBAL | T1 | Twitter/X | @aabormasad | 150K+ | HIGH | AI coding, Replit | daily | HIGH | DM | 8 | CEO Replit; covers AI coding tools | 2026-04-24 | -- |
| 30 | Yoshua Bengio | GLOBAL | T1 | Conference | Mila/U Montreal | -- | LOW | Deep learning, AI safety | irregular | LOW | Academic | 2 | Turing Award, ICML 2026 keynote | 2026-04-24 | -- |

---

## 4. T2 Priority Contacts (100K-1M)

| # | Name | Region | Tier | Platform | Handle | Followers | Eng. | Content Type | Freq. | Relevance | Contact | Priority | Notes | Updated | Cross-Ref |
|---|------|--------|------|----------|--------|-----------|------|-------------|-------|-----------|---------|----------|-------|---------|-----------|
| 31 | Yann LeCun | GLOBAL | T2 | Twitter/X | @ylecun | 972K | MEDIUM | Deep learning, open AI | daily | MEDIUM | Academic | 4 | Chief AI Scientist Meta, NYU | 2026-04-24 | -- |
| 32 | Augusto Backes | BR | T2 | YouTube | Augusto Backes | 900K | MEDIUM | Bitcoin, DeFi, tech | weekly | LOW | DM | 3 | Crypto-focused; tech-savvy audience | 2026-04-24 | X #150 |
| 33 | Lenny Rachitsky | GLOBAL | T2 | Newsletter | Lenny's Newsletter | 800K+ | HIGH | Product + AI intersection | weekly | MEDIUM | Substack | 5 | Product management + AI | 2026-04-24 | Pod #256 |
| 34 | Filipe Deschamps | BR | T2 | YouTube | Filipe Deschamps | 800K+ | HIGH | Tech news, OSS, curso.dev | daily | HIGH | Email | 9 | Largest BR tech newsletter; TabNews founder | 2026-04-24 | NL #266, X #121, Pod #248 |
| 35 | DeepMind | GLOBAL | T2 | YouTube | Google DeepMind | 854K | LOW | AI research videos | weekly | LOW | PR | 2 | Official Google DeepMind | 2026-04-24 | -- |
| 36 | Siraj Raval | GLOBAL | T2 | YouTube | Siraj Raval | 773K | MEDIUM | AI development | weekly | MEDIUM | DM | 4 | AI dev educator | 2026-04-24 | -- |
| 37 | Fabio Akita | BR | T2 | YouTube | Fabio Akita | 700K+ | HIGH | CS fundamentals, history | weekly | HIGH | DM | 9 | Deep technical content; respected in dev community | 2026-04-24 | X #122, IG #82 |
| 38 | Sean Gardner | GLOBAL | T2 | Twitter/X | @2morrowknight | 709K | LOW | AI, ML, ethics | weekly | LOW | DM | 2 | AI/ML thought leader | 2026-04-24 | -- |
| 39 | Skill Leap AI (Saj) | GLOBAL | T2 | YouTube | Saj Adib | 700K+ | HIGH | AI tool tutorials | daily | MEDIUM | DM/email | 6 | Fastest-growing AI tutorial channel | 2026-04-24 | -- |
| 40 | Ai Angel | GLOBAL | T2 | YouTube | Angelica | 672K | LOW | AI variety, tech | weekly | LOW | DM | 2 | Variety streamer | 2026-04-24 | -- |
| 41 | Programador BR | BR | T2 | YouTube | Igor Oliveira | 600K+ | MEDIUM | JavaScript, React, freelance | weekly | MEDIUM | DM | 4 | Freelance dev focus | 2026-04-24 | -- |
| 42 | DeepLearningAI | GLOBAL | T2 | YouTube | Andrew Ng team | 595K | MEDIUM | AI education, courses | weekly | MEDIUM | Email | 4 | Coursera ML programs | 2026-04-24 | -- |
| 43 | Rowan Cheung | GLOBAL | T2 | Twitter/X | @rowancheung | 567K | HIGH | AI newsletter, weekly | daily | HIGH | DM/email | 8 | The Rundown AI (2M+ subs); top newsletter | 2026-04-24 | NL #217 |
| 44 | Francois Chollet | GLOBAL | T2 | Twitter/X | @fchollet | 566K | HIGH | Keras, ARC-AGI | weekly | HIGH | GitHub/DM | 8 | Creator of Keras; typed systems advocate | 2026-04-24 | -- |
| 45 | Robert Scoble | GLOBAL | T2 | Twitter/X | @Scobleizer | 537K | MEDIUM | AI trends, tech | daily | MEDIUM | DM/LinkedIn | 4 | Ex-Microsoft, tech evangelist | 2026-04-24 | -- |
| 46 | Fei-Fei Li | GLOBAL | T2 | Twitter/X | @drfeifei | 516K | LOW | Computer vision, spatial AI | biweekly | LOW | Stanford HAI | 2 | Prof Stanford; Speaker #278 | 2026-04-24 | Speaker #278 |
| 47 | Cassie Kozyrkov | GLOBAL | T2 | Twitter/X | @quaesita | 100K+ (X), 500K+ (LI) | HIGH | Decision science, AI | weekly | MEDIUM | LinkedIn | 5 | Ex-Google Chief Decision Scientist | 2026-04-24 | LI #380 |
| 48 | Rafaella Ballerini | BR | T2 | YouTube | Rafaella Ballerini | 500K+ | HIGH | Frontend, career, beginner | weekly | MEDIUM | DM | 4 | Women in tech advocate | 2026-04-24 | IG #84, X #138 |
| 49 | Lucas Montano | BR | T2 | YouTube | Lucas Montano | 500K+ | HIGH | Career, mobile dev, market | weekly | MEDIUM | DM | 4 | International career insights | 2026-04-24 | X #137, IG #86 |
| 50 | Codigo Fonte TV | BR | T2 | YouTube | Froes + Weber | 500K+ | HIGH | Tech history, languages | weekly | MEDIUM | DM | 4 | Developer couple; entertaining format | 2026-04-24 | IG #85 |
| 51 | Olhar Digital | BR | T2 | YouTube | Olhar Digital | 500K | MEDIUM | Tech news, TV show | daily | MEDIUM | PR | 4 | Also weekly TV program | 2026-04-24 | NL #275 |
| 52 | Nate Herk | GLOBAL | T2 | YouTube | Nate Herkelman | 500K+ | HIGH | AI automation, n8n | weekly | HIGH | DM/email | 8 | AI automation educator; ex-Goldman | 2026-04-24 | -- |
| 53 | Dwarkesh Patel | GLOBAL | T2 | Podcast | Dwarkesh Podcast | 500K+ YT | HIGH | Deep tech interviews | biweekly | MEDIUM | DM/email | 5 | Deep tech interviews | 2026-04-24 | -- |
| 54 | Demis Hassabis | GLOBAL | T2 | Twitter/X | @demishassabis | 480K | LOW | AGI, AlphaFold | irregular | LOW | PR/DeepMind | 2 | Nobel Laureate, CEO Google DeepMind | 2026-04-24 | -- |
| 55 | Geoffrey Hinton | GLOBAL | T2 | Twitter/X | @geoffreyhinton | 489K | LOW | Deep learning, AI safety | irregular | LOW | Academic | 2 | Deep learning pioneer, Turing Award | 2026-04-24 | -- |
| 56 | Thais Martan | BR | T2 | Instagram | @thaismartan | 460K | HIGH | AI for business leaders | daily | HIGH | DM | 7 | Productivity + AI implementation | 2026-04-24 | -- |
| 57 | Kirk Borne | GLOBAL | T2 | Twitter/X | @KirkDBorne | 455K | MEDIUM | Big data, data science | daily | MEDIUM | DM/LinkedIn | 4 | Top data science influencer | 2026-04-24 | -- |
| 58 | Murtaza's Workshop | GLOBAL | T2 | YouTube | Murtaza Hassan | 447K | MEDIUM | Computer vision, robotics | weekly | MEDIUM | DM | 4 | CV/robotics projects | 2026-04-24 | -- |
| 59 | Nerdologia (Atila Iamarino) | BR | T2 | YouTube | Atila Iamarino | 400K+ | HIGH | Science, tech analysis | biweekly | MEDIUM | DM | 5 | PhD microbiology; Yale postdoc | 2026-04-24 | X #133, Acad #315 |
| 60 | Scale AI | GLOBAL | T2 | YouTube | Scale AI | 390K | MEDIUM | ML data lifecycle | weekly | MEDIUM | PR | 3 | Data-centric ML | 2026-04-24 | -- |
| 61 | Jeff Dean | GLOBAL | T2 | Twitter/X | @jeffdean | 361K | LOW | AI systems, Google | irregular | LOW | Google | 2 | Chief Scientist Google DeepMind | 2026-04-24 | -- |
| 62 | Antonio Grasso | GLOBAL | T2 | Twitter/X | @antgrasso | 346K | LOW | Tech, creator economy | daily | LOW | DM/LinkedIn | 2 | Technologist, sustainability | 2026-04-24 | -- |
| 63 | Ronald van Loon | GLOBAL | T2 | Twitter/X | @Ronald_vanLoon | 338K | LOW | AI, big data, IoT | daily | LOW | DM/LinkedIn | 2 | Top 10 Influencer AI/BigData | 2026-04-24 | -- |
| 64 | Aravind Srinivas | GLOBAL | T2 | Twitter/X | @AravSrinivas | 322K | MEDIUM | Conversational AI, search | weekly | MEDIUM | DM | 5 | CEO Perplexity AI | 2026-04-24 | Pod #270 |
| 65 | Ian Goodfellow | GLOBAL | T2 | Twitter/X | @goodfellow_ian | 316K | LOW | GANs, deep learning | irregular | LOW | Academic | 2 | Inventor of GANs, DeepMind | 2026-04-24 | -- |
| 66 | Wes Roth | GLOBAL | T2 | YouTube | Wes Roth | 313K | MEDIUM | AI news, tech | daily | MEDIUM | DM | 5 | AI commentary | 2026-04-24 | Pod #271 |
| 67 | Yannic Kilcher | GLOBAL | T2 | YouTube | Yannic Kilcher | 313K | HIGH | ML paper reviews | weekly | HIGH | DM/email | 8 | ML paper deep dives; ideal for 8F narrative | 2026-04-24 | Pod #276 |
| 68 | Fernando Ulrich | BR | T2 | YouTube | Fernando Ulrich | 300K+ | MEDIUM | Bitcoin, macroeconomics | weekly | LOW | DM | 3 | Economics + tech intersection | 2026-04-24 | -- |
| 69 | Attekita Dev | BR | T2 | YouTube | Karol Attekita | 300K+ | HIGH | International career, dev life | weekly | MEDIUM | DM | 4 | Career tips for devs abroad | 2026-04-24 | IG #83, X #19 |
| 70 | Cod3r (Leonardo Leitao) | BR | T2 | YouTube | Leonardo Leitao | 300K+ | MEDIUM | Fullstack courses | weekly | MEDIUM | DM | 4 | Education platform | 2026-04-24 | Edu #336 |
| 71 | Sujeito Programador | BR | T2 | YouTube | Matheus Fraga | 300K+ | MEDIUM | React, React Native | weekly | MEDIUM | DM | 4 | Mobile-focused | 2026-04-24 | IG #99 |
| 72 | Tamara McCleary | GLOBAL | T2 | Twitter/X | @TamaraMcCleary | 277K | LOW | AI, human purpose | weekly | LOW | DM/LinkedIn | 2 | CEO Thulium | 2026-04-24 | -- |
| 73 | Ken Jee | GLOBAL | T2 | Twitter/X | @ken_jee | 276K | MEDIUM | Data science, ML | weekly | MEDIUM | DM/YT | 4 | YouTube educator | 2026-04-24 | YT #120 |
| 74 | Julia McCoy | GLOBAL | T2 | YouTube | Julia McCoy | 268K | MEDIUM | AGI, AI platforms | weekly | MEDIUM | DM | 4 | AI platform president | 2026-04-24 | -- |
| 75 | TechTudo | BR | T2 | YouTube | TechTudo | 265K | MEDIUM | Tech news (Globo) | daily | MEDIUM | PR | 3 | Also 398K IG; Globo | 2026-04-24 | IG #61 |
| 76 | DevSuperior (Nelio Alves) | BR | T2 | YouTube | Nelio Alves | 250K+ | HIGH | Java, Spring Boot | weekly | MEDIUM | DM | 4 | Complete project-based learning | 2026-04-24 | Edu #337 |
| 77 | Gustavo Caetano | BR | T2 | Instagram | @gustavocaetano | 245K | MEDIUM | Tech entrepreneurship | weekly | MEDIUM | DM | 4 | Samba Tech founder; MIT Tech Review | 2026-04-24 | X #123, LI #172 |
| 78 | Soumith Chintala | GLOBAL | T2 | Twitter/X | @soumithchintala | 247K | HIGH | PyTorch, ML systems | weekly | HIGH | GitHub/DM | 8 | Co-founded PyTorch at Meta; typed systems | 2026-04-24 | -- |
| 79 | AI and Games | GLOBAL | T2 | YouTube | Dr Tommy Thompson | 231K | MEDIUM | AI in gaming | weekly | LOW | DM/email | 3 | AI + game design | 2026-04-24 | -- |
| 80 | All About AI | GLOBAL | T2 | YouTube | Kristian Fagerlie | 220K | HIGH | Generative AI tools | weekly | HIGH | DM | 7 | ChatGPT, Midjourney tutorials | 2026-04-24 | Pod #275 |
| 81 | MLST | GLOBAL | T2 | YouTube | MLST Team | 214K | HIGH | AI discussions, interviews | weekly | HIGH | DM/email | 7 | Deep AI analysis; ideal for 8F narrative | 2026-04-24 | Pod #267 |
| 82 | Varun Mayya | GLOBAL | T2 | Twitter/X | @waitin4agi_ | 214K | MEDIUM | AI tools, AGI experiments | daily | MEDIUM | DM | 4 | Builder, AI experimentalist | 2026-04-24 | -- |
| 83 | AI Andy | GLOBAL | T2 | YouTube | AI Andy | 213K | MEDIUM | AI news with humor | weekly | MEDIUM | DM | 4 | AI commentary | 2026-04-24 | -- |
| 84 | Erik Brynjolfsson | GLOBAL | T2 | Twitter/X | @erikbryn | 210K | LOW | Digital economy, AI policy | biweekly | LOW | Stanford HAI | 2 | Director DigEconLab | 2026-04-24 | -- |
| 85 | Hipsters.tech | BR | T2 | Podcast | Alura team | 200K+ listeners | HIGH | Startups, programming | weekly | HIGH | DM | 7 | By Alura; weekly tech discussions | 2026-04-24 | -- |
| 86 | Swyx (Shawn Wang) | GLOBAL | T2 | Newsletter | Latent Space | 200K+ | HIGH | AI engineering | weekly | HIGH | DM/Substack | 9 | Top 10 US Tech podcast; AI engineering authority; also 50K+ on Twitter/X @swyx; merged from X #146 | 2026-04-24 | X #146, Pod #249 |
| 87 | Pascal Bornet | GLOBAL | T2 | Twitter/X | @pascal_bornet | 158K | MEDIUM | AI automation | weekly | MEDIUM | LinkedIn/DM | 4 | Best-selling author, McKinsey alum | 2026-04-24 | LI #383 |
| 88 | Oriol Vinyals | GLOBAL | T2 | Twitter/X | @oriolvinyalsml | 182K | LOW | Deep learning, Gemini | irregular | LOW | DeepMind | 2 | VP Research Google DeepMind | 2026-04-24 | -- |
| 89 | Gary Marcus | GLOBAL | T2 | Twitter/X | @GaryMarcus | 173K | MEDIUM | AI critique, AGI debate | daily | MEDIUM | DM/email | 5 | Author, AI company founder | 2026-04-24 | -- |
| 90 | Robert Miles | GLOBAL | T2 | YouTube | Robert Miles | 169K | HIGH | AI safety research | biweekly | MEDIUM | DM | 5 | AI safety videos | 2026-04-24 | -- |
| 91 | Eldo Gomes | BR | T2 | Instagram | @eldogomes | 165K | MEDIUM | Innovation, tech trends | weekly | MEDIUM | DM | 4 | InfluTechs list curator | 2026-04-24 | -- |
| 92 | Timnit Gebru | GLOBAL | T2 | Twitter/X | @timnitgebru | 162K | MEDIUM | AI ethics, fairness | weekly | LOW | DAIR Institute | 3 | AI ethics researcher | 2026-04-24 | -- |
| 93 | Vincent Boucher | GLOBAL | T2 | Twitter/X | @ceobillionaire | 154K | LOW | Montreal AI, physics | weekly | LOW | DM | 2 | President Montreal AI | 2026-04-24 | -- |
| 94 | Programacao Dinamica | BR | T2 | YouTube | Prog. Dinamica | 150K+ | HIGH | CS, algorithms, Python | weekly | HIGH | DM | 8 | Academic-quality CS; ideal audience | 2026-04-24 | IG #88, X #-- |
| 95 | DevPleno (Tulio Faria) | BR | T2 | YouTube | Tulio Faria | 150K+ | MEDIUM | Career, JS, Node mentoring | weekly | MEDIUM | DM | 4 | Mentorship focus | 2026-04-24 | Edu #338 |
| 96 | Bubows (Bruno Belissimo) | BR | T2 | Instagram | @bubows.ia | 150K+ | HIGH | AI demos, visual content | daily | HIGH | DM | 7 | Simple language; direct AI tool demos | 2026-04-24 | -- |
| 97 | Jeremy Howard | GLOBAL | T2 | YouTube | Jeremy Howard | 145K | HIGH | Deep learning courses | weekly | HIGH | DM/email | 8 | fast.ai co-founder; OSS advocate; also conference speaker; merged from Conf #128 | 2026-04-24 | Blog #317, Speaker #298, Conf #128 |
| 98 | Sally Eaves | GLOBAL | T2 | Twitter/X | @sallyeaves | 138K | LOW | AI, 5G, digital transform | weekly | LOW | DM/LinkedIn | 2 | CEO, CTO, thought leader | 2026-04-24 | -- |
| 99 | Bernard Marr | GLOBAL | T2 | Twitter/X | @bernardmarr | 139K | LOW | AI futurism, keynote | weekly | LOW | PR/email | 2 | Best-selling author | 2026-04-24 | -- |
| 100 | Rob Lennon | GLOBAL | T2 | Twitter/X | @thatroblennon | 133K | MEDIUM | AI business, prompt writing | weekly | MEDIUM | DM | 4 | 17+ yrs startups | 2026-04-24 | -- |
| 101 | Fabio Moioli | GLOBAL | T2 | Twitter/X | @fabiomoioli | 125K | LOW | AI strategy, consulting | weekly | LOW | LinkedIn | 2 | Spencer Stuart | 2026-04-24 | -- |
| 102 | Nicolai Nielsen | GLOBAL | T2 | YouTube | Nicolai Nielsen | 122K | MEDIUM | Coding education | weekly | MEDIUM | DM | 4 | Tech educator | 2026-04-24 | -- |
| 103 | HuggingFace YT | GLOBAL | T2 | YouTube | HuggingFace | 119K | HIGH | NLP/ML tools, tutorials | weekly | HIGH | Community/email | 7 | Official HF channel | 2026-04-24 | GH #195-196 |
| 104 | Harold Sinnott | GLOBAL | T2 | Twitter/X | @HaroldSinnott | 113K | LOW | AI, IoT, 5G | weekly | LOW | DM/LinkedIn | 2 | Tech thought leader | 2026-04-24 | -- |
| 105 | Data Chaz | GLOBAL | T2 | Twitter/X | @DataChaz | 114K | HIGH | LLMs, Streamlit | daily | HIGH | DM/GitHub | 8 | Dev Advocate Streamlit; builder community | 2026-04-24 | -- |
| 106 | Randy Olson | GLOBAL | T2 | Twitter/X | @randal_olson | 111K | MEDIUM | Data science, ML research | weekly | MEDIUM | DM | 4 | Full stack data scientist | 2026-04-24 | -- |
| 107 | Nicolas Babin | GLOBAL | T2 | Twitter/X | @Nicochan33 | 117K | LOW | AI, 5G, digital transform | daily | LOW | DM/LinkedIn | 2 | Key Opinion Leader | 2026-04-24 | -- |
| 108 | Yohei Nakajima | GLOBAL | T2 | Twitter/X | @yoheinakajima | 108K | HIGH | AI agents, BabyAGI | weekly | HIGH | DM/GitHub | 9 | Creator BabyAGI; agent framework pioneer | 2026-04-24 | -- |
| 109 | Iain Brown | GLOBAL | T2 | Twitter/X | @iainljbrown | 105K | MEDIUM | Data science, AI/ML/NLP | weekly | MEDIUM | DM | 4 | Head of DS at SAS | 2026-04-24 | -- |
| 110 | Chris Messina | GLOBAL | T2 | Twitter/X | @chrismessina | 105K | LOW | Tech innovation | weekly | LOW | DM | 2 | Hashtag inventor | 2026-04-24 | -- |
| 111 | Danilo Gato | BR | T2 | Twitter/X | @odanilogato | 100K+ | HIGH | AI content, tools | daily | HIGH | DM | 10 | #1 AI content creator BR (Favikon); CPDF founder; FGV professor | 2026-04-24 | YT #30, IG #68, LI #190, Pod #251, NL #267 |
| 112 | Matt Wolfe | GLOBAL | T2 | YouTube | Matt Wolfe | 100K+ | HIGH | AI tools, Future Tools | weekly | HIGH | DM/email | 8 | Creator futuretools.io | 2026-04-24 | Pod #273, NL #-- |
| 113 | Matthew Berman | GLOBAL | T2 | YouTube | Matthew Berman | 100K+ | HIGH | LLMs, OSS AI, news | daily | HIGH | DM/email | 8 | AI product coverage; open-source AI | 2026-04-24 | -- |
| 114 | AI Explained | GLOBAL | T2 | YouTube | AI Explained | 100K+ | HIGH | LLM analysis, reasoning | weekly | HIGH | DM | 8 | Signal over noise AI coverage | 2026-04-24 | -- |
| 115 | David Shapiro | GLOBAL | T2 | YouTube | David Shapiro | 100K+ | HIGH | AGI, 4th industrial rev | weekly | HIGH | DM/email | 8 | Autonomous AI deep dives | 2026-04-24 | Pod #272 |
| 116 | Rafael Milagre | BR | T2 | YouTube | Viver de IA | 100K+ | HIGH | AI for business, mentoring | weekly | HIGH | DM (@rafaelmilagre) | 9 | Largest AI education platform BR; ESPM prof | 2026-04-24 | IG #71, X #145, LI #189, Pod #264, NL #268 |
| 117 | Erick Wendel | BR | T2 | YouTube | Erick Wendel | 100K+ | HIGH | Advanced JS, Node.js | weekly | HIGH | DM | 8 | Deep technical; conference speaker | 2026-04-24 | X #124, IG #81 |
| 118 | Loiane Groner | BR | T2 | YouTube | Loiane Groner | 100K+ | MEDIUM | Angular, Java, data struct | weekly | MEDIUM | DM | 4 | Also author of tech books | 2026-04-24 | IG #91, X #140, Edu #339 |
| 119 | Eduardo Mendes (Dunossauro) | BR | T2 | YouTube | Dunossauro | 100K+ | HIGH | Python, FastAPI, OSS | weekly | HIGH | DM | 8 | Live de Python; open source contributor | 2026-04-24 | IG #101, X #139 |
| 120 | Otavio Miranda | BR | T2 | YouTube | Otavio Miranda | 100K+ | MEDIUM | Python, Django | weekly | MEDIUM | DM | 4 | Also Linux content | 2026-04-24 | -- |
| 121 | NerdTech | BR | T2 | Podcast | JovemNerd + Alura | 100K+ listeners | MEDIUM | Technology deep dives | biweekly | MEDIUM | PR | 4 | Spinoff of NerdCast | 2026-04-24 | -- |
| 122 | TecMundo NL | BR | T2 | Newsletter | TecMundo | 100K+ subs | MEDIUM | Tech news | daily | MEDIUM | PR | 3 | Part of NZN | 2026-04-24 | YT #6 |
| 123 | Theo Browne | GLOBAL | T2 | Twitter/X | @t3dotgg | 80K+ | HIGH | Full-stack dev, AI tools | daily | HIGH | DM/YouTube | 8 | CEO, T3 stack creator | 2026-04-24 | -- |
| 124 | Zain Kahn | GLOBAL | T2 | Twitter/X | @zainkahn | 80K+ (X), 1M+ (LI) | HIGH | AI newsletter, business | daily | HIGH | DM/LinkedIn | 9 | Superhuman AI (1M+ subs); cross-platform | 2026-04-24 | NL #218, LI #381 |
| 125 | Filipe Deschamps NL | BR | T2 | Podcast | Filipe Deschamps | 100K+ listeners | HIGH | Daily tech news | daily | HIGH | Email | 8 | Companion podcast to newsletter | 2026-04-24 | YT #34 |
| 126 | Thomas Wolf | GLOBAL | T2 | Conference | HuggingFace | -- | HIGH | Transformers library | weekly | HIGH | DM/GH | 8 | Co-founder HuggingFace | 2026-04-24 | Speaker #308 |
| 127 | Matei Zaharia | GLOBAL | T2 | Conference | Databricks | -- | MEDIUM | Spark, MLflow | irregular | HIGH | DM | 7 | CTO Databricks, Stanford prof | 2026-04-24 | Speaker #291 |
| 129 | Percy Liang | GLOBAL | T2 | Conference | Stanford CRFM | -- | HIGH | Foundation models, HELM | irregular | HIGH | Academic | 7 | Stanford CRFM; typed eval | 2026-04-24 | Speaker #281 |
| 130 | Dario Amodei | GLOBAL | T2 | Conference | Anthropic | -- | LOW | AI safety, Claude | irregular | MEDIUM | PR | 4 | CEO Anthropic, ICML 2026 | 2026-04-24 | Speaker #279 |
| 131 | Canaltech NL | BR | T2 | Newsletter | Canaltech | 80K+ subs | MEDIUM | Tech news | daily | MEDIUM | PR | 3 | Daily tech news | 2026-04-24 | YT #12 |

---

## 5. T3 Contacts (10K-100K)

Due to the large number (452 contacts), this section is organized by sub-region and platform for navigability.

### 5.1 T3 GLOBAL -- Twitter/X (43 contacts)

| # | Name | Region | Platform | Handle | Followers | Relevance | Priority | Notes |
|---|------|--------|----------|--------|-----------|-----------|----------|-------|
| 132 | Nando de Freitas | GLOBAL | Twitter/X | @NandoDF | 96K | LOW | 3 | Research lead DeepMind |
| 133 | Claire Silver | GLOBAL | Twitter/X | @clairesilver12 | 97K | LOW | 3 | AI artist since 2018 |
| 134 | Lorenzo Green | GLOBAL | Twitter/X | @mrgreen | 90K | MEDIUM | 4 | Serial entrepreneur |
| 135 | Abhishek Thakur | GLOBAL | Twitter/X | @abhi1thakur | 83K | HIGH | 7 | 4x Kaggle GM, HuggingFace |
| 136 | Kate Crawford | GLOBAL | Twitter/X | @katecrawford | 82K | LOW | 3 | MIT, Atlas of AI author |
| 137 | Nathan Lands | GLOBAL | Twitter/X | @nathanlands | 77K | MEDIUM | 4 | GP Lands Capital (AI fund) |
| 138 | Hassan Rashidi | GLOBAL | Twitter/X | @drhassanrashidi | 75K | MEDIUM | 4 | Keynote speaker, advisor |
| 139 | Bilawal Sidhu | GLOBAL | Twitter/X | @bilawalsidhu | 69K | MEDIUM | 4 | Ex-Google (XR, Maps) |
| 140 | Matt Shumer | GLOBAL | Twitter/X | @mattshumer_ | 65K+ | HIGH | 7 | LLM builder, OthersideAI |
| 141 | Karen Hao | GLOBAL | Twitter/X | @2_karenhao | 62K | MEDIUM | 4 | National magazine award |
| 142 | Helen Yu | GLOBAL | Twitter/X | @YuHelenYu | 61K | MEDIUM | 4 | CEO Tigon Advisory |
| 143 | Nathan Benaich | GLOBAL | Twitter/X | @nathanbenaich | 61K | MEDIUM | 4 | Air Street Capital |
| 144 | Giuliano Liguori | GLOBAL | Twitter/X | @ingliguori | 61K | LOW | 3 | CEO Kenovy |
| 145 | Monica Rogati | GLOBAL | Twitter/X | @mrogati | 50K | MEDIUM | 4 | Fractional CDO |
| 147 | Martin Ford | GLOBAL | Twitter/X | @mfordfuture | 45K | LOW | 3 | NY Times bestselling author |
| 149 | Catherine Adenle | GLOBAL | Twitter/X | @CatherineAdenle | 43K | LOW | 3 | Women in Tech leader |
| 150 | Marcus Borba | GLOBAL | Twitter/X | @marcusborba | 40K | LOW | 3 | Global thought leader |
| 152 | Mike Tamir | GLOBAL | Twitter/X | @miketamir | 39K | HIGH | 6 | ML Scientist Shopify |
| 153 | Max Welling | GLOBAL | Twitter/X | @wellingmax | 38K | LOW | 3 | ML researcher |
| 154 | Aaron Ng | GLOBAL | Twitter/X | @localghost | 36K | HIGH | 7 | Creator Apollo AI |
| 155 | Kate Darling | GLOBAL | Twitter/X | @grok_ | 35K | LOW | 3 | MIT Media Lab |
| 156 | Jim Fan | GLOBAL | Twitter/X | @DrJimFan | 33K+ | HIGH | 7 | NVIDIA senior research scientist; also conference speaker (embodied AI, humanoid robots); merged from Conf #286 |
| 157 | Rodney Brooks | GLOBAL | Twitter/X | @rodneyabrooks | 32K | LOW | 3 | Robotics pioneer |
| 158 | Cade Metz | GLOBAL | Twitter/X | @CadeMetz | 31K | MEDIUM | 4 | NYT AI reporter |
| 160 | Oren Etzioni | GLOBAL | Twitter/X | @etzioni | 27K | MEDIUM | 4 | Co-founder AI2 |
| 161 | Daphne Koller | GLOBAL | Twitter/X | @DaphneKoller | 26K | LOW | 3 | CEO insitro |
| 162 | Alex Champandard | GLOBAL | Twitter/X | @alexjc | 26K | HIGH | 7 | AI tool builder |
| 163 | Gene Kogan | GLOBAL | Twitter/X | @genekogan | 26K | LOW | 3 | Artist/technologist |
| 164 | Logan Kilpatrick | GLOBAL | Twitter/X | @OfficialLoganK | 25K+ | HIGH | 7 | Google AI Studio lead |
| 165 | Justine Moore | GLOBAL | Twitter/X | @justine_moore | 25K+ | MEDIUM | 4 | Partner a16z |
| 166 | Sebastian Raschka | GLOBAL | Twitter/X | @rasaborsx | 25K+ | HIGH | 8 | Lightning AI; Ahead of AI |
| 167 | Paul Roetzer | GLOBAL | Twitter/X | @paulroetzer | 21K | MEDIUM | 4 | Marketing AI Institute |
| 168 | Andy Jankowski | GLOBAL | Twitter/X | @andyjankowski | 20K | MEDIUM | 4 | AI Advisor |
| 169 | Luiza Jarovsky | GLOBAL | Twitter/X | @LuizaJarovsky | 20K+ | MEDIUM | 4 | AI governance |
| 170 | Alessio Fanelli | GLOBAL | Twitter/X | @alessiofanelli | 15K+ | HIGH | 8 | Co-host Latent Space |
| 171 | Nathan Labenz | GLOBAL | Twitter/X | @labenz | 15K+ | HIGH | 8 | Host Cognitive Revolution |
| 172 | Peter Steinberger | GLOBAL | Twitter/X | @steipete | 30K+ | HIGH | 8 | OpenClaw, agents; now at OpenAI |
| 173 | Marcell Vollmer | GLOBAL | Twitter/X | @mvollmer1 | 96K | LOW | 3 | AI, digital transformation |

### 5.2 T3 GLOBAL -- YouTube (35 contacts)

| # | Name | Region | Platform | Handle/Channel | Subs | Relevance | Priority | Notes |
|---|------|--------|----------|----------------|------|-----------|----------|-------|
| 174 | MITCSAIL | GLOBAL | YouTube | MIT CSAIL | 88K | LOW | 3 | MIT AI lab |
| 175 | AI News | GLOBAL | YouTube | AI News | 92K | MEDIUM | 4 | Education format news |
| 176 | James Briggs | GLOBAL | YouTube | James Briggs | 80K | HIGH | 7 | Pinecone, vector DB content |
| 177 | What's AI | GLOBAL | YouTube | Louis Bouchard | 71K | MEDIUM | 5 | Co-founder towards_ai |
| 178 | InsiderPhD | GLOBAL | YouTube | Katie Paxton-Fear | 68K | LOW | 3 | Cybersecurity |
| 179 | Aleksa Gordic | GLOBAL | YouTube | Aleksa Gordic | 64K | HIGH | 7 | Paper breakdowns + code |
| 180 | AI Coffee Break | GLOBAL | YouTube | Letitia Parcalabescu | 63K | MEDIUM | 4 | Lighthearted ML content |
| 181 | AI News Daily | GLOBAL | YouTube | Alex | 58K | MEDIUM | 4 | Daily AI news |
| 182 | Rithesh Sreenivasan | GLOBAL | YouTube | Rithesh Sreenivasan | 51K | MEDIUM | 4 | NLP, CV, data science |
| 183 | Connor Shorten | GLOBAL | YouTube | Connor Shorten | 45K | HIGH | 7 | CV, NLP, GAN research |
| 184 | AI Joe | GLOBAL | YouTube | AI Joe | 44K | MEDIUM | 4 | AI business strategies |
| 185 | Jack Roberts | GLOBAL | YouTube | Jack Roberts | 40K+ | HIGH | 7 | AI automation, no-code agents |
| 186 | The A.I. Whisperer | GLOBAL | YouTube | A.I. Whisperer | 40K | MEDIUM | 4 | Themed AI content |
| 187 | Meta AI | GLOBAL | YouTube | Meta AI | 38K | LOW | 2 | Official Meta AI |
| 188 | AI Sciences | GLOBAL | YouTube | AI Sciences | 37K | MEDIUM | 4 | ML/stats education |
| 189 | Valerio Velardo | GLOBAL | YouTube | Valerio Velardo | 36K | LOW | 3 | Audio AI specialist |
| 190 | Venelin Valkov | GLOBAL | YouTube | Venelin Valkov | 33K | MEDIUM | 4 | AI critique |
| 191 | Eye on AI | GLOBAL | YouTube | Craig S. Smith | 33K | MEDIUM | 4 | AI podcast/news |
| 192 | Stanford HAI | GLOBAL | YouTube | Stanford HAI | 33K | LOW | 3 | Human-centered AI |
| 193 | Dr Waku | GLOBAL | YouTube | Dr Waku | 31K | LOW | 3 | AI philosophy |
| 194 | SingularityNET | GLOBAL | YouTube | SingularityNET | 32K | MEDIUM | 4 | Decentralized AI |
| 195 | Global AI Community | GLOBAL | YouTube | Global AI Community | 30K | MEDIUM | 4 | Connecting AI communities |
| 196 | The AI University | GLOBAL | YouTube | AI University | 30K | MEDIUM | 4 | Democratizing AI |
| 197 | TWIML AI Podcast (Sam Charrington) | GLOBAL | YouTube | Sam Charrington | 29K | HIGH | 7 | This Week in ML; also longest-running ML podcast; merged from Pod #263 |
| 198 | Leo Isikdogan | GLOBAL | YouTube | Leo Isikdogan | 25K | MEDIUM | 4 | CV, deep learning |
| 199 | H2O.ai | GLOBAL | YouTube | H2O.ai | 23K | MEDIUM | 3 | AI cloud platform |
| 200 | AI for Good | GLOBAL | YouTube | AI for Good | 22K | LOW | 2 | Social impact AI |
| 201 | Nachiketa Hebbar | GLOBAL | YouTube | Nachiketa Hebbar | 19K | MEDIUM | 4 | CV engineering |
| 202 | Learn Robotics | GLOBAL | YouTube | Building Culture | 19K | MEDIUM | 4 | Meetups, podcasts |
| 203 | Marketing AI Inst. | GLOBAL | YouTube | Marketing AI | 17K | MEDIUM | 4 | MAICON conference |
| 204 | Amii Intelligence | GLOBAL | YouTube | Amii | 15K | LOW | 2 | Alberta ML institute |
| 205 | Micah | GLOBAL | YouTube | Micah | 15K | MEDIUM | 4 | Data viz, no-code, AI |
| 206 | Lightning AI | GLOBAL | YouTube | Lightning AI | 13K | HIGH | 7 | PyTorch Lightning |

### 5.3 T3 GLOBAL -- GitHub Maintainers (48 contacts)

| # | Name | Region | Platform | GitHub Handle | Project | Stars | Relevance | Priority | Notes |
|---|------|--------|----------|---------------|---------|-------|-----------|----------|-------|
| 207 | Harrison Chase | GLOBAL | GitHub | hwchase17 | LangChain | 100K+ | HIGH | 9 | CEO LangChain; also 45K+ Twitter/X @hwchase17; merged from X #148 |
| 208 | Joao Moura | GLOBAL | GitHub | joaomdmoura | CrewAI | 25K+ | HIGH | 9 | Founder CrewAI; Brazilian; also 30K+ Twitter/X @joaomdmoura; merged from X #159 |
| 209 | Paul Gauthier | GLOBAL | GitHub | paul-gauthier | Aider | 30K+ | HIGH | 9 | AI pair programming |
| 210 | Simon Willison | GLOBAL | GitHub | simonw | llm, Datasette | 15K+ | HIGH | 9 | CLI LLM tools; also 40K+ Twitter/X @simonw + 100K+ blog; merged from X #151, Blog #267 |
| 211 | Toran Bruce Richards | GLOBAL | GitHub | torantulino | AutoGPT | 167K+ | HIGH | 8 | Pioneer autonomous agent |
| 212 | Danny Avila | GLOBAL | GitHub | danny-avila | LibreChat | 20K+ | HIGH | 8 | Multi-model chat UI |
| 213 | Mintplex Labs | GLOBAL | GitHub | Mintplex-Labs | AnythingLLM | 30K+ | HIGH | 8 | All-in-one AI app |
| 214 | LangGenius | GLOBAL | GitHub | langgenius | Dify | 130K+ | HIGH | 8 | Visual agent builder |
| 215 | FlowiseAI | GLOBAL | GitHub | FlowiseAI | Flowise | 35K+ | HIGH | 8 | Drag-drop LLM agents |
| 216 | Langflow AI | GLOBAL | GitHub | langflow-ai | Langflow | 45K+ | HIGH | 8 | Visual multi-agent builder |
| 217 | Lobehub | GLOBAL | GitHub | lobehub | LobeChat | 55K+ | HIGH | 8 | Self-hosted chat UI |
| 218 | Mudler | GLOBAL | GitHub | mudler | LocalAI | 30K+ | HIGH | 8 | Drop-in OpenAI API |
| 219 | Nomic AI | GLOBAL | GitHub | nomic-ai | GPT4All | 72K+ | HIGH | 7 | Local LLM desktop |
| 220 | Mozilla | GLOBAL | GitHub | Mozilla-Ocho | Llamafile | 25K+ | HIGH | 7 | Single-file LLMs |
| 221 | Ollama team | GLOBAL | GitHub | ollama | Ollama | 162K+ | HIGH | 9 | Run LLMs locally; CEX runtime |
| 222 | GGML org | GLOBAL | GitHub | ggml-org | llama.cpp | 75K+ | HIGH | 7 | C++ LLM inference |
| 223 | Open WebUI | GLOBAL | GitHub | open-webui | Open WebUI | 70K+ | HIGH | 8 | Self-hosted ChatGPT UI |
| 224 | Microsoft | GLOBAL | GitHub | microsoft | AutoGen | 40K+ | HIGH | 7 | Multi-agent conversations |
| 225 | Microsoft | GLOBAL | GitHub | microsoft | Semantic Kernel | 25K+ | HIGH | 7 | LLM enterprise SDK |
| 226 | Microsoft | GLOBAL | GitHub | microsoft | Playwright MCP | 10K+ | HIGH | 7 | MCP for Playwright |
| 227 | Stanford NLP | GLOBAL | GitHub | stanfordnlp | DSPy | 20K+ | HIGH | 8 | Prompt optimization |
| 228 | Princeton NLP | GLOBAL | GitHub | princeton-nlp | SWE-Agent | 15K+ | HIGH | 7 | Autonomous GH issues |
| 229 | All Hands AI | GLOBAL | GitHub | All-Hands-AI | OpenHands | 50K+ | HIGH | 8 | OSS autonomous engineer |
| 230 | ByteDance | GLOBAL | GitHub | bytedance | DeerFlow | 25K+ | HIGH | 7 | #1 GH trending Feb 2026 |
| 231 | HuggingFace | GLOBAL | GitHub | huggingface | Smolagents | 15K+ | HIGH | 8 | Minimal agents |
| 232 | HuggingFace | GLOBAL | GitHub | huggingface | Transformers | 140K+ | HIGH | 7 | Foundation ML library |
| 233 | Infiniflow | GLOBAL | GitHub | infiniflow | RAGFlow | 35K+ | HIGH | 7 | OSS RAG engine |
| 234 | Mem0 AI | GLOBAL | GitHub | mem0ai | Mem0 | 25K+ | HIGH | 8 | Memory layer for agents; relevant to CEX P10 |
| 235 | Chroma | GLOBAL | GitHub | chroma-core | Chroma | 15K+ | HIGH | 7 | Embedding database |
| 236 | LiveKit | GLOBAL | GitHub | livekit | LiveKit Agents | 10K+ | HIGH | 7 | Real-time voice/video AI |
| 237 | Pipecat AI | GLOBAL | GitHub | pipecat-ai | Pipecat | 8K+ | HIGH | 7 | Voice conversational AI |
| 238 | Langfuse | GLOBAL | GitHub | langfuse | Langfuse | 8K+ | HIGH | 8 | LLM observability |
| 239 | N8N | GLOBAL | GitHub | n8n-io | n8n | 55K+ | HIGH | 8 | Workflow automation |
| 240 | Browser Use | GLOBAL | GitHub | browser-use | browser-use | 55K+ | HIGH | 7 | OSS browser agent |
| 241 | Skyvern | GLOBAL | GitHub | Skyvern-AI | Skyvern | 12K+ | HIGH | 7 | Vision browser agent |
| 242 | Geekan | GLOBAL | GitHub | geekan | MetaGPT | 50K+ | HIGH | 7 | Multi-agent software company |
| 243 | CAMEL AI | GLOBAL | GitHub | camel-ai | CAMEL | 6K+ | HIGH | 7 | Role-based agent simulation |
| 244 | OpenAI | GLOBAL | GitHub | openai | Codex CLI | 20K+ | HIGH | 8 | Terminal agent; CEX runtime |
| 245 | Google | GLOBAL | GitHub | google | A2A Protocol | 15K+ | HIGH | 8 | Agent-to-Agent protocol |
| 246 | Google | GLOBAL | GitHub | google | ADK Python | 10K+ | HIGH | 7 | Agent Development Kit |
| 247 | Anthropic | GLOBAL | GitHub | anthropics | Claude SDK | 10K+ | HIGH | 8 | Official Claude SDK; CEX primary runtime |
| 248 | Anthropic | GLOBAL | GitHub | modelcontextprotocol | MCP | 20K+ | HIGH | 9 | Model Context Protocol; CEX uses MCP |
| 249 | Cline | GLOBAL | GitHub | cline | Cline | 20K+ | HIGH | 8 | VS Code AI extension |

### 5.4 T3 GLOBAL -- Newsletters, Podcasts, Blogs, Speakers (remaining)

| # | Name | Region | Platform | Followers | Relevance | Priority | Notes |
|---|------|--------|----------|-----------|-----------|----------|-------|
| 250 | TLDR AI | GLOBAL | Newsletter | 1.25M+ | HIGH | 7 | Technical AI filter |
| 251 | Steve Nouri | GLOBAL | LinkedIn | 2M+ (LI), 3.15M newsletter | MEDIUM | 5 | Largest AI community (14M) |
| 252 | The Neuron | GLOBAL | Newsletter | 550K+ | MEDIUM | 5 | Morning Brew style AI |
| 253 | Andrew Ng / The Batch | GLOBAL | Newsletter | 500K+ | MEDIUM | 5 | DeepLearning.AI newsletter |
| 254 | AlphaSignal | GLOBAL | Newsletter | 180K+ | HIGH | 7 | By researchers, for researchers |
| 255 | Sebastian Raschka NL | GLOBAL | Newsletter | 150K+ | HIGH | 8 | Ahead of AI ML research |
| 256 | Ben Tossell | GLOBAL | Newsletter | 100K+ | HIGH | 7 | Ben's Bites; AI news, tools |
| 257 | Nathan Labenz NL | GLOBAL | Newsletter | 50K+ | HIGH | 7 | AI engineering deep dives |
| 258 | Jack Clark | GLOBAL | Newsletter | 50K+ | HIGH | 7 | Import AI policy + research |
| 259 | Davis Blalock | GLOBAL | Newsletter | 30K+ | HIGH | 7 | ML arXiv summaries |
| 260 | Christoph Molnar | GLOBAL | Newsletter | 30K+ | HIGH | 7 | Stats-grounded AI analysis |
| 261 | Interconnects AI | GLOBAL | Newsletter | 50K+ | HIGH | 7 | RLHF, AI alignment |
| 262 | Dan Shipper | GLOBAL | Newsletter | 50K+ | HIGH | 7 | Every (AI productivity) |
| 264 | Practical AI | GLOBAL | Podcast | large | HIGH | 7 | Lockheed Martin + PredictionGuard |
| 265 | AI Agents Podcast | GLOBAL | Podcast | growing | HIGH | 7 | Jotform CEO + Rise Productive |
| 266 | AI Native Dev | GLOBAL | Podcast | growing | HIGH | 7 | AI-native software dev |
| 268 | Lilian Weng | GLOBAL | Blog | 500K+ | HIGH | 7 | OpenAI, legendary ML blog; also conference speaker (ML research); merged from Conf #285 |
| 269 | Chip Huyen | GLOBAL | Blog | 200K+ | HIGH | 8 | ML systems author; also conference speaker; merged from Conf #284 |
| 270 | Chris Olah | GLOBAL | Blog | 200K+ | HIGH | 7 | Neural net visualization; also conference speaker (interpretability, Anthropic); merged from Conf #288 |
| 271 | Jay Alammar | GLOBAL | Blog | 300K+ | HIGH | 7 | Transformer visualizations |
| 272 | Eugene Yan | GLOBAL | Blog | 50K+ | HIGH | 7 | ML engineering practice |
| 273 | Vicki Boykis | GLOBAL | Blog | 30K+ | HIGH | 7 | ML engineering, search |
| 274 | Hamel Husain | GLOBAL | Blog | 20K+ | HIGH | 7 | ML tools, nbdev |
| 275 | W&B blog | GLOBAL | Blog | 100K+ | HIGH | 6 | ML experiment tracking |
| 276 | Pinecone blog | GLOBAL | Blog | 200K+ | HIGH | 6 | Vector DB, RAG guides |
| 277 | LangChain blog | GLOBAL | Blog | 100K+ | HIGH | 6 | Agent framework updates |
| 278 | Anthropic blog | GLOBAL | Blog | 500K+ | HIGH | 6 | Claude research |
| 279 | Together AI blog | GLOBAL | Blog | 50K+ | HIGH | 6 | Open models, inference |
| 280 | Modal blog | GLOBAL | Blog | 30K+ | HIGH | 6 | Serverless AI compute |

### 5.5 T3 GLOBAL -- Conference Speakers & Researchers (selected HIGH relevance)

| # | Name | Region | Platform | Focus | Relevance | Priority | Notes |
|---|------|--------|----------|-------|-----------|----------|-------|
| 281 | Jason Wei | GLOBAL | Conference | Chain of thought, reasoning | HIGH | 8 | CoT prompting pioneer; relevant to 8F |
| 282 | Tri Dao | GLOBAL | Conference | FlashAttention | HIGH | 7 | FlashAttention creator |
| 283 | Douwe Kiela | GLOBAL | Conference | RAG, retrieval | HIGH | 7 | RAG systems expert |
| 287 | Sara Hooker | GLOBAL | Conference | Model efficiency | HIGH | 7 | Cohere research lead |
| 289 | Clementine Fourrier | GLOBAL | Conference | Open LLM Leaderboard | HIGH | 7 | HF leaderboard maintainer |

### 5.6 T3 BR -- YouTube (25 contacts)

| # | Name | Region | Platform | Handle | Subs | Relevance | Priority | Notes |
|---|------|--------|----------|--------|------|-----------|----------|-------|
| 290 | Marco Bruno | BR | YouTube | Marco Bruno | 80K+ | MEDIUM | 4 | Beginner-friendly |
| 291 | Diolinux | BR | YouTube | Diolinux | 80K+ | MEDIUM | 4 | Linux, open source |
| 292 | Macoratti | BR | YouTube | Macoratti | 70K+ | MEDIUM | 4 | Oldest BR dev channels |
| 293 | LinuxTips | BR | YouTube | Jeferson Fernando | 70K+ | HIGH | 7 | DevOps training; LINUXtips |
| 294 | Gabriel Pato | BR | YouTube | Gabriel Pato | 60K+ | MEDIUM | 4 | Cybersecurity focus |
| 295 | BrazilJS | BR | YouTube | BrazilJS | 50K+ | HIGH | 7 | Largest JS event LatAm |
| 296 | Waldemar Neto | BR | YouTube | Dev Lab | 50K+ | HIGH | 7 | Node.js, DevOps, Docker |
| 297 | Prof. Sandeco | BR | YouTube | Sandeco | 51K+ | HIGH | 8 | University professor; AI + LLMs + data science/ML; also Canal Sandeco (35K+); merged from YT #303 |
| 298 | Hugo Vasconcelos | BR | YouTube | Hugo Vasconcelos | 50K+ | HIGH | 7 | Python, automation, bots |
| 299 | IA Todo Dia | BR | YouTube | IA Todo Dia | 40K+ | HIGH | 8 | AI news, tools; also largest AI podcast BR (top Spotify); merged from Pod #457 |
| 300 | Didatica Tech | BR | YouTube | Didatica Tech | 40K+ | HIGH | 7 | Education-focused AI |
| 301 | Flutterando | BR | YouTube | Flutterando | 40K+ | MEDIUM | 4 | Flutter, mobile dev |
| 302 | Full Cycle | BR | YouTube | Full Cycle | 35K+ | HIGH | 7 | Architecture-focused |
| 304 | ML4U | BR | YouTube | ML4U | 30K+ | HIGH | 7 | Academic ML content |
| 305 | Universo Programado | BR | YouTube | Universo Programado | 30K+ | HIGH | 7 | AI demos and tutorials |
| 306 | DevMedia | BR | YouTube | DevMedia | 30K+ | MEDIUM | 4 | Knowledge portal |
| 307 | Lambda3 | BR | YouTube | Lambda3 | 25K+ | MEDIUM | 4 | Enterprise tech |
| 308 | Michelli Brito | BR | YouTube | Michelli Brito | 25K+ | MEDIUM | 4 | Java community leader |
| 309 | One Bit Code | BR | YouTube | One Bit Code | 20K+ | MEDIUM | 4 | Ruby on Rails |
| 310 | Rodrigo Branas | BR | YouTube | Rodrigo Branas | 20K+ | MEDIUM | 4 | JS, Angular specialist |
| 311 | Mario Filho | BR | YouTube | Mario Filho | 15K+ | HIGH | 7 | Kaggle competitor; ML |
| 312 | Glaucia Lemos | BR | YouTube | Glaucia Lemos | 15K+ | HIGH | 7 | Microsoft Dev Advocate |
| 313 | Teo Calvo | BR | YouTube | Teo Calvo | 15K+ | HIGH | 7 | Twitch live data science |

### 5.7 T3 BR -- Instagram (50 contacts)

| # | Name | Region | Platform | Handle | Followers | Relevance | Priority | Notes |
|---|------|--------|----------|--------|-----------|-----------|----------|-------|
| 314 | Andre Lug | BR | Instagram | @andre_lug | 85K | HIGH | 7 | Practical AI tools |
| 315 | Alura | BR | Instagram | @aluraonline | 80K+ | MEDIUM | 4 | Largest BR tech school |
| 316 | Nina da Hora | BR | Instagram | @ninadhora | 58K | HIGH | 7 | Hacker antirracista; Forbes U30 |
| 317 | Danilo Gato IG | BR | Instagram | @odanilogato | 50K+ | HIGH | 8 | #1 AI BR; cross-ref YT |
| 318 | Gabi and Rafa (EuSouTwins) | BR | Instagram | @eusoutwins | 50K+ | HIGH | 7 | Teaching duo; AI strategies |
| 319 | Rocketseat IG | BR | Instagram | @rocketseat | 50K+ | HIGH | 7 | Programming, AI courses |
| 320 | Camila Achutti | BR | Instagram | @camilaachutti | 40K+ | HIGH | 7 | Mastertech founder |
| 321 | Rafael Milagre IG | BR | Instagram | @rafaelmilagre | 40K+ | HIGH | 7 | Viver de IA; ESPM prof |
| 322 | Paulo Aguiar | BR | Instagram | @paulo.ia | 35K+ | HIGH | 7 | CR_IA co-founder |
| 323 | Tudo Sobre IA | BR | Instagram | @tudosobre.ai | 30K | HIGH | 7 | Dedicated AI profile |
| 324 | Rafaella Ballerini IG | BR | Instagram | @rafaballerini | 30K+ | MEDIUM | 4 | Frontend, women in tech |
| 325 | Filipe Deschamps IG | BR | Instagram | @filipedeschamps | 30K+ | HIGH | 6 | Newsletter powerhouse |
| 326 | Silvio Meira | BR | Instagram | @silviomeira | 28K | HIGH | 7 | Chief Scientist TDS.company |
| 327 | Diego Almeida | BR | Instagram | @diegoalmeida.ia | 25K+ | HIGH | 7 | AI tool compilations |
| 328 | Attekita Dev IG | BR | Instagram | @attekitadev | 25K+ | MEDIUM | 4 | International career |
| 329 | Erick Wendel IG | BR | Instagram | @erickwendel_ | 20K+ | HIGH | 6 | Conference speaker |
| 330 | Codigo Fonte IG | BR | Instagram | @codigofontetv | 20K+ | MEDIUM | 4 | Dev culture |
| 331 | Thassius Veloso | BR | Instagram | @thassius | 19K | MEDIUM | 4 | Tech journalist |
| 332 | DIO | BR | Instagram | @digitalinnovationone | 40K+ | MEDIUM | 4 | Dev education |
| 333 | Data Hackers IG | BR | Instagram | @datahackersbr | 15K+ | HIGH | 7 | 45K+ community |
| 334 | WoMakersCode | BR | Instagram | @womakerscodebr | 15K+ | MEDIUM | 4 | Women in IT; also 5K+ community org; merged from Community #622 |
| 335 | IlustraDev | BR | Instagram | @ilustradev | 15K+ | MEDIUM | 4 | Illustrated programming |
| 336 | Verena Paccola | BR | Instagram | @verenapaccola | 15K+ | MEDIUM | 4 | Interdisciplinary tech |
| 337 | Fabio Akita IG | BR | Instagram | @akitaonrails | 15K+ | HIGH | 6 | CS deep dives |
| 338 | Lucas Montano IG | BR | Instagram | @lucasmontano | 15K+ | MEDIUM | 4 | Career, mobile dev |
| 339 | Mayk Brito | BR | Instagram | @maaborykbrito | 15K+ | MEDIUM | 4 | HTML, CSS, JS |
| 340 | Cod3r IG | BR | Instagram | @cod3r_ | 15K+ | MEDIUM | 4 | Fullstack courses |
| 341 | LinuxTips IG | BR | Instagram | @linuxtips | 15K+ | HIGH | 6 | DevOps training |
| 342 | DevSuperior IG | BR | Instagram | @devsuperior | 15K+ | MEDIUM | 4 | Java, Spring Boot |
| 343 | Laboratorio da Julia | BR | Instagram | @labdajulia | 12K+ | MEDIUM | 4 | Student perspective |
| 344 | Programacao Dinamica IG | BR | Instagram | @progdinamica | 12K+ | HIGH | 6 | Academic CS |
| 345 | Glaucia Lemos IG | BR | Instagram | @glaucialemos_ | 12K+ | HIGH | 6 | Node, AI, Microsoft |
| 346 | Diolinux IG | BR | Instagram | @diolinux | 12K+ | MEDIUM | 4 | FOSS advocate |
| 347-363 | (Additional BR IG T3 contacts) | BR | Instagram | various | 10K+ each | MEDIUM-HIGH | 3-5 | See source kc_influencer_directory_br.md entries #90-117 |

### 5.8 T3 BR -- Twitter/X (51 contacts)

| # | Name | Region | Platform | Handle | Followers | Relevance | Priority | Notes |
|---|------|--------|----------|--------|-----------|-----------|----------|-------|
| 364 | Silvio Meira | BR | Twitter/X | @silvio | 80K+ | HIGH | 7 | Innovation, digital strategy |
| 365 | Filipe Deschamps | BR | Twitter/X | @filipedeschamps | 80K+ | HIGH | 7 | Tech news, open source |
| 366 | Atila Iamarino | BR | Twitter/X | @oatila | 80K+ | MEDIUM | 4 | Nerdologia; PhD |
| 367 | Fabio Akita | BR | Twitter/X | @AkitaOnRails | 60K+ | HIGH | 7 | CS fundamentals, career |
| 368 | Nina da Hora | BR | Twitter/X | @ninahora | 50K+ | HIGH | 7 | AI ethics, diversity |
| 369 | Gustavo Caetano | BR | Twitter/X | @gustcaetano | 40K+ | MEDIUM | 4 | Samba Tech founder |
| 370 | Diego Fernandes | BR | Twitter/X | @diegoFernandes | 30K+ | HIGH | 7 | Rocketseat CTO |
| 371 | Erick Wendel X | BR | Twitter/X | @erickwendel_ | 30K+ | HIGH | 7 | JS, Node.js |
| 372 | Lucas Montano X | BR | Twitter/X | @lucasmontano | 20K+ | MEDIUM | 4 | Career, mobile |
| 373 | PrimoDev | BR | Twitter/X | @primodev | 20K+ | MEDIUM | 4 | Dev + finance |
| 374 | Paulo Silveira | BR | Twitter/X | @paulo_caelum | 20K+ | MEDIUM | 4 | Alura co-founder |
| 375 | Gabriel Pato X | BR | Twitter/X | @gabrielpato | 20K+ | MEDIUM | 4 | Security |
| 376 | Andre Lug X | BR | Twitter/X | @andre_lug | 15K+ | HIGH | 7 | AI + productivity |
| 377 | Jeferson Fernando X | BR | Twitter/X | @badtux_ | 15K+ | HIGH | 6 | LinuxTips founder |
| 378 | Camila Achutti X | BR | Twitter/X | @camilaachutti | 15K+ | HIGH | 6 | Mastertech |
| 379 | Rafael Milagre X | BR | Twitter/X | @rafaelmilagre | 15K+ | HIGH | 7 | Viver de IA |
| 380 | Mano Deyvin | BR | Twitter/X | @manodeyvin | 15K+ | MEDIUM | 4 | Dev humor |
| 381 | Rafaella Ballerini X | BR | Twitter/X | @rafaballerini | 15K+ | MEDIUM | 4 | Frontend |
| 382 | Glaucia Lemos X | BR | Twitter/X | @glaboremos | 15K+ | HIGH | 6 | Microsoft advocate |
| 383 | Augusto Backes X | BR | Twitter/X | @augustobackes | 15K+ | LOW | 3 | Blockchain |
| 384 | Mayk Brito X | BR | Twitter/X | @maykbrito | 15K+ | MEDIUM | 4 | Frontend educator |
| 385-414 | (Remaining BR X T3) | BR | Twitter/X | various | 10K+ each | MEDIUM-HIGH | 3-7 | See source entries #126-169 |

### 5.9 T3 BR -- LinkedIn (42 contacts)

| # | Name | Region | Platform | Followers | Relevance | Priority | Notes |
|---|------|--------|----------|-----------|-----------|----------|-------|
| 415 | Leo Candido | BR | LinkedIn | 50K+ | HIGH | 7 | LinkedIn Top Voice AI |
| 416 | Silvio Meira LI | BR | LinkedIn | 80K+ | HIGH | 7 | TDS.company |
| 417 | Gustavo Caetano LI | BR | LinkedIn | 60K+ | MEDIUM | 4 | Samba Tech/Digital |
| 418 | Paulo Silveira LI | BR | LinkedIn | 50K+ | MEDIUM | 4 | Alura co-founder |
| 419 | Ricardo Amorim | BR | LinkedIn | 30K+ | MEDIUM | 4 | Economist, Top Voice |
| 420 | Diego Fernandes LI | BR | LinkedIn | 30K+ | HIGH | 7 | Rocketseat CTO |
| 421 | Camila Achutti LI | BR | LinkedIn | 30K+ | HIGH | 7 | Mastertech founder |
| 422 | Joel Jota | BR | LinkedIn | 25K+ | LOW | 2 | Business, high performance |
| 423 | Igla Generoso | BR | LinkedIn | 25K+ | MEDIUM | 4 | DIO CEO |
| 424 | Sergio Gaiotto | BR | LinkedIn | 20K+ | HIGH | 7 | Chief Data & AI, Claro |
| 425 | Rafael Milagre LI | BR | LinkedIn | 20K+ | HIGH | 7 | Viver de IA |
| 426 | Rony Meisler | BR | LinkedIn | 20K+ | MEDIUM | 4 | Reserva co-founder |
| 427 | Flavio Augusto | BR | LinkedIn | 40K+ | LOW | 2 | Entrepreneur |
| 429 | Onedio Seabra Jr | BR | LinkedIn | 15K+ | HIGH | 7 | i2AI President |
| 430 | Ana Paula Appel | BR | LinkedIn | 15K+ | HIGH | 7 | IBM; TDC Summit speaker; also conference speaker (AI research); merged from Conf #473 |
| 431 | Marcos Santos | BR | LinkedIn | 15K+ | HIGH | 7 | Aquarela Analytics CEO |
| 432 | Danilo Gato LI | BR | LinkedIn | 15K+ | HIGH | 8 | CPDF founder |
| 433 | Marcello Zillo | BR | LinkedIn | 12K+ | HIGH | 6 | Google Cloud; also conference speaker (cybersecurity, cloud); merged from Conf #476 |
| 434 | Gabriela Haddad | BR | LinkedIn | 12K+ | HIGH | 6 | Accenture |
| 435 | Elder Moraes | BR | LinkedIn | 12K+ | HIGH | 6 | IBM |
| 436 | Arthur Fucher | BR | LinkedIn | 12K+ | HIGH | 6 | Nubank; also conference speaker (data, AI at scale); merged from Conf #474 |
| 437-456 | (Remaining BR LI T3) | BR | LinkedIn | 10K+ each | MEDIUM-HIGH | 4-7 | See source entries #183-211 |

### 5.10 T3 BR -- Podcasts (22 contacts)

| # | Name | Region | Platform | Show | Relevance | Priority | Notes |
|---|------|--------|----------|------|-----------|----------|-------|
| 458 | IA Sob Controle | BR | Podcast | IA Sob Controle | HIGH | 7 | AI news, interviews |
| 459 | Papo de IA | BR | Podcast | Danilo Gato | HIGH | 8 | #1 tech on Spotify |
| 460 | Vida com IA | BR | Podcast | Filipe Lauar | HIGH | 7 | AI accessible language |
| 461 | IA para Negocios | BR | Podcast | Leandro Aveiro | HIGH | 7 | AI for business |
| 462 | IA Aplicada | BR | Podcast | Guilherme Favaron | HIGH | 7 | AI applications |
| 463 | Folha Artificial | BR | Podcast | Pablo Mascarenhas | HIGH | 7 | AI weekly news |
| 464 | Be-a-ba da IA | BR | Podcast | Fernando Melo | HIGH | 6 | Radio Senado |
| 465 | Pizza de Dados | BR | Podcast | team | HIGH | 7 | Data science pod |
| 466 | DevNaEstrada | BR | Podcast | team | MEDIUM | 4 | Dev career |
| 467 | Lambda3 Podcast | BR | Podcast | Lambda3 | MEDIUM | 4 | Enterprise tech |
| 468 | Viver de IA Pod | BR | Podcast | Rafael Milagre | HIGH | 7 | AI for business leaders |
| 469 | Act4AI | BR | Podcast | Danilo | HIGH | 7 | AI dev interviews |
| 470 | SABIA | BR | Podcast | Unicamp students | HIGH | 6 | Academic AI |
| 471 | Cafe com IA | BR | Podcast | Inner AI | HIGH | 7 | 100% AI-narrated; also 10K+ newsletter; merged from NL #625 |

### 5.11 T3 BR -- Event Speakers/Organizers (25 contacts)

| # | Name | Region | Platform | Focus | Relevance | Priority | Notes |
|---|------|--------|----------|-------|-----------|----------|-------|
| 472 | Adriano Pereira | BR | Conference | AI healthcare | HIGH | 6 | UFMG; InWeb |
| 475 | Junia Ortiz | BR | Conference | Deep learning, NLP, LLMs | HIGH | 7 | SENAI CIMATEC; also academic researcher (DL, NLP, LLMs); merged from Acad #497 |
| 477 | Ricardo Saraiva | BR | Conference | AI, metaverse | HIGH | 6 | AIAT President |
| 478 | Evandro Rosa | BR | Conference | Quantum computing | HIGH | 6 | Quantuloop |
| 479 | Daniel Collaco | BR | Conference | Software innovation | HIGH | 7 | NASA Space Apps winner |
| 480 | Clarissa Lopes | BR | Conference | Future strategy | HIGH | 6 | Deloitte |
| 481 | Augusto Salomon | BR | Conference | AI innovation | HIGH | 6 | StarMind CEO |
| 482 | Diego Bonilla | BR | Conference | Software engineering | HIGH | 7 | Nareia CEO |
| 483 | Rafael Guerra | BR | Conference | E-commerce AI | HIGH | 6 | Sinatra founder |
| 484 | StartSe | BR | Conference | AI Festival 2026 | HIGH | 7 | Largest AI event BR |
| 485 | IA Conference Brasil | BR | Conference | IA Conference 2026 | HIGH | 7 | Major AI conference |
| 486 | AI Summit Brasil | BR | Conference | AI Summit 2026 | HIGH | 7 | Most technical AI congress LatAm |
| 487 | TDC | BR | Conference | TDC Summit IA 2026 | HIGH | 7 | Largest dev conference BR |
| 488 | BrazilJS Conf | BR | Conference | BrazilJS Conference | HIGH | 7 | Largest JS event LatAm |

### 5.12 T3 BR -- University Researchers (22 contacts)

| # | Name | Region | Platform | Institution | Relevance | Priority | Notes |
|---|------|--------|----------|-------------|-----------|----------|-------|
| 489 | Sandra E. F. de Avila | BR | Academic | Unicamp | HIGH | 6 | ML, AI |
| 490 | Washington L. M. da Cunha | BR | Academic | Unicamp | HIGH | 6 | ML, AI, NLP |
| 491 | Leandro A. Villas | BR | Academic | Unicamp | HIGH | 6 | ML, cloud, AI |
| 492 | Joao M. T. Romano | BR | Academic | Unicamp | HIGH | 6 | FEEC AI Center lead |
| 493 | Claudio M. Toledo | BR | Academic | USP | HIGH | 6 | AI, optimization |
| 494 | Julio C. Estrella | BR | Academic | USP | HIGH | 6 | AI, intelligent systems |
| 495 | Roberto C. S. Pacheco | BR | Academic | UFSC | HIGH | 6 | Digital platforms |
| 496 | Paulo Silvestre | BR | Academic | Mackenzie/PUC-SP | HIGH | 6 | AI, digital culture |
| 498 | Joao M. S. Souza | BR | Academic | SENAI CIMATEC | HIGH | 6 | Quantum computing |
| 499 | Marcio B. Amaral | BR | Academic | HC FMUSP | HIGH | 6 | AI engineering, healthcare |

### 5.13 T3 BR -- Education Platform Leaders (14 contacts)

| # | Name | Region | Platform | Organization | Relevance | Priority | Notes |
|---|------|--------|----------|-------------|-----------|----------|-------|
| 500 | Paulo Silveira | BR | Education | Alura | MEDIUM | 4 | CVO Grupo Alun |
| 501 | Guilherme Silveira | BR | Education | Alura | MEDIUM | 4 | 20+ years teaching |
| 502 | Diego Fernandes | BR | Education | Rocketseat | HIGH | 7 | CTO |
| 503 | Mayk Brito | BR | Education | Rocketseat | MEDIUM | 4 | CCO/Senior Dev |
| 504 | Igla Generoso | BR | Education | DIO | MEDIUM | 4 | 1M+ developers |
| 505 | Camila Achutti | BR | Education | Mastertech | HIGH | 7 | Founder |
| 506 | Marcel Nobre | BR | Education | BetaLab | HIGH | 7 | Innovation + AI education |

---

## 6. T4 Micro-Influencers (<10K)

T4 micro-influencers are community builders and niche creators with often the highest engagement rates. They are the grassroots seeding layer.

### 6.1 T4 GLOBAL -- Discord Server Admins (22 contacts)

| # | Name/Community | Region | Platform | Members | Relevance | Priority | Notes |
|---|---------------|--------|----------|---------|-----------|----------|-------|
| 507 | LangChain Discord | GLOBAL | Discord | 30K+ | HIGH | 7 | Framework community |
| 508 | HuggingFace Discord | GLOBAL | Discord | 50K+ | HIGH | 7 | ML model hub |
| 509 | CrewAI Discord | GLOBAL | Discord | 10K+ | HIGH | 8 | Multi-agent crews; direct competitor space |
| 510 | AutoGPT Discord | GLOBAL | Discord | 20K+ | HIGH | 7 | Autonomous agents |
| 511 | n8n Discord | GLOBAL | Discord | 25K+ | HIGH | 7 | Workflow automation |
| 512 | OpenRouter Discord | GLOBAL | Discord | 8K+ | HIGH | 7 | Multi-model API |
| 513 | Ollama Discord | GLOBAL | Discord | 15K+ | HIGH | 8 | Local LLMs; CEX runtime |
| 514 | AnythingLLM Discord | GLOBAL | Discord | 6K+ | HIGH | 7 | Self-hosted LLM |
| 515 | Continue Discord | GLOBAL | Discord | 10K+ | HIGH | 7 | AI coding assistant |
| 516 | SuperAGI Discord | GLOBAL | Discord | 8K+ | HIGH | 7 | Agent architecture |
| 517 | Open WebUI Discord | GLOBAL | Discord | 10K+ | HIGH | 7 | Self-hosted chat |
| 518 | GPT Researcher Discord | GLOBAL | Discord | 5K+ | HIGH | 7 | Research automation |
| 519 | Langroid Discord | GLOBAL | Discord | 3K+ | HIGH | 7 | Multi-agent LLM |
| 520 | Semantic Kernel Discord | GLOBAL | Discord | 8K+ | HIGH | 7 | Microsoft LLM SDK |
| 521 | Dify Discord | GLOBAL | Discord | 20K+ | HIGH | 7 | Visual agent builder |
| 522 | Perplexity Discord | GLOBAL | Discord | 10K+ | MEDIUM | 5 | AI search |
| 523 | Voiceflow Discord | GLOBAL | Discord | 12K+ | MEDIUM | 5 | Conversational AI |
| 524 | Botpress Discord | GLOBAL | Discord | 15K+ | MEDIUM | 5 | Chatbot platform |
| 525 | Learn AI Together | GLOBAL | Discord | 30K+ | MEDIUM | 5 | Learning community |
| 526 | Lablab AI Discord | GLOBAL | Discord | 15K+ | MEDIUM | 5 | AI hackathons |
| 527 | Phind Discord | GLOBAL | Discord | 8K+ | MEDIUM | 5 | Dev search |
| 528 | Groq Discord | GLOBAL | Discord | 8K+ | MEDIUM | 5 | Fast AI inference |

### 6.2 T4 GLOBAL -- Reddit Moderators (18 contacts)

| # | Subreddit | Region | Members | Relevance | Priority | Notes |
|---|-----------|--------|---------|-----------|----------|-------|
| 529 | r/MachineLearning | GLOBAL | 3.0M | HIGH | 7 | Premier ML subreddit |
| 530 | r/ClaudeAI | GLOBAL | 747K | HIGH | 8 | Claude/Anthropic ecosystem; CEX primary runtime |
| 531 | r/LocalLLaMA | GLOBAL | 694K | HIGH | 8 | Local LLM community; sovereignty narrative |
| 532 | r/LangChain | GLOBAL | 80K+ | HIGH | 7 | LangChain framework |
| 533 | r/ChatGPT | GLOBAL | 11.4M | MEDIUM | 5 | Largest ChatGPT sub |
| 534 | r/singularity | GLOBAL | 3.9M | MEDIUM | 4 | AGI/singularity |
| 535 | r/artificial | GLOBAL | 700K+ | MEDIUM | 4 | General AI news |
| 536 | r/OpenAI | GLOBAL | 1.5M+ | MEDIUM | 5 | OpenAI ecosystem |
| 537 | r/PromptEngineering | GLOBAL | 200K+ | HIGH | 7 | Prompt design |
| 538 | r/AutoGPT | GLOBAL | 100K+ | HIGH | 7 | Autonomous agents |
| 539 | r/ArtificialIntelligence | GLOBAL | 400K+ | MEDIUM | 4 | AI news broad |
| 540 | r/learnmachinelearning | GLOBAL | 350K+ | MEDIUM | 4 | ML learning |
| 541 | r/deeplearning | GLOBAL | 150K+ | MEDIUM | 4 | DL research |
| 542 | r/MLOps | GLOBAL | 30K+ | HIGH | 7 | ML operations |
| 543 | r/ollama | GLOBAL | 50K+ | HIGH | 8 | Ollama/local LLMs; CEX runtime |
| 544 | r/SelfHosted | GLOBAL | 400K+ | MEDIUM | 5 | Self-hosted AI apps |
| 545 | r/datascience | GLOBAL | 500K+ | LOW | 3 | Data science pros |
| 546 | r/StableDiffusion | GLOBAL | 700K+ | LOW | 2 | Image generation |

### 6.3 T4 GLOBAL -- Blog/Substack Authors & Company Blogs

| # | Name/Org | Region | Platform | Audience | Relevance | Priority | Notes |
|---|----------|--------|----------|----------|-----------|----------|-------|
| 547 | Omar Sanseviero | GLOBAL | Blog | 15K+ | HIGH | 7 | HF dev advocacy |
| 548 | Neel Nanda | GLOBAL | Blog | 20K+ | HIGH | 7 | Mechanistic interpretability |
| 549 | Aparna Dhinakaran | GLOBAL | Blog | 15K+ | MEDIUM | 5 | AI observability |
| 550 | Matt Rickard | GLOBAL | Blog | 20K+ | MEDIUM | 5 | AI infra, eng mgmt |
| 551 | Pratik Bhavsar | GLOBAL | Blog | 15K+ | MEDIUM | 5 | NLP engineering |
| 552 | Zac Hatfield-Dodds | GLOBAL | Blog | 15K+ | HIGH | 7 | Hypothesis, ML testing |
| 553 | Patrick Lewis | GLOBAL | Blog | Academic | HIGH | 7 | RAG original author |
| 554 | Cohere blog | GLOBAL | Blog | 50K+ | MEDIUM | 5 | Enterprise LLMs |
| 555 | OpenAI blog | GLOBAL | Blog | 1M+ | MEDIUM | 4 | GPT research |
| 556 | DeepMind blog | GLOBAL | Blog | 500K+ | LOW | 3 | AGI research |
| 557 | Meta AI blog | GLOBAL | Blog | 300K+ | MEDIUM | 4 | Open-source AI |

### 6.4 T4 GLOBAL -- Remaining Newsletters, Podcasts, LinkedIn

| # | Name | Region | Platform | Audience | Relevance | Priority | Notes |
|---|------|--------|----------|----------|-----------|----------|-------|
| 558 | Nathaniel Whittemore | GLOBAL | Podcast | 50K+ | MEDIUM | 5 | AI Daily Brief |
| 559 | Rachel Woods | GLOBAL | Podcast | 20K+ | MEDIUM | 5 | AI Exchange |
| 560 | Modern CTO | GLOBAL | Podcast | 8K YT | MEDIUM | 5 | CTO interviews |
| 561 | Timothy B. Lee | GLOBAL | Newsletter | 25K+ | MEDIUM | 5 | Understanding AI |
| 562 | Melanie Mitchell | GLOBAL | Newsletter | 20K+ | MEDIUM | 5 | AI Guide |
| 563 | Jurgen Appelo | GLOBAL | Newsletter | 15K+ | MEDIUM | 5 | Meta-curator |
| 564 | Ruben Hassid | GLOBAL | Newsletter | 30K+ | MEDIUM | 5 | How to AI |
| 565 | Matthew Linley | GLOBAL | Newsletter | 10K+ | MEDIUM | 5 | Supervised |
| 566 | AI Tidbits | GLOBAL | Newsletter | 20K+ | MEDIUM | 5 | Bite-sized AI |
| 567 | Last Week in AI | GLOBAL | Newsletter | 30K+ | MEDIUM | 5 | AI news roundup |
| 568 | AI Weekly | GLOBAL | Newsletter | 15K+ | MEDIUM | 5 | Professional AI |
| 569 | Pete Huang | GLOBAL | Newsletter | 550K+ shared | MEDIUM | 5 | The Neuron co-editor |
| 570 | Product Power AI | GLOBAL | Newsletter | 10K+ | MEDIUM | 5 | AI product strategy |
| 571 | GenAI Works | GLOBAL | Newsletter | 50K+ | MEDIUM | 5 | Enterprise AI |
| 572 | Jean Ng | GLOBAL | LinkedIn | 20K+ | LOW | 3 | Influencer list curator |
| 573 | Daliana Liu | GLOBAL | LinkedIn | 100K+ | MEDIUM | 4 | DS educator |
| 574 | Ravit Jain | GLOBAL | LinkedIn | 100K+ | MEDIUM | 4 | AI community building |
| 575 | Arize AI (Phoenix) | GLOBAL | GitHub | 10K+ | MEDIUM | 5 | AI observability |
| 576 | Activepieces | GLOBAL | GitHub | 12K+ | MEDIUM | 5 | OSS Zapier alternative |
| 577 | Rasa | GLOBAL | GitHub | 19K+ | MEDIUM | 5 | Conversational AI |
| 578 | Sinaptik AI (PandasAI) | GLOBAL | GitHub | 15K+ | MEDIUM | 5 | Chat with data |
| 579 | Microsoft TaskWeaver | GLOBAL | GitHub | 5K+ | MEDIUM | 5 | Data analytics agents |
| 580 | Pradip Nichite YT | GLOBAL | YouTube | 7K | MEDIUM | 4 | NLP tutorials |
| 581 | Jay Shah YT | GLOBAL | YouTube | 7K | MEDIUM | 4 | Industry ML |

### 6.5 T4 BR -- Telegram/Community Groups (32 contacts)

| # | Community | Region | Platform | Members | Relevance | Priority | Notes |
|---|-----------|--------|----------|---------|-----------|----------|-------|
| 582 | Os Programadores | BR | Telegram | 10K+ | HIGH | 7 | Largest BR dev group |
| 583 | Python Brasil | BR | Telegram | 8K+ | HIGH | 7 | Official Python BR |
| 584 | JS Brasil | BR | Telegram | 5K+ | HIGH | 6 | JS community |
| 585 | Devs Brasil | BR | Telegram | 5K+ | HIGH | 6 | General dev |
| 586 | IA Brasil (Oficial) | BR | Telegram | 5K+ | HIGH | 8 | Largest AI discussion group BR |
| 587 | Node.js Brasil | BR | Telegram | 3K+ | HIGH | 6 | Node community |
| 588 | DevOps BR | BR | Telegram | 3K+ | HIGH | 6 | Infrastructure |
| 589 | Docker BR | BR | Telegram | 3K+ | HIGH | 6 | Containers |
| 590 | AWS Users BR | BR | Telegram | 3K+ | HIGH | 6 | Cloud community |
| 591 | PHP Brasil | BR | Telegram | 3K+ | MEDIUM | 4 | PHP community |
| 592 | Frontend Brasil | BR | Telegram | 3K+ | MEDIUM | 4 | Frontend dev |
| 593 | Flutter Brasil | BR | Telegram | 3K+ | MEDIUM | 4 | Mobile dev |
| 594 | React.js BR | BR | Telegram | 2K+ | HIGH | 6 | React community |
| 595 | Go BR | BR | Telegram | 2K+ | HIGH | 6 | Go community |
| 596 | VueJS Brasil | BR | Telegram | 2K+ | MEDIUM | 4 | Vue community |
| 597 | .NET Brasil | BR | Telegram | 2K+ | MEDIUM | 4 | .NET community |
| 598 | PostgreSQL Brasil | BR | Telegram | 2K+ | MEDIUM | 4 | Database |
| 599 | Laravel BR | BR | Telegram | 2K+ | MEDIUM | 4 | Laravel framework |
| 600 | CaveiraTech | BR | Telegram | 2K+ | MEDIUM | 4 | Cybersecurity |
| 601 | EthereumBR | BR | Telegram | 2K+ | MEDIUM | 4 | Web3/Ethereum |
| 602 | Grupy-SP | BR | Telegram | 2K+ | HIGH | 6 | Python Sao Paulo |
| 603 | Elixir Brasil | BR | Telegram | 1K+ | MEDIUM | 4 | Elixir community |
| 604 | Ruby Brasil | BR | Telegram | 1K+ | MEDIUM | 4 | Ruby community |
| 605 | MongoDB Brasil | BR | Telegram | 1K+ | MEDIUM | 4 | NoSQL |
| 606 | GraphQL Brasil | BR | Telegram | 1K+ | HIGH | 6 | API tech |
| 607 | API Builders BR | BR | Telegram | 1K+ | HIGH | 6 | API development |
| 608 | Programacao Funcional BR | BR | Telegram | 1K+ | HIGH | 5 | Functional programming |
| 609 | Rust Floripa | BR | Telegram | 500+ | HIGH | 5 | Rust community |
| 610 | Programadores BR | BR | Discord | 32K+ | HIGH | 7 | Largest BR dev Discord |
| 611 | He4rt Developers | BR | Discord | 10K+ | HIGH | 7 | Non-profit; beginner-friendly; also community org; merged from Community #621 |
| 612 | Data Hackers | BR | Slack | 45K+ | HIGH | 8 | Data science + AI community |
| 613 | Training Center | BR | Slack/Discord | 5K+ | MEDIUM | 4 | Knowledge sharing; also community org (education); merged from Community #624 |

### 6.6 T4 BR -- Community Leaders & Meetup Organizers (11 contacts)

| # | Name/Org | Region | Platform | Members | Relevance | Priority | Notes |
|---|----------|--------|----------|---------|-----------|----------|-------|
| 614 | Allan Sene | BR | Community | 45K+ | HIGH | 8 | Data Hackers + Dadosfera; also 15K+ LinkedIn; merged from LI #428 |
| 615 | Paulo Vasconcellos | BR | Community | -- | HIGH | 6 | Data Hackers co-founder |
| 616 | Gabriel Lages | BR | Community | -- | HIGH | 6 | Data Hackers co-founder |
| 617 | AI Brasil Meetup | BR | Meetup | 5K+ | HIGH | 7 | Largest AI meetup BR |
| 618 | AI Tinkerers SP | BR | Meetup | 2K+ | HIGH | 8 | Builder-focused; ideal for CEX demo |
| 619 | SP AI Developer Group | BR | Meetup | 3K+ | HIGH | 7 | Tech talks + workshops |
| 620 | AI Professionals SP | BR | Meetup | 70K+ | HIGH | 6 | Global with SP chapter |
| 623 | Devs Java Girl | BR | Community | 2K+ | MEDIUM | 4 | Women + Java |

### 6.7 T4 BR -- Remaining Newsletter, Podcast, Education entries

| # | Name | Region | Platform | Audience | Relevance | Priority | Notes |
|---|------|--------|----------|----------|-----------|----------|-------|
| 626 | IA Todo Dia NL | BR | Newsletter | 15K+ | HIGH | 7 | Companion to podcast |
| 627 | Manual do Usuario | BR | Newsletter | 15K+ | HIGH | 6 | Independent tech journalism |
| 628 | iMasters | BR | Newsletter | 10K+ | MEDIUM | 4 | Developer community |
| 629 | Folha Artificial NL | BR | Newsletter | 5K+ | HIGH | 6 | Tuesday AI digest |
| 630 | IA Sob Controle NL | BR | Newsletter | 5K+ | HIGH | 6 | Companion to podcast |
| 631 | Digitalmente | BR | Newsletter | 5K+ | MEDIUM | 4 | Tech and society |
| 632 | The News BR | BR | Newsletter | 30K+ | MEDIUM | 4 | Portuguese business |
| 633 | Tecnoblog NL | BR | Newsletter | 30K+ | MEDIUM | 4 | Daily tech |
| 634 | Olhar Digital NL | BR | Newsletter | 20K+ | MEDIUM | 4 | Daily tech |
| 635 | Hack n Cast | BR | Podcast | 5K+ | MEDIUM | 4 | FOSS podcast |
| 636 | KardiaCast | BR | Podcast | growing | MEDIUM | 4 | Healthcare + AI |
| 637 | Mente Aberta | BR | Podcast | growing | MEDIUM | 4 | AI, YouTube, philosophy |
| 638 | Juliana Amoasei | BR | Education | Alura | MEDIUM | 4 | Alura instructor |

---

## 7. Platform Distribution Analysis

### Which platforms have the most contacts?

| Platform | Global | BR | Total | % | Avg Relevance |
|----------|--------|-----|-------|---|---------------|
| Twitter/X | 100 | 52 | 152 | 20.6% | MEDIUM-HIGH (56% HIGH) |
| YouTube | 68 | 55 | 123 | 16.7% | MEDIUM-HIGH (44% HIGH) |
| Instagram | 0 | 62 | 62 | 8.4% | MEDIUM (52% HIGH) |
| Conference/Speaker | 32 | 25 | 57 | 7.7% | MEDIUM-HIGH (66% HIGH) |
| Podcast | 28 | 22 | 50 | 6.8% | HIGH (68% HIGH) |
| LinkedIn | 7 | 42 | 49 | 6.6% | MEDIUM-HIGH (57% HIGH) |
| GitHub | 48 | 0 | 48 | 6.5% | VERY HIGH (90% HIGH) |
| Newsletter | 32 | 16 | 48 | 6.5% | HIGH (63% HIGH) |
| Telegram | 0 | 32 | 32 | 4.3% | HIGH (69% HIGH) |
| Blog/Substack | 30 | 0 | 30 | 4.1% | HIGH (73% HIGH) |
| Discord | 22 | 2 | 24 | 3.3% | HIGH (71% HIGH) |
| Academic | 0 | 22 | 22 | 3.0% | HIGH (82% HIGH) |
| Reddit | 18 | 0 | 18 | 2.4% | HIGH (56% HIGH) |
| Education | 0 | 14 | 14 | 1.9% | MEDIUM (36% HIGH) |
| Community | 0 | 11 | 11 | 1.5% | HIGH (73% HIGH) |

### Highest Relevance Density Platforms (>70% HIGH relevance)

1. **GitHub** (90% HIGH) -- Open-source maintainers are the highest-value targets for CEX
2. **Academic** (82% HIGH) -- University researchers cover typed systems and ML infrastructure
3. **Blog/Substack** (73% HIGH) -- Technical writers whose audience directly overlaps CEX users
4. **Community Leaders** (73% HIGH) -- Grassroots organizers who amplify within niche communities
5. **Discord** (71% HIGH) -- Server admins for agent framework communities

### Platform-CEX Fit Assessment

| Platform | CEX Fit Score | Rationale |
|----------|--------------|-----------|
| GitHub | 10/10 | OSS project → star, fork, PR = direct adoption signal |
| Twitter/X | 9/10 | Viral reach + developer community engagement |
| YouTube | 8/10 | Demo-ability (8F trace, 4-runtime dispatch) = compelling content |
| Discord | 8/10 | Community seeding in competitor spaces (LangChain, CrewAI, Ollama) |
| Reddit | 8/10 | r/LocalLLaMA and r/ClaudeAI = sovereignty narrative |
| Newsletter | 7/10 | Feature/mention generates sustained traffic |
| Blog/Substack | 7/10 | Technical deep-dives match CEX complexity |
| Podcast | 7/10 | Guest appearance for "AI Brain" narrative |
| LinkedIn | 6/10 | Enterprise CTO audience for governance narrative |
| Telegram | 6/10 | BR developer communities for localized seeding |
| Instagram | 5/10 | Visual AI demos possible but not core developer audience |
| Conference | 5/10 | Long lead time but high credibility |
| Academic | 4/10 | Publication pathway but slow adoption cycle |

---

## 8. Outreach Priority Matrix -- Top 50

Top 50 contacts ranked by composite score: (relevance x reach x engagement x platform_fit).
These are the first 50 to contact in the CEX open-source seeding campaign.

| Rank | Name | Region | Platform | Priority Score | Tier | Relevance | Why First |
|------|------|--------|----------|---------------|------|-----------|-----------|
| 1 | Danilo Gato | BR | Multi (YT/IG/X/Pod/LI) | 10 | T2 | HIGH | #1 AI content creator BR; cross-platform; CPDF community; FGV prof |
| 2 | Simon Willison | GLOBAL | GitHub/Blog/X | 9 | T3 | HIGH | Creator llm, datasette; OSS CLI tools; typed systems advocate |
| 3 | Harrison Chase | GLOBAL | GitHub/X | 9 | T3 | HIGH | CEO LangChain; positioning as competitor validates CEX category |
| 4 | Joao Moura | GLOBAL | GitHub/X | 9 | T3 | HIGH | Founder CrewAI; Brazilian; multi-agent pioneer |
| 5 | Swyx (Shawn Wang) | GLOBAL | NL/Pod/X/Blog | 9 | T2 | HIGH | Latent Space; top AI engineering voice; "AI Engineer" popularizer |
| 6 | Yohei Nakajima | GLOBAL | Twitter/X/GH | 9 | T2 | HIGH | Creator BabyAGI; agent framework pioneer |
| 7 | Filipe Deschamps | BR | NL/YT/Pod/X | 9 | T2 | HIGH | Largest BR tech newsletter; TabNews; OSS community |
| 8 | Rocketseat (Diego Fernandes) | BR | YT/IG/LI | 9 | T1 | HIGH | 55K+ students; covers AI tooling |
| 9 | Rafael Milagre | BR | Multi (YT/IG/X/LI/Pod) | 9 | T2 | HIGH | Viver de IA; largest AI education BR; ESPM prof |
| 10 | Paul Gauthier | GLOBAL | GitHub | 9 | T3 | HIGH | Aider; AI pair programming; direct use case overlap |
| 11 | Fabio Akita | BR | YouTube/X | 9 | T2 | HIGH | Deep technical authority; respected in BR dev community |
| 12 | Ollama team | GLOBAL | GitHub/Discord | 9 | T3 | HIGH | 162K stars; CEX runtime partner |
| 13 | Anthropic MCP | GLOBAL | GitHub | 9 | T3 | HIGH | MCP spec; CEX uses MCP |
| 14 | Fireship | GLOBAL | YouTube | 8 | T1 | HIGH | 4M subs; 100-second format ideal for CEX demo |
| 15 | sentdex | GLOBAL | YouTube | 8 | T1 | HIGH | 1.4M; Python ML tutorials; direct audience match |
| 16 | Amjad Masad | GLOBAL | Twitter/X | 8 | T1 | HIGH | CEO Replit; AI coding tools |
| 17 | Francois Chollet | GLOBAL | Twitter/X | 8 | T2 | HIGH | Creator of Keras; typed systems thinker |
| 18 | Soumith Chintala | GLOBAL | Twitter/X | 8 | T2 | HIGH | PyTorch; ML systems builder |
| 19 | Rowan Cheung | GLOBAL | Twitter/X/NL | 8 | T2 | HIGH | Rundown AI (2M+ subs); top AI newsletter |
| 20 | Yannic Kilcher | GLOBAL | YouTube | 8 | T2 | HIGH | ML paper deep dives; can explain 8F pipeline |
| 21 | Data Chaz | GLOBAL | Twitter/X | 8 | T2 | HIGH | LLMs + Streamlit; dev advocacy |
| 22 | Zain Kahn | GLOBAL | NL/LI/X | 9 | T2 | HIGH | Superhuman AI (1M+ subs); cross-platform |
| 23 | Nate Herk | GLOBAL | YouTube | 8 | T2 | HIGH | AI automation; n8n workflow; audience overlap |
| 24 | Sebastian Raschka | GLOBAL | NL/X | 8 | T2 | HIGH | Ahead of AI; LLM research authority |
| 25 | Matt Wolfe | GLOBAL | YouTube/NL | 8 | T2 | HIGH | futuretools.io; AI tools coverage |
| 26 | Matthew Berman | GLOBAL | YouTube | 8 | T2 | HIGH | LLM/OSS AI coverage |
| 27 | AI Explained | GLOBAL | YouTube | 8 | T2 | HIGH | Signal-over-noise AI; reasoning systems |
| 28 | David Shapiro | GLOBAL | YouTube | 8 | T2 | HIGH | AGI deep dives; autonomous AI |
| 29 | Jeremy Howard | GLOBAL | YT/Blog/Conf | 8 | T2 | HIGH | fast.ai; OSS deep learning |
| 30 | Erick Wendel | BR | YouTube/X | 8 | T2 | HIGH | Advanced JS/Node; conference speaker |
| 31 | Eduardo Mendes | BR | YouTube/X | 8 | T2 | HIGH | Python/FastAPI/OSS; Live de Python |
| 32 | Programacao Dinamica | BR | YouTube/IG | 8 | T2 | HIGH | Academic CS; Python |
| 33 | Prof. Sandeco | BR | YouTube | 8 | T3 | HIGH | University prof; AI + LLMs |
| 34 | IA Todo Dia | BR | Pod/NL/YT | 8 | T3 | HIGH | Largest AI podcast BR |
| 35 | Danilo Gato Pod | BR | Podcast | 8 | T3 | HIGH | #1 tech on Spotify BR |
| 36 | Allan Sene (Data Hackers) | BR | Community/Slack | 8 | T3 | HIGH | 45K+ data/AI community |
| 37 | Theo Browne | GLOBAL | Twitter/X/YT | 8 | T2 | HIGH | T3 stack; full-stack AI |
| 38 | Peter Steinberger | GLOBAL | Twitter/X/GH | 8 | T3 | HIGH | OpenClaw; now at OpenAI |
| 39 | Alessio Fanelli | GLOBAL | Twitter/X/Pod | 8 | T3 | HIGH | Latent Space co-host |
| 40 | Nathan Labenz | GLOBAL | Twitter/X/Pod/NL | 8 | T3 | HIGH | Cognitive Revolution |
| 41 | DSPy (Stanford NLP) | GLOBAL | GitHub | 8 | T3 | HIGH | Prompt optimization; typed approach |
| 42 | OpenHands (All Hands AI) | GLOBAL | GitHub | 8 | T3 | HIGH | OSS autonomous engineer |
| 43 | Langfuse | GLOBAL | GitHub | 8 | T3 | HIGH | LLM observability |
| 44 | n8n | GLOBAL | GitHub/Discord | 8 | T3 | HIGH | Workflow automation |
| 45 | Chip Huyen | GLOBAL | Blog/Conf | 8 | T3 | HIGH | ML systems author |
| 46 | Jason Wei | GLOBAL | Conference | 8 | T3 | HIGH | CoT pioneer; 8F narrative |
| 47 | Bubows (Bruno Belissimo) | BR | Instagram | 7 | T2 | HIGH | Simple AI demos; visual |
| 48 | Andre Lug | BR | IG/X | 7 | T3 | HIGH | AI productivity tools |
| 49 | AI Tinkerers SP | BR | Meetup | 8 | T4 | HIGH | Builder-focused; live demo venue |
| 50 | r/ClaudeAI mods | GLOBAL | Reddit | 8 | T4 | HIGH | Claude ecosystem; CEX runs on Claude |

### Outreach Wave Plan (derived from Top 50)

| Wave | Timeline | Targets | Action | Expected Impact |
|------|----------|---------|--------|----------------|
| Wave 1 (Week 1) | Day 1-7 | GitHub maintainers (#2,3,4,10,12,13,41-44) | Star/fork their repos, open issue mentioning CEX, DM with demo link | 10-50 stars from maintainer network effect |
| Wave 2 (Week 1-2) | Day 3-14 | Twitter/X HIGH (#5,6,17,18,21,37-40) | Follow, engage threads, DM with 30-second demo GIF | Viral thread potential (100K+ impressions) |
| Wave 3 (Week 2) | Day 7-14 | Newsletter authors (#5,7,19,22,24) | Pitch email for feature/mention in next issue | 100K-2M newsletter subscriber exposure |
| Wave 4 (Week 2-3) | Day 10-21 | Podcast hosts (#5,34,35,39,40) | Guest pitch with "AI Brain" narrative hook | Long-form authority building |
| Wave 5 (Week 3) | Day 14-21 | YouTube creators (#14,15,20,25-28) | Send demo reel, offer collab video | 500K-4M potential video views |
| Wave 6 (Week 3-4) | Day 14-28 | BR community (#1,7,8,9,11,30-36,47-49) | Portuguese outreach, community posts, meetup demo | BR developer market penetration |
| Wave 7 (Month 2) | Day 28+ | Discord/Reddit (#50, Discord admins, Reddit mods) | Community announcements, bot-posts, engagement | Sustained grassroots growth |
| Wave 8 (Month 2+) | Day 30+ | Remaining T2/T3 MEDIUM relevance | Broader outreach campaign | Long-tail awareness |

---

## Data Quality Notes

1. Follower counts are approximate as of April 2026; refresh quarterly
2. Cross-platform contacts (e.g., Danilo Gato in 7 categories) are listed in their primary category with cross-references; 24 true duplicates were merged during dedup pass (2026-04-25)
3. GitHub star counts are approximate ranges
4. Reddit/Discord listed as team entries (5-15 moderators per team)
5. Contact methods prioritize public/professional channels -- no private emails or phone numbers
6. Priority scores are CEX-specific: optimized for typed-systems, multi-agent, OSS AI framework seeding
7. Relevance scoring informed by cm_cex_vs_landscape.md: contacts covering typed systems, multi-agent orchestration, or open-source AI infrastructure scored HIGH
8. BR contacts often appear on multiple platforms; the CRM entry uses the platform with highest follower count as primary
9. Outreach_status initialized to `not_started` for all 714 entries
10. This CRM should be updated monthly as follower counts and platform activity shift rapidly

---

## Source Artifacts

| Source | Contacts | Region |
|--------|----------|--------|
| kc_influencer_directory_global.md | 385 | GLOBAL |
| kc_influencer_directory_br.md | 353 | BR |
| cm_cex_vs_landscape.md | -- | Relevance scoring criteria |
| kc_cex_positioning_analysis.md | -- | Priority scoring alignment |
| **TOTAL MERGED** | **714** | **GLOBAL + BR** (24 cross-platform dupes removed) |
