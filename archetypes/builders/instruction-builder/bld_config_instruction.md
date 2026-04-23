---
kind: config
id: bld_config_instruction
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Instruction"
version: "1.0.0"
author: n03_builder
tags: [instruction, builder, examples]
tldr: "Golden and anti-examples for instruction construction, demonstrating ideal structure and common pitfalls."
domain: "instruction construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_prompt_version
  - bld_config_action_prompt
  - bld_config_constraint_spec
  - bld_config_retriever_config
  - bld_config_memory_scope
  - bld_config_chain
  - bld_config_output_validator
  - bld_config_workflow
  - bld_config_handoff_protocol
  - p10_lr_instruction_builder
---
# Config: instruction Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_ins_{task_slug}.md` | `p03_ins_rebuild_brain_faiss.md` |
| Builder directory | kebab-case | `instruction-builder/` |
| Frontmatter fields | snake_case | `steps_count`, `validation_method` |
| Task slug | snake_case, lowercase | `rebuild_brain_faiss`, `deploy_api` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `cex/P03_prompt/examples/p03_ins_{task_slug}.md`
2. Compiled: `cex/P03_prompt/compiled/p03_ins_{task_slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Total (frontmatter + body): ~5500 bytes
3. Density: >= 0.80
## Validation Method Enum
| Value | When to use |
|-------|-------------|
| checklist | Manual verification via checkbox list (most common) |
| automated | Script or test validates outcome |
| manual | Human judgment required (subjective) |
| none | Fire-and-forget (rare, discouraged) |
## Step Writing Rules
1. One action per step (verb + object + expected outcome)
2. Steps numbered sequentially (1, 2, 3...)
3. Include concrete commands where applicable (not "run the script" but `python build.py --all`)
4. Expected outcome after dash: "1. Run build — output shows 0 errors"
5. If step has conditional: split into sub-steps (1a, 1b) or separate steps

## Metadata

```yaml
id: bld_config_instruction
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-instruction.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_prompt_version]] | sibling | 0.36 |
| [[bld_config_action_prompt]] | sibling | 0.34 |
| [[bld_config_constraint_spec]] | sibling | 0.33 |
| [[bld_config_retriever_config]] | sibling | 0.33 |
| [[bld_config_memory_scope]] | sibling | 0.33 |
| [[bld_config_chain]] | sibling | 0.32 |
| [[bld_config_output_validator]] | sibling | 0.32 |
| [[bld_config_workflow]] | sibling | 0.30 |
| [[bld_config_handoff_protocol]] | sibling | 0.30 |
| [[p10_lr_instruction_builder]] | downstream | 0.30 |
