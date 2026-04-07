---
kind: tools
id: bld_tools_context_window_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for context_window_config production
---

# Tools: context-window-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_token_budget.py | Token counting + budget allocation | Phase 1-2 | ACTIVE |
| cex_compile.py | Compile .md to .yaml | Phase 3 | ACTIVE |
| cex_retriever.py | Search existing configs | Phase 1 | ACTIVE |
## cex_token_budget.py Usage
```bash
python _tools/cex_token_budget.py --model claude-opus --sections system,context,examples,query,output
```
## Data Sources
| Source | Path | Data |
|--------|------|------|
| CEX Schema | P03_prompt/_schema.yaml | Config field definitions |
| Kind KC | P01_knowledge/library/kind/kc_context_window_config.md | Deep knowledge |
| Model configs | .cex/config/nucleus_models.yaml | Model limits |
## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | — |
