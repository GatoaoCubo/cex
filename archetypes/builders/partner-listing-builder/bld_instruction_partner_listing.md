---
kind: instruction
id: bld_instruction_partner_listing
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for partner_listing
quality: 8.9
title: "Instruction Partner Listing"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [partner_listing, builder, instruction]
tldr: "Step-by-step production process for partner_listing"
domain: "partner_listing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify partner data sources (CRM, ERP, channel portals).  
2. Extract partner tier classifications (Gold, Silver, etc.) and region codes.  
3. Map certifications to industry standards (ISO, CSP, etc.).  
4. Validate contact info formats (email, phone, URL).  
5. Audit for duplicate partner entries across regions.  
6. Analyze regional distribution gaps for partner coverage.  

## Phase 2: COMPOSE  
1. Reference SCHEMA.md for required fields (name, tier, region, certifications).  
2. Populate OUTPUT_TEMPLATE.md with partner data from validated sources.  
3. Format tier labels consistently (e.g., "Gold", "Platinum").  
4. Use ISO 3166-1 alpha-2 codes for region fields.  
5. List certifications as comma-separated values (e.g., "CSP, ISO 27001").  
6. Ensure contact fields follow schema (email: user@domain.com, phone: +1234567890).  
7. Cross-reference partner names with schema for spelling accuracy.  
8. Add metadata tags for filtering (e.g., `tier:Gold`, `region:US`).  
9. Proofread for typos and schema compliance.  

## Phase 3: VALIDATE  
- [ ] ✅ All required fields present (name, tier, region, certifications, contact).  
- [ ] ✅ Data formats match SCHEMA.md (e.g., region codes, email syntax).  
- [ ] ✅ Certifications mapped to valid industry standards.  
- [ ] ✅ Contact info validated (email deliverability, phone format).  
- [ ] ✅ Regional distribution aligns with research phase findings.
