---
kind: tools
id: bld_tools_function_def
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for function_def production
---

# Tools: function-def-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing function_def artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
| jsonschema_validate | Validate parameters against JSON Schema draft-07 | Phase 3 | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, function_def kind |
| CEX Examples | P04_tools/examples/ | Real function_def artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_function_def |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| OpenAI Docs | platform.openai.com/docs/guides/function-calling | Provider reference |
| Anthropic Docs | docs.anthropic.com/en/docs/build-with-claude/tool-use | Provider reference |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, parameters is valid JSON Schema,
body <= 2048 bytes, quality == null, returns defined.
