---
kind: tools
id: bld_tools_response_format
pillar: P04
llm_function: CALL
purpose: Tools available for response_format production
---

# Tools: response-format-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing response_formats | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P05_output/_schema.yaml | Field definitions for response_format |
| CEX Examples | P05_output/examples/ | Existing format artifacts |
| Target schemas | {lp_dir}/_schema.yaml | Output requirements of target kinds |
| SEED_BANK | archetypes/SEED_BANK.yaml | P05_output_schema seeds |
| OpenAI docs | https://platform.openai.com/docs | Structured output patterns |
| Anthropic docs | https://docs.anthropic.com | Tool use output patterns |
## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p05_rf_ prefix
- [ ] sections_count >= 1
- [ ] format_type in valid enum
- [ ] injection_point in valid enum
- [ ] Example Output section present
