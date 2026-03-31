# N04 Task: Rebuild Knowledge Nucleus — 12 Artefatos
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
Você é N04, o Knowledge Nucleus. Seus 12 artefatos estão com quality:null (placeholder genérico). Reconstrua TODOS com identidade REAL do seu domínio: knowledge management, RAG, indexação, embeddings, taxonomia, documentation.

## REFERÊNCIAS
- **Golden agent (9.0)**: `N03_engineering/agents/agent_engineering.md` — modelo de qualidade
- **Seu fractal**: `N04_knowledge/` (12 subdirs)
- **CLAUDE.md**: regras globais, 8F pipeline

## SUA IDENTIDADE (use em TODOS os artefatos)
- **Role**: Knowledge Management Nucleus
- **CLI**: Gemini 2.5-pro (1M context, Google subscription)
- **Domínio**: RAG pipelines, knowledge cards, embeddings, chunking, retrieval, taxonomy, documentation
- **Capacidades**: large-context ingestion, semantic indexing, knowledge graph construction, deduplication
- **MCPs futuros**: vector DB, document loaders, embedding APIs
- **Tools futuros**: chunk optimizer, semantic search, knowledge graph builder, consolidate

## 12 ARTEFATOS
1. `agent_knowledge.md` — identidade completa do N04
2. `system_prompt_knowledge.md` — regras para LLM ser o knowledge manager
3. `knowledge_card_knowledge.md` — KC destilado do domínio knowledge
4. `agent_card_knowledge.md` — deployment spec (gemini, 1M ctx)
5. `dispatch_rule_knowledge.md` — quando rotear para N04
6. `workflow_knowledge.md` — workflows (KC authoring, RAG indexing, taxonomy build)
7. `quality_gate_knowledge.md` — gates de validação para knowledge artifacts
8. `scoring_rubric_knowledge.md` — rubrica de scoring
9. `chunk_strategy_knowledge.md` — estratégias de chunking para RAG
10. `embedding_config_knowledge.md` — config de embeddings
11. `rag_source_knowledge.md` — fontes e retrieval config
12. `retriever_config_knowledge.md` — config do retriever

## REGRAS
1. Leia cada artefato existente ANTES de reescrever
2. Mantenha frontmatter válido com quality: null (sem self-score)
3. Conteúdo REAL e específico do domínio knowledge — ZERO placeholder genérico
4. Compile cada um: `python _tools/cex_compile.py {path}`
5. Crie dir `N04_knowledge/compiled/` se não existir

## COMMIT
```bash
git add N04_knowledge/
git commit -m "[N04] rebuild knowledge nucleus — 12 artefatos via 8F"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'complete', 9.0, 'FASE3')"
```
