---
id: p11_qg_marketing_artifacts
kind: quality_gate
8f: F7_govern
pillar: P11
title: "Gate: Marketing Artifacts"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "quality-gate-builder"
domain: "marketing"
quality: 9.1
tags: [quality-gate, marketing, N02, brand-voice, conversion, pre-publish]
tldr: "Pre-publish gate for marketing artifacts: 8 HARD checks + 5-dimension scoring >= 8.5"
density_score: 0.91
related:
  - p11_qg_creation_artifacts
  - p11_qg_brand_artifacts
  - p11_qg_engineering_artifacts
  - p11_qg_orchestration_artifacts
  - p11_qg_intelligence_artifact
  - p11_qg_quality_gate
  - p11_qg_response_format
  - p11_qg_chunk_strategy
  - p11_qg_prompt_template
  - bld_knowledge_card_quality_gate
---
## Definition

| Property | Value |
|----------|-------|
| Metric | marketing_quality_score |
| Threshold | 8.5 |
| Operator | >= |
| Scope | All marketing artifacts produced by N02 before pool merge or publication |

## HARD Gates

Failure on any single gate sets final score to 0 and blocks pool merge immediately.

| ID  | Criterion | Failure Action |
|-----|-----------|----------------|
| H01 | YAML frontmatter parses without syntax errors | block |
| H02 | `id` matches pattern `p{nn}_{kind}_{slug}` — no uppercase, no spaces | block |
| H03 | `id` value equals filename stem exactly (case-sensitive) | block |
| H04 | `kind` field matches a literal registered in `kinds_meta.json` | block |
| H05 | `quality` field is null at authoring time (self-scoring forbidden) | block |
| H06 | All required frontmatter fields present and non-empty: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | block |
| H07 | At least one explicit target audience segment is defined in the body | block |
| H08 | At least one concrete, measurable CTA or conversion goal is present | block |

## SOFT Scoring

Score each dimension 0.0 (absent/fails) to 1.0 (present/passes). Apply weight, sum, normalize.

| ID  | Dimension | Weight | Scoring Method | Criteria |
|-----|-----------|--------|----------------|----------|
| S01 | Brand Voice Alignment | 25% | graduated | Tone, vocabulary, and personality match `brand_config.yaml` — formal/casual register, preferred terms, prohibited terms; 0 if no brand signals present |
| S02 | Conversion Clarity | 25% | graduated | CTA is specific (verb + object + channel), audience need is named, offer value is stated; deduct 0.33 per missing element |
| S03 | Completeness | 20% | binary | All sections required by the artifact kind's output template are present and non-empty; 0 if any required section is absent |
| S04 | Content Density | 20% | graduated | `density_score` >= 0.80 and body contains no filler phrases ("in order to", "it is important to note", "as we all know"); deduct 0.25 per filler occurrence beyond 1 |
| S05 | Structural Compliance | 10% | binary | Artifact follows the N02 format convention for its kind (headers, table format, character limits per section); 0 if format deviates |

**Formula**: `final_score = SUM(score_i × weight_i) × 10`
Weight total: 100%. PASS condition: all HARD gates pass AND `final_score >= 8.5`.

## Actions

| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Merge to pool as golden reference; flag for N06 monetization use |
| PUBLISH | >= 8.5 | Merge to pool; mark production-ready for campaign deployment |
| REVIEW | >= 7.0 | Return to N02 with scored dimension breakdown; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |

## Bypass

| Field | Value |
|-------|-------|
| condition | Score in REVIEW band (7.0–8.4) for a time-critical campaign launch where deadline is < 24 hours |
| approver | Brand owner must approve in writing (Slack or email) before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver identity, campaign name, score at bypass, and reason |
| expiry | Bypass valid for the single campaign only; artifact must reach PUBLISH score before next use |

H01 (YAML parse) and H05 (quality null) cannot be bypassed under any condition.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_creation_artifacts]] | sibling | 0.69 |
| [[p11_qg_brand_artifacts]] | sibling | 0.61 |
| [[p11_qg_engineering_artifacts]] | sibling | 0.57 |
| [[p11_qg_orchestration_artifacts]] | sibling | 0.56 |
| [[p11_qg_intelligence_artifact]] | sibling | 0.55 |
| [[p11_qg_quality_gate]] | sibling | 0.48 |
| [[p11_qg_response_format]] | sibling | 0.44 |
| [[p11_qg_chunk_strategy]] | sibling | 0.38 |
| [[p11_qg_prompt_template]] | sibling | 0.36 |
| [[bld_knowledge_card_quality_gate]] | related | 0.36 |
