# N01 Task: Rebuild Intelligence Nucleus — 11 Artefatos
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
Você é N01, o Research Nucleus. Seus 11 artefatos estão com quality:null (placeholder genérico). Reconstrua TODOS com identidade REAL do seu domínio: research, análise de mercado, papers, competidores. Gemini 2.5-pro com 1M context.

## REFERÊNCIAS
- **Golden agent (9.0)**: `N03_engineering/agents/agent_engineering.md` — modelo de qualidade
- **Schema P02 (agent)**: `P02_model/_schema.yaml`
- **Seu fractal**: `N01_intelligence/` (12 subdirs)
- **CLAUDE.md**: regras globais, 8F pipeline

## SUA IDENTIDADE (use em TODOS os artefatos)
- **Role**: Research & Intelligence Nucleus
- **CLI**: Gemini 2.5-pro (1M context, Google subscription)
- **Domínio**: research, market analysis, competitor intelligence, papers, benchmarks
- **Capacidades**: deep research, large document analysis, RAG over papers, trend detection
- **MCPs futuros**: Google Scholar, arxiv, web search, markitdown
- **Tools futuros**: semantic search, citation graph, summarizer

## 11 ARTEFATOS
1. `agent_intelligence.md` — identidade completa do N01
2. `system_prompt_intelligence.md` — regras para LLM ser o researcher
3. `knowledge_card_intelligence.md` — KC destilado do domínio research
4. `agent_card_intelligence.md` — deployment spec (gemini, 1M ctx)
5. `dispatch_rule_intelligence.md` — quando rotear para N01
6. `workflow_intelligence.md` — workflows de research (solo analysis, comparative study, literature review)
7. `quality_gate_intelligence.md` — gates de validação para research output
8. `scoring_rubric_intelligence.md` — rubrica de scoring para research artifacts
9. `prompt_template_intelligence.md` — templates de prompts para research tasks
10. `embedding_config_intelligence.md` — config de embeddings para RAG
11. `rag_source_intelligence.md` — fontes de RAG e retrieval config

## REGRAS
1. Leia cada artefato existente ANTES de reescrever
2. Mantenha frontmatter válido com quality: null (sem self-score)
3. Conteúdo REAL e específico do domínio research — ZERO placeholder genérico
4. Compile cada um: `python _tools/cex_compile.py {path}`
5. Crie dir `N01_intelligence/compiled/` se não existir

## COMMIT
```bash
git add N01_intelligence/
git commit -m "[N01] rebuild intelligence nucleus — 11 artefatos via 8F"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n01', 'complete', 9.0, 'FASE3')"
```
