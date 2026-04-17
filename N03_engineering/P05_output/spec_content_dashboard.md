---
id: p05_spec_content_dashboard
kind: interface
pillar: P06
version: "1.0.0"
created: "2026-04-10"
updated: "2026-04-10"
author: "n03_builder"
title: "Content Dashboard Specification -- GATO3 Admin Content Management"
domain: "content_pipeline"
quality: null
tags: [dashboard, content-pipeline, admin, next-js, supabase, gato3, interface, spec]
tldr: "Next.js admin page spec for managing 96 content items across 13 weeks. Calendar view, pipeline kanban, pillar mix analytics, quality gates, and publish tracking."
density_score: 0.92
---

## Purpose

Specifies the `/admin/content` page for the `gato-cubo-commerce` Next.js application.
This dashboard is the operational control center for the GATO3 content pipeline --
where the admin reviews, schedules, and tracks all 96 content items (70 Instagram +
26 blog posts) across the 13-week Q2 editorial calendar.

Designed for the semi-automated workflow (DP8): content is created by CEX nuclei,
seeded into Supabase by `seed_content_pipeline.py`, managed via this dashboard, and
published manually to platforms.

## Target Stack

| Layer | Technology |
|-------|-----------|
| Framework | Next.js (existing commerce app) |
| UI | shadcn/ui + Tailwind CSS |
| Data | Supabase (fuuguegkqnpzrrhwymgw) |
| Auth | Supabase Auth (authenticated role) |
| State | React Query (TanStack Query) for server state |
| Route | `/admin/content` (protected, authenticated only) |

## Data Sources

All data comes from 4 Supabase tables created by `20260410220003_content_pipeline_clean.sql`:

| Table | Purpose | Key columns |
|-------|---------|-------------|
| `content_items` | Core content | id, title, slug, content_type, category, status, body_markdown, caption, hashtags, scheduled_date, published_url |
| `content_schedule` | Per-platform scheduling | id, content_item_id, scheduled_date, scheduled_time, platform, status |
| `content_media` | Attached assets | id, content_item_id, media_type, storage_path, external_url |
| `content_sources` | Reference sources | id, title, url, source_type |

## Page Layout

```
+------------------------------------------------------------------+
| GATO3 Admin > Content Pipeline                    [Week 3 of 13] |
+------------------------------------------------------------------+
| [Calendar] [Pipeline] [Analytics] [Settings]                      |
+------------------------------------------------------------------+
|                                                                    |
|  (Active tab content renders here)                                 |
|                                                                    |
+------------------------------------------------------------------+
```

### Navigation Tabs

| Tab | Route | Purpose |
|-----|-------|---------|
| Calendar | `/admin/content` | Week-by-week content schedule |
| Pipeline | `/admin/content/pipeline` | Kanban board of content status |
| Analytics | `/admin/content/analytics` | Pillar mix, publishing velocity, quality |
| Settings | `/admin/content/settings` | Re-seed, export, sync options |

## Tab 1: Calendar View

### Layout

```
+------------------------------------------------------------------+
| < Week 1: Apr 15-20              [Today] [Prev] [Next]   Week > |
+------------------------------------------------------------------+
| Mon 14   | Tue 15      | Wed 16      | Thu 17     | Fri 18      |
|----------|-------------|-------------|------------|-------------- |
|          | [IG-FEED]   | [IG-REEL]   | [IG-FEED]  | [IG-REEL]   |
|          | Carrossel   | Meme 30s    | Single     | Meme 15s    |
|          | Educativo   | Meme/Humor  | Produto    | Meme/Humor  |
|          | "5 sinais   | "POV 3h     | "Donut     | "Gato vs    |
|          |  estresse"  |  da manha"  |  GATO3"    |  arranhador"|
|          |  07:00      |  12:00      |  10:00     |  12:00      |
|          | [DRAFT]     | [DRAFT]     | [DRAFT]    | [DRAFT]     |
|          |             |             |            |             |
|          | [BLOG]      |             | [BLOG]     |             |
|          | "Estresse   |             | "Donut     |             |
|          |  felino"    |             |  review"   |             |
|          |  10:00      |             |  10:00     |             |
|          | [DRAFT]     |             | [DRAFT]    |             |
+----------+-------------+-------------+------------+-------------|
| Sat 19   | Sun 20      |
|----------|-------------|
|          | [IG-STORY]  |
|          | Quiz        |
|          | Engagement  |
|          | "Por que    |
|          |  ronronam?" |
|          | [DRAFT]     |
+----------+-------------+
```

