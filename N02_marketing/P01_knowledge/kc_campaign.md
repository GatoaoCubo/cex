---
id: n02_kc_campaign
kind: knowledge_card
pillar: P01
title: "Campaign Architecture — From Brief to Conversion"
domain: N02_marketing / Campaigns
tags: [campaign, marketing, funnel, strategy, multichannel, conversion, launch, N02]
quality: 9.1
source: internal_distillation
created: 2026-04-07
author: n02_marketing
tldr: "Complete campaign mental model — brief structure, channel orchestration, funnel mapping, creative frameworks, budget allocation, and post-campaign analysis. Every campaign is a persuasion system, not a collection of ads."
density_score: 0.95
---

# KC: Campaign Architecture

## Core Mental Model

A campaign is a **coordinated persuasion system** across multiple touchpoints. It's not "make some ads." It's architect a journey where every piece — ad, email, landing page, social post, retarget — plays a specific role in moving one person from *unaware* to *converted*.

```
BRIEF → AUDIENCE → FUNNEL → CHANNELS → CREATIVE → LAUNCH → OPTIMIZE → ANALYZE
  ↑                                                                        │
  └────────────────── learning feeds next campaign ─────────────────────────┘
```

The campaign that works is the one where every asset knows *what came before it* and *what comes after it*.

---

## Campaign Brief — The 10 Decisions

Every campaign starts with 10 answered questions. Skip one, and the whole system leaks.

```yaml
campaign_brief:
  1_objective:        # What exactly must happen? (leads, sales, signups, awareness)
  2_audience:         # Who specifically? (demographics + psychographics + behavior)
  3_offer:            # What's the value exchange? (what they get vs what they give)
  4_positioning:      # Why you vs alternatives? (1 sentence maximum)
  5_channels:         # Where will they see this? (ordered by priority)
  6_budget:           # Total budget + per-channel allocation
  7_timeline:         # Start date, end date, key milestones
  8_success_metrics:  # What numbers = success? (be specific)
  9_constraints:      # Legal, brand, technical, platform limits
  10_assets_needed:   # Exact list of creative deliverables
```

**Rule**: The brief is a CONTRACT between strategy (what) and execution (how). If the brief changes mid-campaign, the campaign restarts from that decision forward.

---

## The 6 Campaign Archetypes

### 1. Launch Campaign
**Goal**: Introduce new product/feature to market
**Duration**: 2-4 weeks
**Structure**:
```
Week -1: Teaser (curiosity, waitlist)
Week 0:  Launch (full pitch, early-bird offer)
Week 1:  Social proof (testimonials, case studies)
Week 2:  Last chance (scarcity, deadline)
```
**Key channels**: Email (primary), social (amplification), paid ads (reach)
**Critical metric**: Revenue in first 72 hours (predicts total launch performance)

### 2. Lead Generation Campaign
**Goal**: Capture qualified leads for nurture/sales
**Duration**: Ongoing (4-week test cycles)
**Structure**:
```
Ad → Landing page → Lead magnet → Thank you page → Nurture sequence
  ↳ Retarget non-converters after 3 days
```
**Key channels**: Paid ads (Facebook/Google), landing pages, email automation
**Critical metric**: Cost per lead (CPL) and lead-to-customer conversion rate

### 3. Brand Awareness Campaign
**Goal**: Increase recognition in target market
**Duration**: 8-12 weeks minimum
**Structure**:
```
Phase 1 (Wk 1-4): High-frequency exposure (video, display)
Phase 2 (Wk 5-8): Engagement content (stories, polls, UGC)
Phase 3 (Wk 9-12): Retarget engaged users with conversion offer
```
**Key channels**: Video (YouTube, TikTok), social organic, display
**Critical metric**: Brand recall lift + aided awareness surveys

### 4. Re-engagement Campaign
**Goal**: Reactivate dormant users/customers
**Duration**: 2-3 weeks
**Structure**:
```
Day 0: "We miss you" (emotional hook)
Day 3: "Best of" content (remind them of value)
Day 7: Win-back offer (exclusive discount/bonus)
Day 14: Goodbye (loss aversion trigger)
```
**Key channels**: Email, push notifications, retargeting ads
**Critical metric**: Reactivation rate (% of dormant users who take action)

