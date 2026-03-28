---
kind: tools
id: bld_tools_axiom
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for axiom production
---

# Tools: axiom-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing axioms in pool | Phase 1 (check duplicates) | CONDITIONAL [MCP] |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions for P10 kinds |
| CEX Taxonomy | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Seed Bank | archetypes/SEED_BANK.yaml | Seeds: rule, rationale, scope, enforcement |
| Existing axioms | P10_memory/examples/ | Reference artifacts |
| Builder Norms | archetypes/builders/BUILDER_NORMS.md | 12 mandatory rules |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate:
- [ ] YAML frontmatter parses without error
- [ ] id matches `p10_ax_` pattern
- [ ] kind == "axiom"
- [ ] quality == null
- [ ] rule is ONE atomic sentence
- [ ] scope names concrete domain boundary
- [ ] density >= 0.80 (no filler phrases)
