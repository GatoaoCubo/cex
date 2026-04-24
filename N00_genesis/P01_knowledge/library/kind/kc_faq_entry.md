---
id: p01_kc_faq_entry
kind: knowledge_card
8f: F3_inject
kc_type: meta_kc
pillar: P01
title: "FAQ Entry Kind — Atomic Q&A for Support Deflection"
version: "1.1.0"
created: "2026-04-07"
updated: "2026-04-22"
author: knowledge-card-builder
domain: knowledge_management
subdomain: faq_content
quality: 8.8
tags: [faq, support-deflection, knowledge-base, onboarding, self-service]
tldr: "faq_entry: atomic Q&A unit (max 3072B) with canonical answer, deflection metric, and related links — pillar P01."
when_to_use: "When a question recurs across support channels and a single canonical answer reduces ticket volume."
keywords: [faq_entry, faq, support deflection, canonical answer, knowledge base]
long_tails:
  - "How to structure FAQ entries for support deflection in CEXAI"
  - "Difference between faq_entry and knowledge_card in P01"
axioms:
  - "ALWAYS write the canonical answer first — do not bury it behind context."
  - "NEVER duplicate a faq_entry across domains — update the source, reference it elsewhere."
  - "ALWAYS include a deflection_metric to prove the entry earns its place."
  - "IF a question requires > 400 words to answer, split into 2+ entries or promote to knowledge_card."
linked_artifacts:
  primary: null
  related: [kc_knowledge_card, kc_glossary_entry, kc_onboarding_flow, kc_quickstart_guide, kc_support_macro]
density_score: 0.88
data_source: "https://github.com/cexai/cex"
---

## Executive Summary

`faq_entry` is an atomic P01 artifact that encodes one recurring question with its
canonical answer, support deflection evidence, and related navigation links.
Max size: 3072 bytes. LLM function: INJECT — FAQ entries are context injected into
support agents, onboarding flows, and chatbots to reduce live support load.
Distinct from `knowledge_card` (broader, analytical) and `support_macro` (agent
canned reply, not human-readable Q&A).

## Spec Table

| Field | Value |
|-------|-------|
| Kind | `faq_entry` |
| Pillar | P01 |
| LLM function | INJECT |
| Max bytes | 3072 |
| Naming | `p01_faq_{{name}}.md` |
| Depends on | `knowledge_card` |
| Status | stable (last reviewed 2026-04-14) |
| Quality target | null on creation; 8.0+ after review |

## Required Frontmatter Fields

| Field | Type | Example |
|-------|------|---------|
| `id` | `p01_faq_{slug}` | `p01_faq_support_request` |
| `kind` | literal `faq_entry` | `faq_entry` |
| `pillar` | literal `P01` | `P01` |
| `title` | string <= 80 chars | `"Submitting a Support Request"` |
| `version` | semver | `1.0.0` |
| `created` | YYYY-MM-DD | `2026-04-07` |
| `updated` | YYYY-MM-DD | `2026-04-22` |
| `author` | string (not orchestrator) | `N04_knowledge` |
| `domain` | string | `contributor_onboarding` |
| `quality` | null | `null` |
| `tags` | list 3-7 | `[faq, onboarding, support]` |
| `question` | string (the question verbatim) | `"How do I submit...?"` |
| `answer` | string (one-line summary of answer) | `"Use the Help Center form..."` |
| `category` | string | `getting_started` |
| `deflection_metric` | string or float | `"35% ticket reduction"` |

## Body Structure

| Section | Content |
|---------|---------|
| `**Question**` | Verbatim user question |
| `**Canonical Answer**` | Numbered steps or bullets — no prose |
| `**Related Links**` | 1-5 URLs or artifact paths |
| `**Support Deflection Metric**` | Evidence string with date |

## Patterns (What Works)

| Pattern | Why it works |
|---------|--------------|
| Numbered steps in answer | Scannable; user can follow without re-reading |
| Deflection metric present | Forces evidence-based inclusion; prunes low-value entries |
| Category field populated | Enables grouping in portals (getting_started, billing, technical) |
| question field = verbatim user phrasing | Improves semantic search match from support tickets |
| max 5 related links | Prevents navigation overload; surfaces only next-step resources |

## Anti-Patterns (What Fails)

| Anti-Pattern | Failure Mode |
|-------------|--------------|
| Prose paragraphs in answer | User does not read; deflection fails |
| Missing `deflection_metric` | Entry cannot be pruned during quarterly review |
| answer field vague ("see the docs") | No self-service value; ticket opened anyway |
| Duplicate entries across domains | Stale copies diverge; canonical answer breaks |
| Body > 3072 bytes | Exceeds kind max; truncated during injection |
| question field absent | Semantic search cannot match user phrasing |

## Integration Points

| Artifact | How faq_entry connects |
|----------|----------------------|
| `knowledge_card` | faq_entry depends on KC for deep-dive context; link to parent KC in Related Links |
| `glossary_entry` | Answers that define a term link to matching glossary_entry |
| `onboarding_flow` | Onboarding sequences INJECT faq_entries as contextual Q&A |
| `support_macro` | support_macro is the agent-facing canned reply; faq_entry is the human-readable source |
| `quickstart_guide` | quickstart_guide references faq_entries in its "Common Questions" section |

## Minimal Valid Example

```yaml
id: p01_faq_support_request
kind: faq_entry
pillar: P01
title: "Submitting a Support Request"
version: "1.0.0"
created: "2026-04-22"
updated: "2026-04-22"
author: N04_knowledge
domain: product_support
quality: null
tags: [faq, support, getting-started]
question: "How do I submit a support request?"
answer: "Help Center contact form; 24-hour response SLA."
category: getting_started
deflection_metric: "35% ticket reduction (Q1 2026)"
density_score: 0.82
```

Body:

```
**Question**: How do I submit a support request?

**Canonical Answer**:
1. Go to Help Center > Contact Support.
2. Select category: billing, technical, or other.
3. Fill the form and submit.
4. Response within 24 business hours.

**Related Links**: [Help Center](https://example.com/help)

**Support Deflection Metric**: 35% ticket reduction (Q1 2026).
```

## References

- Kind registry: `.cex/kinds_meta.json` (key: `faq_entry`)
- Real example: `N04_knowledge/P01_knowledge/faq_entry_cex_common_questions.md`
- Builder: `archetypes/builders/faq-entry-builder/`
- Depends on: `knowledge_card` kind (broader domain reference)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_knowledge_card]] | upstream | 0.52 |
| [[kc_glossary_entry]] | sibling | 0.44 |
| [[kc_quickstart_guide]] | sibling | 0.41 |
| [[kc_onboarding_flow]] | sibling | 0.39 |
| [[kc_support_macro]] | sibling | 0.37 |
| [[bld_instruction_faq_entry]] | downstream | 0.35 |
| [[faq-entry-builder]] | downstream | 0.33 |
| [[bld_examples_faq_entry]] | downstream | 0.28 |
| [[p01_qg_faq_entry]] | downstream | 0.26 |
| [[bld_knowledge_card_faq_entry]] | downstream | 0.24 |
