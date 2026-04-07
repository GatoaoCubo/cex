---
id: p01_kc_agentskills_spec
kind: knowledge_card
pillar: P01
title: "AgentSkills.io — Open Standard for Reusable AI Agent Skills"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [agentskills, skill-format, agent-interop, markdown-skills, cross-platform]
tldr: "AgentSkills.io empacota conhecimento como SKILL.md reutilizavel por qualquer agente — Claude Code, Codex CLI, OpenCode"
when_to_use: "Projetar skills portaveis entre plataformas LLM ou entender o padrao SKILL.md"
keywords: [agentskills-io, skill-md, agent-skills, cross-platform-skills]
long_tails:
  - "Como criar skills reutilizaveis para agentes de IA"
  - "Qual o formato padrao de SKILL.md para agentes LLM"
axioms:
  - "SEMPRE separar interface (SKILL.md) de profundidade (references/)"
  - "NUNCA criar SKILL.md monolitico com toda a documentacao"
linked_artifacts:
  primary: null
  related: [p01_kc_brand_skill, p01_kc_csv_as_knowledge]
density_score: null
data_source: "https://github.com/kepano/obsidian-skills"
---

## TL;DR

Standard aberto que empacota conhecimento especializado como Markdown files consumiveis por qualquer agente de IA. Cada skill tem SKILL.md (interface leve) + references/ (profundidade on-demand). Discovery automatico via campo `description` no frontmatter.

## Conceito Central

AgentSkills.io resolve o problema de portabilidade de conhecimento entre agentes. Uma skill e um diretorio com arquivo SKILL.md contendo frontmatter YAML (name + description) e body Markdown com workflow e referencia. O campo `description` funciona como trigger rule — o agente le esse campo para decidir se ativa a skill. Cross-platform por design: Claude Code, Codex CLI e OpenCode consomem o mesmo formato sem adaptacao.

A separacao interface/profundidade e fundamental: SKILL.md carrega rapido (~1KB), enquanto references/ contem exemplos, schemas e docs completas que o agente carrega sob demanda. Isso otimiza uso de contexto — so carrega o que precisa.

## Arquitetura/Patterns

| Componente | Papel | Tamanho |
|------------|-------|---------|
| SKILL.md | Interface principal, trigger rule | Leve (~1KB) |
| references/EXAMPLES.md | Exemplos de uso concretos | On-demand |
| references/FUNCTIONS_REF.md | API e funcoes disponiveis | On-demand |
| references/*.md | Docs especializados por topico | On-demand |

Formato do frontmatter obrigatorio:

```yaml
---
name: skill-name        # kebab-case, identificador unico
description: "Use when..." # trigger rule para o agente
---
```

Instalacao por plataforma:
- Claude Code: plugin marketplace ou diretorio de comandos do projeto
- Codex CLI: copiar skills/ para `~/.codex/skills/`
- OpenCode: clonar repo completo em `~/.opencode/skills/`
- Universal: `npx skills add <repo-url>`

Discovery pattern: agente escaneia diretorios de skills, le `description` de cada SKILL.md, ativa quando contexto do request faz match com o trigger.

## Exemplos Praticos

| Skill | Trigger | Dominio |
|-------|---------|---------|
| obsidian-markdown | Arquivos .md, wikilinks, callouts | Obsidian editing |
| obsidian-bases | Arquivos .base, filtros, formulas | Database views |
| json-canvas | Arquivos .canvas, mind maps | Visual mapping |
| defuddle | Extrair markdown de URLs | Web content |

Exemplo de description eficaz:
```
"Create and edit Obsidian Bases (.base files)
with views, filters, formulas. Use when working
with .base files or database-like content."
```

O "Use when..." e a parte critica — sem ele, o agente nao sabe quando ativar.

## Anti-Patterns

- SKILL.md monolitico com toda documentacao embutida
- Campo description vago sem contexto de ativacao
- Copiar apenas skills/ sem estrutura do repo (OpenCode)
- Confundir com MCP tools — agentskills e file-based
- Skills sem references/ quando dominio e complexo
- Name com espacos ou camelCase (deve ser kebab-case)

## Referencias

- source: https://github.com/kepano/obsidian-skills
- related: p01_kc_brand_skill
- related: p01_kc_csv_as_knowledge
