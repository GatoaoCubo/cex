---
id: kc_data_residency
kind: knowledge_card
title: Data Residency Configuration for GDPR and Regional Compliance
version: 1.0.0
quality: null
pillar: P01
---

# Data Residency Configuration Guide

Data residency defines where data is stored and processed to meet regulatory requirements. Key configuration parameters include:

1. **Regional Compliance**
   - GDPR: EU data must reside within EU borders
   - CCPA: California resident data must comply with state laws
   - Other regions: Data must reside in designated jurisdictions

2. **Technical Implementation**
   - Region-specific data centers (EU/US/APAC)
   - TLS 1.3 encryption for cross-border transfers
   - Geofenced access controls

3. **Configuration Parameters**
   - `data_residency.region`: EU/US/APAC/OTHER
   - `data_residency.compliance`: GDPR/CCPA/OTHER
   - `data_residency.storage`: Regional data center location
   - `data_residency.transfer`: TLS protocol version

4. **Operational Requirements**
   - Data sovereignty enforcement
   - Audit trail retention (min 7 years)
   - Breach notification thresholds

5. **Cross-Platform Mapping**
| Framework/Provider | Data Residency Support |
|-------------------|------------------------|
| LangChain         | Regional data routing  |
| LlamaIndex        | Jurisdiction caching   |
| CrewAI            | GDPR-aware workflows   |
| DSPy              | Geofenced computation  |
| Microsoft SK      | Region-bound functions |

6. **Quality Gates**
| Gate              | Validation            | Failure Impact         |
|-------------------|-----------------------|------------------------|
| H01_region_defined| Region not empty      | Non-compliant storage  |
| H02_compliance_valid| Jurisdiction matches | Legal exposure risk    |
| H03_encryption_in_place| TLS < 1.3         | Data breach vulnerability |
| H04_access_controls| No geographic restrictions | Unauthorized access |
