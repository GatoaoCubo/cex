---
kind: schema
id: bld_schema_bias_audit
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for bias_audit
quality: 9.2
title: "Schema Bias Audit"
version: "1.1.0"
author: n06_hybrid_review
tags: [bias_audit, builder, schema]
tldr: "Formal schema for bias_audit artifacts -- adds benchmarks_used, jurisdiction_applicability, audit_tool fields; fixes pillar inconsistency (P07 throughout)."
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
---

## Frontmatter Fields

This ISO drives a bias audit: measuring fairness across demographic slices.

### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | - | Unique identifier, pattern: ^p07_ba_[a-zA-Z0-9_]+$ |
| kind | string | yes | "bias_audit" | CEX kind |
| pillar | string | yes | "P07" | Evaluation pillar -- always P07 for bias_audit |
| title | string | yes | - | Audit title |
| version | string | yes | "1.0.0" | Semantic versioning |
| created | date | yes | - | ISO 8601 format |
| updated | date | yes | - | ISO 8601 format |
| author | string | yes | - | Auditor name or team |
| domain | string | yes | - | Application domain (e.g., "HR AI", "credit scoring") |
| quality | string | yes | null | Never self-score -- peer review assigns |
| tags | list | yes | [] | Lowercase keywords |
| tldr | string | yes | - | One-sentence summary |
| bias_types | list | yes | [] | Types present: algorithmic, data, interaction, evaluation |
| affected_groups | list | yes | [] | Protected attributes audited: race, gender, age, religion, disability, national_origin, sexual_orientation |
| benchmarks_used | list | yes | [] | Named benchmarks applied: BBQ, WinoBias, StereoSet, BOLD, HolisticBias, Winogender |
| audit_tool | string | yes | - | Primary tool: IBM_AIF360, Fairlearn, Aequitas, custom |
| jurisdiction_applicability | list | yes | [] | Laws applicable: EU_AI_Act, NYC_LL144, Colorado_SB22169, AIVIA, ECOA |

### Recommended
| Field | Type | Notes |
|-------|------|-------|
| mitigation_steps | list | Actions taken / recommended to address bias |
| audit_date | date | ISO 8601: date audit was executed |
| model_version | string | Audited model version identifier |
| dataset_version | string | Audited dataset version or hash |
| statistical_significance_threshold | float | p-value threshold used (default: 0.05) |
| disparate_impact_threshold | float | EEOC 4/5 rule threshold (default: 0.80) |
| independent_auditor | bool | True if conducted by independent party (required for NYC LL144) |
| public_summary_url | string | URL of public summary (required by NYC LL144) |

## ID Pattern
^p07_ba_[a-zA-Z0-9_]+\.md$

## Body Structure
1. **Overview** -- purpose, scope, deployment context, audit trigger (pre-deployment / periodic / incident)
2. **Methodology** -- tools used (name + version), datasets, evaluation criteria, statistical methods, significance thresholds
3. **Findings** -- disparity metrics table per protected attribute and benchmark; raw numbers, p-values, effect sizes
4. **Jurisdiction Compliance** -- per-law checklist (NYC LL144 impact ratio, Colorado SB 22-169 high-risk classification)
5. **Recommendations** -- mitigation strategy with expected disparity reduction, accuracy-fairness tradeoff analysis
6. **Stakeholder Impact** -- business impact, legal exposure, public summary (if NYC LL144 applies)

## Constraints
- All required fields must be present and non-null.
- pillar MUST be "P07" (not P06, not P11).
- quality MUST be null (never self-score).
- benchmarks_used MUST contain at least one named benchmark from: BBQ, WinoBias, StereoSet, BOLD, HolisticBias, Winogender.
- affected_groups MUST list at least one protected attribute.
- Version must follow semantic versioning (MAJOR.MINOR.PATCH).
- File size must not exceed 5120 bytes.
- Tags must be lowercase.
