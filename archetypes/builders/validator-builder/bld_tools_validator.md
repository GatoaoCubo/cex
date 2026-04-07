---
kind: tools
id: bld_tools_validator
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for validator production
quality: 9.1
title: "Tools Validator"
version: "1.0.0"
author: n03_builder
tags: [validator, builder, examples]
tldr: "Golden and anti-examples for validator construction, demonstrating ideal structure and common pitfalls."
domain: "validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Tools: validator-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing validators in pool | Phase 1 (check duplicates) | CONDITIONAL |
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
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet for validators.
Manually check each QUALITY_GATES.md gate against produced artifact:
1. [ ] YAML parses without error
2. [ ] id matches p06_val_ prefix
3. [ ] severity is one of: error, warning, info
4. [ ] conditions list is non-empty
5. [ ] quality is null
6. [ ] error_message is actionable (tells HOW to fix)

## Metadata

```yaml
id: bld_tools_validator
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-validator.md
```
