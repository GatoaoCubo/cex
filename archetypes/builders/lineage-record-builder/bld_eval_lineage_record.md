---
id: bld_quality_gate_lineage_record
kind: quality_gate
pillar: P07
title: "Gate: lineage_record"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: lineage_record
quality: 8.7
tags: [quality_gate, lineage_record, P01]
llm_function: GOVERN
tldr: "Validates lineage records for completeness of provenance chain using PROV-O."
density_score: null
related:
  - p11_qg_agent
  - p11_qg_type_def
  - p11_qg_quality_gate
  - agent_card_n04
  - n04_qg_knowledge
  - p11_qg_response_format
  - p11_qg_boot_config
  - bld_knowledge_card_quality_gate
  - p11_qg_system_prompt
  - p11_qg_builder
---

## Quality Gate

## Definition
A lineage_record must be complete enough to reconstruct the derivation path of a knowledge artifact without relying on memory or implicit context.

## HARD Gates
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML valid |
| H02 | ID matches namespace | `^p01_lr_[a-z][a-z0-9_]+$` |
| H03 | Kind matches literal | `kind` is exactly `lineage_record` |
| H04 | Quality is null | `quality: null` |
| H05 | target_artifact set | Non-empty |
| H06 | sources_count >= 1 | At least 1 source entity |
| H07 | Timestamps present | At least 1 ISO 8601 timestamp on entities |
| H08 | Agent identified | At least 1 agent in agents list |

## SOFT Scoring
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| PROV-O relations explicit | 1.0 | Derivation Relations section uses PROV-O vocabulary |
| All activities have agents | 1.0 | No activity without agent assignment |
| sources_count matches list | 0.5 | frontmatter count = actual list length |
| activities_count matches list | 0.5 | frontmatter count = actual list length |
| Derivation type set | 0.5 | derivation_type is one of the 4 PROV-O types |

Sum of weights: 3.5. `soft_score = sum / 3.5 * 10`

## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |

## Examples

# Examples: lineage_record

## Golden Example: KC synthesized from RAG sources
```yaml
---
id: p01_lr_kc_slo_definition_synthesis
kind: lineage_record
pillar: P01
version: 1.0.0
target_artifact: "kc_slo_definition"
sources_count: 3
activities_count: 2
derivation_type: wasDerivedFrom
domain: knowledge-taxonomy
quality: null
tags: [lineage_record, knowledge-taxonomy, slo]
tldr: "Provenance for kc_slo_definition: 3 sources synthesized by N04 via ingestion + synthesis"
---
## Entities
| ID | Type | Location | Retrieved |
|----|------|----------|-----------|
| google_sre_book_ch4 | document | https://sre.google/sre-book/service-level-objectives/ | 2026-04-17T10:00:00Z |
| prometheus_slo_docs | document | https://prometheus.io/docs/practices/histograms/ | 2026-04-17T10:01:00Z |
| internal_slo_template | artifact | N04_knowledge/P01_knowledge/kc_quality_gate.md | 2026-04-17T10:02:00Z |

## Activities
| ID | Label | Used | Generated | Agent | Timestamp |
|----|-------|------|-----------|-------|-----------|
| act_ingest_slo | ingestion | google_sre_book_ch4, prometheus_slo_docs | chunk_slo_raw | N04 | 2026-04-17T10:05:00Z |
| act_synthesize_slo | synthesis | chunk_slo_raw, internal_slo_template | kc_slo_definition | N04 | 2026-04-17T10:15:00Z |

## Agents
| ID | Type | Role |
|----|------|------|
| N04 | nucleus | synthesizer + curator |

## Derivation Relations
- kc_slo_definition wasDerivedFrom google_sre_book_ch4
- kc_slo_definition wasDerivedFrom prometheus_slo_docs
- kc_slo_definition wasGeneratedBy act_synthesize_slo
- kc_slo_definition wasAttributedTo N04
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
