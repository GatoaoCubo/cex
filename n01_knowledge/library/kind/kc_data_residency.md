---
id: kc_data_residency
kind: knowledge_card
title: Data Residency Configuration
version: 1.0.0
quality: null
pillar: P01
---

# Data Residency Configuration

Data residency refers to the physical location where data is stored and processed. It is critical for compliance with regulations like GDPR and regional data laws.

## Key Considerations
1. **Legal Requirements**  
   - GDPR: Data must be processed within the EU for EU citizens' data  
   - CCPA: California residents' data must be handled under specific conditions  
   - Other regional laws: Data must reside in specific jurisdictions

2. **Technical Implementation**  
   - Use region-specific data centers  
   - Ensure data transfer encryption (TLS 1.2+)  
   - Implement access controls based on geographic location  

3. **Compliance Frameworks**  
   - GDPR Article 4(13): "Data subject's country of residence"  
   - Schrems II ruling: Data transfers to non-EU countries must include adequacy decisions or SCCs  
   - Privacy Shield Framework: For data transfers to the US  

## Implementation Steps
1. Identify data categories requiring residency compliance  
2. Map data flows to geographic regions  
3. Configure infrastructure for regional data storage  
4. Implement monitoring and audit trails  
5. Document compliance procedures  

## Cross-Platform Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `DataResidencyMiddleware` | Regional data routing |
| LlamaIndex | `RegionAwareStorage` | Jurisdiction-specific caching |
| CrewAI | `ComplianceTask` | GDPR-aware workflow execution |
| DSPy | `DataLocalizationModule` | Geofenced computation |
| Microsoft Semantic Kernel | `RegionBoundFunction` | Data residency enforcement |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_residency_defined | Residency policy not empty | Non-compliant data handling |
| H02_legal_valid | Jurisdiction matches regulatory requirements | Legal exposure risk |
| H03_encryption_in_place | Data transfer without TLS 1.2+ | Data breach vulnerability |
| H04_access_controls | No geographic access restrictions | Unauthorized data access |
