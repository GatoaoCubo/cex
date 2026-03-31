---
kind: tools
id: bld_tools_prompt_version
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for prompt_version production
---

# Tools: prompt-version-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing prompt_version artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P03_prompt/_schema.yaml | Field definitions, prompt_version kind |
| CEX Examples | P03_prompt/examples/ | Real prompt_version artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P03_prompt_version |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, required fields present,
body <= 2048 bytes, quality == null.
