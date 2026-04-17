---
kind: examples
id: bld_examples_govtech_vertical
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of govtech_vertical artifacts
quality: 8.9
title: "Examples Govtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [govtech_vertical, builder, examples]
tldr: "Golden and anti-examples of govtech_vertical artifacts"
domain: "govtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example  
```yaml  
kind: govtech_vertical  
title: Secure Cloud Storage for Federal Agencies  
provider: AWS GovCloud (US)  
compliance:  
  - FedRAMP: High  
  - FISMA: Compliant  
  - CJIS: Certified  
  - Section 508: Accessible  
use_case:  
  - Secure storage of classified data under CJIS standards  
  - FedRAMP-compliant cloud infrastructure for federal agencies  
  - Section 508-compliant UI for public-facing services  
description:  
  AWS GovCloud (US) provides a secure, isolated cloud environment tailored for U.S. government workloads. It meets FedRAMP High requirements, FISMA guidelines, and CJIS standards for handling sensitive data. The platform includes accessibility features compliant with Section 508, ensuring equitable access for users with disabilities.  
```  

## Anti-Example 1: Missing FedRAMP Compliance  
```yaml  
kind: govtech_vertical  
title: Cloud Backup Solution  
provider: Dropbox Business  
compliance:  
  - FedRAMP: Not applicable  
  - FISMA: Not assessed  
use_case:  
  - Data backup for state agencies  
description:  
  Dropbox Business lacks FedRAMP certification and has not undergone FISMA compliance assessments. It cannot be used for federal agencies handling sensitive data.  
```  
## Why it fails  
The tool is not FedRAMP-compliant, disqualifying it for federal use. FISMA compliance is also absent, increasing security risks.  

## Anti-Example 2: Ignoring Section 508 Standards  
```yaml  
kind: govtech_vertical  
title: Video Conferencing Platform  
provider: Zoom for Government  
compliance:  
  - FedRAMP: Compliant  
  - Section 508: Not fully compliant  
use_case:  
  - Remote collaboration for federal employees  
description:  
  Zoom for Government meets FedRAMP requirements but lacks features like closed captions and keyboard navigation, failing Section 508 accessibility standards.  
```  
## Why it fails  
Section 508 compliance is mandatory for government tools. Missing accessibility features excludes users with disabilities and violates legal requirements.
