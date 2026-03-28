---
kind: tools
id: bld_tools_permission
pillar: P04
llm_function: CALL
purpose: Tools available for permission production
---

# Tools: permission-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing permissions | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions for permission |
| CEX Examples | P09_config/examples/ | Existing permission artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P09_permission seeds |
| RBAC Patterns | NIST RBAC standard | Role hierarchy best practices |
## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p09_perm_ prefix
- [ ] read/write/execute in [allow, deny, conditional]
- [ ] roles is non-empty list
- [ ] Access Matrix present with roles
