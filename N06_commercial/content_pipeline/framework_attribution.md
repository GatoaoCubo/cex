---
id: framework_attribution
kind: content_monetization
pillar: P11
version: 1.0.0
title: "Content Attribution Framework -- Tracking Content-to-Revenue"
description: "UTM conventions, GA4 events, Supabase tracking, Instagram Insights integration, and blog-to-product click tracking. Full measurement stack for GATO3 content ROI."
domain: content_monetization
tags: [attribution, utm, GA4, analytics, tracking, GATO3, content-pipeline]
quality: null
nucleus: N06
mission: CONTENT_PIPELINE
created: 2026-04-10
horizon: 2026-04-15 to 2026-07-15
---

# Content Attribution Framework

> If you can't measure it, you can't optimize it. This framework ensures every content piece
> can be traced to revenue impact -- or conclusively shown to have none.

---

## 1. Attribution Architecture

```
CONTENT TOUCHPOINT            TRACKING LAYER              REVENUE LAYER
                                                         
IG Post (feed/reel/story)     UTM params on link          Shopify order
   |                            |                           |
Blog Article                  GA4 events                  Supabase content_attribution table
   |                            |                           |
Email                         Shopify UTM capture         Mercado Livre (limited)
   |                            |                           |
WhatsApp                      Manual tagging              Shopee (limited)
   |                                                        |
Marketplace card              Coupon codes                Aggregate: monthly report
```

---

## 2. UTM Convention (MANDATORY for all links)

### Structure

```
https://gato3.com.br/{path}?utm_source={source}&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}
```

### Parameter Definitions

| Parameter | Definition | Values |
|-----------|-----------|--------|
| `utm_source` | Where the click originates | `instagram`, `blog`, `email`, `whatsapp`, `tiktok`, `google`, `mercadolivre`, `shopee` |
| `utm_medium` | What type of content/placement | `feed`, `reel`, `story`, `linkinbio`, `article`, `newsletter`, `message`, `organic` |
| `utm_campaign` | Content campaign or topic | `educativo_s{week}`, `produto_{slug}`, `showcase_{slug}`, `promo_{event}`, `retention_{type}` |
| `utm_content` | Specific content piece identifier | `post_{YYYYMMDD}`, `cta_inline`, `cta_footer`, `carousel_s{slide}`, `reel_{id}` |

### UTM Templates by Channel

#### Instagram

| Content Type | UTM Template | Example |
|-------------|-------------|---------|
| Feed post -> site | `utm_source=instagram&utm_medium=feed&utm_campaign=produto_{slug}&utm_content=post_{date}` | `...produto_donut&utm_content=post_20260420` |
| Reel -> site | `utm_source=instagram&utm_medium=reel&utm_campaign=showcase_{slug}&utm_content=reel_{id}` | `...showcase_fonte_agua&utm_content=reel_001` |
| Story -> site | `utm_source=instagram&utm_medium=story&utm_campaign=promo_{event}&utm_content=swipeup` | `...promo_diadasmaes&utm_content=swipeup` |
| Link in bio -> site | `utm_source=instagram&utm_medium=linkinbio&utm_campaign=educativo_s{week}` | `...educativo_s03` |
| Link in bio -> blog | `utm_source=instagram&utm_medium=linkinbio&utm_campaign=blog_{article_slug}` | `...blog_por-que-gatos-arranham` |

#### Blog

| Content Type | UTM Template | Example |
|-------------|-------------|---------|
| Article -> product page | `utm_source=blog&utm_medium=article&utm_campaign=review_{slug}&utm_content=cta_inline` | `...review_donut&utm_content=cta_inline` |
| Article -> product (footer CTA) | `utm_source=blog&utm_medium=article&utm_campaign={topic}&utm_content=cta_footer` | `...hidratacao_felina&utm_content=cta_footer` |
| Article -> article (internal) | No UTM needed (same site) | Track via GA4 internal navigation |

#### Email

| Content Type | UTM Template | Example |
|-------------|-------------|---------|
| Newsletter -> site | `utm_source=email&utm_medium=newsletter&utm_campaign=weekly_s{week}&utm_content=cta_{position}` | `...weekly_s05&utm_content=cta_hero` |
| Post-purchase -> reorder | `utm_source=email&utm_medium=retention&utm_campaign=reorder_{product}&utm_content=cta_main` | `...reorder_escova&utm_content=cta_main` |

