---
kind: tools
id: bld_tools_runtime_rule
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for runtime_rule production
---

# Tools: runtime-rule-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing runtime_rule artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, runtime_rule kind |
| CEX Examples | P09_config/examples/ | Real runtime_rule artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P09 types |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| Release It! patterns | Nygard (2007, 2018) | Stability patterns reference |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, rule_type enum, all values
have units, no vague terms, body <= 3072 bytes, quality == null.
