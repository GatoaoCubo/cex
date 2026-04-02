---
id: tpl_social_publisher_content_calendar
kind: cli_tool
pillar: P04
title: "Social Publisher — Output Template for Content Calendar"
version: "1.0.0"
created: "2026-04-02"
author: "social-publisher-builder"
domain: social_publisher
quality: 8.9
tags: [social-publisher, content-calendar, automation, template]
tldr: "Config-driven social media publishing pipeline with 10-step automation: LOAD→FETCH→SELECT→GENERATE→OPTIMIZE→HASHTAGS→PUBLISH→LOG→NOTIFY→ROTATE"
density_score: 0.92
---
# Social Publisher — Output Template for Content Calendar

## Pipeline Architecture

### 10-Step Publishing Pipeline
| Step | Name | Input | Process | Output | Failure Recovery |
|------|------|-------|---------|--------|-----------------|
| 1 | LOAD | config.yaml path | Parse and validate configuration | Validated config object | FileNotFound → abort with error |
| 2 | FETCH | catalog source + credentials | Query API/DB for content list | Array of content items | Timeout → retry 3x, then skip cycle |
| 3 | SELECT | content list + rotation state | Apply cooldown rules and content mix | Next item to publish | Empty queue → skip cycle gracefully |
| 4 | GENERATE | item + persona + platform | LLM call for caption generation | Platform-optimized caption | LLM error → use fallback template |
| 5 | OPTIMIZE | platform + timezone + calendar | Calculate best posting time | Scheduled datetime | Missing data → use default schedule |
| 6 | HASHTAGS | niche + brand tags + platform limits | Generate hashtag string | Optimized hashtags within limits | Over limit → truncate to max |
| 7 | PUBLISH | caption + media + hashtags + API | Send to social platform | Post ID + public URL | API error → exponential backoff retry |
| 8 | LOG | post result + metadata + timestamp | Write structured JSON log | Audit trail entry | Log failure → stderr + continue |
| 9 | NOTIFY | post URL + status + webhook config | Send notification to team | Notification delivered | Channel down → skip silently |
| 10 | ROTATE | posted item + cooldown period | Update rotation state | Refreshed cooldown tracker | State corrupt → rebuild from logs |

## Configuration Template

