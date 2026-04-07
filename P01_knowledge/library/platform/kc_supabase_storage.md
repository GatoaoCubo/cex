---
id: p01_kc_supabase_storage
kind: knowledge_card
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
tldr: "Storage S3-compatible com buckets public/private, RLS policies, image transforms via imgproxy, resumable uploads (TUS), e CDN Cloudflare no Pro+"
when_to_use: "Quando configurar upload/download de arquivos e media em projetos Supabase"
keywords: [supabase-storage, buckets, imgproxy, tus-upload, cdn]
long_tails:
  - Como criar bucket privado com RLS no Supabase Storage
  - Resize de imagens on-the-fly com Supabase transforms
  - Upload resumable de arquivos grandes no Supabase
axioms:
  - SEMPRE defina max_file_size e allowed_mime_types por bucket
  - NUNCA crie bucket público para dados sensíveis
  - SEMPRE use resumable upload (TUS) para arquivos >6MB
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_auth, p01_kc_supabase_database]
density_score: 0.87
data_source: "https://supabase.com/docs/guides/storage"
---

# Supabase Storage — Buckets + Transforms

## Quick Reference
```yaml
topic: supabase_storage
scope: S3-compatible storage, RLS policies, image transforms, CDN
owner: n04_knowledge
criticality: high
service: storage-api (porta 5000)
```

## Limites por Tier
| Metrica | Free | Pro | Team |
|---------|------|-----|------|
| Storage total | 1 GB | 100 GB (USD 0.021/GB extra) | 100 GB+ |
| Upload max file | 50 MB | 5 GB | 5 GB |
| Image transforms | Incluso | Incluso | Incluso |
| CDN (Cloudflare) | Não | Sim | Sim |
| Bandwidth | 2 GB | 250 GB | 250 GB+ |

## Bucket Types
| Tipo | Acesso | Uso | URL Pattern |
|------|--------|-----|-------------|
| Public | Qualquer um (sem auth) | Imagens de produto, assets, avatares | `/storage/v1/object/public/bucket/file` |
| Private | Apenas com auth + RLS policy | Documentos, uploads de usuario | `/storage/v1/object/authenticated/bucket/file` |

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
-- Owner upload: user pode fazer upload na sua pasta
CREATE POLICY "user_upload" ON storage.objects
  FOR INSERT WITH CHECK (
    bucket_id = 'avatars' AND
    (storage.foldername(name))[1] = auth.uid()::text
  );

-- Owner read: user pode ler seus arquivos
CREATE POLICY "user_read" ON storage.objects
  FOR SELECT USING (
    bucket_id = 'avatars' AND
    (storage.foldername(name))[1] = auth.uid()::text
  );

-- Public read: qualquer um le (bucket publico)
CREATE POLICY "public_read" ON storage.objects
  FOR SELECT USING (bucket_id = 'public-assets');
```

## Folder Convention
```text
bucket/
  {user_id}/          ← RLS por owner
    avatars/
    documents/
  {org_id}/           ← RLS por org (multi-tenant)
    media/
    exports/
  public/             ← sem RLS, CDN cached
    logos/
    assets/
```

## Anti-Patterns
| Anti-Pattern | Risco | Fix |
|-------------|-------|-----|
| Bucket público para uploads de user | Arquivos acessiveis sem auth | Bucket private + RLS |
| Upload sem mime type check | User sobe .exe como .jpg | `allowed_mime_types: ['image/*']` |
| Sem max_file_size | User sobe arquivo de 5GB no free | Definir limite por bucket |
| Imagens sem transform | Serve original 4K pro mobile | Usar width/quality params |

## Golden Rules
- ORGANIZE arquivos por `{user_id}/` ou `{org_id}/` para RLS simples
- CONFIGURE transforms para servir webp em vez de PNG/JPEG original
- USE CDN (Pro+) para assets estáticos com alto tráfego
- LIMITE mime types por bucket — nunca aceitar `*/*`

## References
- Docs: https://supabase.com/docs/guides/storage
- Transforms: https://supabase.com/docs/guides/storage/serving/image-transformations
- TUS: https://supabase.com/docs/guides/storage/uploads/resumable-uploads
