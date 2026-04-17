---
kind: quality_gate
id: p11_qg_agent_profile
pillar: P11
llm_function: GOVERN
purpose: HARD gates and SOFT 5D scoring rubric for agent_profile artifacts
quality: 9.2
title: "Quality Gate Agent Profile"
version: "1.1.0"
author: n03_builder
tags: [agent_profile, builder, quality_gate, P11, governance]
keywords: [hard_gate, soft_scoring, 5d_rubric, density, persona_completeness]
triggers: ["score agent_profile", "validate p02_ap", "quality gate persona"]
tldr: "10 HARD gates (YAML, id pattern, enum values, section presence, constraint form) + 5D SOFT rubric (density, specificity, correctness, completeness, consistency) with thresholds: GOLDEN >=9.5, PUBLISH >=8.0, REVIEW >=7.0, REJECT <7.0."
domain: "agent_profile governance"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.89
---

# Quality Gate: agent_profile

## Definition
Validates every `p02_ap_*.md` before publish. Reads the artifact, applies 10 HARD gates (any fail -> reject), then the 5D SOFT rubric for numeric score. Peer review (not self) assigns `quality`.

## HARD Gates (all 10 must PASS)
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter parses | Invalid YAML, tabs in indent, missing `---` delimiters |
| H02 | id pattern | id does not match `^p02_ap_[a-z][a-z0-9_]+$` |
| H03 | kind value | kind != `agent_profile` |
| H04 | pillar value | pillar != `P02` |
| H05 | quality is null | quality is self-scored (not null) |
| H06 | agent_type enum | agent_type not in {operator, analyst, automaton} |
| H07 | status enum | status not in {active, inactive, pending} |
| H08 | expertise populated | expertise is empty list or missing |
| H09 | body sections | Missing any of: Overview, Identity Vectors, Capabilities, Constraints, Collaborators, Compliance |
| H10 | constraint form | Fewer than 3 constraints in ALWAYS/NEVER/IF-THEN form |

## SOFT Scoring (5D rubric, weighted average, each 0-10)
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D1 | Density | 0.20 | 10=tables/vectors, zero filler. 5=mixed. 0=prose padding. Target >= 0.85 density_score. |
| D2 | Specificity | 0.25 | 10=named domain terms, cited regulations. 0=generic "helpful assistant" phrasing. |
| D3 | Correctness | 0.20 | 10=no scope leaks (system_prompt, runtime code, agent_card content). 0=full leak. |
| D4 | Completeness | 0.20 | 10=all frontmatter + 6 sections filled. 0=stub placeholders visible. |
| D5 | Consistency | 0.15 | 10=collaborators reference real sibling ids; identity vectors align. 0=contradictions. |

Final score = 0.20*D1 + 0.25*D2 + 0.20*D3 + 0.20*D4 + 0.15*D5

## Actions (by final score)
| Band | Score | Action |
|---|---|---|
| GOLDEN | >= 9.5 | Auto-approve; eligible for example library |
| PUBLISH | >= 8.0 | Merge to production; notify consuming agent_card owners |
| REVIEW | >= 7.0 | Return to N03 for targeted fixes; list failing dimension(s) |
| REJECT | < 7.0 | Block publish; require full rebuild via `bld_instruction_agent_profile.md` |

## Common Fail Patterns (observed)
1. Merging system_prompt rules into Constraints section (fails D3 Correctness).
2. Empty identity_vectors or stub `{{var}}` placeholders (fails H09 + D4).
3. Generic capabilities like "Answers questions" (fails D2 Specificity, score <=3).
4. Collaborators listed by role ("Manager") instead of sibling id (fails D5 Consistency).
5. Invented ID pattern like `agent-abc12345` instead of `p02_ap_<slug>` (fails H02).

## Bypass
| Conditions | Approver | Audit Trail |
|---|---|---|
| Urgent production hotfix, score in [7.0, 8.0) | N07 orchestrator | Record in `.cex/runtime/decisions/` with rationale + rollback plan |

## Tooling
- `python _tools/cex_score.py --apply <file>` -> numeric score
- `python _tools/cex_doctor.py` -> structural check
- Reference: `bld_schema_agent_profile.md` (fields), `bld_examples_agent_profile.md` (calibration)
