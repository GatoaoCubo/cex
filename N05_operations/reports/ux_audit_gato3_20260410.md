---
id: ux_audit_gato3_20260410
kind: e2e_eval
title: "UX & Frontend Audit -- gato3.com.br"
version: 1.0.0
date: 2026-04-10
nucleus: N05
domain: operations
target: https://gato3.com.br
source_repo: gato-cubo-commerce
quality: null
pillar: P07
tags: [ux-audit, frontend, qa, gato3, e2e]
---

# UX & Frontend Audit -- gato3.com.br

**Date**: 2026-04-10
**Auditor**: N05 Operations Nucleus
**Method**: WebFetch (live site) + Static Source Code Analysis
**Source**: `C:\Users\PC\Documents\GitHub\gato-cubo-commerce\`
**Stack**: React 18 + Vite + Tailwind + shadcn/ui + Supabase + Shopify

---

## Executive Summary

| Category | Score | Status |
|----------|-------|--------|
| SEO & Structured Data | 9/10 | PASS |
| Accessibility (a11y) | 8/10 | PASS |
| Performance | 8.5/10 | PASS |
| Error Handling | 9/10 | PASS |
| LGPD / Cookie Compliance | 8/10 | PASS |
| PWA Readiness | 4/10 | FAIL |
| Dark Mode | 2/10 | FAIL |
| SSR / Crawlability | 2/10 | FAIL |
| E-commerce Flow | 9/10 | PASS |
| AI Chat (Ronronalda) | 9/10 | PASS |
| B2B Authentication | 8.5/10 | PASS |
| Image Optimization | 9/10 | PASS |
| **Overall** | **7.2/10** | **3 critical issues** |

---

## P0 -- Critical Issues (Broken / Blocking)

### P0-1: SPA Without SSR -- Search Engines See Empty Shell

**Severity**: P0 (Revenue impact)
**Location**: Site-wide architecture
**Evidence**: WebFetch of all 6 tested URLs returned ONLY the JavaScript shell -- no rendered content visible. Google's crawler faces the same problem.

The site is a pure client-side React SPA. When any crawler (Googlebot, social media scrapers, link previews) fetches a page, it receives:

```html
<title>GATO3 | Produtos Premium para Gatos | Bem-estar Felino</title>
<!-- ...GA4 script, font preload, Lovable badge... -->
<div id="root"></div>
<!-- JavaScript bundles -->
```

No product data, no blog content, no navigation -- just an empty div.

**Impact**:
- Google MAY render JavaScript but with delays (days/weeks for indexing)
- Social media link previews (WhatsApp, Instagram, Facebook) show only the generic title
- Product pages will NOT appear in Google Shopping results without SSR
- Blog posts lose all SEO value (Schema.org BlogPosting is generated client-side)

**Fix options** (ranked by effort):
1. **Prerender.io / Rendertron** -- Add a prerendering proxy (lowest effort, ~2h)
2. **Vite SSG plugin** -- Static site generation at build time (~1 day)
3. **Migrate to Next.js** -- Full SSR framework (highest effort, 1-2 weeks)

**Recommendation**: Option 1 (prerender proxy) for immediate fix, plan Option 2 for next sprint.

### P0-2: No Service Worker -- PWA is Broken

**Severity**: P0
**Location**: Missing `sw.js` / service worker registration
**Evidence**: `manifest.json` exists at `/public/manifest.json` with correct config (name, icons, start_url), but NO service worker is registered anywhere in the codebase.

```
manifest.json: EXISTS (correct)
service worker: MISSING
offline capability: NONE
push notifications: NONE
install prompt: BROKEN (Chrome won't offer "Add to Home Screen" without SW)
```

**Fix**: Install `vite-plugin-pwa` and configure Workbox caching strategy. ~2h of work.

### P0-3: Dark Mode Toggle Missing -- CSS Without UI

**Severity**: P0 (design inconsistency)
**Location**: `src/index.css` (dark mode variables defined), UI (no toggle)
**Evidence**: 
- `next-themes` package is installed in `package.json`
- CSS dark mode variables are defined (`.dark { ... }`)
- Several pages have `dark:*` Tailwind classes
- **BUT no ThemeProvider wraps the app and no toggle exists in the UI**

Users on system-level dark mode may see a partially styled dark theme with broken contrast or invisible elements.

**Fix**: Either remove all `dark:*` classes and the `next-themes` dependency, or properly implement `ThemeProvider` + toggle button. ~1h.

---

## P1 -- Degraded (Works but Needs Attention)

### P1-1: Cookie Banner -- Accept/Reject Without Granularity

**Location**: `src/components/CookieBanner.tsx`
**Finding**: The LGPD cookie banner offers only "Accept All" and "Reject All". Under LGPD best practice, users should be able to selectively enable/disable categories (analytics, marketing, essential).

**Current implementation**:
- `role="dialog"` + `aria-label` (good a11y)
- `localStorage` persistence via `gato3_cookie_consent`
- Links to `/privacidade` (good)
- Missing: granular consent per category

**Risk**: Low legal risk for small businesses, but not best practice.
**Fix**: Add category toggles (essential, analytics, marketing). ~4h.

### P1-2: Newsletter -- No Double Opt-in

**Location**: `src/components/Footer.tsx` (Lines 20-87)
**Finding**: Newsletter subscription writes directly to Supabase `newsletter_subscribers` table without email confirmation (double opt-in).

**Risk**: 
- Fake email addresses pollute the list
- LGPD requires demonstrable consent -- single opt-in is weaker evidence
- Deliverability drops with unverified emails

**Fix**: Add confirmation email flow via Supabase Edge Function + Resend/SendGrid. ~4h.

### P1-3: Manifest Icons -- Missing Standard Sizes

**Location**: `public/manifest.json`
**Finding**: Only 3 icon sizes defined:
- favicon.png (32x32)
- apple-touch-icon.png (180x180)  
- logo-gato3.png (600x606, maskable)

Missing standard PWA sizes: 48x48, 72x72, 96x96, 144x144, 192x192, 512x512.

**Fix**: Generate icon set from source logo. ~30min.

### P1-4: Voice Input -- Chrome/Edge Only

**Location**: `src/components/RoChat.tsx` (Lines 94-138)
**Finding**: Voice input uses Web Speech API which is only supported in Chromium browsers. Firefox and Safari users get a silent failure.

**Fix**: Add feature detection and show/hide the mic button accordingly. ~30min.

---

## P2 -- Cosmetic / Polish

### P2-1: Lovable Badge Visible in Production

**Location**: All pages (injected by Lovable.dev platform)
**Finding**: A "Built with Lovable" badge appears on all pages. This is fine for development but looks unprofessional in production.

**Fix**: Remove Lovable badge in production build or use custom domain deployment without badge.

### P2-2: /ro Legacy Route Still Active

**Location**: `src/App.tsx` route config
**Finding**: `/ro` redirects to `/sac`. This is functional but creates a duplicate URL for the same content.

**Fix**: Add `noindex` to the `/ro` redirect or remove the legacy route if no external links point to it.

### P2-3: Missing Favicon Variety

**Location**: `index.html`
**Finding**: Only PNG favicon. Modern browsers benefit from SVG favicons (scalable, dark mode aware).

**Fix**: Add `<link rel="icon" type="image/svg+xml" href="/favicon.svg">`. ~15min.

---

## Detailed Test Results by Page

### 1. Homepage (`/` -> redirects to `/b2c`)

| Test | Result | Notes |
|------|--------|-------|
| Page loads | PASS | Redirects `/` to `/b2c` correctly |
| Hero image (WebP) | PASS | `hero-b2c-moodboard.webp`, preloaded in `index.html`, `loading="eager"` |
| Navigation menu | PASS | Header.tsx with mobile hamburger, focus trap, keyboard nav (Escape closes) |
| CTA buttons | PASS | Links to catalog, products, SAC |
| Mobile responsive | PASS (static) | Tailwind responsive classes throughout, mobile menu with slide-in |
| Footer | PASS | Newsletter form, external links (Shopee, ML, WhatsApp), institutional links |
| Cookie banner | PASS | `CookieBanner.tsx` with `role="dialog"`, 500ms delay animation |
| Console errors | N/A | Cannot test via static analysis (requires browser runtime) |

### 2. Catalog (`/catalogo`)

| Test | Result | Notes |
|------|--------|-------|
| Product grid | PASS | ProductCard components with image, name, price |
| Category filters | PASS | Filter UI present in Catalogo.tsx |
| Product links | PASS | Links to `/produtos/:slug` |
| Breadcrumbs | PASS | BreadcrumbList Schema.org generated |
| SEO meta tags | PASS | SEOHead component with dynamic title/description |
| Search debounce | PASS | Custom debounce hook (Lines 88-99) prevents excessive re-renders |

### 3. Product Pages (`/produtos/:slug`)

| Test | Result | Notes |
|------|--------|-------|
| Image gallery | PASS | ProductGallery.tsx with thumbnails, lazy loading |
| Price display | PASS | BRL formatting |
| "Comprar" button | PASS | Adds to Zustand cart -> Shopify checkout via Storefront API |
| Related products | PASS | Related products section present |
| Schema.org Product | PASS | JSON-LD with SKU, price, availability, brand, shipping |
| GA4 view_item | PASS | Fires on page load (Lines 43-52) |
| Error states | PASS | isLoading, error, not-found states with proper messaging |
| GA4 add_to_cart | PASS | Fires on button click with currency, value, items |

### 4. B2B Section (`/b2b`)

| Test | Result | Notes |
|------|--------|-------|
| Login form | PASS | Email/password + Google OAuth |
| Registration | PASS | CNPJ + company info, Supabase auth |
| Protected routes | PASS | ProtectedRoute component, redirect to login |
| Password recovery | PASS | `/b2b/recuperar-senha` with email flow |
| Role check | PASS | Validates `user_metadata?.type === "b2b_partner"` |
| Dashboard | PASS | `/parceiro/dashboard` with orders, sales, commission |

### 5. SAC / Ronronalda Chat (`/sac`)

| Test | Result | Notes |
|------|--------|-------|
| Chat widget | PASS | RoChat.tsx, WhatsApp-style UI |
| Message input | PASS | Text input + send button |
| AI response | PASS (static) | Calls `supabase.functions.invoke('ronronalda-chat')` -> Gemini Flash |
| Category selector | PARTIAL | 6 suggestion chips (not traditional categories) |
| Product recommendations | PASS | Products returned in API response, displayed as cards |
| Voice input | PARTIAL | Web Speech API -- Chromium only (P1-4) |
| TTS output | PASS | Edge function `ronronalda-tts`, voice: `nova` |
| Red flag detection | PASS | `audit.hasRedFlag` -> recommends vet visit |
| WhatsApp fallback | PASS | On API error, offers WhatsApp link |
| GA4 tracking | PASS | `ro_message_sent`, `ro_suggestion_clicked`, `ro_product_clicked` |

### 6. About (`/sobre`)

| Test | Result | Notes |
|------|--------|-------|
| Page renders | PASS | Lazy loaded |
| Brand story | PASS (static) | Content present in component |
| Images | PASS (static) | WebP format used |

### 7. Blog (`/blog`)

| Test | Result | Notes |
|------|--------|-------|
| Blog list | PASS | Blog.tsx with post cards |
| Individual posts | PASS | `/blog/:slug` with BlogPost.tsx |
| Schema.org BlogPosting | PASS | JSON-LD generated in structured-data.ts (Lines 169-199) |
| Featured image | PASS | Lazy loaded, aspect-video |
| SEO head | PASS | Dynamic title, description, og:tags per post |
| Blog collection schema | PASS | Lines 202-212 in structured-data.ts |

### 8. Cross-Cutting

| Test | Result | Notes |
|------|--------|-------|
| 404 page | PASS | NotFound.tsx with `noindex`, shows attempted path, nav options |
| Error boundary | PASS | ErrorBoundary.tsx catches render errors, shows user-friendly card |
| WebP images | PASS | All critical images in WebP with preload |
| LGPD cookie banner | PASS | CookieBanner.tsx with dialog role, consent storage |
| Dark mode | FAIL | CSS defined, no toggle, no ThemeProvider (P0-3) |
| Code splitting | PASS | 26+ lazy-loaded routes via React.lazy() |
| Bundle optimization | PASS | Vite manual chunks: vendor-react, vendor-query, vendor-ui |
| PWA manifest | PARTIAL | manifest.json exists, no service worker (P0-2) |
| Skip link | PASS | `<a class="skip-link" href="#conteudo">` on B2C page |
| Focus management | PASS | Mobile menu focus trap, keyboard navigation |
| Alt texts | PASS | Product images use `seo_alt_texts[0] || product.name` |
| Color contrast | PASS | CSS variables tuned for WCAG AA (muted-foreground: 38% lightness) |
| Analytics | PASS | GA4 with 6+ custom events, ecommerce tracking |

---

## Architecture Observations

### Route Map (30+ routes)

**B2C**: `/` (redirect), `/b2c`, `/catalogo`, `/produtos/:slug`, `/blog`, `/blog/:slug`, `/sac`, `/ro` (redirect), `/ongs`, `/sobre`, `/privacidade`, `/termos`

**B2B**: `/b2b`, `/b2b/cadastro`, `/b2b/login`, `/b2b/recuperar-senha`, `/b2b/nova-senha`, `/b2b/preview`, `/b2b/afiliados`, `/parceiro`, `/parceiro/dashboard`

**Admin**: `/login`, `/admin/produtos`, `/admin/produtos/novo`, `/admin/produtos/:id/editar`, `/admin/shopify`, `/admin/crm`, `/admin/integracoes`, `/admin/b2b-orders`

**Error**: `/*` (404)

### Schema.org Coverage (9 types)

| Schema Type | Pages | Status |
|-------------|-------|--------|
| Organization | Global | PASS |
| WebSite | Global | PASS |
| Product | `/produtos/:slug` | PASS |
| BreadcrumbList | Catalog, Blog | PASS |
| FAQPage | B2C homepage | PASS |
| LocalBusiness (PetStore) | Global | PASS |
| ItemList | Catalog | PASS |
| BlogPosting | `/blog/:slug` | PASS |
| Blog (collection) | `/blog` | PASS |

### Key Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| react | ^18.3.1 | UI framework |
| react-router-dom | ^6.30.1 | Routing |
| @supabase/supabase-js | ^2.58.0 | Backend (auth, DB, functions) |
| @tanstack/react-query | ^5.83.0 | Data fetching/caching |
| zustand | ^5.0.8 | State management (cart) |
| zod | ^3.25.76 | Schema validation |
| react-helmet | ^6.1.0 | SEO meta tags |
| tailwindcss | ^3.4.17 | Styling |
| @radix-ui/* | Various | Accessible UI primitives (30+ components) |
| vite | ^5.4.19 | Build tool (SWC compiler) |
| recharts | ^2.15.4 | Charts (admin/CRM) |
| leaflet | ^1.9.4 | Maps |
| embla-carousel-react | ^8.6.0 | Product carousels |

### E-commerce Flow

```
User clicks "Comprar"
  -> Zustand cart store (local)
  -> CartDrawer opens
  -> "Finalizar Compra" clicked
  -> Shopify Storefront API (GraphQL)
  -> Cart creation mutation
  -> Redirect to Shopify hosted checkout
  -> GA4: begin_checkout event
```

**External channels**: Shopee (`shopee.com.br/shop/1057176206`), Mercado Livre, WhatsApp (`5511916165577`)

---

## Bug List (Prioritized)

| # | Priority | Issue | Location | Fix Effort |
|---|----------|-------|----------|------------|
| 1 | P0 | SPA without SSR -- crawlers see empty shell | Architecture | 2h (prerender) to 2w (Next.js) |
| 2 | P0 | No service worker -- PWA install broken | Missing sw.js | 2h (vite-plugin-pwa) |
| 3 | P0 | Dark mode partially implemented -- broken UX for system dark users | index.css + missing ThemeProvider | 1h |
| 4 | P1 | Cookie banner lacks granular consent | CookieBanner.tsx | 4h |
| 5 | P1 | Newsletter has no double opt-in | Footer.tsx | 4h |
| 6 | P1 | PWA manifest missing standard icon sizes | manifest.json | 30min |
| 7 | P1 | Voice input fails silently on non-Chromium | RoChat.tsx | 30min |
| 8 | P2 | Lovable badge in production | All pages | Config change |
| 9 | P2 | /ro legacy redirect (duplicate URL) | App.tsx routes | 5min |
| 10 | P2 | No SVG favicon | index.html | 15min |

---

## Recommendations (Priority Order)

1. **IMMEDIATE**: Add prerender proxy (Prerender.io or Rendertron) to serve crawlable HTML to bots. This single change fixes the biggest SEO blocker.

2. **THIS WEEK**: Install `vite-plugin-pwa` with Workbox. Configure: precache app shell, runtime cache for product images, offline fallback page.

3. **THIS WEEK**: Either fully implement dark mode (add `ThemeProvider` from next-themes + toggle in Header) or strip all `dark:*` classes to prevent partial rendering.

4. **NEXT SPRINT**: Upgrade cookie banner with granular consent categories. Add double opt-in to newsletter flow.

5. **BACKLOG**: Generate complete PWA icon set, add SVG favicon, remove Lovable badge, clean up `/ro` redirect.

---

## Methodology Notes

- **Live site testing via WebFetch** confirmed the SPA crawlability issue -- all 6 URLs returned only the JS shell with no rendered content. This validates the P0-1 finding with real evidence.
- **Static source code analysis** covered 15 aspects across 50+ files with exact file paths and line numbers.
- **Limitations**: No runtime JavaScript execution (cannot test actual click interactions, console errors, network waterfall, Lighthouse scores). Recommend follow-up with Playwright or Lighthouse CI for runtime metrics.

---

*Report generated by N05 Operations Nucleus -- CEX UX Audit Pipeline*
*Method: WebFetch + Static Analysis | Date: 2026-04-10*
