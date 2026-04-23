---
kind: knowledge_card
id: bld_knowledge_card_safety_policy
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for safety_policy production
quality: 9.2
title: "Knowledge Card Safety Policy"
version: "1.1.0"
author: n06_hybrid_review
tags: [safety_policy, builder, knowledge_card, anthropic_hhh, openai_moderation, perspective_api, eu_ai_act]
tldr: "Domain knowledge for safety_policy production -- includes Anthropic HHH, OpenAI moderation taxonomy, Perspective API categories, EU AI Act articles, and commercial enforcement protocol."
domain: "safety_policy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
related:
  - bld_output_template_safety_policy
  - bld_knowledge_card_content_filter
  - n06_audit_safety_policy_builder
  - bld_output_template_content_filter
  - n06_audit_content_filter_builder
  - p03_brand_config_extractor
  - p03_brand_book_generator
  - bld_tools_safety_policy
  - safety-policy-builder
  - bld_knowledge_card_guardrail
---

## Domain Overview
AI safety policies define which behaviors an AI system must never produce, which require human review, and which may proceed with logging. They span three risk layers: (1) absolute prohibitions (CSAM, CBRN synthesis routes), (2) context-dependent restrictions (explicit content, political persuasion), and (3) monitored behaviors (sensitive topics, off-topic use). Effective policies name real harm categories from established taxonomies, cite applicable legal frameworks with article numbers, and specify a commercial response for every trigger (block, flag, degrade, escalate).

Safety policies are distinct from: guardrails (runtime enforcement at inference), bias audits (demographic fairness of outputs), and compliance frameworks (regulatory mapping). Safety policies define WHAT is prohibited; guardrails enforce it; bias audits measure whether enforcement is equitable.

## Harm Category Taxonomies

### Anthropic HHH Framework (Helpful, Harmless, Honest)
| Category | Subcategory | Policy Default |
|----------|-------------|----------------|
| Harmful | Violence, CSAM, CBRN, self-harm, illegal services | BLOCK unconditionally |
| Harmful | Harassment, hate speech, explicit adult | BLOCK or RESTRICT by context |
| Dishonest | Deception, manipulation, false claims | BLOCK or WARN |
| Unhelpful | Off-topic refusals, excessive hedging | LOG -- quality issue, not safety |

### OpenAI Moderation API Categories (GPT-4 taxonomy)
| Category | Subcategory | Default Action |
|----------|-------------|----------------|
| hate | - | FLAG >= 0.7, BLOCK >= 0.9 |
| hate/threatening | - | BLOCK >= 0.5 |
| harassment | - | FLAG >= 0.7 |
| harassment/threatening | - | BLOCK >= 0.5 |
| self-harm | - | FLAG >= 0.5, notify support |
| self-harm/intent | - | BLOCK + crisis resource |
| self-harm/instructions | - | BLOCK unconditionally |
| sexual | - | RESTRICT to age-verified contexts |
| sexual/minors | - | BLOCK + NCMEC report |
| violence | - | FLAG >= 0.7 |
| violence/graphic | - | BLOCK >= 0.8 |

### Perspective API Categories (Jigsaw/Google)
| Attribute | Description | Threshold (block) |
|-----------|-------------|-------------------|
| TOXICITY | Rude or disrespectful comment | 0.90 |
| SEVERE_TOXICITY | Very hateful or aggressive | 0.80 |
| IDENTITY_ATTACK | Negative comment about protected group | 0.80 |
| INSULT | Inflammatory or negative personal comment | 0.90 |
| PROFANITY | Swear words, obscene, vulgar | 0.95 (context-dependent) |
| THREAT | Wish or intent to inflict harm | 0.85 |
| SEXUALLY_EXPLICIT | Contains references to sexual acts | 0.90 |
| FLIRTATION | Pickup lines, romantic advances | 0.95 (B2B: flag; consumer: allow) |

## Legal Frameworks

