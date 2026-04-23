---
id: kc_partner_listing
kind: knowledge_card
title: Partner Directory Listing
version: 1.0.0
quality: 8.7
pillar: P01
density_score: 1.0
related:
  - bld_instruction_partner_listing
  - p03_sp_partner_listing_builder
  - bld_knowledge_card_partner_listing
  - partner-listing-builder
  - p05_qg_partner_listing
  - p10_lr_partner_listing_builder
  - bld_examples_partner_listing
  - bld_collaboration_partner_listing
  - bld_knowledge_card_white_label_config
  - tpl_response_format
---

# Partner Directory Listing Specification

## 1. Core Fields
- **partner_id**: Unique identifier (UUID format)
- **name**: Full legal name of the organization
- **type**: `si` (System Integrator) or `reseller` (Value Added Reseller)
- **region**: ISO 3166-1 alpha-2 country code
- **certifications**: Array of certification names (e.g., `ISO 27001`, `GDPR`)
- **contact**: 
  - **email**: Primary contact email
  - **phone**: International format with country code
  - **website**: Official company website URL

## 2. Optional Enhancements
- **active**: Boolean indicating current partnership status
- **specialization**: Array of service areas (e.g., `cloud_migration`, `data_security`)
- **anniversary**: Date of partnership commencement
- **renewal_date**: Date of upcoming contract renewal
- **performance_score**: Numerical rating (0-100) based on KPIs

## 3. Formatting Guidelines
- Use `application/json` content type
- Implement schema validation via `kc_partner_listing_v1.0.0.json`
- Include `Content-Type: application/json` header
- Add `X-Partner-Type` header with value `si` or `reseller`

## 4. Example
```json
{
  "partner_id": "si-001",
  "name": "SecureNet Systems Inc.",
  "type": "si",
  "region": "US",
  "certifications": ["ISO 27001", "SOC 2"],
  "contact": {
    "email": "partners@securenet.com",
    "phone": "+1-800-555-0199",
    "website": "https://www.securenetsystems.com"
  },
  "active": true,
  "specialization": ["cloud_migration", "data_security"],
  "anniversary": "2018-03-15",
  "renewal_date": "2024-03-15",
  "performance_score": 92
}
```

## 5. Best Practices
- Update directory monthly for accuracy
- Flag inactive partners with `active: false`
- Use `performance_score` for prioritization
- Include all required fields for GDPR compliance
```
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_partner_listing]] | downstream | 0.30 |
| [[p03_sp_partner_listing_builder]] | downstream | 0.28 |
| [[bld_knowledge_card_partner_listing]] | sibling | 0.26 |
| [[partner-listing-builder]] | downstream | 0.26 |
| [[p05_qg_partner_listing]] | downstream | 0.24 |
| [[p10_lr_partner_listing_builder]] | downstream | 0.21 |
| [[bld_examples_partner_listing]] | downstream | 0.21 |
| [[bld_collaboration_partner_listing]] | downstream | 0.20 |
| [[bld_knowledge_card_white_label_config]] | sibling | 0.19 |
| [[tpl_response_format]] | downstream | 0.17 |
