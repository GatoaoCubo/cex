---
kind: tools
id: bld_tools_pattern
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for pattern production
---

# Tools: pattern-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing patterns in pool | Phase 1 (check duplicates) | CONDITIONAL [MCP] |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P08_architecture/_schema.yaml | Field definitions for P08 kinds |
| CEX Taxonomy | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Seed Bank | archetypes/SEED_BANK.yaml | Seeds: name, problem, solution, forces |
| Existing patterns | P08_architecture/examples/ | Reference artifacts |
| GoF Patterns | Design Patterns (Gamma et al. 1994) | Classical pattern catalog |
| POSA Patterns | Pattern-Oriented Software Architecture | Distributed system patterns |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate:
- [ ] YAML frontmatter parses without error
- [ ] id matches `p08_pat_` pattern
- [ ] kind == "pattern"
- [ ] quality == null
- [ ] name is 2-5 words
- [ ] problem describes RECURRING situation
- [ ] consequences include at least 1 cost
- [ ] density >= 0.80 (no filler)
