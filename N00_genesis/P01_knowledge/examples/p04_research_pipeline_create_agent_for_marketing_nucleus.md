---
id: p04_rp_marketing_nucleus
kind: cli_tool
pillar: P04
title: "Research Pipeline: Marketing Intelligence (N02)"
version: "1.0.0"
created: "2026-04-02"
author: "research-pipeline-builder"
domain: research_pipeline
quality: 9.2
tags: [research-pipeline, STORM, CRAG, CRITIC, marketing, N02, content-intelligence]
tldr: "7-stage market intelligence pipeline feeding N02 — collects social signals, competitor messaging, and trend data for copy, campaigns, and content briefs."
density_score: 1.0
related:
  - p02_agent_research_pipeline_intelligence
  - bld_instruction_research_pipeline
  - tpl_research_pipeline
  - n01_tool_research_pipeline
  - bld_knowledge_card_research_pipeline
  - p03_sp_research_pipeline_builder
  - bld_architecture_research_pipeline
  - research-pipeline-builder
  - p04_rp_weekly_market_intelligence_brief_output_template
  - p08_ac_n02
---
# Research Pipeline: Marketing Intelligence (N02)

## Pipeline (7 Stages)

| Stage | Name | Model | Input | Output |
|-------|------|-------|-------|--------|
| S1 | INTENT | regex + embed | Marketing query | domain, verb, content_type, audience |
| S2 | PLAN (STORM) | reasoning | Intent + perspectives | 25–35 sub-questions across 5 angles |
| S3 | RETRIEVE (CRAG) | APIs + scraping | Sub-questions | Scored results (≥0.6 social, ≥0.7 web) |
| S4 | RESOLVE | deterministic | Raw results | Deduplicated entities, merged competitor data |
| S5 | SCORE | fast model | Entities | Engagement score + content relevance (7-dim) |
| S6 | SYNTHESIZE (GoT) | domain models | Scored data | Content briefs, positioning map, copy hooks |
| S7 | VERIFY (CRITIC) | thinking model | Synthesis + sources | Verified intelligence brief (max 3 iter) |

### Stage Detail

**S1 INTENT** — Classify incoming marketing query:
- domain: `competitor_analysis | trend_research | audience_insight | content_gap | campaign_brief`
- verb: `analyze | discover | map | generate | audit`
- content_type: `social_post | ad_copy | landing_page | email | blog | video_script`
- Routes `competitor_analysis` → heavier inbound+outbound; `trend_research` → heavier trends+social

**S2 PLAN (STORM)** — 5 marketing perspectives, 5–7 sub-questions each:
- `buyer`: What motivates purchase? What language do buyers use in reviews/social?
- `competitor`: How are rivals positioning? What gaps exist in their messaging?
- `trend_analyst`: What formats/topics are gaining velocity? Seasonal patterns?
- `content_creator`: Which post formats drive highest engagement per platform?
- `brand_strategist`: Where does brand voice diverge from audience language?

**S3 RETRIEVE (CRAG)** — Parallel fetch, quality gate per source category:
- Social (outbound) min score: 0.5 — volume data, directional only
- Web (search) min score: 0.7 — competitor copy, landing pages
- Trends min score: 0.4 — directional signal, not precise
- RAG (internal) min score: 0.8 — past campaigns, brand docs

**S4 RESOLVE** — Dedup by: URL canonical + title similarity (≥0.85 cosine) + brand entity

**S5 SCORE** — 7-dimension content relevance scoring:
1. Audience alignment (matches target persona)
2. Topic velocity (trending + timeframe)
3. Competitor presence (saturation risk)
4. Engagement signal (likes, shares, comments normalized)
5. Brand safety (no toxic associations)
6. Recency (penalize >90d for social, >180d for web)
7. Copy hook density (action verbs, emotion triggers, specificity)

**S6 SYNTHESIZE (GoT)** — Multi-model merge:
- Fast model: extract themes, keywords, CTAs from source corpus
- Reasoning model: build positioning map, identify content gaps, draft 3 copy angles
- Domain merge: Graph-of-Thoughts connects buyer pain → competitor gap → brand opportunity

**S7 VERIFY (CRITIC)** — Thinking model checks:
- All claims traceable to retrieved sources
- No invented statistics or engagement numbers
- Copy hooks match brand_config.yaml voice and tone
- Competitor claims verifiable (URLs cited)
- Max 3 correction iterations; flag unresolved gaps

---

## Sources

```yaml
sources:
  inbound:                        # competitor content, product pages
    - competitor_websites         # via firecrawl (scrape landing pages, about, pricing)
    - g2                          # SaaS reviews with verbatim buyer language
    - capterra                    # alternative review source
    - producthunt                 # launch copy, upvote patterns
  outbound:                       # social signals, community voice
    - twitter_x                   # real-time trend + hashtag velocity
    - instagram                   # visual format performance
    - linkedin                    # B2B positioning + thought leadership
    - reddit                      # unfiltered buyer language (r/niche subs)
    - youtube                     # video format + title/thumbnail patterns
    - tiktok                      # short-form trend signals
  search:                         # web copy, SEO, SERP analysis
    - serper                      # SERP + ad copy (auth: SERPER_API_KEY)
    - exa                         # semantic web search (auth: EXA_API_KEY)
    - gemini_search               # broad coverage fallback
  trends:                         # velocity and seasonality
    - pytrends                    # Google Trends (unofficial, free, throttled)
    - semrush                     # keyword volume + competitor traffic (auth: SEMRUSH_API_KEY)
  rag:                            # internal brand context
    - brand_config                # voice, tone, persona from brand_config.yaml
    - past_campaigns              # local_docs of previous campaign performance
    - audience_segments           # ICP definitions from N06 commercial
```

