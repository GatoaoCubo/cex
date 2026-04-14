---
id: bld_knowledge_card_landing_page
kind: knowledge_card
pillar: P01
builder: landing-page-builder
version: 1.0.0
quality: 9.0
title: "Knowledge Card Landing Page"
author: n03_builder
tags: [landing_page, builder, examples]
tldr: "Golden and anti-examples for landing page construction, demonstrating ideal structure and common pitfalls."
domain: "landing page construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: INJECT
---
# Knowledge Card: Landing Page

## What is a Landing Page?
A landing page is a standalone web page designed for a single conversion goal.
Unlike a full website with navigation, a landing page focuses the visitor on ONE action:
sign up, buy, download, or schedule.

## Section Psychology
| Section | Purpose | Conversion Role |
|---------|---------|-----------------|
| Hero | First impression, value prop | Hook (3-second decision) |
| Problem | Empathy, "they understand me" | Pain amplification |
| Solution | Relief, "this fixes it" | Promise |
| Features | Rational justification | Logic backup |
| Social Proof | Trust, "others trust this" | Risk reduction |
| How It Works | Simplicity, "it's easy" | Objection handling |
| Pricing | Decision, "what does it cost" | Value framing |
| Testimonials | Stories, "people like me" | Social validation |
| FAQ | Objections, "but what about..." | Final objection clearing |
| CTA | Urgency, "do it now" | Conversion trigger |

## Conversion Best Practices
- Above fold: headline + sub + CTA visible without scroll
- One CTA per section (repeated but consistent)
- F-pattern reading for desktop, single-column for mobile
- Visual hierarchy: largest text = most important message
- White space > clutter (breathing room increases comprehension)
- Loading speed: every 100ms delay = -7% conversion (Google data)

## Stack Comparison
| Stack | Build Step | Best For | Deploy |
|-------|-----------|----------|--------|
| HTML + Tailwind CDN | None | Quick pages, non-devs | Any static host |
| React + Tailwind | npm build | Existing React apps | Vercel, Netlify |
| Next.js | next build | SEO-critical, SSR needed | Vercel |
| Astro | astro build | Multi-page, content-heavy | Any static host |

## Competitors We Replace
| Tool | What they do | What we do differently |
|------|-------------|----------------------|
| Lovable | AI builds web apps from prompts | We give you the CODE, not a platform lock |
| Bolt.new | AI generates full-stack apps | We focus on conversion-optimized pages |
| v0.dev | AI generates UI components | We build COMPLETE pages, not components |
| Framer | Visual page builder | We produce code you own and modify |
| Webflow | No-code page builder | We produce portable HTML/React, no vendor lock |
