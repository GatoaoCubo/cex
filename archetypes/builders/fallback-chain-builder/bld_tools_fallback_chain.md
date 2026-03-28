---
kind: tools
id: bld_tools_fallback_chain
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for fallback_chain production
---

# Tools: fallback-chain-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing fallback_chains to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | SCHEMA.md (this builder) | Field definitions, step object |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_fallback_chain |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Model Cards | P02_model/examples/p02_mc_*.md | Model specs, pricing, capabilities |
| LiteLLM | docs.litellm.ai/docs/set_keys | Provider model identifiers |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == fallback_chain, quality == null,
steps_count matches chain rows, steps ordered by decreasing capability, timeout > 0.
