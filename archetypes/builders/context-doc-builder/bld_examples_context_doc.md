---
kind: examples
id: bld_examples_context_doc
pillar: P07
llm_function: GOVERN
purpose: Golden example and anti-example for context_doc production
---

# Examples: context_doc
## Golden Example
```markdown
id: p01_ctx_br_ecommerce_import_regs
kind: context_doc
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: builder_agent
domain: ecommerce_imports
scope: "Brazilian import regulations for marketplace sellers, 2025-2026 enforcement cycle"
quality: null
tags: [context-doc, ecommerce_imports, brazil, regulation]
tldr: "BR marketplace imports: ICMS 17-20%, NCM code required, Receita Federal DI threshold R$50"
keywords: [icms, ncm, receita_federal, import, brazil, marketplace, tax]
density_score: 0.87
## Scope
In scope: ICMS rates by state, NCM classification requirements, Receita Federal DI thresholds,
marketplace seller obligations under Lei 14.781/2024.
Out of scope: international shipping logistics, payment processing, consumer returns law.
## Background
Brazil levies ICMS (17-20% by state) on all imported goods sold via marketplace.
NCM codes (8-digit Nomenclatura Comum do Mercosul) are mandatory on all listings.
Receita Federal requires Declaracao de Importacao (DI) for shipments > R$50 commercial value.
Lei 14.781/2024 expanded marketplace platform liability for seller tax compliance.
## Stakeholders
- Marketplace seller agents: need tax rates and NCM requirements before listing
- Compliance agents: enforce DI threshold checks pre-shipment
- Pricing agents: require ICMS rates to compute landed cost
## Constraints & Assumptions
- ICMS rates are state-specific; this context uses SP rate (18%) as default
- NCM codes assumed valid per MDIC 2025 table (update required if MDIC revises)
- DI threshold R$50 is current as of 2026-01-01; subject to Receita Federal portaria changes
## Dependencies
- `p01_kc_ncm_classification_rules` — atomic NCM lookup facts
- `p01_kc_icms_state_rates_2025` — per-state rate table
- Receita Federal Portaria RFB 1.073/2025 (external)
## References
- Lei 14.781/2024: planalto.gov.br/lei-14781
- MDIC NCM table: mdic.gov.br/nomenclatura
```
### Why Golden (gate mapping)
| Gate | Status | Reason |
|------|--------|--------|
| H01 | PASS | YAML parses without error |
| H02 | PASS | id matches `^p01_ctx_[a-z][a-z0-9_]+$` |
| H03 | PASS | id == filename stem |
| H04 | PASS | kind == "context_doc" |
| H05 | PASS | quality == null |
| H06 | PASS | id, kind, domain, scope all present |
| H07 | PASS | body <= 2048 bytes |
| S01 | PASS | tldr <= 160ch, non-empty |
| S02 | PASS | tags len 4, includes "context-doc" |
| S03 | PASS | Scope section present, 4 lines |
| S04 | PASS | Background section non-empty, 4 dense facts |
| S05 | PASS | No filler phrases detected |
| S06 | PASS | density_score 0.87 >= 0.80 |
| S07 | PASS | Constraints section present |
| S08 | PASS | Dependencies listed with artifact ids |
## Anti-Example
```markdown
id: ctx_brazil_imports
kind: context_doc
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: builder_agent
domain: imports
quality: 8.5
tags: [context-doc]
tldr: "This document provides a comprehensive overview of the various regulatory frameworks
that apply to the importation of goods into Brazil through various channels including
ecommerce marketplaces and direct consumer imports."
## Overview
This document is about Brazilian imports. It covers many things related to importing
goods. Basically, there are taxes involved and you need to follow some rules.
In summary, compliance is important.
```
### Failures (gate mapping)
| Gate | Status | Failure |
|------|--------|---------|
| H02 | FAIL | id `ctx_brazil_imports` missing `p01_` prefix |
| H05 | FAIL | quality: 8.5 — self-scored, must be null |
| H06 | FAIL | scope field absent from frontmatter |
| S01 | FAIL | tldr > 160 chars (224 chars) |
| S02 | FAIL | tags len 1 (< 3 required) |
| S03 | FAIL | No `## Scope` section present |
| S05 | FAIL | Filler: "this document", "basically", "in summary" |
| S06 | FAIL | density_score absent |
