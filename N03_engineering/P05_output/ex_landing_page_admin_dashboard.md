---
id: ex_landing_page_admin_dashboard
kind: landing_page
pillar: P05
title: "Admin Dashboard SaaS - Unified Commerce Operations Hub"
version: 1.1.0
created: "2026-04-17"
updated: "2026-04-22"
author: landing-page-builder
quality: 8.6
tags: [landing-page, admin, dashboard, saas, commerce, html-tailwind, example]
tldr: "Production-ready landing page for a SaaS admin dashboard that unifies Shopify, Bling, and Mercado Livre operations."
domain: "saas-admin-dashboard"
stack: html-tailwind
sections_count: 12
responsive: true
dark_mode: true
a11y: AA
seo:
  title: "Admin Dashboard - Unified Commerce Operations Hub"
  description: "One hub to sync products, track orders, and manage integrations across Shopify, Bling, and Mercado Livre."
  og_image: "https://example.com/og-admin-dashboard.jpg"
  canonical: "https://example.com/admin"
  json_ld_type: SoftwareApplication
design_tokens:
  colors: {primary: "#4F46E5", secondary: "#10B981", accent: "#F59E0B", bg: "#0F172A", text: "#F8FAFC", muted: "#94A3B8"}
  fonts: {heading: "Inter", body: "Inter", mono: "JetBrains Mono"}
  radius: "0.5rem"
  shadow: "0 1px 3px rgba(0,0,0,0.3)"
density_score: 0.89
related:
  - bld_schema_landing_page
  - bld_quality_gate_landing_page
  - bld_output_template_landing_page
  - bld_memory_landing_page
  - bld_model_landing_page
  - bld_tools_landing_page
  - bld_architecture_landing_page
  - p01_kc_tailwind_patterns
  - p09_lpt_landing_page_template
  - p05_output_style_guide
---

## Design Tokens

| Token | Value |
|-------|-------|
| Primary | #4F46E5 (indigo) |
| Secondary | #10B981 (emerald) |
| Accent | #F59E0B (amber) |
| Background | #0F172A (slate-900) |
| Font | Inter + JetBrains Mono |

## Sections

| # | ID | Type | CTA |
|---|----|------|-----|
| 1 | hero | hero | yes |
| 2 | problem | problem | no |
| 3 | solution | solution | no |
| 4 | features | features | no |
| 5 | social-proof | social-proof | no |
| 6 | how-it-works | how-it-works | yes |
| 7 | integrations | integrations | no |
| 8 | pricing | pricing | yes |
| 9 | testimonials | testimonials | no |
| 10 | faq | faq | no |
| 11 | cta | cta | yes |
| 12 | footer | footer | no |

## Code

