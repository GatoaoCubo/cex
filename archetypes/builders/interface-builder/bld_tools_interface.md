---
kind: tools
id: bld_tools_interface
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for interface production
---

# Tools: interface-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing interfaces in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P06_schema/_schema.yaml | Field definitions for interface |
| CEX Examples | P06_schema/examples/ | Real interface artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P06_interface seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| OpenAPI Spec | https://spec.openapis.org/oas/latest.html | Method/contract patterns |
## Interim Validation
No automated validator exists yet for interfaces.
Manually check each QUALITY_GATES.md gate against produced artifact:
- [ ] YAML parses without error
- [ ] id matches p06_iface_ prefix
- [ ] methods list is non-empty
- [ ] each method has name, input, output
- [ ] quality is null
- [ ] backward_compatible is boolean
