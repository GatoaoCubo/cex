---
kind: tools
id: bld_tools_feature_flag
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for feature_flag production
---

# Tools: feature-flag-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing feature_flag artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, feature_flag kind |
| CEX Examples | P09_config/examples/ | Real feature_flag artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P09 types |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, default_state enum, rollout
integer 0-100, category enum, body <= 1536 bytes, quality == null.
