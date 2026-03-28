---
kind: tools
id: bld_tools_hook
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for hook production
---

# Tools: hook-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing hooks to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | SCHEMA.md (this builder) | Field definitions, condition object |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_hook |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Claude Code hooks | .claude/settings.json hooks section | Real hook configurations |
| Hook lifecycle docs | Claude Code documentation | Event types and payloads |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == hook, quality == null,
trigger_event valid enum, timeout in range, script_path present.
