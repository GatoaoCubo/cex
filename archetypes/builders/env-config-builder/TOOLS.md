---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for env_config production
---

# Tools: env-config-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing env_config artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, env_config kind |
| CEX Examples | P09_config/examples/ | Real env_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P09_env_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| .env files | Project .env, .env.example | Existing variable definitions |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, variables list matches catalog,
body <= 4096 bytes, quality == null, no actual secret values in artifact.
