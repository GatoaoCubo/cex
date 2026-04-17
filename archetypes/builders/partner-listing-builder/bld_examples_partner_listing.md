---
kind: examples
id: bld_examples_partner_listing
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of partner_listing artifacts
quality: 8.9
title: "Examples Partner Listing"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [partner_listing, builder, examples]
tldr: "Golden and anti-examples of partner_listing artifacts"
domain: "partner_listing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
kind: partner_listing
title: Cisco Systems Inc. Partner Listing
---
**Partner Name**: Cisco Systems Inc.
**Tier**: Platinum
**Region**: North America
**Certifications**:
- Cisco Certified Partner (CCP)
- Cisco Partner Advantage (CPA)
**Contact**:
- Email: partners@cisco.com
- Phone: +1 800 553 2447
**Description**: Cisco Systems Inc. is a global leader in networking and IT solutions, offering enterprise-grade hardware, software, and services. As a Platinum partner, they provide advanced consulting, deployment, and support services for Cisco products across North America.
```

## Anti-Example 1: Missing Key Fields
```markdown
---
kind: partner_listing
title: TechSolutions Inc. Listing
---
**Partner Name**: TechSolutions Inc.
**Region**: Europe
**Certifications**:
- ISO 9001
**Contact**:
- Email: contact@techsolutions.com
```
## Why it fails:
Omits **tier** (critical for partner categorization) and lacks **specific certifications** relevant to the partner's domain (e.g., IT, cloud, etc.), making the listing incomplete and unactionable for potential collaborators.

## Anti-Example 2: Case Study Confusion
```markdown
---
kind: partner_listing
title: How ABC Corp Boosted Efficiency with XYZ Tools
---
**Customer**: ABC Corp
**Solution**: XYZ Tools' AI-driven analytics platform
**Outcome**: 30% faster processing times
**Contact**: sales@xyztools.com
```
## Why it fails:
This is a **case study**, not a partner listing. It focuses on a customer's success story rather than detailing the partner's **tier, region, certifications**, or direct contact methods for collaboration.
