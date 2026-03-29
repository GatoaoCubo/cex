---
id: p11_qg_knowledge_nucleus
kind: quality_gate
pillar: P11
title: "Gate: Knowledge Nucleus"
version: "1.0.0"
created: "2023-10-08"
updated: "2023-10-08"
author: "quality-gate-builder"
domain: "knowledge_card"
quality: null
tags: [quality-gate, knowledge, pre-publish]
tldr: "Pre-publish quality gate for Knowledge Nucleus ensuring completeness, correctness, and relevance."
density_score: 0.85

---

## Definition
| Property | Value |
|----------|-------|
| Metric | aggregate_score |
| Threshold | 0.8 |
| Operator | >= |
| Scope | All knowledge_card artifacts before publication |

## Hard Gates
| Gate ID | Description | Threshold | Block |
|---------|-------------|-----------|-------|
| H01     | YAML parses without error | N/A | true |
| H02     | ID follows the pattern p11_qg_ | N/A | true |
| H03     | ID matches filename stem | N/A | true |
| H04     | 'kind' is defined as 'knowledge_card' | N/A | true |
| H05     | 'quality' field is null | N/A | true |
| H06     | Required fields present in frontmatter | N/A | true |

## Soft Gates
| Gate ID | Description | Max Penalty | Weight |
|---------|-------------|-------------|--------|
| S01     | Completeness: All necessary information and sections are included | 0.2 | 30% |
| S02     | Correctness: Information is accurate and verified | 0.2 | 40% |
| S03     | Relevance: Content is pertinent to topic and audience | 0.1 | 30% |

## Scoring Formula
final_score = (S01 * 0.30) + (S02 * 0.40) + (S03 * 0.30)

## Bypass Policy
- Who can override: Admin
- Condition: When artifact is critical for an immediate operational requirement
- Audit Requirement: Override must be logged with timestamp, actor, and justification

## Audit Trail
- What is logged per evaluation: Gate ID, pass/fail status, rationale for any soft penalties
- Retention Policy: Logs will be stored for one year for audit and review purposes

The quality gate for the Knowledge Nucleus ensures that the knowledge_cards are thoroughly vetted for completeness, correctness, and relevance before being approved for publication. Hard gates provide non-negotiable structural checks, while soft gates offer a nuanced scoring system weighted according to the artifact's attributes. The inclusion of a robust bypass policy ensures flexibility in critical cases, guarded by stringent audit requirements to maintain process integrity.