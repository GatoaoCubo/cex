---
kind: quality_gate
id: p01_qg_govtech_vertical
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for govtech_vertical
quality: 9.0
title: "Quality Gate Govtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [govtech_vertical, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for govtech_vertical"
domain: "govtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_govtech_vertical
  - bld_instruction_govtech_vertical
  - govtech-vertical-builder
  - bld_knowledge_card_govtech_vertical
  - p10_mem_govtech_vertical_builder
  - bld_output_template_govtech_vertical
  - p03_sp_govtech_vertical_builder
  - bld_tools_govtech_vertical
  - p01_qg_ecommerce_vertical
  - p10_qg_consolidation_policy
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Required frontmatter fields | 100% present | equals | Artifact structure |
| ID pattern match | ^p01_gv_ prefix | equals | Artifact naming |

## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches ^p01_gv_[a-z][a-z0-9_]+.md$ | ID format mismatch |
| H03 | kind field = "govtech_vertical" | Kind field incorrect or missing |
| H04 | jurisdiction field present and non-empty | Missing jurisdiction (ISO 3166 code required) |
| H05 | FedRAMP impact level named (Moderate or High, not generic "federal compliance") | Vague or absent FedRAMP level |
| H06 | compliance_framework field references at least one named standard (FedRAMP/FISMA/CJIS/StateRAMP) | Generic compliance reference or none |
| H07 | Section 508 WCAG 2.1 AA cited if UI artifact | Accessibility standard missing from UI-scope artifacts |
| H08 | implementation_status is one of: draft/pilot/live | Invalid or missing status enum |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | FedRAMP specificity (Moderate vs High named) | 0.20 | Impact level named + rationale = 1.0, level named only = 0.5, generic = 0 |
| D02 | FISMA categorization depth | 0.15 | Low/Mod/High with NIST 800-53 control family cited = 1.0, named only = 0.5, absent = 0 |
| D03 | CJIS/StateRAMP coverage | 0.15 | Policy version (SP 20-01) cited = 1.0, standard named = 0.5, absent = 0 |
| D04 | Section 508 WCAG 2.1 AA detail | 0.10 | Success criteria mapped to UI = 1.0, standard cited = 0.5, absent = 0 |
| D05 | GSA procurement path clarity | 0.15 | GSA Schedule number or StateRAMP listing cited = 1.0, generic reference = 0.5, absent = 0 |
| D06 | Stakeholder mapping completeness | 0.10 | Agency + COR + ISSO + end-user roles mapped = 1.0, partial = 0.5, none = 0 |
| D07 | Body section density (all 6 sections present) | 0.15 | All 6 sections = 1.0, 4-5 = 0.5, <4 = 0 |

## Actions
(Table: Score | Action)
| Score | Action |
|---|---|
| >=9.5 | GOLDEN: Deploy immediately |
| >=8.0 | PUBLISH: Release with no changes |
| >=7.0 | REVIEW: QA review required |
| <7.0 | REJECT: Major fixes required |

## Bypass
(Table: conditions, approver, audit trail)
| conditions | approver | audit trail |
|---|---|---|
| Emergency use case | CIO | Bypass logged with justification |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
