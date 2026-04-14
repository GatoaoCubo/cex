---
id: p11_qg_multi_modal_config
kind: quality_gate
pillar: P11
title: "Gate: Multi-Modal Config"
version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "n04_knowledge"
domain: "multi_modal_config — input format, resolution, and routing for multi-modal LLM interactions"
quality: 9.0
tags: [quality-gate, multi-modal-config, modality, routing, resolution]
tldr: "Gates ensuring multi_modal_config artifacts have explicit modalities, format constraints, routing, and cost estimates."
density_score: 0.90
llm_function: GOVERN
---
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
