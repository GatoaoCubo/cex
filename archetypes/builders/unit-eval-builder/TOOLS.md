---
pillar: P04
llm_function: CALL
purpose: Tools available for unit_eval production
---

# Tools: unit-eval-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing unit_evals | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions for unit_eval |
| CEX Examples | P07_evals/examples/ | Existing unit_eval artifacts |
| Builder QG files | archetypes/builders/*/QUALITY_GATES.md | Gate refs for assertions |
| Target builders | archetypes/builders/{target}/ | Target schema and gates |
| SEED_BANK | archetypes/SEED_BANK.yaml | P07_unit_eval seeds |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p07_ue_ prefix
- [ ] assertions is non-empty list
- [ ] each assertion has gate_ref
- [ ] timeout is positive integer
