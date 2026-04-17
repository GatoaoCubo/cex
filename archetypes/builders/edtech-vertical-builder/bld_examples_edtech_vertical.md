---
kind: examples
id: bld_examples_edtech_vertical
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of edtech_vertical artifacts
quality: 8.9
title: "Examples Edtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [edtech_vertical, builder, examples]
tldr: "Golden and anti-examples of edtech_vertical artifacts"
domain: "edtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example  
```yaml  
title: EdTech Vertical Integration with LTI and Privacy Compliance  
kind: edtech_vertical  
description: Secure student data management with LTI integration and FERPA/COPPA compliance  
tools:  
  - LMS: Canvas LMS  
  - Data Privacy: Google Workspace for Education (with encryption at rest and in transit)  
  - LTI Provider: Microsoft Teams for Education (LTI 1.3 compliant)  
use_cases:  
  - Student performance analytics with anonymized data  
  - Parental consent workflows for COPPA-compliant data collection  
  - Seamless grade sync between LMS and external assessment tools  
compliance:  
  - FERPA: Data access restricted to authorized educational purposes  
  - COPPA: Age verification and opt-in mechanisms for under-13 users  
```  

## Anti-Example 1: Missing LTI Compliance  
```yaml  
title: EdTech Vertical Integration (Incomplete)  
kind: edtech_vertical  
description: Student data management without LTI integration  
tools:  
  - LMS: Moodle  
  - Data Privacy: Custom in-house solution (no third-party audits)  
use_cases:  
  - Manual data transfer between systems  
  - No student consent tracking  
compliance:  
  - FERPA: Not explicitly addressed  
  - COPPA: Not applicable (no under-13 user handling)  
```  
## Why it fails  
Lacks LTI integration, leading to insecure data silos and non-compliant manual workflows. No third-party audits or encryption mechanisms violate FERPA/COPPA requirements.  

## Anti-Example 2: Overlooking COPPA Scope  
```yaml  
title: EdTech Vertical for K-12  
kind: edtech_vertical  
description: LMS integration with student data collection  
tools:  
  - LMS: Schoology  
  - Data Privacy: Third-party analytics tool (no COPPA certification)  
use_cases:  
  - Real-time student behavior tracking  
  - Automated reporting to school admins  
compliance:  
  - FERPA: Partially addressed  
  - COPPA: Ignored (tool collects data from under-13 users without consent)  
```  
## Why it fails  
The analytics tool collects data from minors without COPPA-compliant consent mechanisms, exposing the organization to legal risks and data breaches.
