---
kind: tools
id: bld_tools_golden_test
pillar: P04
llm_function: CALL
purpose: Tools available for golden_test production
---

# Tools: golden-test-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing golden_tests | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions for golden_test |
| CEX Examples | P07_evals/examples/ | Existing golden_test artifacts |
| Builder QG files | archetypes/builders/*/QUALITY_GATES.md | Gate refs for rationale mapping |
| Pool artifacts | pool/ | Candidate golden artifacts (9.5+) |
| SEED_BANK | archetypes/SEED_BANK.yaml | P07_golden_test seeds |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p07_gt_ prefix
- [ ] quality_threshold >= 9.5
- [ ] golden_output is complete (no abbreviation)
- [ ] rationale references gate IDs
