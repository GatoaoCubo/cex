---
id: p11_qg_brand_artifacts
kind: quality_gate
pillar: P11
title: "Gate: Brand Artifacts"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "quality-gate-builder"
domain: "brand"
target_kind: "brand_config,brand_template,brand_guideline"
delivery_threshold: 8.0
bypass_policy: "owner"
dimensions: ["consistency", "completeness", "visual_coherence", "voice_alignment", "legal_compliance", "implementation"]
quality: 8.9
tags: [quality-gate, brand, governance, consistency, guidelines]
tldr: "Pre-publish gate for brand artifacts: ensures brand consistency, completeness, and implementation readiness with 8.0+ score threshold."
density_score: 0.88
---
## Definition
| Property | Value |
|----------|-------|
| Metric | weighted_brand_score |
| Threshold | 8.0 |
| Operator | >= |
| Scope | All brand-related artifacts before pool integration or external publication |

## HARD Gates
All gates must pass. Single failure blocks delivery regardless of soft score.

| ID | Criterion | Failure Action |
|----|-----------|----------------|
| H01 | YAML frontmatter parses without error | block |
| H02 | ID matches pattern `p11_qg_*` or domain-specific namespace | block |
| H03 | ID equals filename stem exactly | block |
| H04 | Kind field matches expected artifact type | block |
| H05 | Quality field is null at authoring time | block |
| H06 | All required frontmatter fields present and non-empty | block |
| H07 | Brand config reference present and valid | block |
| H08 | No conflicting brand directives within artifact | block |

## SOFT Gates
Weighted scoring dimensions contributing to final quality score.

| ID | Criterion | Weight | Scoring Method |
|----|-----------|--------|----------------|
| S01 | Brand consistency with `.cex/brand/brand_config.yaml` | 1.0 | graduated |
| S02 | Completeness of required brand elements (colors, fonts, voice) | 1.0 | graduated |
| S03 | Visual coherence across all brand touchpoints | 1.0 | graduated |
| S04 | Voice and tone alignment with brand personality | 1.0 | graduated |
| S05 | Legal compliance (trademark usage, copyright notices) | 1.0 | binary |
| S06 | Implementation readiness with actionable guidelines | 0.5 | graduated |
| S07 | Cross-platform compatibility considerations | 0.5 | graduated |

## Scoring Formula
```
aggregate_score = (S01*1.0 + S02*1.0 + S03*1.0 + S04*1.0 + S05*1.0 + S06*0.5 + S07*0.5) / 6.0
final_score = all_hard_gates_pass ? aggregate_score * 10 : 0
```
Weight total: 6.0. Pass condition: all HARD gates pass AND aggregate_score >= 0.80

## Actions
| Outcome | Consequence |
|---------|-------------|
| GOLDEN (>= 9.5) | Publish to brand pool as reference standard; use for onboarding templates |
| PUBLISH (>= 8.0) | Approve for production use; integrate into brand system |
| REVIEW (>= 7.0) | Return with dimension feedback; one revision cycle permitted |
| REJECT (< 7.0) | Block from brand pool; requires substantial rework before re-evaluation |

## Bypass Policy
| Field | Specification |
|-------|---------------|
| **Condition** | Emergency brand update required for legal compliance or crisis response |
| **Approver** | Brand owner or designated brand steward with written authorization |
| **Audit Log** | Record in `.cex/runtime/audits/brand_bypasses.md` with timestamp, approver signature, and business justification |
| **Expiry** | 72 hours from bypass activation; artifact must achieve full compliance within window |

**Non-bypassable gates**: H01 (YAML validity), H05 (quality null), H07 (brand config reference) - these ensure basic structural integrity and prevent self-scoring violations.