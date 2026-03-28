---
kind: tools
id: bld_tools_connector
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for connector production
---

# Tools: connector-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing connector artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, connector kind |
| CEX Examples | P04_tools/examples/ | Real connector artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_connector |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| Service Docs | Target service documentation | Endpoints, auth, webhooks |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, endpoints list matches body,
body <= 1024 bytes, quality == null, each endpoint has direction annotation.
