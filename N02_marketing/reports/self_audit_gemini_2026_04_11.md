---
id: self_audit_n02_gemini_2026_04_11
kind: self_audit
pillar: P06_schema
title: N02 Marketing Self-Audit (Gemini)
version: 1.0
quality: null
tags: [audit, self_review, n02, marketing, gemini]
created: 2026-04-11
nucleus: n02
---

# N02 Marketing Self-Audit (Gemini Runtime)

This report was generated autonomously by the N02 nucleus running on the Gemini CLI in response to the `SELF_AUDIT_GEMINI` mission. It provides a snapshot of the nucleus's state, capabilities, and dependencies.

## 1. Current State

An analysis of the `N02_marketing/` directory was performed. The nucleus contains a mix of marketing-focused prompts and a significant number of artifacts related to UI components and knowledge structuring, indicating a broader scope than pure copywriting.

### Artifact Count by Kind
The 64 source artifacts are distributed across 23 kinds.
| Kind | Count |
|------|-------|
| knowledge_card | 14 |
| prompt_template | 8 |
| output_validator | 8 |
| input_schema | 5 |
| context_doc | 5 |
| *Other* | 24 |

### Quality Distribution
| Quality Bracket | Count | Notes |
|-----------------|-------|-------|
| >= 9.0 | 52 | All scored artifacts are 9.0, 9.1, or 9.2. |
| 8.0 - 8.9 | 0 | |
| < 8.0 | 0 | |
| null / missing | 12 | A rule violation was noted in a parallel audit that 81% of artifacts were self-scored. |

### Largest 5 Artifacts
| Path | Size (Bytes) |
|------|--------------|
| `N02_marketing/output/landing_page_template.md` | 23972 |
| `N02_marketing/knowledge/kc_tailwind_patterns.md` | 20787 |
| `N02_marketing/output/report_intent_resolution_value_prop.md` | 17020 |
| `N02_marketing/output/output_email_template.md` | 16987 |
| `N02_marketing/knowledge/knowledge_card_marketing.md` | 16803 |

### Most Recently Modified 5 Artifacts
1. `N02_marketing/compiled/self_audit_2026_04_11.yaml`
2. `N02_marketing/reports/self_audit_2026_04_11.md`
3. `N02_marketing/workflows/wf_kc_to_content.md`
4. `N02_marketing/tools/social_publisher_marketing.md`
5. `N02_marketing/tools/headline_scorer.md`

### P03 Prompt Pillar Coverage
Of the marketing-related kinds defined in the `P03_prompt` pillar, the following is the coverage in `N02_marketing/`:
- **Present**: `action_prompt`, `prompt_template`, `system_prompt`.
- **Not Present**: `chain`, `constraint_spec`, `context_window_config`, `instruction`, `prompt_version`, `reasoning_trace`, `tagline`.

## 2. Rules Compliance

Analysis of `.claude/rules/n02-marketing.md`. The investigation was partially completed.

| Rule | Score | Justification & Evidence | Aspirational |
|------|-------|--------------------------|--------------|
| Content Domain | 10/10 | All artifacts are within the marketing, copywriting, and advertising domains. | false |
| Persuasive Structure | 10/10 | The `clarity -> desire -> action` model is explicit in templates like `N02_marketing/artifacts/ad_copy_template.md`. | false |
| A/B Variants | 10/10 | The practice is embedded in prompts (`prompts/system_prompt_marketing.md`) and rubrics (`quality/scoring_rubric_marketing.md`). Historical data suggests a past gap here has been closed. | false |
| 8F Protocol & Metadata | 1/10 | **Major Gap**. No source files were found with `pipeline: 8F` in their frontmatter. The 8F reasoning steps are not documented in artifacts. | true |
| `quality: null` | ?/10 | Investigation was interrupted before this could be fully assessed. However, a parallel audit noted widespread self-scoring, which violates the "Peer-review assigns quality" rule. | false |

## 3. Gaps

The most significant gaps are in process adherence and advanced prompt engineering.

| Priority | Gap Description | Effort |
|----------|-----------------|--------|
| High | **No `tagline` artifacts exist.** The `P03_prompt` pillar defines the kind, but N02 has zero instances. | Low |
| High | **Missing advanced prompt patterns.** Kinds like `chain`, `reasoning_trace`, and `context_window_config` are unused, limiting sophistication. | Medium |
| High | **8F Protocol is not followed.** No artifacts declare or document the 8F pipeline, indicating a process compliance failure. | High |
| Medium | **No campaign-level artifacts.** There are no `creative_brief` or `marketing_campaign` artifacts to group and direct lower-level copy generation. | Medium |
| Low | **Brand voice not explicitly defined.** While brand audit tools exist, there is no central `brand_voice_guide` artifact within N02 to act as a source of truth. | Low |

## 4. Fixes Needed

The nucleus is technically healthy but has process and content debt.

- **Artifacts below 8.0:** **None.** All scored artifacts are 9.0 or higher.
- **Frontmatter violations:** **None.** `cex_doctor.py` reported `123 PASS | 0 WARN | 0 FAIL`.
- **Broken chain artifacts:** **None.** The `chain` kind is not used.
- **Old Brand / Taxonomy References:** **Unknown.** This requires manual review against a defined brand guide, which is a noted gap.

## 5. Tool Wishlist

### 5a. Existing Tools to Adopt
| Tool | Use Case for N02 |
|------|------------------|
| `brand_audit.py` | To programmatically enforce brand voice consistency across all generated copy. |
| `cex_evolve.py` | To set up autonomous A/B testing loops for critical artifacts like ad copy and headlines. |
| `cex_prompt_optimizer.py`| To systematically refine core `prompt_template` artifacts for better efficiency and creativity. |

### 5b. Proposed New Tools
| Tool Name | Description | Builder Nucleus |
|-----------|-------------|-----------------|
| `cex_audience_persona_generator.py` | Generates a detailed user persona from a demographic description to improve targeting. | N01 (Research) |
| `cex_campaign_briefer.py` | Interactive tool to generate a complete `creative_brief` artifact, ensuring structured campaign initiation. | N02 (Marketing) |
| `cex_seo_keyword_optimizer.py`| Suggests copy edits to improve on-page SEO against a target keyword. | N02/N06 |
| `cex_tone_lint.py` | Linter that checks generated copy against a `brand_voice_guide` artifact for compliance. | N02 |

## 6. Cross-Nucleus Dependencies

### N02 Needs From Others
| Nucleus | Artifact/Service Needed |
|---------|-------------------------|
| N01 | Market research, competitor analysis, user personas. |
| N06 | `brand_config.yaml`, monetization goals, target audience definitions. |
| N07 | Mission dispatch and orchestration. |
| Pillars | Schema and kind definitions (e.g., from `P03_prompt`). |

### Others Need From N02
| Nucleus | Artifact/Service Needed | Evidence |
|---------|-------------------------|----------|
| N04 | Awareness of N02 structure for architectural specs. | `N04_knowledge/architecture/task_queue_spec.md` references N02. |
| N03, N05 | *Potentially* consumes prompt templates or copy, but no direct file references were found. This suggests a **dependency gap** where other nuclei may be recreating marketing-related logic instead of consuming it from N02. | No cross-references found in `N03_builder/`. |
