---
kind: schema
id: bld_schema_healthcare_vertical
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for healthcare_vertical
quality: 9.1
title: "Schema Healthcare Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [healthcare_vertical, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for healthcare_vertical"
domain: "healthcare_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field        | Type   | Required | Default | Notes                              |  
|--------------|--------|----------|---------|------------------------------------|  
| id           | string | yes      | null    | Must match ID Pattern              |  
| kind         | string | yes      | null    | Always "healthcare_vertical"       |  
| pillar       | string | yes      | null    | Always "P01"                       |  
| title        | string | yes      | null    | Descriptive name                   |  
| version      | string | yes      | "1.0"   | Semantic versioning                |  
| created      | date   | yes      | null    | ISO 8601 format                    |  
| updated      | date   | yes      | null    | ISO 8601 format                    |  
| author       | string | yes      | null    | Primary contributor                |  
| domain       | string | yes      | null    | Healthcare subdomain (e.g., "diagnostics") |  
| quality      | null   | yes      | null    | Never self-score; peer review assigns |  
| tags         | array  | yes      | []      | Keywords for searchability         |  
| tldr         | string | yes      | null    | One-sentence summary               |  
| patient_population | string | yes | null | Target demographic                 |  
| clinical_use_case  | string | yes | null | Specific application in care     |  

### Recommended  
| Field              | Type   | Notes                          |  
|--------------------|--------|--------------------------------|  
| regulatory_compliance | string | FDA/EMA/other certifications   |  
| data_sources       | array  | EHR, genomics, wearables       |  

## ID Pattern  
^p01_hv_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Clinical Use Case**  
   - Detailed description of healthcare application  
2. **Patient Population**  
   - Demographics, conditions, and needs  
3. **Regulatory Compliance**  
   - Certifications and standards met  
4. **Data Integration**  
   - EHR, IoT, or genomic data sources  
5. **Outcomes Metrics**  
   - Clinical, operational, or patient-reported outcomes  

## Constraints  
- ID must match ^p01_hv_[a-z][a-z0-9_]+.md$  
- All required fields must be present and valid  
- Quality field must be peer-reviewed, not self-assigned  
- Domain-specific fields must align with healthcare subdomains  
- Version must follow semantic versioning (e.g., "1.2.3")  
- Total markdown body must be ≤ 6144 bytes
