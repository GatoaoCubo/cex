---
kind: instruction
id: bld_instruction_press_release
pillar: P03
llm_function: REASON
purpose: Step-by-step construction instructions for producing AP-style press releases
quality: 9.1
title: "Press Release Builder Instructions"
version: "1.0.0"
author: n02_wave6
tags: [press_release, builder, instruction]
tldr: "Three-phase build protocol: research the news hook, compose in AP style, validate all gates"
domain: "press_release construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_press_release
  - p05_qg_press_release
  - p03_sp_press_release_builder
  - bld_schema_press_release
  - bld_tools_press_release
  - bld_knowledge_card_press_release
  - bld_collaboration_press_release
  - bld_examples_press_release
  - p10_lr_press_release_builder
  - kc_press_release
---

## Phase 1: RESEARCH

Before writing a single word, gather all required inputs.

| Step | Action | Required output |
|---|---|---|
| 1.1 | Identify the news hook -- what has changed or happened? | One-sentence news fact |
| 1.2 | Identify target audience and relevant publications | Publication list + beat |
| 1.3 | Gather at least one attributed quote from a named executive | Full name, title, company |
| 1.4 | Collect approved boilerplate from brand config or client | Paragraph, 50-100 words |
| 1.5 | Confirm embargo date or "FOR IMMEDIATE RELEASE" status | Date + time + timezone or none |
| 1.6 | Confirm media contact details (name, email, phone) | Contact block data |
| 1.7 | Verify all 5 Ws are answerable: Who, What, When, Where, Why | Checklist |

If any required input is missing, stop and request it. Do not fabricate quotes
or boilerplate. Do not proceed to Phase 2 without a confirmed news hook.

## Phase 2: COMPOSE

Write the press release in strict AP style, inverted pyramid structure.

| Section | Rules | Word target |
|---|---|---|
| Embargo / Release line | Line 1. Either "FOR IMMEDIATE RELEASE" or "EMBARGOED UNTIL: [Date, Time TZ]" | 5-8 words |
| Headline | ALL CAPS. Active voice. Under 80 characters. No verb-less fragments. | 8-15 words |
| Dateline | CITY, State, Date -- (two hyphens). City in CAPS. AP state abbreviation. | One line |
| Lede | Answers all 5 Ws in one sentence. Most newsworthy fact first. | Under 35 words |
| Body paragraph 1 | Expands the lede with supporting details. No new headlines buried here. | 60-80 words |
| Body paragraph 2 | Secondary context: market background, product details, timeline. | 60-80 words |
| Quote block | One or two quotes. Attribution: "said [First Last], [Title] at [Company]." | 30-50 words/quote |
| ### (end mark) | Three hash symbols on their own line. Signals end of editorial content. | 1 line |
| About boilerplate | Standard company description. Present tense. Third person. | 50-100 words |
| Media Contact | Name, title, email, phone. One contact per release. | 4-5 lines |

AP style rules enforced during composition:

- Use "said" for attribution, not "stated," "remarked," or "noted"
- Spell out numbers one through nine; use numerals for 10 and above
- No Oxford comma
- Titles before names, not after: "Chief Executive Officer A. Smith" not "A. Smith, CEO"
- Dates: January 15, 2026 (spell out month, no st/nd/rd/th)
- Times: 10 a.m. EDT (not AM, not 10:00 AM)

## Phase 3: VALIDATE

Run all checks before delivering the press release.

| Gate | Check | Pass condition |
|---|---|---|
| AP style compliance | Read every sentence for style violations | Zero violations |
| Embargo line | Line 1 of document is release status | Present and correct |
| Headline | Character count, voice, case | Under 80 chars, active, ALL CAPS |
| Dateline | City in CAPS, AP state abbr, em-dash format | Present and formatted |
| Lede | Word count, 5 Ws present | Under 35 words, all 5 Ws |
| Quote attribution | Full name, full title, correct verb | "said [Name], [Title]" |
| End mark | ### present | Present on its own line |
| Boilerplate | Paragraph present, third person | Present, no first-person |
| Contact block | Name, email, phone all present | All three fields filled |
| Word count | Total body words | 300-500 words |

If any HARD gate fails, return to Phase 2 and correct before delivery.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_press_release]] | downstream | 0.48 |
| [[p05_qg_press_release]] | downstream | 0.43 |
| [[p03_sp_press_release_builder]] | related | 0.43 |
| [[bld_schema_press_release]] | downstream | 0.36 |
| [[bld_tools_press_release]] | downstream | 0.33 |
| [[bld_knowledge_card_press_release]] | upstream | 0.29 |
| [[bld_collaboration_press_release]] | downstream | 0.28 |
| [[bld_examples_press_release]] | downstream | 0.27 |
| [[p10_lr_press_release_builder]] | downstream | 0.27 |
| [[kc_press_release]] | upstream | 0.23 |
