---
kind: tools
id: bld_tools_citation
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for citation production
---

# Tools: citation-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile .md to .yaml | Phase 3 | ACTIVE |
| cex_retriever.py | Search existing citations | Phase 1 | ACTIVE |
| brain_query [MCP] | Search knowledge pool | Phase 1 | CONDITIONAL |
## Data Sources
| Source | Path | Data |
|--------|------|------|
| CEX Schema | P01_knowledge/_schema.yaml | Citation field definitions |
| Kind KC | P01_knowledge/library/kind/kc_citation.md | Deep knowledge about citation |
## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |
