---
kind: tools
id: bld_tools_handoff_protocol
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for handoff_protocol production
---

# Tools: handoff-protocol-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing handoff_protocol artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P02_model/_schema.yaml | Field definitions, handoff_protocol kind |
| CEX Examples | P02_model/examples/ | Real handoff_protocol artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_handoff_protocol |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, required fields present,
body <= 2048 bytes, quality == null.
