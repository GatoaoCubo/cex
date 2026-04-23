---
kind: tools
id: bld_tools_lens
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for lens production
quality: 9.0
title: "Tools Lens"
version: "1.0.0"
author: n03_builder
tags: [lens, builder, examples]
tldr: "Golden and anti-examples for lens construction, demonstrating ideal structure and common pitfalls."
domain: "lens construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_memory_scope
  - bld_tools_retriever_config
  - bld_tools_validator
  - bld_tools_handoff_protocol
  - bld_tools_cli_tool
  - bld_tools_input_schema
  - bld_tools_prompt_version
  - bld_tools_path_config
  - bld_tools_action_prompt
  - bld_tools_output_validator
---

# Tools: lens-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing lenses in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P02_model/_schema.yaml | Field definitions for lens |
| CEX Examples | P02_model/examples/ | Real lens artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P02_lens seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Existing pool | pool/ (brain_query) | Existing lenses |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet for lenses.
Manually check each QUALITY_GATES.md gate against produced artifact:
1. [ ] YAML parses without error
2. [ ] id matches p02_lens_ prefix
3. [ ] perspective is non-empty
4. [ ] applies_to is list with >= 1 entry
5. [ ] quality is null
6. [ ] All 4 body sections present

## Metadata

```yaml
id: bld_tools_lens
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-lens.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_memory_scope]] | sibling | 0.69 |
| [[bld_tools_retriever_config]] | sibling | 0.66 |
| [[bld_tools_validator]] | sibling | 0.66 |
| [[bld_tools_handoff_protocol]] | sibling | 0.66 |
| [[bld_tools_cli_tool]] | sibling | 0.66 |
| [[bld_tools_input_schema]] | sibling | 0.65 |
| [[bld_tools_prompt_version]] | sibling | 0.64 |
| [[bld_tools_path_config]] | sibling | 0.64 |
| [[bld_tools_action_prompt]] | sibling | 0.63 |
| [[bld_tools_output_validator]] | sibling | 0.63 |