```yaml
# Social Publisher Configuration
# Company: {{empresa}}
# Generated: {{timestamp}}

identity:
  empresa: "{{empresa}}"
  handle: "{{social_handle}}"
  nicho: "{{nicho}}"           # pet, food, saas, fashion, fitness, beauty, tech, education
  tom: "{{tom}}"               # casual/professional, friendly/formal, playful/serious
  persona: "{{persona_name}}"  # Brand voice persona name
  bio: "{{brand_bio}}"         # Max 160 chars for bio optimization

platforms: [{{platforms_list}}]  # instagram, facebook, tiktok, linkedin, twitter, youtube

schedule:
  timezone: "{{timezone}}"      # IANA timezone: America/Sao_Paulo, US/Eastern, Europe/London
  calendar:
    monday:    { type: "{{mon_type}}", time: "{{mon_time}}" }    # product/educational/tips/trends
    tuesday:   { type: "{{tue_type}}", time: "{{tue_time}}" }
    wednesday: { type: "{{wed_type}}", time: "{{wed_time}}" }
    thursday:  { type: "{{thu_type}}", time: "{{thu_time}}" }
    friday:    { type: "{{fri_type}}", time: "{{fri_time}}" }
    saturday:  { type: "{{sat_type}}", time: "{{sat_time}}" }
    sunday:    { type: "{{sun_type}}", time: "{{sun_time}}" }

content_mix:
  product: {{pct_product}}       # 0-100: % posts featuring products/services
  educational: {{pct_educational}} # 0-100: % educational/how-to content
  tips: {{pct_tips}}             # 0-100: % quick tips and tricks
  trends: {{pct_trends}}         # 0-100: % trending topics and news
  # CONSTRAINT: product + educational + tips + trends MUST = 100

catalog:
  type: "{{catalog_type}}"      # supabase, shopify, airtable, csv, api, manual
  url_env: "{{CATALOG_URL_ENV}}"        # Environment variable for connection URL
  key_env: "{{CATALOG_KEY_ENV}}"        # Environment variable for API key
  table: "{{catalog_table}}"            # Table/collection name
  fields:
    title: "{{title_field}}"           # Product/content title field
    description: "{{desc_field}}"      # Description field
    image: "{{image_field}}"           # Image URL field
    price: "{{price_field}}"           # Price field (optional)
    category: "{{category_field}}"     # Category/type field
  cooldown_days: {{cooldown}}           # Min days before reposting same item (1-30)

publisher:
  type: "{{publisher_type}}"    # ayrshare, postiz, meta_graph
  api_key_env: "{{PUBLISHER_KEY_ENV}}"  # Environment variable for API key
  base_url_env: "{{PUBLISHER_URL_ENV}}" # For self-hosted (Postiz)
  batch_size: {{batch_size}}            # Posts per batch (1-10)
  retry:
    max: {{retry_max}}                  # Maximum retry attempts (1-5)
    backoff: "exponential"              # exponential, linear, fixed
    base_seconds: {{retry_base}}        # Base wait time in seconds (10-300)

hashtags:
  brand: [{{brand_hashtags}}]           # Brand-specific hashtags
  niche: [{{niche_hashtags}}]           # Niche/industry hashtags
  trending: [{{trending_hashtags}}]     # Trending/seasonal hashtags
  max_per_post: {{max_hashtags}}        # Platform limit (IG: 30, TW: 3, LI: 5)
  strategy: "{{hashtag_strategy}}"      # mix_all, brand_first, niche_heavy

llm_generation:
  provider: "{{llm_provider}}"          # anthropic, openai, google
  model: "{{llm_model}}"                # claude-3-sonnet, gpt-4, gemini-pro
  api_key_env: "{{LLM_KEY_ENV}}"       # Environment variable for LLM API key
  max_tokens: {{max_tokens}}            # Token limit for caption generation
  temperature: {{temperature}}          # Creativity level (0.0-1.0)
  system_prompt: |
    You are {{persona_name}} from {{empresa}}. 
    Write {{tom}} social media captions for {{nicho}} audience.
    Brand bio: {{brand_bio}}

notifications:
  enabled: {{notify_enabled}}           # true/false
  channels:
    discord:
      enabled: {{discord_enabled}}      # true/false
      webhook_env: "{{DISCORD_WEBHOOK_ENV}}"
    slack:
      enabled: {{slack_enabled}}        # true/false
      webhook_env: "{{SLACK_WEBHOOK_ENV}}"
    email:
      enabled: {{email_enabled}}        # true/false
      smtp_env: "{{EMAIL_SMTP_ENV}}"
      recipient: "{{notification_email}}"

automation:
  cron:
    type: "{{cron_type}}"              # windows_task, crontab, systemd
    interval: "{{cron_interval}}"      # daily, hourly, "0 19 * * *"
    enabled: {{cron_enabled}}          # true/false
  monitoring:
    health_check_url: "{{health_url}}"  # Optional health check endpoint
    log_level: "{{log_level}}"          # DEBUG, INFO, WARN, ERROR
    max_log_files: {{max_logs}}         # Log rotation limit

quality_gates:
  caption:
    min_length: {{min_caption}}         # Minimum caption length
    max_length: {{max_caption}}         # Platform-specific max length
    required_elements: [{{required_elements}}]  # call_to_action, brand_mention, hashtags
  engagement:
    min_quality_score: {{min_score}}    # Minimum LLM quality score (0-10)
    profanity_check: {{profanity_check}} # true/false
    brand_voice_check: {{voice_check}}   # true/false
  posting:
    avoid_duplicates: {{avoid_dupes}}    # true/false
    respect_cooldown: {{respect_cool}}   # true/false
    platform_limits: {{platform_lims}}  # true/false
```

## Platform Matrix

