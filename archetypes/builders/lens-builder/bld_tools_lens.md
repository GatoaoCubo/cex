---
kind: tools
id: bld_tools_lens
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for lens production
---

# Tools: lens-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing lenses in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P02_model/_schema.yaml | Field definitions for lens |
| CEX Examples | P02_model/examples/ | Real lens artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P02_lens seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Existing pool | pool/ (brain_query) | Existing lenses |
## Interim Validation
No automated validator exists yet for lenses.
Manually check each QUALITY_GATES.md gate against produced artifact:
- [ ] YAML parses without error
- [ ] id matches p02_lens_ prefix
- [ ] perspective is non-empty
- [ ] applies_to is list with >= 1 entry
- [ ] quality is null
- [ ] All 4 body sections present
