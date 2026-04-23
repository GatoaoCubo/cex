---
id: p05_output_dashboard_ui
kind: output_validator
pillar: P05
title: "Dashboard UI Template — Sidebar + Main Content"
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend
domain: frontend
quality: 9.1
tags: [output, template, dashboard, tailwind, responsive]
tldr: "Production dashboard layout — collapsible sidebar, stat cards, data table, responsive drawer."
density_score: 0.90
related:
  - p10_dtc_design_token_contract
  - p06_schema_tailwind_palette
  - p05_output_style_guide
  - p09_lpt_landing_page_template
  - landing_page_petshop_crm
  - p05_output_visual_report
  - spec_n02_part2
  - p10_hos_html_output_visual_frontend
  - p05_output_social_card
  - bld_examples_landing_page
---

# Dashboard UI Template

## Purpose
Copy-paste ready dashboard layout for internal tools, admin panels, and analytics views.
Uses CODEXA design tokens. Responsive: sidebar → drawer on mobile.

---

## Template Structure

```
┌─────────────────────────────────────────────────┐
│ Top Bar: [☰] Search...          [🔔] [Avatar]  │
├────────┬────────────────────────────────────────┤
│        │ Stat Cards (4-grid)                    │
│  Side  │ ┌──────┬──────┬──────┬──────┐         │
│  bar   │ │ Stat │ Stat │ Stat │ Stat │         │
│        │ └──────┴──────┴──────┴──────┘         │
│  Nav   │                                        │
│  Items │ Data Table (sortable)                  │
│        │ ┌────────────────────────────┐         │
│  [Dash]│ │ Name │ Status │ Date │ ▼  │         │
│  [Data]│ │──────│────────│──────│────│         │
│  [Users│ │ ...  │ ...    │ ...  │    │         │
│  [Setgs│ └────────────────────────────┘         │
└────────┴────────────────────────────────────────┘
```

## Complete HTML Example

