---
kind: examples
id: bld_examples_referral_program
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of referral_program artifacts
quality: 8.9
title: "Examples Referral Program"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [referral_program, builder, examples]
tldr: "Golden and anti-examples of referral_program artifacts"
domain: "referral_program construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example  
```yaml  
kind: referral_program  
name: "Dropbox Referral Program"  
vendor: Dropbox Inc.  
description: "Incentivizes users to invite peers via tiered rewards and viral sharing mechanics."  
spec:  
  viral_coefficient: 2.5  
  reward_structure:  
    - level: 1  
      condition: "Invite 1 user"  
      reward: "5GB of storage"  
    - level: 5  
      condition: "Invite 5 users"  
      reward: "100GB of storage + $10 credit"  
  tracking:  
    - method: "Unique referral links with UTM parameters"  
    - attribution: "First-click model for credit assignment"  
  metrics:  
    - "Referral conversion rate"  
    - "Average number of referrals per user"  
```  

## Anti-Example 1: Missing Viral Coefficient  
```yaml  
kind: referral_program  
name: "FakeApp Referral Program"  
vendor: FakeApp LLC.  
description: "Users earn points for referrals, but no clear viral mechanics."  
spec:  
  reward_structure:  
    - level: 1  
      condition: "Invite 1 user"  
      reward: "10 points"  
  tracking:  
    - method: "Email-based referral codes"  
```  
## Why it fails  
No viral coefficient defined; users have no incentive to share beyond minimal rewards. Points system lacks scalability or urgency, leading to low participation.  

## Anti-Example 2: Unaligned Reward Structure  
```yaml  
kind: referral_program  
name: "BrokenReferral Program"  
vendor: BrokenCo Inc.  
description: "Rewards are given only after 100 referrals, deterring early engagement."  
spec:  
  viral_coefficient: 1.2  
  reward_structure:  
    - level: 100  
      condition: "Invite 100 users"  
      reward: "Free premium subscription"  
```  
## Why it fails  
Reward structure is too distant (100 invites) to motivate participation. High threshold creates friction, making the program ineffective for viral growth.
