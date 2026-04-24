---
id: ex-component-map-admin-dashboard
kind: component_map
8f: F4_reason
pillar: P08
title: Admin Dashboard Component Map
version: 0.1.0
quality: 8.9
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_PRIMARY_COLOR
tags: [commerce, template, distillation, admin, component_map]
density_score: 1.0
related:
  - bld_architecture_kind
  - bld_instruction_kind
  - bld_tools_landing_page
  - landing-page-builder
  - p01_kc_cex_as_digital_asset
  - bld_memory_landing_page
  - bld_schema_kind
  - bld_collaboration_component_map
---

# Admin Dashboard Component Map

## Purpose
Decomposes the admin dashboard landing page into reusable React components and documents their contracts (props, state, events). Lets multiple developers build different tiles in parallel without clashing.

## When to use
- You have the landing page spec (`ex_landing_page_admin_dashboard.md`) and need to break it into buildable units.
- A new tile is being added -- this doc dictates which component to reuse vs build new.
- Frontend performance audit -- identify which tiles fetch too aggressively.

## Brand variables used
- `{{BRAND_NAME}}` -- header component prop.
- `{{BRAND_PRIMARY_COLOR}}` -- passed to theming provider, not hard-coded per component.

## Component tree

```
<AdminDashboardPage>
  +-- <AdminLayout>
  |   +-- <AdminSidebar items=... />
  |   +-- <AdminTopBar brand logo user />
  +-- <HealthStrip>
  |   +-- <HealthTile kind="orders_today" />
  |   +-- <HealthTile kind="sync_status" />
  |   +-- <HealthTile kind="stock_anomalies" />
  |   +-- <HealthTile kind="webhook_queue" />
  +-- <NavGrid items=adminNavItems />
  |   +-- <NavCard * 7 />
  +-- <ActivityFeed limit />
  |   +-- <ActivityRow * N />
  +-- <AdminFooter supportEmail />
```

## Component contracts

### `<HealthTile kind>`
- Props: `{ kind: "orders_today" | "sync_status" | "stock_anomalies" | "webhook_queue" }`
- Internal: `useQuery(["dashboard", kind], fetchTileData, { refetchInterval: 60000 })`.
- States: `loading`, `ok`, `warn`, `error` -- color by threshold defined per kind.
- Emits: none (read-only).

### `<NavCard>`
- Props: `{ label: string, to: string, icon: ReactNode, badgeCount?: number }`.
- Renders a `<Link>` (react-router) with icon + label + optional badge.
- No data fetching; pure presentational.

### `<ActivityFeed>`
- Props: `{ limit: number }`.
- Fetches last N rows from `sync_runs` order by `started_at desc`.
- Polls every 60s; flashes new rows for 2s.

### `<AdminSidebar>`
- Props: `{ items: NavItem[] }`.
- Sticky on desktop, drawer on mobile.
- Active route highlighted with `{{BRAND_PRIMARY_COLOR}}` via CSS var.

### `<AdminTopBar>`
- Props: `{ brand, logo, user: UserCtx }`.
- User menu includes role badge; admin-only items gated by `user.role === "admin"`.

## State ownership
- Global: auth context, theme, query client.
- Per-tile: react-query caches keyed by tile kind.
- Local: drawer open/close, user menu open/close.

## Data flow
```
Supabase v_admin_dashboard --> react-query --> <HealthTile>
Supabase sync_runs          --> react-query --> <ActivityFeed>
Route table                 --> static       --> <NavGrid>
```

## Reuse notes
- `<NavCard>` is reused in `/admin/integracoes` with different icons; keep props permissive.
- `<HealthTile>` is specific to the dashboard -- do NOT generalize until a second use-case emerges.
- `<AdminLayout>` is shared across ALL admin pages; any layout change cascades -- guard with visual regression test.

## Related artifacts
- `ex_landing_page_admin_dashboard.md`
- `ex_supabase_data_layer.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | related | 0.17 |
| [[bld_instruction_kind]] | upstream | 0.17 |
| [[bld_tools_landing_page]] | upstream | 0.16 |
| [[landing-page-builder]] | upstream | 0.16 |
| [[p01_kc_cex_as_digital_asset]] | upstream | 0.16 |
| [[bld_memory_landing_page]] | downstream | 0.15 |
| [[bld_schema_kind]] | upstream | 0.15 |
| [[bld_collaboration_component_map]] | downstream | 0.15 |
