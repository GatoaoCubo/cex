---
id: p01_kc_youtube_api
kind: knowledge_card
type: domain
pillar: P01
title: "YouTube Data API — Video Publishing for Content Factory"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n04_knowledge
domain: youtube_api
quality: 9.0
tags: [youtube, api, video, upload, publishing, content-factory, integration, INJECT]
tldr: "OAuth 2.0 + REST API for uploading videos, setting metadata, managing playlists, and reading basic analytics"
when_to_use: "When any nucleus needs to publish video content to YouTube or manage channel playlists"
keywords: [youtube, data-api, upload, playlist, metadata, oauth, video-publishing]
feeds_kinds: [api_client, workflow, dag]
linked_artifacts: [kc_runway_api, kc_ffmpeg_patterns, kc_elevenlabs_tts, kc_ayrshare_api]
density_score: null
related:
  - p12_wf_cf_publish_youtube
  - p01_kc_ayrshare_api
  - bld_tools_vc_credential
  - bld_examples_vc_credential
  - n04_output_cf_integration_kcs
  - p01_kc_supabase_storage
  - wf_kc_to_content
  - p01_kc_canva_connect_api
---

# YouTube Data API

## Quick Reference
```yaml
base_url: https://www.googleapis.com/youtube/v3
upload_url: https://www.googleapis.com/upload/youtube/v3/videos
auth: OAuth 2.0 (installed app or web server flow)
api_key: YOUTUBE_API_KEY (for read-only public data)
scopes:
  - https://www.googleapis.com/auth/youtube.upload        # Upload videos
  - https://www.googleapis.com/auth/youtube               # Full channel management
  - https://www.googleapis.com/auth/youtube.readonly       # Read-only data
  - https://www.googleapis.com/auth/youtube.force-ssl      # Required for captions
quota: 10,000 units/day (default). Upload = 1,600 units. List = 1 unit.
rate_limit: ~5 requests/second per user
```

## Authentication (OAuth 2.0 for uploads)

```python
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import pickle, os

SCOPES = ["https://www.googleapis.com/auth/youtube.upload",
          "https://www.googleapis.com/auth/youtube"]

def get_youtube_service():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as f:
            creds = pickle.load(f)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", SCOPES)
            creds = flow.run_local_server(port=8080)
        with open("token.pickle", "wb") as f:
            pickle.dump(creds, f)
    return build("youtube", "v3", credentials=creds)
```

## Upload Video with Metadata

```python
from googleapiclient.http import MediaFileUpload

youtube = get_youtube_service()

# 1. Upload with resumable (handles large files + network interruptions)
body = {
    "snippet": {
        "title": "5 Dicas de Produtividade com IA",
        "description": """Neste vídeo, você vai aprender:
✅ Como usar IA para criar conteúdo 10x mais rápido
✅ Ferramentas que todo criador precisa conhecer
✅ Workflow completo: da ideia ao vídeo publicado

🔗 Links mencionados:
- Ferramenta 1: https://example.com
- Ferramenta 2: https://example.com

📧 Contato: email@brand.com

#ia #produtividade #contentcreator""",
        "tags": ["inteligência artificial", "produtividade", "criação de conteúdo",
                 "content creator", "IA", "automação"],
        "categoryId": "28",  # 28=Science & Technology, 22=People & Blogs, 27=Education
        "defaultLanguage": "pt-BR",
        "defaultAudioLanguage": "pt-BR"
    },
    "status": {
        "privacyStatus": "private",         # private → review → public
        "publishAt": "2026-04-07T10:00:00.000Z",  # Schedule (requires private status)
        "selfDeclaredMadeForKids": False,
        "embeddable": True,
        "license": "youtube"                # or "creativeCommon"
    }
}

media = MediaFileUpload("final_video.mp4",
    mimetype="video/mp4",
    resumable=True,
    chunksize=10*1024*1024   # 10MB chunks
)

request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

# Resumable upload with progress
response = None
while response is None:
    status, response = request.next_chunk()
    if status:
        print(f"Upload {int(status.progress() * 100)}%")

video_id = response["id"]
print(f"Uploaded: https://youtube.com/watch?v={video_id}")
```

