---
kind: quality_gate
id: p05_qg_interactive_demo
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for interactive_demo
quality: 9.0
title: "Quality Gate Interactive Demo"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [interactive_demo, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for interactive_demo"
domain: "interactive_demo construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_interactive_demo
  - kc_interactive_demo
  - bld_output_template_interactive_demo
  - p05_qg_product_tour
  - p10_mem_interactive_demo_builder
  - interactive-demo-builder
  - p05_qg_pricing_page
  - p05_qg_integration_guide
  - bld_instruction_interactive_demo
  - bld_tools_interactive_demo
---

## Quality Gate

## Definition
(Table: metric, threshold, operator, scope)
| metric | threshold | operator | scope |
|---|---|---|---|
| Interactive demo script completeness | 100% | = | Entire product |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML syntax |
| H02 | ID matches pattern ^p05_id_[a-z][a-z0-9_]+.md$ | ID format mismatch |
| H03 | kind field matches 'interactive_demo' | Kind field incorrect |
| H04 | Guided tour steps present | Missing or incomplete steps |
| H05 | Talk track script included | Script missing or incomplete |
| H06 | User flow aligns with product | Inconsistent or broken flow |
| H07 | Accessibility compliance (WCAG 2.1 AA) | Fails accessibility checks |
| H08 | Device compatibility (desktop/mobile) | Not functional on required platforms |

## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide)
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Script completeness | 0.20 | 1.0 = all steps, talk track, and objection map present |
| D02 | User experience | 0.20 | 1.0 = seamless guided flow, no dead ends |
| D03 | Clarity | 0.15 | 1.0 = no ambiguity, active voice throughout |
| D04 | Engagement | 0.15 | 1.0 = compelling proof points and CTA present |
| D05 | Accessibility | 0.10 | 1.0 = WCAG 2.1 AA compliant |
| D06 | Localization | 0.05 | 1.0 = all target locales supported |
| D07 | Performance | 0.05 | 1.0 = <2s load time per step |
| D08 | Device compatibility | 0.10 | 1.0 = desktop and mobile verified |

## Actions
(Table: Score | Action)
| Score | Action |
|---|---|
| GOLDEN | >=9.5 | Auto-publish with celebration |
| PUBLISH | >=8.0 | Publish to production |
| REVIEW | >=7.0 | Send to UX team for review |
| REJECT | <7.0 | Block release, fix required |

## Bypass
(Table: conditions, approver, audit trail)
| conditions | approver | audit trail |
|---|---|---|
| Prototype/demo version | Product Lead | Meeting note dated 2023-10-01 |

## Examples

## Golden Example
---
title: "Notion Interactive Demo for Project Management"
kind: interactive_demo
---
**Step 1: Welcome**
- Action: Open Notion workspace
- Talk Track: "Welcome! Today, we'll explore how Notion streamlines project management."

**Step 2: Create a New Page**
- Action: Click "New Page" > Select "Project Template"
- Talk Track: "Here's a pre-built template. Customize it with your team's workflow."

**Step 3: Add Tasks**
- Action: Drag "Task" block into the page
- Talk Track: "Add tasks here. Use checkboxes for progress tracking."

**Step 4: Collaborate**
- Action: Invite team via email
- Talk Track: "Real-time collaboration is enabled. See edits as they happen."

**Step 5: Wrap-Up**
- Action: Save and share the page
- Talk Track: "That's it! Your team now has a centralized hub for projects."

## Anti-Example 1: Missing Guided Steps
---
**Step 1: Welcome**
- Talk Track: "Welcome to our demo! Let's see how this works."
---
## Why it fails
No actionable steps or structure. The demo lacks a clear tour path, making it unguided and confusing for users.

## Anti-Example 2: Placeholder Vendors
---
**Step 1: Welcome**
- Action: Use "ProviderA's tool"
- Talk Track: "ProviderA's tool helps with X. Let's see how."
---
## Why it fails
Uses generic vendor names instead of real tools. This reduces credibility and makes the demo feel generic, not tailored to actual products.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
