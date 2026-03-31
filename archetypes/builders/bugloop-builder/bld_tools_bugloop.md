---
kind: tools
id: bld_tools_bugloop
pillar: P04
llm_function: CALL
purpose: Tools available for bugloop production
---

# Tools: bugloop-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing bugloops in P11_feedback/examples/ | Phase 1 (check duplicates, find patterns) | CONDITIONAL |
| brain_query [MCP] | Find validators (P06) that implement detect.pattern | Phase 1 (cross-ref detection logic) | CONDITIONAL |
| validate_artifact.py | Validate bugloop YAML against SCHEMA.md | Phase 3 | [PLANNED] |
| signal_writer.py | Reference pattern for fix confirmation signals | Design time | CONDITIONAL |
## Reference Artifacts (existing)
| Artifact | File | Domain |
|----------|------|--------|
| KC Pipeline Bugloop | P11_feedback/examples/p11_bl_kc_pipeline.md | KC validation failures |
| API Schema Bugloop | P11_feedback/examples/p11_bl_api_schema.md | API drift detection |
| Embedding Refresh Bugloop | P11_feedback/examples/p11_bl_embedding_refresh.md | Stale vector index |
## Tool Usage Notes
- brain_query is CONDITIONAL: only available when MCP server is running
- Without MCP: manually inspect P11_feedback/examples/ for existing bugloops
- validate_artifact.py is PLANNED: until available, use QUALITY_GATES.md checklist manually
- signal_writer.py: reference its interface when defining escalation.target="signal_bus"

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |
