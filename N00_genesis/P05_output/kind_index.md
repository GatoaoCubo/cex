---
id: n00_p05_kind_index
kind: knowledge_card
pillar: P05
nucleus: n00
title: "P05 Output -- Kind Index"
version: 1.0
quality: null
tags: [index, p05, archetype, n00]
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Master index of all 23 kinds in pillar P05. Reference for /mentor, nucleus builders, and the 8F pipeline.

## Pillar: P05 Output
Production-ready artifacts for human consumption: landing pages, pitch decks, case studies, quickstart guides, onboarding flows, and press releases. Translates internal knowledge into external value.

## Kinds in P05

| Kind | Purpose | Primary Nucleus | Builder |
|------|---------|-----------------|---------|
| `analyst_briefing` | Gartner/Forrester/IDC analyst briefing deck with positioning, proof po | N03 | `analyst_briefing-builder` |
| `app_directory_entry` | App directory entry for FREE-tier discovery: tagline, screenshots, ins | N03 | `app_directory_entry-builder` |
| `case_study` | Customer case study with challenge/solution/outcome/quote narrative | N03 | `case_study-builder` |
| `code_of_conduct` | Community code of conduct (Contributor Covenant pattern) with reportin | N03 | `code_of_conduct-builder` |
| `contributor_guide` | OSS CONTRIBUTING.md spec: dev setup, PR flow, coding standards, review | N03 | `contributor_guide-builder` |
| `course_module` | Online course module with learning objectives and assessments | N03 | `course_module-builder` |
| `formatter` | Output formatter (json, md, yaml) | N03 | `formatter-builder` |
| `github_issue_template` | GitHub issue template (bug/feature/question) with required fields and  | N03 | `github_issue_template-builder` |
| `integration_guide` | Deep integration guide for platform partners and paid-tier onboarding | N03 | `integration_guide-builder` |
| `interactive_demo` | Interactive product demo script with guided-tour steps and talk track | N03 | `interactive_demo-builder` |
| `landing_page` | Complete production-ready landing page with 12 sections, responsive, d | N02 | `landing_page-builder` |
| `onboarding_flow` | User onboarding flow with activation milestones and aha-moment design | N03 | `onboarding_flow-builder` |
| `output_validator` | Validacao pos-LLM | N03 | `output_validator-builder` |
| `parser` | Output data extractor | N03 | `parser-builder` |
| `partner_listing` | Partner directory listing for SI/reseller channels with tier, region,  | N03 | `partner_listing-builder` |
| `pitch_deck` | Sales pitch deck with problem/solution/traction/ask slide structure | N03 | `pitch_deck-builder` |
| `press_release` | Press release with AP-style headline, dateline, lede, quotes, boilerpl | N03 | `press_release-builder` |
| `pricing_page` | Pricing page artifact with tier comparison and conversion copy | N06 | `pricing_page-builder` |
| `product_tour` | In-app product tour walkthrough with step/tooltip/trigger spec | N03 | `product_tour-builder` |
| `quickstart_guide` | Quickstart guide artifact for product/API onboarding in under 5 minute | N03 | `quickstart_guide-builder` |
| `response_format` | LLM response format (how the agent responds) | N03 | `response_format-builder` |
| `streaming_config` | SSE, WebSocket, and chunked response streaming configuration for real- | N03 | `streaming_config-builder` |
| `user_journey` | End-to-end user journey map from awareness to conversion | N03 | `user_journey-builder` |

## Usage
```python
# Build any of these via 8F:
python _tools/cex_8f_runner.py "your intent" --kind {kind} --execute
```

## CoC Hierarchy Note
These 23 kinds follow the convention-over-configuration hierarchy: each instance
(N01-N07) inherits this schema and fills the variables for its sin lens.
N00_genesis holds the canonical archetype; nuclei hold the instantiated versions.
