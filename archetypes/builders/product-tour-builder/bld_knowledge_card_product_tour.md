---
kind: knowledge_card
id: bld_knowledge_card_product_tour
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for product_tour production
quality: 9.2
title: "Knowledge Card Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, knowledge_card]
tldr: "Domain knowledge for product_tour production"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview
Product tours are guided experiences embedded within software interfaces to highlight features, reduce cognitive load, and accelerate feature discovery. Unlike onboarding flows (focused on activation) or sales demos (interactive and scenario-based), product tours prioritize contextual education through tooltips, modals, and step-by-step guidance. They are commonly used in SaaS applications to surface underutilized features, improve user retention, and align product usage with business goals. Effective tours balance visibility with intrusiveness, leveraging principles from UX design and cognitive psychology to minimize friction.

## Key Concepts
| Concept | Definition | Source |
|---|---|---|
| Progressive Disclosure | Revealing information incrementally to avoid overwhelming users | Nielsen, 1993 |
| Trigger Event | User action (e.g., clicking a button) that initiates a tour step | UX Design Patterns (Baymard Institute) |
| Tooltip Microinteraction | Brief, contextual UI feedback to guide user attention | Material Design Guidelines |
| Skip/Close Mechanism | Optional exit point for users who already know the feature | WCAG 2.1 (Accessibility) |
| Sequential Progress | Visual indicator of tour completion (e.g., numbered steps) | UX Booth (2020) |
| Scaffolding | Temporary UI elements that fade as user proficiency increases | Educational Psychology (Hattie & Timperley, 2007) |
| Visual Highlighting | Use of color, borders, or animation to draw attention to UI elements | Nielsen Norman Group |
| Tour Context | Alignment of tour content with user role (e.g., admin vs. end-user) | UXmatters (2018) |

## Platform Patterns (In-App Tour Platforms)
| Platform | Trigger Model | Key Pattern |
|---|---|---|
| Pendo | Event-based (page load, feature flag) | Tooltip + spotlight + beacon; embedded analytics |
| Appcues | Condition-based flows | Multi-step checklists; NPS integration |
| WalkMe | DOM-selector overlay | Enterprise; deep customization; SmartTip |
| Intercom Product Tours | User segment triggers | Lightweight; best for conversational onboarding |

## Trigger Anatomy
| Trigger Type | When to Use | Example Condition |
|---|---|---|
| entry | First time on page or feature | `user.feature_seen_count == 0` |
| scroll | Deep engagement signal | `scroll_depth >= 60%` |
| click | Post-action context | `button#export clicked` |
| feature_flag | Controlled rollout | `flag.new_dashboard == true` |
| inactivity | Re-engagement nudge | `idle_seconds >= 30` |

## Activation Metrics (time-to-value)
The primary KPI for any product tour is time-to-value (TTV): how quickly a new user reaches their first "aha moment".
- Measure: steps-to-aha / time-to-aha / completion-rate per step
- Empty-state coaching: tours triggered when a feature has no data yet ("Add your first item to get started")
- Benchmark: TTV reduction of 20-40% is typical for well-designed tours (Appcues 2023 report)

## Industry Standards
- W3C ARIA (Accessible Rich Internet Applications) standards
- Nielsen Norman Group 10 Usability Heuristics (1994)
- WCAG 2.1 AA (tooltip contrast, keyboard focus, skip mechanism)
- Material Design Tour component specification (Google, 2021)
- Pendo Product Analytics Benchmarks (2023)

## Common Patterns
1. Step-based Navigation: Linear progression through pre-defined feature highlights.
2. Trigger-based Activation: Tours initiate based on user behavior (e.g., first-time login).
3. Tooltip Microinteractions: Subtle animations to emphasize UI elements during tours.
4. Skip/Close Options: Allow users to bypass tours if they’re already familiar with features.
5. Visual Highlighting: Use of borders, color, or motion to focus attention on key elements.

## Pitfalls
- Overloading tours with too many steps, leading to user fatigue.
- Poor trigger timing (e.g., interrupting critical workflows).
- Ignoring accessibility standards (e.g., lack of keyboard navigation).
- Hardcoding tour content without localization or role-based customization.
- Failing to align tour goals with user personas or business KPIs.
