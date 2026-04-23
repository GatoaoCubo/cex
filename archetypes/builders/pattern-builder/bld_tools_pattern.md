---
kind: tools
id: bld_tools_pattern
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for pattern production
quality: 9.0
title: "Tools Pattern"
version: "1.0.0"
author: n03_builder
tags: [pattern, builder, examples]
tldr: "Golden and anti-examples for pattern construction, demonstrating ideal structure and common pitfalls."
domain: "pattern construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_learning_record
  - bld_tools_validator
  - bld_tools_input_schema
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_agent_card
  - bld_tools_path_config
  - bld_tools_runtime_rule
  - bld_tools_axiom
---

# Tools: pattern-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing patterns in pool | Phase 1 (check duplicates) | CONDITIONAL [MCP] |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P08_architecture/_schema.yaml | Field definitions for P08 kinds |
| CEX Taxonomy | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Seed Bank | archetypes/SEED_BANK.yaml | Seeds: name, problem, solution, forces |
| Existing patterns | P08_architecture/examples/ | Reference artifacts |
| GoF Patterns | Design Patterns (Gamma et al. 1994) | Classical pattern catalog |
| POSA Patterns | Pattern-Oriented Software Architecture | Distributed system patterns |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate:
- [ ] YAML frontmatter parses without error
- [ ] id matches `p08_pat_` pattern
- [ ] kind == "pattern"
- [ ] quality == null
- [ ] name is 2-5 words
- [ ] problem describes RECURRING situation
- [ ] consequences include at least 1 cost
- [ ] density >= 0.80 (no filler)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_learning_record]] | sibling | 0.57 |
| [[bld_tools_validator]] | sibling | 0.56 |
| [[bld_tools_input_schema]] | sibling | 0.56 |
| [[bld_tools_retriever_config]] | sibling | 0.56 |
| [[bld_tools_memory_scope]] | sibling | 0.55 |
| [[bld_tools_cli_tool]] | sibling | 0.55 |
| [[bld_tools_agent_card]] | sibling | 0.54 |
| [[bld_tools_path_config]] | sibling | 0.54 |
| [[bld_tools_runtime_rule]] | sibling | 0.54 |
| [[bld_tools_axiom]] | sibling | 0.54 |
