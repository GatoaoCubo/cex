---
kind: tools
id: bld_tools_constraint_spec
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for constraint_spec production
---

# Tools: constraint-spec-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing constraint_spec artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P03_prompt/_schema.yaml | Field definitions, constraint_spec kind |
| CEX Examples | P03_prompt/examples/ | Real constraint_spec artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P03_constraint_spec |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, required fields present,
body <= 2048 bytes, quality == null.
