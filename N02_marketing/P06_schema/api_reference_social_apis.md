---
id: api_reference_social_apis
kind: api_reference
8f: F5_call
pillar: P06
nucleus: n02
title: "Social Platform API Reference -- Meta, LinkedIn, X"
version: 1.0.0
quality: 9.0
tags: [api_reference, social_apis, meta, linkedin, x_twitter, publishing_contract, P06, n02_marketing]
domain: social-distribution
status: active
density_score: 1.0
related:
  - p01_kc_ayrshare_api
  - n06_schema_brand_config
  - kc_api_reference
  - p03_ch_content_pipeline
  - bld_tools_social_publisher
  - bld_schema_api_reference
  - bld_schema_model_registry
  - bld_examples_api_reference
  - p12_wf_cf_publish_social
  - p03_ch_kc_to_notebooklm
---

# Social Platform API Reference

## Purpose

N02 distributes content. Distribution requires platform contracts.
This reference defines the posting APIs, rate limits, authentication,
and payload schemas for the three primary B2B+B2C social platforms.
`social_publisher_n02.md` consumes this directly.

---

## Meta Graph API (Instagram + Facebook)

### Authentication
```
Type: OAuth 2.0
Token: User Access Token or Page Access Token
Scopes: instagram_basic, instagram_content_publish, pages_read_engagement
Token TTL: 60 days (long-lived); refresh via /{user-id}/accounts
Base URL: https://graph.facebook.com/v21.0/
```

### Instagram Publishing Flow

```
Step 1 -- Create Media Container:
POST /{ig-user-id}/media
Payload:
  image_url: string (public URL, JPEG/PNG, max 8MB)
  caption: string (max 2200 chars)
  location_id: string (optional)
  user_tags: array (optional)
  hashtags: embedded in caption

Step 2 -- Publish Container:
POST /{ig-user-id}/media_publish
Payload:
  creation_id: string (from Step 1 response)

Response:
  id: string (published media ID)
```

### Meta Ads API (Campaign Creation)

```
POST /act_{ad-account-id}/campaigns
Payload:
  name: string
  objective: OUTCOME_AWARENESS|OUTCOME_TRAFFIC|OUTCOME_ENGAGEMENT|
             OUTCOME_LEADS|OUTCOME_APP_PROMOTION|OUTCOME_SALES
  status: ACTIVE|PAUSED
  special_ad_categories: array (HOUSING|CREDIT|EMPLOYMENT|[] for none)
  budget_optimization: {budget_rebalance_flag: true}

POST /act_{ad-account-id}/adsets
POST /act_{ad-account-id}/ads
POST /act_{ad-account-id}/adcreatives
```

### Rate Limits (Meta)

| Endpoint Class | Limit | Window |
|---------------|-------|--------|
| Graph API | 200 calls | per user per hour |
| Instagram Content Publish | 25 posts | per 24 hours |
| Ads API | 100 calls | per user per hour |
| Business Discovery API | 200 calls | per app per hour |

---

## LinkedIn API

### Authentication
```
Type: OAuth 2.0 (3-legged)
Scopes: w_member_social, r_emailaddress, r_liteprofile
        (org posts): w_organization_social, r_organization_social
Base URL: https://api.linkedin.com/v2/
```

### Post Creation (UGC API)

```
POST /ugcPosts
Headers:
  Authorization: Bearer {access_token}
  Content-Type: application/json
  X-Restli-Protocol-Version: 2.0.0

Payload:
  author: "urn:li:person:{personId}" | "urn:li:organization:{orgId}"
  lifecycleState: PUBLISHED
  specificContent:
    com.linkedin.ugc.ShareContent:
      shareCommentary:
        text: string (max 3000 chars)
      shareMediaCategory: NONE|ARTICLE|IMAGE|VIDEO|RICH
      media: array (if image/video)
  visibility:
    com.linkedin.ugc.MemberNetworkVisibility: PUBLIC|CONNECTIONS
```

### Image Upload (2-step)

```
Step 1 -- Initialize Upload:
POST /assets?action=registerUpload
Payload:
  registerUploadRequest:
    recipes: ["urn:li:digitalmediaRecipe:feedshare-image"]
    owner: "urn:li:person:{personId}"
    serviceRelationships: [{relationshipType: OWNER, identifier: urn:li:userGeneratedContent}]

Step 2 -- Binary Upload:
PUT {uploadUrl} (from Step 1 response)
Body: binary image data
Content-Type: image/jpeg|image/png
```

### Rate Limits (LinkedIn)

| Endpoint | Limit | Window |
|---------|-------|--------|
| UGC Posts | 150 posts | per day per member |
| Video Uploads | 50 | per day |
| API Calls | 100,000 | per day per app |
| Throttle | 3 req/sec | sustained |

---

## X (Twitter) API v2

### Authentication
```
Type: OAuth 2.0 (PKCE) or OAuth 1.0a
Scopes: tweet.read, tweet.write, users.read, offline.access
Base URL: https://api.twitter.com/2/
```

### Tweet Creation

```
POST /tweets
Headers:
  Authorization: Bearer {access_token}
  Content-Type: application/json

Payload:
  text: string (max 280 chars; URLs = 23 chars each)
  media:
    media_ids: array[string]
    tagged_user_ids: array[string]
  poll:
    options: array[string] (2-4 options)
    duration_minutes: integer (5-10080)
  reply:
    in_reply_to_tweet_id: string
  quote_tweet_id: string
```

### Media Upload

```
POST https://upload.twitter.com/1.1/media/upload.json
Method: INIT + APPEND + FINALIZE (chunked for video)

INIT:
  command: INIT
  total_bytes: integer
  media_type: image/jpeg|image/png|image/gif|video/mp4

FINALIZE:
  command: FINALIZE
  media_id_string: string (from INIT)
```

### Rate Limits (X)

| Tier | Monthly Tweets | Per-Request |
|------|-------------|-------------|
| Free | 1,500 | 1 req/15min writes |
| Basic ($100/mo) | 3,000 | 100 tweets/day |
| Pro ($5000/mo) | 300,000 | enterprise SLAs |

---

## Error Handling Contract

```yaml
social_api_error:
  platform: meta|linkedin|x
  error_code: string
  error_message: string
  retry_eligible: boolean
  backoff_seconds: integer
  fallback_action: skip|queue|draft|alert

common_errors:
  - code: "190" (Meta): token expired -> refresh flow
  - code: "32" (X): token invalid -> re-auth
  - code: "429": rate limit -> exponential backoff (30s, 60s, 120s)
  - code: "400": payload invalid -> validate against schema before retry
```

## Integration Reference

- Consumed by: `social_publisher_n02.md` (publishing tool)
- Validated against: `validation_schema_content_spec.md` (before payload construction)
- Scheduled via: `workflow_campaign_pipeline.md` (F8 COLLABORATE step)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_ayrshare_api]] | upstream | 0.35 |
| [[n06_schema_brand_config]] | related | 0.29 |
| [[kc_api_reference]] | upstream | 0.27 |
| [[p03_ch_content_pipeline]] | upstream | 0.26 |
| [[bld_tools_social_publisher]] | upstream | 0.26 |
| [[bld_schema_api_reference]] | related | 0.25 |
| [[bld_schema_model_registry]] | related | 0.25 |
| [[bld_examples_api_reference]] | downstream | 0.24 |
| [[p12_wf_cf_publish_social]] | downstream | 0.23 |
| [[p03_ch_kc_to_notebooklm]] | upstream | 0.23 |