### Content Card Component

Each card in the calendar displays:

| Field | Source | Display |
|-------|--------|---------|
| Platform badge | content_type | Color-coded: IG-FEED (blue), IG-REEL (purple), IG-STORY (orange), BLOG (green) |
| Format | content_type | Carrossel, Reel, Single, Story, Blog |
| Category | category | Tag with pillar color |
| Title | title | Truncated to 2 lines |
| Time | content_schedule.scheduled_time | HH:MM format |
| Status | status | Badge: draft (gray), ready (yellow), scheduled (blue), published (green) |
| Media indicator | content_media join | Camera icon if media attached, empty circle if not |
| Product refs | product_refs | Small product tag(s) |

### Card Actions (on click/expand)

| Action | Effect | API call |
|--------|--------|----------|
| View details | Opens detail drawer | GET content_items?id=eq.{id} |
| Edit status | Status dropdown | PATCH content_items {status} |
| Reschedule | Date picker | PATCH content_schedule {scheduled_date, scheduled_time} |
| Copy caption | Copies caption + hashtags to clipboard | Client-side |
| Mark published | Sets published_at + URL input | PATCH content_items + content_schedule |
| Skip | Marks as skipped | PATCH content_schedule {status: 'skipped'} |

### Calendar Filters

| Filter | Options | Default |
|--------|---------|---------|
| Platform | All, Instagram, Blog | All |
| Category | All, Educativo, Meme/Humor, Produto, Seasonal | All |
| Status | All, Draft, Ready, Scheduled, Published | All |
| Week | 1-13 | Current week |

## Tab 2: Pipeline View (Kanban)

```
+-----------+-----------+-----------+-----------+-----------+
|  DRAFT    |  READY    | SCHEDULED | PUBLISHED | ARCHIVED  |
|  (43)     |  (12)     |  (7)      |  (34)     |  (0)      |
+-----------+-----------+-----------+-----------+-----------+
| [Card]    | [Card]    | [Card]    | [Card]    |           |
| [Card]    | [Card]    | [Card]    | [Card]    |           |
| [Card]    |           | [Card]    | [Card]    |           |
| ...       |           |           | ...       |           |
+-----------+-----------+-----------+-----------+-----------+
```

- Drag-and-drop to change status (draft -> ready -> scheduled)
- Published column shows published_url as link
- Cards are the same component as Calendar view (compact variant)
- Filter bar: same filters as Calendar + search by title

### Pipeline Queries

```sql
-- Draft items needing review
SELECT * FROM content_items WHERE status = 'draft'
  ORDER BY scheduled_date ASC;

-- This week's scheduled items
SELECT ci.*, cs.scheduled_time, cs.platform
FROM content_items ci
JOIN content_schedule cs ON cs.content_item_id = ci.id
WHERE cs.scheduled_date BETWEEN current_date AND current_date + 7
  AND cs.status = 'pending'
ORDER BY cs.scheduled_date, cs.scheduled_time;

-- Publishing velocity (items published per week)
SELECT date_trunc('week', published_at) AS week,
       count(*) AS published_count
FROM content_items WHERE status = 'published'
GROUP BY 1 ORDER BY 1;
```

## Tab 3: Analytics View

### Summary Cards (top row)

| Card | Query | Display |
|------|-------|---------|
| Total items | COUNT(*) FROM content_items | Number + progress bar (vs 96 target) |
| Published | COUNT(*) WHERE status='published' | Number + % of total |
| This week | COUNT(*) WHERE scheduled_date in current week | Number + daily breakdown |
| Avg quality | Not in DB yet (future: quality_score column) | Placeholder for rubric integration |

