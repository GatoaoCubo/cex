---
kind: instruction
id: bld_instruction_content_monetization
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for content_monetization artifacts
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a content_monetization

## Phase 1: RESEARCH
1. Identify the business: niche, country, currency, target audience, content type
2. Audit existing monetization: current pricing, payment provider, course platform
3. Catalog content assets: what can be monetized (tools, reports, courses, data, API access)
4. Map pipeline costs: LLM tokens per operation, API calls, compute — express in credits
5. Research competitors: pricing ranges, tier names, feature bundling in the niche
6. Identify payment providers available in the target market:
   - Global: Stripe (cards + subscriptions + usage billing)
   - BR infoproducts: Hotmart, Kiwify, Monetizze, Eduzz (checkout pages + affiliates)
7. Define email provider: Resend (dev-friendly), SendGrid (scale), SES (cost), Mailchimp (no-code)
8. Define ad platforms: Meta Ads (B2C), Google Ads (intent), LinkedIn Ads (B2B), TikTok Ads (gen-z)
9. Check existing content_monetization artifacts to avoid config overlap

## Phase 2: COMPOSE
1. Read bld_schema_content_monetization.md — source of truth for config fields
2. Read bld_output_template_content_monetization.md — template structure
3. Fill frontmatter: id, kind, pillar, title, version, quality: null
4. Write PARSE stage: inventory content assets, classify by monetization potential
5. Write PRICING stage: define strategy and tiers
   - Choose strategy: freemium (free + paid), tiered (good/better/best), usage (pay-per-use),
     credit_pack (prepaid bundles), hybrid (tier + overage credits)
   - Define tiers: name, monthly price (centavos), yearly price, credits included, features
   - Set floor_margin_pct >= 0.30 — calculate: (price - pipeline_cost) / price >= 0.30
   - Optional: trial_days (7-30), annual discount (typically 2 months free)
6. Write CREDITS stage: map pipeline operations to credit costs
   - Each operation: name, credit cost, underlying cost (LLM tokens, API, compute)
   - Define packs for pay-as-you-go users: name, credits, price
   - Set overdraft_policy: block (safest), notify_then_block, allow_negative (risky)
7. Write CHECKOUT stage: payment provider integration
   - Provider config: API key env var, webhook URL, webhook secret env var
   - Webhook handling: idempotency_key dedup, signature verification, event mapping
   - Redirects: success URL, cancel URL
   - Mock mode: true by default, false only after validation
8. Write COURSES stage (if applicable):
   - Module structure: title, lessons (title + type + duration), drip_days
   - Certification: completion_threshold (default 0.80), certificate template
   - Content types: video, text, quiz, assignment, live session
9. Write ADS stage (if applicable):
   - Platform selection: Meta (B2C awareness), Google (intent capture), LinkedIn (B2B)
   - Budget allocation: monthly budget in centavos, target CPA
   - Tracking: pixel/tag env vars, conversion events
10. Write EMAILS stage (if applicable):
    - Sequences: onboarding (post-signup), upsell (after trial), churn prevention (pre-cancel)
    - Triggers: behavioral (used feature X), time-based (day 3), threshold (credits < 10%)
    - Provider config: API key env var, from address, reply-to
11. Write VALIDATE stage: pre-launch checks
    - Margin validation: every tier must pass floor_margin_pct
    - Webhook test: send test event, verify idempotent handling
    - Mock checkout: complete full flow with test credentials
12. Write DEPLOY stage: mock→production cutover checklist

## Phase 3: VALIDATE
1. Check all 9 pipeline stages documented with inputs/outputs
2. Verify pricing: all amounts in centavos/cents (integers, not floats)
3. Verify margins: floor_margin_pct >= 0.30 for every tier
4. Verify no API keys/secrets in plaintext — only ENV_VAR references
5. Verify webhook idempotency is configured (idempotency_key + dedup)
6. Verify mock_mode defaults to true
7. Verify credit costs cover all pipeline operations (no untracked ops)
8. Verify overdraft_policy is explicitly set (no implicit behavior)
9. Check body <= 4096 bytes per file (6144 for instruction)
