---
id: social_publisher_n02
kind: browser_tool
pillar: P04
nucleus: n02
title: "Social Publisher -- Multi-Channel Content Publishing Tool"
version: 1.0.0
quality: 8.9
tags: [browser_tool, social_publisher, multi_channel, distribution, publishing, P04, n02_marketing]
domain: content-distribution
status: active
density_score: 1.0
---

# Social Publisher -- Multi-Channel Content Distribution Tool

## Purpose

Copy that never ships is a draft. This tool is the final mile:
structured publishing to multiple social platforms, respecting rate limits,
handling errors, and recording proof of delivery for every asset.

## Tool Interface

```python
# Tool signature
def publish_asset(
    asset_id: str,
    copy_text: str,
    visual_path: str | None,
    platform: str,
    format: str,
    scheduled_at: str | None,
    campaign_id: str,
    dry_run: bool = False
) -> PublishResult
```

## Publisher Architecture

```
INPUT: validated copy asset + optional visual
    |
    v
ROUTE: platform selector
    |
    +-- instagram -> IGPublisher (Meta Graph API)
    +-- linkedin  -> LIPublisher (LinkedIn UGC API)
    +-- x         -> XPublisher (Twitter API v2)
    +-- meta_ads  -> MetaAdsPublisher (Meta Ads API)
    +-- email     -> EmailPublisher (SMTP/ESP integration)
    |
    v
PRE-FLIGHT: validate payload against api_reference_social_apis.md constraints
    |
    v
EXECUTE: API call with retry logic
    |
    v
LOG: publish record (platform_post_id, timestamp, asset_id, campaign_id)
    |
    v
RETURN: PublishResult object
```

## Platform Publisher Specs

### IGPublisher (Instagram)

```python
class IGPublisher:
    base_url = "https://graph.facebook.com/v21.0"
    auth: OAuth2 user access token
    rate_limit: 25 posts / 24h (tracked in session)

    def publish_post(self, ig_user_id, image_url, caption):
        # Step 1: create media container
        container_id = self._create_media(ig_user_id, image_url, caption)
        # Step 2: publish container
        return self._publish_media(ig_user_id, container_id)

    def publish_story(self, ig_user_id, media_url, sticker_data=None):
        ...

    def publish_carousel(self, ig_user_id, items, caption):
        # items: [{image_url, caption_per_card}]
        children = [self._create_media(ig_user_id, item["url"]) for item in items]
        return self._create_carousel(ig_user_id, children, caption)
```

### LIPublisher (LinkedIn)

```python
class LIPublisher:
    base_url = "https://api.linkedin.com/v2"
    auth: OAuth2 3-legged token
    rate_limit: 150 posts / day (tracked)

    def publish_post(self, author_urn, text, image_urn=None):
        payload = {
            "author": author_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": text},
                    "shareMediaCategory": "IMAGE" if image_urn else "NONE",
                    "media": [{"status": "READY", "media": image_urn}] if image_urn else []
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
        }
        return self._post("/ugcPosts", payload)

    def upload_image(self, owner_urn, image_path) -> str:
        # returns asset URN for use in publish_post
        ...
```

### XPublisher (X/Twitter)

```python
class XPublisher:
    base_url = "https://api.twitter.com/2"
    auth: OAuth 2.0 PKCE
    rate_limit: 300 tweets / 3h (Basic tier)

    def publish_tweet(self, text, media_ids=None, reply_to=None):
        payload = {"text": text}
        if media_ids:
            payload["media"] = {"media_ids": media_ids}
        if reply_to:
            payload["reply"] = {"in_reply_to_tweet_id": reply_to}
        return self._post("/tweets", payload)

    def upload_media(self, media_path) -> str:
        # INIT + APPEND + FINALIZE flow
        # Returns media_id_string
        ...
```

## Rate Limit Tracking

```yaml
rate_limit_tracker:
  instagram:
    daily_posts_used: integer
    daily_posts_limit: 25
    reset_at: ISO 8601 datetime
  linkedin:
    daily_posts_used: integer
    daily_posts_limit: 150
    reset_at: ISO 8601 datetime
  x:
    window_tweets_used: integer
    window_tweets_limit: 300
    window_reset_at: ISO 8601 datetime

enforcement:
  on_limit_reached: queue_for_next_window
  queue_max_hours: 48
```

## Retry Logic

```yaml
retry_policy:
  max_attempts: 3
  backoff: exponential (base: 30s, factor: 2)
  retryable_errors: [429, 503, 504, 524]
  non_retryable_errors: [400, 401, 403]
  on_non_retryable:
    action: log_failure + notify_n07 + set_asset_status=failed
```

## PublishResult Schema

```yaml
publish_result:
  asset_id: string
  campaign_id: string
  platform: string
  format: string
  status: published|scheduled|failed|rate_limited|queued
  platform_post_id: string (nullable -- populated on success)
  published_at: ISO 8601 datetime (nullable)
  scheduled_at: ISO 8601 datetime (nullable)
  error: string (nullable)
  retry_count: integer
  dry_run: boolean
```

## Scheduling

```yaml
scheduler:
  engine: cron or datetime queue
  timezone: from brand_config.yaml (default: UTC)
  optimal_posting_times:
    instagram:
      B2C: ["09:00", "12:00", "17:00", "19:00"]
      B2B: ["08:00", "12:00", "17:00"]
    linkedin:
      B2B: ["07:30", "12:00", "17:00", "18:00"]
    x:
      B2B: ["08:00", "12:00", "17:00"]
  buffer_between_posts_minutes: 30  # min spacing to avoid spam signals
```

## Integration

- Consumes: `api_reference_social_apis.md` (platform API specs)
- Consumes: `validation_schema_content_spec.md` (pre-flight validation)
- Invoked by: `workflow_campaign_pipeline.md` (F8 DISTRIBUTE step)
- Feeds: `cohort_analysis_n02.md` (platform_post_id as tracking anchor)
