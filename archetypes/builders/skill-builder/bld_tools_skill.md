---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for skill production
---

# Tools: skill-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing skills in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, skill kind |
| CEX Examples | P04_tools/examples/ | Real skill artifacts |
| CODEXA Skills | records/skills/*/SKILL.md | 118 existing skills corpus |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_skill |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern matches, phases list equals
body subsections, no identity language in body, trigger is specific.
