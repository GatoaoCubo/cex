---
kind: tools
id: bld_tools_knowledge_index
pillar: P04
llm_function: CALL
purpose: Tools available for knowledge_index production
---

# Tools: knowledge-index-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing knowledge_indexes | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions for knowledge_index |
| CEX Examples | P10_memory/examples/ | Existing knowledge_index artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P10_knowledge_index seeds |
| FAISS Docs | faiss.ai | Index types, parameters, performance characteristics |
| BM25 Theory | Robertson & Zaragoza 2009 | BM25 parameters and scoring |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p10_bi_ prefix
- [ ] algorithm in [bm25, faiss, hybrid]
- [ ] corpus_type in [text, vector, structured]
- [ ] rebuild_schedule valid enum
