---
id: content_pipeline_schema_n05
kind: knowledge_card
pillar: P04
title: "Content Pipeline Supabase Schema"
version: 1.0.0
quality: null
tags: [supabase, schema, content-pipeline, gato3, n05]
mission: CONTENT_PIPELINE
created: 2026-04-10
---

# Content Pipeline -- Supabase Schema Reference

## Overview

4 tables, 16 indexes, 1 trigger, 22 RLS policies for the GATO3 content pipeline.
Stores 90 Instagram posts + 26 blog posts + media assets for 3-month horizon.

| Component | Location |
|-----------|----------|
| Migration | `supabase/migrations/20260410220000_content_pipeline.sql` |
| Edge Function (CRUD) | `supabase/functions/content-crud/index.ts` |
| Edge Function (Schedule) | `supabase/functions/content-schedule/index.ts` |
| Target repo | `gato-cubo-commerce` |
| Supabase project | `fuuguegkqnpzrrhwymgw` |

## Tables

### content_items

Core content table. One row per piece of content.

| Column | Type | Constraints | Notes |
|--------|------|-------------|-------|
| id | uuid | PK, auto | |
| title | text | NOT NULL | |
| slug | text | UNIQUE | Auto-generated from title |
| content_type | text | NOT NULL, CHECK | blog_post, instagram_feed, instagram_reel, instagram_carrossel, instagram_story |
| category | text | NOT NULL, CHECK | educativo, meme_humor, produto, seasonal |
| status | text | NOT NULL, default 'draft', CHECK | draft, ready, scheduled, published, archived |
| body_markdown | text | | Blog post full content |
| caption | text | | Instagram caption |
| alt_text | text | | Accessibility |
| hashtags | text[] | | Instagram hashtags |
| target_platform | text | NOT NULL, CHECK | blog, instagram, both |
| content_pillar | text | | behavior, health, product, humor |
| product_refs | text[] | | Linked product slugs |
| source_kc_id | text | | N01 knowledge card ref |
| scheduled_date | date | | |
| scheduled_time | time | | |
| published_at | timestamptz | | |
| published_url | text | | |
| seo_title | text | | Blog only |
| seo_description | text | | Blog only |
| seo_keywords | text[] | | Blog only |
| created_at | timestamptz | default now() | |
| updated_at | timestamptz | default now(), trigger | Auto-updated |
| created_by | text | default 'system' | |

### content_media

Media assets linked to content items (1:many).

| Column | Type | Constraints | Notes |
|--------|------|-------------|-------|
| id | uuid | PK, auto | |
| content_item_id | uuid | FK -> content_items, CASCADE | |
| media_type | text | NOT NULL, CHECK | image, video, gif, audio |
| storage_type | text | NOT NULL, CHECK | supabase, external_url |
| storage_path | text | | Bucket path for Supabase Storage |
| external_url | text | | For external media |
| source_attribution | text | | Credit for third-party content |
| license_type | text | | own, creative_commons, fair_use, reference_only |
| file_size_bytes | bigint | | |
| mime_type | text | | |
| width | int | | |
| height | int | | |
| duration_seconds | int | | Video/audio only |
| alt_text | text | | |
| sort_order | int | default 0 | For carousel ordering |
| created_at | timestamptz | default now() | |

### content_schedule

Calendar view -- which content goes when on which platform.

| Column | Type | Constraints | Notes |
|--------|------|-------------|-------|
| id | uuid | PK, auto | |
| content_item_id | uuid | FK -> content_items, CASCADE | |
| scheduled_date | date | NOT NULL | |
| scheduled_time | time | default '10:00' | |
| platform | text | NOT NULL | |
| status | text | NOT NULL, default 'pending', CHECK | pending, published, skipped, rescheduled |
| published_at | timestamptz | | |
| notes | text | | |
| created_at | timestamptz | default now() | |
| | | UNIQUE(content_item_id, platform, scheduled_date) | |

### content_sources

Master registry of research sources from N01.

| Column | Type | Constraints | Notes |
|--------|------|-------------|-------|
| id | uuid | PK, auto | |
| title | text | NOT NULL | |
| url | text | | |
| source_type | text | CHECK | scientific_paper, blog, video, social_media, book, expert, meme_source |
| domain | text | | behavior, health, humor, seasonal, product |
| reliability | text | CHECK | high, medium, low |
| language | text | default 'en' | |
| notes | text | | |
| last_checked | date | | |
| created_at | timestamptz | default now() | |

## RLS Policy Summary

| Table | Public (anon) | Authenticated | Service Role |
|-------|---------------|---------------|--------------|
| content_items | SELECT where published | Full CRUD | Full access |
| content_media | SELECT where parent published | Full CRUD | Full access |
| content_schedule | SELECT where published | Full CRUD | Full access |
| content_sources | SELECT all | Full CRUD | Full access |

## Edge Functions API

### content-crud

All endpoints are POST with JSON body `{ action: "...", ... }`.

| Action | Required Fields | Description |
|--------|----------------|-------------|
| `create` | data.title, data.content_type, data.category, data.target_platform | Create content item + optional media[] |
| `list` | | List with filters (status, content_type, platform, category, date_from, date_to, search) + pagination (limit, offset) |
| `get` | id | Single item with all media |
| `update` | id, data | Update content item fields |
| `delete` | id | Soft delete (sets status=archived) |
| `add_media` | content_item_id, media[] | Add media to existing content item |
| `remove_media` | media_id | Remove single media asset |
| `stats` | | Counts by status, type, platform, category |
| `add_source` | data.title | Add research source |
| `list_sources` | | List sources, optional domain filter |

### content-schedule

| Action | Required Fields | Description |
|--------|----------------|-------------|
| `schedule` | content_item_id, date, platform | Schedule content item, updates item status |
| `calendar` | month (YYYY-MM) | Month view grouped by date, optional platform filter |
| `reschedule` | schedule_id, new_date | Move scheduled item, optional new_time and notes |
| `upcoming` | | Next N days (default 7), optional platform filter |
| `mark_published` | schedule_id | Mark as published, updates content_item too |
| `skip` | schedule_id | Skip scheduled item, optional notes |
| `calendar_fill` | month (YYYY-MM) | Coverage % per platform for the month |

## Storage Bucket

Bucket `content-assets` (manual creation via Dashboard):

```
content-assets/
  images/blog/          -- hero + inline images
  images/instagram/     -- feed images
  videos/               -- reels, stories
  templates/            -- Canva/design templates
  references/           -- mood boards, screenshots
```

Settings: private bucket, signed URLs for public access, 50MB max, image/video/audio MIME types.

## Deployment

1. Apply migration: `npx supabase db push` or paste SQL in Dashboard > SQL Editor
2. Deploy functions: `npx supabase functions deploy content-crud` and `content-schedule`
3. Create storage bucket manually via Dashboard
4. Regenerate types: `npx supabase gen types typescript --project-id fuuguegkqnpzrrhwymgw > src/types/database.ts`
