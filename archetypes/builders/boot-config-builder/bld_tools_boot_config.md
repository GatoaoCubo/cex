---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for boot_config production
---

# Tools: boot-config-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing boot_configs to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P02_model/_schema.yaml | boot_config field definitions |
| Boot Examples | P02_model/examples/ | Existing boot_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_boot_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position (runtime), overlaps |
| Provider Docs | Per provider | Runtime limits, flags, tools |
| agent-builder | archetypes/builders/agent-builder/ | Agent identity reference |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == boot_config, quality == null,
identity object complete, constraints object complete, tools non-empty.