### Pillar Mix Chart

Pie/donut chart showing category distribution:

| Category | Target % | Color |
|----------|----------|-------|
| Educativo | 40% | #2563EB (blue) |
| Meme/Humor | 30% | #7C3AED (purple) |
| Produto | 20% | #059669 (green) |
| Seasonal | 10% | #D97706 (amber) |

```sql
SELECT category, count(*) AS total,
       count(*) FILTER (WHERE status = 'published') AS published
FROM content_items
GROUP BY category;
```

Display: dual ring -- outer = total, inner = published. Shows deviation from target.

### Content Type Distribution

Bar chart:

```sql
SELECT content_type, count(*) AS total
FROM content_items
GROUP BY content_type
ORDER BY total DESC;
```

### Publishing Timeline

Line chart showing cumulative published items over 13-week horizon:

```sql
SELECT cs.scheduled_date, count(*) AS scheduled,
       count(*) FILTER (WHERE cs.status = 'published') AS published
FROM content_schedule cs
GROUP BY cs.scheduled_date
ORDER BY cs.scheduled_date;
```

X-axis: dates (Apr 15 - Jul 15), Y-axis: cumulative count.
Two lines: planned (total scheduled) vs actual (published).

### Product Integration Heatmap

Table showing which products appear most frequently in content:

```sql
SELECT unnest(product_refs) AS product, count(*) AS mentions,
       count(*) FILTER (WHERE status = 'published') AS published_mentions
FROM content_items
WHERE product_refs IS NOT NULL
GROUP BY 1
ORDER BY mentions DESC;
```

## Tab 4: Settings

| Setting | Action | Implementation |
|---------|--------|----------------|
| Re-seed | Run seed script against current markdown files | API route calls seed_content_pipeline.py |
| Export calendar | Download current schedule as CSV | Client-side CSV from Supabase query |
| Sync check | Compare markdown files vs DB items | Diff slug lists, show additions/removals |
| Clear and re-seed | Drop all items and re-insert | Confirmation modal, then clear + seed |

## Detail Drawer

When a content card is clicked, a side drawer opens:

```
+--------------------------------------------------+
| X  [Blog Post] [Educativo]          [DRAFT v]    |
+--------------------------------------------------+
| Estresse Felino: 5 Sinais de Alerta              |
| Slug: estresse-felino-sinais                      |
| Scheduled: Apr 15, 2026 at 10:00                  |
| Week: 1 | Blog #1                                 |
+--------------------------------------------------+
| SEO                                               |
| Title: Estresse Felino: 5 Sinais de Alerta...    |
| Description: Aprenda a identificar os 5 sinais...|
| Keywords: estresse felino, sinais de estresse...  |
+--------------------------------------------------+
| Products: arranhador, brinquedos-interativos,     |
|           cama-suspensa-janela                    |
+--------------------------------------------------+
| Content Preview                                   |
| (Rendered markdown body -- first 500 chars)       |
| [View full content]                               |
+--------------------------------------------------+
| Media (0 attached)                                |
| [+ Upload image] [+ Add external URL]            |
+--------------------------------------------------+
| Actions                                           |
| [Copy caption + hashtags]  [Open in new tab]      |
| [Mark as published]  URL: [____________] [Save]   |
+--------------------------------------------------+
| Schedule History                                  |
| Apr 15 10:00 blog   pending                      |
+--------------------------------------------------+
```

For Instagram posts, the drawer shows:
- Caption (full text with line breaks preserved)
- Hashtags (as tags, with copy button)
- Alt text
- Visual brief (collapsible, for reference during media creation)

## Component Hierarchy

```
/admin/content/
  ContentDashboard (layout + tabs)
    CalendarView
      WeekNavigator
      DayColumn (x7)
        ContentCard (compact)
    PipelineView
      StatusColumn (x5)
        ContentCard (compact, draggable)
    AnalyticsView
      SummaryCards (x4)
      PillarMixChart (donut)
      ContentTypeChart (bar)
      PublishingTimeline (line)
      ProductHeatmap (table)
    SettingsView
      SeedAction
      ExportAction
      SyncCheckAction
    ContentDetailDrawer
      StatusSelector
      SeoSection
      ProductTags
      ContentPreview
      MediaSection
      ActionBar
      ScheduleHistory
```

