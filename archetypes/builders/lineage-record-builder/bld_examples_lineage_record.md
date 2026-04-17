---
id: bld_examples_lineage_record
kind: knowledge_card
pillar: P01
title: "Examples: lineage_record"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: lineage_record
quality: null
tags: [examples, lineage_record, P01]
llm_function: GOVERN
tldr: "Golden example for lineage_record construction."
density_score: null
---

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
