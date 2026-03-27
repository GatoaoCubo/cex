---
pillar: P04
llm_function: CALL
purpose: Tools available for validation_schema production
---

# Tools: validation-schema-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing validation_schemas | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P06_schema/_schema.yaml | Field definitions for validation_schema |
| CEX Examples | P06_schema/examples/ | Existing schema artifacts |
| Target schemas | {lp_dir}/_schema.yaml | Field definitions of target kinds |
| SEED_BANK | archetypes/SEED_BANK.yaml | P06_output_schema seeds |
| validate_kc.py | _tools/validate_kc.py | Reference implementation of KC validation |
| JSON Schema spec | https://json-schema.org | Industry standard reference |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p06_vs_ prefix
- [ ] fields_count >= 1
- [ ] on_failure in [reject, warn, auto_fix]
- [ ] format in [json, yaml]
- [ ] target_kind non-empty
