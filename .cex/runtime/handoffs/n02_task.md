# N02 Task — PSPEC Visual Frontend Engineer: Rewrite Identity + Quality
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
N02 evolui de copywriter para **Visual Frontend Engineer** (dual-role: copy + HTML/CSS).
Leia a spec completa: `_docs/pspecs/PSPEC_N02_VISUAL_FRONTEND_ENGINEER.md`

## 20 KCs JÁ CRIADOS EM
`P01_knowledge/library/frontend/` — 10 KCs novos (tailwind, shadcn, a11y, typography, color, responsive, animation, email, visual-hierarchy, component-lib)

## TAREFA — Rewrite 14 artefatos existentes em N02_marketing/

### Identidade (rewrite com dual-role visual + copy):
1. `agents/agent_marketing.md` — Visual Frontend Engineer + Copywriter, 12 capabilities do F2
2. `prompts/system_prompt_marketing.md` — Persona dual, Tailwind/shadcn/Radix fluent
3. `architecture/agent_card_marketing.md` — Deploy spec com browser MCP, sonnet+opus
4. `prompts/prompt_template_marketing.md` — Templates para HTML gen + copy gen
5. `prompts/action_prompt_marketing.md` — Action prompts para landing pages, components

### Quality (rewrite com 9 gates visuais):
6. `feedback/quality_gate_marketing.md` — Lighthouse 90+, WCAG AA, contrast 4.5:1, responsive, F/Z-pattern, semantic HTML, font pairing, 0 hardcoded hex
7. `quality/scoring_rubric_marketing.md` — 5D scoring com dimensões visuais

### Orchestration (rewrite com dispatch visual):
8. `orchestration/dispatch_rule_marketing.md` — Triggers: html/frontend/landing/visual/design/tailwind/component/css + copy/ad
9. `orchestration/workflow_marketing.md` — Workflow: intent→select-mode(copy|visual)→build→validate→compile

### Knowledge (link novos KCs):
10. `knowledge/knowledge_card_marketing.md` — Rewrite com referências aos 10 frontend KCs

### CREATE novos:
11. `schemas/html_output_schema.md` — Schema para output HTML (frontmatter + HTML body)
12. `schemas/design_token_contract.md` — Schema para design tokens (3-layer)
13. `output/landing_page_template.md` — Output template para landing pages
14. `output/component_template.md` — Output template para components

## REFERÊNCIAS
- PSPEC: `_docs/pspecs/PSPEC_N02_VISUAL_FRONTEND_ENGINEER.md`
- Golden agent: `N03_engineering/agents/agent_engineering.md`
- KCs: `P01_knowledge/library/frontend/kc_*.md`

## COMMIT
```bash
git add -A && git commit -m "[N02] pspec: Visual Frontend Engineer — 14 artifacts rewritten"
```

## SIGNAL
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n02', 'pspec_n02_complete', 9.0)"
```
