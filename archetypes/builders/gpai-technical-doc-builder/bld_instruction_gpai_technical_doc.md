---
kind: instruction
id: bld_instruction_gpai_technical_doc
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for gpai_technical_doc
quality: 8.9
title: "Instruction GPAI Technical Doc"
version: "1.0.0"
author: n01_wave7
tags: [gpai_technical_doc, builder, instruction, GPAI, EU-AI-Act, Annex-IV, Article-53, training-data, compute-budget]
tldr: "Step-by-step production process for gpai_technical_doc"
domain: "gpai_technical_doc construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH
1. Identify the GPAI model: name, version, model family, provider entity (legal name + EU representative if non-EU).
2. Collect training data inventory: dataset names, sources, volumes (tokens/samples), languages, date range.
3. Gather compute budget data: total FLOP count, hardware type, training duration, datacenter location.
4. Compile energy consumption figures: MWh consumed during training, estimated CO2-eq, PUE of datacenter.
5. Retrieve evaluation results: benchmark names (MMLU, HellaSwag, HumanEval, etc.), scores, evaluation date.
6. Document intended purpose and known limitations per Article 53(1)(a)-(b).
7. Define downstream-limit clauses: prohibited use cases, required safeguards for integrators.

## Phase 2: COMPOSE
1. Reference SCHEMA for Annex IV required fields.
2. Populate Section 1: Model Identity (name, version, provider, release date, model family).
3. Populate Section 2: Training Data Summary (datasets, volumes, preprocessing, filtering methods, data governance).
4. Populate Section 3: Compute Budget (FLOP estimate, hardware type, training duration, location).
5. Populate Section 4: Energy Consumption (MWh, CO2-eq, PUE, reporting methodology per GHG Protocol).
6. Populate Section 5: Evaluation Results (benchmarks, scores, evaluation methodology, known gaps).
7. Populate Section 6: Intended Purpose and Use Cases (primary use cases, target users, deployment context).
8. Populate Section 7: Downstream Integration Limits (prohibited uses, required safety measures, API terms).
9. Populate Section 8: Risk Mitigation Measures (known limitations, bias assessments, safety evaluations run).
10. Cross-reference with EU AI Office submission checklist to ensure completeness.

## Phase 3: VALIDATE
- [ ] All Annex IV fields present (model identity, training data, compute, energy, evaluation, purpose, limits).
- [ ] Training data summary includes dataset names, volumes, and data governance procedures.
- [ ] Compute budget expressed in FLOP or equivalent standardized unit.
- [ ] Energy consumption reported in MWh with CO2-eq equivalent.
- [ ] At least 3 evaluation benchmarks cited with scores and methodology.
- [ ] Downstream-limit clauses explicitly list prohibited use cases.
- [ ] Provider legal entity name and EU representative (if non-EU) present.
- [ ] Document dated and versioned for EU AI Office submission tracking.