```html
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard — CODEXA</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --codexa-surface-900: hsl(240 10% 5%);
      --codexa-surface-800: hsl(240 8% 12%);
      --codexa-surface-700: hsl(240 6% 20%);
      --codexa-accent: #50C878;
      --codexa-text-primary: hsl(0 0% 95%);
      --codexa-text-secondary: hsl(0 0% 70%);
      --codexa-border: hsl(240 5% 25%);
    }
    body { font-family: 'Inter', sans-serif; }
  </style>
</head>
<body class="bg-[var(--codexa-surface-900)] text-[var(--codexa-text-primary)]">

  <!-- SIDEBAR (hidden mobile, visible lg+) -->
  <aside id="sidebar" class="fixed inset-y-0 left-0 z-30 w-64 bg-[var(--codexa-surface-800)]
         border-r border-[var(--codexa-border)] transform -translate-x-full lg:translate-x-0
         transition-transform duration-200">
    <!-- Logo -->
    <div class="h-16 flex items-center px-6 border-b border-[var(--codexa-border)]">
      <span class="text-xl font-bold" style="color: var(--codexa-accent)">CODEXA</span>
    </div>
    <!-- Nav -->
    <nav class="p-4 space-y-1">
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg bg-[var(--codexa-surface-700)]
         text-[var(--codexa-text-primary)]">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3"/>
        </svg>
        Dashboard
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-[var(--codexa-text-secondary)]
         hover:bg-[var(--codexa-surface-700)] transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10"/>
        </svg>
        Analytics
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-[var(--codexa-text-secondary)]
         hover:bg-[var(--codexa-surface-700)] transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197"/>
        </svg>
        Users
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-[var(--codexa-text-secondary)]
         hover:bg-[var(--codexa-surface-700)] transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35"/>
        </svg>
        Settings
      </a>
    </nav>
  </aside>

  <!-- MAIN CONTENT -->
  <div class="lg:ml-64 min-h-screen">
    <!-- Top Bar -->
    <header class="h-16 border-b border-[var(--codexa-border)] flex items-center justify-between px-6">
      <div class="flex items-center gap-4">
        <button onclick="document.getElementById('sidebar').classList.toggle('-translate-x-full')"
                class="lg:hidden p-2 rounded-lg hover:bg-[var(--codexa-surface-700)]">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
        </button>
        <div class="relative">
          <input type="search" placeholder="Search..."
                 class="w-64 px-4 py-2 rounded-lg bg-[var(--codexa-surface-700)] border border-[var(--codexa-border)]
                        text-sm focus:outline-none focus:ring-2 focus:ring-[var(--codexa-accent)]">
        </div>
      </div>
      <div class="flex items-center gap-4">
        <button class="p-2 rounded-lg hover:bg-[var(--codexa-surface-700)] relative">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
          </svg>
          <span class="absolute -top-1 -right-1 w-4 h-4 rounded-full text-xs flex items-center justify-center"
                style="background: var(--codexa-accent); color: #000">3</span>
        </button>
        <div class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold"
             style="background: var(--codexa-accent); color: #000">U</div>
      </div>
    </header>

    <!-- Page Content -->
    <main class="p-6">
      <!-- Stat Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4 mb-8">
        <div class="p-6 rounded-xl bg-[var(--codexa-surface-800)] border border-[var(--codexa-border)]">
          <p class="text-sm text-[var(--codexa-text-secondary)]">Total Revenue</p>
          <p class="text-2xl font-bold mt-1">R$ 45.231</p>
          <p class="text-sm mt-2" style="color: var(--codexa-accent)">+20.1% vs last month</p>
        </div>
        <div class="p-6 rounded-xl bg-[var(--codexa-surface-800)] border border-[var(--codexa-border)]">
          <p class="text-sm text-[var(--codexa-text-secondary)]">Active Users</p>
          <p class="text-2xl font-bold mt-1">2,350</p>
          <p class="text-sm mt-2" style="color: var(--codexa-accent)">+180 this week</p>
        </div>
        <div class="p-6 rounded-xl bg-[var(--codexa-surface-800)] border border-[var(--codexa-border)]">
          <p class="text-sm text-[var(--codexa-text-secondary)]">API Calls</p>
          <p class="text-2xl font-bold mt-1">1.2M</p>
          <p class="text-sm mt-2 text-amber-400">p95 latency: 342ms</p>
        </div>
        <div class="p-6 rounded-xl bg-[var(--codexa-surface-800)] border border-[var(--codexa-border)]">
          <p class="text-sm text-[var(--codexa-text-secondary)]">Uptime</p>
          <p class="text-2xl font-bold mt-1">99.97%</p>
          <p class="text-sm mt-2" style="color: var(--codexa-accent)">Last 30 days</p>
        </div>
      </div>

      <!-- Data Table -->
      <div class="rounded-xl bg-[var(--codexa-surface-800)] border border-[var(--codexa-border)] overflow-hidden">
        <div class="p-4 border-b border-[var(--codexa-border)]">
          <h2 class="text-lg font-semibold">Recent Activity</h2>
        </div>
        <table class="w-full">
          <thead>
            <tr class="border-b border-[var(--codexa-border)] text-left text-sm text-[var(--codexa-text-secondary)]">
              <th class="px-4 py-3 font-medium">User</th>
              <th class="px-4 py-3 font-medium">Action</th>
              <th class="px-4 py-3 font-medium">Status</th>
              <th class="px-4 py-3 font-medium">Date</th>
            </tr>
          </thead>
          <tbody class="text-sm">
            <tr class="border-b border-[var(--codexa-border)] hover:bg-[var(--codexa-surface-700)] transition-colors">
              <td class="px-4 py-3">maria@codexa.com.br</td>
              <td class="px-4 py-3">Pipeline execution</td>
              <td class="px-4 py-3"><span class="px-2 py-1 rounded-full text-xs bg-green-500/20 text-green-400">Success</span></td>
              <td class="px-4 py-3 text-[var(--codexa-text-secondary)]">2 min ago</td>
            </tr>
            <tr class="border-b border-[var(--codexa-border)] hover:bg-[var(--codexa-surface-700)] transition-colors">
              <td class="px-4 py-3">joao@empresa.com</td>
              <td class="px-4 py-3">Credit purchase</td>
              <td class="px-4 py-3"><span class="px-2 py-1 rounded-full text-xs bg-blue-500/20 text-blue-400">Processing</span></td>
              <td class="px-4 py-3 text-[var(--codexa-text-secondary)]">15 min ago</td>
            </tr>
            <tr class="hover:bg-[var(--codexa-surface-700)] transition-colors">
              <td class="px-4 py-3">ana@startup.io</td>
              <td class="px-4 py-3">API key generated</td>
              <td class="px-4 py-3"><span class="px-2 py-1 rounded-full text-xs bg-amber-500/20 text-amber-400">Pending</span></td>
              <td class="px-4 py-3 text-[var(--codexa-text-secondary)]">1 hour ago</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  </div>

</body>
</html>
```

## Responsive Behavior

| Breakpoint | Sidebar | Grid | Table |
|------------|---------|------|-------|
| base (mobile) | hidden, hamburger toggle | 1 column | horizontal scroll |
| sm (640px) | hidden, hamburger toggle | 2 columns | horizontal scroll |
| lg (1024px) | fixed visible | 3 columns | full width |
| xl (1280px) | fixed visible | 4 columns | full width |

## Variants
- **Analytics Dashboard**: chart-heavy, Recharts placeholders, time-range selector
- **Admin Panel**: user management table, role badges, action buttons
- **E-commerce**: order list, revenue chart, product grid

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_dtc_design_token_contract]] | downstream | 0.61 |
| [[p06_schema_tailwind_palette]] | downstream | 0.56 |
| [[p05_output_style_guide]] | sibling | 0.54 |
| [[p09_lpt_landing_page_template]] | sibling | 0.44 |
| [[landing_page_petshop_crm]] | related | 0.41 |
| [[p05_output_visual_report]] | sibling | 0.36 |
| [[spec_n02_part2]] | downstream | 0.31 |
| [[p10_hos_html_output_visual_frontend]] | downstream | 0.29 |
| [[p05_output_social_card]] | sibling | 0.29 |
| [[bld_examples_landing_page]] | upstream | 0.26 |
