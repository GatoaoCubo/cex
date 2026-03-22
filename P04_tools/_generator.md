# Generator: P04 Skill

## QUANDO USAR
- Documentar habilidade reutilizavel
- Criar skill nova com workflow em fases
- Padronizar ferramenta existente

## PASSO A PASSO
1. SCOUT: verificar se skill similar ja existe
2. DEFINIR frontmatter completo (name, trigger, phases, examples)
3. ESCREVER workflow em fases numeradas (input > process > output)
4. INCLUIR metricas reais se disponiveis (speedup, utilization)
5. LISTAR anti-patterns com exemplos concretos
6. VALIDAR contra P04/_schema.yaml
7. SALVAR dual output (.md + .yaml)

## FRONTMATTER = SINGLE SOURCE OF TRUTH
O frontmatter YAML de cada SKILL.md eh a fonte para:
- Routing e descoberta (Brain MCP)
- Invocacao automatica (trigger field)
- Documentacao (description + examples)

## METRICAS (opcional mas valorizado)
Skills com metricas reais tem confianca 2x maior.
Campos: speedup, utilization, latency, error_rate
Fonte: testes reais, nao estimativas

## ANTI-PATTERNS
- Skill sem trigger (ninguem sabe como ativar)
- Skill sem examples (ninguem sabe o que esperar)
- Metricas inventadas (prefira ausencia a mentira)
- Fases sem input/output claro

---
*Generator v1.0 | Evidence: 58 golden skills, 124 total | 2026-03-22*