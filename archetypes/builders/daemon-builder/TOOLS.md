---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for daemon production
---

# Tools: daemon-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing daemon artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, daemon kind |
| CEX Examples | P04_tools/examples/ | Real daemon artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_daemon |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| systemd docs | freedesktop.org/software/systemd | Unit file conventions |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, schedule is concrete,
body <= 1024 bytes, quality == null, signal_handling includes SIGTERM.
