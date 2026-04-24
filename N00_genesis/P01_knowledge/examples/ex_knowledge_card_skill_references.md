---
id: p01_kc_skill_references
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Skill References Pattern — Interface Leve + Profundidade On-Demand"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: knowledge_engineering
quality: 9.1
tags: [skill-references, token-efficiency, progressive-disclosure, information-architecture]
tldr: "SKILL.md leve (workflow + quick ref) + sub-arquivos profundos (tabelas, exemplos) otimiza tokens e mantem profundidade acessivel"
when_to_use: "Decidir como estruturar conteudo de skill entre interface leve e referencia profunda"
keywords: [skill-references, progressive-disclosure, token-efficiency, information-architecture]
long_tails:
  - "Como separar interface de skill de referencias profundas para otimizar tokens"
  - "Quando criar arquivos de referencia auxiliares para uma skill de agente"
axioms:
  - "SEMPRE manter SKILL.md abaixo de 200 linhas — profundidade vai para sub-arquivos"
  - "NUNCA duplicar conteudo entre SKILL.md e arquivos de referencia"
linked_artifacts:
  primary: p01_kc_skill_format_universal
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://github.com/kepano/obsidian-skills"
related:
  - p01_kc_agentskills_spec
  - p01_kc_skill_format_universal
  - bld_collaboration_skill
  - p01_kc_query_decomposition
  - bld_architecture_skill
  - bld_memory_skill
  - bld_knowledge_card_procedural_memory
  - procedural-memory-builder
  - bld_system_prompt_skill
  - skill-builder
---

## Summary

Pattern de dois niveis para skills de agentes LLM: SKILL.md como interface leve (carregada sempre) + sub-arquivos de referencia como profundidade on-demand.
Reduz custo de tokens em 60-80% mantendo acesso completo a detalhes quando necessario.
Originado no obsidian-skills (kepano), replicado em sistemas multi-agente com ISO vectorstore.

## Spec

| Camada | Conteudo | Carregamento | Tamanho Alvo |
|--------|----------|-------------|--------------|
| SKILL.md | Workflow, quick ref, links, exemplos simples | Sempre (contexto) | < 200 linhas |
| sub-arquivos | Tabelas completas, edge cases, exemplos extensos | On-demand | Sem limite fixo |

Criterios para criar sub-arquivo de referencia:

| Condicao | Acao |
|----------|------|
| SKILL.md passaria de 200 linhas | Extrair para sub-arquivo |
| Tabela com mais de 10 itens | Mover tabela completa |
| Exemplos completos e pesados | Manter sintese inline, completo em sub-arquivo |

SKILL.md faz links explicitos para sub-arquivos:
```markdown
See [CALLOUTS.md](sub-arquivo/CALLOUTS.md) for the full list.
```

## Patterns

| Trigger | Action |
|---------|--------|
| Skill com >200 linhas de conteudo total | Extrair tabelas e exemplos para sub-arquivos |
| Tabela de referencia com >10 entradas | Sub-arquivo dedicado com link do SKILL.md |
| Agente precisa de detalhes edge-case | Link explicito no SKILL.md aponta para detalhe |
| Multiplos exemplos completos | Inline tem sintese, sub-arquivo tem completo |
| Novo skill sendo criado em sistema multi-agente | Planejar SKILL.md + sub-arquivos desde o inicio |

## Anti-Patterns

- Skill monolitica sem sub-arquivos (contexto inflado, tokens desperdicados)
- Sub-arquivos sem links explicitos do SKILL.md (profundidade inacessivel)
- Duplicacao de conteudo entre SKILL.md e sub-arquivos (inconsistencia)
- Conteudo critico apenas em sub-arquivo (agente perde info essencial)
- Sub-arquivo com 1-2 linhas (overhead de arquivo sem beneficio real)

## Code

<!-- lang: text | purpose: exemplos reais do obsidian-skills -->
```
# obsidian-markdown/ (kepano/obsidian-skills)
SKILL.md                  # Workflow 6 steps, wikilinks, callouts basicos
  sub-arquivos/
    CALLOUTS.md           # 13 tipos + aliases, foldable, nested, custom CSS
    EMBEDS.md             # Audio, video, PDF, search embeds, external images
    PROPERTIES.md         # Todos os tipos de property, tag syntax rules

# obsidian-bases/
SKILL.md                  # Schema YAML, filter/formula syntax, view types
  sub-arquivos/
    FUNCTIONS_REFERENCE.md  # Funcoes por tipo: Date, String, Number, List

# json-canvas/
SKILL.md                  # Spec completa: nodes, edges, colors, layout
  sub-arquivos/
    EXAMPLES.md           # 4 exemplos JSON: mind map, project board, flowchart
```

```yaml
# Equivalente em sistema multi-agente:
agent_structure:
  interface: "README.md"           # Overview, quick ref
  depth:
    - "MANIFEST.md"                # Capabilities list
    - "INSTRUCTIONS.md"            # Execution protocol
    - "EXAMPLES.md"                # Input/output samples
    - "SCHEMA.md"                  # JSON schema
  principle: "interface leve + profundidade on-demand"
```

## References

- source: https://github.com/kepano/obsidian-skills
- source: https://docs.anthropic.com/en/docs/claude-code
- related: p01_kc_skill_format_universal
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_agentskills_spec]] | sibling | 0.43 |
| [[p01_kc_skill_format_universal]] | sibling | 0.40 |
| [[bld_collaboration_skill]] | downstream | 0.38 |
| [[p01_kc_query_decomposition]] | sibling | 0.33 |
| [[bld_architecture_skill]] | downstream | 0.33 |
| [[bld_memory_skill]] | downstream | 0.32 |
| [[bld_knowledge_card_procedural_memory]] | sibling | 0.30 |
| [[procedural-memory-builder]] | downstream | 0.30 |
| [[bld_system_prompt_skill]] | downstream | 0.30 |
| [[skill-builder]] | downstream | 0.28 |
