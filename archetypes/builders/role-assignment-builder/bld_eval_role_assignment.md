---
kind: quality_gate
id: p11_qg_role_assignment
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for role_assignment
quality: 9.0
title: "Quality Gate Role Assignment"
version: "1.0.0"
author: n03_wave8_builder
tags: [role_assignment, builder, quality_gate, composable, crewai]
tldr: "Quality gate with HARD and SOFT scoring for role_assignment"
domain: "role_assignment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
related:
  - bld_examples_role_assignment
  - role-assignment-builder
  - bld_output_template_role_assignment
  - bld_instruction_role_assignment
  - bld_knowledge_card_role_assignment
  - p03_sp_role_assignment_builder
  - bld_schema_role_assignment
  - bld_tools_role_assignment
  - bld_collaboration_role_assignment
  - p11_qg_crew_template
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|---|---|---|---|
| Role binding resolvability | 100% | equals | All role_assignment artifacts |
| Tools-allowed subset validity | 100% | equals | vs. agent native toolkit |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML or missing required fields |
| H02 | ID matches ^p02_ra_[a-z][a-z0-9_]+\.md$ | ID pattern mismatch |
| H03 | kind field == 'role_assignment' | Kind field incorrect or missing |
| H04 | agent_id resolves to .claude/agents/*.md OR N0x/agents/* | Broken agent_id reference |
| H05 | role_name is snake_case | Non-snake_case role_name |
| H06 | tools_allowed is subset of agent native toolkit | Phantom tool in tools_allowed |
| H07 | delegation_policy.can_delegate_to uses role_names not agent_ids | agent_id leaked into delegation list |
| H08 | backstory present + goal present + measurable | Missing or vague goal/backstory |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Responsibility clarity (3-5 testable bullets) | 0.25 | All testable = 1.0, mixed = 0.5, vague = 0 |
| D02 | Backstory quality (CrewAI persona hook) | 0.20 | Domain-grounded = 1.0, generic = 0.5, absent = 0 |
| D03 | Goal measurability (outcome not activity) | 0.25 | Has threshold/check = 1.0, outcome-shaped = 0.5, activity = 0 |
| D04 | Tools-allowed precision (least-privilege) | 0.15 | Minimal subset = 1.0, broad = 0.5, wildcard = 0 |
| D05 | Delegation policy specificity | 0.15 | Conditions+roles = 1.0, roles only = 0.5, open = 0 |

## Actions
| Score | Action |
|---|---|
| GOLDEN | >=9.5 | Auto-register as reusable role atom |
| PUBLISH | >=8.0 | Publish to role-assignment library |
| REVIEW | >=7.0 | Request peer review |
| REJECT | <7.0 | Rebuild per 8F F6 |

## Bypass
| Conditions | Approver | Audit Trail |
|---|---|---|
| Temporary one-off role (research) | Nucleus lead | .cex/experiments/results.tsv |

## Examples

## Golden Example
```markdown
---
id: p02_ra_domain_researcher.md
kind: role_assignment
pillar: P02
role_name: domain_researcher
agent_id: .claude/agents/research-pipeline-builder.md
goal: Produce 8-12 citable sources per brief with confidence score >= 0.75 avg.
backstory: You are a senior market intelligence analyst with 10y in AI/SaaS competitive research. You triangulate primary sources (SEC filings, GitHub, product docs) before citing any claim.
crewai_equivalent: "Agent(role='Domain Researcher', goal=..., backstory=...)"
quality: null
---

## Responsibilities
1. Accept research brief (topic, scope, deadline); return 8-12 sources.
2. Validate each source against freshness (<= 12 months) and authority heuristics.
3. Output citation objects with url, confidence, snippet, fetched_at.
4. Surface gaps/contradictions in a `caveats` block.

## Tools Allowed
- WebSearch
- WebFetch
- cex_retriever
- -cex_compile  <!-- writer, not editor -->

## Delegation Policy
can_delegate_to: [peer_reviewer]
conditions:
  on_source_count_below: 6
```

## Anti-Example 1: Inline Agent Identity
```markdown
---
kind: role_assignment
role_name: writer
agent_id: "You are a helpful writer agent with tools..."
---
```
## Why it fails:
`agent_id` inlines identity instead of pointing to an agent artifact. Fails H04 (broken ref). Breaks reuse -- every crew referencing this role duplicates the inline identity. Must be `.claude/agents/{slug}.md` or `N0x/agents/{slug}.md`.

## Anti-Example 2: Delegation by agent_id (portability break)
```markdown
---
role_name: manager
agent_id: .claude/agents/supervisor-builder.md
---
## Delegation Policy
can_delegate_to:
  - .claude/agents/research-pipeline-builder.md   # agent_id, not role_name
  - .claude/agents/changelog-builder.md
```
## Why it fails:
`can_delegate_to` leaks agent_ids instead of role_names. Fails H07. Breaks crew portability -- swapping the underlying agent requires rewriting every role that delegates to it. Always name roles (e.g., `researcher`, `editor`), not agents.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
