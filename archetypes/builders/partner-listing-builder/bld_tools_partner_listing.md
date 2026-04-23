---
kind: tools
id: bld_tools_partner_listing
pillar: P04
llm_function: CALL
purpose: Tools available for partner_listing production
quality: 8.9
title: "Tools Partner Listing"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [partner_listing, builder, tools]
tldr: "Tools available for partner_listing production"
domain: "partner_listing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - partner-listing-builder
  - bld_collaboration_partner_listing
  - bld_output_template_partner_listing
  - bld_knowledge_card_partner_listing
  - p03_sp_partner_listing_builder
  - bld_instruction_partner_listing
  - p05_qg_partner_listing
  - bld_tools_ab_test_config
  - bld_tools_faq_entry
  - bld_examples_partner_listing
---

## Production Tools
| Tool              | Purpose                  | When                      |
|-------------------|--------------------------|---------------------------|
| cex_compile.py    | Aggregates partner data  | During data collection    |
| cex_score.py      | Assigns partner ratings  | Post-validation phase     |
| cex_retriever.py  | Fetches partner metadata | On-demand queries         |
| cex_doctor.py     | Diagnoses data issues    | Pre-validation checks     |
| cex_validator.py  | Enforces schema rules    | Data ingestion pipeline   |
| cex_analyzer.py   | Generates partner insights | Reporting cycles        |

## Validation Tools
| Tool              | Purpose                  | When                      |
|-------------------|--------------------------|---------------------------|
| val_check.py      | Verifies data consistency| Pre-deployment            |
| val_audit.py      | Cross-references records | Quarterly reviews         |
| val_comparator.py | Detects duplicates       | Merge operations          |
| val_sanitizer.py  | Cleans invalid entries   | Data preprocessing        |

## External References
- Partner API (v3.2): For real-time partner data integration
- Data Validation Framework (DVX): Schema enforcement library
- Partner Schema (v1.1): Standardized structure for listings

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[partner-listing-builder]] | downstream | 0.43 |
| [[bld_collaboration_partner_listing]] | downstream | 0.35 |
| [[bld_output_template_partner_listing]] | downstream | 0.35 |
| [[bld_knowledge_card_partner_listing]] | upstream | 0.34 |
| [[p03_sp_partner_listing_builder]] | upstream | 0.31 |
| [[bld_instruction_partner_listing]] | upstream | 0.27 |
| [[p05_qg_partner_listing]] | downstream | 0.26 |
| [[bld_tools_ab_test_config]] | sibling | 0.25 |
| [[bld_tools_faq_entry]] | sibling | 0.25 |
| [[bld_examples_partner_listing]] | downstream | 0.25 |
