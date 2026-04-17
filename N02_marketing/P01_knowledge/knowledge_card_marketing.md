---
id: knowledge_card_marketing
kind: knowledge_card
pillar: P01
nucleus: N02
title: "Knowledge Card -- Marketing Domain (N02)"
version: "2.0.0"
quality: 9.1
density_score: 0.99
tags: [knowledge_card, marketing, copy, campaign, brand, n02, creative_lust]
domain: marketing
tldr: "Canonical knowledge base for N02: copy theory, campaign structure, channel mix, conversion mechanics, quality gates."
created: "2026-04-17"
updated: "2026-04-17"
---
<!-- 8F: F1=knowledge_card/P01 F2=knowledge-card-builder F3=kc_marketing_vocabulary+kc_campaign+nucleus_def_n02 F4=full_domain_coverage F6=structured_tables F7=9.1/10 F8=N02_marketing/P01_knowledge/knowledge_card_marketing.md -->

# Marketing Domain -- N02 Knowledge Card

## Domain Identity

| Property | Value |
|----------|-------|
| Nucleus | N02 -- Marketing |
| Sin lens | Creative Lust *(Luxuria Criativa)* |
| Core drive | Make the reader WANT, not just KNOW |
| Quality floor | 9.0 |
| Density target | 0.85+ |

---

## 1. Copy Theory

Marketing copy converts attention into action. N02 applies three laws:

| Law | Principle | Failure mode |
|-----|-----------|-------------|
| Desire before logic | Emotion opens the door; reason locks the deal | Pure feature list = ignored |
| Specificity beats superlatives | "23% lift in demos" > "best results ever" | Vague claims erode trust |
| One CTA per unit | Clarity of action = higher conversion | Multiple CTAs = decision paralysis |

### Persuasion architecture (AIDA+)

```
Attention -> Interest -> Desire -> Action -> Retention
     |              |          |         |
  headline      proof      urgency     CTA      loop
```

Every piece of copy N02 produces maps to at least one AIDA+ stage.

---

## 2. Campaign Structure

### Anatomy of a campaign

| Component | Function | Artifact |
|-----------|----------|---------|
| Brief | audience + offer + proof + constraints | input_schema_campaign_brief |
| Copy variants | 3+ angle variants per asset | prompt_template_marketing |
| Distribution plan | channel x timing x audience | tpl_content_distribution_plan |
| Quality gate | score >= 9.0 before publish | quality_gate_marketing |
| Signal | campaign_complete -> N06/N07 | dispatch_rule_marketing |

### Funnel stage vocabulary

| Stage | Audience state | Copy job | Banned |
|-------|---------------|----------|--------|
| TOFU | Problem-unaware | Educate, frame pain | Hard CTAs |
| MOFU | Solution-aware | Differentiate, prove | Vague claims |
| BOFU | Decision-ready | Remove risk, close | "Maybe", "might" |

---

## 3. Channel Mix

| Channel | Format | Max length | Primary metric |
|---------|--------|-----------|----------------|
| LinkedIn (B2B) | post + carousel | 3,000 chars | impressions -> connections |
| Instagram (D2C) | caption + reel | 2,200 chars | saves + shares |
| Email | subject + body | 40 chars subject | open rate + click |
| Landing page | full page | above-fold CTA | conversion rate |
| Blog | SEO post | 1,500+ words | organic traffic |

---

## 4. Conversion Mechanics

### Copy quality indicators (measurable)

| Indicator | Target | Tooling |
|-----------|--------|---------|
| Specific proof present | >= 1 stat or testimonial | copy_analyzer.md |
| CTA present | exactly 1 per unit | quality_gate_marketing |
| Brand voice match | 80%+ vocabulary overlap | brand_voice_templates.md |
| Readability | Flesch >= 60 | headline_scorer.md |
| Hook in first 2 sentences | yes | copy_analyzer.md |

### Headline scoring model

| Score range | Signal | Action |
|------------|--------|--------|
| 9.0-10 | Publish | -- |
| 8.0-8.9 | Improve one element | add proof OR sharpen CTA |
| 7.0-7.9 | Major revision | rewrite hook |
| < 7.0 | Discard | rebuild from brief |

---

## 5. Brand Voice System

N02 loads brand context from `.cex/brand/brand_config.yaml` at F3 INJECT:

| Brand field | Marketing use |
|-------------|---------------|
| BRAND_VOICE | Tone and personality for all copy |
| BRAND_PRIMARY_COLOR | Anchor for visual copy decisions |
| BRAND_VERTICAL | Industry language and norms |
| BRAND_PERSONA_SEED | Character consistency for persona prompts |

Without brand config, N02 defaults to generic copy. Brand config = the difference between
copy that sounds like the company and copy that could belong to anyone.

---

## 6. Content Factory Patterns

### Q2 pipeline (91 IG + 26 blog)

| Template type | Volume | Kind | Nucleus |
|---------------|--------|------|---------|
| Instagram caption | 91 | prompt_template | N02 |
| Blog post brief | 26 | prompt_template | N02 |
| Editorial calendar | 1 | schedule | N02 |
| Publishing workflow | 1 | workflow | N02/N05 |

### Media kit generation

```
product brief -> persona prompt -> media kit copy -> generate-media-kit workflow
```

Media kits always include: brand origin, founder story, audience profile, press stats, contact.

---

## 7. Quality Gates (N02-specific)

| Gate | Check | Fail action |
|------|-------|-------------|
| H01 Brief completeness | audience + offer + proof all present | request missing fields |
| H02 No banned hype | no "best", "amazing", "revolutionary" | replace with specifics |
| H03 CTA presence | exactly 1 clear CTA | add or consolidate |
| H04 Brand voice match | matches brand_config.yaml tone | rewrite with brand lens |
| H05 Stage alignment | copy stage matches funnel intent | shift vocabulary |
| H06 Proof discipline | at least 1 concrete evidence point | request proof or add placeholder |

---

## 8. Cross-Nucleus Interfaces

| Nucleus | N02 consumes | N02 produces |
|---------|--------------|--------------|
| N01 | competitor_analysis_brief, market_data | -- |
| N03 | component_map, design_tokens | -- |
| N05 | social_publisher_config, webhook events | publish requests |
| N06 | pricing_tier specs, monetization briefs | sales copy, landing pages |
| N07 | handoff + decisions manifest | signal_complete with quality score |

---

## Anti-Patterns

| Anti-pattern | Why it fails |
|-------------|-------------|
| "Write good copy for our product" | No brief = no strategy = no conversion |
| All variants share same angle | A/B tests need distinct hypotheses |
| Copy produced without brand config | Generic voice alienates loyal audience |
| Quality gate skipped | Publish-ready == 9.0, not "looks okay" |
| Proof added as afterthought | Suspicion persists when proof is bolted on |
