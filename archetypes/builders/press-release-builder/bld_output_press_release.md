---
kind: output_template
id: bld_output_template_press_release
pillar: P05
llm_function: PRODUCE
purpose: Canonical markdown template for press_release artifacts in wire-service-ready format
quality: 9.1
title: "Press Release Output Template"
version: "1.0.0"
author: n02_wave6
tags: [press_release, builder, output_template]
tldr: "Wire-service-ready template with all required sections in correct AP order"
domain: "press_release construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_press_release
  - p05_qg_press_release
  - p03_sp_press_release_builder
  - bld_schema_press_release
  - bld_knowledge_card_press_release
  - bld_examples_press_release
  - bld_collaboration_press_release
  - bld_tools_press_release
  - p10_lr_press_release_builder
  - kc_press_release
---

## Usage Notes
Replace all `{{placeholder}}` tokens with real content before delivery.
Remove this Usage Notes section from the final artifact.
Embargo line: use ONE of the two options below, delete the other.
All CAPS sections remain in CAPS in the final artifact.

## Template
```
FOR IMMEDIATE RELEASE
EMBARGOED UNTIL: {{embargo_date}} {{embargo_time}} {{embargo_timezone}}

{{HEADLINE IN ALL CAPS, UNDER 80 CHARACTERS, ACTIVE VOICE}}

{{CITY}}, {{State Abbr.}}, {{Month DD, YYYY}} -- {{lede: one sentence answering
who, what, when, where, and why -- under 35 words total}}

{{body_paragraph_1: expand the lede with the most important supporting details.
Include product name, key features, availability date, or deal terms as relevant.
Target 60-80 words.}}

{{body_paragraph_2: provide secondary context -- market background, company
milestone, customer problem being solved, or industry significance.
Target 60-80 words.}}

"{{quote: a natural-sounding statement from the executive that adds perspective,
not marketing copy}}," said {{First Last}}, {{Full Title}} at {{Company Name}}.

"{{optional_second_quote: partner, customer, or second executive}}," said
{{First Last}}, {{Full Title}} at {{Company Name or Partner Org}}.

###

About {{Company Name}}:
{{boilerplate: 50-100 words in third person, present tense. Cover what the company
does, who it serves, when it was founded, and one key differentiator.}}

Media Contact:
{{contact_name}}
{{contact_title}}
{{contact_email}}
{{contact_phone}}
```

## Section Annotations
| Section | Annotation |
|---|---|
| Embargo / Release line | Mandatory line 1. Delete the line that does not apply. |
| Headline | Replace {{HEADLINE...}} with actual headline in ALL CAPS. |
| Dateline | {{CITY}} in ALL CAPS. {{State Abbr.}} per AP abbreviations (Calif., N.Y.). |
| Lede | Single sentence. If it exceeds 35 words, split or compress. |
| Body paragraphs | Two minimum. Do not add a third without hitting 300-word minimum first. |
| Quote block | Second quote is optional. First quote is required (H07 gate). |
| ### end mark | Do not change. Signals end of editorial content to wire services. |
| Boilerplate | Provided by client or brand config. Do not paraphrase -- use approved text. |
| Media Contact | One contact only. Do not list two contacts without user request. |

## AP State Abbreviations (Reference)
| State | AP abbr | State | AP abbr |
|---|---|---|---|
| California | Calif. | New York | N.Y. |
| Texas | Texas | Florida | Fla. |
| Illinois | Ill. | Massachusetts | Mass. |
| Washington | Wash. | Georgia | Ga. |

Note: Eight states are never abbreviated in AP style: Alaska, Hawaii, Idaho,
Iowa, Maine, Ohio, Texas, Utah.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_press_release]] | upstream | 0.55 |
| [[p05_qg_press_release]] | downstream | 0.39 |
| [[p03_sp_press_release_builder]] | upstream | 0.36 |
| [[bld_schema_press_release]] | downstream | 0.31 |
| [[bld_knowledge_card_press_release]] | upstream | 0.26 |
| [[bld_examples_press_release]] | downstream | 0.26 |
| [[bld_collaboration_press_release]] | downstream | 0.24 |
| [[bld_tools_press_release]] | upstream | 0.24 |
| [[p10_lr_press_release_builder]] | downstream | 0.21 |
| [[kc_press_release]] | upstream | 0.20 |
