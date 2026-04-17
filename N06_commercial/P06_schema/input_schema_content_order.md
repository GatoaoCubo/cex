---
id: n06_input_schema_content_order
kind: input_schema
pillar: P06
title: "Input Schema -- Content Factory Order"
version: 1.0.0
created: 2026-04-08
author: n06_commercial
nucleus: N06
domain: content-factory-ordering
quality: 8.9
tags: [input-schema, content-factory, order, brief, customer, checkout]
tldr: "Complete input schema for Content Factory orders. Defines every field a customer submits to produce content: topic, audience, formats, brand config, delivery preferences, billing. Validates before pipeline execution."
density_score: 0.93
depends_on:
  - spec_content_factory_v1
  - n06_content_factory_pricing
linked_artifacts:
  primary: n06_content_factory_pricing
  related:
    - spec_content_factory_v1
    - n06_kc_content_monetization
    - p12_dag_cf_master
---

# Input Schema -- Content Factory Order

> What a customer submits to order content. Every field has a purpose.
> Incomplete orders get rejected at validation, not halfway through the pipeline.

---

## 1. Schema Definition (YAML)

```yaml
content_order:
  # === REQUIRED FIELDS ===
  
  topic:
    type: string
    required: true
    min_length: 10
    max_length: 500
    description: "What the content is about. Be specific."
    examples:
      - "How to use the 8F pipeline in CEX to build typed knowledge artifacts"
      - "React Server Components vs Client Components for mid-level devs"
      - "Pricing strategies for SaaS in the Brazilian market"
    validation: "Must be a declarative topic, not a command. Reject: 'make me content'"

  audience:
    type: object
    required: true
    description: "Who consumes this content. Determines tone, depth, vocabulary."
    properties:
      segment:
        type: string
        required: true
        enum: [developer, marketer, executive, student, general, custom]
        description: "Primary audience segment"
      skill_level:
        type: string
        required: true
        enum: [beginner, intermediate, advanced, expert]
        description: "Technical depth calibration"
      custom_description:
        type: string
        required: false
        max_length: 300
        description: "Free-text audience description when segment=custom"
    examples:
      - { segment: developer, skill_level: intermediate }
      - { segment: custom, skill_level: beginner, custom_description: "Brazilian solopreneurs launching their first digital product" }

  formats:
    type: array
    required: true
    min_items: 1
    max_items: 11
    items:
      type: string
      enum:
        - blog_post
        - social_media_set
        - video_script
        - video_produced_short   # 90s
        - video_produced_long    # 5min
        - podcast_episode
        - course_module
        - ebook_chapter
        - presentation
        - email_sequence
        - landing_page
    description: "Which output formats to produce. Order does not matter."
    presets:
      lite: [blog_post, social_media_set, email_sequence]
      standard: [blog_post, social_media_set, email_sequence, video_produced_short, podcast_episode, presentation]
      complete: [blog_post, social_media_set, email_sequence, video_produced_short, podcast_episode, presentation, course_module, ebook_chapter, landing_page]
      full_factory: [blog_post, social_media_set, video_script, video_produced_short, video_produced_long, podcast_episode, course_module, ebook_chapter, presentation, email_sequence, landing_page]

  # === OPTIONAL FIELDS (with smart defaults) ===

  brand_config:
    type: string
    required: false
    default: "auto"
    description: "Path to brand_config.yaml or 'auto' to use .cex/brand/brand_config.yaml"
    validation: "File must exist and pass brand_validate.py"

  language:
    type: string
    required: false
    default: "pt-BR"
    enum: [pt-BR, en, es, fr, de]
    description: "Primary content language"

  tone:
    type: string
    required: false
    default: "from_brand_config"
    enum: [technical, casual, formal, provocative, educational, inspirational, from_brand_config]
    description: "Override brand voice tone for this specific order"

  depth:
    type: string
    required: false
    default: "standard"
    enum: [brief, standard, deep, exhaustive]
    description: "Content depth. Brief=overview, deep=tutorial, exhaustive=reference"
    mapping:
      brief: "500-800 words/blog, 5 slides, 60s video"
      standard: "1200-1800 words/blog, 12 slides, 90s video"
      deep: "2500-3500 words/blog, 20 slides, 3min video"
      exhaustive: "4000-6000 words/blog, 30 slides, 5min video"

  course_config:
    type: object
    required: false
    description: "Only required when formats includes course_module"
    properties:
      modules:
        type: integer
        min: 1
        max: 12
        default: 8
      include_quiz:
        type: boolean
        default: true
      include_certificate:
        type: boolean
        default: false
      platform:
        type: string
        enum: [hotmart, self_hosted, youtube, none]
        default: hotmart

  social_config:
    type: object
    required: false
    description: "Only required when formats includes social_media_set"
    properties:
      platforms:
        type: array
        items:
          type: string
          enum: [instagram, linkedin, twitter_x, youtube, tiktok, facebook]
        default: [instagram, linkedin, twitter_x]
      posts_per_platform:
        type: integer
        min: 1
        max: 7
        default: 3
      include_canva_designs:
        type: boolean
        default: true

  video_config:
    type: object
    required: false
    description: "Only for video_produced_short or video_produced_long"
    properties:
      voice:
        type: string
        enum: [elevenlabs_default, elevenlabs_custom, notebooklm, none]
        default: elevenlabs_default
      subtitles:
        type: boolean
        default: true
      aspect_ratio:
        type: string
        enum: ["16:9", "9:16", "1:1"]
        default: "9:16"

  delivery:
    type: object
    required: false
    properties:
      priority:
        type: string
        enum: [standard, rush]
        default: standard
        description: "Rush = process immediately (costs 1.5x credits)"
      notify_email:
        type: string
        format: email
        required: false
        description: "Email for delivery notification"
      auto_publish:
        type: boolean
        default: false
        description: "Publish to configured channels on completion"
      output_format:
        type: string
        enum: [markdown, html, pdf, all]
        default: markdown

  # === BILLING FIELDS (auto-populated by checkout) ===

  billing:
    type: object
    required: false
    description: "Populated by checkout system, not by customer directly"
    properties:
      customer_id:
        type: string
        description: "Stripe/MP customer ID"
      tier:
        type: string
        enum: [free, creator, pro, studio, factory]
      credits_available:
        type: integer
        description: "Current balance in credits"
      credits_required:
        type: integer
        description: "Estimated cost for this order (calculated at validation)"
      payment_method:
        type: string
        enum: [subscription, credit_pack, pix, card]

  # === METADATA ===

  metadata:
    type: object
    required: false
    properties:
      campaign_name:
        type: string
        max_length: 100
        description: "Group orders by campaign for analytics"
      reference_urls:
        type: array
        items:
          type: string
          format: uri
        max_items: 5
        description: "URLs for research context (competitor pages, source material)"
      notes:
        type: string
        max_length: 1000
        description: "Free-text instructions for the pipeline"
```

