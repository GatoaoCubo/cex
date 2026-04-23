---
kind: quality_gate
id: p11_qg_crew_template
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for crew_template
quality: 9.0
title: "Quality Gate Crew Template"
version: "1.0.0"
author: n03_wave8_builder
tags: [crew_template, builder, quality_gate, composable, crewai]
tldr: "Quality gate with HARD and SOFT scoring for crew_template"
domain: "crew_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
related:
  - bld_examples_crew_template
  - bld_instruction_crew_template
  - p03_sp_crew_template_builder
  - p10_lr_crew_template_builder
  - bld_output_template_crew_template
  - crew-template-builder
  - bld_schema_crew_template
  - bld_knowledge_card_crew_template
  - p11_qg_role_assignment
  - bld_collaboration_crew_template
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|---|---|---|---|
| Crew blueprint completeness | 100% | equals | All composable-crew templates |
| Role reference validity | 100% | equals | Every role_assignment reference |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches ^p12_ct_[a-z][a-z0-9_]+\.md$ | ID pattern mismatch |
| H03 | kind field == 'crew_template' | Kind field incorrect or missing |
| H04 | process in {sequential, hierarchical, consensus} | Invalid process topology |
| H05 | All role refs resolve to existing role_assignment artifacts | Broken role_assignment reference |
| H06 | memory_scope declared per role | Missing memory_scope for any role |
| H07 | success_criteria measurable (threshold / count / gate_id) | Subjective or missing success_criteria |
| H08 | handoff_protocol specified and consistent | Missing or mixed handoff-protocols |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Role composition coherence (roles cover task boundary) | 0.25 | Full coverage = 1.0, gaps = 0.5, mismatched = 0 |
| D02 | Process topology fit (matches dependency graph) | 0.20 | Optimal = 1.0, workable = 0.5, wrong = 0 |
| D03 | Memory-scope precision (least-privilege per role) | 0.15 | Minimal scope = 1.0, over-shared = 0.5, leaky = 0 |
| D04 | Handoff-protocol portability (A2A / Swarm / native) | 0.15 | Industry-standard = 1.0, adapted = 0.5, ad-hoc = 0 |
| D05 | Success-criteria measurability and specificity | 0.25 | Gate-IDs + thresholds = 1.0, counts only = 0.5, vague = 0 |

## Actions
| Score | Action |
|---|---|
| GOLDEN | >=9.5 | Auto-register as reusable crew template |
| PUBLISH | >=8.0 | Publish to crew-template library |
| REVIEW | >=7.0 | Request peer review from N03 |
| REJECT | <7.0 | Rebuild per 8F F6 |

## Bypass
| Conditions | Approver | Audit Trail |
|---|---|---|
| Experimental crew pattern (research) | N01 lead | .cex/experiments/results.tsv |

## Examples

## Golden Example
```markdown
---
id: p12_ct_research_brief.md
kind: crew_template
pillar: P12
crew_name: research_brief
purpose: Produce a peer-reviewed market intelligence brief in one pass.
process: hierarchical
crewai_equivalent: Process.hierarchical
autogen_equivalent: GroupChat.manager_delegated
swarm_equivalent: triage -> researcher -> editor -> reviewer
handoff_protocol_id: p12_hp_a2a_task.md
quality: null
---

## Roles
| Role | Assignment ID | Reason |
|------|----|----|
| manager | p02_ra_research_manager.md | Delegates, checks quality, closes loop |
| researcher | p02_ra_domain_researcher.md | Gathers sources, synthesizes |
| editor | p02_ra_brief_editor.md | Compresses to 1-page brief |
| reviewer | p02_ra_peer_reviewer.md | Scores against quality_gate 8.0 floor |

## Memory Scope
| Role | Scope | Retention |
|------|----|----|
| manager | shared | crew-session |
| researcher | private | 24h |
| editor | shared | crew-session |
| reviewer | shared | persistent |

## Success Criteria
- [ ] brief artifact quality >= 9.0 (gate p11_qg_analyst_briefing)
- [ ] all 4 roles signaled complete
- [ ] total runtime < 15min
```

## Anti-Example 1: Inline Role Identity (schema violation)
```markdown
---
kind: crew_template
crew_name: bad_crew
---
## Roles
- researcher: "You are a helpful researcher with 10y exp..."
- editor: "You edit text concisely..."
```
## Why it fails:
Inlines role definitions instead of referencing role_assignment artifacts. Breaks H05 (role-ref validity), makes roles non-reusable, duplicates content across templates. Must use `p02_ra_*.md` references.

## Anti-Example 2: Missing Process + Memory-Scope
```markdown
---
kind: crew_template
crew_name: another_bad
---
## Roles
| Role | ID |
| writer | p02_ra_writer.md |
| proofreader | p02_ra_proofreader.md |
```
## Why it fails:
No `process` field (H04 fails -- unknown topology). No memory_scope (H06 fails). No success_criteria (H07 fails). A crew blueprint without coordination semantics is just a role list, not a template.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
