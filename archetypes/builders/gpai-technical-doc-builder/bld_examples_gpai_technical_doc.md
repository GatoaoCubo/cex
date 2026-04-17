---
kind: examples
id: bld_examples_gpai_technical_doc
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of gpai_technical_doc artifacts
quality: 9.1
title: "Examples GPAI Technical Doc"
version: "1.0.0"
author: n01_wave7
tags: [gpai_technical_doc, builder, examples, GPAI, EU-AI-Act, Annex-IV, Article-53, training-data, compute-budget, downstream-limit, technical-documentation]
tldr: "Golden and anti-examples of gpai_technical_doc artifacts"
domain: "gpai_technical_doc construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
