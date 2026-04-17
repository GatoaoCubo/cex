---
id: p01_fse_n02_email_campaign
kind: few_shot_example
pillar: P01
nucleus: N02
title: "Few-Shot Example -- N02 Email Campaign via 8F Pipeline"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: few-shot-example-builder
domain: marketing
difficulty: medium-hard
edge_case: false
format: "8F pipeline trace + email sequence output (subject + preview + body structure)"
quality: 9.1
tags: [few-shot, email, marketing, 8f-pipeline, n02, drip-sequence, campaign]
tldr: "3 input/output pairs teaching N02 how to run 8F for email campaigns: welcome drip, nurture sequence, and re-engagement."
keywords: [email, drip, sequence, subject-line, preview, welcome, nurture, re-engagement, n02]
density_score: 1.0
---
<!-- 8F TRACE
F1 CONSTRAIN: kind=few_shot_example, pillar=P01, naming=p01_fse_{topic}.md
F2 BECOME: few-shot-example-builder (13 ISOs). Sin lens: Creative Lust.
F3 INJECT: kc_email_sequence + kc_campaign + kno_few_shot_example_n02 + quality_gate_marketing. Match: 79%
F4 REASON: 3 examples -- welcome drip, nurture sequence, re-engagement; each with full 8F trace
F5 CALL: Read+Write+compile ready. kc_email_html_responsive for format reference.
F6 PRODUCE: 3 input/output pairs with structured email outputs
F7 GOVERN: frontmatter complete, id=p01_fse_n02_email_campaign, tags>=3, examples non-empty x3
F8 COLLABORATE: compiled via cex_compile.py
-->

## Explanation

Email is the highest-ROI channel in most marketing stacks -- and the most abused.
N02 treats email copy as a relationship, not a broadcast.

These 3 examples teach:
1. Welcome drip (first impression, set expectations)
2. Nurture sequence (build desire over 3+ emails)
3. Re-engagement (win back dormant subscribers without begging)

Every email must earn the reader's next open. Creative Lust means the subject line
makes them WANT to open before they know what is inside.

---

## Example 1 (easy) -- Welcome drip, new trial signup, SaaS

**Input brief**
```yaml
task: write_3_email_welcome_drip
trigger: new_trial_signup
product: ai_agent_platform
audience: technical_founders_and_engineers
sequence_goal: activate trial user to first agent deployment
emails:
  email_1: immediate (day 0) -- welcome + first action
  email_2: day 2 -- proof + feature spotlight
  email_3: day 5 -- objection handling + upgrade path
tone: helpful_direct
cta:
  email_1: deploy_first_agent
  email_2: explore_templates
  email_3: start_pro_trial
```

**8F trace (abbreviated)**
```
F1: kind=email_sequence/P01, 3-email drip, activation sequence
F2: N02. Welcome sequence = trust-first, value-fast. No pitching in email 1.
F3: kc_email_sequence (welcome pattern: value first, CTA single), kc_campaign
F4: email 1=orientation+first_win; email 2=social_proof+feature; email 3=remove_risk+close
F6: subject + preview + structured body outline per email
F7: subject <= 50 chars x3, single CTA x3, no pitch in email_1 = pass
```

