---
pillar: P04
llm_function: CALL
purpose: Tools available for e2e_eval production
---

# Tools: e2e-eval-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing e2e_evals | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions for e2e_eval |
| CEX Examples | P07_evals/examples/ | Existing e2e_eval artifacts |
| Workflow definitions | P12_orchestration/ | Pipeline definitions to test |
| Builder QG files | archetypes/builders/*/QUALITY_GATES.md | Gate refs for assertions |
| SEED_BANK | archetypes/SEED_BANK.yaml | P07_e2e_eval seeds |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p07_e2e_ prefix
- [ ] stages is non-empty list with connected flow
- [ ] environment specified
- [ ] cleanup procedure defined
