---
id: p05_output_social_card
kind: output_validator
pillar: P05
title: "Social Media Card Templates"
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend
domain: frontend
quality: 9.1
tags: [output, template, social, og-image, tailwind]
tldr: "HTML/CSS card templates for og:image, Instagram, LinkedIn, Twitter — screenshot-renderable."
density_score: 0.88
---

# Social Media Card Templates

## Purpose
Generate social sharing cards as styled HTML, renderable to image via browser-mcp screenshot.
Each format has fixed dimensions matching platform requirements.

---

## Format Specifications

| Platform | Dimensions | Aspect Ratio | File |
|----------|-----------|--------------|------|
| Open Graph (og:image) | 1200 × 630 | 1.91:1 | og-card.html |
| Instagram Post | 1080 × 1080 | 1:1 | ig-card.html |
| LinkedIn Share | 1200 × 627 | 1.91:1 | li-card.html |
| Twitter/X Card | 1200 × 675 | 16:9 | tw-card.html |

## og:image Template (1200×630)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    .card {
      width: 1200px;
      height: 630px;
      background: linear-gradient(135deg, hsl(240 10% 5%) 0%, hsl(240 8% 15%) 100%);
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 80px;
      font-family: 'Inter', sans-serif;
      color: hsl(0 0% 95%);
      position: relative;
      overflow: hidden;
    }

    /* Accent glow */
    .card::before {
      content: '';
      position: absolute;
      top: -100px;
      right: -100px;
      width: 400px;
      height: 400px;
      background: radial-gradient(circle, rgba(80, 200, 120, 0.15) 0%, transparent 70%);
      border-radius: 50%;
    }

    .badge {
      display: inline-block;
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 14px;
      font-weight: 600;
      background: rgba(80, 200, 120, 0.15);
      color: #50C878;
      border: 1px solid rgba(80, 200, 120, 0.3);
      margin-bottom: 24px;
    }

    h1 {
      font-size: 56px;
      font-weight: 800;
      line-height: 1.1;
      margin-bottom: 20px;
      max-width: 800px;
    }

    .subtitle {
      font-size: 22px;
      color: hsl(0 0% 60%);
      max-width: 600px;
      line-height: 1.5;
    }

    .logo {
      position: absolute;
      bottom: 60px;
      right: 80px;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .logo-mark {
      width: 40px;
      height: 40px;
      background: #50C878;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 20px;
      color: #000;
    }

    .logo-text {
      font-size: 24px;
      font-weight: 700;
      letter-spacing: -0.02em;
    }
  </style>
</head>
<body>
  <div class="card">
    <span class="badge">{{BADGE_TEXT}}</span>
    <h1>{{HEADLINE}}</h1>
    <p class="subtitle">{{SUBTITLE}}</p>
    <div class="logo">
      <div class="logo-mark">C</div>
      <span class="logo-text">CODEXA</span>
    </div>
  </div>
</body>
</html>
```

## Instagram Square (1080×1080)

```html
<style>
  .card {
    width: 1080px;
    height: 1080px;
    background: linear-gradient(180deg, hsl(240 10% 5%) 0%, hsl(160 40% 10%) 100%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 100px;
  }
  h1 { font-size: 64px; margin-bottom: 32px; }
  .subtitle { font-size: 24px; }
  .logo { position: absolute; bottom: 80px; }
</style>
```

## Rendering to Image

```bash
# Via browser-mcp (Puppeteer)
# 1. Open HTML file in headless browser
# 2. Set viewport to exact dimensions
# 3. Screenshot as PNG
# 4. Optimize with sharp/squoosh

# Via CLI
npx puppeteer screenshot og-card.html --viewport 1200x630 --output og-card.png
```

## Template Variables

| Variable | Example | Used In |
|----------|---------|---------|
| `{{BADGE_TEXT}}` | "New Feature" | All formats |
| `{{HEADLINE}}` | "Automate Your E-commerce" | All formats |
| `{{SUBTITLE}}` | "AI-powered product listing..." | og, LinkedIn, Twitter |
| `{{LOGO_URL}}` | "/assets/logo.svg" | All formats |
| `{{GRADIENT_FROM}}` | "hsl(240 10% 5%)" | Background |
| `{{GRADIENT_TO}}` | "hsl(160 40% 10%)" | Background |
