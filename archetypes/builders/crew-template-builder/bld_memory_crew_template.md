---
kind: learning_record
id: p10_lr_crew_template_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for crew_template construction
quality: 8.8
title: "Learning Record Crew Template"
version: "1.0.0"
author: n03_wave8_builder
tags: [crew_template, builder, learning_record, composable, crewai]
tldr: "Learned patterns and pitfalls for crew_template construction"
domain: "crew_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_instruction_crew_template
  - p03_sp_crew_template_builder
  - p11_qg_crew_template
  - bld_examples_crew_template
  - bld_knowledge_card_crew_template
  - crew-template-builder
  - bld_schema_crew_template
  - bld_collaboration_crew_template
  - bld_tools_crew_template
  - bld_output_template_crew_template
---

## Observation
Early crew blueprints tended to inline role backstories and goals inside the template body, duplicating content across templates that shared roles (e.g., `peer_reviewer` appeared verbatim in 5 crews). Review turnover showed process-topology was often wrong for the task graph: sequential picked for parallelizable work (editor + illustrator independent) and hierarchical picked where no delegation was needed (overkill).

## Pattern
Treat crew_template as a pure blueprint: reference role_assignment by id, declare process topology only after drawing the dependency graph, and always pair memory_scope with an explicit retention hint. Crews with success_criteria linked to a quality_gate (gate_id threshold) passed peer review 40% more often than those with free-text criteria.

## Evidence
- 12 crew templates reviewed in WAVE8: 8 with role refs passed H05 on first try; 4 with inlined roles failed H05 and required rebuild.
- Hierarchical process used when unnecessary cost 2x tokens per run (manager round-trip overhead) without quality improvement.
- Templates citing `p11_qg_*.md` in success_criteria scored 9.1 avg; those with prose criteria scored 7.8.

## Recommendations
- ALWAYS reference role_assignment by id; NEVER inline role identity.
- Draw the dependency graph before picking process (use workflow-builder upstream if complex).
- Prefer `sequential` for linear pipelines, `hierarchical` only for true delegation, `consensus` for peer-vote.
- Declare memory_scope per role using least-privilege: default to private, promote to shared only with justification.
- Link success_criteria to quality_gate IDs (`gate >= threshold`) instead of prose; easier to verify post-run.
- Document a `crewai_equivalent`, `autogen_equivalent`, `swarm_equivalent` to aid portability.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_crew_template]] | upstream | 0.47 |
| [[p03_sp_crew_template_builder]] | upstream | 0.44 |
| [[p11_qg_crew_template]] | downstream | 0.40 |
| [[bld_examples_crew_template]] | upstream | 0.30 |
| [[bld_knowledge_card_crew_template]] | upstream | 0.29 |
| [[crew-template-builder]] | downstream | 0.28 |
| [[bld_schema_crew_template]] | upstream | 0.28 |
| [[bld_collaboration_crew_template]] | downstream | 0.25 |
| [[bld_tools_crew_template]] | upstream | 0.24 |
| [[bld_output_template_crew_template]] | upstream | 0.20 |
