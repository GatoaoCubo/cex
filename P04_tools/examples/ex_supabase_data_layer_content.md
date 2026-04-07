---
id: p04_ex_supabase_data_layer_content
kind: example
pillar: P04
title: "Example — Supabase Data Layer for Content Platform"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [example, supabase, data-layer, content, platform, config]
tldr: "Content platform config: posts, comments, media, feeds, moderation, busca semantica de conteudo, real-time comments e likes"
density_score: 0.89
---

# Content Platform — Supabase Data Layer

## Vertical Profile
| Aspect | Value |
|--------|-------|
| Vertical | content |
| Tier | pro |
| Key tables | posts, comments, media, feeds, moderation_queue |
| Extensions | pgvector (content search), pg_cron (feed refresh), pg_trgm (fuzzy search) |
| Storage | content-media (public CDN), user-uploads (private) |
| Realtime | live comments, like counts, feed updates |
| Vectors | Content semantic search + recommendations |

## Config
```yaml
identidade:
  vertical: content
  regiao: us-east-1
  tier: pro

database:
  schemas: [public, moderation]
  extensions:
    obrigatorias: [pgcrypto, pg_graphql]
    opcionais: [pgvector, pg_cron, pg_trgm]
  tables:
    - name: posts
      columns: [id UUID PK, author_id UUID FK, org_id UUID FK, title TEXT, body TEXT, status TEXT DEFAULT 'draft', published_at TIMESTAMPTZ, embedding VECTOR(1536), like_count INT DEFAULT 0, comment_count INT DEFAULT 0]
      rls: public_read_author_write
      indexes: [author_id, org_id, status, published_at, "embedding HNSW vector_cosine_ops"]
    - name: comments
      columns: [id UUID PK, post_id UUID FK, author_id UUID FK, body TEXT, parent_id UUID FK SELF, created_at TIMESTAMPTZ]
      rls: public_read_author_write
      indexes: [post_id, author_id, parent_id]
    - name: media
      columns: [id UUID PK, post_id UUID FK, author_id UUID FK, storage_path TEXT, mime_type TEXT, size_bytes BIGINT]
      rls: author_owner
    - name: feeds
      columns: [id UUID PK, user_id UUID FK, post_id UUID FK, score FLOAT, created_at TIMESTAMPTZ]
      rls: owner
      indexes: [user_id, score, created_at]
    - name: moderation_queue
      schema: moderation
      columns: [id UUID PK, content_type TEXT, content_id UUID, reason TEXT, status TEXT DEFAULT 'pending', moderator_id UUID]
      rls: moderator_only

auth:
  providers: [email, google, apple, github]
  mfa: false
  custom_claims: [org_id, role]

rls:
  multi_tenant_column: org_id
  patterns:
    - nome: public_read_author_write
      policy: "true FOR SELECT WHERE status='published'; author_id = auth.uid() FOR INSERT/UPDATE/DELETE"
      tabelas: [posts, comments]
    - nome: author_owner
      policy: "author_id = auth.uid()"
      tabelas: [media]
    - nome: moderator_only
      policy: "(auth.jwt()->'app_metadata'->>'role') IN ('admin','moderator')"
      tabelas: [moderation_queue]

storage:
  buckets:
    - nome: content-media
      publico: true
      max_file_size: 52428800
      allowed_mime_types: [image/jpeg, image/png, image/webp, image/gif, video/mp4]
      transform: true
    - nome: user-uploads
      publico: false
      max_file_size: 10485760
      allowed_mime_types: [image/jpeg, image/png]

realtime:
  habilitado: true
  postgres_changes:
    - tabela: comments
      eventos: [INSERT]
    - tabela: posts
      eventos: [UPDATE]
      filter: "status=eq.published"

vectors:
  habilitado: true
  embedding_model: text-embedding-3-small
  dimensions: 1536
  distance_function: cosine
  search_function: match_posts

edge_functions:
  functions:
    - nome: refresh-feeds
      trigger: cron
      schedule: "*/15 * * * *"
    - nome: moderate-content
      trigger: webhook
      secrets: [OPENAI_KEY]
    - nome: process-media
      trigger: http
      secrets: [CDN_KEY]
  deploy_method: cli

budget:
  alertas:
    - metrica: storage
      threshold: 75
      acao: email
    - metrica: bandwidth
      threshold: 90
      acao: slack
```
