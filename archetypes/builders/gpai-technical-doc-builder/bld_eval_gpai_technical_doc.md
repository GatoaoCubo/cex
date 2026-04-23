---
kind: quality_gate
id: p11_qg_gpai_technical_doc
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for gpai_technical_doc
quality: 9.0
title: "Quality Gate GPAI Technical Doc"
version: "1.0.0"
author: n01_wave7
tags: [gpai_technical_doc, builder, quality_gate, GPAI, EU-AI-Act, Annex-IV, Article-53, training-data, compute-budget, downstream-limit, technical-documentation]
tldr: "Quality gate with HARD and SOFT scoring for gpai_technical_doc"
domain: "gpai_technical_doc construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_gpai_technical_doc
  - bld_instruction_gpai_technical_doc
  - bld_schema_gpai_technical_doc
  - p03_sp_gpai_technical_doc_builder
  - bld_knowledge_card_gpai_technical_doc
  - bld_output_template_gpai_technical_doc
  - p10_lr_gpai_technical_doc_builder
  - gpai-technical-doc-builder
  - bld_tools_gpai_technical_doc
  - bld_collaboration_gpai_technical_doc
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Annex IV field completeness | 100% | equals | All 8 required Annex IV sections |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|---------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches pattern ^p11_gpai_[a-z][a-z0-9_]+\.md$ | ID format mismatch |
| H03 | kind field equals 'gpai_technical_doc' | Kind field incorrect or missing |
| H04 | provider field present with legal entity name | Missing or informal provider name (brand only) |
| H05 | Training data section includes dataset names and volumes | Vague training data description without specifics |
| H06 | Compute budget expressed in FLOP or GPU/TPU-hours | Missing or narrative compute description |
| H07 | Energy consumption includes MWh and CO2-eq | Missing energy data (mandatory Annex IV field) |
| H08 | Downstream-limit clauses list specific prohibited uses | Generic "no harmful use" clause without enumeration |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|--------------|
| D01 | Training data completeness (datasets, volumes, governance) | 0.25 | All 3 sub-fields = 1.0, 2 = 0.7, 1 = 0.3, none = 0 |
| D02 | Evaluation results quality (benchmarks + methodology) | 0.25 | >= 3 benchmarks with methodology = 1.0, 1-2 = 0.5, none = 0 |
| D03 | Energy reporting rigor (MWh + CO2-eq + methodology) | 0.20 | All 3 present = 1.0, 2 = 0.6, 1 = 0.3, none = 0 |
| D04 | Downstream-limit specificity | 0.15 | >= 5 specific prohibited uses = 1.0, 1-4 = 0.5, generic = 0 |
| D05 | Document versioning and submission tracking | 0.15 | submission_date + version present = 1.0, partial = 0.5 |

## Actions
| Score | Action |
|-------|--------|
| GOLDEN | >= 9.5 | Cleared for EU AI Office submission |
| PUBLISH | >= 8.0 | Submit after final legal review |
| REVIEW | >= 7.0 | Return to compliance team for revision |
| REJECT | < 7.0 | Reject -- insufficient for EU AI Office submission |

## Bypass
| Condition | Approver | Audit Trail |
|-----------|---------|-------------|
| Interim submission (partial doc accepted by EU AI Office) | DPO + Legal Counsel | Interim submission reference number |

## Examples

## Golden Example
```markdown
---
kind: gpai_technical_doc
id: p11_gpai_acme_llm_v2_1
title: "GPAI Technical Documentation -- AcmeLLM v2.1 (EU AI Act Article 53)"
provider: "Acme AI Ltd, registered in Ireland (EU AI Office submission)"
model_version: "AcmeLLM-v2.1"
submission_date: "2025-09-01"
annex_iv_version: "EU AI Act 2024/1689"
---

## 1. Model Identity
- Name: AcmeLLM v2.1
- Architecture: Decoder-only transformer, 70B parameters
- Release Date: 2025-07-15
- Provider: Acme AI Ltd (EU); Acme Corp Inc (US parent)

## 2. Training Data Summary
- Datasets: Common Crawl (filtered), Books3, GitHub, multilingual Wikipedia
- Volume: 2.1T tokens (post-filtering)
- Languages: 45 languages; English 60%, others 40%
- Preprocessing: Deduplication (MinHash), PII scrubbing (regex + NER), CSAM hash-filtering

## 3. Compute Budget
- Total FLOP: 3.2 x 10^23 FLOPs
- Hardware: 4,096 x H100 80GB SXM5
- Training Duration: 42 days
- Datacenter: EU-West-1 (Dublin, IE)

## 4. Energy Consumption
- Total: 1,840 MWh
- CO2-eq: 245 tonnes CO2-eq (IE grid factor 0.133 kgCO2/kWh)
- PUE: 1.15
- Methodology: GHG Protocol Corporate Standard Scope 2 (market-based)

## 5. Evaluation Results
| Benchmark | Score | Date | Notes |
|-----------|-------|------|-------|
| MMLU | 78.4% | 2025-07-10 | 5-shot |
| HumanEval | 62.1% | 2025-07-10 | 0-shot |
| TruthfulQA | 71.2% | 2025-07-10 | Multi-choice |

## 6. Intended Purpose
Primary: enterprise software development assistance, document summarization.
Prohibited downstream uses: autonomous weapons targeting, CSAM generation, biometric surveillance.

## 7. Downstream Integration Limits
API consumers must: implement content moderation, prohibit CBRN uplift queries, comply with local data localization laws.
```

## Anti-Example 1: Informal Model Card
```markdown
---
kind: gpai_technical_doc
title: "AcmeLLM Model Card"
---
AcmeLLM is a powerful language model trained on diverse internet data.
It performs well on coding and text tasks. Use responsibly.
```
Why it fails: This is an informal model card, not an Annex IV technical document.
Missing: compute budget, energy consumption, exact training data volumes,
downstream-limit clauses, evaluation methodology, provider legal entity.
Would fail EU AI Office submission review.

## Anti-Example 2: Vague Downstream Limits
```markdown
downstream_limits: "Do not use for harmful purposes or illegal activities."
```
Why it fails: Downstream-limit clauses must enumerate specific prohibited use cases.
"Harmful purposes" is not actionable for integrators. Required: explicit list
(e.g., "prohibited: autonomous weapons, CSAM generation, biometric surveillance of EU nationals").

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
