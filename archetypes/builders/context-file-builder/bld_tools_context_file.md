---
kind: tools
id: bld_tools_context_file
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for context_file production
quality: 8.6
title: "Tools: context-file-builder"
version: "1.0.0"
author: n03_builder
tags: [context_file, builder, tools, hermes_origin]
tldr: "Tools for context_file production: Read/Write/Edit for file ops, cex_compile.py for compilation, cex_doctor.py for validation."
domain: "workspace instruction auto-injection"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.89
related:
  - bld_tools_kind
  - bld_tools_path_config
  - bld_tools_validation_schema
  - bld_tools_memory_scope
  - bld_tools_hitl_config
  - bld_tools_golden_test
  - bld_tools_retriever_config
  - bld_tools_prompt_version
  - bld_tools_response_format
  - bld_tools_constraint_spec
---

# Tools: context-file-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| Read | Load existing context_files in inheritance_chain | Phase 2 (inherit) | REQUIRED |
| Write | Create new context_file artifact | Phase 4 (compose) | REQUIRED |
| Edit | Modify existing context_file | Phase 4 (update) | CONDITIONAL |
| Glob | Discover existing context_files in project | Phase 1 (scan) | CONDITIONAL |
| Grep | Search for scope references in existing files | Phase 1 (scan) | CONDITIONAL |
| cex_compile.py | Compile .md to .yaml | Phase 5 (F8) | REQUIRED |
| cex_doctor.py | Validate artifact health | Phase 5 (F8) | RECOMMENDED |

## Data Sources
| Source | Path | Data |
|--------|------|------|
| CEX Schema | `N00_genesis/P03_prompt/_schema.yaml` | Pillar definitions, kind registry |
| Builder schema | `archetypes/builders/context-file-builder/bld_schema_context_file.md` | Field definitions |
| Builder examples | `archetypes/builders/context-file-builder/bld_examples_context_file.md` | Golden patterns |
| kinds_meta | `.cex/kinds_meta.json` | Kind registry entry |
| Inheritance parents | `{scope_path}/ctx_*.md` | Parent context_files to inherit |
| HERMES spec | `_docs/compiled/spec_hermes_assimilation.yaml` | HERMES origin patterns |

## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| EFFECTIVE | Read, Write, Edit, Glob, Grep | Core production tools |
| POST-BUILD | `python _tools/cex_compile.py {path}` | Mandatory compilation |

## Validation Steps
```
# 1. Validate frontmatter parses
python -c "import yaml; yaml.safe_load(open('{path}').read().split('---')[1])"

# 2. Compile artifact
python _tools/cex_compile.py {path}

# 3. Check scope
grep "scope:" {path}  # must be workspace|nucleus|session|global

# 4. Check injection_point
grep "injection_point:" {path}  # must be session_start|every_turn|f3_inject

# 5. Check byte budget
wc -c {path}  # total; body should be within max_bytes declared
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_kind]] | sibling | 0.49 |
| [[bld_tools_path_config]] | sibling | 0.42 |
| [[bld_tools_validation_schema]] | sibling | 0.41 |
| [[bld_tools_memory_scope]] | sibling | 0.41 |
| [[bld_tools_hitl_config]] | sibling | 0.41 |
| [[bld_tools_golden_test]] | sibling | 0.40 |
| [[bld_tools_retriever_config]] | sibling | 0.39 |
| [[bld_tools_prompt_version]] | sibling | 0.39 |
| [[bld_tools_response_format]] | sibling | 0.39 |
| [[bld_tools_constraint_spec]] | sibling | 0.39 |
