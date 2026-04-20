---
id: lr_gato3_content_approval_pipeline_2026_04_20
kind: learning_record
pillar: P11
nucleus: N07
domain: gato3_content_ops
title: "GATO3 content library -> Ayshare pipeline wiring + readiness report"
version: 1.0.0
quality: null
created: "2026-04-20"
updated: "2026-04-20"
status: ready_for_deploy
tags: [gato3, content_library, ayshare, supabase, approval_gate, readiness_report]
---

# GATO3 Content Approval -> Ayshare Publishing Pipeline

## Mission Context

User directive: "yeah i want all videos rendered and everything to reflect in frontend wired so i can aprove for further post automation" (2026-04-20), followed by `/mission continue autonomo com fallback decision`.

Autonomous fallback decision taken: **Option A** -- extend `ayshare-publish` edge function with library-aware actions. Rejected Option B (sync-trigger hack) for being load-bearing duct tape.

## What Landed

### Supabase Storage (bucket: content_library, public)
```
w01_p01/9x16/reels.mp4                         (2.1 MB, real reel composition)
w02_p05/4x5/01_janela_hero.png                 (1.4 MB)
w02_p05/4x5/02_observacao.png                  (1.4 MB)
w02_p05/4x5/03_cama_suspensa.png               (1.4 MB)
w02_p05/4x5/04_ambiente.png                    (1.4 MB)
w02_p05/2x3/pinterest.png                      (copy of scene 01)
w02_p05/1x1/threads.png                        (copy of scene 01)
w02_p05/9x16/reels.mp4                         (1.29 MB, 18.5s slideshow, xfade 0.5s)
```

### content_library rows populated (9 of 224 = 4.0%)

| post_id   | channel    | asset_type | format | storage_url      | approved |
|-----------|-----------|-----------|--------|------------------|----------|
| w01_p01   | ig_reels  | video     | 9x16   | reels.mp4        | false    |
| w01_p01   | ig_stories| video     | 9x16   | reels.mp4        | false    |
| w01_p01   | tiktok    | video     | 9x16   | reels.mp4        | false    |
| w02_p05   | ig_reels  | video     | 9x16   | reels.mp4        | false    |
| w02_p05   | ig_stories| video     | 9x16   | reels.mp4        | false    |
| w02_p05   | tiktok    | video     | 9x16   | reels.mp4        | false    |
| w02_p05   | pinterest | image     | 2x3    | pinterest.png    | false    |
| w02_p05   | threads   | image     | 1x1    | threads.png      | false    |
| w02_p05   | ig_feed   | carousel  | 4x5    | 01_janela_hero   | false    |

Remaining 215 rows: `storage_url IS NULL` -- blocked on source material.

### Edge function changes (committed 266cef3)

File: `supabase/functions/ayshare-publish/index.ts` (+386 / -2 lines)

New actions wired into the POST handler's switch:

| Action                  | Purpose                                                           |
|------------------------|-------------------------------------------------------------------|
| `publish_library_due`  | Publish all approved rows where storage_url set and no ayshare_job_id |
| `library_dry_run`      | Preview batch payloads without calling Ayshare                    |
| `library_publish_one`  | Publish single row by UUID (needs `row_id` in body)               |
| `library_status`       | Recent publishes + pending-ready queue + failed list              |

Approval gate enforced in `fetchLibraryDue()`:
```sql
WHERE approved = true
  AND publish_status IN ('pending','scheduled')
  AND storage_url IS NOT NULL
  AND ayshare_job_id IS NULL
  AND (scheduled_at IS NULL OR scheduled_at <= NOW())
ORDER BY scheduled_at ASC NULLS FIRST
LIMIT 50;
```

Platform mapping (`CHANNEL_TO_AYSHARE_PLATFORM`):
- ig_feed, ig_reels, ig_stories -> `instagram`
- fb -> `facebook` | tiktok -> `tiktok` | linkedin -> `linkedin`
- pinterest -> `pinterest` | threads -> `threads` | x -> `twitter`
- blog, email -> **not routable** (fail with explanatory error)

Carousel support: `buildLibraryMediaUrls` reads `metadata.carousel_urls[]` when `asset_type = 'carousel'`; falls back to single `storage_url` otherwise.

Idempotency: `ayshare_job_id NOT NULL` = skip (already posted).

## Next Step for User (deploy blocker)

