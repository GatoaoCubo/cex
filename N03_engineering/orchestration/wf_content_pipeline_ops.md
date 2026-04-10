---
id: p12_wf_content_pipeline_ops
kind: workflow
pillar: P12
version: "1.0.0"
created: "2026-04-10"
updated: "2026-04-10"
author: "n03_builder"
title: "Content Pipeline Operations -- Editorial Calendar to Published Content"
steps_count: 8
execution: mixed
agent_groups: [n02_marketing, n03_engineering, n04_knowledge, n05_operations]
timeout: 604800
retry_policy: per_step
depends_on: [brand_config_yaml, content_pipeline_clean_sql, editorial_calendar_template]
signals: [complete, error]
domain: "content_pipeline_ops"
quality: null
tags: [workflow, content-pipeline, operations, semi-auto, supabase, gato3]
tldr: "8-step operational workflow: parse editorial content -> seed Supabase -> review via dashboard -> manual publish. Semi-automated per DP8."
density_score: 0.91
---

## Purpose

Operationalizes the GATO3 content pipeline from editorial calendar artifacts (produced
by N02 + N04) into a managed Supabase-backed workflow. This workflow covers the
repeatable weekly cycle: content exists as markdown in the CEX repo, gets seeded into
the `content_items` database, passes through quality review, and is manually published
to Instagram and the blog.

This is the **operations layer** -- distinct from `wf_content_factory_v1.md` (the
production pipeline that creates content from briefs). This workflow assumes content
already exists and focuses on scheduling, quality gating, and publishing.

## Architecture

```
N02_marketing/content_pipeline/     Supabase                  Platforms
  blog/*.md  ----+                 +------------------+
  instagram/*.md-+---> seed.py --->| content_items    |-----> Blog (manual)
                                   | content_schedule |-----> Instagram (manual)
                                   | content_media    |       Stories (manual)
                                   +------------------+
                                          |
                                   Dashboard (read)
                                   /admin/content
```

## Decision Context

| Decision | Value | Source |
|----------|-------|--------|
| DP1 Platforms | Instagram + Blog | decision_manifest.yaml |
| DP2 Frequency | 5x/week IG + 2x/week blog | decision_manifest.yaml |
| DP8 Automation | Semi-auto (DB + scheduler, publish manual) | decision_manifest.yaml |
| Storage | Supabase (fuuguegkqnpzrrhwymgw) | decision_manifest.yaml |
| Horizon | 2026-04-15 to 2026-07-15 (90 days, 13 weeks) | decision_manifest.yaml |

## Steps

### Step 1: Content Production [N02 + N04, async]
- **Agent**: N02 (marketing copy), N04 (taxonomy, calendar, rubric)
- **Action**: Produce editorial content as markdown files in `N02_marketing/content_pipeline/`
- **Input**: Editorial calendar template, brand config, taxonomy, product xref
- **Output**: 26 blog posts in `blog/` + 13 week files in `instagram/` (~91 posts)
- **Signal**: content_production_complete
- **Depends on**: Brand bootstrapped, editorial calendar exists
- **Frequency**: Once per quarter (bulk), weekly for adjustments
- **Quality gate**: Each piece scores >= 4.0/5.0 on rubric_content_quality before commit

### Step 2: Seed Database [N03 tool]
- **Agent**: seed_content_pipeline.py (N03_engineering/tools/)
- **Action**: Parse all markdown content and insert into Supabase tables
- **Input**: Blog .md files (YAML frontmatter + body) + IG week .md files (structured posts)
- **Output**: Rows in `content_items` + `content_schedule` tables
- **Signal**: seed_complete
- **Depends on**: Step 1, Supabase migration applied (20260410220003)
- **Frequency**: Once per quarter (initial seed), on-demand for updates
- **Commands**:
  - Preview: `python N03_engineering/tools/seed_content_pipeline.py --dry-run`
  - Seed: `python N03_engineering/tools/seed_content_pipeline.py --clear`
  - Count: `python N03_engineering/tools/seed_content_pipeline.py --count`