## API Routes (Next.js)

| Route | Method | Purpose |
|-------|--------|---------|
| `/api/content/items` | GET | List items with filters (status, category, type, week) |
| `/api/content/items/[id]` | GET | Single item with schedule + media joins |
| `/api/content/items/[id]` | PATCH | Update status, published_url, published_at |
| `/api/content/schedule` | GET | List schedule entries (date range filter) |
| `/api/content/schedule/[id]` | PATCH | Reschedule, skip, mark published |
| `/api/content/media` | POST | Upload media (Supabase Storage) |
| `/api/content/analytics` | GET | Aggregated stats (pillar mix, velocity, types) |
| `/api/content/seed` | POST | Trigger re-seed (protected, admin only) |

All routes use Supabase client with service_role for server-side operations.
Client-side uses authenticated user's session for RLS-compliant reads.

## State Management

```
ContentDashboardProvider
  activeTab: 'calendar' | 'pipeline' | 'analytics' | 'settings'
  selectedWeek: number (1-13)
  filters: { platform, category, status }
  selectedItem: string | null (content_item id for drawer)
  
  React Query keys:
    ['content-items', filters]
    ['content-item', id]
    ['content-schedule', weekRange]
    ['content-analytics']
```

## Responsive Behavior

| Breakpoint | Calendar | Pipeline | Analytics |
|------------|----------|----------|-----------|
| Desktop (>1280px) | 7-column week grid | 5-column kanban | Charts + table side by side |
| Tablet (768-1280px) | 5-column (Mon-Fri), scroll for Sat-Sun | 3 columns visible, scroll | Charts stacked |
| Mobile (<768px) | Day list (vertical scroll) | Single column, tabs for status | Cards + simplified charts |

## Visual Design

Follows GATO3 brand guidelines adapted for admin UI:

| Element | Style |
|---------|-------|
| Background | #FAFAFA (light gray, not pure white) |
| Cards | White, 1px border #E5E5E5, rounded-lg |
| Category: Educativo | bg-blue-50 text-blue-700 |
| Category: Meme/Humor | bg-purple-50 text-purple-700 |
| Category: Produto | bg-green-50 text-green-700 |
| Category: Seasonal | bg-amber-50 text-amber-700 |
| Status: Draft | bg-gray-100 text-gray-600 |
| Status: Ready | bg-yellow-100 text-yellow-700 |
| Status: Scheduled | bg-blue-100 text-blue-700 |
| Status: Published | bg-green-100 text-green-700 |
| Typography | Inter (UI), JetBrains Mono (slugs, dates) |
| Accent | #000000 (buttons, links -- PB brand) |

## Implementation Priority

| Phase | Components | Effort |
|-------|-----------|--------|
| P0 (MVP) | CalendarView + ContentCard + DetailDrawer + StatusSelector | 2-3 days |
| P1 | PipelineView (kanban) + drag-and-drop status changes | 1-2 days |
| P2 | AnalyticsView (summary cards + pillar mix chart) | 1-2 days |
| P3 | Settings (seed trigger, export) + media upload | 1 day |
| P4 | Full analytics (timeline, heatmap) + mobile responsive | 2 days |

**Total estimate**: 7-10 days for full implementation.

## References

1. `20260410220003_content_pipeline_clean.sql` -- Supabase schema
2. `N03_engineering/tools/seed_content_pipeline.py` -- database seeder
3. `N03_engineering/orchestration/wf_content_pipeline_ops.md` -- operational workflow
4. `N04_knowledge/compiled/taxonomy_content_gato3.yaml` -- content taxonomy
5. `N04_knowledge/compiled/rubric_content_quality.yaml` -- quality rubric
6. `N04_knowledge/compiled/editorial_calendar_template.yaml` -- 13-week calendar
7. shadcn/ui documentation (components library)
8. Supabase JS client v2 documentation
