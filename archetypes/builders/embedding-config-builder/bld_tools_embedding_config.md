---
kind: tools
id: bld_tools_embedding_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for embedding_config production
---

# Tools: embedding-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing embedding_configs in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P01_knowledge/_schema.yaml | Field definitions for embedding_config |
| CEX Examples | P01_knowledge/examples/ | Real embedding_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P01_embedding_config seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| MTEB Leaderboard | huggingface.co/spaces/mteb/leaderboard | Model quality comparison |
| Ollama Library | ollama.com/library | Local model specs |
| OpenAI Embeddings | platform.openai.com/docs/guides/embeddings | API model specs |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet for embedding_configs.
Manually check each QUALITY_GATES.md gate against produced artifact:
- [ ] YAML parses without error
- [ ] id matches p01_emb_ prefix
- [ ] dimensions is positive integer
- [ ] chunk_size is positive integer
- [ ] quality is null
- [ ] model_name is specific identifier
