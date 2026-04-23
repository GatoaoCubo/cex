---
kind: quality_gate
id: p05_qg_quickstart_guide
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for quickstart_guide
quality: 9.0
title: "Quality Gate Quickstart Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [quickstart_guide, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for quickstart_guide"
domain: "quickstart_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_quickstart_guide
  - p05_qg_github_issue_template
  - bld_instruction_quickstart_guide
  - bld_examples_integration_guide
  - p05_qg_integration_guide
  - p03_qg_reasoning_strategy
  - p05_qg_product_tour
  - p11_qg_instruction
  - p05_qg_contributor_guide
  - p06_qg_api_reference
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| ID pattern | ^p05_qs_[a-z][a-z0-9_]+.md$ | matches | all artifacts |
| step count | 3-7 numbered steps | range | guide body |
| prerequisite section present | true | equals | all artifacts |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML syntax |
| H02 | ID matches pattern ^p05_qs_[a-z][a-z0-9_]+.md$ | invalid filename format |
| H03 | kind field matches 'quickstart_guide' | incorrect kind value |
| H04 | guide includes clear title | missing or ambiguous title |
| H05 | steps are numbered sequentially | non-sequential or missing steps |
| H06 | no markdown in step content | presence of markdown formatting |
| H07 | prerequisites listed | missing prerequisite section |
| H08 | success criteria defined | no success criteria |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Clarity | 0.15 | 1.0 = unambiguous instructions |
| D02 | Completeness | 0.15 | 1.0 = all required sections present |
| D03 | Usability | 0.15 | 1.0 = actionable and concise |
| D04 | Structure | 0.10 | 1.0 = logical flow |
| D05 | Language | 0.10 | 1.0 = plain English, no jargon |
| D06 | Visuals | 0.10 | 1.0 = diagrams/tables where needed |
| D07 | Accessibility | 0.10 | 1.0 = screen-reader compatible |
| D08 | Feedback | 0.15 | 1.0 = user testing results included |

## Actions
| Score | Action |
|---|---|
| GOLDEN >=9.5 | Automate deployment |
| PUBLISH >=8.0 | Schedule review |
| REVIEW >=7.0 | Request revisions |
| REJECT <7.0 | Block release |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Legacy system integration | Senior Engineer | Note: "Legacy system exception approved" |

## Examples

## Golden Example
---
title: "Quickstart: Deploy a Static Website with Vercel and GitHub"
description: "Deploy a static website in under 5 minutes using Vercel and GitHub."
audience: "Developers new to deployment"
time: "5 minutes"
---
**Steps:**
1. **Create a GitHub repo** with your static files (HTML/CSS/JS).
2. **Install Vercel CLI** via `npm install -g vercel`.
3. **Login to Vercel** with `vercel login`.
4. **Deploy your site** with `vercel --github <your-repo>`.
5. **Access your site** via the URL provided in the CLI output.

**Notes:** No server configuration required. Uses GitHub for source control and Vercel for deployment.

## Anti-Example 1: Vague and Placeholder-Heavy
---
title: "Quickstart: Use SomeService"
description: "Get started with SomeService in minutes."
audience: "Everyone"
time: "5 minutes"
---
**Steps:**
1. **Sign up** at [somevendor.com](http://somevendor.com).
2. **Create a project** with a name and description.
3. **Use the API** with your `API_KEY` and `ENDPOINT`.
4. **Check the docs** for more info.

**Why it fails:** Uses generic terms like "SomeService" and "ENDPOINT" with no actionable steps. No real tools or vendors named. Fails to guide the user through a concrete workflow.

## Anti-Example 2: Overly Technical
---
title: "Quickstart: Use AWS S3"
description: "Set up AWS S3 in 5 minutes."
audience: "Developers"
time: "5 minutes"
---
**Steps:**
1. **Install AWS CLI** with `pip install awscli`.
2. **Configure AWS** with `aws configure`.
3. **Create a bucket** via AWS Console.
4. **Upload files** with `aws s3 cp file.txt s3://my-bucket/`.
5. **Verify** with `aws s3 ls s3://my-bucket/`.

**Why it fails:** Focuses on CLI commands and infrastructure setup, which is more suited for an integration guide. Omits high-level context like purpose or use cases, making it less accessible for quick onboarding.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
