---
quality: 8.0
quality: 7.6
kind: config
id: bld_config_working_memory
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, size limits, and operational constraints for working_memory
effort: low
max_turns: 15
disallowed_tools: []
title: "Config Working Memory"
version: "1.0.0"
author: n03_builder
tags: [working_memory, builder, config]
tldr: "Naming, paths, size limits, and enum constraints for working_memory production."
domain: "working memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_config_memory_scope
  - bld_config_retriever_config
  - bld_config_prompt_version
  - bld_config_output_validator
  - bld_config_handoff_protocol
  - bld_config_constraint_spec
  - bld_config_context_window_config
  - bld_config_hook_config
  - bld_config_chunk_strategy
  - bld_config_learning_record
---
# Config: working_memory Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_wm_{scope}.md` | `p10_wm_n04_kc_builder.md` |
| Builder directory | kebab-case | `working-memory-builder/` |
| Frontmatter fields | snake_case | `task_id`, `context_slots`, `clear_on_complete` |
| Task slug | snake_case, lowercase | `n04_kc_builder`, `n01_research_task` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `N0x_{domain}/P10_memory/p10_wm_{scope}.md`
- Compiled: `N0x_{domain}/P10_memory/compiled/p10_wm_{scope}.yaml`

## Size Limits
- Body: max 3072 bytes
- Density: >= 0.80

## Clear Policy Enum
| Value | When | Target |
|-------|------|--------|
| clear | Pure computation, no persistent knowledge | None |
| promote | Research, analysis, knowledge extraction | entity_memory, episodic_memory, learning_record |

## Expiry Options
| Value | When to use |
|-------|-------------|
| on_task_complete | Standard; clear when task signals done |
| on_session_end | Task may span multiple turns |
| {integer}min | Fallback TTL for stuck tasks |
| manual | Developer-controlled (debugging only) |

## Capacity Unit Options
| Unit | When | Notes |
|------|------|-------|
| tokens | LLM context-aware | Measure against model's context window |
| slots | Simple key-value stores | Count of slot entries |

## Configuration Checklist

- Verify all required fields are present in frontmatter before saving
- Validate config values against schema constraints (type, range, enum)
- Cross-reference with related configs to avoid contradictions
- Test config loading in target runtime before committing

## Validation

```yaml
# Required config validation
fields_present: true
types_valid: true
ranges_checked: true
cross_refs_verified: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_memory_scope]] | sibling | 0.34 |
| [[bld_config_retriever_config]] | sibling | 0.27 |
| [[bld_config_prompt_version]] | sibling | 0.26 |
| [[bld_config_output_validator]] | sibling | 0.26 |
| [[bld_config_handoff_protocol]] | sibling | 0.25 |
| [[bld_config_constraint_spec]] | sibling | 0.25 |
| [[bld_config_context_window_config]] | sibling | 0.24 |
| [[bld_config_hook_config]] | sibling | 0.24 |
| [[bld_config_chunk_strategy]] | sibling | 0.24 |
| [[bld_config_learning_record]] | sibling | 0.24 |
