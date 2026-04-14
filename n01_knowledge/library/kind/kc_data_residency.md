---
id: kc_data_residency
kind: knowledge_card
title: Data Residency Configuration
version: 1.0.0
quality: null
pillar: P01
---

# Data Residency Configuration for GDPR and Regional Compliance

Data residency refers to the physical location of data storage and processing. Organizations must configure data residency to comply with regulations like GDPR and regional data sovereignty laws.

## Key Considerations
1. **GDPR Compliance**: EU data must be stored and processed within the EU unless explicit consent allows transfers to countries with adequate data protection.
2. **Regional Requirements**: 
   - US: Follow CCPA/CPRA for California residents
   - Canada: Adhere to PIPEDA regulations
   - Asia: Comply with China's Data Security Law and Japan's APPI
3. **Data Flow Mapping**: Document all data movement paths between storage locations and processing centers.
4. **Encryption**: Implement strong encryption for data in transit and at rest across all regions.
5. **Audit Trails**: Maintain detailed records of data access and modification activities.

## Configuration Recommendations
- Use regional data centers for location-specific data
- Implement strict access controls based on data sensitivity
- Regularly review compliance status with legal counsel
- Maintain documentation of all data processing activities

## YAML Structure
```yaml
data_residency:
  region: EU/US/ASIA
  compliance:
    gdpr: true/false
    ccpa: true/false
    pipl: true/false
  storage:
    locations: [list of data centers]
    encryption: AES-256
  access:
    controls: [role-based permissions]
    audit: true/false
```

This configuration ensures legal compliance while maintaining operational efficiency across global data operations.
