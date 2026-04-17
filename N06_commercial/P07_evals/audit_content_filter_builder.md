---
id: n06_audit_content_filter_builder
kind: audit_report
nucleus: n06
pillar: P11
mission: HYBRID_REVIEW
quality: 8.9
title: "Audit: content_filter-builder (13 ISOs)"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
tags: [content_filter, audit, hybrid_review, n06]
tldr: "13 ISOs audited. 3 pass, 8 need taxonomy injection, 2 rebuilt. Main gap: no named harm categories, fictional external tools, missing enforcement_action field."
---

# Audit: content_filter-builder

## Scoring Matrix

| ISO | File | D1-Completeness | D2-Real Taxonomies | D3-Legal Frameworks | D4-Commercial Lens | Score | Action |
|-----|------|-----------------|-------------------|---------------------|-------------------|-------|--------|
| manifest | bld_manifest_content_filter.md | 0.80 | 0.60 (GDPR, COPPA named) | 0.60 | 0.45 | 6.5 | FIX |
| instruction | bld_instruction_content_filter.md | 0.75 | 0.50 (no taxonomy step) | 0.50 | 0.35 | 6.0 | FIX |
| knowledge_card | bld_knowledge_card_content_filter.md | 0.80 | 0.65 (Perspective API named) | 0.55 | 0.45 | 6.5 | FIX |
| schema | bld_schema_content_filter.md | 0.75 | 0.55 | 0.50 | 0.40 | 6.5 | FIX |
| quality_gate | bld_quality_gate_content_filter.md | 0.80 | 0.70 (latency threshold, operators) | 0.60 | 0.65 | 7.0 | PASS |
| output_template | bld_output_template_content_filter.md | 0.50 | 0.20 (wrong frontmatter) | 0.20 | 0.10 | 5.0 | REBUILD |
| examples | bld_examples_content_filter.md | 0.65 | 0.55 (regex pattern, keywords) | 0.40 | 0.35 | 6.0 | FIX |
| system_prompt | bld_system_prompt_content_filter.md | 0.75 | 0.60 | 0.50 | 0.40 | 6.5 | FIX |
| architecture | bld_architecture_content_filter.md | 0.80 | 0.65 | 0.60 | 0.65 | 7.0 | PASS |
| collaboration | bld_collaboration_content_filter.md | 0.70 | 0.55 | 0.50 | 0.50 | 6.5 | FIX |
| config | bld_config_content_filter.md | 0.75 | 0.60 | 0.55 | 0.55 | 6.5 | FIX |
| memory | bld_memory_content_filter.md | 0.70 | 0.50 | 0.45 | 0.40 | 6.0 | FIX |
| tools | bld_tools_content_filter.md | 0.55 | 0.25 (fictional: Content Policy Library) | 0.35 | 0.25 | 5.5 | REBUILD |

**Summary: 2 pass, 9 fix, 2 rebuild**

## Critical Gaps

### Missing Harm Category Taxonomy
The knowledge_card mentions Perspective API for "toxicity scoring" but lists no categories.
Required taxonomy table:

| Source | Categories | Product Action |
|--------|-----------|----------------|
| Perspective API | TOXICITY, SEVERE_TOXICITY, IDENTITY_ATTACK, INSULT, PROFANITY, THREAT, SEXUALLY_EXPLICIT, FLIRTATION | block >= 0.9 / flag >= 0.7 |
| OpenAI Moderation | hate, hate/threatening, self-harm, sexual, sexual/minors, violence, violence/graphic | block always: sexual/minors, hate/threatening |
| AWS Comprehend | HATE_SPEECH, HARASSMENT_OR_ABUSE, SEXUAL, VIOLENCE_OR_THREAT, INSULT, GRAPHIC | BLOCK >= 0.95 |
| CSAM (PhotoDNA / NCMEC) | Child sexual abuse material hash matching | BLOCK + report + terminate session |

### Missing output_template fix
Current template has wrong frontmatter (title, description, keywords, categories -- not kind, id, filter_type).
Missing `enforcement_action` section entirely.

### Missing Legal Frameworks
- DSA (EU Digital Services Act) Article 34 -- risk assessment mandate for large platforms
- EU AI Act Article 52 -- transparency for deep fakes and synthetic content
- COPPA Rule Section 312.3 -- collection constraints (the manifest mentions COPPA but no articles)

### Fictional External Tools
"Content Policy Library (open-source guidelines)" -- does not exist.
Real tools: Google Cloud Natural Language Toxicity API, AWS Rekognition Content Moderation,
Microsoft Azure Content Moderator, OpenAI Moderation Endpoint, PhotoDNA (CSAM), Jigsaw Perspective API.

### Missing enforcement_action field in schema
Current schema has `filter_type` and `sensitivity_level` but no `enforcement_action`.
Products MUST define per-category action at schema level: block | flag | degrade | log | escalate.

## Commercial Risk Classification

| ISO | Legal Liability Risk | Brand Risk | Product Quality Risk |
|-----|---------------------|------------|---------------------|
| output_template | CRITICAL -- wrong frontmatter = 0 valid artifacts | HIGH | HIGH |
| knowledge_card | HIGH -- no CSAM detection documented | CRITICAL -- brand damage if CSAM passes | HIGH |
| schema | HIGH -- no enforcement_action = undefined product behavior | HIGH | HIGH |
| tools | HIGH -- no real detection tools cited = no actual pipeline | MEDIUM | HIGH |
| examples | MEDIUM -- example keywords "nsfw", "hate_speech" as filter terms, not actual words | MEDIUM | MEDIUM |

## Fixed ISOs (see actual file changes)

### Rebuilt: bld_output_template_content_filter.md
- Corrected frontmatter to match bld_schema_content_filter.md (kind, id, filter_type, sensitivity_level)
- Added harm_categories table (Perspective API / OpenAI / AWS taxonomy)
- Added enforcement_actions section with block/flag/degrade/log protocol
- Added platform_applicability section (B2C consumer product vs enterprise API)

### Rebuilt: bld_tools_content_filter.md
- Removed "Content Policy Library" (fictional)
- Added: Perspective API, OpenAI Moderation API, AWS Rekognition Content Moderation,
  Microsoft Azure Content Moderator, PhotoDNA (CSAM hash matching), Jigsaw Unintended Bias API
