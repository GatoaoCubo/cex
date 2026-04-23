---
id: kno_competitive_matrix_n01
kind: competitive_matrix
pillar: P01
nucleus: N01
title: "N01 Competitive Matrix"
version: "1.0.0"
quality: 9.0
tags: [competitive_matrix, n01, p01, analytical_envy, comparison]
density_score: 0.97
related:
  - p06_schema_competitive_analysis
  - p02_nd_n01.md
  - p03_sp_competitive_matrix_builder
  - p02_agent_competitor_tracker
  - bld_knowledge_card_competitive_matrix
  - competitive-matrix-builder
  - bld_config_competitive_matrix
  - n06_kc_competitive_positioning
  - bld_instruction_competitive_matrix
  - p02_card_intelligence
---
<!-- 8F: F1=competitive_matrix/P01 F2=kc_competitive_matrix+competitive_analysis_contract F3=nucleus_def_n01+competitive_analysis_contract+agent_competitor_tracker+kc_competitive_matrix F4=decision-grade battle card matrix
     F5=rg+Get-Content+apply_patch F6=target dense markdown artifact F7=self-check properties+8F+ascii+80lines F8=N01_intelligence/P01_knowledge/kno_competitive_matrix_n01.md -->

# N01 Competitive Matrix

## Purpose
The N01 matrix is built to force positioning clarity.
Analytical Envy means the matrix should reveal where a rival is stronger, where they are weaker, and which claims survive evidence review.
A matrix that flatters everyone is not intelligence.

## Properties

| Property | Value |
|----------|-------|
| Kind | `competitive_matrix` |
| Pillar | `P01` |
| Nucleus | `N01` |
| Lens | `Analytical Envy` |
| Canonical contract | `competitive_analysis_contract` |
| Primary outputs | battle cards, procurement briefs, positioning notes |
| Standard row count | 5 to 8 competitors |
| Standard column count | 8 to 14 dimensions |
| Refresh cadence | quarterly or on major product launch |
| Evidence rule | every volatile field should map to citation(s) |

## Matrix Thesis
N01 does not compare products to summarize the market.
N01 compares products to create strategic pressure.
Each row should make a decision easier:
- how to position
- what to copy
- what to avoid
- where to sell against
- where not to overclaim

## Core Dimensions

| Dimension | Why it exists |
|-----------|---------------|
| vendor | stable identity anchor |
| positioning | one-sentence market claim |
| target_segment | who they win with |
| pricing_model | monetization logic |
| price_range | economic pressure point |
| top_features | what they advertise and ship |
| strengths | where they genuinely outperform |
| weaknesses | where they leave openings |
| deployment_model | cloud, on-prem, hybrid, self-hosted |
| proof_quality | strength of the available evidence |
| switching_cost | procurement friction |
| threat_level | practical urgency for response |

## N01-Specific Columns
Generic competitive grids stop too early.
N01 adds pressure columns that matter for action.

| Column | Function |
|--------|----------|
| claim_confidence | how defensible the row is given current citations |
| freshness_window | whether data is still decision-grade |
| beat_strategy | how to win against the competitor |
| lose_condition | where the competitor should be favored |
| unresolved_questions | what still needs research before using the row in external collateral |

## Scoring Pattern
The matrix should support qualitative synthesis and lightweight scoring.

| Axis | Range | Interpretation |
|------|-------|----------------|
| market_fit | 1-5 | suitability for target buyer |
| evidence_strength | 1-5 | citation quality and recency |
| feature_depth | 1-5 | breadth plus maturity |
| commercial_pressure | 1-5 | pricing and procurement threat |
| differentiation_gap | -2 to 2 | negative means rival leads, positive means we lead |

## Build Rules
1. Limit to direct competitors unless a category creator or substitute clearly affects deals.
2. Use one time window for all rows when comparing volatile facts.
3. Separate vendor claims from third-party verification.
4. Keep opinions out unless labeled as hypotheses.
5. Distinguish unknown from weak.
6. If evidence is mixed, show mixed.
7. Record the buyer context that makes the comparison valid.

## Battle Card Orientation
An N01 matrix is meant to feed downstream sales and strategy artifacts.

| Use case | Matrix emphasis |
|----------|-----------------|
| sales battle card | objections, weaknesses, beat strategy |
| procurement evaluation | proof quality, deployment, cost, risk |
| product roadmap | strengths to match, weaknesses to exploit |
| investor or board brief | market structure, segment coverage, threat level |

## Example Decision Questions
- Against whom do we have the cleanest value-for-money story.
- Which rival has the strongest evidence-backed differentiation.
- Where is the market crowded but weakly served.
- Which competitor looks strong only because the data is stale or self-reported.
- Which gap is strategic versus merely cosmetic.

## Red-Team Rules
Analytical Envy requires adversarial reading of the matrix.

| Check | Failure sign |
|-------|--------------|
| Row symmetry | every competitor looks conveniently average |
| Citation pressure | prices or features lack dates and URLs |
| Positioning clarity | segment blur makes row non-actionable |
| Loss honesty | no row records where the rival actually wins |
| Freshness | recent launch data missing in fast-moving categories |

## Anti-Patterns
- twelve weak competitors instead of six real ones
- pricing columns with mixed currencies and periods
- strengths copied from marketing copy without proof
- no explicit target segment
- AI-powered treated as differentiator
- no note on what evidence is missing

## Recommended Markdown Shape
1. Matrix objective and buyer context.
2. Competitor table.
3. Evidence notes by row.
4. N01 synthesis.
5. Beat strategies.
6. Open research gaps.

## N01 Decision
The competitive matrix is not a spreadsheet artifact.
It is a strategic instrument that turns scattered market observations into ranked pressure.
When built correctly, it tells N01 where envy is justified, where it is misplaced, and where advantage can be created faster than the market notices.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_schema_competitive_analysis]] | downstream | 0.25 |
| [[p02_nd_n01.md]] | downstream | 0.24 |
| [[p03_sp_competitive_matrix_builder]] | downstream | 0.23 |
| [[p02_agent_competitor_tracker]] | downstream | 0.22 |
| [[bld_knowledge_card_competitive_matrix]] | related | 0.22 |
| [[competitive-matrix-builder]] | related | 0.22 |
| [[bld_config_competitive_matrix]] | downstream | 0.22 |
| [[n06_kc_competitive_positioning]] | related | 0.22 |
| [[bld_instruction_competitive_matrix]] | downstream | 0.21 |
| [[p02_card_intelligence]] | downstream | 0.20 |
