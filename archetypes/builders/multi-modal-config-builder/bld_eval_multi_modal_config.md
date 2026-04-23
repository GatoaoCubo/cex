---
kind: quality_gate
id: p11_qg_multi_modal_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of multi_modal_config artifacts
pattern: few-shot learning — LLM reads these before producing
updated: "2026-04-07"
domain: "multi_modal_config — input format, resolution, and routing for multi-modal LLM interactions"
title: "Gate: Multi-Modal Config"
version: "1.0.0"
author: "n04_knowledge"
created: "2026-04-07"
density_score: 0.90
tldr: "Gates ensuring multi_modal_config artifacts have explicit modalities, format constraints, routing, and cost estimates."
quality: 9.0
tags: [quality-gate, multi-modal-config, modality, routing, resolution]
related:
  - bld_examples_multi_modal_config
  - bld_instruction_multi_modal_config
  - p03_sp_multi_modal_config_builder
  - bld_output_template_multi_modal_config
  - bld_collaboration_multi_modal_config
  - multi-modal-config-builder
  - p01_kc_multi_modal_config
  - bld_schema_multi_modal_config
  - bld_config_multi_modal_config
  - bld_architecture_multi_modal_config
---

## Quality Gate

# Gate: Multi-Modal Config
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: multi_modal_config` |
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | ID matches `^p04_mmc_[a-z][a-z0-9_]+$` | Wrong prefix |
| H03 | Kind equals literal `multi_modal_config` | Wrong kind |
| H04 | Quality field is `null` | Non-null value |
| H05 | supported_modalities is non-empty list | Missing or empty |
| H06 | Modality values are valid enums | Not in image/audio/video/document/text |
| H07 | Format constraints present for each modality | Missing formats |
| H08 | Total file <= 2048 bytes | Exceeds limit |
## SOFT Scoring
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Resolution limits | 1.0 | Per-modality limits set | Partial limits | No limits |
| S02 | Routing map | 1.0 | Complete modality→model mapping | Partial routing | No routing |
| S03 | Token cost estimates | 1.0 | Per-modality costs documented | Partial | None |
| S04 | Preprocessing pipeline | 1.0 | Steps per modality | Some steps | No preprocessing |
| S05 | Fallback chain | 0.5 | Fallback for unsupported modalities | Partial | None |
| S06 | Format validation | 0.5 | Accepted formats listed per modality | Some listed | None |

## Cross-References

- **Pillar**: P11 (Feedback)
- **Kind**: `quality gate`
- **Artifact ID**: `p11_qg_multi_modal_config`
- **Tags**: [quality-gate, multi-modal-config, modality, routing, resolution]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P11 | Feedback domain |
| Kind `quality gate` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Examples

# Examples: multi-modal-config-builder
## Golden Example
INPUT: "Create multi-modal config for document analysis with Claude"
OUTPUT:
```yaml
---
id: p04_mmc_document_analysis
kind: multi_modal_config
pillar: P04
title: "Document Analysis Multi-Modal Config"

version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "multi-modal-config-builder"
supported_modalities: [image, document, text]

image_max_resolution: "2048x2048"
image_format: [png, jpg, webp, gif]
preprocessing: [resize, compress]
routing_model:
  image: claude-sonnet-4-20250514

  document: claude-sonnet-4-20250514
  text: claude-sonnet-4-20250514
token_cost_estimate:
  image_1024: 750
  image_2048: 1500

  document_page: 1200
domain: document_processing
quality: 9.0
tags: [multi_modal_config, document, image, analysis]
tldr: "Document analysis: image+PDF via Claude Sonnet, max 2048px, ~1500 tokens/image, resize preprocessing"
---
```
WHY THIS IS GOLDEN:
1. quality: null
2. supported_modalities explicit
3. Resolution limits set
4. Routing map present
5. Token costs estimated
6. Preprocessing defined

## Anti-Example
BAD OUTPUT:
```yaml
id: modal_cfg
supported_modalities: all
image_max_resolution: unlimited
quality: 8.0
```
FAILURES:
1. id: no p04_mmc_ prefix
2. supported_modalities: "all" not valid — must be explicit list
3. Resolution: "unlimited" burns budget

4. quality: not null
5. No routing, no preprocessing, no token costs

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | examples artifact construction |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
