---
kind: examples
id: bld_examples_webinar_script
pillar: P07
llm_function: GOVERN
purpose: Golden example and anti-examples for webinar_script to calibrate builder output quality
quality: 9.1
title: "Webinar Script Examples"
version: "1.0.0"
author: n02_wave6
tags: [webinar_script, builder, examples]
tldr: "Golden 60-min SaaS demo webinar script and 2 anti-examples showing hook failure and missing slide cues."
domain: "webinar_script construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---
## Golden Example

**Score**: 9.6 / 10.0 | **Kind**: webinar_script | **ID**: p03_ws_saas_product_demo

**Context**: 60-minute SaaS product demo webinar targeting operations managers. Goal: trial sign-ups.

**Why it scores GOLDEN:**
- Hook states attendee benefit in sentence 1 with a quantified outcome ("cut onboarding time by 50%")
- Agenda lists exactly 3 items with Q&A timing stated upfront
- Each segment has [SLIDE X] cues and [SPEAKER NOTE] instructions
- Demo includes step-by-step narration and a live-fail fallback note
- 3 seed questions prevent dead air in Q&A
- CTA names the action, URL, and benefit -- restated once
- Word count fits 60-min budget (7,200 word limit, script at 6,800 words)

**Excerpt (Hook section)**:

```
## [0:00] HOOK / OPENING (60 sec)
[SLIDE 1: Title Slide]
Speaker: "By the end of this session, you will have a repeatable onboarding workflow
that cuts new-hire ramp time by 50% -- without adding a single headcount to your ops team.
I am going to show you exactly how 140 teams did it last quarter. Let's get started."
[SPEAKER NOTE: Deliver this from memory. No notes. High energy. Pause after "50%".]
```

**Excerpt (Q&A section)**:

```
## [50:00] Q&A FACILITATION (10 min)
[SLIDE 8: Q&A]
Moderator: "We are opening Q&A now. Sarah, first question from the chat --"
Seed Question 1: "How long does implementation typically take for a team of 20?"
Suggested direction: Typical 2-week setup, highlight onboarding specialist support.
Seed Question 2: "Does this integrate with our existing HRIS tools?"
Suggested direction: Native integrations with Workday, BambooHR, ADP -- see integration page.
Seed Question 3: "What happens to our data if we cancel?"
Suggested direction: Full data export, 30-day retention window, no lock-in.
```
## Anti-Example 1: No Hook (Company Bio Opener)

**Score**: 3.8 / 10.0 | **Gate H04**: FAIL | **Why it fails**

**Problematic opening**:

```
## Opening
Speaker: "Welcome everyone. My name is James Wilson and I am the VP of Customer Success
at Acme Corp. Acme was founded in 2018 and we serve over 400 enterprise customers across
14 industries. Today I want to share with you a little bit about our journey and what we
have been working on in terms of new product features..."
```

**Why this fails**:

| Failure | Impact |
|---------|--------|
| No benefit statement in first 60 seconds | 30% of attendees mentally disengage before agenda is stated |
| Speaker bio as opener | Audience does not care about speaker credentials before they care about their own outcome |
| Vague framing ("a little bit about") | Signals low information density -- attendees begin multitasking |
| No hook framework applied | Attention curve drops from peak at second 0 to near-zero by minute 2 |
| Missing [SLIDE 1] cue | Presenter has no visual anchor -- opens on wrong slide in 40% of live events |

**Fix**: Replace with benefit-led hook in 2 sentences. State what attendee will know or be able to do by end of session. Add [SLIDE 1] cue. Reserve speaker bio for the agenda slide intro ("I am Sarah, and I have run 300 onboarding programs -- here is what I have learned").
## Anti-Example 2: Missing Slide Cues (Script Desync)

**Score**: 5.1 / 10.0 | **Dimension D03**: 2/10 | **Why it fails**

**Problematic segment**:

```
## Segment 2: How to Set Up Your First Workflow
Speaker: "Let me walk you through the setup process. First you go to the dashboard.
Then you click on Workflows in the left menu. From there you create a new workflow
and give it a name. You will see some template options -- we recommend starting with
the Onboarding template. Once you select it, you can customize each step. The drag
and drop editor makes it easy to reorder steps. When you are done just hit publish
and the workflow goes live immediately."
```

**Why this fails**:

| Failure | Impact |
|---------|--------|
| No [SLIDE X] cues in 8-step demo narration | Presenter has no visual anchor -- slides and script desync at step 3 |
| No [SCREEN] cues | Live demo operator does not know when to click or navigate |
| No [SPEAKER NOTE] | Presenter has no pacing guidance -- typically rushes this segment |
| No fallback note | If live demo environment fails, presenter has no recovery instruction |
| Passive voice narration ("you will see") | Weak demo energy -- use active imperative: "Click Workflows. You will see three templates." |

**Fix**: Add [SLIDE X] cue before each logical step. Add [SCREEN: action] for each click. Add [SPEAKER NOTE: pause after publish, let attendees see the confirmation screen]. Add fallback: [SPEAKER NOTE: If demo environment unavailable, switch to pre-recorded demo video].