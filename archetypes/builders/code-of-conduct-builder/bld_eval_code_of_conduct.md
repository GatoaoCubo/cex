---
kind: quality_gate
id: p05_qg_code_of_conduct
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for code_of_conduct
quality: 9.0
title: "Quality Gate Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for code_of_conduct"
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_examples_code_of_conduct
  - bld_instruction_code_of_conduct
  - bld_knowledge_card_code_of_conduct
  - bld_output_template_code_of_conduct
  - code-of-conduct-builder
  - p03_sp_code_of_conduct_builder
  - bld_schema_code_of_conduct
  - p10_mem_code_of_conduct_builder
  - p05_qg_github_issue_template
  - p11_qg_audit_log
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Enforcement ladder completeness | 4 levels | equals | All CoC artifacts |
| Reporting channel present | 1 contact | minimum | All CoC artifacts |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches pattern ^p05_coc_[a-z][a-z0-9_]+.md$ | ID format mismatch |
| H03 | kind field matches "code_of_conduct" | Kind field incorrect or missing |
| H04 | contact_email field present and non-empty | Missing or empty reporting channel |
| H05 | Enforcement ladder has all 4 levels | Missing Correction, Warning, Temp Ban, or Perm Ban |
| H06 | Our Pledge section present | Missing pledge commitment statement |
| H07 | Attribution to Contributor Covenant present | Missing source attribution |
| H08 | Scope section covers online spaces | No scope definition |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Pledge quality (inclusive, specific commitment) | 0.25 | 1.0 (specific + inclusive) to 0.0 (vague or missing) |
| D02 | Standards completeness (positive + negative behaviors) | 0.25 | 1.0 (5+ each) to 0.0 (<3 total) |
| D03 | Enforcement ladder clarity (4 tiers with consequences) | 0.25 | 1.0 (all 4 tiers with consequences) to 0.0 (<2 tiers) |
| D04 | Reporting channel usability (email + SLA + confidentiality) | 0.15 | 1.0 (all 3 elements) to 0.0 (email only) |
| D05 | Attribution and version accuracy | 0.10 | 1.0 (correct version + URL) to 0.0 (missing) |

## Actions
| Score | Action |
|-------|--------|
| GOLDEN (>=9.5) | Auto-publish; no review required |
| PUBLISH (>=8.0) | Publish after maintainer approval |
| REVIEW (>=7.0) | Flag for community review |
| REJECT (<7.0) | Reject; request revision against H gates |

## Bypass
| Conditions | Approver | Audit Trail |
|------------|----------|-------------|
| Emergency conduct incident | Lead Maintainer | GitHub issue + approval comment |

## Examples

## Golden Example
```markdown
---
id: p05_coc_openwidget.md
kind: code_of_conduct
pillar: P05
title: "OpenWidget Code of Conduct"
contact_email: "conduct@openwidget.org"
enforcement_version: "2.1"
scope: "online_and_offline"
response_sla: "48h"
quality: null
version: "1.0.0"
created: "2026-04-14"
updated: "2026-04-14"
---

# Contributor Covenant Code of Conduct

## Our Pledge
We as members, contributors, and leaders of OpenWidget pledge to make
participation in our community a harassment-free experience for everyone...

## Our Standards
Examples of behavior that contributes to a positive environment:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints

Examples of unacceptable behavior:
- Harassment, trolling, or personal attacks
- Publishing others' private information

## Enforcement Responsibilities
Community leaders are responsible for clarifying and enforcing standards...

## Scope
This CoC applies within all community spaces, online and offline.

## Enforcement
Report incidents to conduct@openwidget.org. Response within 48h guaranteed.

### Enforcement Guidelines
1. Correction -- written warning for minor infractions
2. Warning -- formal warning with restrictions
3. Temporary Ban -- time-limited removal from community
4. Permanent Ban -- permanent removal for repeated violations

## Attribution
Adapted from the Contributor Covenant, version 2.1.
```

## Anti-Example 1: Missing Enforcement Ladder
```markdown
---
kind: code_of_conduct
title: "Project Rules"
---
Be nice. No harassment. Email us if there are problems at info@project.com.
```
Why it fails: No enforcement ladder, no pledge section, no scope definition, no attribution. Unactionable for maintainers facing a real incident.

## Anti-Example 2: Domain Contamination
```markdown
---
kind: code_of_conduct
title: "Investment Community Code of Conduct"
---
All members must disclose financial interests before recommending assets...
```
Why it fails: Financial/investment domain language contaminating an OSS community conduct document. CoC is about contributor behavior, not financial disclosures.

## Anti-Example 3: Weights Not Summing to 1.0
```
D01 | Pledge quality | 0.10
D02 | Standards | 0.20
D03 | Enforcement | 0.15
D04 | Reporting | 0.10
-- Total: 0.55 (FAIL -- must be 1.00)
```
Why it fails: Quality gate soft scoring weights must sum exactly to 1.00 for valid normalization.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
