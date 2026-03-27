---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for instruction production
---

# Tools: instruction-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing instructions in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P03_prompt/_schema.yaml | Field definitions, kinds |
| CEX Examples | P03_prompt/examples/ | Real instruction artifacts |
| ISO Instructions | records/agents/*/iso_vectorstore/ISO_*_INSTRUCTIONS.md | 213 existing instructions |
| Handoff files | .claude/handoffs/*.md | 255 operational handoffs (instruction-like) |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P03_instruction |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, steps_count match,
one action per step, prerequisites are verifiable, no identity/persona content.
