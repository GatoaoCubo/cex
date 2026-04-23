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
related:
  - bld_examples_c2pa_manifest
  - bld_instruction_c2pa_manifest
  - c2pa-manifest-builder
  - p03_sp_c2pa_manifest_builder
  - bld_knowledge_card_c2pa_manifest
  - p10_lr_c2pa_manifest_builder
  - bld_output_template_c2pa_manifest
  - bld_schema_c2pa_manifest
  - p10_qg_vc_credential
  - bld_tools_c2pa_manifest
---

## Quality Gate

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

## Examples

## Golden Example
```json
{
  "manifests": {
    "cex:firefly-campaign-banner": {
      "claim_generator": "CEX-N02-Marketing/1.0 c2pa-rs/0.36",
      "title": "Black Friday Campaign Banner 2026",
      "format": "image/jpeg",
      "instance_id": "xmp:iid:f3a9b2c1-d4e5-4f6a-8b7c-9d0e1f2a3b4c",
      "ingredients": [],
      "assertions": [
        {
          "label": "c2pa.ai_generator",
          "data": {
            "digitalSourceType": "trainedAlgorithmicMedia",
            "generatorModel": {
              "name": "Adobe Firefly",
              "version": "3.0"
            },
            "promptText": "Black Friday sale banner, dark background, gold typography, shopping bags, 4K"
          }
        },
        {
          "label": "c2pa.training-mining",
          "data": {
            "dataType": "trainedAlgorithmicMedia",
            "entries": [
              {"uri": "https://firefly.adobe.com/training-data-manifest", "alg": "sha256", "hash": "a1b2c3..."}
            ]
          }
        }
      ],
      "signature_info": {
        "issuer": "Adobe Inc.",
        "cert_serial_number": "0x1234ABCD"
      }
    }
  },
  "active_manifest": "cex:firefly-campaign-banner"
}
```

## Anti-Example 1: Missing AI Generator Assertion
```json
{
  "manifests": {
    "unknown:manifest": {
      "title": "Generated Image",
      "format": "image/png",
      "assertions": []
    }
  }
}
```
**Why it fails**: No c2pa.ai_generator assertion. C2PA 2.2+ requires AI-ML generator attribution for AI-generated content. Empty assertions array provides no provenance information to content consumers or auditors.

## Anti-Example 2: Missing Ingredient Hashes
```json
{
  "assertions": [
    {
      "label": "c2pa.ingredient",
      "data": {
        "title": "Source Image",
        "relationship": "parentOf"
      }
    }
  ]
}
```
**Why it fails**: Ingredient assertion without content hash. Without SHA-256 hash binding the ingredient reference to actual file content, the provenance chain is unverifiable and can be spoofed.

## Anti-Example 3: Non-IANA MIME Type
```json
{"format": "jpg"}
```
**Why it fails**: "jpg" is not an IANA MIME type. Must be "image/jpeg". Invalid format breaks manifest parsing in all C2PA-compliant readers (Adobe, Nikon, Canon, Microsoft).

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
