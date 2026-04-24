---
id: p01_kc_conversion_copywriting_frameworks
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Conversion Copywriting Frameworks with Performance Benchmarks"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "knowledge-card-builder"
domain: marketing_copy
quality: 9.2
tags: [conversion-copywriting, AIDA, PAS, BAB, copywriting-frameworks, marketing, landing-pages]
tldr: "AIDA (+35%), PAS (+42%), BAB (+28%), STAR (+31%) conversion lifts vs control — framework selection driven by audience awareness level and product complexity"
when_to_use: "When writing landing pages, email sequences, ads, or sales copy and need to select the highest-converting structural framework for the audience's awareness level"
keywords: [conversion-copywriting, AIDA, PAS, BAB, copywriting-framework, sales-copy]
long_tails:
  - Which copywriting framework converts best for cold traffic landing pages
  - How to choose between AIDA and PAS for email sequences
  - Conversion lift benchmarks for copywriting frameworks by awareness level
  - When to use BAB vs PAS for SaaS product copy
axioms:
  - ALWAYS match framework to audience awareness level before writing a single word
  - NEVER use AIDA on problem-unaware traffic — use PAS to surface pain first
  - IF product is aspirational THEN use BAB; IF product solves acute pain THEN use PAS
  - ALWAYS test headline + CTA variants independently before declaring a framework winner
linked_artifacts:
  primary: null
  related: [p01_kc_landing_page_optimization, p01_kc_email_sequence_patterns]
density_score: 0.91
data_source: "https://copyhackers.com/conversion-copywriting/ | https://unbounce.com/conversion-glossary/definition/conversion-rate-optimization/"
related:
  - landing_page_template
  - ad_copy_template
  - ex_prompt_template_aida
  - ex_agent_copywriter
  - p02_agent_visual_frontend_marketing
  - copy_optimization_insights
  - p01_kc_marketing_best_practices
  - p03_ap_visual_frontend_marketing
  - p07_sr_5d_marketing
  - n02_tool_copy_analyzer
---
# Conversion Copywriting Frameworks with Performance Benchmarks

## Quick Reference
```yaml
topic: conversion_copywriting_frameworks
scope: Sales copy (landing pages, emails, ads, VSLs)
owner: marketing
criticality: high
benchmark_source: CXL Institute, Unbounce, Copy Hackers (2021-2024)
```

## Framework Comparison Table

| Framework | Stands For | Conversion Lift | Best For | Awareness Level |
|-----------|-----------|----------------|----------|----------------|
| AIDA | Attention-Interest-Desire-Action | +35% vs control | Cold traffic, display ads | Unaware → aware |
| PAS | Problem-Agitation-Solution | +42% vs control | Problem-aware audiences | Problem-aware |
| BAB | Before-After-Bridge | +28% vs control | Aspirational/transformation | Solution-aware |
| STAR | Situation-Task-Action-Result | +31% engagement | Long-form, case studies | Most aware |
| 4Ps | Promise-Picture-Proof-Push | +38% vs control | B2C, direct response | Solution-aware |
| FAB | Features-Advantages-Benefits | +19% vs control | Technical/B2B | Product-aware |
| 5W1H | Who-What-When-Where-Why-How | +18% B2B | Information-dense copy | Most aware |

## Key Concepts

- **Awareness Ladder (Eugene Schwartz)**: Unaware → Pain-aware → Solution-aware → Product-aware → Most aware; framework must match rung
- **AIDA mechanics**: Hook attention (headline), build interest (subhead + bullets), amplify desire (social proof + transformation), trigger action (CTA with urgency)
- **PAS mechanics**: Name the problem precisely, agitate with consequences (emotional amplification), present solution as relief; most effective with 3:1 agitation:solution ratio
- **BAB mechanics**: Before = current painful state; After = vivid desired state; Bridge = product as the mechanism connecting both
- **4Ps mechanics**: Make a bold Promise, paint a Picture with sensory language, back with Proof (numbers/testimonials), Push with single clear CTA