#### WhatsApp

| Content Type | UTM Template | Example |
|-------------|-------------|---------|
| Message -> site | `utm_source=whatsapp&utm_medium=message&utm_campaign=followup_{order_id}` | `...followup_12345` |

### UTM Naming Rules

| Rule | Detail |
|------|--------|
| All lowercase | Never mix cases |
| Underscores for spaces | `tapete_gelado` not `tapete-gelado` |
| Week numbers are 2 digits | `s01`, `s02`, ... `s13` |
| Dates are YYYYMMDD | `20260420` |
| Product slugs match Shopify handles | Use Shopify product URL slug |
| No accented characters | `hidratacao` not `hidratacao` (in this case same, but `fonte_agua` not `fonte_agua`) |
| Max 50 chars per parameter | Truncate if needed |

---

## 3. GA4 Event Configuration

### Custom Events to Create

| Event Name | Trigger | Parameters | Purpose |
|-----------|---------|-----------|---------|
| `content_click_product` | User clicks product link from blog article | `article_slug`, `product_slug`, `cta_position` | Track blog-to-product conversion |
| `content_save_guide` | User downloads/saves a guide or checklist | `guide_slug`, `content_type` | Track content value perception |
| `content_read_complete` | User scrolls to 90% of blog article | `article_slug`, `time_on_page` | Track content quality |
| `content_utm_landing` | User lands on site with UTM params | `utm_source`, `utm_medium`, `utm_campaign` | Track content-driven arrivals |
| `content_product_view` | User views product page from content source | `product_slug`, `referrer_type` | Track content-to-consideration |
| `content_add_to_cart` | User adds to cart after content-driven visit | `product_slug`, `utm_campaign` | Track content-to-intent |
| `content_purchase` | User completes purchase from content source | `order_id`, `utm_campaign`, `order_value` | Track content-to-revenue |

### GA4 Implementation (Shopify + GA4)

```
Shopify theme.liquid:
  - GA4 tag: G-XXXXXXXXXX
  - Capture UTM params on landing: store in session/cookie
  - Pass UTMs through to purchase event

Blog article template:
  - data-article-slug="{{ article.handle }}"
  - Product link onclick: ga('send', 'event', 'content_click_product', ...)
  - Scroll tracking: IntersectionObserver at 90% article height

Product page template:
  - Check referrer for blog/article URL patterns
  - Tag content_product_view event with referrer context
```

### GA4 Conversion Funnel

```
content_utm_landing
  |
  +--> content_read_complete (blog) or content_engagement (IG)
        |
        +--> content_click_product
              |
              +--> content_product_view
                    |
                    +--> content_add_to_cart
                          |
                          +--> content_purchase   <-- REVENUE EVENT
```

---

## 4. Supabase Tracking Layer

### Content Attribution Table

```sql
CREATE TABLE content_attribution (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  order_id TEXT NOT NULL,
  utm_source TEXT,
  utm_medium TEXT,
  utm_campaign TEXT,
  utm_content TEXT,
  landing_page TEXT,
  referrer TEXT,
  session_start TIMESTAMPTZ,
  purchase_at TIMESTAMPTZ,
  order_value DECIMAL(10,2),
  products JSONB,
  touchpoints JSONB,  -- array of content touchpoints before purchase
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_content_attr_source ON content_attribution(utm_source);
CREATE INDEX idx_content_attr_campaign ON content_attribution(utm_campaign);
CREATE INDEX idx_content_attr_date ON content_attribution(purchase_at);
```

### Content Performance Table

```sql
CREATE TABLE content_performance (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  content_id TEXT NOT NULL,       -- article slug or IG post ID
  content_type TEXT NOT NULL,     -- 'blog', 'ig_feed', 'ig_reel', 'ig_story'
  platform TEXT NOT NULL,         -- 'instagram', 'blog', 'tiktok'
  published_at TIMESTAMPTZ,
  funnel_stage TEXT,              -- 'awareness', 'consideration', 'conversion', 'retention'
  product_mentioned TEXT[],       -- array of product slugs
  impressions INTEGER,
  reach INTEGER,
  engagement INTEGER,
  saves INTEGER,
  shares INTEGER,
  clicks INTEGER,
  orders_attributed INTEGER DEFAULT 0,
  revenue_attributed DECIMAL(10,2) DEFAULT 0,
  updated_at TIMESTAMPTZ DEFAULT now()
);
```

