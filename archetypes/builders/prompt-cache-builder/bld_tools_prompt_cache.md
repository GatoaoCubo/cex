---
kind: tools
id: bld_tools_prompt_cache
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for prompt_cache production
---

# Tools: prompt-cache-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile .md to .yaml | Phase 3 | ACTIVE |
| cex_retriever.py | Search existing cache configs | Phase 1 | ACTIVE |
## Data Sources
| Source | Path | Data |
|--------|------|------|
| CEX Schema | P10_memory/_schema.yaml | Cache config field definitions |
| Kind KC | P01_knowledge/library/kind/kc_prompt_cache.md | Deep knowledge |
| Provider docs | External | Anthropic/OpenAI caching specifics |
## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | — |
