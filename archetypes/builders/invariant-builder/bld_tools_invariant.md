---
id: bld_tools_invariant
kind: tools_manifest
pillar: P08
parent: invariant-builder
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder_agent
tags: [tools, invariant-builder, data-sources, P08]
quality: 9.1
title: "Tools Invariant"
tldr: "Golden and anti-examples for invariant construction, demonstrating ideal structure and common pitfalls."
domain: "invariant construction"
density_score: 0.90
llm_function: CALL
related:
  - bld_tools_guardrail
  - bld_tools_pattern
  - bld_tools_validator
  - bld_tools_input_schema
  - bld_tools_diagram
  - bld_tools_axiom
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_learning_record
  - bld_tools_golden_test
---
# invariant-builder — TOOLS
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing laws and governance artifacts in pool | Phase 1: check for number collisions and prior art | CONDITIONAL [MCP] |
| validate_artifact.py | Generic artifact validator against SCHEMA.md | Phase 3: automated HARD gate checks | [PLANNED] |
| cex_forge.py | Generate artifact from seeds via template | Alternative compose path | [PLANNED] |
## Data Sources
| Source | Path / URL | Data provided |
|--------|-----------|---------------|
| CEX Schema | `cex/P08_architecture/_schema.yaml` | Field definitions, constraints, max_bytes for P08 kinds |
| CEX Taxonomy | `cex/archetypes/TAXONOMY_LAYERS.yaml` | Layer position, sibling kinds, overlap warnings |
| Seed Bank | `cex/archetypes/SEED_BANK.yaml` | Seeds: number, statement, rationale, enforcement, exceptions |
| Existing CEX laws | `records/framework/docs/LAWS_v3_PRACTICAL.md` | Current operational laws (Laws 1-11) for collision avoidance |
| Builder Norms | `cex/archetypes/builders/BUILDER_NORMS.md` | Mandatory authoring constraints for all builders |
| RFC 2119 | `https://www.rfc-editor.org/rfc/rfc2119` | MUST/SHALL/SHOULD/MAY requirement level definitions |
| Google SRE Book | SRE Book (O'Reilly), Chapter 4 | SLA/SLO governance patterns, enforcement models |
## brain_query Usage [IF MCP]
```
# Check for existing laws to avoid number collision
brain_query("P08 law governance existing numbers")
# Find related patterns that may justify a new law
brain_query("pattern [domain] proven solution")
# Find quality gates that enforce laws
brain_query("quality gate law enforcement compliance")
```
Mark as `CONDITIONAL` — brain_query requires Ollama running locally with nomic-embed-text model.
Fallback when MCP unavailable: grep `records/framework/docs/LAWS_v3_PRACTICAL.md` for existing numbers.
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation (No Automated Validator Yet)
Until `validate_artifact.py` is built:
1. Manually parse YAML frontmatter (copy to YAML linter)
2. Check each HARD gate against QUALITY_GATES.md checklist
3. Count SOFT gate passes and compute score
4. Self-review statement for imperative mood (MUST/SHALL/NEVER/ALWAYS)
5. Confirm number uniqueness in LAWS_v3_PRACTICAL.md

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_guardrail]] | upstream | 0.48 |
| [[bld_tools_pattern]] | upstream | 0.48 |
| [[bld_tools_validator]] | upstream | 0.46 |
| [[bld_tools_input_schema]] | upstream | 0.46 |
| [[bld_tools_diagram]] | related | 0.46 |
| [[bld_tools_axiom]] | upstream | 0.45 |
| [[bld_tools_retriever_config]] | upstream | 0.45 |
| [[bld_tools_memory_scope]] | upstream | 0.45 |
| [[bld_tools_learning_record]] | upstream | 0.45 |
| [[bld_tools_golden_test]] | upstream | 0.45 |
