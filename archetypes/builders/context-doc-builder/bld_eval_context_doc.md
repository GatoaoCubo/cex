---
kind: quality_gate
id: p11_qg_context_doc
pillar: P11
llm_function: GOVERN
purpose: Golden example and anti-example for context_doc production
quality: 9.0
title: "Gate: context_doc"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, context-doc, P01, prompt-hydration, domain-scope, constraints]
tldr: "Pass/fail gate for context_doc artifacts: domain scope precision, constraint completeness, assumption capture, and hydration readiness."
domain: "domain context documentation — background documents that hydrate prompts with scope, stakeholders, constraints, and assumptions"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.91
related:
  - p11_qg_chunk_strategy
  - p11_qg_constraint_spec
  - bld_instruction_context_doc
  - context-doc-builder
  - p11_qg_memory_scope
  - p11_qg_retriever_config
  - bld_output_template_context_doc
  - p11_qg_handoff_protocol
  - p11_qg_component_map
  - p11_qg_output_validator
---

## Quality Gate

# Gate: context_doc
## Definition
| Field | Value |
|---|---|
| metric | context_doc artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: context_doc` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | `id: my_ctx` but file is `other_ctx.md` |
| H04 | Kind equals literal `context_doc` | `kind: knowledge_card` or `kind: glossary_entry` or any other value |
| H05 | Quality field is null | `quality: 7.0` or any non-null value |
| H06 | All required fields present | Missing `domain`, `scope`, or `constraints` |
| H07 | Body size <= 2048 bytes | Body exceeds 2048 bytes — trim or split into knowledge_card |
| H08 | Scope section states what is OUT of scope | Scope only lists what is included; exclusions absent |
| H09 | At least one constraint documented | `constraints: []` or constraints section empty |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Scope precision | 1.0 | Domain boundary is specific enough to exclude adjacent domains unambiguously |
| Out-of-scope completeness | 1.0 | Adjacent domains that could be confused are explicitly excluded |
| Constraint actionability | 1.0 | Each constraint is a specific rule a prompt can apply, not a vague guideline |
| Assumption explicitness | 1.0 | Assumptions are stated as assumptions (not facts), with source noted |
| Stakeholder relevance | 0.5 | Stakeholders listed are those whose concerns affect prompt behavior |
| Dependency mapping | 0.5 | External dependencies that constrain the domain are identified |
| Hydration readiness | 1.0 | Document structured so key facts can be injected into a prompt without editing |
| Freshness | 0.5 | `updated` date is recent; stale context docs noted as requiring review |
| Terminology consistency | 0.5 | Key terms used consistently throughout; ambiguous terms defined inline |
| Density apownteness | 1.0 | Content is dense but readable; no padding or repeated constraints |
| Boundary from knowledge_card | 1.0 | Document is context or background, not a distilled atomic fact (that belongs in knowledge_card) |
| Domain specificity | 1.0 | Content specific to the declared domain; no generic boilerplate |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Context doc for an emerging domain where constraints are still being discovered; used only in internal experiments |
| approver | Domain owner acknowledgment that constraints are provisional |
| audit_trail | Bypass reason and list of known-incomplete constraint areas in frontmatter comment |
| expiry | 7d — context docs for active domains must reach >= 7.0 within one week of first use |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |

## Examples

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
quality: 8.9
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
Receita Federal requires Declaraction de Importaction (DI) for shipments > R$50 commercial value.
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
- MDIC NCM table: mdic.gov.br/namenclatura
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
