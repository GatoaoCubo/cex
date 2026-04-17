---
id: user_journey_n02
kind: user_journey
pillar: P05
nucleus: n02
title: "Funnel-Stage Content Mapping -- User Journey"
version: 1.0.0
quality: 9.0
tags: [user_journey, funnel_mapping, content_strategy, TOFU_MOFU_BOFU, P05, n02_marketing]
domain: content-strategy
status: active
density_score: 1.0
---

# User Journey -- Funnel-Stage Content Mapping

## Purpose

Every piece of content exists at a specific moment in the user's journey.
Wrong content at wrong moment = wasted budget, confused audience, and
a brand that feels like it doesn't listen. This map ensures N02 produces
content that meets the audience WHERE THEY ARE, not where we want them to be.

## The Funnel Model

```
AWARENESS (TOFU) -- Top of Funnel
Problem-aware, not solution-aware. Seeking understanding.
    |
    v
CONSIDERATION (MOFU) -- Middle of Funnel
Solution-aware, evaluating options. Seeking proof.
    |
    v
DECISION (BOFU) -- Bottom of Funnel
Vendor-aware, ready to commit. Seeking confidence.
    |
    v
RETENTION
Customer. Seeking value realization. Risk: churn.
    |
    v
ADVOCACY
Delighted customer. Potential amplifier. Seeking recognition.
```

## Stage-by-Stage Content Map

### TOFU -- Awareness

| Element | Specification |
|---------|--------------|
| **Goal** | Generate awareness; build brand familiarity |
| **Audience State** | Experiencing a pain; not yet seeking solutions |
| **Primary Metric** | Impressions, reach, engagement rate, saves |
| **Hook Type** | pain, curiosity (never authority -- not earned yet) |
| **CTA Type** | Soft -- "See how", "Learn more", "Discover" |
| **Urgency** | None or very light |
| **Formats** | Reels, carousels, short posts, educational threads |
| **Length** | Short-form (15-60s video; 100-300 word post) |
| **Tone** | Conversational, empathetic; meet them where they are |

**TOFU Content Types:**
- Pain-point education posts ("Why X doesn't work")
- Industry insight ("The stat nobody talks about")
- Aspirational storytelling ("How [person] went from X to Y")
- How-to content (surface-level, not complete solution)
- Trending topic commentary (brand perspective)

---

### MOFU -- Consideration

| Element | Specification |
|---------|--------------|
| **Goal** | Build trust; differentiate from alternatives |
| **Audience State** | Aware of solutions; evaluating you vs. others |
| **Primary Metric** | Link clicks, profile visits, email sign-ups, downloads |
| **Hook Type** | social_proof, data, authority |
| **CTA Type** | Resource -- "Get the guide", "Watch the demo", "Read the case study" |
| **Urgency** | Moderate -- deadline for resource, limited cohort size |
| **Formats** | Carousels, long posts, email sequences, webinars, case studies |
| **Length** | Medium-form (300-800 words; 2-4 min video) |
| **Tone** | Professional + proof-heavy; let results speak |

**MOFU Content Types:**
- Customer case studies (specific results, named if possible)
- Comparison content ("[Category] done right vs. done wrong")
- Data-backed insights ("We analyzed X campaigns -- here's what worked")
- Behind-the-scenes process content
- Expert interviews / authority amplification
- Free tools, templates, calculators (gated for lead capture)

---

### BOFU -- Decision

| Element | Specification |
|---------|--------------|
| **Goal** | Convert -- trial, demo, purchase, sign-up |
| **Audience State** | Ready to decide; needs final confidence to act |
| **Primary Metric** | Conversion rate, cost_per_acquisition, demo book rate |
| **Hook Type** | Urgency + social_proof + authority |
| **CTA Type** | Direct -- "Start free trial", "Book your demo", "Claim offer" |
| **Urgency** | High -- scarcity, deadline, bonus |
| **Formats** | Direct-response ads, retargeting, email drip, landing page |
| **Length** | Short and punchy (ad: 125 words; landing page: complete value prop) |
| **Tone** | Bold, confident, urgency-forward |

**BOFU Content Types:**
- Limited-time offers (deadline copy)
- Risk-reversal content ("Try free for 14 days, cancel anytime")
- Final objection handling ("Still not sure? Here's what [customer] said")
- Retargeting copy ("You were this close...")
- Side-by-side feature comparison
- ROI calculator copy ("See your estimated savings")

---

### RETENTION

| Element | Specification |
|---------|--------------|
| **Goal** | Reduce churn; increase LTV |
| **Audience State** | Paying customer; evaluating ongoing value |
| **Primary Metric** | Renewal rate, NPS score, feature adoption, support tickets |
| **Hook Type** | Value demonstration + milestone recognition |
| **CTA Type** | Engagement -- "Unlock feature", "Access your [report]", "Upgrade" |
| **Formats** | In-app, email, community, exclusive content |
| **Tone** | Warm, personal, progress-acknowledging |

---

### ADVOCACY

| Element | Specification |
|---------|--------------|
| **Goal** | Convert happy customers into amplifiers |
| **Audience State** | Delighted; NPS 9-10 promoter |
| **Primary Metric** | Referral rate, testimonial capture, user-generated content |
| **Hook Type** | Recognition + belonging |
| **CTA Type** | Community -- "Share your story", "Refer a friend", "Join our community" |
| **Formats** | Email, community, social mention, referral program |
| **Tone** | Celebratory, inclusive, grateful |

## Content Calendar Logic

```yaml
content_calendar_rule:
  tofu_mofu_bofu_ratio:
    default: "60:30:10"     # most brands need more awareness
    product_launch: "40:40:20"
    growth_phase: "50:35:15"
    mature_product: "30:40:30"

  posting_cadence:
    instagram: 4-5x per week
    linkedin: 3-4x per week
    x: 5-7x per week
    email: 1-2x per week

  stage_rotation:
    rule: "No more than 2 consecutive BOFU posts on any platform"
    reason: audience fatigue + algorithmic suppression of sales-heavy content
```

## Journey Analytics

Track journey progression per cohort (maps to `cohort_analysis_n02.md`):

```yaml
journey_metric:
  cohort_id: string
  entry_stage: TOFU|MOFU|BOFU|RETENTION|ADVOCACY
  current_stage: string
  stages_touched: array[string]
  days_in_journey: integer
  conversion_event: string (nullable)
  churn_event: string (nullable)
  journey_velocity: float  # stages per week
```

## Integration

- Consumed by: `workflow_campaign_pipeline.md` (F2 STRATEGIZE)
- Consumed by: `action_prompt_n02_copy.md` (funnel_stage injection)
- Cross-references: `customer_segment_n02.md` (segment + journey stage combo)
- Measured by: `cohort_analysis_n02.md` (journey progression tracking)
