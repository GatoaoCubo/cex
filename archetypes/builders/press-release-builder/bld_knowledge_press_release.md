---
kind: knowledge_card
id: bld_knowledge_card_press_release
pillar: P01
llm_function: INJECT
purpose: Domain knowledge on press release construction, AP style, and wire service distribution
quality: 9.1
title: "Press Release Knowledge Card"
version: "1.0.0"
author: n02_wave6
tags: [press_release, builder, knowledge_card]
tldr: "AP Stylebook conventions, wire service requirements, and earned media fundamentals for press release construction"
domain: "press_release construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_press_release_builder
  - press-release-builder
  - bld_collaboration_press_release
  - bld_tools_press_release
  - bld_instruction_press_release
  - p10_lr_press_release_builder
  - bld_output_template_press_release
  - p05_qg_press_release
  - bld_architecture_press_release
  - bld_config_press_release
---

## Domain Overview

A press release is the primary earned media instrument for announcing
newsworthy events to journalists, editors, and wire service subscribers.
Unlike paid advertising, a press release succeeds only if a journalist
independently decides it is worth covering -- making AP Stylebook compliance
and inverted pyramid structure non-negotiable, not stylistic preferences.

The Associated Press Stylebook (AP Stylebook) is the de facto editorial
standard for U.S. press releases. Wire services including PR Newswire,
BusinessWire, and GlobeNewswire publish formatting guidelines that derive
directly from AP style. Journalists trained in any U.S. newsroom expect
AP style; deviations signal an amateur sender and reduce pickup rates.

Distribution channels: direct pitch (email to specific reporter), newswire
(PR Newswire, BusinessWire), social distribution (Business Wire Social),
and owned media (company newsroom/press page).

## Key Concepts

| Concept | Definition | Source |
|---|---|---|
| Dateline | The city and date that appear before the lede, identifying where and when the news originates. Format: CITY, State, Date -- | AP Stylebook, "datelines" entry |
| Lede | The opening sentence of a news story or press release, containing the most newsworthy fact. Must answer who, what, when, where, why. Limit: 35 words. | AP Stylebook, "lede" entry |
| Inverted Pyramid | Story structure that places the most important information first, followed by supporting detail, with least critical content last. Survives editing from the bottom up. | Journalism 101 convention |
| Boilerplate | Standardized paragraph describing the company, placed after the ### end mark. Purpose: give journalists company context without requiring them to research. | PR Newswire submission guidelines |
| Embargo | Agreement that the release will not be published before a specified date and time. Must be stated explicitly on line 1. No legal enforceability; relies on journalist honor. | PR industry convention |
| Wire Service | Subscription distribution service (PR Newswire, BusinessWire, GlobeNewswire) that syndicates press releases to newsrooms, online databases, and financial terminals. | PR industry |
| 5 Ws | Who, What, When, Where, Why -- the five questions that the lede must answer. A lede missing any W invites journalist follow-up or discard. | AP Stylebook |
| ### (end mark) | Three hash marks on their own line. Signals to editors and wire systems that editorial content ends here. Content below (boilerplate, contact) is reference material. | Wire service standard |
| Attribution verb | The verb connecting a quote to its speaker. AP style: always "said." Never "stated," "remarked," "exclaimed," "noted," or "shared." | AP Stylebook, "attribution" entry |

## Industry Standards

| Standard | Authority | Key requirements |
|---|---|---|
| AP Stylebook 2024 | Associated Press | Attribution verbs, number rules, title format, state abbreviations, date format, time format |
| PR Newswire submission | Cision/PR Newswire | Minimum 400 characters; boilerplate required; headline under 170 chars (their system); contact block required |
| BusinessWire guidelines | Berkshire Hathaway | HTML-compatible formatting; multimedia supported; ###  end mark required; embargo honored |
| GlobeNewswire guidelines | Notified/GlobeNewswire | PDF and Word submission; embargo scheduling via portal; media contact with phone required |

## Common Patterns

| Pattern | When to use | Example |
|---|---|---|
| Product launch | New product or feature announcement | "COMPANY_NAME Launches PRODUCT for TARGET_AUDIENCE" |
| Funding announcement | Venture or debt financing round | "COMPANY_NAME Raises $AMOUNT SERIES Led by FIRM" |
| Partnership announcement | Strategic alliance or OEM deal | "COMPANY_A and COMPANY_B Partner to OUTCOME" |
| Executive appointment | C-suite or VP hire | "COMPANY_NAME Names EXEC_NAME as TITLE" |
| Award / recognition | Industry award or ranking | "COMPANY_NAME Named to LIST for DISTINCTION" |

## Pitfalls

| Pitfall | Why it hurts | Fix |
|---|---|---|
| Marketing language in lede | "Best-in-class solution" is not news. Journalists delete marketing copy. | Replace with a specific, verifiable fact. |
| Passive headline | "Award Is Announced by Company" buries the subject and weakens the hook. | Rewrite: active verb + subject + news. |
| Unattributed quote | Quote with no speaker name cannot be used by a journalist -- it is fabricated until proven. | Every quote must have first name, last name, full title, company. |
| Missing embargo on line 1 | If an embargo date exists anywhere but line 1, some systems ignore it and publish immediately. | Move embargo notice to the first line of the document. |
| Boilerplate in first person | "We are a leading provider..." is unpublishable. Journalists copy boilerplate verbatim. | Rewrite in third person: "COMPANY_NAME is a leading provider..." |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_press_release_builder]] | downstream | 0.57 |
| [[press-release-builder]] | downstream | 0.55 |
| [[bld_collaboration_press_release]] | downstream | 0.44 |
| [[bld_tools_press_release]] | downstream | 0.43 |
| [[bld_instruction_press_release]] | downstream | 0.39 |
| [[p10_lr_press_release_builder]] | downstream | 0.34 |
| [[bld_output_template_press_release]] | downstream | 0.30 |
| [[p05_qg_press_release]] | downstream | 0.30 |
| [[bld_architecture_press_release]] | downstream | 0.28 |
| [[bld_config_press_release]] | downstream | 0.28 |
