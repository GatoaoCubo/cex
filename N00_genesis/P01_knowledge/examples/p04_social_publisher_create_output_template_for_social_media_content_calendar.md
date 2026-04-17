---
id: p04_output_template_social_publisher_content_calendar
kind: output_template
pillar: P04
title: "Output Template: Social Media Content Calendar"
version: "1.0.0"
created: "2026-04-02"
author: "social-publisher-builder"
domain: social_publisher
quality: 9.1
tags: [social-publisher, output-template, content-calendar, automation, scheduling]
keywords: [content-calendar, social-media, auto-posting, pipeline, schedule, weekly-plan]
tldr: "Weekly content calendar template for config-driven social publishing — maps days × post types × platforms with rotation rules, quality gates, and pipeline trace format."
density_score: 0.92
---
# Output Template: Social Media Content Calendar

## Purpose
This template defines the **output structure** for a social publisher's weekly content calendar. It governs what gets generated at F6 (PRODUCE) and validated at F7 (GOVERN) for any `social_publisher` instance. Fill `{{variables}}` per company config.

---

## 1. Weekly Calendar Block

```yaml
# Content Calendar — {{empresa}} — Week of {{week_start_date}}
# Generated: {{generated_at}} | Pipeline: social-publisher-builder v1.0.0

calendar:
  week_start: "{{week_start_date}}"       # ISO 8601 — e.g. 2026-04-06
  timezone: "{{timezone}}"               # IANA — e.g. America/Sao_Paulo
  total_posts: {{total_posts_week}}       # integer, computed from calendar
  platforms: [{{platforms_list}}]

  days:
    monday:
      date: "{{mon_date}}"
      slots:
        - time: "{{mon_slot1_time}}"
          platform: "{{mon_slot1_platform}}"
          content_type: "{{mon_slot1_type}}"   # product|educational|tips|trends
          item_id: "{{mon_slot1_item_id}}"
          status: pending                       # pending|approved|published|failed
          caption_preview: "{{mon_slot1_caption_preview}}"  # first 80 chars
          hashtags: [{{mon_slot1_hashtags}}]
          media_url_env: "{{MON_SLOT1_MEDIA_ENV}}"

    tuesday:
      date: "{{tue_date}}"
      slots:
        - time: "{{tue_slot1_time}}"
          platform: "{{tue_slot1_platform}}"
          content_type: "{{tue_slot1_type}}"
          item_id: "{{tue_slot1_item_id}}"
          status: pending
          caption_preview: "{{tue_slot1_caption_preview}}"
          hashtags: [{{tue_slot1_hashtags}}]
          media_url_env: "{{TUE_SLOT1_MEDIA_ENV}}"

    wednesday:
      date: "{{wed_date}}"
      slots:
        - time: "{{wed_slot1_time}}"
          platform: "{{wed_slot1_platform}}"
          content_type: "{{wed_slot1_type}}"
          item_id: "{{wed_slot1_item_id}}"
          status: pending
          caption_preview: "{{wed_slot1_caption_preview}}"
          hashtags: [{{wed_slot1_hashtags}}]
          media_url_env: "{{WED_SLOT1_MEDIA_ENV}}"

    thursday:
      date: "{{thu_date}}"
      slots:
        - time: "{{thu_slot1_time}}"
          platform: "{{thu_slot1_platform}}"
          content_type: "{{thu_slot1_type}}"
          item_id: "{{thu_slot1_item_id}}"
          status: pending
          caption_preview: "{{thu_slot1_caption_preview}}"
          hashtags: [{{thu_slot1_hashtags}}]
          media_url_env: "{{THU_SLOT1_MEDIA_ENV}}"

    friday:
      date: "{{fri_date}}"
      slots:
        - time: "{{fri_slot1_time}}"
          platform: "{{fri_slot1_platform}}"
          content_type: "{{fri_slot1_type}}"
          item_id: "{{fri_slot1_item_id}}"
          status: pending
          caption_preview: "{{fri_slot1_caption_preview}}"
          hashtags: [{{fri_slot1_hashtags}}]
          media_url_env: "{{FRI_SLOT1_MEDIA_ENV}}"

    saturday:
      date: "{{sat_date}}"
      slots:
        - time: "{{sat_slot1_time}}"
          platform: "{{sat_slot1_platform}}"
          content_type: "{{sat_slot1_type}}"
          item_id: "{{sat_slot1_item_id}}"
          status: pending
          caption_preview: "{{sat_slot1_caption_preview}}"
          hashtags: [{{sat_slot1_hashtags}}]
          media_url_env: "{{SAT_SLOT1_MEDIA_ENV}}"

    sunday:
      date: "{{sun_date}}"
      slots:
        - time: "{{sun_slot1_time}}"
          platform: "{{sun_slot1_platform}}"
          content_type: "{{sun_slot1_type}}"
          item_id: "{{sun_slot1_item_id}}"
          status: pending
          caption_preview: "{{sun_slot1_caption_preview}}"
          hashtags: [{{sun_slot1_hashtags}}]
          media_url_env: "{{SUN_SLOT1_MEDIA_ENV}}"
```

---

## 2. Content Mix Validation Block

