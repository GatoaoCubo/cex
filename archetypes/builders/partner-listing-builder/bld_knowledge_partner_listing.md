---
kind: knowledge_card
id: bld_knowledge_card_partner_listing
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for partner_listing production
quality: 9.1
title: "Knowledge Card Partner Listing"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [partner_listing, builder, knowledge_card]
tldr: "Domain knowledge for partner_listing production"
domain: "partner_listing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - partner-listing-builder
  - p03_sp_partner_listing_builder
  - bld_instruction_partner_listing
  - bld_tools_partner_listing
  - p05_qg_partner_listing
  - bld_collaboration_partner_listing
  - bld_examples_partner_listing
  - bld_output_template_partner_listing
  - kc_partner_listing
  - p10_lr_partner_listing_builder
---

## Domain Overview  
Partner listing artifacts organize SI/reseller channel data to enable ecosystem collaboration, sales enablement, and compliance tracking. They standardize attributes like tier levels (e.g., platinum, gold), geographic regions, certifications (e.g., ISO/IEC 27001), and contact details, ensuring stakeholders can quickly identify qualified partners. These listings are critical for vendor-managed programs, channel incentives, and ensuring alignment with industry compliance frameworks.  

Effective partner listings integrate data from CRM systems, partner portals, and certification databases, often requiring normalization to avoid duplication and ensure consistency. They also support dynamic filtering for sales teams, auditors, and customers seeking verified resellers.  

## Key Concepts  
| Concept               | Definition                                                                 | Source                              |  
|----------------------|----------------------------------------------------------------------------|-------------------------------------|  
| Partner Tier         | Classification (e.g., platinum, silver) based on revenue, capabilities, or certifications | Gartner Partner Ecosystem Framework |  
| Certification        | Formal validation of technical or compliance standards (e.g., ISO/IEC 27001) | ISO/IEC 20000-1:2018                |  
| Region               | Geographic scope (e.g., APAC, EMEA) defining partner operational reach      | ITIL 4 Service Management           |  
| Channel Type         | SI, reseller, value-added distributor, or authorized partner                | Forrester Channel Strategy Report   |  
| Contact Information  | Structured data (name, title, email, phone) for direct engagement         | RFC 5322 (email format)             |  
| Partner ID           | Unique identifier for tracking across systems (e.g., ERP, CRM)             | GS1 Standards                       |  
| Compliance Status    | Legal/contractual adherence (e.g., GDPR, CCPA)                             | ISO/IEC 27701:2019                  |  
| Capability Matrix    | Tabular view of partner skills (e.g., cloud, AI, cybersecurity)            | PMI Partner Management Guide        |  

## Industry Standards  
- ISO/IEC 20000-1:2018 (IT service management)  
- ISO/IEC 27701:2019 (privacy extensions for ISO/IEC 27001)  
- ITIL 4 (service management frameworks)  
- GS1 General Specifications (global trade standards)  
- RFC 5322 (email message format)  
- Gartner Partner Ecosystem Framework  
- PMI Partner Management Guide  

## Common Patterns  
1. Use ISO/IEC certification tiers for partner classification.  
2. Segment regions using ISO 3166-1 alpha-2 country codes.  
3. Align certifications with ISO/IEC 27001 or industry-specific standards.  
4. Normalize contact data using RFC 5322 email and phone formats.  
5. Embed partner IDs as GS1-compliant identifiers.  
6. Map capabilities to PMI-defined skill categories.  

## Pitfalls  
- Inconsistent tier definitions across regions (e.g., "gold" meaning different things).  
- Missing region-specific compliance data (e.g., GDPR vs. CCPA).  
- Overlooking certification expiration dates in listings.  
- Poorly formatted contact info leading to failed outreach.  
- Failing to synchronize listings with real-time CRM data.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[partner-listing-builder]] | downstream | 0.57 |
| [[p03_sp_partner_listing_builder]] | downstream | 0.54 |
| [[bld_instruction_partner_listing]] | downstream | 0.49 |
| [[bld_tools_partner_listing]] | downstream | 0.42 |
| [[p05_qg_partner_listing]] | downstream | 0.41 |
| [[bld_collaboration_partner_listing]] | downstream | 0.36 |
| [[bld_examples_partner_listing]] | downstream | 0.36 |
| [[bld_output_template_partner_listing]] | downstream | 0.34 |
| [[kc_partner_listing]] | sibling | 0.31 |
| [[p10_lr_partner_listing_builder]] | downstream | 0.28 |
