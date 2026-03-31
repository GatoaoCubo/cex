---
kind: tools
id: bld_tools_output_validator
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for output_validator production
---

# Tools: output-validator-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing output_validator artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P05_output/_schema.yaml | Field definitions, output_validator kind |
| CEX Examples | P05_output/examples/ | Real output_validator artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P05_output_validator |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | Write, BashTool | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, required fields present,
body <= 2048 bytes, quality == null.
