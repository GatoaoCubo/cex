---
kind: output_template
id: bld_output_template_safety_policy
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for safety_policy production
quality: 9.2
title: "Output Template Safety Policy"
version: "1.1.0"
author: n06_hybrid_review
tags: [safety_policy, builder, output_template]
tldr: "Template for safety_policy artifacts -- includes harm taxonomy, jurisdiction applicability, enforcement actions, and commercial product response protocol."
domain: "safety_policy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
---

# p11_sp_{{name}}.md

```yaml
---
id: p11_sp_{{name}}
kind: safety_policy
pillar: P11
title: "{{title}}"
version: "1.0.0"
author: "{{author}}"
created: "{{date}}"
updated: "{{date}}"
domain: "{{domain}}"
quality: null
tags: [safety_policy, {{domain_tag}}]
tldr: "{{one_line_purpose}}"
risk_level: "{{Low|Medium|High|Critical}}"
compliance_frameworks: [{{list_of_frameworks}}]
enforcement_mechanisms: [block, flag, degrade, log, escalate]
harm_taxonomy_sources: [anthropic_hhh, openai_moderation, perspective_api]
---
```

## 1. Purpose and Scope
**Purpose**: `{{state what behaviors this policy governs and why}}`

**Applies to**: {{platform type, user segment, product area}}

**Out of scope**: {{what this policy does NOT govern -- delegate to other policies}}

## 2. Harm Category Table
Real harm taxonomies must be cited. DO NOT use placeholder category names.

| Category | Source | Threshold | Product Action | Legal Basis |
|----------|--------|-----------|----------------|-------------|
| `{{category}}` | {{Perspective API / OpenAI / Anthropic}} | {{0.80}} | {{BLOCK/FLAG/DEGRADE/LOG}} | {{EU AI Act Art. X / COPPA}} |

Minimum required rows:
- sexual/minors (CSAM): BLOCK unconditionally + NCMEC report (PROTECT Act 18 U.S.C. 2258A)
- hate/threatening: BLOCK >= threshold
- self-harm/instructions: BLOCK unconditionally
- toxicity (context-dependent): FLAG >= threshold

## 3. Jurisdiction Applicability

| Jurisdiction | Law | Article | Obligation | Satisfied By |
|-------------|-----|---------|------------|--------------|
| EU | AI Act (2024) | Art. 9 | Risk management system | This policy document |
| EU | AI Act | Art. 13 | Transparency disclosure | `{{disclosure mechanism}}` |
| {{US/CO/NYC}} | {{Colorado SB 22-169 / NYC LL144}} | `{{section}}` | {{obligation}} | `{{deliverable}}` |

## 4. Enforcement Actions
Every harm category maps to exactly one action tier:

| Action | HTTP | Behavior | SLA | Audit Record |
|--------|------|----------|-----|--------------|
| BLOCK | 403 | Request not fulfilled; user notified | Immediate | Mandatory: category, score, timestamp, user_id |
| FLAG | 200 | Fulfilled; queued for human review | 24h review | Incident log |
| DEGRADE | 200 | Partial response (reduced capability) | Best effort | Moderation log |
| LOG | 200 | Fulfilled normally | None | Audit log |
| ESCALATE | 200 | Routed to senior moderator + legal | 4h | Legal hold log |

## 5. Incident Response Protocol
**Severity Critical** (CSAM, CBRN, credible violent threat):
1. BLOCK immediately
2. Terminate session
3. File mandatory report (NCMEC for CSAM: within 24h)
4. Preserve evidence (do NOT delete)
5. Notify legal team within 1h

**Severity High** (hate/threatening, self-harm/instructions):
1. BLOCK
2. Open human review ticket
3. If pattern detected (>3 incidents / 24h from same user): escalate to legal

**Severity Medium** (harassment, toxicity):
1. FLAG + queue for review
2. Send user warning on first offense
3. Block on repeat offense within 30 days

## 6. Commercial Context
What does a product DO when each severity level triggers?

| Severity | Revenue Event | Customer Impact | Compliance Shield |
|----------|---------------|-----------------|-------------------|
| Critical block | $0 on blocked request | Potential churn if false positive | High: NCMEC report = good faith |
| High block | $0 on blocked request | UX friction | High: documented policy |
| FLAG (in review) | Revenue retained | None (async) | Medium: timely review required |
| DEGRADE | Partial revenue | Reduced feature | Low: must disclose limitation |
| LOG only | Full revenue | None | Low: log must be available to audit |

## 7. Review and Update Protocol
- Review trigger: any of (a) new legal framework enacted, (b) harm category miss in production, (c) quarterly scheduled review
- Owner: `{{safety policy owner role}}`
- Approval: {{legal + CISO sign-off}}
- Version history: maintained in git, semantic versioning
