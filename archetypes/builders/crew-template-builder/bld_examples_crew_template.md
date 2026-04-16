---
kind: examples
id: bld_examples_crew_template
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of crew_template artifacts
quality: 9.1
title: "Examples Crew Template"
version: "1.0.0"
author: n03_wave8_builder
tags: [crew_template, builder, examples, composable, crewai]
tldr: "Golden and anti-examples of crew_template artifacts"
domain: "crew_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

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
