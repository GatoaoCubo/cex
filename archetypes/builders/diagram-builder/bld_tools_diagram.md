---
pillar: P00
id: bld_tools_diagram
kind: tools
builder: diagram-builder
version: 1.0.0
quality: 9.1
title: "Tools Diagram"
author: n03_builder
tags: [diagram, builder, examples]
tldr: "Golden and anti-examples for diagram construction, demonstrating ideal structure and common pitfalls."
domain: "diagram construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CALL
related:
  - bld_tools_input_schema
  - bld_tools_pattern
  - bld_tools_validator
  - bld_tools_memory_scope
  - bld_tools_axiom
  - bld_tools_retriever_config
  - bld_tools_workflow
  - bld_tools_component_map
  - bld_tools_cli_tool
  - bld_tools_validation_schema
---
# diagram-builder — TOOLS
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing diagrams in pool | Phase 1 Step 5 | CONDITIONAL [MCP] |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## brain_query Usage
```
brain_query("diagram {scope_keywords}")
brain_query("p08_diag {domain}")
brain_query("architecture visualization {component_name}")
```
Condition: only execute if Brain MCP is active. Skip gracefully if unavailable.
Purpose: detect existing diagrams before creating duplicates.
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P08_architecture/_schema.yaml | Field definitions, constraints |
| CEX Taxonomy | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Seed Bank | archetypes/SEED_BANK.yaml | Seeds: scope, notation, components |
| Builder Norms | archetypes/builders/BUILDER_NORMS.md | Quality standards |
| Mermaid docs | https://mermaid.js.org/syntax/ | Mermaid syntax reference |
| C4 Model | https://c4model.com/ | Zoom level framework |
## No External API Required
diagram-builder is self-contained. All required knowledge is in:
- SCHEMA.md (field rules)
- QUALITY_GATES.md (validation)
- KNOWLEDGE.md (patterns and boundaries)
- OUTPUT_TEMPLATE.md (structure)
brain_query is enhancement only — builder functions without it.

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_input_schema]] | sibling | 0.54 |
| [[bld_tools_pattern]] | sibling | 0.53 |
| [[bld_tools_validator]] | sibling | 0.53 |
| [[bld_tools_memory_scope]] | sibling | 0.52 |
| [[bld_tools_axiom]] | sibling | 0.52 |
| [[bld_tools_retriever_config]] | sibling | 0.52 |
| [[bld_tools_workflow]] | sibling | 0.52 |
| [[bld_tools_component_map]] | sibling | 0.51 |
| [[bld_tools_cli_tool]] | sibling | 0.51 |
| [[bld_tools_validation_schema]] | sibling | 0.50 |
