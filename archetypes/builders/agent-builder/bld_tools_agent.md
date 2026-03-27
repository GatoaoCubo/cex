---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for agent production
---

# Tools: agent-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing agents to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
| iso_scaffold.py | Generate iso_vectorstore skeleton (10 files) | Phase 2 (compose) | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P02_model/_schema.yaml | Field definitions, kinds, constraints |
| Agent Examples | P02_model/examples/ | Real agent artifacts |
| CODEXA Agents | records/agents/ | 118+ agents with complete iso_vectorstore |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_agent |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps, boundary |
| system-prompt-builder | archetypes/builders/system-prompt-builder/ | Upstream dependency reference |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == agent, quality == null,
iso_vectorstore lists >= 10 files, capabilities_count matches body, llm_function == BECOME.
