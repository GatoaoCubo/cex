---
kind: instruction
id: bld_instruction_ecommerce_vertical
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for ecommerce_vertical
quality: 8.9
title: "Instruction Ecommerce Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ecommerce_vertical, builder, instruction]
tldr: "Step-by-step production process for ecommerce_vertical"
domain: "ecommerce_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze cart/checkout user flows and pain points across major platforms.  
2. Map PCI-DSS compliance requirements for payment handling and data storage.  
3. Study recommendation engine algorithms (collaborative filtering, ML-based).  
4. Identify fraud detection patterns (velocity checks, device fingerprinting).  
5. Document use cases for abandoned cart recovery and dynamic pricing.  
6. Benchmark industry standards for checkout conversion rates and load times.  

## Phase 2: COMPOSE  
1. Define artifact schema per bld_schema_ecommerce_vertical.md (sections: compliance, flows, engines).  
2. Map PCI-DSS requirements to checkout data fields and encryption protocols.  
3. Write recommendation engine logic using bld_output_template_ecommerce_vertical.md’s ML integration block.  
4. Draft fraud detection rules (thresholds, anomaly scoring) in JSON format.  
5. Outline cart/checkout UX steps with error handling and validation rules.  
6. Embed use case examples (e.g., “guest checkout”, “multi-currency support”).  
7. Integrate schema versioning and artifact metadata (author, date, version).  
8. Validate template syntax against bld_output_template_ecommerce_vertical.md’s placeholder structure.  
9. Finalize artifact with cross-references to compliance and performance metrics.  

## Phase 3: VALIDATE  
- [ ] Schema matches bld_schema_ecommerce_vertical.md (no missing fields or invalid types)  
- [ ] PCI-DSS compliance rules pass static code analysis  
- [ ] Fraud detection thresholds align with industry benchmarks  
- [ ] Recommendation engine outputs match sample data in bld_output_template_ecommerce_vertical.md  
- [ ] Cart/checkout flow passes end-to-end simulation (no deadlocks or errors)

## Domain Scope
This instruction applies to ecommerce vertical artifacts (cart, checkout, catalog, payments, recommendations). It covers the full ecommerce transaction lifecycle from product discovery through post-purchase loyalty mechanics.
