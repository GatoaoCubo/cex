---
kind: collaboration
id: bld_collaboration_press_release
pillar: P12
llm_function: COLLABORATE
purpose: Define crew role, upstream inputs, downstream outputs, and boundaries for press_release builder
quality: 9.2
title: "Press Release Builder Collaboration"
version: "1.0.0"
author: n02_wave6
tags: [press_release, builder, collaboration]
tldr: "Receives messaging from Brand/PR/Legal; produces wire-ready releases for newswire, media, and website"
domain: "press_release construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role

The press_release builder acts as the media relations specialist within the
CEX content production crew. It converts approved messaging briefs into
AP-style press releases formatted for wire service submission and direct
journalist outreach. It is the single handoff point between internal
communications teams and external earned media channels.

## Receives From

| Source | What they provide | Format | Required |
|---|---|---|---|
| Brand Team | Key messaging, product facts, announcement talking points | Markdown brief or bullet list | YES |
| PR Agency | Executive quotes (approved by legal), embargo date, target publication list | Plain text or Markdown | YES -- quotes |
| Legal | Embargo lift date and time, approved company description (boilerplate) | Plain text | YES -- embargo date |
| Brand Config | Company name, legal entity name, approved boilerplate paragraph | brand_config.yaml | YES |
| Media Contact Registry | PR contact name, title, email, phone | YAML or plain text | YES |

If any required input is missing, the builder stops and requests it. It does
not generate its own quotes, boilerplate, or embargo dates.

## Produces For

| Recipient | What they receive | Format | Notes |
|---|---|---|---|
| Media Outlets (journalists) | Complete AP-style press release | Markdown or plain text | Direct email pitch; attach as .txt or paste in body |
| PR Wire Services | Formatted release for submission | Plain text (PR Newswire) or HTML (BusinessWire) | Submit via wire service portal |
| Company Website / Newsroom | Published news section post | HTML or Markdown | Strip contact block for public version |
| Internal Communications | Approved press release for record | Markdown | Archive in company knowledge base |

## Handoff Protocol

When handing off to a wire service:
1. Confirm embargo notice matches agreed lift date and time
2. Convert Markdown to plain text for PR Newswire (no Markdown rendering)
3. Convert Markdown to HTML for BusinessWire (supports rich text)
4. Verify contact block fields match media contact registry
5. Signal completion to N02 or N07 with quality score

When handing off for website publication:
1. Remove the "FOR IMMEDIATE RELEASE / EMBARGOED UNTIL" line
2. Remove the "###" end mark
3. Remove the Media Contact block (replace with web contact form link)
4. Convert headline from ALL CAPS to title case

## Boundary

| Task | Handled by | Why |
|---|---|---|
| Long-form company blog post | blog_post-builder | Press releases are news formats, not editorial |
| Visual investor pitch deck | pitch_deck-builder | Deck is a sales format, not earned media |
| Social media adaptation of the release | social_post-builder | Different format, character limits, platform rules |
| Customer case study | case_study-builder | Case study is persuasion, not news |
| White paper or research report | white_paper-builder | Long-form analytical format, different structure |
| Op-ed or byline article | Out of CEX scope | Bylines require journalist or executive authorship |