### Sync Process

| Step | Frequency | Source | Destination |
|------|-----------|--------|-------------|
| 1. IG metrics import | Weekly (manual) | Instagram Insights export | content_performance |
| 2. GA4 event sync | Daily (automated) | GA4 BigQuery export or API | content_attribution |
| 3. Shopify order sync | Real-time (webhook) | Shopify order webhook | content_attribution |
| 4. Attribution join | Weekly (manual SQL) | content_attribution + content_performance | Revenue per content piece |

---

## 5. Instagram Insights Integration

### What to Track (Manual Weekly)

| Metric | Where to Find | What It Tells Us |
|--------|--------------|-----------------|
| Reach per post | Post Insights | Content discovery effectiveness |
| Engagement rate | Post Insights (calculate) | Content resonance |
| Saves | Post Insights | Content value (consideration stage) |
| Shares | Post Insights | Content virality (awareness stage) |
| Profile visits | Account Insights | Content -> curiosity bridge |
| Website clicks | Account Insights | Content -> site conversion |
| Follower growth source | Account Insights | Which content types attract followers |
| Top posts by reach | Account Insights | Content format optimization |
| Top posts by saves | Account Insights | Education content optimization |

### Weekly Tracking Spreadsheet Template

| Week | Post ID | Format | Funnel Stage | Reach | Engagement | Saves | Shares | Comments | Profile Visits | Website Clicks |
|------|---------|--------|-------------|-------|------------|-------|--------|----------|---------------|---------------|
| S01 | ... | Reel | Awareness | ... | ... | ... | ... | ... | ... | ... |
| S01 | ... | Carousel | Consideration | ... | ... | ... | ... | ... | ... | ... |

### Automation Opportunity (Phase 2)

In Phase 1 (90 days), Instagram Insights are tracked manually (weekly export).
In Phase 2, consider:
- Instagram Graph API integration (requires Facebook app review)
- Buffer/Later analytics integration (auto-export)
- Custom Supabase function to sync via Instagram Basic Display API

---

## 6. Blog-to-Product Click Tracking

### Implementation

```html
<!-- In blog article template -->
<a href="/products/{product-handle}?utm_source=blog&utm_medium=article&utm_campaign={article-handle}&utm_content=cta_inline"
   class="gato3-product-link"
   data-product="{product-handle}"
   data-article="{article-handle}"
   data-position="inline">
  Conheca o {Product Name}
</a>

<script>
document.querySelectorAll('.gato3-product-link').forEach(link => {
  link.addEventListener('click', () => {
    gtag('event', 'content_click_product', {
      article_slug: link.dataset.article,
      product_slug: link.dataset.product,
      cta_position: link.dataset.position
    });
  });
});
</script>
```

### Blog Content Performance Metrics

| Metric | Tool | Target |
|--------|------|--------|
| Unique pageviews per article | GA4 | 200+ (month 1), 500+ (month 3) |
| Avg time on page | GA4 | 3+ minutes |
| Scroll depth (90%+) | GA4 + scroll tracking | 40%+ of readers |
| Product link CTR | GA4 custom event | 3-5% of article readers |
| Bounce rate | GA4 | < 60% |
| Internal navigation (articles -> articles) | GA4 | 1.5+ pages/session |

---

## 7. Marketplace Attribution (Limitations)

### Mercado Livre

| What You Can Track | How |
|-------------------|-----|
| Total orders/revenue | ML seller dashboard |
| Search terms that led to product | ML analytics |
| GATO3 brand search volume | ML analytics (track "gato3", "gato ao cubo") |

| What You Can't Track | Workaround |
|---------------------|-----------|
| Which content piece drove the ML purchase | Correlation: spike in IG content -> spike in ML "gato3" searches |
| UTM-level attribution | Promo codes: "INSTAGRAM10" (10% off for IG followers) |
| Multi-touch journey | Survey: "Como nos conheceu?" in package insert card |

### Shopee

Same limitations as ML. Use Shopee-specific promo codes to differentiate:
- `GATO3BLOG` -- mentioned in blog articles pointing to Shopee
- `GATO3INSTA` -- mentioned in Instagram stories
- `GATO3WELCOME` -- new customer code from any channel

