---
kind: tools
id: bld_tools_workflow
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for workflow production
---

# Tools: workflow-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing workflows in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P12_orchestration/_schema.yaml | Field definitions, workflow kind |
| ADW files | records/pool/workflows/ADW_*.md | ~240 existing implicit workflows |
| Signal Builder | archetypes/builders/signal-builder/ | Signal conventions and schema |
| Spawn Config Builder | archetypes/builders/spawn-config-builder/ | Spawn parameter patterns |
| Satellite PRIMEs | records/satellites/*/PRIME_*.md | Satellite capabilities and routing |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P12_workflow |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, steps_count match,
body has all 4 required sections, signals reference signal conventions, no prompt chaining leaked.
