---
kind: tools
id: bld_tools_agent_package
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for agent_package production
---

# Tools: agent-package-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing agent_packages to avoid duplicates | Phase 1 (discover) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
| iso_scaffold.py | Generate package directory skeleton by tier | Phase 2 (compose) | [PLANNED] |
| token_counter.py | Count tokens in system_instruction.md | Phase 3 (validate) | [PLANNED] |
| path_scanner.py | Scan files for hardcoded paths | Phase 3 (validate) | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P02_model/_schema.yaml | agent_package field definitions, tiers, lp_mapping |
| Agent Definitions | P02_model/examples/ | Source agent artifacts |
| framework Agents | records/agents/ | 118+ agents with iso_vectorstore to reference |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_agent_package |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position (spec), overlaps |
| agent-builder | archetypes/builders/agent-builder/ | Upstream: agent definition reference |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == agent_package, quality == null,
3 required files exist, files_count matches directory, system_instruction <= 4096 tokens,
no hardcoded paths, tier matches file count.
