---
id: p11_qg_citation
kind: quality_gate
pillar: P11
title: "Gate: Citation"
version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "n04_knowledge"
domain: "citation — structured source attribution with provenance"
quality: 9.0
tags: [quality-gate, citation, provenance, attribution, reliability]
tldr: "Gates ensuring citation artifacts have verifiable provenance, reliability tier, excerpt, and temporal freshness."
density_score: 0.90
llm_function: GOVERN
---
# Gate: Citation
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: citation` |
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | ID matches `^p01_cit_[a-z][a-z0-9_]+$` | Wrong prefix or format |
| H03 | ID equals filename stem | Mismatch |
| H04 | Kind equals literal `citation` | Wrong kind |
| H05 | Quality field is `null` | Non-null value |
| H06 | source_type is valid enum | Not in web/paper/book/internal/api |
| H07 | reliability_tier is valid enum | Not in tier_1/tier_2/tier_3 |
| H08 | url is present and non-empty | Missing URL |
| H09 | date_accessed is present | Missing access date |
| H10 | excerpt is 1-3 sentences | Empty or too long |
| H11 | Total file <= 2048 bytes | Exceeds limit |
## SOFT Scoring
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Excerpt concreteness | 1.0 | Specific numbers, dates, named entities | Partial specifics | Vague summary |
| S02 | Reliability classification | 1.0 | Tier matches source type correctly | Reasonable but debatable | Wrong tier |
| S03 | Relevance mapping | 0.5 | relevance_scope with 2+ specific domains | 1 domain | No mapping |
| S04 | Temporal freshness | 0.5 | Freshness policy defined with days | Date only | No temporal info |
| S05 | Verification completeness | 1.0 | URL + DOI/ISBN + access date | URL + date | URL only |
| S06 | Body structure | 1.0 | All 5 sections present with content | 3-4 sections | Fewer |

## Cross-References

- **Pillar**: P11 (Feedback)
- **Kind**: `quality gate`
- **Artifact ID**: `p11_qg_citation`
- **Tags**: [quality-gate, citation, provenance, attribution, reliability]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P11 | Feedback domain |
| Kind `quality gate` | Artifact type |
| Pipeline | 8F (F1→F8) |