### Step 3: Dashboard Review [N05, admin UI]
- **Agent**: Admin user via content dashboard (`/admin/content` in commerce app)
- **Action**: Review seeded content in calendar view. Verify scheduling, check pillar mix, flag issues.
- **Input**: content_items + content_schedule data via Supabase queries
- **Output**: Status updates (draft -> ready), reschedule actions, skip decisions
- **Signal**: review_batch_complete
- **Depends on**: Step 2
- **Frequency**: Weekly (every Saturday per calendar template)
- **Dashboard views**:
  - Calendar: week grid with content cards by day
  - Pipeline: kanban (draft -> ready -> scheduled -> published)
  - Mix: pie chart of pillar distribution (target: 40/30/20/10)
  - Quality: per-item rubric scores with dimension breakdown

### Step 4: Media Preparation [Manual]
- **Agent**: Admin user (Canva, image editing, video production)
- **Action**: Create visual assets matching the visual brief in each IG post
- **Input**: Visual brief field from content_items, brand guidelines (PB minimalista)
- **Output**: Images/videos uploaded to Supabase Storage (`content-assets` bucket) or linked as external URLs in `content_media` table
- **Signal**: media_attached (content_item status -> 'ready')
- **Depends on**: Step 3
- **Frequency**: Weekly batch (create week's assets in one session)
- **Spec references**:
  - Instagram Feed: 1080x1080px (1:1) or 1080x1350px (4:5)
  - Instagram Reel: 1080x1920px (9:16), 15-90s
  - Blog hero: 1200x630px (OG) + 800x450px (in-post)

### Step 5: Schedule Confirmation [Dashboard]
- **Agent**: Admin user via dashboard
- **Action**: Confirm scheduled dates/times for the upcoming week. Move items from 'ready' to 'scheduled'.
- **Input**: content_schedule entries for the week
- **Output**: Status updates: ready -> scheduled
- **Signal**: week_scheduled
- **Depends on**: Step 4
- **Frequency**: Weekly (every Saturday/Sunday)
- **Scheduling rules**:
  - Optimal IG posting: 07:00-09:00 BRT (morning), 12:00-13:00 BRT (lunch)
  - Blog posting: 10:00 BRT (Tuesday + Thursday)
  - Story posting: 18:00-20:00 BRT (evening engagement)

### Step 6: Publish [Manual]
- **Agent**: Admin user (Instagram app, blog CMS)
- **Action**: Copy caption + hashtags from dashboard, attach media, publish on platform
- **Input**: Scheduled content with all fields populated
- **Output**: Published URL recorded in content_items.published_url + content_schedule.published_at
- **Signal**: item_published
- **Depends on**: Step 5
- **Frequency**: Daily (per schedule)
- **Publishing checklist**:
  1. Open dashboard -> filter by today's date + 'scheduled' status
  2. For each item: copy caption, attach image/video, paste hashtags in first comment
  3. Publish on platform
  4. Copy published URL back to dashboard
  5. Mark as 'published' in dashboard

### Step 7: Analytics Collection [Weekly]
- **Agent**: Admin user + Instagram Insights + blog analytics
- **Action**: Collect 7-day performance data for published content. Record in notes field.
- **Input**: Instagram Insights (reach, saves, shares, comments), blog analytics (views, time on page, bounce rate)
- **Output**: Performance notes per content item
- **Signal**: analytics_collected
- **Depends on**: Step 6 (7 days post-publish)
- **Frequency**: Weekly (every Monday review of previous week)
- **Key metrics**:
  - IG: reach, impressions, saves, shares, comments, profile visits
  - Blog: pageviews, avg read time, bounce rate, internal link clicks
  - Product: click-through to product pages (UTM tracking)

### Step 8: Iterate and Optimize [Weekly]
- **Agent**: N02 (adjust content) + Admin (adjust schedule)
- **Action**: Review top 3 / bottom 3 performers. Adjust upcoming content topics, formats, and scheduling based on data.
- **Input**: Analytics from Step 7, pillar mix actuals vs targets
- **Output**: Updated content items (topic swaps), adjusted schedule, taxonomy feedback
- **Signal**: iteration_complete
- **Depends on**: Step 7
- **Frequency**: Weekly
- **Optimization rules**:
  - If pillar % deviates > 5% from target: adjust next week's schedule
  - If content type consistently underperforms: swap format in upcoming weeks
  - If product integration avg > 2.0: reduce product mentions
  - If product integration avg < 1.0: add subtle product hooks
  - Feed top performers into N04 taxonomy updates

## Wave Plan

| Wave | Steps | Cadence | Who | Duration |
|------|-------|---------|-----|----------|
| 1: Produce | 1 (Content Production) | Quarterly | N02, N04 | 2-4 hours |
| 2: Seed | 2 (Seed Database) | Quarterly | Script | 2 minutes |
| 3: Weekly Ops | 3-6 (Review, Media, Schedule, Publish) | Weekly | Admin | 3-5 hours/week |
| 4: Learn | 7-8 (Analytics, Iterate) | Weekly | Admin + N02 | 1 hour/week |

**Total weekly operational load**: 4-6 hours per week for 5 IG posts + 2 blog posts.

## Dependencies

| Dependency | Status | Location |
|------------|--------|----------|
| Brand config | Required | `.cex/brand/brand_config.yaml` |
| Supabase migration | Required | `gato-cubo-commerce/supabase/migrations/20260410220003_content_pipeline_clean.sql` |
| Editorial calendar | Required | `N04_knowledge/compiled/editorial_calendar_template.yaml` |
| Content taxonomy | Required | `N04_knowledge/compiled/taxonomy_content_gato3.yaml` |
| Quality rubric | Required | `N04_knowledge/compiled/rubric_content_quality.yaml` |
| Product xref | Required | `N04_knowledge/compiled/xref_product_content.yaml` |
| Seed script | Required | `N03_engineering/tools/seed_content_pipeline.py` |
| Dashboard | Planned | `spec_content_dashboard.md` (commerce app `/admin/content`) |
| Blog posts (26) | Produced | `N02_marketing/content_pipeline/blog/` |
| IG weeks (13) | Produced | `N02_marketing/content_pipeline/instagram/` |

## Signals

| Signal | When | Producer | Consumer |
|--------|------|----------|----------|
| content_production_complete | All 96 pieces written | N02 + N04 | N03 (seed) |
| seed_complete | All items in Supabase | seed script | Admin (dashboard) |
| review_batch_complete | Weekly review done | Admin | Admin (media prep) |
| week_scheduled | Week's content confirmed | Admin | Admin (daily publish) |
| item_published | Single item published | Admin | Analytics |
| analytics_collected | Weekly data recorded | Admin | N02 (iteration) |
| iteration_complete | Adjustments made | N02 + Admin | Next week cycle |

## Error Recovery

| Error | Action | Owner |
|-------|--------|-------|
| Seed script fails (bad YAML) | Fix markdown frontmatter, re-run seed | N03 |
| Supabase connection error | Check service key, retry | N05 |
| Duplicate slug on insert | Script uses --clear for fresh seed | N03 |
| Media not ready by schedule | Reschedule item (+1 day) via dashboard | Admin |
| Content scores below 4.0 | Return to N02 for revision before scheduling | Admin |
| Pillar mix off target | Swap upcoming items from backlog | Admin + N02 |
| Platform API changes | Update publishing checklist | N05 |

## References

1. `N03_engineering/tools/seed_content_pipeline.py` -- database seeder
2. `N03_engineering/output/spec_content_dashboard.md` -- dashboard specification
3. `N03_engineering/workflows/wf_content_factory_v1.md` -- content production workflow (upstream)
4. `N04_knowledge/compiled/editorial_calendar_template.yaml` -- 13-week calendar
5. `N04_knowledge/compiled/taxonomy_content_gato3.yaml` -- content taxonomy
6. `N04_knowledge/compiled/rubric_content_quality.yaml` -- quality scoring rubric
7. `20260410220003_content_pipeline_clean.sql` -- Supabase schema
