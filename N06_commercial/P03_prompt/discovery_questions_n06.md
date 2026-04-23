---
id: discovery_questions_n06
kind: discovery_questions
pillar: P01
nucleus: n06
title: "Discovery Questions -- Structured Commercial Qualification Bank"
version: 1.0.0
quality: 9.0
tags: [discovery, qualification, sales, questions, commercial, spin, meddic]
density_score: 0.94
related:
  - bld_examples_discovery_questions
  - kc_competitive_matrix
  - p10_mem_discovery_questions_builder
  - n06_kc_icp_frameworks
  - email_sequence_template
  - kc_discovery_questions
  - brand_bootstrap
  - n06_commercial
  - n04_knowledge
  - landing_page_template
---

# Discovery Questions: Structured Commercial Qualification Bank

## Purpose

Provides N06 with a structured question bank for commercial discovery. Questions follow SPIN methodology (Situation, Problem, Implication, Need-Payoff) and are organized by persona, use case, and stage. Every question has a purpose -- extract information that maps directly to ROI calculator inputs, ICP scoring, or tier recommendation.

## SPIN Question Bank

### SITUATION Questions (Context Building)

```
S1: "How large is your team that creates [artifact type / content / commercial materials]?"
    -> Input: team_size for roi_calculator

S2: "How often do you produce [artifact type] -- weekly, daily, monthly?"
    -> Input: builds_per_week for roi_calculator

S3: "What tools are you currently using for this?"
    -> Informs: competitive context + switch cost

S4: "Who typically reviews and approves these outputs before they go live?"
    -> Informs: revision_cycles for roi_calculator + decision process

S5: "Do you have brand guidelines documented anywhere today?"
    -> Informs: brand_config value proposition strength

S6: "Are these mostly internal documents or customer-facing materials?"
    -> Informs: quality sensitivity + tier recommendation
```

### PROBLEM Questions (Pain Identification)

```
P1: "What's the most frustrating part of how you create [artifact type] today?"
    -> Informs: pain framing for demo and close

P2: "How many revision cycles does a typical [artifact] go through before sign-off?"
    -> Input: revision_cycles for roi_calculator

P3: "Has inconsistent quality or off-brand output ever caused a real problem?"
    -> Informs: quality risk framing; high-value if yes

P4: "How long does it take from 'we need a [artifact]' to having a final version?"
    -> Input: hours_per_build baseline

P5: "Are there requests you can't currently meet because the team doesn't have enough capacity?"
    -> Informs: capacity constraint = strong purchase motivation

P6: "When someone leaves your team, what happens to their knowledge and templates?"
    -> Informs: institutional knowledge loss angle (CEX entity_memory value prop)
```

### IMPLICATION Questions (Amplify Pain)

```
I1: "If you could cut [hours_per_build] in half, what would your team do with that time?"
    -> Purpose: make status quo pain concrete; ROI calculator preview

I2: "What's the downstream impact when [artifact] is delayed or off-brand?"
    -> Purpose: connect pain to business outcome (lost revenue, deals slipped)

I3: "If this pace continues, how does that affect your team's ability to scale?"
    -> Purpose: create urgency around growth bottleneck

I4: "What's the cost of having a senior person spend [X hours] on this vs strategic work?"
    -> Input: hourly_rate for roi_calculator (prompt for fully-loaded cost)

I5: "Has a missed [artifact] or slow turnaround ever cost you a deal or a customer?"
    -> Purpose: monetize pain; creates powerful close anchor
```

### NEED-PAYOFF Questions (Solve and Close)

```
N1: "If you could produce a professional [artifact] in under 5 minutes -- with brand voice locked in --
     what would you use that time for?"
    -> Purpose: make the benefit concrete in their terms

N2: "If the ROI math works out to [X]% return -- is that the kind of decision that's
     straightforward for you to make, or does it need sign-off?"
    -> Purpose: identify economic buyer and decision process simultaneously

N3: "What would need to be true about [CEX] for you to be confident enough to try it?"
    -> Purpose: uncover hidden objections; surface specific proof needs

N4: "If we could get your team running in one day -- would starting this week make sense?"
    -> Purpose: test urgency + timeline; identify blockers
```

## Persona-Specific Questions

### Founder / Solo Operator

```
"How much of your week goes into content and commercial materials vs actual [core work]?"
"What's the hourly rate you'd assign to that time?"
"If you had an assistant who could handle 80% of this -- what would you do differently?"
```

### Marketing Manager (Team Lead)

```
"How many pieces of content / commercial output does your team produce per month?"
"What's your current workflow from brief to final output?"
"How do you maintain brand consistency across team members?"
```

### Sales Leader

```
"How long does it take your reps to create custom proposals or decks for prospects?"
"Do your reps go off-brand or off-message when customizing materials?"
"What's the cost when a deal slips because materials weren't ready in time?"
```

### Enterprise Procurement / IT

```
"What compliance requirements do you have for AI tools? (GDPR, SOC2, data residency?)"
"Who owns vendor evaluation -- is this a procurement-led or team-led process?"
"What's your standard SLA requirement for business-critical tools?"
```

## Question Sequencing Protocol

```
Stage 1 -- Opening (5 min): 2-3 SITUATION questions
  Goal: understand context, avoid asking things you could have researched

Stage 2 -- Pain exploration (8 min): 2-3 PROBLEM questions
  Goal: find the primary pain; get quantifiable data for roi_calculator

Stage 3 -- Amplification (5 min): 1-2 IMPLICATION questions
  Goal: make status quo cost feel real and urgent

Stage 4 -- Vision (5 min): 2 NEED-PAYOFF questions
  Goal: get them articulating the solution in their own words

DO NOT: run through all questions sequentially. Adapt to what they say.
DO: let their answers guide which question comes next.
```

## Question Red Flags

| Answer | Interpretation | Action |
|--------|---------------|--------|
| "We don't really have a process" | Very early stage, no urgency | Educate; longer sales cycle |
| "We need to check with [many people]" | Committee decision, low champion | Find champion, loop them in early |
| "We already tried [AI tool] and it didn't work" | AI skepticism from bad experience | Differentiation conversation + focused demo |
| "We're not looking to buy right now" | No urgency | Quantify status quo cost; create urgency |
| "Budget isn't approved yet" | Budget cycle mismatch | Understand when and follow up on schedule |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_discovery_questions]] | downstream | 0.30 |
| [[kc_competitive_matrix]] | related | 0.28 |
| [[p10_mem_discovery_questions_builder]] | downstream | 0.27 |
| [[n06_kc_icp_frameworks]] | related | 0.27 |
| [[email_sequence_template]] | downstream | 0.26 |
| [[kc_discovery_questions]] | related | 0.26 |
| [[brand_bootstrap]] | downstream | 0.23 |
| [[n06_commercial]] | downstream | 0.23 |
| [[n04_knowledge]] | related | 0.22 |
| [[landing_page_template]] | downstream | 0.22 |