---

## 2. Validation Rules

### 2.1 Pre-Pipeline Gates

| # | Rule | Error Code | Message |
|---|------|-----------|---------|
| V1 | `topic.length >= 10` | TOPIC_TOO_SHORT | "Topic must be at least 10 characters. Be specific." |
| V2 | `audience` object present | AUDIENCE_MISSING | "Who is this for? Specify segment and skill_level." |
| V3 | `formats` has >= 1 item | NO_FORMATS | "Select at least 1 output format." |
| V4 | `course_config` present if `course_module` in formats | COURSE_CONFIG_MISSING | "Course module selected but no course_config provided." |
| V5 | `billing.credits_available >= billing.credits_required` | INSUFFICIENT_CREDITS | "Not enough credits. Need {required}, have {available}." |
| V6 | `brand_config` file exists (if not 'auto') | BRAND_NOT_FOUND | "Brand config file not found at specified path." |
| V7 | No duplicate formats in array | DUPLICATE_FORMAT | "Format '{format}' listed twice." |
| V8 | `video_produced_*` requires tier >= creator | VIDEO_REQUIRES_PAID | "Video production requires Creator tier or above." |
| V9 | `course_module` requires tier >= pro | COURSE_REQUIRES_PRO | "Course modules require Pro tier or above." |

### 2.2 Credit Calculation

```python
def calculate_credits(order):
    CREDIT_MAP = {
        "blog_post": 8,
        "social_media_set": 12,
        "video_script": 5,
        "video_produced_short": 25,
        "video_produced_long": 45,
        "podcast_episode": 10,
        "course_module": 30,
        "ebook_chapter": 10,
        "presentation": 12,
        "email_sequence": 8,
        "landing_page": 15,
    }
    
    base = sum(CREDIT_MAP[f] for f in order["formats"])
    
    # Course modules multiply by count
    if "course_module" in order["formats"]:
        modules = order.get("course_config", {}).get("modules", 8)
        base += CREDIT_MAP["course_module"] * (modules - 1)  # first already counted
    
    # Rush surcharge
    if order.get("delivery", {}).get("priority") == "rush":
        base = int(base * 1.5)
    
    # Bundle discount (4+ formats = 20% off)
    if len(order["formats"]) >= 4:
        base = int(base * 0.80)
    
    return base
```

