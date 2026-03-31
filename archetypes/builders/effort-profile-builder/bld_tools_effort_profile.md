---
kind: tools
id: bld_tools_effort_profile
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for effort_profile production
---

# Tools: effort-profile-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing effort_profile artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, effort_profile kind |
| CEX Examples | P09_config/examples/ | Real effort_profile artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P09_effort_profile |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, config layer |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, required fields present,
body <= 4096 bytes, quality == null.
