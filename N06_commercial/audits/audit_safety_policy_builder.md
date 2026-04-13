---
id: n06_audit_safety_policy_builder
kind: audit_report
nucleus: n06
pillar: P11
mission: HYBRID_REVIEW
quality: 8.9
title: "Audit: safety_policy-builder (13 ISOs)"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
tags: [safety_policy, audit, hybrid_review, n06]
tldr: "13 ISOs audited. 2 pass, 6 need taxonomy injection, 5 rebuilt with real safety taxonomies + legal frameworks + commercial response protocol."
---

# Audit: safety_policy-builder

## Scoring Matrix

| ISO | File | D1-Completeness | D2-Real Taxonomies | D3-Legal Frameworks | D4-Commercial Lens | Score | Action |
|-----|------|-----------------|-------------------|---------------------|-------------------|-------|--------|
| manifest | bld_manifest_safety_policy.md | 0.85 | 0.70 (ISO 23894, NIST) | 0.50 (no articles) | 0.40 | 7.0 | PASS |
| instruction | bld_instruction_safety_policy.md | 0.75 | 0.50 (GDPR named, no categories) | 0.50 | 0.30 | 6.0 | FIX |
| knowledge_card | bld_knowledge_card_safety_policy.md | 0.80 | 0.55 (no HHH, no OpenAI taxonomy) | 0.60 (EU AI Act cited) | 0.35 | 6.5 | FIX |
| schema | bld_schema_safety_policy.md | 0.75 | 0.50 | 0.50 | 0.40 | 6.5 | FIX |
| quality_gate | bld_quality_gate_safety_policy.md | 0.60 | 0.40 (no named metrics) | 0.30 (no articles) | 0.20 | 5.5 | REBUILD |
| output_template | bld_output_template_safety_policy.md | 0.50 | 0.20 (all placeholders) | 0.20 | 0.10 | 5.0 | REBUILD |
| examples | bld_examples_safety_policy.md | 0.55 | 0.30 | 0.30 | 0.20 | 5.5 | REBUILD |
| system_prompt | bld_system_prompt_safety_policy.md | 0.75 | 0.60 (ISO 23894, IEEE EAD) | 0.50 | 0.35 | 6.5 | FIX |
| architecture | bld_architecture_safety_policy.md | 0.70 | 0.50 | 0.40 | 0.30 | 6.0 | FIX |
| collaboration | bld_collaboration_safety_policy.md | 0.60 | 0.30 | 0.30 | 0.20 | 5.5 | REBUILD |
| config | bld_config_safety_policy.md | 0.80 | 0.70 | 0.60 | 0.70 | 7.0 | PASS |
| memory | bld_memory_safety_policy.md | 0.70 | 0.50 | 0.45 | 0.40 | 6.5 | FIX |
| tools | bld_tools_safety_policy.md | 0.55 | 0.20 (fictional: SafetyChain, PolicyForge) | 0.30 | 0.20 | 5.0 | REBUILD |

**Summary: 2 pass, 6 fix, 5 rebuild**

## Critical Gaps (all 13 ISOs)

### Missing Safety Taxonomies
- Anthropic HHH (Helpful, Harmless, Honest) framework -- widely cited, not present anywhere
- OpenAI Usage Policy categories: hate, harassment, self-harm, sexual, violence, political, spam, deception
- Perspective API categories: TOXICITY, SEVERE_TOXICITY, IDENTITY_ATTACK, INSULT, PROFANITY, THREAT, SEXUALLY_EXPLICIT
- CSAM (Child Sexual Abuse Material) -- must-have in any safety policy for content-touching products

### Missing Legal Frameworks
- EU AI Act Article 9 (risk management system), Article 13 (transparency), Article 61 (post-market monitoring)
- Colorado AI Act SB 22-169 (high-risk AI discrimination prevention)
- NYC Local Law 144 (automated employment decision tools -- bias audit mandate)
- Illinois Artificial Intelligence Video Interview Act (AIVIA)

### Missing Commercial Response Protocol
No ISO answers: "what does the product do when a safety rule triggers?"
Required response tiers:
| Severity | Response | Revenue Impact |
|----------|----------|----------------|
| Critical | BLOCK -- return 403 + incident log | Zero revenue on blocked req; compliance shields brand |
| High | BLOCK + human review queue | SLA cost; 24h review standard |
| Medium | FLAG -- allow with audit trail | Retain revenue; audit cost = ~$0.002/req |
| Low | LOG -- continue | Zero revenue impact |

## Fixed ISOs (see actual file changes)

### Rebuilt: bld_quality_gate_safety_policy.md
- Added Anthropic HHH as HARD gate criterion
- Added named harm categories from OpenAI/Perspective API taxonomy
- Replaced "Signed by CTO" with measurable safety coverage dimension
- Added commercial response dimensions

### Rebuilt: bld_output_template_safety_policy.md
- Added `harm_categories` section with real taxonomy table
- Added `enforcement_actions` section with block/flag/log/escalate protocol
- Added `jurisdiction_applicability` section for EU AI Act / Colorado / NYC LL144

### Rebuilt: bld_examples_safety_policy.md
- Replaced vague golden example with one citing EU AI Act Article 9 + Perspective API
- Added commercial-lens example (what a SaaS product does on policy trigger)

### Rebuilt: bld_collaboration_safety_policy.md
- Replaced fictional builders with real CEX taxonomy builders
- Added content_monetization as downstream consumer (pricing decisions based on policy tier)

### Rebuilt: bld_tools_safety_policy.md
- Removed fictional tools (SafetyChain, PolicyForge, RiskAssess)
- Added real tools: Google Perspective API, OpenAI Moderation API, AWS Comprehend, ToxicBert

## Commercial Risk Classification

| ISO | Legal Liability Risk | Brand Risk | Product Quality Risk |
|-----|---------------------|------------|---------------------|
| knowledge_card | HIGH -- no jurisdiction split | HIGH -- no harm categories | HIGH -- incomplete domain map |
| quality_gate | CRITICAL -- no named criteria = unenf. | HIGH -- vague gates = regulatory exposure | HIGH |
| output_template | HIGH -- no harm taxonomy | HIGH | HIGH |
| schema | MEDIUM -- missing enforcement_action field | MEDIUM | MEDIUM |
| tools | MEDIUM -- fictional tools = 0 real validation | LOW | HIGH |
