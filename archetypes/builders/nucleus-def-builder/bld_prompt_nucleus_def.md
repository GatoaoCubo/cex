---
kind: instruction
id: bld_instruction_nucleus_def
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for nucleus_def
quality: 8.9
title: "Instruction Nucleus Def"
version: "1.0.0"
author: n05_wave8
tags: [nucleus_def, builder, instruction]
tldr: "Step-by-step production process for nucleus_def"
domain: "nucleus_def construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_nucleus_def
  - bld_schema_nucleus_def
  - bld_tools_nucleus_def
  - p02_qg_nucleus_def
  - bld_knowledge_card_nucleus_def
  - p10_lr_nucleus_def_builder
  - nucleus-def-builder
  - bld_output_template_nucleus_def
  - bld_collaboration_nucleus_def
  - bld_system_prompt_nucleus_def
---

## Phase 1: RESEARCH
1. Read `.cex/config/nucleus_models.yaml` to extract cli_binding and model_tier for the target nucleus.
2. Read `.claude/rules/n0{X}-*.md` rule file to extract role, domain, and sin_lens.
3. Read `N0{X}_*/agent_card_n0{X}.md` to enumerate domain_agents and kinds_owned.
4. Scan `N0{X}_*/agents/` directory for non-builder agent definitions.
5. Scan `N0{X}_*/` for boot_script path (boot/n0{X}.ps1).
6. Read `N00_genesis/README.md` for fractal structure and pillar assignment.
7. Cross-reference `.cex/kinds_meta.json` for pillar ownership mapping.

## Phase 2: COMPOSE
1. Reference bld_schema_nucleus_def.md for required frontmatter fields.
2. Set nucleus_id to canonical form: N00, N01, N02, N03, N04, N05, N06, N07.
3. Set role from enum: genesis | intelligence | marketing | builder | knowledge | operations | commercial | orchestrator.
4. Populate pillars_owned as array of pillar codes (e.g., [P01, P07, P08, P09]).
5. Set sin_lens from nucleus rule file (e.g., "Gating Wrath").
6. Set cli_binding from nucleus_models.yaml (claude | gemini | codex | ollama).
7. Set model_tier from nucleus_models.yaml (opus | sonnet | haiku | local).
8. Set boot_script to canonical path (e.g., boot/n05.ps1).
9. Set agent_card_path to canonical path (e.g., N05_operations/agent_card_n05.md).
10. List crew_templates_exposed: which crew patterns this nucleus assembles.
11. List domain_agents: all non-builder agents in N0{X}_*/agents/.
12. Use OUTPUT_TEMPLATE.md to produce the artifact body.

## Phase 3: VALIDATE
- [ ] All required fields present (nucleus_id, role, pillars_owned, sin_lens, cli_binding, model_tier).
- [ ] nucleus_id matches pattern N0[0-7].
- [ ] role is one of the 8 valid enum values.
- [ ] pillars_owned is a non-empty array of valid P01-P12 codes.
- [ ] cli_binding matches nucleus_models.yaml for the target nucleus.
- [ ] crew_templates_exposed lists at least 1 composable pattern.
- [ ] domain_agents lists known agents or empty array if none.
- [ ] ID matches pattern ^p02_nd_n0[0-7]\.md$.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_nucleus_def]] | downstream | 0.43 |
| [[bld_schema_nucleus_def]] | downstream | 0.41 |
| [[bld_tools_nucleus_def]] | downstream | 0.40 |
| [[p02_qg_nucleus_def]] | downstream | 0.38 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.36 |
| [[p10_lr_nucleus_def_builder]] | downstream | 0.34 |
| [[nucleus-def-builder]] | upstream | 0.30 |
| [[bld_output_template_nucleus_def]] | downstream | 0.30 |
| [[bld_collaboration_nucleus_def]] | downstream | 0.29 |
| [[bld_system_prompt_nucleus_def]] | related | 0.28 |
