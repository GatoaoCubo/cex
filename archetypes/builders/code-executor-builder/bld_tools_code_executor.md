---
kind: tools
id: bld_tools_code_executor
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for code_executor production
---

# Tools: code-executor-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing code_executor artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, code_executor kind |
| CEX Examples | P04_tools/examples/ | Real code_executor artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_code_executor |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| Docker Docs | docs.docker.com/engine/security | Container isolation reference |
| E2B Docs | e2b.dev/docs | Cloud sandbox reference |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, sandbox_type defined,
body <= 2048 bytes, quality == null, timeout > 0, languages listed.