---

## 3. Example Orders

### 3.1 Minimal Order (Free Tier)

```yaml
topic: "Introduction to Python type hints for beginners"
audience:
  segment: developer
  skill_level: beginner
formats:
  - blog_post
  - social_media_set
# Credits: 8 + 12 = 20 (within free tier limits)
```

### 3.2 Standard Order (Pro Tier)

```yaml
topic: "How to build a content pipeline using CEX 8F"
audience:
  segment: developer
  skill_level: intermediate
formats:
  - blog_post
  - social_media_set
  - video_produced_short
  - podcast_episode
  - presentation
  - email_sequence
language: pt-BR
tone: technical
depth: standard
social_config:
  platforms: [instagram, linkedin, twitter_x, youtube]
  posts_per_platform: 3
  include_canva_designs: true
video_config:
  voice: elevenlabs_default
  subtitles: true
  aspect_ratio: "9:16"
delivery:
  priority: standard
  auto_publish: false
  output_format: all
metadata:
  campaign_name: "CEX_launch_week1"
# Credits: (8+12+25+10+12+8) * 0.80 = 60 credits (bundle discount applied)
```

### 3.3 Full Factory Order (Studio Tier)

```yaml
topic: "Complete guide to pricing SaaS products in Brazil: strategy, psychology, competitors"
audience:
  segment: executive
  skill_level: advanced
formats:
  - blog_post
  - social_media_set
  - video_script
  - video_produced_short
  - video_produced_long
  - podcast_episode
  - course_module
  - ebook_chapter
  - presentation
  - email_sequence
  - landing_page
language: pt-BR
tone: educational
depth: deep
course_config:
  modules: 6
  include_quiz: true
  include_certificate: true
  platform: hotmart
social_config:
  platforms: [instagram, linkedin, twitter_x, youtube, tiktok]
  posts_per_platform: 5
  include_canva_designs: true
video_config:
  voice: elevenlabs_default
  subtitles: true
  aspect_ratio: "9:16"
delivery:
  priority: rush
  notify_email: customer@example.com
  auto_publish: false
  output_format: all
metadata:
  campaign_name: "saas_pricing_masterclass"
  reference_urls:
    - "https://example.com/competitor-pricing"
  notes: "Focus on Brazilian market dynamics. Include PIX payment psychology."
# Credits: base ~330 + 5 extra modules (150) = 480. Bundle 20% = 384. Rush 1.5x = 576 credits
```

---

## 4. Order Lifecycle

```
[SUBMIT] --> [VALIDATE] --> [ESTIMATE] --> [AUTHORIZE] --> [QUEUE] --> [EXECUTE] --> [DELIVER]
               |               |               |
               v               v               v
          Reject if       Calculate        Check credits
          invalid        credits needed    or trigger
          (V1-V9)                          checkout
```

| Stage | Owner | Output |
|-------|-------|--------|
| SUBMIT | Customer (UI/API/CLI) | Raw order payload |
| VALIDATE | N05 (input validator) | Validated order or error codes |
| ESTIMATE | N06 (pricing engine) | credits_required, estimated_time |
| AUTHORIZE | N06 (billing) | Payment confirmed or checkout_url |
| QUEUE | N07 (orchestrator) | Position in pipeline, ETA |
| EXECUTE | N03+N04 (producers) | Content artifacts per format |
| DELIVER | N05 (ops) | Files + notification + optional auto-publish |

---

## 5. API Endpoint Mapping

```yaml
endpoints:
  create_order:
    method: POST
    path: /api/v1/orders
    body: content_order (this schema)
    response: { order_id, credits_required, estimated_time, status }
    
  get_order:
    method: GET
    path: /api/v1/orders/{order_id}
    response: { order, status, outputs[], progress_pct }
    
  list_orders:
    method: GET
    path: /api/v1/orders?status={status}&campaign={campaign}
    response: { orders[], total, page }
    
  cancel_order:
    method: DELETE
    path: /api/v1/orders/{order_id}
    response: { refunded_credits }
    constraints: "Only cancellable if status=queued. In-progress orders: partial refund."
    
  estimate_order:
    method: POST
    path: /api/v1/orders/estimate
    body: content_order (partial -- topic + formats minimum)
    response: { credits_required, estimated_time, available_credits }
```

---

*Generated by N06 Commercial Nucleus -- Content Order Schema*
*Every field earns its place. No optional bloat. Validates before burning credits.*

## Boundary

Contrato de entrada que define dados requeridos. NAO eh validation_schema (saida) nem type_def (definicao abstrata).


## 8F Pipeline Function

Primary function: **CONSTRAIN**
