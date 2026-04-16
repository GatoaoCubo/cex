---
kind: examples
id: bld_examples_onboarding_flow
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of onboarding_flow artifacts
quality: 9.0
title: "Examples Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, examples]
tldr: "Golden and anti-examples of onboarding_flow artifacts"
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example  
**Title**: Notion Onboarding Flow -- "Create Your First Page" Aha-Moment  
**Kind**: onboarding_flow  
**Description**: A 4-step PLG activation flow that engineers the aha-moment at the first collaborative doc creation, driving team invites and habit formation.  
**Boundary**: Account creation -> first shared workspace (activation, not retention).  

**Steps**:  
1. **Sign-up**: Email or Google SSO. Single screen, no password confirmation required. Time-to-screen: <30s.  
2. **Use-case selection**: "What will you use Notion for?" (3 choices: Personal, Team, Work). Pre-populates workspace template. Reduces blank-canvas paralysis.  
3. **First page creation**: Pre-filled template based on use-case. User edits one field. Aha-moment trigger: real-time collaborative cursor appears after 10s, showing "You could invite your team here."  
4. **Invite hook**: "Notion is better with your team -- add 2 colleagues to unlock 1,000 AI credits." Double reward: social proof + tangible value.  

**Aha-Moment Design**:  
- Trigger: first edit saved (Sean Ellis activation event).  
- Signal: empty-state replaced with a filled page + teammate ghost cursor.  
- CTA: "Share this page" appears above fold, no scroll required.  
- Time-to-aha target: <2 minutes from sign-up.  

**Why it works**:  
- Mirrors Reforge activation framework: reduce friction, deliver value before asking for commitment.  
- Invite hook at aha-moment maximizes k-factor (viral coefficient).  
- Progress bar (3 of 4 steps complete) reduces abandonment via Zeigarnik effect.  

## Anti-Example 1: Missing Aha-Moment (Slack circa 2018)  
**Title**: Slack Onboarding -- Team-First Dead-End  
**Kind**: onboarding_flow  
**Description**: Flow that gates all value behind team setup, leaving solo sign-ups with an empty workspace and no activation path.  
**Boundary**: Activation flow.  

**Steps**:  
1. Sign-up with email.  
2. Create workspace name.  
3. Invite teammates (mandatory, 3 email fields).  
4. End flow -- empty #general channel.  

**Why it fails**:  
- Solo users who skip step 3 land on an empty channel with zero value. No aha-moment, no product tour, no template.  
- Mandatory invite field blocks 40%+ of sign-ups who don’t have emails ready.  
- No progress indicator -- users don’t know how close they are to finishing.  

## Anti-Example 2: Feature Tour Overload (Legacy SaaS pattern)  
**Title**: Generic SaaS 12-Step Product Tour  
**Kind**: onboarding_flow  
**Description**: Modal-driven feature tour that explains every capability before the user has created anything.  
**Boundary**: Activation flow.  

**Steps**:  
1. "Welcome to [Product]!" modal -- Dismiss or Next.  
2. "Here is your dashboard" tooltip.  
3. "Here is the sidebar" tooltip.  
4. "Here are your settings" tooltip.  
5-12. (Eight more tooltips explaining UI chrome)  

**Why it fails**:  
- Time-to-first-value (TTV) exceeds 10 minutes. Users abandon before aha-moment.  
- Feature explanations before value delivery violate Reforge activation principle: earn trust through value, then teach features.  
- 60%+ of users skip the tour immediately -- zero activation benefit.  
- No empty-state design: after tour, user still faces blank canvas with no next action.
