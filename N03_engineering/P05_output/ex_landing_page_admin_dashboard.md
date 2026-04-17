---
id: ex_landing_page_admin_dashboard
kind: landing_page
pillar: P05
title: Admin Dashboard Landing Page
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_PRIMARY_COLOR
tags: [commerce, template, distillation, admin, dashboard, landing_page]
---

## Purpose

Admin hub page for the commerce platform — displays KPI summary cards, navigation links to all admin modules (Products, Shopify Sync, Integrations, CRM, Sales), and real-time sync status indicators.

## When to Use

- Serving as the entry point after admin login at `/admin`.
- Providing a high-level overview of platform health (sync status, product count, error alerts).
- Navigating to specialized admin modules without memorizing deep URLs.

## Page Structure

```
/admin (AdminDashboard.tsx)
  |
  +-- [Header] {{BRAND_NAME}} Admin — logo + nav + user menu
  |
  +-- [Stats Row] 4 KPI cards
  |     |-- Total Products (from Supabase)
  |     |-- Shopify Synced (shopify_id IS NOT NULL)
  |     |-- Bling Synced (bling_id IS NOT NULL)
  |     |-- Pending Sync (shopify_synced_at < updated_at)
  |
  +-- [Integration Status] Badge row
  |     |-- Shopify: connected | error | not_configured
  |     |-- Bling: connected | token_expiring | error
  |     |-- ML: connected | token_expiring | not_connected
  |
  +-- [Quick Actions] Button grid
  |     |-- "Sync All" -> POST /unified-sync (bidirectional)
  |     |-- "Reconcile Inventory" -> POST /inventory-reconcile (dry_run=true)
  |     |-- "Audit Catalog" -> POST /bling-audit (dry_run=true)
  |     |-- "Manage Webhooks" -> GET /webhook-manager?action=list
  |
  +-- [Navigation Cards] Grid (2x3)
        |-- Products (/admin/products)
        |-- Shopify Sync (/admin/shopify-sync)
        |-- Integrations (/admin/integracoes)
        |-- CRM (/admin/crm)
        |-- Sales Composer (/admin/vendas)
        |-- Orders (/admin/b2b-orders)
```

## KPI Data Queries

```typescript
// Stats loaded on page mount
const { data: stats } = await supabase.rpc('get_dashboard_stats');

// Or equivalent manual queries:
const { count: total } = await supabase.from('products').select('*', { count: 'exact', head: true });
const { count: shopifySynced } = await supabase.from('products')
  .select('*', { count: 'exact', head: true }).not('shopify_id', 'is', null);
const { count: blingSynced } = await supabase.from('products')
  .select('*', { count: 'exact', head: true }).not('bling_id', 'is', null);
const { count: pending } = await supabase.from('products')
  .select('*', { count: 'exact', head: true })
  .lt('shopify_synced_at', 'updated_at');
```

## Component Architecture

| Component | Type | Purpose |
|-----------|------|---------|
| `StatCard` | presentational | Single KPI with icon + count + label |
| `IntegrationBadge` | smart | Checks token expiry from DB; shows status color |
| `QuickAction` | smart | Button that calls edge function + shows result toast |
| `NavCard` | presentational | Large click target with icon + module name |
| `AdminLayout` | layout | Sidebar + header wrapper (shared by all /admin/* pages) |

## Styling Contract

| Token | Value |
|-------|-------|
| Primary color | `{{BRAND_PRIMARY_COLOR}}` |
| Background | `#FAFAFA` |
| Card shadow | `0 1px 3px rgba(0,0,0,0.1)` |
| Stat card width | 25% of container (4-column grid, responsive 2-column mobile) |
| Nav card size | 160x160px minimum |

## Auth Guard

This page requires admin authentication. Wrap the route with `ProtectedRoute`:

```tsx
<Route
  path="/admin"
  element={
    <ProtectedRoute adminOnly={true}>
      <AdminDashboard />
    </ProtectedRoute>
  }
/>
```

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_NAME}}` | App name shown in header + page title |
| `{{BRAND_PRIMARY_COLOR}}` | Primary button and active state color |

## Example Mock Render

```tsx
// Stat cards
<StatCard icon={Package} label="Total Products" count={312} />
<StatCard icon={CheckCircle} label="Shopify Synced" count={289} color="green" />
<StatCard icon={AlertTriangle} label="Pending Sync" count={15} color="amber" />

// Integration badges
<IntegrationBadge name="Shopify" status="connected" />
<IntegrationBadge name="Bling" status="token_expiring" warningAt="2026-04-20" />
```

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_component_map_admin_dashboard.md` | component_map | Component layout map |
| `ex_supabase_data_layer.md` | supabase_data_layer | Data source for KPIs |
| `ex_workflow_multi_marketplace_sync.md` | workflow | Quick Action target |
