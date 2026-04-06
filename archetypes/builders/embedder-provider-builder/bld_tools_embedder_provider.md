---
kind: tools
id: bld_tools_embedder_provider
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for embedder_provider production
---

# Tools: embedder-provider-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing embedder_provider configs in pool | Phase 1 (check duplicates) | CONDITIONAL |
| cex_retriever.py | TF-IDF search for similar embedding configs | Phase 1 (find references) | ACTIVE |
| validate_artifact.py | Validate any artifact kind via builder gates | Phase 3 | [PLANNED] |
| cex_compile.py | Compile .md to .yaml | Phase 4 (post-save) | ACTIVE |
## Data Sources (APIs and Docs)
| Source | URL | Data |
|--------|-----|------|
| OpenAI embeddings | https://platform.openai.com/docs/guides/embeddings | text-embedding-3 specs |
| OpenAI pricing | https://platform.openai.com/docs/pricing | Embedding pricing |
| Cohere embed | https://docs.cohere.com/docs/models#embed | embed-v3 specs |
| Cohere pricing | https://cohere.com/pricing | Embed pricing |
| Voyage AI | https://docs.voyageai.com/docs/embeddings | voyage-3 specs |
| Jina embeddings | https://jina.ai/embeddings/ | jina-embeddings-v3 specs |
| Nomic embed | https://docs.nomic.ai/atlas/models/text-embedding | nomic-embed specs |
| Sentence-transformers | https://www.sbert.net/docs/pretrained_models.html | Local model specs |
| MTEB leaderboard | https://huggingface.co/spaces/mteb/leaderboard | Benchmark scores |
| HuggingFace API | https://huggingface.co/api/models/{id} | Model metadata |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation (until validate_artifact.py exists)
Manually check each QUALITY_GATES gate against produced artifact.
All 10 HARD gates must pass. SOFT gates contribute to score.
## SDK References
| Provider | SDK | Install |
|----------|-----|---------|
| OpenAI | `openai` | `pip install openai` |
| Cohere | `cohere` | `pip install cohere` |
| Voyage | `voyageai` | `pip install voyageai` |
| Jina | `jina` | `pip install jina` |
| Local | `sentence-transformers` | `pip install sentence-transformers` |
