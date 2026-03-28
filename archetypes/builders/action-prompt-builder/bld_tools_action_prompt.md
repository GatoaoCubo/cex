---
kind: tools
id: bld_tools_action_prompt
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for action_prompt production
---

# Tools: action-prompt-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing action_prompts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P03_prompt/_schema.yaml | Field definitions, kinds |
| CEX Examples | P03_prompt/examples/ | Real action_prompt artifacts |
| HOP files | records/pool/*/task_prompt_*.md | 287 existing task prompts (action_prompt-like) |
| Handoff files | .claude/handoffs/*.md | 255 handoffs with task sections |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P03_action_prompt |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, action is verb phrase,
input_required is specific, edge_cases >= 2, no identity content, body has all 5 sections.