**Output**
```yaml
email_1:
  send_day: 0
  subject: "Your first agent deploys in under 10 minutes"
  subject_chars: 46
  preview: "No plumbing required. We mapped the shortest path from sign-up to running agent."
  body_outline:
    - greeting: "Welcome to CEX. You are 10 minutes from your first running agent."
    - value_line: "We skipped the feature tour. Here is the one thing that matters: your first deployment."
    - action_block:
        step_1: "Open your dashboard"
        step_2: "Pick a builder from the 257-kind library"
        step_3: "Run the 8F pipeline -- your agent is live"
    - cta: "Deploy my first agent"
    - ps: "Questions? Reply directly. This inbox is monitored by humans."

email_2:
  send_day: 2
  subject: "40+ teams. One thing they did first."
  subject_chars: 38
  preview: "They deployed fast and iterated from working code -- not from scratch."
  body_outline:
    - opener: "If you have not deployed yet, that is okay. Here is what the teams who did found."
    - proof_block:
        stat: "40+ enterprise teams deployed their first agent in under 2 hours."
        testimonial: "This is the Rails of AI infrastructure. -- CTO, Series B startup"
    - feature_spotlight:
        title: "The 8F pipeline"
        body: "Every artifact passes 8 reasoning functions: Constrain, Become, Inject, Reason, Call, Produce, Govern, Collaborate. Nothing ships below 9.0."
    - cta: "Explore agent templates"
    - ps: "Your trial expires in 8 days. No pressure -- but here is what Pro unlocks."

email_3:
  send_day: 5
  subject: "Still thinking? Here is the honest answer."
  subject_chars: 40
  preview: "The two most common hesitations -- and what we actually found in the data."
  body_outline:
    - opener: "You signed up, which means you saw something. Let us address the two things that usually stop a trial from converting."
    - objection_1:
        fear: "This looks complex"
        answer: "CEX is typed infrastructure. Complexity is the alternative -- building this from scratch. The 8F pipeline removes the plumbing so you can focus on the output."
    - objection_2:
        fear: "I am not sure it will work for my stack"
        answer: "4 runtimes: Claude, Codex, Gemini, Ollama. Your stack is covered. If not, reply and we will check."
    - upgrade_path:
        offer: "Pro trial -- 14 more days, team collaboration, advanced analytics"
        cta: "Start Pro trial -- 14 days free"
    - ps: "If this is not the right time, keep your free tier. We will be here when it is."

quality_check:
  subject_length: "all <= 50 chars"
  pitch_in_email_1: false
  cta_count: "1 per email"
  tone: "helpful_direct throughout"
  objections_addressed: "email 3 (2 objections)"
```

---

## Example 2 (medium) -- Nurture sequence, content brand, creator economy

**Input brief**
```yaml
task: write_5_email_nurture_sequence
trigger: lead_magnet_download
product: content_creation_course_for_creators
audience: aspiring_content_creators_early_stage
sequence_goal: build trust and desire over 5 emails before making offer on day 10
emails:
  email_1: deliver_lead_magnet + first_value
  email_2: pain_empathy
  email_3: proof_story
  email_4: pre-objection
  email_5: soft_offer
tone: warm_confessional_mentoring
rule: no hard pitch before email_5
```

**8F trace (abbreviated)**
```
F1: 5-email nurture, no pitch before email_5, warm_confessional tone
F2: N02. Nurture = relationship building. Creative Lust in nurture = make them look forward to the next email.
F3: kc_email_sequence (nurture pattern: deliver-empathize-prove-anticipate-invite)
F4: arc: lead_magnet -> empathy -> story_proof -> objection_pre-empt -> soft_offer
F6: subject + preview + body_focus per email
F7: no hard pitch before email_5, warm_confessional maintained x5 = pass
```

**Output**
```yaml
email_1:
  send_day: 0
  subject: "Your guide is here -- plus one thing nobody tells you"
  subject_chars: 49
  preview: "The guide is attached. But the thing that matters more is what I learned after I made every mistake."
  body_focus: "Deliver lead magnet. Share one non-obvious lesson that validates their desire and makes email_2 irresistible."

email_2:
  send_day: 2
  subject: "The part of content creation they do not show you"
  subject_chars: 50
  preview: "I spent 6 months posting into nothing. Here is what that actually looks like."
  body_focus: "Empathize with the exact pain of posting without traction. Name it precisely. No solution yet -- just recognition. Make them feel understood."

email_3:
  send_day: 4
  subject: "What changed when she stopped guessing"
  subject_chars: 40
  preview: "Ana posted 3 times a week for a year. Then she changed one thing and her account grew 4x in 60 days."
  body_focus: "Tell a specific student story (named, with timeline and metric). Show transformation. CTA=reply with their biggest obstacle."

email_4:
  send_day: 7
  subject: "The two things people worry about (answered)"
  subject_chars: 47
  preview: "Before you ask: yes, both of these are addressed in the program."
  body_focus: "Pre-empt the two most common objections: time and uniqueness. Answer with specifics, not reassurance. Seed the offer without naming it."

email_5:
  send_day: 10
  subject: "I am opening 12 spots. Here is what is inside."
  subject_chars: 47
  preview: "If you have been following along, this is the part where I tell you what we actually do together."
  body_focus: "Soft offer: name the cohort, describe what happens inside, include testimonial, single CTA. No countdown timer. No fake scarcity. Real invitation."

quality_check:
  hard_pitch_before_email_5: false
  tone_consistency: "warm_confessional x5"
  subject_length: "all <= 50 chars"
  empathy_email_present: true (email_2)
  proof_email_present: true (email_3)
  objection_email_present: true (email_4)
```