### 5. Seasonal/Event Campaign
**Goal**: Capitalize on time-bound opportunity
**Duration**: 1-2 weeks (concentrated)
**Structure**:
```
Pre-event: Countdown + anticipation
Event day: Full push (all channels)
Post-event: Extended offer for latecomers (24-48h)
```
**Key channels**: All channels simultaneously (synchronized)
**Critical metric**: Revenue per impression (efficiency under time pressure)

### 6. Content Campaign
**Goal**: Build authority and organic reach
**Duration**: 12+ weeks (long game)
**Structure**:
```
Weekly: Publish pillar content (blog/video)
Daily: Distribute micro-content across social
Monthly: Compile insights into lead magnet
Quarterly: Promote lead magnet via paid (amplify best performers)
```
**Key channels**: Blog/SEO, social organic, email newsletter
**Critical metric**: Organic traffic growth rate + email list growth rate

---

## Funnel Architecture

```
┌─────────────────────────────────────────────────────┐
│  TOFU — Top of Funnel (Awareness)                   │
│  Goal: Stop the scroll. Make them notice.           │
│  Assets: Social ads, video, blog posts, PR          │
│  Formula: AIDA hook + curiosity gap                 │
│  Metric: Impressions, reach, video views            │
├─────────────────────────────────────────────────────┤
│  MOFU — Middle of Funnel (Consideration)            │
│  Goal: Build preference. Earn trust.                │
│  Assets: Landing pages, case studies, webinars      │
│  Formula: PAS/BAB + social proof                    │
│  Metric: Leads captured, engagement rate, time on page│
├─────────────────────────────────────────────────────┤
│  BOFU — Bottom of Funnel (Decision)                 │
│  Goal: Remove last objection. Close.                │
│  Assets: Sales page, demo, offer email, retarget ad │
│  Formula: Offer + urgency + guarantee               │
│  Metric: Conversion rate, revenue, ROAS             │
├─────────────────────────────────────────────────────┤
│  POST — Post-Funnel (Advocacy)                      │
│  Goal: Turn buyer into promoter.                    │
│  Assets: Onboarding, review request, referral prog  │
│  Formula: Delight + reciprocity                     │
│  Metric: NPS, referral rate, repeat purchase rate   │
└─────────────────────────────────────────────────────┘
```

---

## Channel Orchestration Matrix

| Channel | Best For | TOFU | MOFU | BOFU | Cost |
|---------|----------|------|------|------|------|
| Facebook/Meta Ads | Lead gen, awareness | ★★★ | ★★ | ★ | $$ |
| Google Search Ads | Intent capture | ★ | ★★ | ★★★ | $$$ |
| Instagram Organic | Brand personality | ★★★ | ★★ | ★ | Free |
| Email Sequences | Nurture, convert | ★ | ★★★ | ★★★ | $ |
| YouTube Video | Authority, education | ★★★ | ★★★ | ★ | $$ |
| TikTok | Virality, awareness | ★★★ | ★ | — | $ |
| LinkedIn | B2B, thought leadership | ★★ | ★★★ | ★★ | $$$ |
| SEO/Blog | Long-term organic | ★★★ | ★★★ | ★ | Time |
| Retargeting | Re-engage warm leads | — | ★★ | ★★★ | $$ |
| SMS/Push | Urgency, flash sales | — | ★ | ★★★ | $ |

### Channel Sync Rules
1. **TOFU channels** drive traffic → **MOFU assets** capture leads → **BOFU sequences** convert
2. Never run BOFU without TOFU warming first (cold conversion = expensive)
3. Retargeting connects the gaps — every non-converter gets a second chance
4. Email is the backbone — it's the only channel you OWN (algorithm-proof)

---

## Creative Framework

### The 3x3 Creative Matrix
For every campaign, produce:

| Variant | Hook Style | Visual Style | CTA Style |
|---------|-----------|-------------|-----------|
| V1 | Pain-based | Problem image | Direct ("Get X now") |
| V2 | Benefit-based | Solution image | Soft ("See how it works") |
| V3 | Curiosity-based | Abstract/metaphor | Social proof ("Join 4K+ users") |

**Why 3x3**: You need 9 creative variants minimum to find the winner. The ad you think will win rarely does. Let data decide.

### Copy Frameworks Per Funnel Stage