Deploy command:
```bash
npx supabase functions deploy ayshare-publish --project-ref fuuguegkqnpzrrhwymgw
```

Requires: `SUPABASE_ACCESS_TOKEN` env var set to the user's personal Supabase access token (distinct from `service_role_key`). This token is NOT in the CEX env and should NOT be -- it's a user-account credential. Get it from <https://supabase.com/dashboard/account/tokens>.

After deploy, smoke-test order:
```bash
# 1. Confirm the 4 new actions are live
curl -X POST https://fuuguegkqnpzrrhwymgw.supabase.co/functions/v1/ayshare-publish \
  -H "Authorization: Bearer $SUPABASE_ANON_KEY" \
  -H "Content-Type: application/json" \
  -d '{"action":"library_status"}'

# 2. Preview what would publish (zero rows because nothing approved yet)
curl ... -d '{"action":"library_dry_run"}'

# 3. Flip approval on ONE row in /admin/conteudo UI
# 4. library_dry_run again -- should now show 1 payload

# 5. When satisfied, real publish:
curl ... -d '{"action":"publish_library_due"}'
```

## What Is Still Blocked

### 31 / 32 video posts cannot be rendered

Root cause: `_concat_list.txt` files reference body scenes at `%TEMP%/gato3_core_reels_{post}_{nn}.mp4` that Windows Temp cleanup already purged. Only `_hook.mp4` (0.8s) and `_endcard.mp4` (2.0s) remain -- insufficient for honest reels.

Workaround used on w02_p05: rendered slideshow from scene PNGs via ffmpeg xfade. This only works for posts that have scene PNG assets in `.cex/cache/`. Of 32 video posts, only w02_p05 had them.

**Actual fix required**: regenerate the body scenes. Either:
1. Re-run the scene pipeline (N02 `generate_scenes` action), OR
2. Produce fresh reel compositions per post (requires creative input: shot list, narration)

Recommend: add to next N02 sprint. Not an orchestration problem.

### 215 / 224 content_library rows still unlinked

Breakdown of the gap:
- 180+ rows are images (ig_feed static, blog covers, email headers) that need per-post visual assets generated and uploaded
- ~30 rows are video formats where source is missing per above
- Small remainder are copy-only channels (blog text, x, threads) missing the final render step

Not a blocker for the 9 populated rows -- the approval flow will work for those today.

## Architectural Notes

### Why Option A (not B)

Option B considered: Postgres trigger on `content_library.approved = true` that copies the row into `content_schedule` so the existing publish pipeline picks it up. Rejected because:
1. Two tables become truth for the same concept (dual-write drift)
2. Column mismatch: `content_library.caption_text` vs `content_schedule.caption`; carousel metadata has no home in schedule
3. content_schedule was meant to deprecate -- wiring a trigger into it reverses direction
4. The comment in migration `20260414180000_content_library.sql` explicitly flagged "future: switch source from content_schedule to content_library". Option A honors that intent.

### Legacy `publish_due` still works

Did not remove any existing action. `content_schedule` path remains functional for rows already there. This means:
- **/admin/conteudo** approvals -> `publish_library_due` (new)
- **Legacy content_schedule rows** -> `publish_due` (unchanged)

Both can run simultaneously. Cron can be scheduled against either action; recommendation is to switch cron to `publish_library_due` once confidence is established and content_schedule is fully drained.

## Quality Posture

- Code syntax: validated (balanced braces, 0 depth at EOF, 1158 lines)
- Logic: mirrors existing `publishBatch` pattern; idempotency + rate-limit handling + auth-failure short-circuit all preserved
- Deploy test: **NOT run** (blocked on user access token)
- Dry-run verification on live function: **deferred** (post-deploy user action)

## Commits Landed This Session

```
gato-cubo-commerce 266cef3  feat(ayshare): wire content_library -> Ayshare publish pipeline
gato-cubo-commerce (prior)  storage uploads + DB row population via REST (ad-hoc, no commit)
```

## Properties

| Property       | Value                                              |
|----------------|----------------------------------------------------|
| Mission        | GATO3 content approval -> publish wiring           |
| Nucleus        | N07 (orchestrated direct edits in commerce repo)   |
| Kind           | learning_record                                    |
| Pillar         | P11 feedback                                       |
| Status         | ready_for_deploy (awaiting SUPABASE_ACCESS_TOKEN)  |
| Date           | 2026-04-20                                         |
