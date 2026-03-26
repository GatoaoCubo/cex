---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for input_schema production
---

# Tools: input-schema-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing input_schemas in pool | Phase 1 (check duplicates) | ACTIVE |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P06_schema/_schema.yaml | Field definitions for input_schema |
| CEX Examples | P06_schema/examples/ | Real input_schema artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P06_input_schema seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| JSON Schema spec | https://json-schema.org/ | Type/constraint patterns |
| Pydantic docs | https://docs.pydantic.dev/ | Coercion/default patterns |

## Interim Validation
No automated validator exists yet for input_schemas.
Manually check each QUALITY_GATES.md gate against produced artifact:
- [ ] YAML parses without error
- [ ] id matches p06_is_ prefix
- [ ] fields list is non-empty
- [ ] each field has name and type
- [ ] quality is null
- [ ] optional fields have defaults
