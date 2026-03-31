---
kind: tools
id: bld_tools_mental_model
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for mental_model (P02) production
---

# Tools: mental-model-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing mental_models to avoid duplicates | Phase 1 (analyze) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P02_model/_schema.yaml | mental_model field definitions |
| MM Examples | P02_model/examples/ | Existing mental_model artifacts |
| framework MMs | records/agent_nodes/*/mental_model.yaml | 7 agent_node mental models |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_mental_model |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | P02/P10 overlap, layer position |
| agent-builder | archetypes/builders/agent-builder/ | Agent identity reference |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == mental_model, pillar == P02 (not P10),
quality == null, routing_rules >= 3, decision_tree >= 2, keywords are specific.
