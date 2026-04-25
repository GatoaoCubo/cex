---
id: p01_kc_supabase_storage
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase Storage — S3-Compatible Buckets + Transforms + CDN"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [supabase, storage, s3, buckets, cdn, imgproxy, tus, platform]
tldr: "S3-compatible storage with public/private buckets, RLS policies, image transforms via imgproxy, resumable uploads (TUS), and Cloudflare CDN on Pro+"
when_to_use: "When configuring file and media upload/download in Supabase projects"
keywords: [supabase-storage, buckets, imgproxy, tus-upload, cdn]
long_tails:
  - How to create a private bucket with RLS in Supabase Storage
  - On-the-fly image resizing with Supabase transforms
  - Resumable upload of large files in Supabase
axioms:
  - ALWAYS define max_file_size and allowed_mime_types per bucket
  - NEVER create a public bucket for sensitive data
  - ALWAYS use resumable upload (TUS) for files >6MB
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_auth, p01_kc_supabase_database]
density_score: 0.87
data_source: "https://supabase.com/docs/guides/storage"
related:
  - bld_instruction_supabase_data_layer
  - bld_examples_supabase_data_layer
  - bld_knowledge_card_supabase_data_layer
  - p04_tool_supabase_data_layer
  - bld_manifest_supabase_data_layer
  - p01_kc_supabase_auth
  - p12_wf_supabase_setup
  - p04_tpl_supabase_data_layer
  - bld_schema_supabase_data_layer
  - p01_kc_supabase_multi_tenant
---

# Supabase Storage — Buckets + Transforms

## Quick Reference
```yaml
topic: supabase_storage
scope: S3-compatible storage, RLS policies, image transforms, CDN
owner: n04_knowledge
criticality: high
service: storage-api (port 5000)
```

## Limits per Tier
| Metric | Free | Pro | Team |
|--------|------|-----|------|
| Storage total | 1 GB | 100 GB (USD 0.021/GB extra) | 100 GB+ |
| Upload max file | 50 MB | 5 GB | 5 GB |
| Image transforms | Included | Included | Included |
| CDN (Cloudflare) | No | Yes | Yes |
| Bandwidth | 2 GB | 250 GB | 250 GB+ |

## Bucket Types
| Type | Access | Use | URL Pattern |
|------|--------|-----|-------------|
| Public | Anyone (no auth) | Product images, assets, avatars | `/storage/v1/object/public/bucket/file` |
| Private | Auth + RLS policy only | Documents, user uploads | `/storage/v1/object/authenticated/bucket/file` |

## Upload Patterns
```javascript
// Standard upload (< 6MB)
const { data, error } = await supabase.storage
  .from('avatars')
  .upload('user-123/photo.jpg', file, {
    contentType: 'image/jpeg',
    upsert: true
  })

// Resumable upload (> 6MB, TUS protocol)
const { data, error } = await supabase.storage
  .from('videos')
  .upload('user-123/video.mp4', file, {
    uploadType: 'resumable',
    chunkSize: 6 * 1024 * 1024  // 6MB chunks
  })
```

## Image Transforms (imgproxy)
```text
/storage/v1/render/image/public/bucket/photo.jpg
  ?width=300&height=200&resize=cover&quality=80&format=webp
```

| Param | Valores | Default |
|-------|---------|---------|
| width | 1-2560 px | original |
| height | 1-2560 px | original |
| resize | cover, contain, fill | cover |
| quality | 20-100 | 80 |
| format | origin, webp, avif | origin |

## Storage RLS Policies
```sql
-- Owner upload: user can upload to their folder
CREATE POLICY "user_upload" ON storage.objects
  FOR INSERT WITH CHECK (
    bucket_id = 'avatars' AND
    (storage.foldername(name))[1] = auth.uid()::text
  );

-- Owner read: user can read their files
CREATE POLICY "user_read" ON storage.objects
  FOR SELECT USING (
    bucket_id = 'avatars' AND
    (storage.foldername(name))[1] = auth.uid()::text
  );

-- Public read: anyone can read (public bucket)
CREATE POLICY "public_read" ON storage.objects
  FOR SELECT USING (bucket_id = 'public-assets');
```

## Folder Convention
```text
bucket/
  {user_id}/          ← RLS by owner
    avatars/
    documents/
  {org_id}/           ← RLS by org (multi-tenant)
    media/
    exports/
  public/             ← no RLS, CDN cached
    logos/
    assets/
```

## Anti-Patterns
| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Public bucket for user uploads | Files accessible without auth | Private bucket + RLS |
| Upload without mime type check | User uploads .exe as .jpg | `allowed_mime_types: ['image/*']` |
| No max_file_size | User uploads 5GB file on free | Set limit per bucket |
| Images without transform | Serves original 4K to mobile | Use width/quality params |

## Golden Rules
- ORGANIZE files by `{user_id}/` or `{org_id}/` for simple RLS
- CONFIGURE transforms to serve webp instead of original PNG/JPEG
- USE CDN (Pro+) for high-traffic static assets
- LIMIT mime types per bucket — never accept `*/*`

## References
- Docs: https://supabase.com/docs/guides/storage
- Transforms: https://supabase.com/docs/guides/storage/serving/image-transformations
- TUS: https://supabase.com/docs/guides/storage/uploads/resumable-uploads

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_supabase_data_layer]] | downstream | 0.33 |
| [[bld_examples_supabase_data_layer]] | related | 0.32 |
| [[bld_knowledge_card_supabase_data_layer]] | sibling | 0.28 |
| [[p04_tool_supabase_data_layer]] | downstream | 0.27 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.27 |
| [[p01_kc_supabase_auth]] | sibling | 0.26 |
| [[p12_wf_supabase_setup]] | downstream | 0.25 |
| [[p04_tpl_supabase_data_layer]] | downstream | 0.25 |
| [[bld_schema_supabase_data_layer]] | downstream | 0.23 |
| [[p01_kc_supabase_multi_tenant]] | sibling | 0.23 |
