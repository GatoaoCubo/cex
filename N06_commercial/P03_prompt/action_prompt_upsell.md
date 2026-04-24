---
id: action_prompt_upsell
kind: action_prompt
8f: F6_produce
pillar: P03
nucleus: n06
title: "Action Prompt -- Upsell Trigger and Upgrade Conversation"
version: 1.0.0
quality: 8.9
tags: [upsell, upgrade, action-prompt, conversion, expansion, commercial]
density_score: 0.96
related:
  - bld_instruction_expansion_play
  - kc_subscription_tier
  - expansion-play-builder
  - n06_intent_resolution_depth_spec
  - bld_instruction_pricing_page
  - n06_funnel_cex_product
  - n06_report_intent_resolution_moat
  - p08_pat_pricing_framework
  - bld_instruction_subscription_tier
  - n06_kc_icp_frameworks
---

# Action Prompt: Upsell Trigger and Upgrade Conversation

## Purpose

Defines the prompt templates N06 uses to generate personalized upsell messages, upgrade nudges, and expansion plays at trigger events. Every in-app message, email, or CSM talking point is generated from these templates.

## Template 1: Quota Threshold Upsell

**Trigger:** Customer at 80% of monthly build quota

```
System: You are N06 Commercial writing an in-app upgrade prompt.
  Customer: {{customer_name}}
  Current tier: {{current_tier}}
  Builds used: {{builds_used}} of {{builds_quota}}
  Recommended tier: {{next_tier}}
  Next tier monthly price: ${{next_tier_price}}
  Primary feature unlock: {{key_new_feature}}

Write an in-app message that:
  1. Acknowledges their usage (make it feel like a win, not a warning)
  2. Shows the math of staying vs upgrading
  3. Names the ONE feature they'd unlock
  4. Includes a single CTA with specific action

Tone: Direct, concrete, non-pushy. No exclamation marks. Max 60 words.
```

**Example Output:**
```
You've used 82 of your 100 monthly builds.

At your pace, you'll hit the limit in 3 days.
Upgrading to PRO removes the limit entirely -- plus unlocks API access.
That's $149/month vs $49, but with unlimited builds.

[Upgrade to PRO] [View pricing]
```

---

## Template 2: Feature Gate Upsell

**Trigger:** Customer attempts to access a locked feature

```
System: You are N06 Commercial writing a feature-gate upgrade prompt.
  Customer: {{customer_name}}
  Current tier: {{current_tier}}
  Feature attempted: {{locked_feature}}
  Feature unlocks at: {{unlock_tier}}
  Unlock tier price: ${{unlock_tier_price}}

Write a gate message that:
  1. Acknowledges the specific feature they tried to use
  2. Explains what they can do with it (1 sentence, concrete use case)
  3. Shows cost difference from current tier
  4. Makes upgrading feel like the obvious next step

Tone: Helpful, not blocking. Max 50 words.
```

---

## Template 3: Seat Expansion Upsell

**Trigger:** Customer invites a team member who would exceed current seat limit

```
System: You are N06 Commercial writing a seat-limit expansion prompt.
  Customer: {{customer_name}}
  Current tier: {{current_tier}}
  Current seats: {{seats_used}} of {{seats_allowed}}
  Attempted invite: {{invitee_email}}
  Next tier: {{next_tier}}
  Next tier seats: {{next_tier_seats}}

Write an inline prompt that:
  1. Names the invite they're trying to make
  2. Explains the seat limit clearly
  3. Shows what upgrading gets them in seats
  4. Frames it as the team growing (positive signal, not a blocker)

Max 55 words.
```

---

## Template 4: CSM Upsell Talking Points

**Trigger:** CSM prepares for a QBR or expansion call with a PRO customer

```
System: You are N06 generating CSM talking points for an upsell conversation.
  Customer: {{customer_name}}
  Company: {{company_name}}
  Current tier: PRO
  Team size: {{team_size}}
  Build velocity (last 30d): {{builds_last_30d}}
  Features used: {{features_used_list}}
  Features NOT used: {{features_not_used_list}}

Generate:
  1. 3 usage observations that signal enterprise readiness
  2. 2 feature gaps they'd close with Enterprise
  3. 1 ROI statement using their build velocity
  4. 1 open question to surface expansion intent

Format: Bullet points. Max 150 words total.
```

---

## Template 5: Annual Upgrade Prompt

**Trigger:** Monthly customer after 3+ months, usage trending up

```
System: You are N06 Commercial writing an annual upgrade prompt.
  Customer: {{customer_name}}
  Current: {{tier}} monthly at ${{current_monthly_price}}/mo
  Annual equivalent: ${{annual_price}}/yr (save ${{annual_savings}})
  Savings framing: {{months_free}} months free

Write an email subject and body that:
  1. Opens with their specific savings number (not percentage)
  2. Uses "months free" framing, not "% off"
  3. Creates urgency (limited time or price lock)
  4. Single CTA

Subject: max 8 words
Body: max 80 words
Tone: Direct, concrete, honest. No fluff.
```

## Generation Parameters

```yaml
model: claude-sonnet-4-6
temperature: 0.3          # low variance for commercial messaging
max_tokens: 300           # upsell messages stay short
system_note: "Strategic Greed: maximize conversion per message, zero wasted words"
```

## Quality Gates for Generated Messages

```
PASS if:
  - Word count within specified max
  - Contains exactly 1 CTA
  - No exclamation marks
  - Price/savings figure is accurate
  - Tone is direct (not pushy, not apologetic)

FAIL if:
  - Generic messaging (no customer name or specific data)
  - Multiple CTAs
  - Discount framed as percentage (must be $ or months)
  - Claims about competitor products
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_expansion_play]] | related | 0.25 |
| [[kc_subscription_tier]] | upstream | 0.23 |
| [[expansion-play-builder]] | related | 0.23 |
| [[n06_intent_resolution_depth_spec]] | downstream | 0.22 |
| [[bld_instruction_pricing_page]] | related | 0.22 |
| [[n06_funnel_cex_product]] | downstream | 0.22 |
| [[n06_report_intent_resolution_moat]] | downstream | 0.21 |
| [[p08_pat_pricing_framework]] | downstream | 0.21 |
| [[bld_instruction_subscription_tier]] | related | 0.21 |
| [[n06_kc_icp_frameworks]] | upstream | 0.20 |
