---
kind: quality_gate
id: p10_qg_c2pa_manifest
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for c2pa_manifest
quality: 9.0
title: "Quality Gate C2PA Manifest"
version: "1.0.0"
author: n04_wave7
tags: [c2pa_manifest, builder, quality_gate, C2PA, content-credential, AI-ML-generator, claim, assertion, ingredient, signature]
tldr: "Quality gate with HARD and SOFT scoring for c2pa_manifest"
domain: "c2pa_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| C2PA 2.3 spec compliance | 100% | equals | All HARD gates |

## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing fields |
| H02 | ID matches pattern ^p10_cm_[a-z][a-z0-9_]+\.md$ | ID format mismatch |
| H03 | kind field is "c2pa_manifest" | Kind field incorrect or missing |
| H04 | content_format is valid IANA MIME type | Non-IANA or missing MIME type |
| H05 | digital_source_type is trainedAlgorithmicMedia or compositeSynthetic | Unknown or missing DST |
| H06 | c2pa.ai_generator assertion present for AI-generated content | Missing AI attribution assertion |
| H07 | signer_id is X.509 CN or DID | Invalid or missing signer reference |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Claim completeness (format, assertions, signature_info) | 0.25 | All present = 1.0, partial = 0.5, missing critical = 0 |
| D02 | AI assertion quality (digitalSourceType, model, prompt present) | 0.25 | Full attribution = 1.0, partial = 0.5, absent = 0 |
| D03 | Ingredient coverage (hashes present for all referenced sources) | 0.20 | All hashed = 1.0, partial = 0.5, none = 0 |
| D04 | Signature binding (signer cert/DID reference valid) | 0.20 | Valid reference = 1.0, placeholder = 0.5, absent = 0 |
| D05 | Domain keyword density (C2PA, content-credential, claim, assertion, ingredient, signature, AI-ML-generator) | 0.10 | 7+ keywords = 1.0, 5-6 = 0.7, <5 = 0.3 |

## Actions
| Score | Action |
|-------|--------|
| GOLDEN | >=9.5 | Auto-publish with no review |
| PUBLISH | >=8.0 | Auto-publish after validation |
| REVIEW | >=7.0 | Require manual review |
| REJECT | <7.0 | Reject and flag for correction |

## Bypass
| Conditions | Approver | Audit Trail |
|------------|----------|-------------|
| Prototype manifest (no live signer) | N07 orchestrator | Escalation log with PROTOTYPE tag |