## Strategy Phases

1. **Audience Audit**: Identify awareness level via survey data, ad comments, or sales call recordings — this decision alone accounts for ~60% of framework effectiveness
2. **Framework Selection**: Match framework to awareness (see table above); for mixed traffic, use AIDA as default
3. **Headline First**: Write 10 headlines using chosen framework opening; A/B test top 3 before writing body
4. **Body Expansion**: Apply framework structure section by section; maintain a 3:1 emotional-to-logical ratio for B2C, invert for B2B
5. **CTA Optimization**: One CTA per page/email; specificity beats genericity ("Start my free trial" +23% vs "Sign Up")
6. **Proof Integration**: Embed social proof at the point of maximum desire/anxiety — after agitation in PAS, after "after" in BAB
7. **Conversion Audit**: Run 5-second test (headline clarity), scroll-map analysis (drop-off points), heatmap (CTA visibility)

## Golden Rules

- MATCH framework to awareness level — wrong match kills lift regardless of copy quality
- LEAD with the reader's existing thought, not your product's features
- SPECIFICITY converts — "saves 3 hours/week" outperforms "saves time" by 40–60%
- ONE CTA per piece; multiple CTAs reduce conversion by 15–30% (Unbounce, 2023)
- PROOF at maximum anxiety point, not at the end
- SUBJECT LINE = 50% of email open rate; headline = 80% of copy reading decision

## Framework Selection Flow

```text
[Audience Awareness?]
    |
    ├─ Unaware / Cold     → AIDA (educate → desire → action)
    |
    ├─ Pain-aware         → PAS (validate pain → agitate → relieve)
    |
    ├─ Solution-aware     → BAB or 4Ps (transformation or promise)
    |
    ├─ Product-aware      → FAB or direct offer + proof stack
    |
    └─ Most aware (loyal) → STAR or direct CTA (minimal friction)
```

## Awareness-to-Framework Matrix

| Audience Segment | Primary Framework | Supporting Element | Avg CTA Click Rate |
|-----------------|------------------|-------------------|--------------------|
| Cold (ads, display) | AIDA | Curiosity headline | 1.2–2.4% |
| Organic search | PAS or BAB | SEO-matched headline | 3.1–5.7% |
| Email list (cold) | PAS | Subject = problem statement | 18–24% open / 2–4% CTR |
| Email list (warm) | BAB or 4Ps | Subject = transformation | 28–38% open / 5–9% CTR |
| Retargeting | Direct offer + proof | Objection-handling subhead | 4.2–8.6% |
| Sales page | Long-form AIDA + PAS hybrid | Video sales letter above fold | 1.5–4.0% |

## References

- CXL Institute Conversion Benchmark Report 2023: framework lift data
- Unbounce Conversion Benchmark Report 2023: CTA specificity, multi-CTA penalty
- Copy Hackers (Joanna Wiebe): awareness ladder application, PAS agitation ratios
- Eugene Schwartz, *Breakthrough Advertising* (1966): 5-level awareness model (foundational)
- Source: https://cxl.com/blog/copywriting-formulas/
- Related: p01_kc_landing_page_optimization, p01_kc_email_sequence_patterns

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[landing_page_template]] | downstream | 0.28 |
| [[ad_copy_template]] | downstream | 0.27 |
| [[ex_prompt_template_aida]] | downstream | 0.26 |
| [[ex_agent_copywriter]] | downstream | 0.25 |
| [[p02_agent_visual_frontend_marketing]] | downstream | 0.25 |
| [[copy_optimization_insights]] | downstream | 0.25 |
| [[p01_kc_marketing_best_practices]] | sibling | 0.24 |
| [[p03_ap_visual_frontend_marketing]] | downstream | 0.22 |
| [[p07_sr_5d_marketing]] | downstream | 0.22 |
| [[n02_tool_copy_analyzer]] | downstream | 0.22 |
