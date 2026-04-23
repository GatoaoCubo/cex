---
kind: quality_gate
id: p05_qg_partner_listing
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for partner_listing
quality: 9.0
title: "Quality Gate Partner Listing"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [partner_listing, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for partner_listing"
domain: "partner_listing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_partner_listing
  - bld_instruction_partner_listing
  - partner-listing-builder
  - p03_sp_partner_listing_builder
  - bld_knowledge_card_partner_listing
  - bld_tools_partner_listing
  - bld_output_template_partner_listing
  - bld_collaboration_partner_listing
  - p10_lr_partner_listing_builder
  - p05_qg_integration_guide
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|---|---|---|---|
| Partner directory completeness | 100% | equals | All SI/reseller channels |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing fields |
| H02 | ID matches pattern ^p05_pl_[a-z][a-z0-9_]+.md$ | ID format mismatch |
| H03 | kind field matches 'partner_listing' | Kind field incorrect or missing |
| H04 | Tier field present and valid | Missing or invalid tier (e.g., Gold, Silver) |
| H05 | Region field present and valid | Missing or invalid region (e.g., APAC, EMEA) |
| H06 | Certifications field present and valid | Missing or invalid certifications (e.g., ISO, SOC2) |
| H07 | Contact info field present and valid | Missing or invalid contact details (email, phone) |
| H08 | Unique partner ID exists | Duplicate or missing partner ID |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Listing completeness (AppExchange-style fields) | 0.25 | All required listing fields present = 1.0, partial = 0.5, <50% = 0 |
| D02 | Tier accuracy (AWS PN: Select/Advanced/Premier or HubSpot Solutions tiers) | 0.20 | Tier matches partner program criteria = 1.0, mismatch = 0.5, missing = 0 |
| D03 | Certification validity (badges, expiry, issuer) | 0.20 | Current verified certs = 1.0, expired = 0.5, none = 0 |
| D04 | Region/industry filter coverage (ISO 3166-1 + NAICS) | 0.15 | All applicable filters = 1.0, partial = 0.5, none = 0 |
| D05 | Contact and URL reachability (RFC 5322 email + valid HTTPS) | 0.20 | All reachable = 1.0, partial = 0.5, invalid = 0 |

## Actions
| Score | Action |
|---|---|
| GOLDEN | >=9.5 | Auto-publish with no review |
| PUBLISH | >=8.0 | Auto-publish after validation |
| REVIEW | >=7.0 | Require manual review |
| REJECT | <7.0 | Reject and flag for correction |

## Bypass
| Conditions | Approver | Audit Trail |
|---|---|---|
| Emergency partner onboarding | Head of Partner Management | Escalation log |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
