---
kind: tools
id: bld_tools_parser
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for parser production
---

# Tools: parser-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing parsers to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | SCHEMA.md (this builder) | Field definitions, rule object |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P05_parser |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Existing parsers | P05_output/examples/p05_parser_*.md | Real parser artifacts |
| Regex reference | pcre2pattern man page | PCRE2 syntax for regex method |
## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == parser, quality == null,
extraction_count matches rules, input/output formats valid, at least 1 required rule.
