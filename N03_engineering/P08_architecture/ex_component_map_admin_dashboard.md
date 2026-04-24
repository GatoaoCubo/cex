---
id: ex_component_map_admin_dashboard
kind: component_map
8f: F4_reason
pillar: P08
title: Admin Dashboard Component Map
version: 0.1.0
quality: 8.3
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_PRIMARY_COLOR
tags: [commerce, template, distillation, component_map, admin, dashboard]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_schema_model_registry
  - n06_schema_brand_config
  - bld_schema_component_map
  - bld_schema_landing_page
  - tpl_crm_admin_spec
  - bld_schema_agent_computer_interface
  - bld_schema_experiment_tracker
  - bld_schema_training_method
  - bld_schema_tagline
  - bld_output_template_rbac_policy
---

## Purpose

React component architecture map for the admin dashboard page (`/admin`) — defines component boundaries, prop contracts, data flows, and reuse relationships across all admin modules.

## When to Use

- Planning a new admin module that reuses shared components.
- Debugging rendering issues by tracing component boundaries.
- Onboarding a frontend developer to the admin UI architecture.
- Spec'ing a UI design handoff for the admin hub.

## Component Tree

```
<AdminLayout>                          # shared: sidebar + header
  <AdminDashboard>                     # route: /admin
    <DashboardHeader>                  # title + refresh button
    <StatsGrid>                        # 4-column KPI row
      <StatCard x4>                    # count + label + icon
    <IntegrationStatusRow>             # badge row
      <IntegrationBadge x3>            # shopify | bling | meli
    <QuickActionsPanel>                # 4 action buttons
      <QuickActionButton x4>
    <NavCardGrid>                      # 6 module entry points
      <NavCard x6>
```

## Component Contracts

### `AdminLayout`

```tsx
interface AdminLayoutProps {
  children: React.ReactNode;
}
// Renders: sidebar (fixed, 240px) + main content area
// Context: AuthContext (reads user for nav items)
// Route: wraps all /admin/* routes
```

### `StatCard`

```tsx
interface StatCardProps {
  icon:    LucideIcon;
  label:   string;
  count:   number;
  color?:  'default' | 'green' | 'amber' | 'red';
  loading?: boolean;
}
```

### `IntegrationBadge`

```tsx
interface IntegrationBadgeProps {
  name:        'Shopify' | 'Bling' | 'Mercado Livre';
  status:      'connected' | 'token_expiring' | 'error' | 'not_configured';
  expiresAt?:  string;  // ISO 8601 — shown when status == token_expiring
}
// Data source: meli_tokens + bling_tokens tables
// Refresh: on page mount + every 5 min (polling)
```

### `QuickActionButton`

```tsx
interface QuickActionButtonProps {
  label:    string;
  icon:     LucideIcon;
  endpoint: string;       // Edge function URL
  method:   'GET' | 'POST';
  body?:    object;
  onSuccess?: (result: unknown) => void;
}
// Shows loading spinner during call; toast on success/error
```

### `NavCard`

```tsx
interface NavCardProps {
  label: string;
  description: string;
  icon:  LucideIcon;
  href:  string;
  badge?: string;  // e.g., "15 pending" for sync status
}
```

## Data Flows

```
Page mount
  |
  v
[useEffect] parallel:
  |-- fetchDashboardStats() -> StatsGrid (count queries)
  |-- fetchTokenStatuses()  -> IntegrationStatusRow (token expiry check)
  |-- fetchPendingCount()   -> NavCard "Products" badge
  |
  v
User clicks "Sync All"
  |
  v
QuickActionButton:
  |-- POST /unified-sync { mode: "bidirectional" }
  |-- loading=true -> spinner
  |-- on response -> toast ("Synced 23 products, 0 errors")
  |-- refresh StatsGrid
```

## Routing

| Route | Component | Guard |
|-------|-----------|-------|
| `/admin` | `AdminDashboard` | `ProtectedRoute adminOnly` |
| `/admin/products` | `ProductsAdmin` | `ProtectedRoute adminOnly` |
| `/admin/shopify-sync` | `ShopifySync` | `ProtectedRoute adminOnly` |
| `/admin/integracoes` | `Integracoes` | `ProtectedRoute adminOnly` |
| `/admin/crm` | `CRM` | `ProtectedRoute adminOnly` |
| `/admin/vendas` | `Vendas` | `ProtectedRoute adminOnly` |

## State Management

| State | Location | Persistence |
|-------|----------|-------------|
| Auth session | `AuthContext` + Supabase auth | sessionStorage |
| Dashboard stats | Local `useState` | None (refetched on mount) |
| Integration status | Local `useState` | None (refetched on mount) |
| Toast notifications | Global `ToastContext` | Session-scoped |

## Theming

```tsx
// Primary brand color applied to:
// - Active nav item background
// - QuickActionButton hover
// - StatCard accent bar
const theme = {
  primary: '{{BRAND_PRIMARY_COLOR}}',  // e.g., #C71585
  sidebar_bg: '#1E1E2E',
  header_bg: '#FFFFFF',
};
```

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_NAME}}` | Page title + sidebar header |
| `{{BRAND_PRIMARY_COLOR}}` | Active state + accent color |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_registry]] | upstream | 0.21 |
| [[n06_schema_brand_config]] | upstream | 0.19 |
| [[bld_schema_component_map]] | related | 0.19 |
| [[bld_schema_landing_page]] | upstream | 0.19 |
| [[tpl_crm_admin_spec]] | downstream | 0.19 |
| [[bld_schema_agent_computer_interface]] | upstream | 0.18 |
| [[bld_schema_experiment_tracker]] | upstream | 0.18 |
| [[bld_schema_training_method]] | upstream | 0.17 |
| [[bld_schema_tagline]] | upstream | 0.17 |
| [[bld_output_template_rbac_policy]] | upstream | 0.17 |
