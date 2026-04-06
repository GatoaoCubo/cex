---
kind: tools
id: bld_tools_trace_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for trace_config production
---

# Tools: trace-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing trace_config artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| cex_8f_runner.py | Read 8F pipeline stages to map span attributes | Phase 1 (understand pipeline) | AVAILABLE |
| cex_quality_monitor.py | Understand quality snapshots that consume trace data | Phase 1 (understand consumers) | AVAILABLE |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_testing/_schema.yaml | Field definitions, trace_config kind |
| CEX Examples | P07_testing/examples/ | Real trace_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P07_trace_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, testing layer |
| 8F Runner | _tools/cex_8f_runner.py | Pipeline stages with state.timings |
| SDK Tracing | cex_sdk/tracing/ | Tracing interface implementation |
| Quality Monitor | _tools/cex_quality_monitor.py | Quality snapshots from trace data |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, export_format enum valid,
sample_rate in range, capture_prompts/capture_responses are explicit booleans,
retention_days positive, body <= 4096 bytes, quality == null.