| Stage | Primary Formula | Secondary | Tone |
|-------|----------------|-----------|------|
| TOFU | AIDA | 4U headlines | Bold, curiosity-driven |
| MOFU | PAS | BAB (for case studies) | Educational, credible |
| BOFU | Offer stack | FAB (for features) | Confident, urgent |
| POST | Thank you + next step | — | Warm, personal |

---

## Budget Allocation Models

### The 70/20/10 Rule (proven allocation)
```
70% — Proven channels (what's already working)
20% — Scaling channels (promising, need more data)
10% — Experimental channels (new, unproven, high-potential)
```

### Funnel-Based Allocation
```yaml
awareness_campaign:
  tofu: 60%
  mofu: 25%
  bofu: 15%

lead_gen_campaign:
  tofu: 40%
  mofu: 35%
  bofu: 25%

launch_campaign:
  tofu: 30%
  mofu: 30%
  bofu: 40%  # heavier bottom = more conversion focus
```

### Daily Budget Pacing
```
Day 1-3:   Learning phase — do NOT touch (let algorithms optimize)
Day 4-7:   Kill underperformers (bottom 30% by CPA)
Day 8-14:  Scale winners (increase budget 20-30% per day max)
Day 15+:   Creative refresh (fatigue sets in around day 10-14)
```

---

## Campaign Timeline Template

```
T-14d: Brief finalized + audience research complete
T-10d: Creative concepts approved (3x3 matrix)
T-7d:  All assets produced (ads, LPs, emails, sequences)
T-3d:  Technical setup (tracking, pixels, UTMs, automation)
T-1d:  Final QA (all links, all tracking, all sequences tested)
T-0:   LAUNCH (monitor hourly for first 24h)
T+3d:  First optimization pass (kill losers, scale winners)
T+7d:  Mid-campaign review (metrics vs brief targets)
T+14d: Campaign close (or scale decision)
T+17d: Post-mortem report (what worked, what didn't, what next)
```

---

## Tracking & Attribution

### UTM Convention
```
utm_source:   {platform} (facebook, google, email, linkedin)
utm_medium:   {type} (cpc, organic, email, social)
utm_campaign: {campaign_id} (launch_2026q2, leadgen_webinar)
utm_content:  {creative_variant} (v1_pain, v2_benefit, v3_curiosity)
utm_term:     {audience_segment} (cold, warm, retarget)
```

### Attribution Models
| Model | Best For | Caveat |
|-------|----------|--------|
| Last-click | Short funnels (<7d) | Ignores TOFU contribution |
| First-click | Brand awareness | Ignores conversion optimization |
| Linear | Multi-touch B2B | Equal weight = misleading for long funnels |
| Time-decay | Launch campaigns | Good balance, favors recent touches |
| Data-driven | 1000+ conversions/mo | Requires volume; best but needs data |

---

## Post-Campaign Analysis

### The 5-Question Debrief
```
1. Did we hit the objective? (yes/no + by how much)
2. What was our best-performing creative/channel? (data)
3. What was our worst-performing creative/channel? (why)
4. What did we learn about the audience? (new insight)
5. What would we do differently next time? (specific action)
```

### Campaign Scorecard
```yaml
metrics:
  reach: {actual} vs {target}
  leads: {actual} vs {target}
  conversion_rate: {actual} vs {target}
  cpl: {actual} vs {target}
  roas: {actual} vs {target}
  
qualitative:
  brand_consistency: {1-10}
  creative_quality: {1-10}
  audience_response: {sentiment_summary}
  
next_actions:
  - {action_1}
  - {action_2}
  - {action_3}
```

---

## Integration With N02 Artifacts

| Artifact | How This KC Feeds It |
|----------|---------------------|
| `email_sequence_template.md` | Sequences implement arcs mapped to campaign funnel stages |
| `ad_copy_template.md` | Ad variants follow 3x3 creative matrix from this KC |
| `landing_page_template.md` | LP structure mirrors funnel stage (TOFU/MOFU/BOFU) |
| `campaign_performance_memory.md` | Post-campaign scorecard data feeds memory |
| `ab_testing_framework.md` | Creative matrix drives test priorities |
| `scoring_rubric_marketing.md` | Campaign quality gates derived from this KC |
| `cross_nucleus_handoffs.md` | Channel orchestration defines N02↔N01/N05/N06 interfaces |
| `workflow_marketing.md` | Campaign timeline maps to workflow execution phases |
