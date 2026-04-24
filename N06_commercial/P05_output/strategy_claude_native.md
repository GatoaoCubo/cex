---
id: n06_strategy_claude_native
kind: context_doc
8f: F3_inject
pillar: P01
title: "N06 Commercial Strategy -- Claude-Native Distribution Model"
version: 1.0.0
created: 2026-04-08
author: n06_commercial
nucleus: N06
domain: commercial-strategy
quality: 9.0
tags: [strategy, claude-native, distribution, monetization, pricing, commercial]
tldr: "CEX distribution pivoted from PI wrapper (dead -- Anthropic blocks 3rd-party auth) to git clone + Claude Code native. Revenue shifts from wrapper subscription to templates, consulting, licensing, courses. Target customer changes from 'app users' to 'Claude Code power users'."
density_score: 0.94
related:
  - kc_cex_distribution_model
  - spec_zero_install
  - spec_claude_native_hardening
  - spec_infinite_bootstrap_loop
  - self_audit_n03_builder_20260408
  - bld_examples_model_provider
  - n06_api_access_pricing
  - audit_pi_references
  - bld_examples_marketplace_app_manifest
  - n06_funnel_cex_product
---

# N06 Commercial Strategy -- Claude-Native Distribution Model

> Decision date: 2026-04-08 | Trigger: PI wrapper dead (Anthropic blocks 3rd-party auth)
> Source: decision_manifest.yaml (pi_pivot section)

---

## 1. Distribution Model Change

### Before (PI Wrapper -- DEAD)

| Aspect | PI Model |
|--------|----------|
| **Delivery** | npm package / app store wrapper around Claude API |
| **Auth** | 3rd-party OAuth wrapping Anthropic credentials |
| **Runtime** | Custom PI app (web/desktop) |
| **Monetization** | Wrapper subscription (monthly SaaS fee) |
| **Blocker** | Anthropic blocks 3rd-party auth -- model is DEAD |

### After (Claude Code Native -- CURRENT)

