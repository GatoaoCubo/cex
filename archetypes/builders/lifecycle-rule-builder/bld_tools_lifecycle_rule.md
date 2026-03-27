```yaml
---
pillar: P04
llm_function: CALL
purpose: Tools available for lifecycle_rule production
---
```

# Tools: lifecycle-rule-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing lifecycle_rules | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P11_feedback/_schema.yaml | Field definitions for lifecycle_rule |
| CEX Examples | P11_feedback/examples/ | Existing lifecycle_rule artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P11_lifecycle_rule seeds |
| TAXONOMY_LAYERS | archetypes/TAXONOMY_LAYERS.yaml | Position and overlap info |
| Quality Gates | archetypes/builders/quality-gate-builder/ | Reference for gate integration |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p11_lc_ prefix
- [ ] freshness_days is positive integer
- [ ] review_cycle in [weekly, monthly, quarterly, yearly]
- [ ] States table >= 3 states
- [ ] Transitions table >= 3 transitions
- [ ] All triggers are measurable
