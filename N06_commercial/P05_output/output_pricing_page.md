---
id: n06_output_pricing_page
kind: output_template
pillar: P05
title: "Pricing Page — HTML Responsive Template"
version: 1.0.0
created: 2026-04-01
author: n06_commercial
domain: brand-monetization
quality: 9.1
updated: 2026-04-07
tags: [output, brand, pricing, html, responsive, n06]
tldr: "HTML pricing page with 2-4 tiers, anchoring, social proof, FAQ, CTA per tier. Brazilian market: BRL, PIX, parcelamento. Uses brand_config colors and fonts."
density_score: 0.93
axioms:
  - "ALWAYS highlight middle tier as 'most popular' — anchoring increases Pro conversion by 20-40%."
  - "NEVER show more than 4 tiers — choice paralysis kills conversion."
  - "ALWAYS include PIX discount and parcelamento for Brazilian market."
linked_artifacts:
  primary: p01_kc_brand_monetization_models
  related: [n06_output_monetization_business_plan, p01_kc_commercial_nucleus, n06_output_brand_book]
---

# Pricing Page — {{BRAND_NAME}}

## Template Structure

```html
<!DOCTYPE html>
<html lang="{{BRAND_LANGUAGE}}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{BRAND_NAME}} — Preços</title>
  <style>
    :root {
      --primary: {{PRIMARY_HEX}};
      --secondary: {{SECONDARY_HEX}};
      --accent: {{ACCENT_HEX}};
      --bg: {{BG_HEX}};
      --fg: {{FG_HEX}};
      --surface: {{SURFACE_HEX}};
      --font-heading: '{{HEADING_FONT}}', sans-serif;
      --font-body: '{{BODY_FONT}}', sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--font-body);
      background: var(--bg);
      color: var(--fg);
      line-height: 1.6;
    }

    .pricing-header {
      text-align: center;
      padding: 4rem 1rem 2rem;
    }
    .pricing-header h1 {
      font-family: var(--font-heading);
      font-size: 2.5rem;
      margin-bottom: 0.5rem;
    }
    .pricing-header p {
      font-size: 1.2rem;
      opacity: 0.8;
      max-width: 600px;
      margin: 0 auto;
    }

    .pricing-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 2rem;
      padding: 2rem;
      max-width: 1200px;
      margin: 0 auto;
    }

    .pricing-card {
      background: var(--surface);
      border-radius: 12px;
      padding: 2rem;
      text-align: center;
      position: relative;
      border: 1px solid rgba(255,255,255,0.1);
    }
    .pricing-card.featured {
      border-color: var(--accent);
      transform: scale(1.05);
    }
    .pricing-card.featured::before {
      content: '{{FEATURED_BADGE}}';
      position: absolute;
      top: -12px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--accent);
      color: var(--bg);
      padding: 4px 16px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 600;
    }

    .tier-name {
      font-family: var(--font-heading);
      font-size: 1.5rem;
      margin-bottom: 0.5rem;
    }
    .tier-price {
      font-size: 3rem;
      font-weight: 700;
      color: var(--accent);
    }
    .tier-price small {
      font-size: 1rem;
      opacity: 0.7;
    }
    .tier-installment {
      font-size: 0.9rem;
      opacity: 0.7;
      margin-top: 0.25rem;
    }

    .tier-features {
      list-style: none;
      padding: 1.5rem 0;
      text-align: left;
    }
    .tier-features li {
      padding: 0.5rem 0;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .tier-features li::before { content: '✅ '; }
    .tier-features li.no::before { content: '❌ '; opacity: 0.4; }

    .cta-btn {
      display: block;
      background: var(--accent);
      color: var(--bg);
      text-decoration: none;
      padding: 1rem 2rem;
      border-radius: 8px;
      font-weight: 600;
      font-size: 1.1rem;
      margin-top: 1rem;
      transition: opacity 0.2s;
    }
    .cta-btn:hover { opacity: 0.9; }

    .social-proof {
      text-align: center;
      padding: 3rem 1rem;
      font-size: 1.1rem;
      opacity: 0.8;
    }

    .faq {
      max-width: 800px;
      margin: 0 auto;
      padding: 2rem;
    }
    .faq details {
      background: var(--surface);
      border-radius: 8px;
      margin-bottom: 0.5rem;
      padding: 1rem;
    }
    .faq summary {
      cursor: pointer;
      font-weight: 600;
    }

    @media (max-width: 768px) {
      .pricing-card.featured { transform: scale(1); }
      .pricing-header h1 { font-size: 1.8rem; }
      .tier-price { font-size: 2.2rem; }
    }
  </style>
</head>
<body>

  <section class="pricing-header">
    <h1>{{PRICING_HEADLINE}}</h1>
    <p>{{PRICING_SUBHEADLINE}}</p>
  </section>

  <section class="pricing-grid">
    <!-- TIER 1 -->
    <div class="pricing-card">
      <div class="tier-name">{{TIER_1_NAME}}</div>
      <div class="tier-price">{{BRAND_CURRENCY}} {{TIER_1_PRICE}}<small>/mês</small></div>
      <div class="tier-installment">ou {{TIER_1_ANNUAL}} /ano ({{TIER_1_DISCOUNT}}% off)</div>
      <ul class="tier-features">
        <li>{{TIER_1_FEAT_1}}</li>
        <li>{{TIER_1_FEAT_2}}</li>
        <li>{{TIER_1_FEAT_3}}</li>
        <li class="no">{{TIER_1_NO_1}}</li>
      </ul>
      <a href="{{TIER_1_URL}}" class="cta-btn">{{TIER_1_CTA}}</a>
    </div>

    <!-- TIER 2 (Featured) -->
    <div class="pricing-card featured">
      <div class="tier-name">{{TIER_2_NAME}}</div>
      <div class="tier-price">{{BRAND_CURRENCY}} {{TIER_2_PRICE}}<small>/mês</small></div>
      <div class="tier-installment">ou {{TIER_2_ANNUAL}} /ano ({{TIER_2_DISCOUNT}}% off)</div>
      <ul class="tier-features">
        <li>{{TIER_2_FEAT_1}}</li>
        <li>{{TIER_2_FEAT_2}}</li>
        <li>{{TIER_2_FEAT_3}}</li>
        <li>{{TIER_2_FEAT_4}}</li>
      </ul>
      <a href="{{TIER_2_URL}}" class="cta-btn">{{TIER_2_CTA}}</a>
    </div>

    <!-- TIER 3 (Anchor) -->
    <div class="pricing-card">
      <div class="tier-name">{{TIER_3_NAME}}</div>
      <div class="tier-price">{{BRAND_CURRENCY}} {{TIER_3_PRICE}}<small>/mês</small></div>
      <div class="tier-installment">ou {{TIER_3_ANNUAL}} /ano ({{TIER_3_DISCOUNT}}% off)</div>
      <ul class="tier-features">
        <li>{{TIER_3_FEAT_1}}</li>
        <li>{{TIER_3_FEAT_2}}</li>
        <li>{{TIER_3_FEAT_3}}</li>
        <li>{{TIER_3_FEAT_4}}</li>
        <li>{{TIER_3_FEAT_5}}</li>
      </ul>
      <a href="{{TIER_3_URL}}" class="cta-btn">{{TIER_3_CTA}}</a>
    </div>
  </section>

  <section class="social-proof">
    <p>{{SOCIAL_PROOF_TEXT}}</p>
  </section>

  <section class="faq">
    <h2>Perguntas Frequentes</h2>
    <details><summary>{{FAQ_1_Q}}</summary><p>{{FAQ_1_A}}</p></details>
    <details><summary>{{FAQ_2_Q}}</summary><p>{{FAQ_2_A}}</p></details>
    <details><summary>{{FAQ_3_Q}}</summary><p>{{FAQ_3_A}}</p></details>
    <details><summary>Aceita PIX?</summary><p>Sim! PIX com desconto de {{PIX_DISCOUNT}}%.</p></details>
    <details><summary>Tem parcelamento?</summary><p>Sim, em até {{MAX_PARCELAS}}x sem juros no cartão.</p></details>
  </section>

</body>
</html>
```

## Usage Notes

1. All `{{BRAND_*}}` variables from brand_config.yaml
2. Tier-specific variables filled by N06 Revenue Engineer
3. Responsive: mobile-first, breakpoint at 768px
4. Brazilian market: BRL, PIX discount, parcelamento FAQ
5. Anchoring: Tier 3 price makes Tier 2 look affordable
6. Featured badge draws eye to recommended tier
