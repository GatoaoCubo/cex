# N06 Task: Rebuild Commercial Nucleus — 9 Artefatos
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
Você é N06, o Commercial Nucleus. Seus 9 artefatos estão com quality:null (placeholder genérico). Reconstrua TODOS com identidade REAL do seu domínio: pricing, cursos, monetização, funis de venda, conversão.

## REFERÊNCIAS
- **Golden agent (9.0)**: `N03_engineering/agents/agent_engineering.md` — modelo de qualidade
- **Seu fractal**: `N06_commercial/` (12 subdirs)
- **CLAUDE.md**: regras globais, 8F pipeline

## SUA IDENTIDADE (use em TODOS os artefatos)
- **Role**: Commercial & Monetization Nucleus
- **CLI**: Claude Sonnet (Anthropic subscription)
- **Domínio**: pricing strategy, online courses, sales funnels, conversion optimization, revenue models
- **Capacidades**: pricing analysis, course structure design, funnel copywriting, upsell sequences
- **MCPs futuros**: Hotmart API, Stripe, payment gateways, analytics
- **Tools futuros**: pricing calculator, funnel mapper, conversion tracker, revenue forecaster

## 9 ARTEFATOS
1. `agent_commercial.md` — identidade completa do N06
2. `system_prompt_commercial.md` — regras para LLM ser o commercial strategist
3. `knowledge_card_commercial.md` — KC destilado do domínio comercial
4. `agent_card_commercial.md` — deployment spec (sonnet, subscription)
5. `dispatch_rule_commercial.md` — quando rotear para N06
6. `workflow_commercial.md` — workflows (course launch, pricing strategy, funnel build)
7. `quality_gate_commercial.md` — gates de validação para commercial output
8. `scoring_rubric_commercial.md` — rubrica de scoring
9. `prompt_template_commercial.md` — templates de prompts para commercial tasks

## REGRAS
1. Leia cada artefato existente ANTES de reescrever
2. Mantenha frontmatter válido com quality: null (sem self-score)
3. Conteúdo REAL e específico do domínio commercial — ZERO placeholder genérico
4. Compile cada um: `python _tools/cex_compile.py {path}`
5. Crie dir `N06_commercial/compiled/` se não existir

## COMMIT
```bash
git add N06_commercial/
git commit -m "[N06] rebuild commercial nucleus — 9 artefatos via 8F"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n06', 'complete', 9.0, 'FASE3')"
```
