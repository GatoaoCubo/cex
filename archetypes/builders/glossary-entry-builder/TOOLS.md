---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for glossary_entry production
---

# Tools: glossary-entry-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing glossary entries in pool | Phase 1 (check duplicates) | ACTIVE |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P01_knowledge/_schema.yaml | Field definitions for glossary_entry |
| CEX Examples | P01_knowledge/examples/ | Real glossary_entry artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P01_glossary_entry seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Existing pool | pool/ (brain_query) | Existing term definitions |

## Interim Validation
No automated validator exists yet for glossary entries.
Manually check each QUALITY_GATES.md gate against produced artifact:
- [ ] YAML parses without error
- [ ] id matches p01_gl_ prefix
- [ ] definition is <= 3 lines
- [ ] synonyms list is non-empty
- [ ] quality is null
- [ ] term is non-empty string
