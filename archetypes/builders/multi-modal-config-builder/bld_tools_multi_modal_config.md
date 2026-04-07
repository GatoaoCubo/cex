---
kind: tools
id: bld_tools_multi_modal_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for multi_modal_config production
---

# Tools: multi-modal-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile .md to .yaml | Phase 3 | ACTIVE |
| cex_retriever.py | Search existing configs | Phase 1 | ACTIVE |
| cex_token_budget.py | Estimate token costs per modality | Phase 2 | ACTIVE |
## Data Sources
| Source | Path | Data |
|--------|------|------|
| CEX Schema | P04_tools/_schema.yaml | Config field definitions |
| Kind KC | P01_knowledge/library/kind/kc_multi_modal_config.md | Deep knowledge |
| Model configs | .cex/config/nucleus_models.yaml | Model capabilities |
## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | — |
