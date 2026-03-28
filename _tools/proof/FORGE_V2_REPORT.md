# Forge v2 Builder-Aware: Proof Report

## Comparison Table

| Type | LP | v1 bytes | v2 bytes | Delta | Builder ISOs | Builder KB |
|------|-----|---------|---------|-------|-------------|-----------|
| rag_source | P01 | 2,021 | 41,521 | +1,955% | 13 | 38 |
| model_card | P02 | 2,214 | 43,098 | +1,847% | 13 | 40 |
| prompt_template | P03 | 3,972 | 44,856 | +1,029% | 13 | 43 |
| mcp_server | P04 | 3,003 | 42,083 | +1,301% | 13 | 38 |
| response_format | P05 | 992 | 41,013 | +4,034% | 13 | 39 |

**Average v1**: 2,440 bytes | **Average v2**: 42,514 bytes | **Average delta**: +1,642%

## Extra Sections in v2

Each v2 prompt gains these builder-injected sections (priority order):

1. **Builder Knowledge** - Domain facts, spec tables, patterns, anti-patterns
2. **Builder Instructions** - Step-by-step execution protocol
3. **Builder Quality Gates** - Validation checklist, hard/soft gates
4. **Builder Examples** - Input/output examples (truncated to 3KB)
5. **Builder Manifest** - Identity, version, capabilities
6. **Builder Schema** - Input/output JSON schema
7. **Builder Architecture** - Component relationships
8. **Builder System Prompt** - Role definition
9. **Builder Tools** - Available tooling
10. **Builder Config** - Configuration rules
11. **Builder Collaboration** - Inter-agent protocols
12. **Builder Memory** - Persistence patterns
13. **Builder Output Template** - Expected output format

## Conclusion

Builder ISOs dramatically improve prompt quality:

- **Specificity**: v1 prompts give generic schema rules. v2 prompts include domain-specific patterns, anti-patterns, and quality gates that an LLM can directly apply.
- **Examples**: v2 includes concrete input/output examples (capped at 3KB) that ground the LLM's output format.
- **Quality enforcement**: Builder quality gates (hard gates + soft gates) give the LLM explicit pass/fail criteria instead of vague "quality >= 7.0".
- **Domain knowledge**: The knowledge_card ISO contains atomic facts (spec tables, naming patterns, validation rules) that prevent common errors.

**Verdict**: Builder ISOs transform forge from a structural skeleton (schema + template) into a knowledge-dense prompt that leverages the 932 builder files already in the repo. The 40KB budget keeps prompts within a single LLM context window while prioritizing the highest-value ISOs.

## Notes

- `output_schema` type does not exist in P05; used `response_format` instead.
- `--builder-only` flag available for types where builder knowledge > template value.
- Backward-compatible: without `--builder`, output is identical to v1.
