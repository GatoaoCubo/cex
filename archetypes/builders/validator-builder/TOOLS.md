---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for validator production
---

# Tools: validator-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing validators in pool | Phase 1 (check duplicates) | ACTIVE |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P06_schema/_schema.yaml | Field definitions for validator |
| CEX Examples | P06_schema/examples/ | Real validator artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P06_validator seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Existing validators | pool/ (brain_query) | Patterns to follow |
| JSON Schema spec | https://json-schema.org/ | Operator/condition patterns |

## Interim Validation
No automated validator exists yet for validators.
Manually check each QUALITY_GATES.md gate against produced artifact:
- [ ] YAML parses without error
- [ ] id matches p06_val_ prefix
- [ ] severity is one of: error, warning, info
- [ ] conditions list is non-empty
- [ ] quality is null
- [ ] error_message is actionable (tells HOW to fix)