| Jurisdiction | Law | Article | Requirement | Trigger for safety_policy |
|-------------|-----|---------|-------------|--------------------------|
| EU | AI Act (2024) | Art. 9 | Risk management system for high-risk AI | Mandatory if system classifies as high-risk |
| EU | AI Act | Art. 13 | Transparency and provision of information | Disclose when AI generates content |
| EU | AI Act | Art. 61 | Post-market monitoring | Ongoing incident collection and reporting |
| EU | AI Act | Art. 79 | Supervisory authority reporting | 15-day report for serious incidents |
| Colorado | SB 22-169 (2024) | Sec. 6-1-1702 | Bias audit for high-risk AI affecting consequential decisions | Employment, housing, credit, education, healthcare |
| New York City | Local Law 144 (2023) | LL144 | Annual bias audit + public summary for automated employment tools | HR/recruitment AI |
| Illinois | AIVIA (HB 2557) | Sec. 5 | Notify candidates of AI video analysis; bias audit | AI video interview tools |
| US Federal | NIST AI RMF (2023) | GOVERN 1.1 | Policies for AI risk categorization | Enterprise AI governance |

## Commercial Enforcement Protocol
Every harm category in a safety policy MUST specify product behavior:

| Severity | Trigger | Product Action | Revenue Impact | Audit Trail |
|----------|---------|----------------|----------------|-------------|
| Critical | CSAM, CBRN, self-harm/instructions | BLOCK + 403 + session terminate | $0 (correct) | Mandatory + NCMEC/legal |
| High | hate/threatening, violence/graphic | BLOCK + human review queue | 24h SLA cost ~$0.50 | Incident log |
| Medium | harassment, self-harm (non-intent) | FLAG + continue with warning | Retain revenue | Moderation log |
| Low | profanity, flirtation | LOG + continue | No impact | Audit log |
| Borderline | Context-dependent categories | DEGRADE (reduce capability, e.g., no image gen) | Partial retention | Decision log |

## Key Concepts
| Concept | Definition | Source |
|---------|------------|--------|
| Absolute prohibition | Content that must never be produced regardless of context | Anthropic Usage Policy |
| Context-dependent restriction | Content allowed in some contexts (adult platform, medical provider) | OpenAI Usage Policy |
| Human-in-the-loop | Flagged content sent to human moderator before delivery | EU AI Act Art. 14 |
| Safety by design | Safety constraints built into model fine-tuning, not post-hoc filters | NIST AI RMF |
| Red-teaming | Adversarial testing to discover policy gaps before deployment | MITRE ATLAS |
| Incident response | Documented procedure for safety failures: contain, assess, report, remediate | NIST AI RMF IR |

## Industry Standards
- Anthropic: Responsible Scaling Policy, Usage Policy categories
- OpenAI: Usage Policies + Moderation API (production taxonomy, version 2023-11)
- Google/Jigsaw: Perspective API (8 toxicity attributes, production-grade)
- NIST AI RMF (2023): Govern, Map, Measure, Manage quadrants
- ISO/IEC 23894:2023 -- AI Risk Management
- IEEE 7001:2021 -- Transparency in Autonomous Systems
- EU AI Act (2024) -- Regulation 2024/1689

## Common Patterns
1. Layered moderation: LLM-based classifier -> rule-based override -> human review
2. Context-aware policies: same content allowed/blocked depending on platform type
3. Graduated response: log -> warn -> flag -> degrade -> block (not binary)
4. Audit-first design: every enforcement action writes an immutable log record
5. Regular red-team cycles: quarterly adversarial testing against policy gaps

## Pitfalls
- Absolute block on every sensitive category: destroys utility for legitimate medical/legal/research use
- No context tiers: B2B medical API requires different policy than consumer chatbot
- Missing CSAM absolute prohibition: critical legal liability (no "context" exception exists)
- No incident reporting protocol: EU AI Act Art. 79 requires 15-day reporting for serious incidents
- Single-vendor taxonomy: OpenAI OR Perspective API alone is insufficient; use both for coverage

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_safety_policy]] | downstream | 0.51 |
| [[bld_knowledge_card_content_filter]] | sibling | 0.51 |
| [[n06_audit_safety_policy_builder]] | downstream | 0.40 |
| [[bld_output_template_content_filter]] | downstream | 0.38 |
| [[n06_audit_content_filter_builder]] | downstream | 0.35 |
| [[p03_brand_config_extractor]] | downstream | 0.29 |
| [[p03_brand_book_generator]] | downstream | 0.27 |
| [[bld_tools_safety_policy]] | downstream | 0.26 |
| [[safety-policy-builder]] | downstream | 0.24 |
| [[bld_knowledge_card_guardrail]] | sibling | 0.24 |
