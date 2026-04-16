---
kind: examples
id: bld_examples_product_tour
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of product_tour artifacts
quality: 9.0
title: "Examples Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, examples]
tldr: "Golden and anti-examples of product_tour artifacts"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
title: "Tour: Analytics Dashboard Features"
kind: product_tour
vendor: Pendo
description: "Guided walkthrough of key analytics dashboard features for new users"
---
**Steps:**
1. **Step 1: Filter Bar**
   - Trigger: User clicks "Add Filter" button
   - Tooltip: "Use this bar to narrow down data by date, region, or user segment"
2. **Step 2: Visualization Panel**
   - Trigger: User hovers over chart
   - Tooltip: "Click to edit chart type (bar, line, pie) or export as PNG"
3. **Step 3: Export Options**
   - Trigger: User clicks "Export" dropdown
   - Tooltip: "Download data as CSV, PDF, or share via email"
```

## Anti-Example 1: Confusing with onboarding_flow
```markdown
---
title: "Tour: First Login Setup"
kind: onboarding_flow
vendor: Intercom
description: "Walkthrough for completing user profile during first login"
---
**Steps:**
1. **Step 1: Name Input**
   - Trigger: User arrives at profile page
   - Tooltip: "Enter your full name to personalize your experience"
```
## Why it fails
Mixes product tour with onboarding_flow (activation). Product tours focus on feature discovery, not account setup.

## Anti-Example 2: Missing trigger logic
```markdown
---
title: "Tour: Collaboration Tools"
kind: product_tour
vendor: UserGuiding
description: "Showcase collaboration features"
---
**Steps:**
1. **Step 1: Comment Section**
   - Tooltip: "Add comments to specific data points for team discussion"
```
## Why it fails
No trigger defined - the tour cannot be activated automatically or contextually. Triggers are essential for timed or event-based tours.
