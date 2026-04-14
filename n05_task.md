---
id: kc_product_tour
kind: knowledge_card
title: Product Tour: In-App Walkthrough Guide
version: 1.0.0
quality: null
pillar: P01
---

# Product Tour Specifications

## Overview
An in-app product tour guides users through core features via contextual tooltips and interactive steps. Tours are triggered by user actions or system events.

## Purpose
1. Onboard new users to key functionality
2. Reinforce feature discovery for existing users
3. Reduce support inquiries about feature locations

## Step/Tooltip/Trigger Specifications
- **Step 1**: Welcome message with tour activation button  
  - Tooltip: "Explore our platform's core features"  
  - Trigger: First app launch after 30 seconds of inactivity  
  - Phase: `discover`  
  - Quality Gate: H01_phases_defined (ensure tour steps are not empty)

- **Step 2**: Feature highlight (e.g., dashboard overview)  
  - Tooltip: "This is your central hub for managing all features"  
  - Trigger: User clicks on the dashboard icon  
  - Phase: `execute`  
  - Quality Gate: H02_trigger_valid (validate trigger matches user action)

- **Step 3**: Navigation menu tutorial  
  - Tooltip: "Access settings, help, and account management here"  
  - Trigger: User opens the hamburger menu  
  - Phase: `configure`  
  - Quality Gate: H03_input_schema (ensure tooltip follows schema constraints)

- **Step 4**: Quick action tutorial (e.g., create new project)  
  - Tooltip: "Create projects with one click"  
  - Trigger: User clicks the "New Project" button  
  - Phase: `validate`  
  - Quality Gate: H04_output_format (ensure tooltip uses structured output)

## Best Practices
- Use animated arrows to indicate interaction points  
- Keep tooltips concise (max 3 sentences)  
- Allow users to skip or close the tour at any time  
- Track completion rates for feature adoption analysis  
- Align with [phases lifecycle](p04_kc_phases) for structured execution  

## Integration
- Leverage [API endpoints](kc_api_reference) for tracking tour completion  
- Use [steps framework](p04_kc_steps) for structured review workflows  
- Follow [quality gates](p04_kc_phases#quality-gates) for validation  
