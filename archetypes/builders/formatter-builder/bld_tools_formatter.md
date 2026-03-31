---
kind: tools
id: bld_tools_formatter
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for formatter production
---

# Tools: formatter-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing formatters to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | SCHEMA.md (this builder) | Field definitions, rule object |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P05_formatter |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Existing formatters | P05_output/examples/p05_fmt_*.md | Real formatter artifacts |
| Mustache spec | mustache.github.io | Template syntax reference |
| Jinja2 docs | jinja.palletsprojects.com | Template syntax reference |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == formatter, quality == null,
rule_count matches rules, target_format/input_type valid, at least 1 formatting rule.