```yaml
# Computed at F7 GOVERN — must match config.content_mix within ±5%
mix_audit:
  week_of: "{{week_start_date}}"
  planned:
    product:     {{planned_pct_product}}%      # target: {{cfg_pct_product}}%
    educational: {{planned_pct_educational}}%  # target: {{cfg_pct_educational}}%
    tips:        {{planned_pct_tips}}%         # target: {{cfg_pct_tips}}%
    trends:      {{planned_pct_trends}}%       # target: {{cfg_pct_trends}}%
    total:       100%
  drift_ok: {{mix_drift_ok}}                   # true|false — fail F7 if false
```

---

## 3. Post Log Entry (per published slot)

```yaml
# Written by LOG step (step 8) after each publish
log_entry:
  timestamp: "{{publish_timestamp}}"          # ISO 8601 UTC
  empresa: "{{empresa}}"
  platform: "{{platform}}"
  content_type: "{{content_type}}"
  item_id: "{{item_id}}"
  post_id: "{{platform_post_id}}"             # returned by API
  post_url: "{{post_url}}"
  caption_length: {{caption_char_count}}
  hashtag_count: {{hashtag_count}}
  media_attached: {{media_attached}}          # true|false
  publisher_api: "{{publisher_type}}"
  attempt: {{attempt_number}}                 # 1-3 (retry tracking)
  status: "{{status}}"                        # published|failed|skipped
  error_code: "{{error_code}}"               # null if status=published
  next_eligible: "{{cooldown_expiry_date}}"  # item_id locked until this date
```

---

## 4. Pipeline Execution Trace (per calendar cycle)

```
=== SOCIAL PUBLISHER PIPELINE — {{empresa}} ===
STEP 1  LOAD      config: {{config_path}} → OK ({{config_byte_count}}B)
STEP 2  FETCH     catalog: {{catalog_type}} → {{item_count}} items fetched
STEP 3  SELECT    item {{item_id}} (cooldown OK, type={{content_type}})
STEP 4  GENERATE  caption: {{caption_char_count}} chars (platform={{platform}})
STEP 5  OPTIMIZE  scheduled: {{scheduled_time}} {{timezone}}
STEP 6  HASHTAGS  {{hashtag_count}} tags (brand={{brand_count}}, niche={{niche_count}})
STEP 7  PUBLISH   → {{publisher_type}} → post_id={{post_id}} [attempt {{attempt}}]
STEP 8  LOG       → {{log_path}} ({{log_byte_count}}B appended)
STEP 9  NOTIFY    → {{notify_type}} channel → {{notify_status}}
STEP 10 ROTATE    item {{item_id}} cooldown until {{cooldown_expiry_date}}
=== STATUS: {{cycle_status}} | duration: {{duration_ms}}ms ===
```

---

## 5. Weekly Summary Report Block

```yaml
# Produced at end of week by aggregating log entries
weekly_summary:
  empresa: "{{empresa}}"
  week: "{{week_start_date}}"
  posts_planned: {{posts_planned}}
  posts_published: {{posts_published}}
  posts_failed: {{posts_failed}}
  posts_skipped: {{posts_skipped}}
  publish_rate: "{{publish_rate_pct}}%"
  by_platform:
    instagram:  { planned: {{ig_planned}},  published: {{ig_published}} }
    facebook:   { planned: {{fb_planned}},  published: {{fb_published}} }
    tiktok:     { planned: {{tt_planned}},  published: {{tt_published}} }
    linkedin:   { planned: {{li_planned}},  published: {{li_published}} }
    twitter:    { planned: {{tw_planned}},  published: {{tw_published}} }
  top_item_id: "{{top_performing_item_id}}"   # highest engagement (if analytics hooked)
  mix_compliance: {{mix_drift_ok}}            # true = within ±5% of target
  api_errors: {{api_error_count}}
  retry_total: {{retry_total}}
```

---

## 6. Slot Status Lifecycle

```
pending ──► approved ──► scheduled ──► published
    │                         │
    └──► skipped (empty queue)└──► failed ──► retry (max 3) ──► failed_final
```

| Status | Meaning | Next Action |
|--------|---------|-------------|
| `pending` | Generated, not yet reviewed | Human review OR auto-approve |
| `approved` | Cleared for publishing | Time optimizer schedules |
| `scheduled` | Queued in publisher API | Wait for publish window |
| `published` | Confirmed by API response | Log + Notify + Rotate |
| `failed` | API returned error | Retry (exponential backoff) |
| `skipped` | Empty queue or cooldown | Skip cycle, log reason |
| `failed_final` | Max retries exhausted | Alert via notification channel |

---

## 7. Quality Gate Checklist (F7 GOVERN)

| Gate | Check | Pass Condition |
|------|-------|---------------|
| H1 | Calendar completeness | 7 days defined, each with ≥1 slot |
| H2 | No plaintext secrets | All media/API refs are ENV_VAR names |
| H3 | Mix sum | `planned.*` percentages sum to exactly 100 |
| H4 | Caption length | Each preview ≤ platform max (IG 2200, TW 280) |
| H5 | Hashtag count | Each slot ≤ platform max (IG 30, LI 5, TW 3) |
| H6 | Timezone present | `calendar.timezone` is valid IANA string |
| H7 | Status field present | Every slot has `status: pending` on generation |
| S1 | Log entry schema | All 14 log fields present per entry |
| S2 | Pipeline trace | All 10 steps appear in trace output |
| S3 | Cooldown tracked | `next_eligible` date set after every publish |
| S4 | Retry count tracked | `attempt` field increments per retry |
| S5 | Weekly summary | Summary block generated end-of-week |