### Package Insert Card

Every GATO3 order (any channel) includes:

```
Frente:
  "Obrigado por escolher a GATO3!"
  "Siga @gatoaocubo3 para dicas felinas"
  QR code -> gato3.com.br?utm_source=package&utm_medium=insert&utm_campaign=thankyou

Verso:
  "Como voce nos conheceu?"
  [ ] Instagram
  [ ] Blog
  [ ] Mercado Livre
  [ ] Shopee
  [ ] Indicacao de amigo
  [ ] Google
  [ ] Outro: _______
  
  "Envie uma foto com #MeuGato3 e ganhe 10% na proxima compra"
```

---

## 8. Attribution Model

### First-Touch vs Last-Touch vs Linear

| Model | Definition | When to Use |
|-------|-----------|-------------|
| First-touch | Credit to first content interaction | Understanding which content DISCOVERS customers |
| Last-touch | Credit to last interaction before purchase | Understanding which content CONVERTS customers |
| Linear | Equal credit across all touchpoints | Understanding the full journey |

### GATO3 Phase 1 Recommendation: **Last-Touch**

Why: With low volume (Month 1-3), multi-touch analysis is statistically unreliable. Last-touch is:
- Simplest to implement (Shopify + UTM captures last click)
- Actionable (tells you which CTA/link actually drove the sale)
- Sufficient for optimization decisions at this scale

### Phase 2: Migrate to Linear

When monthly orders from content exceed 100, implement linear attribution via Supabase `touchpoints` JSONB array. Store all content interactions per session, distribute credit equally.

---

## 9. Monthly Attribution Report Template

### Report Structure

```
GATO3 Content Attribution Report -- Month X (YYYY-MM)

1. TRAFFIC SUMMARY
   - Total site visits: X
   - From content: X (Y%)
   - From Instagram: X
   - From Blog: X
   - From Email: X
   - Direct/other: X

2. CONTENT PERFORMANCE (Top 10)
   | Content Piece | Type | Funnel Stage | Reach | Clicks | Orders | Revenue |
   |...|...|...|...|...|...|...|

3. PRODUCT ATTRIBUTION
   | Product | Content-Driven Orders | Content Revenue | Best Performing Content |
   |...|...|...|...|

4. FUNNEL CONVERSION RATES
   | Stage | Volume | Conversion to Next | Change vs Last Month |
   | Awareness (reach) | X | Y% to consideration | +/-Z% |
   | Consideration (saves/profile visits) | X | Y% to click | +/-Z% |
   | Conversion (site visits) | X | Y% to purchase | +/-Z% |
   | Retention (repeat) | X | Y% reorder rate | +/-Z% |

5. INSIGHTS + ACTIONS
   - What worked: [top 3 content pieces and why]
   - What didn't work: [bottom 3 and hypothesis]
   - Next month actions: [3 optimization actions]

6. REVENUE ATTRIBUTION
   - Direct content revenue: R$ X
   - Estimated indirect (marketplace lift): R$ Y
   - Total content-influenced revenue: R$ Z
   - Content ROI: X%
```

---

## 10. Tracking Implementation Checklist

| Task | Priority | Owner | Status |
|------|----------|-------|--------|
| GA4 property setup on gato3.com.br | P0 | N05/Dev | TODO |
| GA4 custom events configuration | P0 | N05/Dev | TODO |
| UTM link generator spreadsheet | P0 | N06 | Defined above |
| Shopify UTM capture on checkout | P0 | N05/Dev | TODO |
| Blog product link tracking (onclick events) | P1 | N05/Dev | TODO |
| Supabase content_attribution table | P1 | N05/Dev | TODO |
| Supabase content_performance table | P1 | N05/Dev | TODO |
| Instagram Insights weekly export template | P1 | N06/Marketing | TODO |
| Package insert card design | P2 | N02/Design | TODO |
| Marketplace promo codes setup | P2 | N06 | TODO |
| Monthly attribution report template | P2 | N06 | Defined above |
| Instagram Graph API integration | P3 (Phase 2) | N05/Dev | FUTURE |
| GA4 BigQuery export | P3 (Phase 2) | N05/Dev | FUTURE |
