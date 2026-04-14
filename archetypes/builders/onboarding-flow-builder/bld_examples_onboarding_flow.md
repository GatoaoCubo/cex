---
kind: examples
id: bld_examples_onboarding_flow
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of onboarding_flow artifacts
quality: null
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
**Title**: Binance Onboarding Flow with Activation Milestones  
**Kind**: onboarding_flow  
**Description**: A streamlined onboarding process for new users with clear milestones and an aha-moment at first trade.  
**Boundary**: Activation flow (account creation to first trade).  

**Steps**:  
1. **Sign-up**: Google reCAPTCHA + email verification (via SendGrid).  
2. **KYC**: Upload ID (via Stripe KYC).  
3. **Wallet Setup**: Connect MetaMask (via WalletConnect).  
4. **First Deposit**: Prompt to deposit fiat (via Plaid integration).  
5. **Aha-Moment**: Display "Your first $100 in BTC is ready!" after deposit confirmation.  
6. **First Trade**: Guided trade tutorial (via TradingView widget).  
7. **Completion**: Badge "Pro Trader" + referral incentive (via Airtable).  

**Aha-Moment Design**:  
- Visual highlight of asset growth post-deposit.  
- Micro-interaction on trade completion ("You’ve unlocked X tokens!").  

## Anti-Example 1: Missing Aha-Moment  
**Title**: Coinbase Onboarding Flow (Incomplete)  
**Kind**: onboarding_flow  
**Description**: A flow that ends at KYC completion without celebrating user progress.  
**Boundary**: Activation flow.  

**Steps**:  
1. Sign-up with email.  
2. KYC verification.  
3. End flow.  

**Why it fails**:  
- No clear milestone or aha-moment after KYC. Users feel unguided and disengaged.  
- Missing the critical step of linking wallet or making a first trade.  

## Anti-Example 2: Over-Complicated Milestones  
**Title**: Kraken Onboarding Flow (Cluttered)  
**Kind**: onboarding_flow  
**Description**: 12 steps with vague milestones and no progress tracking.  
**Boundary**: Activation flow.  

**Steps**:  
1. Sign-up.  
2. Verify phone.  
3. Upload ID.  
4. Set password.  
5. Choose trading preferences.  
6. ... (steps 6–12 omitted for brevity).  

**Why it fails**:  
- Excessive steps without clear purpose or value proposition.  
- No aha-moment to motivate users; high drop-off at step 4.
