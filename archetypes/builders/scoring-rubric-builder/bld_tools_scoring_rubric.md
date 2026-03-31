---
kind: tools
id: bld_tools_scoring_rubric
pillar: P04
llm_function: CALL
purpose: Tools available for scoring_rubric production
---

# Tools: scoring-rubric-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing scoring_rubrics | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions for scoring_rubric |
| CEX Examples | P07_evals/examples/ | Existing rubric artifacts |
| Builder QG files | archetypes/builders/*/QUALITY_GATES.md | Dimension candidates |
| Golden tests | P07_evals/examples/p07_gt_*.md | Calibration anchors |
| SEED_BANK | archetypes/SEED_BANK.yaml | P07_scoring_rubric seeds |
| validate_kc.py | _tools/validate_kc.py | 5D rubric reference implementation |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p07_sr_ prefix
- [ ] Dimension weights sum to exactly 100%
- [ ] All 4 tiers defined (GOLDEN/PUBLISH/REVIEW/REJECT)
- [ ] Criteria are concrete (no subjective language)
