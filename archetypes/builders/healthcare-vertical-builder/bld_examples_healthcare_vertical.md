---
kind: examples
id: bld_examples_healthcare_vertical
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of healthcare_vertical artifacts
quality: 8.9
title: "Examples Healthcare Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [healthcare_vertical, builder, examples]
tldr: "Golden and anti-examples of healthcare_vertical artifacts"
domain: "healthcare_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example  
```markdown  
---  
title: "Secure Patient Data Exchange Using FHIR"  
kind: healthcare_vertical  
vendor: Epic Systems  
tool: Epic EHR Platform  
standard: HL7 FHIR R4  
use_case: Interoperable patient record sharing between hospitals  
description:  
  - Implements HIPAA-compliant PHI encryption (AES-256) at rest and TLS 1.2+ in transit  
  - Integrates with HL7 FHIR API for real-time lab result sharing  
  - Audits all PHI access via AWS CloudTrail with role-based access controls  
  - Uses Athenahealth's patient portal for consumer-facing data access  
  - Complies with ONC 21st Century Cures Final Rule for data blocking  
```  

## Anti-Example 1: Missing HIPAA Compliance  
```markdown  
---  
title: "Basic Lab Result API"  
kind: healthcare_vertical  
vendor: MedTech Inc.  
tool: Legacy Lab API v1.0  
standard: HL7 v2.x  
use_case: Lab result transmission  
description:  
  - No explicit encryption or audit logging for PHI  
  - Uses unauthenticated HTTP endpoints for data transfer  
  - No mention of HIPAA or PHI handling protocols  
```  
## Why it fails  
Lacks fundamental HIPAA requirements (encryption, access controls) and uses deprecated HL7 v2.x without FHIR interoperability, violating modern healthcare data standards.  

## Anti-Example 2: Ignoring FHIR Standards  
```markdown  
---  
title: "Custom EHR Module"  
kind: healthcare_vertical  
vendor: HealthSoft LLC  
tool: Proprietary EHR Module  
standard: Custom HL7 v2.x  
use_case: Internal provider documentation  
description:  
  - No FHIR API integration  
  - Stores PHI in unencrypted flat files  
  - No audit trails for data access  
```  
## Why it fails  
Fails to adopt HL7 FHIR (required for interoperability) and lacks HIPAA-mandated encryption and audit controls, creating compliance and interoperability risks.
