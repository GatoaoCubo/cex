---
title: Input Schema for Content Order Validation
description: Contract defining required data for content pipeline execution
generator: N06 Commercial Nucleus
version: 1.3.2
depends_on: 
  - N05 (input validator)
  - N06 (pricing engine)
  - N07 (orchestrator)
  - N03+N04 (producers)
  - N05 (ops)
pipeline_stage: 1 (submit)
---
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
| AUTHORIZE | N06 (billing engine) | Payment authorization status |
| QUEUE | N07 (orchestrator) | Scheduled execution time |
| EXECUTE | N03+N04 (producers) | Generated content artifacts |
| DELIVER | N05 (ops) | Delivered content to end user |

---

## Related Kinds

- **validation_schema**: Defines output validation rules, ensuring generated content meets quality and format standards. Complements this schema by validating artifacts post-production.
- **type_def**: Abstract data definitions used across the system. This schema references type_def for consistent data modeling.
- **pricing_engine**: Handles credit calculations and cost estimation. Directly integrated with this schema's credit calculation logic.
- **orchestrator**: Manages pipeline stages (queue, execute). Relies on this schema for order validation before execution.
- **billing_engine**: Manages payment methods and credit checks. Works with the billing section of this schema to authorize orders.

---

## 8F Pipeline Function

**Stage 1 (submit)**: Input validation and credit authorization  
**Constraint Type**: Hard constraint (order rejected if validation fails)  
**Dependencies**: N05, N06, N07  
**Output**: Validated order ready for execution

---

## Boundary

**Input Contract**:  
- Required fields: `topic`, `audience`, `formats`  
- Optional fields: `language`, `tone`, `depth`, `delivery`, `metadata`  
- Constraints: Tier-based access control, credit limits, format-specific rules  

**Output Contract**:  
- Validated order object with error codes if invalid  
- Credit requirement calculation  
- Execution readiness status  

**System Interface**:  
- REST API endpoint: `/api/v1/order/validate`  
- Expected response format: JSON with `valid`, `errors`, `credits_required` fields  
- Error codes: 400 (invalid input), 402 (insufficient credits), 500 (system error)