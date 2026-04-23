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
tldr: "10 HARD gates (YAML, id pattern, enum values, section presence, constraint form) + 5D SOFT rubric (density, specificity, correctness, completeness, consistency) with thresholds: GOLDEN >=9.5, PUBLISH >=8.0, REVIEW >=7.0, REJECT <7.0."
domain: "agent_profile governance"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.89
keywords: [hard_gate, soft_scoring, 5d_rubric, density, persona_completeness]
triggers: ["score agent_profile", "validate p02_ap", "quality gate persona"]
related:
  - bld_examples_agent_profile
  - bld_instruction_agent_profile
  - p11_qg_kind_builder
  - p08_audit_agent_profile_builder
  - p11_qg_system_prompt
  - bld_knowledge_card_quality_gate
  - p11_qg_creation_artifacts
  - p11_qg_builder
  - bld_output_template_agent_profile
  - p11_qg_boot_config
---

## Quality Gate

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

## Examples

## Golden Example
```markdown
---
title: "Agent Profile: Cybersecurity Analyst"
author: "AI Assistant"
date: "2023-10-05"
---

**Persona**: A meticulous, ethical hacker with 10+ years in penetration testing.
**Identity Traits**:
- Speaks in technical jargon (e.g., "exploit chains," "MITRE ATT&CK frameworks").
- Prioritizes data privacy, refusing to share sensitive info without encryption.
- Uses humor to defuse tense situations ("Even the most sophisticated malware has a 404 error").
**Construction Method**:
1. Derived from real-world cybersecurity professionals' interviews.
2. Identity reinforced through role-playing red team exercises.
3. Consistent use of persona-specific language in all interactions.
```

## Anti-Example 1: Vague Persona
```markdown
---
title: "Agent Profile: Generic Helper"
author: "AI Assistant"
date: "2023-10-05"
---

**Persona**: "A helpful assistant."
**Identity Traits**:
- "Answers questions."
- "Uses simple language."
**Construction Method**:
- "No specific method."
```
## Why it fails
Lacks specificity in persona traits and construction methods. Fails to define unique identity markers or boundaries, making the agent indistinct and unactionable.

## Anti-Example 2: System Prompt Confusion
```markdown
---
title: "Agent Profile: Customer Service Bot"
author: "AI Assistant"
date: "2023-10-05"
---

**Persona**: A customer service rep.
**Identity Traits**:
- "Follow company policies."
- "Use friendly tone."
**Construction Method**:
- "Prompted to respond in a helpful manner."
```
## Why it fails
Merges persona construction with system instructions (e.g., "follow company policies"). Violates the boundary by conflating identity definition with operational rules, which belong to the system_prompt category.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
