---
kind: quality_gate
id: p05_qg_integration_guide
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for integration_guide
quality: 8.9
title: "Quality Gate Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for integration_guide"
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_integration_guide
  - bld_examples_faq_entry
  - p04_qg_sdk_example
  - p05_qg_product_tour
  - p04_qg_stt_provider
  - p05_qg_quickstart_guide
  - p05_qg_pricing_page
  - p06_qg_api_reference
  - bld_instruction_integration_guide
  - p03_qg_prompt_technique
---

## Quality Gate

## Definition  
(Table: metric, threshold, operator, scope)  
metric | threshold | operator | scope  
--- | --- | --- | ---  
Completeness | 100% | equals | all platform partners  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
ID | Check | Fail Condition  
--- | --- | ---  
H01 | YAML frontmatter valid | invalid YAML syntax  
H02 | ID matches pattern ^p05_ig_[a-z][a-z0-9_]+.md$ | invalid filename pattern  
H03 | kind field matches 'integration_guide' | incorrect kind value  
H04 | API endpoint coverage ≥ 95% | missing critical endpoints  
H05 | Error handling examples ≥ 3 | insufficient error scenarios  
H06 | Authentication methods ≥ 2 | missing required auth protocols  
H07 | Sample code in ≥ 2 languages | no code examples  
H08 | Versioning documented | no versioning info  
H09 | Partner onboarding steps ≥ 5 | incomplete onboarding process  
H10 | Compliance info (KYC/AML) included | missing regulatory details  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
Dim | Dimension | Weight | Scoring Guide  
--- | --- | --- | ---  
D01 | Clarity | 0.15 | 1.0 (clear) to 0.0 (ambiguous)  
D02 | Completeness | 0.15 | 1.0 (full) to 0.0 (incomplete)  
D03 | Technical accuracy | 0.15 | 1.0 (correct) to 0.0 (errors)  
D04 | Compliance alignment | 0.10 | 1.0 (compliant) to 0.0 (non-compliant)  
D05 | Usability | 0.10 | 1.0 (user-friendly) to 0.0 (poor)  
D06 | Code example quality | 0.10 | 1.0 (working) to 0.0 (non-functional)  
D07 | Partner onboarding flow | 0.10 | 1.0 (smooth) to 0.0 (broken)  
D08 | Versioning clarity | 0.10 | 1.0 (clear) to 0.0 (confusing)  
D09 | Language support | 0.05 | 1.0 (≥3 languages) to 0.0 (none)  

## Actions  
(Table: Score | Action)  
Score | Action  
--- | ---  
GOLDEN | ≥9.5 | Auto-publish and notify partners  
PUBLISH | ≥8.0 | Publish to platform  
REVIEW | ≥7.0 | Flag for QA review  
REJECT | <7.0 | Reject and request revisions  

## Bypass  
(Table: conditions, approver, audit trail)  
conditions | approver | audit trail  
--- | --- | ---  
Urgent partner request | CTO | ticket #12345  
Regulatory exception | Legal team | legal review #67890

## Examples

## Golden Example
---
title: "Stripe + AWS Integration Guide for SaaS Platforms"
description: "End-to-end integration guide for connecting Stripe payments with AWS infrastructure for enterprise SaaS onboarding"
audience: "Platform partners, enterprise account managers"
tags: ["payment-processing", "cloud-integration", "onboarding"]

# Stripe & AWS Integration Guide

## Overview
This guide enables seamless integration between Stripe's payment processing and AWS infrastructure for enterprise SaaS onboarding. Targeting organizations requiring PCI-DSS compliance and automated scaling.

## Prerequisites
- Stripe account with API keys (live/test)
- AWS account with IAM roles configured
- Node.js 16+ environment

## Integration Steps
1. **API Setup**
   Configure Stripe Webhook endpoints in AWS API Gateway with Lambda triggers for real-time payment events.

2. **Data Pipeline**
   Use AWS Glue to transform Stripe's JSON events into Parquet format for storage in S3.

3. **Security**
   Implement AWS KMS encryption for payment data at rest, with IAM policies restricting access to payment data.

4. **Monitoring**
   Set up CloudWatch metrics for payment processing latency and error rates.

## Best Practices
- Use Stripe's Radar for fraud detection before AWS processing
- Implement automated scaling in EC2 for high-volume payment periods
- Maintain audit logs in CloudTrail for compliance

## Support
Contact Stripe's enterprise team at enterprise-support@stripe.com and AWS support via AWS Premium Support.

---
## Anti-Example 1: Vague Implementation
---
title: "Generic Payment Integration Guide"
description: "Basic integration steps for payment systems"
audience: "Developers"
tags: ["payments"]

# Payment Integration Guide

## Overview
This guide helps integrate payment systems with your platform.

## Steps
1. Get API keys from your provider
2. Make API calls to process payments
3. Handle webhooks for payment confirmation

## Notes
- Use HTTPS
- Store secrets securely

---
## Why it fails
Lacks specificity about vendors, implementation details, and enterprise requirements. No concrete examples or technical depth for platform partners.

## Anti-Example 2: API Reference Contamination
---
title: "Stripe Integration Guide"
description: "How to use Stripe API"
audience: "Developers"
tags: ["stripe"]

# Stripe Integration Guide

## API Endpoints
- POST /v1/charges (Create charge)
- GET /v1/customers (List customers)

## Parameters
- amount (integer, required)
- currency (string, 3-letter ISO code)
- description (string, max 255 chars)

## Example
```json
{
  "amount": 1000,
  "currency": "usd",
  "description": "Monthly subscription"
}
```

---
## Why it fails
Focuses on API reference content (endpoints, parameters, schema examples) rather than integration workflow, security considerations, or enterprise onboarding processes.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
