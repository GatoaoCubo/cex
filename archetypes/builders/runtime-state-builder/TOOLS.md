---
pillar: P04
llm_function: CALL
purpose: Tools available for runtime_state production
---

# Tools: runtime-state-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing runtime_states | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions for runtime_state |
| CEX Examples | P10_memory/examples/ | Existing runtime_state artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P10_mental_model seeds (runtime_state equivalent) |
| Agent PRIMEs | records/satellites/{name}/PRIME_{NAME}.md | Agent identity for state derivation |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p10_rs_ prefix
- [ ] persistence in [session, cross_session]
- [ ] routing_mode in [keyword, semantic, hybrid, rule_based]
- [ ] Decision Tree has branches
