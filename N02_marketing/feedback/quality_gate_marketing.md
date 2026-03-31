---
id: p11_qg_marketing_nucleus
kind: quality_gate
pillar: P11
title: "Gate: Marketing Copy Quality"
version: 3.0.0
created: 2026-03-30
updated: 2026-03-31
author: n02_marketing
domain: copywriting_and_campaigns
quality: 8.9
tags: [quality_gate, marketing, copy, N02, P11]
tldr: 8 HARD gates (frontmatter, structure, CTA, A/B variants) + 5 SOFT dimensions for marketing copy — threshold 8.0
density_score: 0.89
---

# Gate: Marketing Copy Quality

## Purpose

Validates that N02 copy output meets minimum quality standards before publication.
Applies to all N02 deliverables: ads, emails, landing pages, social posts, campaign briefs.

## Hard Gates (BLOCK if fail)

| gate_id | Description | Threshold | Blocks |
|---------|-------------|-----------|--------|
| H01 | Frontmatter parses without YAML error | N/A | YES |
| H02 | ID matches pattern for artifact kind | kind-specific | YES |
| H03 | quality field is null (no self-score) | quality: null | YES |
| H04 | Funnel stage declared (awareness/consideration/decision) | present | YES |
| H05 | At least 1 CTA present and non-generic | not "Click here" / "Learn more" | YES |
| H06 | A/B variants present for headlines (min 3) | count >= 3 | YES |
| H07 | Artifact size within limit | <= 8192 bytes | YES |
| H08 | No unverified superlatives without [PROOF NEEDED] tag | 0 unmarked superlatives | YES |

## Soft Gates (SCORE penalties)

| gate_id | Description | Max Penalty | Weight |
|---------|-------------|-------------|--------|
| S01 | Hook quality — first 10 words create curiosity or tension | -2.0 | 25% |
| S02 | CTA specificity — names benefit AND action | -1.5 | 20% |
| S03 | Readability — Flesch-Kincaid >= 60 for B2C, >= 40 for B2B | -1.5 | 20% |
| S04 | Brand voice alignment — matches provided voice card | -2.0 | 20% |
| S05 | Density — no padding, every sentence earns its place | -1.0 | 15% |

## Scoring Formula

```
soft_score = SUM(dimension_score * weight for S01–S05)
final_score = soft_score (0–10 scale)
PASS = all HARD gates pass AND final_score >= 8.0
```

## Tier Thresholds

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Save as example in N02_marketing/output/examples/ |
| PUBLISH | >= 8.0 | Approve for delivery to client/campaign |
| REVIEW | >= 7.0 | Return to F6 with specific dimension feedback |
| REJECT | < 7.0 | Full redo — restart F4 with new formula choice |

## Bypass Policy

- **Who may override**: n07-orchestrator only
- **Conditions**: score between 7.5–8.0 AND explicit human approval AND urgent deadline
- **Audit requirement**: note bypass in commit message `[BYPASS score=7.x reason=...]`

## Quick Validation Script

```python
# Run against any N02 copy deliverable
def validate_n02_copy(artifact_text, frontmatter):
    hard_gates = {
        "H01": is_valid_yaml(frontmatter),
        "H02": id_matches_kind_pattern(frontmatter),
        "H03": frontmatter.get("quality") is None,
        "H04": funnel_stage_declared(artifact_text),
        "H05": has_specific_cta(artifact_text),
        "H06": count_headline_variants(artifact_text) >= 3,
        "H07": len(artifact_text.encode()) <= 8192,
        "H08": no_unmarked_superlatives(artifact_text),
    }
    return all(hard_gates.values()), hard_gates
```

## Audit Trail

Each evaluation logs:
- Gate ID and result (pass/fail)
- Specific failing criterion
- Timestamp (UTC)
- Score by dimension
- Revision instructions for S-gate failures

Retention: logs kept in `N02_marketing/output/` per mission.

## Common Failure Patterns

| Failure | Gate | Most Common Cause | Fix |
|---------|------|------------------|-----|
| quality: 8.x set | H03 | Self-scoring after generation | Set `quality: null` always |
| CTA = "Click here" | H05 | Default phrasing used | Rewrite: "[Verb] my [benefit]" |
| Only 1 headline | H06 | Single variant produced | Generate 3 variants minimum |
| No funnel stage | H04 | Stage not declared | Add funnel_stage line to output header |
| Superlative without proof | H08 | "Best" / "The only" used | Add [PROOF NEEDED] or rewrite to specific claim |