---

## Example 3 (hard) -- Re-engagement, lapsed subscribers, B2C

**Input brief**
```yaml
task: write_3_email_re_engagement_sequence
trigger: subscriber_inactive_90_days
product: premium_subscription_box
audience: past_subscribers_who_cancelled
sequence_goal: re-activate or get clean unsubscribe (no zombie list)
emails:
  email_1: curiosity_hook (do not mention they were gone)
  email_2: value_reminder + incentive
  email_3: permission_or_goodbye (clean break option)
tone: warm_no_guilt_no_pressure
rule: email_3 must offer clean unsubscribe as primary option, with re-subscribe as secondary
```

**8F trace (abbreviated)**
```
F1: re-engagement sequence, email_3 must lead with clean_unsubscribe option (inverted CTA priority)
F2: N02. Re-engagement = earn back attention, not demand it. No guilt.
F3: kc_email_sequence (re-engagement: curiosity -> value -> permission)
F4: email_1=curiosity_no_accusation; email_2=value+incentive; email_3=permission_first_then_offer
F6: outputs follow warm_no_guilt tone; email_3 CTA order = unsubscribe first
F7: no guilt language, permission respected in email_3, tone consistent = pass
```

**Output**
```yaml
email_1:
  send_day: 0
  subject: "Something new is in the box this month"
  subject_chars: 41
  preview: "We redesigned the curation. Here is the first preview."
  body_focus: "Pure curiosity hook. No mention of absence. Act as if continuing a conversation. Tease the new curation without pitching. CTA = see what is new."
  note: "Do not say 'we miss you' or 'you have been away' -- it signals accusation, not invitation."

email_2:
  send_day: 4
  subject: "Your subscriber price is still locked in"
  subject_chars: 42
  preview: "Current rate is 20% below the public price. Here is what this month includes."
  body_focus: "Remind them of the concrete value: locked price, exclusive items, curation quality. Include a 10% re-activation discount with code + expiry. CTA = reactivate my box."
  incentive:
    type: discount
    value: "10% off first reactivated box"
    code: COMEBACK10
    expiry: "7 days from send"

email_3:
  send_day: 9
  subject: "Stay or go -- your choice, no judgment"
  subject_chars: 41
  preview: "We would rather you unsubscribe than stay out of obligation. Here is the real offer."
  body_focus: "Lead with unsubscribe as the first option. Frame it as respect, not reverse psychology. Then offer the reactivation option with incentive reminder. CTA_primary=unsubscribe, CTA_secondary=reactivate."
  cta_order:
    primary: "Unsubscribe cleanly -- no hard feelings"
    secondary: "Actually, reactivate at 10% off"
  note: "Inverted CTA priority per brief spec. Primary = clean break."

quality_check:
  guilt_language: 0
  mention_of_absence: 0 (email_1 only)
  clean_unsubscribe_primary: true (email_3)
  incentive_present: true (email_2 + email_3)
  tone: "warm_no_guilt x3"
```

---

## Format Lessons

| Lesson | What the model learns |
|--------|-----------------------|
| Subject line = first decision | Reader decides open/skip in 2 seconds; subject + preview = one unit |
| Welcome = deliver value, no pitch | Email_1 earns trust; pitch comes later in the sequence |
| Nurture arc has a shape | Deliver -> empathize -> prove -> pre-empt -> invite |
| Re-engagement respects autonomy | Offering clean unsubscribe increases re-activation rate |
| Tone declared in brief = tone in every line | One off-tone sentence breaks the relationship |

## Prompting Rules Derived From These Examples

1. Subject line + preview operate together -- always write both.
2. Declare sequence goal and per-email role before writing any copy.
3. Never pitch before trust is built (welcome sequences: value first, offer after email 3).
4. Re-engagement: lead with autonomy, not guilt. Offer the exit before the comeback.
5. For nurture: use the arc (deliver -> empathy -> proof -> pre-empt -> invite).
6. Tone is a constraint, not a suggestion -- enforce it in every email body.

## Anti-Patterns

| Anti-pattern | Failure |
|-------------|---------|
| "We miss you" in re-engagement | Signals accusation, not invitation |
| Hard pitch in welcome email_1 | Breaks trust before it forms |
| Subjects without preview context | Reader sees only half the pitch |
| Nurture sequence without arc | Random emails; no compounding desire |
| CTA count > 1 per email | Decision paralysis; click rate drops |