| Platform | Max Caption | Max Hashtags | Image Sizes | Best Times | API Provider |
|----------|------------|-------------|-------------|------------|-------------|
| Instagram | 2200 chars | 30 (rec: 5-10) | 1080×1080, 1080×1350 | 11-13h, 19-21h | Meta Graph, Ayrshare |
| Facebook | 63206 chars | No limit (rec: 3-5) | 1200×630 | 13-16h | Meta Graph, Ayrshare |
| TikTok | 2200 chars | 5-8 | 1080×1920 (video) | 19-22h | Ayrshare, Postiz |
| LinkedIn | 3000 chars | 3-5 | 1200×627 | 8-10h, 17-18h | Ayrshare, Postiz |
| Twitter/X | 280 chars | 2-3 | 1200×675 | 9-11h, 12-13h | Ayrshare, Postiz |
| YouTube | 5000 chars | No limit | 1280×720 | 14-16h, 20-22h | Direct API |

## Content Calendar Template

```yaml
# 7-Day Content Calendar Template
weekly_schedule:
  structure: |
    MON: Educational (how-to, tutorials)
    TUE: Tips (quick wins, hacks)
    WED: Product (features, launches)
    THU: Educational (industry insights)
    FRI: Trends (news, viral topics)
    SAT: Tips (weekend activities)
    SUN: Product (testimonials, reviews)
  
  posting_times:
    business_hours: "09:00-17:00"
    peak_engagement: "12:00-13:00, 19:00-21:00"
    weekend_shift: "+2h"  # Post 2 hours later on weekends
  
  content_rotation:
    cycle_length: 21  # Days before repeating content themes
    cooldown_enforcement: strict  # strict/flexible
    seasonal_adjustments: true
```

## Quality Validation Rules

### HARD Requirements (must pass)
1. All content_mix percentages sum to exactly 100
2. No API keys in plaintext (only ENV_VAR references)
3. All platforms in list are supported
4. cooldown_days >= 1
5. Timezone is valid IANA string
6. Retry configuration present and valid

### SOFT Requirements (warnings)
1. At least 2 publisher types supported
2. Notification channel configured
3. Hashtag strategy defined
4. Caption length within platform limits
5. Posting times optimized for timezone
6. LLM generation parameters tuned
7. Quality gates configured
8. Monitoring/logging enabled

## Runtime State Management

```yaml
# Runtime state tracking (auto-generated)
rotation_state:
  last_posted: "2026-04-02T10:20:00Z"
  content_history:
    - id: "product_123"
      posted_at: "2026-04-01T19:00:00Z"
      platforms: ["instagram", "facebook"]
      cooldown_until: "2026-04-04T19:00:00Z"
  cycle_position:
    week: 1
    day: "tuesday"
    content_type: "tips"
  next_scheduled: "2026-04-02T19:00:00Z"

analytics_tracking:
  posts_this_month: 28
  engagement_avg: 4.2
  best_performing_time: "19:00"
  best_performing_type: "product"
  platform_performance:
    instagram: { posts: 15, avg_engagement: 5.1 }
    facebook: { posts: 13, avg_engagement: 3.3 }
```

## Security and Environment Variables

```bash
# Required environment variables (.env file)
# Catalog access
SUPABASE_URL=https://xyz.supabase.co
SUPABASE_KEY=eyJ...
SHOPIFY_API_KEY=shpat_...
AIRTABLE_KEY=key...

# Publisher APIs
AYRSHARE_API_KEY=ABCD-1234...
POSTIZ_URL=https://postiz.mycompany.com
POSTIZ_API_KEY=ptz_...
META_GRAPH_TOKEN=EAABw...

# LLM Generation
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
GOOGLE_AI_KEY=AIza...

# Notifications
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PASSWORD=app_password

# Health & Monitoring
HEALTH_CHECK_URL=https://status.mycompany.com/ping
LOG_WEBHOOK_URL=https://logging.mycompany.com/social
```

## Implementation Checklist

- [ ] Config validation (sum checks, required fields)
- [ ] Catalog connector (Supabase/Shopify/API integration)
- [ ] Content selection with cooldown enforcement
- [ ] LLM caption generation with retry logic
- [ ] Platform-specific optimization (hashtags, timing)
- [ ] Multi-provider publishing (Ayrshare/Postiz/Meta)
- [ ] Structured logging and error tracking
- [ ] Notification system (Discord/Slack/email)
- [ ] Rotation state persistence
- [ ] Cron/scheduler integration
- [ ] Health monitoring and alerting
- [ ] Quality gates and validation
- [ ] Analytics and performance tracking
- [ ] Security (environment variables, no plaintext secrets)