```html
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="One hub to sync products, track orders, and manage integrations across Shopify, Bling, and Mercado Livre." />
  <meta property="og:title" content="Admin Dashboard - Unified Commerce Operations Hub" />
  <meta property="og:description" content="Real-time sync. Zero drift. Ship faster." />
  <meta property="og:image" content="https://example.com/og-admin-dashboard.jpg" />
  <meta property="og:type" content="website" />
  <link rel="canonical" href="https://example.com/admin" />
  <title>Admin Dashboard - Unified Commerce Operations Hub</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"SoftwareApplication","name":"Admin Dashboard","applicationCategory":"BusinessApplication","offers":{"@type":"Offer","price":"99","priceCurrency":"USD"}}
  </script>
  <style>
    body { font-family: 'Inter', sans-serif; }
    .faq-answer { display: none; }
    .faq-item.open .faq-answer { display: block; }
  </style>
</head>
<body class="bg-slate-900 text-slate-100 antialiased">

<!-- NAV -->
<header class="sticky top-0 z-50 bg-slate-900/95 backdrop-blur border-b border-slate-800">
  <nav class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between" aria-label="Main navigation">
    <span class="font-bold text-lg text-indigo-400">AdminHub</span>
    <div class="hidden md:flex items-center gap-8 text-sm text-slate-400">
      <a href="#features" class="hover:text-white transition">Features</a>
      <a href="#pricing" class="hover:text-white transition">Pricing</a>
      <a href="#faq" class="hover:text-white transition">FAQ</a>
    </div>
    <a href="#pricing" data-track="nav-cta" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 rounded-lg text-sm font-semibold transition">
      Start Free
    </a>
  </nav>
</header>

<!-- HERO -->
<section id="hero" aria-label="Hero" class="min-h-screen flex items-center py-20">
  <div class="max-w-6xl mx-auto px-6 text-center">
    <span class="inline-block bg-indigo-600/20 text-indigo-400 text-sm font-medium px-3 py-1 rounded-full mb-6">Commerce Operations Hub</span>
    <h1 class="text-5xl md:text-7xl font-bold tracking-tight mb-6">One dashboard.<br/>Zero sync errors.</h1>
    <p class="text-xl text-slate-400 max-w-2xl mx-auto mb-10">
      Sync products across Shopify, Bling, and Mercado Livre in real-time. Monitor KPIs, fire actions, and manage integrations from a single admin hub.
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <a href="#pricing" data-track="hero-primary-cta"
         class="px-8 py-4 bg-indigo-600 hover:bg-indigo-500 rounded-lg font-semibold transition focus:outline-none focus:ring-2 focus:ring-indigo-400">
        Start Free Trial
      </a>
      <a href="#features" data-track="hero-secondary-cta"
         class="px-8 py-4 border border-slate-600 hover:border-slate-400 rounded-lg font-semibold transition">
        See Features
      </a>
    </div>
    <p class="mt-6 text-sm text-slate-500">No credit card required. Setup in 5 minutes.</p>
  </div>
</section>

<!-- PROBLEM -->
<section id="problem" aria-label="Problem" class="py-20 bg-slate-800/50">
  <div class="max-w-4xl mx-auto px-6 text-center">
    <h2 class="text-3xl font-bold mb-4">Managing 3 platforms manually is a full-time job</h2>
    <p class="text-slate-400 mb-10">Every hour spent copying data is an hour not spent growing.</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
      <div class="bg-slate-800 p-6 rounded-lg border border-slate-700">
        <p class="text-amber-400 font-semibold mb-2">Inventory drift</p>
        <p class="text-slate-400 text-sm">Products go out of stock on Shopify while Bling still shows availability, causing overselling.</p>
      </div>
      <div class="bg-slate-800 p-6 rounded-lg border border-slate-700">
        <p class="text-amber-400 font-semibold mb-2">Manual reconciliation</p>
        <p class="text-slate-400 text-sm">Hours per week copying data between platforms and hunting for discrepancies.</p>
      </div>
      <div class="bg-slate-800 p-6 rounded-lg border border-slate-700">
        <p class="text-amber-400 font-semibold mb-2">Blind spots</p>
        <p class="text-slate-400 text-sm">No single view of sync health, pending orders, and token expiry across all channels.</p>
      </div>
    </div>
  </div>
</section>

<!-- SOLUTION -->
<section id="solution" aria-label="Solution" class="py-20">
  <div class="max-w-4xl mx-auto px-6 text-center">
    <h2 class="text-3xl font-bold mb-4">One hub. Every channel. Always in sync.</h2>
    <p class="text-slate-400 max-w-2xl mx-auto">AdminHub connects your entire commerce stack, eliminates drift, and gives you a single source of truth for every SKU, order, and integration token.</p>
    <div class="mt-10 grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
      <div class="bg-indigo-600/10 border border-indigo-600/30 p-6 rounded-lg">
        <p class="text-indigo-400 font-semibold mb-2">Before AdminHub</p>
        <ul class="text-slate-400 text-sm space-y-1 list-disc list-inside">
          <li>3 tabs open at all times</li>
          <li>Inventory spreadsheet updated manually</li>
          <li>Broken integrations found by customers</li>
        </ul>
      </div>
      <div class="flex items-center justify-center text-3xl font-bold text-indigo-400">-&gt;</div>
      <div class="bg-emerald-600/10 border border-emerald-600/30 p-6 rounded-lg">
        <p class="text-emerald-400 font-semibold mb-2">After AdminHub</p>
        <ul class="text-slate-400 text-sm space-y-1 list-disc list-inside">
          <li>One dashboard, all channels live</li>
          <li>Auto-sync on every product update</li>
          <li>Token expiry alerts 7 days early</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- FEATURES -->
<section id="features" aria-label="Features" class="py-20 bg-slate-800/50">
  <div class="max-w-6xl mx-auto px-6">
    <h2 class="text-3xl font-bold text-center mb-4">Everything in one place</h2>
    <p class="text-slate-400 text-center mb-12">Built for commerce operators who run lean teams.</p>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <div class="bg-slate-900 p-6 rounded-xl border border-slate-700 hover:border-indigo-600 transition">
        <div class="w-10 h-10 bg-indigo-600/20 rounded-lg flex items-center justify-center mb-4" aria-hidden="true">
          <svg class="w-5 h-5 text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
        </div>
        <h3 class="font-semibold text-lg mb-2">Real-time KPI Cards</h3>
        <p class="text-slate-400 text-sm">Total products, sync status, and pending errors at a glance with live Supabase queries.</p>
      </div>
      <div class="bg-slate-900 p-6 rounded-xl border border-slate-700 hover:border-emerald-600 transition">
        <div class="w-10 h-10 bg-emerald-600/20 rounded-lg flex items-center justify-center mb-4" aria-hidden="true">
          <svg class="w-5 h-5 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" /></svg>
        </div>
        <h3 class="font-semibold text-lg mb-2">One-Click Sync</h3>
        <p class="text-slate-400 text-sm">Bidirectional sync across all channels with a single POST. Dry-run mode before committing.</p>
      </div>
      <div class="bg-slate-900 p-6 rounded-xl border border-slate-700 hover:border-amber-600 transition">
        <div class="w-10 h-10 bg-amber-600/20 rounded-lg flex items-center justify-center mb-4" aria-hidden="true">
          <svg class="w-5 h-5 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" /></svg>
        </div>
        <h3 class="font-semibold text-lg mb-2">Token Expiry Alerts</h3>
        <p class="text-slate-400 text-sm">Proactive warnings before Bling or ML tokens expire. Never wake up to a broken integration.</p>
      </div>
      <div class="bg-slate-900 p-6 rounded-xl border border-slate-700 hover:border-indigo-600 transition">
        <div class="w-10 h-10 bg-indigo-600/20 rounded-lg flex items-center justify-center mb-4" aria-hidden="true">
          <svg class="w-5 h-5 text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" /></svg>
        </div>
        <h3 class="font-semibold text-lg mb-2">Audit Log</h3>
        <p class="text-slate-400 text-sm">Full history of every sync event, error, and manual override. Export to CSV in one click.</p>
      </div>
      <div class="bg-slate-900 p-6 rounded-xl border border-slate-700 hover:border-emerald-600 transition">
        <div class="w-10 h-10 bg-emerald-600/20 rounded-lg flex items-center justify-center mb-4" aria-hidden="true">
          <svg class="w-5 h-5 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
        </div>
        <h3 class="font-semibold text-lg mb-2">RBAC Permissions</h3>
        <p class="text-slate-400 text-sm">Fine-grained roles: viewer, operator, admin. Supabase RLS enforced at every query.</p>
      </div>
      <div class="bg-slate-900 p-6 rounded-xl border border-slate-700 hover:border-amber-600 transition">
        <div class="w-10 h-10 bg-amber-600/20 rounded-lg flex items-center justify-center mb-4" aria-hidden="true">
          <svg class="w-5 h-5 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
        </div>
        <h3 class="font-semibold text-lg mb-2">Webhook Triggers</h3>
        <p class="text-slate-400 text-sm">Fire custom webhooks on sync events, errors, or threshold breaches. No code required.</p>
      </div>
    </div>
  </div>
</section>

<!-- SOCIAL PROOF -->
<section id="social-proof" aria-label="Social proof" class="py-16 bg-slate-900">
  <div class="max-w-4xl mx-auto px-6 text-center">
    <h2 class="text-2xl font-bold mb-10">Trusted by fast-moving commerce teams</h2>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-8 mb-10">
      <div><p class="text-4xl font-bold text-indigo-400">2.4M+</p><p class="text-slate-400 text-sm mt-1">products synced</p></div>
      <div><p class="text-4xl font-bold text-emerald-400">99.8%</p><p class="text-slate-400 text-sm mt-1">sync success rate</p></div>
      <div><p class="text-4xl font-bold text-amber-400">340+</p><p class="text-slate-400 text-sm mt-1">active stores</p></div>
      <div><p class="text-4xl font-bold text-indigo-400">&lt;2s</p><p class="text-slate-400 text-sm mt-1">avg sync latency</p></div>
    </div>
    <div class="flex flex-wrap justify-center gap-4 text-sm text-slate-500">
      <span class="px-4 py-2 bg-slate-800 rounded-full">Shopify Plus partners</span>
      <span class="px-4 py-2 bg-slate-800 rounded-full">SOC 2 Type II</span>
      <span class="px-4 py-2 bg-slate-800 rounded-full">LGPD compliant</span>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section id="how-it-works" aria-label="How it works" class="py-20 bg-slate-800/50">
  <div class="max-w-4xl mx-auto px-6 text-center">
    <h2 class="text-3xl font-bold mb-12">Up and running in 3 steps</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-left">
      <div class="relative">
        <span class="absolute -top-4 -left-4 w-8 h-8 bg-indigo-600 rounded-full flex items-center justify-center text-sm font-bold">1</span>
        <div class="bg-slate-900 p-6 rounded-xl border border-slate-700 h-full">
          <h3 class="font-semibold mb-2">Connect channels</h3>
          <p class="text-slate-400 text-sm">Paste your Shopify, Bling, and Mercado Livre API keys. OAuth flow for ML handles auth automatically.</p>
        </div>
      </div>
      <div class="relative">
        <span class="absolute -top-4 -left-4 w-8 h-8 bg-indigo-600 rounded-full flex items-center justify-center text-sm font-bold">2</span>
        <div class="bg-slate-900 p-6 rounded-xl border border-slate-700 h-full">
          <h3 class="font-semibold mb-2">Map your products</h3>
          <p class="text-slate-400 text-sm">Auto-match by SKU or manually link products across platforms. Bulk import via CSV or API.</p>
        </div>
      </div>
      <div class="relative">
        <span class="absolute -top-4 -left-4 w-8 h-8 bg-indigo-600 rounded-full flex items-center justify-center text-sm font-bold">3</span>
        <div class="bg-slate-900 p-6 rounded-xl border border-slate-700 h-full">
          <h3 class="font-semibold mb-2">Set sync rules</h3>
          <p class="text-slate-400 text-sm">Define which platform is the source of truth per field. Enable real-time or scheduled batch sync.</p>
        </div>
      </div>
    </div>
    <a href="#pricing" data-track="howitworks-cta" class="inline-block mt-10 px-8 py-3 bg-indigo-600 hover:bg-indigo-500 rounded-lg font-semibold transition">
      Get Started Free
    </a>
  </div>
</section>

<!-- INTEGRATIONS -->
<section id="integrations" aria-label="Supported integrations" class="py-16 bg-slate-900">
  <div class="max-w-4xl mx-auto px-6 text-center">
    <h2 class="text-2xl font-bold mb-8">Connects to your entire stack</h2>
    <div class="flex flex-wrap justify-center gap-4">
      <span class="px-5 py-2 bg-slate-800 border border-slate-700 rounded-full text-sm font-medium">Shopify</span>
      <span class="px-5 py-2 bg-slate-800 border border-slate-700 rounded-full text-sm font-medium">Bling ERP</span>
      <span class="px-5 py-2 bg-slate-800 border border-slate-700 rounded-full text-sm font-medium">Mercado Livre</span>
      <span class="px-5 py-2 bg-slate-800 border border-slate-700 rounded-full text-sm font-medium">Supabase</span>
      <span class="px-5 py-2 bg-slate-800 border border-slate-700 rounded-full text-sm font-medium">Webhooks</span>
      <span class="px-5 py-2 bg-slate-800 border border-slate-700 rounded-full text-sm font-medium">REST API</span>
    </div>
  </div>
</section>

<!-- PRICING -->
<section id="pricing" aria-label="Pricing" class="py-20 bg-slate-800/50">
  <div class="max-w-5xl mx-auto px-6">
    <h2 class="text-3xl font-bold text-center mb-4">Simple, honest pricing</h2>
    <p class="text-slate-400 text-center mb-12">14-day free trial on all plans. No credit card required.</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-slate-900 p-8 rounded-xl border border-slate-700">
        <h3 class="text-xl font-semibold mb-2">Starter</h3>
        <p class="text-4xl font-bold mb-1">$49<span class="text-lg font-normal text-slate-400">/mo</span></p>
        <p class="text-slate-400 text-sm mb-6">Up to 500 products</p>
        <ul class="space-y-3 text-sm mb-8" role="list">
          <li class="flex items-center gap-2"><span class="text-emerald-400" aria-hidden="true">[+]</span> Real-time KPI dashboard</li>
          <li class="flex items-center gap-2"><span class="text-emerald-400" aria-hidden="true">[+]</span> Shopify + Bling sync</li>
          <li class="flex items-center gap-2"><span class="text-slate-500" aria-hidden="true">[-]</span> ML integration</li>
          <li class="flex items-center gap-2"><span class="text-slate-500" aria-hidden="true">[-]</span> RBAC roles</li>
        </ul>
        <a href="#" data-track="pricing-starter" class="block text-center px-6 py-3 border border-indigo-600 text-indigo-400 rounded-lg hover:bg-indigo-600 hover:text-white transition">Get Started</a>
      </div>
      <div class="bg-indigo-600 p-8 rounded-xl border border-indigo-500 relative">
        <span class="absolute -top-3 left-1/2 -translate-x-1/2 bg-amber-500 text-white text-xs font-semibold px-3 py-1 rounded-full">Most Popular</span>
        <h3 class="text-xl font-semibold mb-2">Pro</h3>
        <p class="text-4xl font-bold mb-1">$99<span class="text-lg font-normal text-indigo-200">/mo</span></p>
        <p class="text-indigo-200 text-sm mb-6">Unlimited products</p>
        <ul class="space-y-3 text-sm mb-8" role="list">
          <li class="flex items-center gap-2"><span aria-hidden="true">[+]</span> Everything in Starter</li>
          <li class="flex items-center gap-2"><span aria-hidden="true">[+]</span> Mercado Livre sync</li>
          <li class="flex items-center gap-2"><span aria-hidden="true">[+]</span> RBAC roles</li>
          <li class="flex items-center gap-2"><span aria-hidden="true">[+]</span> Priority support</li>
        </ul>
        <a href="#" data-track="pricing-pro" class="block text-center px-6 py-3 bg-white text-indigo-700 font-semibold rounded-lg hover:bg-indigo-50 transition">Start Free Trial</a>
      </div>
      <div class="bg-slate-900 p-8 rounded-xl border border-slate-700">
        <h3 class="text-xl font-semibold mb-2">Enterprise</h3>
        <p class="text-4xl font-bold mb-1">Custom</p>
        <p class="text-slate-400 text-sm mb-6">Unlimited everything</p>
        <ul class="space-y-3 text-sm mb-8" role="list">
          <li class="flex items-center gap-2"><span class="text-emerald-400" aria-hidden="true">[+]</span> Everything in Pro</li>
          <li class="flex items-center gap-2"><span class="text-emerald-400" aria-hidden="true">[+]</span> SLA guarantee</li>
          <li class="flex items-center gap-2"><span class="text-emerald-400" aria-hidden="true">[+]</span> Dedicated support</li>
          <li class="flex items-center gap-2"><span class="text-emerald-400" aria-hidden="true">[+]</span> Custom integrations</li>
        </ul>
        <a href="mailto:sales@example.com" data-track="pricing-enterprise" class="block text-center px-6 py-3 border border-slate-600 text-slate-300 rounded-lg hover:border-slate-400 transition">Contact Sales</a>
      </div>
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section id="testimonials" aria-label="Testimonials" class="py-20 bg-slate-900">
  <div class="max-w-5xl mx-auto px-6">
    <h2 class="text-3xl font-bold text-center mb-12">What operators say</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <figure class="bg-slate-800 p-6 rounded-xl border border-slate-700">
        <blockquote class="text-slate-300 text-sm mb-4">"We cut reconciliation time from 8 hours a week to zero. AdminHub just handles it."</blockquote>
        <figcaption class="flex items-center gap-3">
          <img src="https://ui-avatars.com/api/?name=Ana+Costa&background=4F46E5&color=fff&size=40" alt="Ana Costa" class="w-10 h-10 rounded-full" loading="lazy" />
          <div><p class="font-semibold text-sm">Ana Costa</p><p class="text-slate-500 text-xs">Head of Ops, Loja Verde</p></div>
        </figcaption>
      </figure>
      <figure class="bg-slate-800 p-6 rounded-xl border border-slate-700">
        <blockquote class="text-slate-300 text-sm mb-4">"The token expiry alert alone saved us from a 48-hour ML outage. Worth every cent."</blockquote>
        <figcaption class="flex items-center gap-3">
          <img src="https://ui-avatars.com/api/?name=Marcos+Lima&background=10B981&color=fff&size=40" alt="Marcos Lima" class="w-10 h-10 rounded-full" loading="lazy" />
          <div><p class="font-semibold text-sm">Marcos Lima</p><p class="text-slate-500 text-xs">CTO, TechModa</p></div>
        </figcaption>
      </figure>
      <figure class="bg-slate-800 p-6 rounded-xl border border-slate-700">
        <blockquote class="text-slate-300 text-sm mb-4">"Setup was 20 minutes. We went from 3 separate tools to one dashboard the whole team uses."</blockquote>
        <figcaption class="flex items-center gap-3">
          <img src="https://ui-avatars.com/api/?name=Beatriz+Souza&background=F59E0B&color=fff&size=40" alt="Beatriz Souza" class="w-10 h-10 rounded-full" loading="lazy" />
          <div><p class="font-semibold text-sm">Beatriz Souza</p><p class="text-slate-500 text-xs">Founder, BelezaHub</p></div>
        </figcaption>
      </figure>
    </div>
  </div>
</section>

<!-- FAQ -->
<section id="faq" aria-label="Frequently asked questions" class="py-20 bg-slate-800/50">
  <div class="max-w-3xl mx-auto px-6">
    <h2 class="text-3xl font-bold text-center mb-12">Frequently asked questions</h2>
    <div class="space-y-4">
      <details class="bg-slate-900 border border-slate-700 rounded-lg" open>
        <summary class="px-6 py-4 cursor-pointer font-semibold text-sm list-none flex justify-between items-center">
          Does AdminHub work with Shopify Basic? <span class="text-slate-500 text-xs">[+]</span>
        </summary>
        <p class="px-6 pb-4 text-slate-400 text-sm">Yes. AdminHub works with all Shopify plans including Basic. The only requirement is a valid Admin API key with read/write product permissions.</p>
      </details>
      <details class="bg-slate-900 border border-slate-700 rounded-lg">
        <summary class="px-6 py-4 cursor-pointer font-semibold text-sm list-none flex justify-between items-center">
          How is pricing calculated for large catalogs? <span class="text-slate-500 text-xs">[+]</span>
        </summary>
        <p class="px-6 pb-4 text-slate-400 text-sm">Pro and Enterprise plans are unlimited. Starter is capped at 500 active SKUs. Adding more? Upgrade to Pro in one click from your dashboard.</p>
      </details>
      <details class="bg-slate-900 border border-slate-700 rounded-lg">
        <summary class="px-6 py-4 cursor-pointer font-semibold text-sm list-none flex justify-between items-center">
          Is data stored on your servers? <span class="text-slate-500 text-xs">[+]</span>
        </summary>
        <p class="px-6 pb-4 text-slate-400 text-sm">AdminHub stores only sync metadata (event timestamps, status). Your product data never rests on our servers; we query channels directly via their APIs.</p>
      </details>
      <details class="bg-slate-900 border border-slate-700 rounded-lg">
        <summary class="px-6 py-4 cursor-pointer font-semibold text-sm list-none flex justify-between items-center">
          Can I cancel anytime? <span class="text-slate-500 text-xs">[+]</span>
        </summary>
        <p class="px-6 pb-4 text-slate-400 text-sm">Yes. Cancel from your account settings at any time. No penalties, no retention calls.</p>
      </details>
      <details class="bg-slate-900 border border-slate-700 rounded-lg">
        <summary class="px-6 py-4 cursor-pointer font-semibold text-sm list-none flex justify-between items-center">
          Do you offer a free trial? <span class="text-slate-500 text-xs">[+]</span>
        </summary>
        <p class="px-6 pb-4 text-slate-400 text-sm">All plans include a 14-day free trial. No credit card required to start.</p>
      </details>
    </div>
  </div>
</section>

<!-- CTA FINAL -->
<section id="cta" aria-label="Call to action" class="py-24 bg-gradient-to-br from-indigo-900 to-slate-900">
  <div class="max-w-3xl mx-auto px-6 text-center">
    <h2 class="text-4xl font-bold mb-6">Stop syncing manually. Start scaling.</h2>
    <p class="text-slate-300 text-xl mb-4">Set up in 5 minutes. Cancel anytime.</p>
    <p class="text-slate-400 text-sm mb-10">Join 340+ commerce teams already running on AdminHub.</p>
    <a href="#" data-track="footer-cta"
       class="inline-block px-10 py-4 bg-indigo-600 hover:bg-indigo-500 rounded-lg text-lg font-semibold transition focus:outline-none focus:ring-2 focus:ring-indigo-400">
      Start Free Trial
    </a>
    <p class="mt-4 text-slate-500 text-sm">14-day free trial. No credit card. Cancel anytime.</p>
  </div>
</section>

<!-- FOOTER -->
<footer class="bg-slate-950 py-10 text-slate-500 text-sm">
  <div class="max-w-6xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-4">
    <p>AdminHub &copy; 2026. All rights reserved.</p>
    <nav aria-label="Footer navigation" class="flex gap-6">
      <a href="/privacy" class="hover:text-slate-300 transition">Privacy</a>
      <a href="/terms" class="hover:text-slate-300 transition">Terms</a>
      <a href="/docs" class="hover:text-slate-300 transition">Docs</a>
      <a href="mailto:support@example.com" class="hover:text-slate-300 transition">Support</a>
    </nav>
  </div>
</footer>

</body>
</html>
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_landing_page]] | upstream | 0.52 |
| [[bld_quality_gate_landing_page]] | upstream | 0.48 |
| [[bld_output_template_landing_page]] | upstream | 0.46 |
| [[bld_memory_landing_page]] | related | 0.44 |
| [[bld_model_landing_page]] | upstream | 0.43 |
| [[bld_tools_landing_page]] | upstream | 0.41 |
| [[bld_architecture_landing_page]] | related | 0.39 |
| [[p01_kc_tailwind_patterns]] | upstream | 0.38 |
| [[p09_lpt_landing_page_template]] | downstream | 0.36 |
| [[p05_output_style_guide]] | related | 0.34 |
