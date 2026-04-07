---
id: p01_kc_skill_format_universal
kind: knowledge_card
pillar: P01
title: "Skill Format Universal — Frontmatter YAML + Markdown para Agentes LLM"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: knowledge_engineering
quality: 9.2
tags: [skill-format, plugin-system, agent-skills, frontmatter, composable-skills]
tldr: "Skills usam frontmatter YAML (name + description-trigger) + body Markdown com workflow, gates e integration — cross-platform"
when_to_use: "Criar ou avaliar skills para agentes LLM em qualquer plataforma"
keywords: [skill-format, frontmatter, trigger-condition, hard-gate, plugin-system]
long_tails:
  - "Como criar uma skill para Claude Code com frontmatter YAML"
  - "Qual o formato universal de skills para agentes LLM"
axioms:
  - "SEMPRE usar description como trigger condition, NUNCA como descricao generica"
  - "NUNCA criar skill monolitica sem sub-arquivos para tecnicas complexas"
linked_artifacts:
  primary: p01_kc_skill_references
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://agentskills.io"
---

## Summary

Skills para agentes LLM seguem formato universal: frontmatter YAML com `name` (kebab-case) e `description` (trigger condition) + body Markdown estruturado.
Funciona cross-platform: Claude Code, Codex, OpenCode, Cursor, Gemini.
O campo `description` eh o mecanismo de routing — o agente le este campo para decidir QUANDO invocar a skill automaticamente.

## Spec

| Campo | Obrigatorio | Formato | Regra |
|-------|-------------|---------|-------|
| `name` | SIM | kebab-case | Unico no namespace do plugin |
| `description` | SIM | Trigger condition | Condicao de quando invocar |
| `model` | NAO | string | `inherit` (padrao) ou modelo especifico |
| Arquivo | SIM | `SKILL.md` | Dentro de `skills/{nome}/` |
| Namespace | NAO | `plugin:skill-name` | Qualificado para registries |

Estrutura de diretorio padrao:

```
skills/{nome}/
  SKILL.md                    # Entry point com frontmatter
  {sub-arquivo}-prompt.md     # Prompts para sub-agentes
  {tecnica}.md                # Documentos de suporte
```

Comparacao entre frameworks:

| Aspecto | superpowers | agentskills.io |
|---------|-------------|----------------|
| Trigger | Campo `description` como condition | Campo `trigger` explicito |
| Namespace | `plugin:skill-name` | `namespace/skill` |
| Distribuicao | Plugin marketplace + git clone | Registry central |
| Cross-platform | Claude/Codex/Cursor/Gemini | Dependente da plataforma |

## Patterns

| Trigger | Action |
|---------|--------|
| Skill precisa invocacao automatica | Description como trigger condition especifica |
| Workflow critico nao pode pular etapas | Hard gate com `<HARD-GATE>` tag |
| Decisao complexa com branches | Flowchart `dot` como algoritmo |
| Skill usa ou eh usada por outras | Integration section com requires/called-by |
| Tecnica complexa com muitos detalhes | Sub-arquivos em pasta de suporte |

## Anti-Patterns

- Description vaga ("Skill for debugging") — agente nunca invoca
- Skill monolitica (>200 linhas) sem sub-arquivos de suporte
- Hard gates ausentes em workflows criticos (code antes de design)
- Sem Integration section — skill isolada no grafo de capacidades
- Exemplos ausentes — padrao fica abstrato e ambiguo

## Code

<!-- lang: markdown | purpose: skill com trigger e hard gate -->
```markdown
---
name: systematic-debugging
description: "Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes"
---

# Systematic Debugging

## The Process
1. Read error and stacktrace
2. Form hypothesis about root cause
3. Verify with minimal reproduction test
4. Fix only after confirmation

<HARD-GATE>
Do NOT write fixes until root cause is confirmed.
</HARD-GATE>

## Integration
- requires: code-review
- called-by: feature-development
```

## References

- source: https://agentskills.io
- source: https://docs.anthropic.com/en/docs/claude-code
- related: p01_kc_skill_references
- related: p01_kc_cex_function_become
