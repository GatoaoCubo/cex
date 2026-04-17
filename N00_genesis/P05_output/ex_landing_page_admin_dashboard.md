---
id: ex-landing-page-admin-dashboard
kind: landing_page
pillar: P05
title: Admin Dashboard Landing Page
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_PRIMARY_COLOR
  - BRAND_LOGO_URL
  - BRAND_SUPPORT_EMAIL
tags: [commerce, template, distillation, admin, landing_page]
---

# Admin Dashboard Landing Page

## Purpose
The entry point an operator sees after authenticating as `admin` role. Surfaces the key health metrics (orders today, sync status per channel, stock anomalies) and navigation cards to every admin module (Products, Shopify Sync, Integracoes, CRM, B2B Orders, Vendas, Content Schedule).

## When to use
- Brand has multi-channel sync and a human operator needs one glance to know "is anything on fire?".
- Replacing individual admin pages with a unified hub reduces context switching.
- Onboarding new ops staff -- this page is the first screen they see.

## When NOT to use
- Brand's ops is a single person who lives in the Bling or Shopify admin directly.
- Catalog is <50 SKUs -- a full dashboard is overkill.

## Brand variables used
- `{{BRAND_NAME}}` -- header text, window title.
- `{{BRAND_PRIMARY_COLOR}}` -- accent on CTAs + active nav.
- `{{BRAND_LOGO_URL}}` -- top-left brand mark.
- `{{BRAND_SUPPORT_EMAIL}}` -- footer mailto for operator help.

## Page sections (top to bottom)

1. **Top bar**
   - Brand logo + `{{BRAND_NAME}} / Admin` label.
   - User menu (profile, role, sign out).
2. **Health strip** (4 tiles, `grid-cols-4`):
   - Orders today (count + delta vs yesterday).
   - Sync status (Shopify / Bling / ML) -- colored dot per channel.
   - Stock anomalies (rows with `inventory.quantity < 0` OR reconcile mismatch > 5 units).
   - Webhook queue (inbound backlog size).
3. **Navigation cards** (responsive grid, minimum 3 cols on desktop):
   | Card | Link | Icon |
   |------|------|------|
   | Products | /admin/products | box |
   | Shopify Sync | /admin/shopify-sync | sync |
   | Integracoes | /admin/integracoes | plug |
   | CRM | /admin/crm | users |
   | B2B Orders | /admin/b2b-orders | clipboard |
   | Vendas (AI) | /admin/vendas | sparkles |
   | Content Schedule | /admin/content-schedule | calendar |
4. **Recent activity feed** -- last 10 sync runs with outcome + runtime.
5. **Footer** -- version + `mailto:{{BRAND_SUPPORT_EMAIL}}`.

## Data sources
| Tile | Query |
|------|-------|
| Orders today | `select count(*) from orders where created_at >= current_date` |
| Sync status | last row per channel in `sync_runs` table |
| Stock anomalies | `select count(*) from inventory where quantity < 0 union ...` |
| Webhook queue | `select count(*) from webhook_inbox_shopify where consumed=false` |

Use materialized view `v_admin_dashboard` refreshed every 60s; raw queries on each tile would hammer the DB.

## Example scaffold (Tailwind + shadcn/ui)
```tsx
<AdminLayout>
  <Header brand="{{BRAND_NAME}}" logo="{{BRAND_LOGO_URL}}" />
  <HealthStrip accent="{{BRAND_PRIMARY_COLOR}}" />
  <NavGrid />
  <ActivityFeed limit={10} />
  <Footer supportEmail="{{BRAND_SUPPORT_EMAIL}}" />
</AdminLayout>
```

## Accessibility
- Each card is a `<button>` or `<a>` with a visible label; no icon-only navigation.
- Color dots in health strip include a text label (`ok`, `stale`, `down`) for color-blind operators.
- Keyboard: Tab order follows visual top-to-bottom, left-to-right.

## Related artifacts
- `ex_component_map_admin_dashboard.md` -- component decomposition.
- `ex_supabase_data_layer.md` -- auth context + client.