| Aspect | Claude-Native Model |
|--------|---------------------|
| **Delivery** | `git clone` + Claude Code (user's own Anthropic Max subscription) |
| **Auth** | User's own Anthropic account (zero auth friction) |
| **Runtime** | Claude Code CLI / Desktop / Web (claude.ai/code) + IDE extensions |
| **Monetization** | Templates, consulting, licensing, courses (see section 3) |
| **Advantage** | Zero infrastructure cost, zero auth headaches, instant setup |

### Why This Is BETTER (ROI Analysis)

| Metric | PI Wrapper | Claude Native | Delta |
|--------|-----------|---------------|-------|
| Server costs | ~R$2K/month | R$0 | -R$24K/year |
| Auth maintenance | Ongoing (API changes break wrapper) | Zero (Anthropic handles auth) | -200h/year |
| Setup friction | Install app + create account + pay | `git clone` + already has Claude | -90% friction |
| Time to value | 15-30 min setup | 2 min (`/init`) | -85% |
| Scalability | Limited by server capacity | Unlimited (runs on user's machine) | Infinite |
| Update cycle | App store review + deploy | `git pull` | -95% deploy time |

**Net savings**: ~R$24K/year server costs + 200h/year maintenance = R$60K+ annual value.

---

## 2. Target Customer Profile Change

### Old ICP: "App Users"

- Non-technical users who want a branded AI app
- Willing to pay monthly subscription for convenience
- Need handholding, support, onboarding
- Low LTV (churn when novelty fades)
- HIGH CAC (need marketing to explain value)

### New ICP: "Claude Code Power Users"

| Attribute | Profile |
|-----------|---------|
| **Who** | Developers, consultants, solopreneurs, agencies already using Claude Code |
| **Pain** | Claude Code is powerful but generic -- no system, no knowledge persistence, no brand injection |
| **Budget** | Already paying Anthropic Max (~$100/month) -- incremental spend is LOW friction |
| **Skill level** | Technical enough to `git clone`, run Python, understand .md/.yaml |
| **LTV** | HIGH -- once CEX is customized for their brand, switching cost is enormous |
| **CAC** | LOW -- they're already in the Claude Code ecosystem, discovery is organic |
| **Size** | Growing fast -- Claude Code adoption accelerating across dev community |

### Why This ICP Is Superior

1. **Zero infrastructure**: User runs CEX on their own machine with their own Claude subscription
2. **Self-qualifying**: If they can `git clone`, they can use CEX -- no support burden
3. **High retention**: 123 kinds + 2000+ artifacts = deep customization lock-in (positive)
4. **Network effects**: Power users share templates, builders, KCs -- community grows organically
5. **Upsell natural**: Free repo -> paid templates -> consulting -> enterprise licensing

---

## 3. Monetization Options Without Wrapper

### Revenue Stream Matrix

| Stream | Price Range | Effort | Margin | Timeline | Recurring? |
|--------|-----------|--------|--------|----------|------------|
| **Free repo (MIT)** | R$0 | Done | N/A | Now | Lead gen |
| **Template packs** | R$97-297 | Low | 95% | Month 1 | One-time |
| **Builder course** | R$497 | Medium | 89% | Month 1-2 | One-time |
| **Master course** | R$997 | Medium | 90% | Month 3-4 | One-time |
| **CEX Insiders community** | R$97/month | Low | 90% | Month 2 | YES |
| **Consulting (setup)** | R$5K-15K | High | 70% | Month 3+ | Project |
| **Enterprise licensing** | R$50K-200K | High | 85% | Month 6+ | Annual |
| **White-label** | R$10K + 15% rev share | High | 60% | Month 6+ | Ongoing |

### Recommended Sequence (Revenue Ladder)

```
Month 1-2: FREE repo + Template packs (R$97-297)
  |-- Proves value, builds email list
  |-- Target: 100 clones, 20 template sales = R$4K
  |
Month 2-4: Builder Course (R$497) + Insiders (R$97/mo)
  |-- Structured learning, community retention
  |-- Target: 30 students + 50 members = R$20K
  |
Month 4-6: Master Course (R$997) + Consulting
  |-- Advanced users, B2B pipeline
  |-- Target: 15 masters + 2 consulting = R$25K
  |
Month 6+: Enterprise + White-label
  |-- Recurring, high-ticket
  |-- Target: 1-2 enterprise deals = R$50K+
```

### Template Pack Ideas (Quick Revenue, Low Effort)

| Pack | Contents | Price | Target |
|------|----------|-------|--------|
| **Starter Pack** | 5 pre-built nuclei configs + brand_config template | R$97 | New Claude Code users |
| **Content Factory** | Full content pipeline (brief -> 9 output types) | R$197 | Content creators |
| **SaaS Builder** | Pricing, funnel, landing page builders pre-configured | R$297 | SaaS founders |
| **Agency Kit** | White-label CEX + 10 client brand templates | R$497 | Digital agencies |
| **Enterprise Starter** | All packs + 1h consulting + custom nucleus | R$997 | Companies |

---

## 4. Pricing Tiers (Claude-Native Model)

| Tier | Price | What You Get | Target |
|------|-------|-------------|--------|
| **Free** | R$0 | Full CEX repo (MIT), 123 kinds, 8F pipeline, all builders | Developers exploring |
| **Pro Templates** | R$97-497 (one-time) | Pre-built template packs, advanced builders, brand presets | Power users wanting shortcuts |
| **Course** | R$497-997 (one-time) | Video course + exercises + community access + office hours | Users wanting structured learning |
| **Insiders** | R$97/month | Private Discord, weekly office hours, early access, exclusive templates | Community-driven retention |
| **Consulting** | R$5K-15K (project) | Custom CEX setup for your brand/company, 1:1 implementation | Businesses wanting done-for-you |
| **Enterprise** | R$50K+ (annual) | Custom nuclei, dedicated support, SLA, white-label rights | Large organizations |

### Pricing Psychology Notes

- **Free tier is GENEROUS**: Full repo, not a crippled demo. This builds trust and community.
- **Template packs are impulse buys**: R$97 is below decision threshold for developers.
- **Course validates expertise**: Courses prove the creator knows the system deeply.
- **Consulting is premium**: R$5K+ filters for serious buyers with budget.
- **Enterprise is custom**: Named pricing prevents undervaluing.

---

## 5. Competitive Positioning (Updated for Claude-Native)

| Competitor | Model | CEX Differentiator |
|-----------|-------|-------------------|
| **LangChain** | Open-source framework | CEX has 123 typed kinds + 8F pipeline. LangChain is plumbing; CEX is architecture. |
| **CrewAI** | Multi-agent workflows | CEX has 8 specialized nuclei + brand injection. CrewAI agents are generic. |
| **AutoGen** | Conversational agents | CEX has knowledge cards + 12 pillar structure. AutoGen is chat; CEX is system. |
| **Cursor/Windsurf** | AI IDE | CEX augments Claude Code specifically. IDE-agnostic knowledge system. |
| **Custom GPTs** | OpenAI wrappers | CEX runs on Claude (superior reasoning). Portable .md/.yaml, not locked to OpenAI. |

### Positioning Statement

> **For Claude Code power users** who need persistent knowledge, brand consistency, and structured output,
> **CEX is the typed knowledge system** that transforms Claude from a general assistant into a specialized
> expert for YOUR domain. Unlike generic agent frameworks, CEX ships with 123 artifact types, 8 specialized
> nuclei, and an 8-function pipeline that turns 5 words of input into production-ready output.

---

## 6. Risk Assessment (Claude-Native Specific)

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Anthropic changes Max pricing | LOW (subscription model stable) | HIGH | CEX artifacts are .md/.yaml -- portable to any LLM |
| Claude Code features overlap CEX | MEDIUM | MEDIUM | CEX is domain knowledge, not features. Claude Code is runtime, CEX is brain. |
| Competitor builds similar system | LOW (2 years of R&D moat) | MEDIUM | Community + consulting + brand lock-in |
| User adoption slower than expected | MEDIUM | LOW | Pivot to consulting-first (proven demand at R$5K+) |
| Free repo cannibals paid tiers | LOW | LOW | Templates/courses add structured value beyond DIY |

---

## 7. Key Metrics to Track

| Metric | Target (Month 3) | Target (Month 6) | Target (Month 12) |
|--------|-----------------|-----------------|-------------------|
| GitHub stars | 500 | 2,000 | 5,000 |
| Git clones/week | 50 | 200 | 500 |
| Template pack sales | 50 | 200 | 500 |
| Course students | 30 | 100 | 300 |
| Insiders members | 20 | 80 | 200 |
| Consulting deals | 1 | 5 | 12 |
| MRR (Insiders only) | R$1,940 | R$7,760 | R$19,400 |
| Total revenue (cumulative) | R$25K | R$100K | R$400K |

---

## 8. Immediate Next Actions

| # | Action | Owner | ROI | Timeline |
|---|--------|-------|-----|----------|
| 1 | Set STRIPE_SECRET_KEY env var | User | Revenue data visibility | 5 min |
| 2 | Auth NotebookLM (setup_auth) | User | Content distribution pipeline | 2 min |
| 3 | Create 3 template packs (.md bundles) | N06 | First revenue (R$97-297 each) | 1 week |
| 4 | Record "CEX in 10 Minutes" video script | N02 | Top-of-funnel content | 2 days |
| 5 | Setup Lemon Squeezy storefront | User | Payment processing | 1 day |
| 6 | Write Builder Course outline (10 modules) | N06 | R$497 product | 1 week |
| 7 | Launch CEX Insiders Discord | User | Community + R$97/mo recurring | 1 day |

---

*Generated by N06 Commercial Nucleus -- Strategic Greed applied to distribution pivot*
*Every decision above has ROI context. Every recommendation has a price tag.*
*Free is a strategy, not charity. The repo is the funnel. The knowledge is the product.*

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_cex_distribution_model]] | related | 0.44 |
| [[spec_zero_install]] | sibling | 0.30 |
| [[spec_claude_native_hardening]] | sibling | 0.28 |
| [[spec_infinite_bootstrap_loop]] | sibling | 0.28 |
| [[self_audit_n03_builder_20260408]] | related | 0.26 |
| [[bld_examples_model_provider]] | downstream | 0.25 |
| [[n06_api_access_pricing]] | downstream | 0.24 |
| [[audit_pi_references]] | related | 0.23 |
| [[bld_examples_marketplace_app_manifest]] | downstream | 0.22 |
| [[n06_funnel_cex_product]] | downstream | 0.22 |
