---
kind: tools
id: bld_tools_nucleus_def
pillar: P04
llm_function: CALL
purpose: Tools available for nucleus_def production
quality: 9.0
title: "Tools Nucleus Def"
version: "1.0.0"
author: n05_wave8
tags: [nucleus_def, builder, tools]
tldr: "Tools available for nucleus_def production"
domain: "nucleus_def construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_nucleus_def
  - bld_collaboration_nucleus_def
  - p10_lr_nucleus_def_builder
  - bld_output_template_nucleus_def
  - nucleus-def-builder
  - bld_architecture_nucleus_def
  - bld_knowledge_card_nucleus_def
  - bld_examples_nucleus_def
  - bld_system_prompt_nucleus_def
  - p02_qg_nucleus_def
---

## Production Tools

| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile nucleus_def .md to .yaml | After save |
| cex_score.py | Apply peer-review quality score | Post-review |
| cex_retriever.py | Find similar nucleus artifacts | During F3 INJECT |
| cex_doctor.py | Verify boot_script paths exist | F7 GOVERN |
| cex_router.py | Validate cli_binding vs nucleus_models.yaml | F7 GOVERN |
| cex_agent_spawn.py | Pre-flight check for boot contract validity | F7 GOVERN |

## Validation Tools

| Tool | Purpose | When |
|------|---------|------|
| cex_sanitize.py | Check ASCII compliance (code files) | Pre-commit |
| cex_hooks.py | Pre-commit validation | Before git commit |
| cex_schema_hydrate.py | Hydrate nucleus_def with universal patterns | F3 INJECT |
| cex_compile.py --check | Verify YAML frontmatter valid | F7 GOVERN |

## Data Sources (read-only)

| Source | What to Extract | Command |
|--------|----------------|---------|
| .cex/config/nucleus_models.yaml | cli_binding, model_tier, model_specific | Read file |
| .cex/kinds_meta.json | Pillar assignments for pillar ownership map | Read + filter by pillar |
| .claude/rules/n0{X}-*.md | Role, sin_lens, domain routing | Grep for Identity section |
| N0{X}_*/agent_card_n0{X}.md | Domain agents, kinds_owned | Read Identity + Kinds sections |
| N00_genesis/README.md | Fractal structure, pillar map | Read full document |
| boot/n0{X}.ps1 | Verify boot script exists | ls / Glob |
| N0{X}_*/agents/*.md | Enumerate domain_agents | Glob pattern |

## kinds_meta.json Update

After creating nucleus-def-builder, add to kinds_meta.json:
```json
"nucleus_def": {
  "pillar": "P02",
  "llm_function": "CONSTRAIN",
  "naming": "p02_nd_{{nucleus_id_lower}}.md",
  "max_bytes": 5120,
  "core": true,
  "description": "Formal definition of a CEX nucleus (N00-N07). Fields: nucleus_id, role, pillars_owned, sin_lens, cli_binding, model_tier, boot_script, agent_card_path, crew_templates_exposed, domain_agents.",
  "boundary": "Nucleus contract. NOT agent (individual agent in N0x/P02_model/) nor model_provider (LLM provider config).",
  "status": "stable"
}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_nucleus_def]] | upstream | 0.41 |
| [[bld_collaboration_nucleus_def]] | downstream | 0.37 |
| [[p10_lr_nucleus_def_builder]] | downstream | 0.37 |
| [[bld_output_template_nucleus_def]] | downstream | 0.34 |
| [[nucleus-def-builder]] | upstream | 0.33 |
| [[bld_architecture_nucleus_def]] | downstream | 0.32 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.32 |
| [[bld_examples_nucleus_def]] | downstream | 0.32 |
| [[bld_system_prompt_nucleus_def]] | upstream | 0.30 |
| [[p02_qg_nucleus_def]] | downstream | 0.30 |