---

## Config Reference

```yaml
# Research Pipeline Config — Marketing Nucleus (N02)
# Env vars: SERPER_API_KEY, EXA_API_KEY, FIRECRAWL_API_KEY, SEMRUSH_API_KEY (optional)

identity:
  empresa: "{{BRAND_NAME}}"          # from brand_config.yaml
  nicho: "{{BRAND_NICHE}}"
  idioma: "{{BRAND_LANGUAGE}}"       # pt-BR | en | es
  pais: "{{BRAND_COUNTRY}}"

sources:
  inbound: [competitor_websites, g2, producthunt]
  outbound: [twitter_x, instagram, reddit, youtube]
  search: [serper, exa, gemini_search]
  trends: [pytrends, semrush]
  rag: [brand_config, past_campaigns]

storm_perspectives:
  - {role: buyer,            focus: "pain-points triggers language reviews objections"}
  - {role: competitor,       focus: "messaging positioning gaps weaknesses CTAs"}
  - {role: trend_analyst,    focus: "velocity seasonality platform-algorithm format-shift"}
  - {role: content_creator,  focus: "hook structure format engagement-pattern virality"}
  - {role: brand_strategist, focus: "voice-gaps audience-language differentiation proof-points"}

multi_model:
  extraction: "gemini-2.5-flash"     # bulk social + SERP extraction
  reasoning:  "claude-sonnet"        # positioning map + copy angle generation
  social:     "gemini-2.5-flash"     # high-volume social feed analysis
  critic:     "o4-mini"              # fact-check + brand-voice verification

budget:
  firecrawl_monthly: 1000            # competitor scraping (lower than e-comm)
  firecrawl_per_research: 5
  serper_daily: 50
  semrush_monthly: 500               # keyword queries

output:
  formats: [json, md]                # JSON → N02 content brief | MD → human review
  idioma: "{{BRAND_LANGUAGE}}"
  template: brief                    # brief | consulting | raw

quality:
  crag_min_score: 0.6               # lower than e-comm; social data is noisier
  critic_max_iterations: 3
  final_min_score: 8.0
```

---

## Quality Gates

### Hard Gates (fail = reject)
| # | Gate | Check |
|---|------|-------|
| H1 | 7-stage complete | All stages S1–S7 documented |
| H2 | Source diversity | outbound + search minimum (social signal required) |
| H3 | STORM perspectives | 5 perspectives, all marketing-domain roles |
| H4 | CRAG threshold | `crag_min_score` defined (0.0–1.0) |
| H5 | CRITIC defined | `critic_max_iterations` set; critic is thinking model |
| H6 | Zero secrets | All API keys as ENV_VAR only |
| H7 | Budget cap | At least `serper_daily` or `firecrawl_monthly` defined |
| H8 | Multi-model routing | extraction + reasoning + critic all specified |

### Soft Gates (warn, don't reject)
| # | Gate | Weight |
|---|------|--------|
| S1 | Brand voice check in CRITIC | 0.9 — enforces brand_config.yaml tone |
| S2 | RAG includes past campaigns | 0.8 — prevents repeating failed angles |
| S3 | Competitor landing pages scraped | 0.7 — inbound required for positioning map |
| S4 | Social outbound ≥ 2 platforms | 0.8 — single platform = sampling bias |
| S5 | Semrush or pytrends in trends | 0.6 — velocity signal improves timing |
| S6 | Output includes JSON copy brief | 0.7 — N02 agents consume JSON, not MD |

---

## Handoff to N02

This pipeline outputs a structured **content brief** (JSON) consumed by N02 marketing agents:

```json
{
  "research_query": "...",
  "top_hooks": ["...", "...", "..."],
  "competitor_gaps": ["...", "..."],
  "buyer_language": ["...", "..."],
  "trending_formats": ["...", "..."],
  "content_angles": [
    {"angle": "pain-point", "evidence": "...", "copy_starter": "..."},
    {"angle": "competitor-gap", "evidence": "...", "copy_starter": "..."},
    {"angle": "trend-ride", "evidence": "...", "copy_starter": "..."}
  ],
  "brand_voice_flags": [],
  "critic_corrections": [],
  "sources_cited": 14,
  "final_score": 8.7
}
```

Signal on complete: `write_signal('n01', 'complete', 8.7)` → N02 reads handoff.
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_research_pipeline_intelligence]] | upstream | 0.36 |
| [[bld_instruction_research_pipeline]] | upstream | 0.32 |
| [[tpl_research_pipeline]] | sibling | 0.31 |
| [[n01_tool_research_pipeline]] | sibling | 0.31 |
| [[bld_knowledge_card_research_pipeline]] | upstream | 0.30 |
| [[p03_sp_research_pipeline_builder]] | upstream | 0.28 |
| [[bld_architecture_research_pipeline]] | downstream | 0.27 |
| [[research-pipeline-builder]] | related | 0.26 |
| [[p04_rp_weekly_market_intelligence_brief_output_template]] | related | 0.25 |
| [[p08_ac_n02]] | downstream | 0.25 |
