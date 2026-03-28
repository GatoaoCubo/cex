---
kind: tools
id: bld_tools_computer_use
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for computer_use production
---

# Tools: computer-use-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing computer_use artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, computer_use kind |
| CEX Examples | P04_tools/examples/ | Real computer_use artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_computer_use |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| Anthropic Docs | docs.anthropic.com/en/docs/agents-and-tools/computer-use | Provider reference |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, resolution WxH format,
body <= 2048 bytes, quality == null, actions_supported listed.