## Set Custom Thumbnail

```python
youtube.thumbnails().set(
    videoId=video_id,
    media_body=MediaFileUpload("thumbnail.jpg", mimetype="image/jpeg")
).execute()
# Requires channel to be verified (phone verification)
# Thumbnail: 1280x720px, <2MB, JPG/PNG
```

## Playlist Management

```python
# Create playlist
playlist = youtube.playlists().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Série IA para Criadores",
            "description": "Curso completo de IA aplicada à criação de conteúdo"
        },
        "status": {"privacyStatus": "public"}
    }
).execute()
playlist_id = playlist["id"]

# Add video to playlist
youtube.playlistItems().insert(
    part="snippet",
    body={
        "snippet": {
            "playlistId": playlist_id,
            "resourceId": {"kind": "youtube#video", "videoId": video_id},
            "position": 0   # First position
        }
    }
).execute()
```

## Read Analytics (basic via Data API)

```python
# Get video statistics
stats = youtube.videos().list(
    part="statistics,snippet",
    id=video_id
).execute()

item = stats["items"][0]
print(f"Views: {item['statistics']['viewCount']}")
print(f"Likes: {item['statistics']['likeCount']}")
print(f"Comments: {item['statistics']['commentCount']}")
```

For advanced analytics (watch time, demographics, traffic sources), use YouTube Analytics API with scope `https://www.googleapis.com/auth/yt-analytics.readonly`.

## Category IDs (common)

| ID | Category |
|----|----------|
| 1 | Film & Animation |
| 10 | Music |
| 15 | Pets & Animals |
| 22 | People & Blogs |
| 24 | Entertainment |
| 25 | News & Politics |
| 26 | Howto & Style |
| 27 | Education |
| 28 | Science & Technology |

## Quota Costs

| Operation | Units |
|-----------|-------|
| videos.insert (upload) | 1,600 |
| videos.list | 1 |
| videos.update | 50 |
| thumbnails.set | 50 |
| playlists.insert | 50 |
| playlistItems.insert | 50 |
| search.list | 100 |

Default quota: 10,000 units/day. That's ~6 uploads/day. Request quota increase via Google Cloud Console if needed (can take weeks).

## Gotchas

- **Quota is 10K units/day.** Each upload costs 1,600 units = max 6 uploads/day on default quota. Plan batch uploads.
- **`publishAt` requires `privacyStatus: "private"`.** Set to private first, schedule the publish time, then YouTube auto-publishes.
- **Custom thumbnails require channel verification.** Verify via phone at https://www.youtube.com/verify. Without it, `thumbnails().set()` returns 403.
- **Resumable upload is mandatory for files >5MB.** Use `chunksize` for progress tracking and network resilience.
- **`client_secrets.json` must NOT be committed to git.** It contains OAuth credentials. Store in `.cex/brand/` or env vars.
- **Description max: 5,000 chars. Title max: 100 chars. Tags total: 500 chars.**
- **Scheduling timezone**: `publishAt` must be UTC ISO 8601. Convert from BRT (UTC-3) before sending.
- **Rate limiting**: burst of uploads in sequence may trigger 403 `quotaExceeded`. Space uploads 5+ seconds apart.
- **Made For Kids flag is legally binding.** If `selfDeclaredMadeForKids: true`, comments are disabled and ads are restricted (COPPA). Set `false` for general content.

## Docs
- Data API Reference: https://developers.google.com/youtube/v3/docs
- Upload guide: https://developers.google.com/youtube/v3/guides/uploading_a_video
- Python quickstart: https://developers.google.com/youtube/v3/quickstart/python

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_cf_publish_youtube]] | downstream | 0.33 |
| [[p01_kc_ayrshare_api]] | sibling | 0.21 |
| [[bld_tools_vc_credential]] | downstream | 0.20 |
| [[bld_examples_vc_credential]] | downstream | 0.18 |
| [[n04_output_cf_integration_kcs]] | related | 0.17 |
| [[p01_kc_supabase_storage]] | sibling | 0.17 |
| [[wf_kc_to_content]] | downstream | 0.16 |
| [[p01_kc_canva_connect_api]] | sibling | 0.16 |
