---
id: p12_wf_marketing_campaign
kind: workflow
pillar: P12
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: n02_marketing
title: Marketing Copy Production Workflows
steps_count: 12
execution: sequential_with_branches
agent_nodes: [n02-marketing-hub, n07-orchestrator]
timeout: 3600000
retry_policy: per_step
depends_on: []
signals: [marketing_copy_complete, marketing_copy_error]
domain: copywriting_and_campaigns
quality: null
tags: [workflow, marketing, copywriting, N02, campaign, landing_page, email]
tldr: 3 production workflows — ad campaign (5 steps), landing page (4 steps), email sequence (3 steps) — all N02 executed.
density_score: 0.90
---

# Marketing Copy Production Workflows

## Overview

Three operational workflows for N02. Each produces committed, compiled artifacts
with quality gate validation. All execute on `n02-marketing-hub` (claude-sonnet-4-6).

---

## Workflow 1: Ad Campaign

**Goal**: Produce complete ad creative set for one campaign (Facebook/Google/LinkedIn)
**Input required**: Product name, audience segment, key benefit, budget range, campaign objective
**Output**: Campaign brief + 3 ad variants per format (image/video/carousel) + copy deck

### Steps

```
Step 1: BRIEF [n02-marketing-hub]
  - Input: product/audience/goal from handoff
  - Action: Write campaign brief (objective, audience, key message, channels, KPIs)
  - Output: campaign_brief_{mission}.md
  - Signal: brief_complete

Step 2: AUDIENCE [n02-marketing-hub]
  - Input: campaign brief
  - Action: Define 3 audience segments with pain points and desire statements
  - Output: audience_profile_{mission}.md
  - Signal: audience_complete

Step 3: HEADLINES [n02-marketing-hub]
  - Input: audience profiles + key benefit
  - Action: Generate 10 headline variants per segment (score with 4U formula)
  - Top 3 per segment advance; output: headlines_{mission}.md
  - Signal: headlines_complete

Step 4: AD COPY [n02-marketing-hub]
  - Input: top headlines + audience profiles
  - Action: Write full ad copy (hook + body + CTA) for each format — 3 A/B variants
  - Output: ad_copy_{mission}.md
  - Depends on: Steps 2, 3
  - Signal: copy_complete

Step 5: COMPILE + COMMIT [n02-marketing-hub]
  - Action: Compile all artifacts, git add + commit, write signal
  - Command: git commit -m "[N02] ad campaign copy — {mission}"
  - Signal: marketing_copy_complete
```

---

## Workflow 2: Landing Page Copy

**Goal**: Produce full landing page copy for a product or offer
**Input required**: Product, audience, offer, primary CTA, optional testimonials
**Output**: Complete LP copy file with all sections

### Steps

```
Step 1: RESEARCH [n02-marketing-hub]
  - Action: If markitdown/fetch available, pull competitor LP for teardown
  - Output: competitor_notes_{mission}.md (optional)
  - Fallback: proceed from KC formulas if no web access

Step 2: HERO SECTION [n02-marketing-hub]
  - Action: Write headline (10 variants, top 3 selected) + subhead + hero CTA
  - Apply: 4U formula scoring; select variant with highest score
  - Output: lp_hero_{mission}.md

Step 3: BODY COPY [n02-marketing-hub]
  - Sections to write:
    a. Problem/Agitate block (PAS formula — 150 words)
    b. Solution intro (2 sentences, transformation language)
    c. Benefits block (FAB format — 5–7 bullets)
    d. Social proof section (3 testimonial slots with [NAME] [COMPANY] placeholders)
    e. Objection-busting FAQ (5 questions, direct answers)
    f. Final CTA section (urgency + benefit restatement + button copy)
  - Output: lp_body_{mission}.md

Step 4: COMPILE + COMMIT [n02-marketing-hub]
  - Merge hero + body into lp_complete_{mission}.md
  - Run readability check (target Flesch >= 60)
  - Compile: python _tools/cex_compile.py
  - Commit: git commit -m "[N02] landing page copy — {mission}"
  - Signal: marketing_copy_complete
```

---

## Workflow 3: Email Sequence

**Goal**: Produce a 5-email nurture or cold outreach sequence
**Input required**: Audience, goal (nurture/cold/cart/re-engagement), product/offer
**Output**: 5 emails with subject lines, preview text, and body copy

### Steps

```
Step 1: SEQUENCE PLAN [n02-marketing-hub]
  - Input: goal type (nurture | cold | cart | re-engagement)
  - Action: Select skeleton from KC, map each email to objective
  - Output: email_plan_{mission}.md
  - Signal: plan_complete

Step 2: EMAIL COPY [n02-marketing-hub]
  - For each email (1–5):
    - Write subject line (3 variants, select best by curiosity gap)
    - Write preview text (40–90 chars)
    - Write email body (formula-matched per email type)
    - Write CTA (specific + benefit-first)
  - Output: email_sequence_{mission}.md
  - Depends on: Step 1
  - Signal: copy_complete

Step 3: COMPILE + COMMIT [n02-marketing-hub]
  - Compile sequence file
  - Commit: git commit -m "[N02] email sequence — {mission}"
  - Signal: marketing_copy_complete
```

---

## Error Handling

- **Step fails**: retry once with revised prompt; if still fail, signal `marketing_copy_error` to N07
- **Quality gate fails** (score < 8.0): return to copy step, apply F6 retry, max 2 revisions
- **MCP unavailable**: proceed with formula-based approach from KC; note in output

## Signals

| Signal | Emitter | Meaning |
|--------|---------|---------|
| marketing_copy_complete | n02-marketing-hub | All deliverables saved, compiled, committed |
| marketing_copy_error | n02-marketing-hub | Unrecoverable failure, escalate to N07 |
