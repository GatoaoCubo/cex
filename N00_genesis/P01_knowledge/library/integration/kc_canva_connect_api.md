---
id: p01_kc_canva_connect_api
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Canva Connect API — Design Automation for Content Factory"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n04_knowledge
domain: canva_api
quality: 9.2
tags: [canva, api, design, content-factory, integration, oauth, INJECT]
tldr: "OAuth PKCE flow + REST endpoints for creating, autofilling, and exporting Canva designs programmatically"
when_to_use: "When any nucleus needs to create, modify, or export designs via Canva's Connect API"
keywords: [canva, connect-api, oauth-pkce, design-automation, brand-templates, export]
feeds_kinds: [api_client, workflow, dag]
linked_artifacts: [kc_ffmpeg_patterns, kc_ayrshare_api, kc_youtube_api]
density_score: null
related:
  - p04_fn_cf_canva_export
  - p01_kc_ayrshare_api
  - p04_fn_cf_canva_create
  - p01_kc_runway_api
  - spec_content_factory_v1
  - kc_api_reference
  - p01_kc_elevenlabs_tts
  - n06_api_access_pricing
  - bld_tools_social_publisher
  - p12_wf_cf_promote
---

# Canva Connect API

## Quick Reference
```yaml
base_url: https://api.canva.com/rest/v1
auth: OAuth 2.0 PKCE (Authorization Code + PKCE)
client_id: OC-AZ1jygW5KXZ_
scopes: design:content:read design:content:write design:meta:read asset:read asset:write brandtemplate:content:read brandtemplate:meta:read folder:read folder:write export:read export:write
token_endpoint: https://api.canva.com/rest/v1/oauth/token
authorize_endpoint: https://www.canva.com/api/oauth/authorize
rate_limit: 100 requests/min per user token
content_type: application/json
```

## Authentication — OAuth 2.0 PKCE Flow

Canva uses Authorization Code with PKCE (no client_secret needed for public clients). The flow:

1. Generate `code_verifier` (43-128 chars, URL-safe random) and `code_challenge` = base64url(SHA256(code_verifier))
2. Redirect user to `authorize_endpoint` with `client_id`, `redirect_uri`, `code_challenge`, `code_challenge_method=S256`, `scope`, `response_type=code`
3. User authorizes → Canva redirects back with `code`
4. Exchange `code` + `code_verifier` at `token_endpoint` for `access_token` (4h TTL) + `refresh_token`
5. Refresh with `grant_type=refresh_token` before expiry

Token storage: persist `refresh_token` securely. Access tokens expire in 4 hours.

## Core Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/designs` | POST | Create blank or from brand template |
| `/designs/{id}` | GET | Get design metadata |
| `/designs/{id}/autofill` | POST | Autofill template placeholders with data |
| `/exports` | POST | Start async export job |
| `/exports/{id}` | GET | Poll export status, get download URL |
| `/assets` | POST | Upload asset to user's media library |
| `/assets/{id}` | GET/DELETE | Get or remove asset |
| `/brand-templates` | GET | List brand templates |
| `/brand-templates/{id}` | GET | Get template details + placeholder names |
| `/folders` | POST | Create folder |
| `/folders/{id}/items` | GET | List folder contents |

## Design Creation + Export Example

```python
import httpx, time

headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

# 1. Create from brand template
resp = httpx.post("https://api.canva.com/rest/v1/designs", headers=headers, json={
    "design_type": {"type": "preset", "name": "InstagramPost"},
    "title": "Weekly Post — Week 14"
})
design_id = resp.json()["design"]["id"]

# 2. Autofill placeholders (template must have named placeholders)
httpx.post(f"https://api.canva.com/rest/v1/designs/{design_id}/autofill", headers=headers, json={
    "data": {
        "title_text": "5 Dicas de Produtividade",
        "body_text": "Aprenda como automatizar seu conteúdo",
        "image_placeholder": {"type": "image", "asset_id": "abc123"}
    }
})

# 3. Export as PNG (async — poll until done)
export_resp = httpx.post("https://api.canva.com/rest/v1/exports", headers=headers, json={
    "design_id": design_id,
    "format": {"type": "png", "quality": "high", "width": 1080, "height": 1080}
})
export_id = export_resp.json()["export"]["id"]

while True:
    status = httpx.get(f"https://api.canva.com/rest/v1/exports/{export_id}", headers=headers).json()
    if status["export"]["status"] == "completed":
        download_url = status["export"]["urls"][0]
        break
    time.sleep(2)
```

## Export Formats

| Format | Extensions | Notes |
|--------|-----------|-------|
| PNG | .png | Up to 4x resolution. Best for social media images. |
| JPG | .jpg | Lossy. Smaller files. Quality param 1-100. |
| PDF (standard) | .pdf | Single or multi-page. |
| PDF (print) | .pdf | Crop marks, bleed (3mm). CMYK profile. |
| PPTX | .pptx | Editable PowerPoint. Text stays editable. |
| MP4 | .mp4 | Video designs only. 720p or 1080p. |
| GIF | .gif | Animated designs. Max 20 pages/frames. |
| SVG | .svg | Pro/Enterprise only. Vector output. |

## Gotchas

- **Autofill requires named placeholders**: template must be set up in Canva with named data fields. If placeholders are unnamed, autofill silently ignores them.
- **Export is async**: always poll `/exports/{id}` — there's no webhook callback. Typical wait: 5-30s for images, 30-120s for video.
- **Rate limit 429**: back off exponentially. The 100/min limit is per-user, not per-app.
- **Brand templates vs regular templates**: only brand templates (Canva for Teams) support autofill. Free/Pro templates do not.
- **Asset upload size**: max 25MB per file for images. Video assets up to 1GB.
- **Token refresh race**: if two processes refresh simultaneously, one token invalidates the other. Use a mutex on refresh.
- **CORS**: API is server-side only. No browser calls — use a backend proxy.

## Cost

Canva Connect API is free for Canva for Teams subscribers. No per-call charges. The cost is the Teams subscription (~$100/year per seat for up to 5 people).

## Docs
- API Reference: https://www.canva.dev/docs/connect/
- Authentication: https://www.canva.dev/docs/connect/authentication/
- Autofill: https://www.canva.dev/docs/connect/autofill/

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_fn_cf_canva_export]] | downstream | 0.39 |
| [[p01_kc_ayrshare_api]] | sibling | 0.37 |
| [[p04_fn_cf_canva_create]] | downstream | 0.32 |
| [[p01_kc_runway_api]] | sibling | 0.28 |
| [[spec_content_factory_v1]] | downstream | 0.23 |
| [[kc_api_reference]] | sibling | 0.22 |
| [[p01_kc_elevenlabs_tts]] | sibling | 0.20 |
| [[n06_api_access_pricing]] | downstream | 0.20 |
| [[bld_tools_social_publisher]] | downstream | 0.20 |
| [[p12_wf_cf_promote]] | downstream | 0.19 |
