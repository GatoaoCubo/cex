---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for client production
---

# Tools: client-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing client artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, client kind |
| CEX Examples | P04_tools/examples/ | Real client artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_client |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| API Docs | Target API documentation | Endpoints, auth, rate limits |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, endpoints list matches body,
body <= 1024 bytes, quality == null, base_url present.
