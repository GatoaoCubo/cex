---
kind: tools
id: bld_tools_memory_summary
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for memory_summary production
---

# Tools: memory-summary-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing memory_summary artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
| token_counter.py | Count tokens in source content to calibrate compression ratio | Phase 1 (research) | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions, memory_summary kind |
| CEX Examples | P10_memory/examples/ | Real memory_summary artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P10_memory_summary |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| LangChain docs | https://python.langchain.com/docs/modules/memory/ | ConversationSummaryMemory patterns |
| Zep docs | https://docs.getzep.com/concepts/memory | Server-side summarization API |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern `^p10_ms_`, source_type enum valid,
compression_method enum valid, body <= 2048 bytes, quality == null, all 4 sections present.
## Compression Ratio Estimation
| Source size | abstractive | extractive | hybrid | sliding_window |
|-------------|-------------|------------|--------|----------------|
| < 500 tokens | 2:1 | 1.5:1 | 2:1 | N/A |
| 500-2000 tokens | 5:1 | 3:1 | 4:1 | 3:1 rolling |
| 2000-8000 tokens | 10:1 | 5:1 | 8:1 | 5:1 rolling |
| > 8000 tokens | 15:1 | 8:1 | 12:1 | 8:1 rolling |
Use these as starting estimates. Adjust based on content density and retention requirements.
