---
kind: quality_gate
id: p05_qg_contributor_guide
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for contributor_guide
quality: 8.9
title: "Quality Gate Contributor Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [contributor_guide, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for contributor_guide"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_contributor_guide
  - bld_output_template_contributor_guide
  - bld_instruction_contributor_guide
  - bld_tools_contributor_guide
  - p03_sp_contributor_guide_builder
  - kc_contributor_guide
  - contributor-guide-builder
  - p05_qg_github_issue_template
  - p10_mem_contributor_guide_builder
  - bld_knowledge_card_contributor_guide
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| completeness | 100% | >= | required sections |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML syntax |
| H02 | ID matches pattern ^p05_cg_[a-z][a-z0-9_]+.md$ | invalid filename |
| H03 | kind field matches 'contributor_guide' | mismatched kind |
| H04 | dev setup instructions present | missing setup guide |
| H05 | PR flow documented | incomplete PR process |
| H06 | coding standards defined | no style guidelines |
| H07 | review process outlined | missing review criteria |
| H08 | CLA process described | no CLA requirements |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Clarity | 0.15 | 1.0=unambiguous |
| D02 | Completeness | 0.20 | 1.0=all sections present |
| D03 | Structure | 0.15 | 1.0=logical flow |
| D04 | Coding standards | 0.15 | 1.0=specific and enforceable |
| D05 | PR process | 0.10 | 1.0=step-by-step |
| D06 | Review process | 0.10 | 1.0=clear expectations |
| D07 | CLA compliance | 0.15 | 1.0=explicit requirements |

## Actions
| Score | Action |
|---|---|
| GOLDEN >=9.5 | Auto-approve and publish |
| PUBLISH >=8.0 | Manual review required |
| REVIEW >=7.0 | Minor edits needed |
| REJECT <7.0 | Reject and request rewrite |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| emergency release | CTO | signed waiver |

## Examples

## Golden Example
**Contributing to Kubernetes**
**Developer Setup**  
1. Install [Go 1.20+](https://golang.org/dl/)  
2. Clone repo: `git clone https://github.com/kubernetes/kubernetes.git`  
3. Run: `make generate && make test`  
**PR Flow**  
1. Fork repo on GitHub  
2. Create branch: `git checkout -b feature/your-fix`  
3. Commit with [Conventional Commits](https://www.conventionalcommits.org/)  
4. Submit PR to `main` with title prefix: `kind/`  
**Coding Standards**  
- Use GoFmt and [golint](https://github.com/golang/lint)  
- 100% test coverage required  
- No unreviewed dependencies  

**Review Process**  
- Requires 2 LGTMs from maintainers  
- Code owners must approve  
- Merge via GitHub squash  

**CLA**  
All contributors must sign [Apache 2.0 CLA](https://cla.apache.org/)  

## Anti-Example 1: Missing CLA Section
**Contributing to ExampleProject**  
**Developer Setup**  
Install Node.js and run `npm install`.  

**PR Flow**  
Submit PRs to `develop` branch.  

**Coding Standards**  
Use ESLint and write tests.  

**Review Process**  
Maintainers will review within 7 days.  

**Why it fails**  
No CLA requirement specified. Contributors may submit code without legal agreement, risking project liability.  

## Anti-Example 2: Vague Setup Instructions
**Contributing to SampleApp**  
**Developer Setup**  
"Set up your environment."  

**PR Flow**  
"Follow standard process."  

**Coding Standards**  
"Follow best practices."  

**Review Process**  
"Get feedback from team."  

**Why it fails**  
Instructions are too vague. Contributors cannot reproduce the environment or follow workflow, leading to failed contributions and wasted time.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
