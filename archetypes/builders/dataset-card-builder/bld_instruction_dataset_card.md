---
kind: instruction
id: bld_instruction_dataset_card
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for dataset_card
quality: 9.0
title: "Instruction Dataset Card"
version: "1.1.0"
author: n03_hybrid_review3
tags: [dataset_card, builder, instruction]
tldr: "Step-by-step production process for dataset_card aligned with Datasheets for Datasets + HF Dataset Cards"
domain: "dataset_card construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.90
---

## Phase 1: DISCOVER
1. Identify dataset name, version, owner, and primary modality (tabular, text, image, audio, multimodal).
2. Locate source systems, raw files, and ingestion timestamps.
3. Determine license (MIT, CC-BY-4.0, CDLA, proprietary) and redistribution constraints.
4. Capture motivation: what task does this dataset enable? Who funded or commissioned it?
5. Verify Datasheets-for-Datasets coverage (Gebru et al. 2021): motivation, composition, collection, preprocessing, uses, distribution, maintenance.

## Phase 2: STRUCTURE
1. Define splits (train/val/test) with row counts and sampling strategy.
2. Enumerate features: name, dtype, cardinality, null-rate, example value.
3. Record collection methodology: crawl, survey, sensor, synthetic, purchased.
4. Document preprocessing: deduplication, normalization, filtering, tokenization.
5. Flag PII fields, consent basis, anonymization method (k-anonymity, differential privacy).

## Phase 3: GOVERN
1. List intended uses AND out-of-scope uses (per HF Dataset Cards spec).
2. Record known biases, distributional gaps, and demographic coverage.
3. Add GDPR/CCPA fields: data origin country, retention policy, subject-access contact.
4. Cite provenance (papers, URLs, contracts) with retrieval dates.
5. Add Croissant-compatible JSON-LD block when dataset will be published to ML Commons.

## Phase 4: EMIT
1. Write frontmatter per bld_schema_dataset_card.md.
2. Fill body sections in order defined by bld_output_template_dataset_card.md.
3. Validate against bld_quality_gate_dataset_card.md (HARD gates H01-H07).
4. Run `python _tools/cex_compile.py {path}`; resolve validator errors.
5. Commit, then signal N04 (knowledge ownership) for indexing.

## Reference Standards
- Datasheets for Datasets (Gebru et al., 2021)
- HuggingFace Dataset Cards spec (dataset_info.yaml)
- ML Commons Croissant metadata format
- Google Data Cards Playbook
- GDPR Art. 30 (records of processing)
