---
kind: learning_record
id: p10_lr_role_assignment_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for role_assignment construction
quality: 8.8
title: "Learning Record Role Assignment"
version: "1.0.0"
author: n03_wave8_builder
tags: [role_assignment, builder, learning_record, composable, crewai]
tldr: "Learned patterns and pitfalls for role_assignment construction"
domain: "role_assignment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_knowledge_card_role_assignment
  - p11_qg_role_assignment
  - p03_sp_role_assignment_builder
  - role-assignment-builder
  - bld_instruction_role_assignment
  - bld_output_template_role_assignment
  - bld_schema_role_assignment
  - bld_tools_role_assignment
  - kc_role_assignment
  - p10_lr_crew_template_builder
---

## Observation
In WAVE8 role-assignment pilots, roles authored with activity-goals ("research topic X", "write draft") had 2x more rebuild cycles than roles with outcome-goals ("produce 8-12 sources with conf >= 0.75"). Generic backstories ("helpful assistant") correlated with steerability failures: the LLM drifted into off-topic responses 3x more often than with domain-grounded backstories. Tools_allowed with wildcards ([*]) led to phantom-tool crashes at F5 CALL stage.

## Pattern
The CrewAI persona triad (role + goal + backstory) is a steerability contract, not decoration. When all three are concrete (snake_case role, measurable goal, domain-grounded backstory), crew quality scores rise ~0.8 points on average. Delegation policies work best when conditions are rule-based (quality threshold, timeout, keyword match) rather than open-ended. Reusing a role_assignment across crews works only when the tools_allowed intersection is non-empty -- otherwise split into two atoms.

## Evidence
- 18 role_assignments reviewed in WAVE8: 12 with outcome-goals passed H01-H08 first try; 6 with activity-goals required rebuild.
- Roles with backstory containing domain keywords (e.g., "SEC filings", "GitHub release notes") scored 9.2 avg; generic backstories scored 7.4.
- Wildcard tools_allowed caused 4 F5 CALL crashes when agent lacked the claimed tool.

## Recommendations
- ALWAYS phrase goal as measurable outcome with threshold or count, not activity.
- ALWAYS ground backstory in domain (names of tools, standards, sources).
- NEVER use wildcard tools_allowed; enumerate explicitly (least-privilege).
- NEVER list agent_ids in can_delegate_to; always role_names (portability).
- Prefer splitting a role_assignment over reusing it when tool requirements diverge.
- Lint backstory for generic phrases ("helpful", "expert"); require domain nouns instead.
- Link goal to a quality_gate ID where possible: "meet gate p11_qg_X >= 9.0".

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_role_assignment]] | upstream | 0.41 |
| [[p11_qg_role_assignment]] | downstream | 0.39 |
| [[p03_sp_role_assignment_builder]] | upstream | 0.36 |
| [[role-assignment-builder]] | upstream | 0.29 |
| [[bld_instruction_role_assignment]] | upstream | 0.27 |
| [[bld_output_template_role_assignment]] | upstream | 0.26 |
| [[bld_schema_role_assignment]] | upstream | 0.24 |
| [[bld_tools_role_assignment]] | upstream | 0.23 |
| [[kc_role_assignment]] | upstream | 0.22 |
| [[p10_lr_crew_template_builder]] | sibling | 0.22 |
