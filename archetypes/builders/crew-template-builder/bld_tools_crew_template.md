---
kind: tools
id: bld_tools_crew_template
pillar: P04
llm_function: CALL
purpose: Tools available for crew_template production
quality: 8.9
title: "Tools Crew Template"
version: "1.0.0"
author: n03_wave8_builder
tags: [crew_template, builder, tools, composable, crewai]
tldr: "Tools available for crew_template production"
domain: "crew_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.86
related:
  - bld_tools_role_assignment
  - bld_knowledge_card_crew_template
  - bld_instruction_crew_template
  - bld_tools_roi_calculator
  - bld_tools_skill
  - p03_sp_crew_template_builder
  - p11_qg_crew_template
  - bld_tools_discovery_questions
  - bld_tools_benchmark_suite
  - bld_tools_sales_playbook
---

## Production Tools
| Tool              | Purpose                                  | When                      |
|-------------------|------------------------------------------|---------------------------|
| cex_compile.py    | Compile crew_template .md to .yaml blueprint | F8 COLLABORATE        |
| cex_retriever.py  | Find similar crew templates (reuse)      | F3 INJECT                 |
| cex_query.py      | Discover role_assignment refs            | F1 CONSTRAIN              |
| cex_doctor.py     | Validate all role refs resolve           | F7 GOVERN                 |
| cex_score.py      | Peer-review scoring (HARD + SOFT)        | F7 GOVERN                 |
| signal_writer.py  | Signal N07 on completion                 | F8 COLLABORATE            |

## Validation Tools
| Tool                  | Purpose                                    | When          |
|-----------------------|--------------------------------------------|---------------|
| cex_validate_refs.py  | Resolve p02_ra_* references                | Pre-commit    |
| cex_process_lint.py   | Check topology vs dependency graph         | F7 GOVERN     |
| cex_memory_scope.py   | Flag over-shared memory_scope              | F7 GOVERN     |
| cex_success_linter.py | Require measurable success_criteria       | F7 GOVERN     |

## External References
- CrewAI Process API docs (`crewai.process.Process`)
- Microsoft Agent Framework GroupChat patterns (MAF v1.0 preview)
- OpenAI Agents SDK v0.6+ handoff/transfer functions
- Google A2A v0.3.0 Task lifecycle specification
- LangGraph StateGraph conditional edges (consensus equivalent)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_role_assignment]] | sibling | 0.51 |
| [[bld_knowledge_card_crew_template]] | upstream | 0.36 |
| [[bld_instruction_crew_template]] | upstream | 0.32 |
| [[bld_tools_roi_calculator]] | sibling | 0.30 |
| [[bld_tools_skill]] | sibling | 0.28 |
| [[p03_sp_crew_template_builder]] | upstream | 0.28 |
| [[p11_qg_crew_template]] | downstream | 0.28 |
| [[bld_tools_discovery_questions]] | sibling | 0.28 |
| [[bld_tools_benchmark_suite]] | sibling | 0.26 |
| [[bld_tools_sales_playbook]] | sibling | 0.26 |
