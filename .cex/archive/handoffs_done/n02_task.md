# N02 Task: Rebuild Marketing Nucleus — 10 Artefatos
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
Você é N02, o Marketing Nucleus. Seus 10 artefatos estão com quality:null (placeholder genérico). Reconstrua TODOS com identidade REAL do seu domínio: copywriting, campanhas, branding, anúncios, social media.

## REFERÊNCIAS
- **Golden agent (9.0)**: `N03_engineering/agents/agent_engineering.md` — modelo de qualidade
- **Seu fractal**: `N02_marketing/` (12 subdirs)
- **CLAUDE.md**: regras globais, 8F pipeline

## SUA IDENTIDADE (use em TODOS os artefatos)
- **Role**: Marketing & Creative Nucleus
- **CLI**: Claude Sonnet (Anthropic subscription)
- **Domínio**: copywriting, ads, campaigns, brand voice, social media, CTAs, landing pages
- **Capacidades**: persuasive writing, A/B copy variants, headline optimization, funnel copy
- **MCPs futuros**: markitdown, fetch (web scraping), social APIs
- **Tools futuros**: headline scorer, readability analyzer, sentiment checker

## 10 ARTEFATOS
1. `agent_marketing.md` — identidade completa do N02
2. `system_prompt_marketing.md` — regras para LLM ser o copywriter
3. `knowledge_card_marketing.md` — KC destilado do domínio marketing
4. `agent_card_marketing.md` — deployment spec (sonnet, subscription)
5. `dispatch_rule_marketing.md` — quando rotear para N02
6. `workflow_marketing.md` — workflows (ad campaign, landing page, email sequence)
7. `quality_gate_marketing.md` — gates de validação para copy
8. `scoring_rubric_marketing.md` — rubrica de scoring para marketing artifacts
9. `prompt_template_marketing.md` — templates de prompts para marketing tasks
10. `action_prompt_marketing.md` — action prompts para execução rápida

## REGRAS
1. Leia cada artefato existente ANTES de reescrever
2. Mantenha frontmatter válido com quality: null (sem self-score)
3. Conteúdo REAL e específico do domínio marketing — ZERO placeholder genérico
4. Compile cada um: `python _tools/cex_compile.py {path}`
5. Crie dir `N02_marketing/compiled/` se não existir

## COMMIT
```bash
git add N02_marketing/
git commit -m "[N02] rebuild marketing nucleus — 10 artefatos via 8F"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n02', 'complete', 9.0, 'FASE3')"
```
