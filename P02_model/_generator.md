# Generator: P02 Agent

## QUANDO USAR
- Definir novo agente (persona + capabilities + routing)
- Documentar agente existente no formato CEX

## PASSO A PASSO
1. SCOUT: verificar se agent similar ja existe
2. DEFINIR identidade: nome, satellite, domain, role
3. DESENHAR architecture (ASCII diagram com INPUT > PROCESS > OUTPUT)
4. LISTAR capabilities (tabela: # | cap | descricao)
5. CRIAR tabela when_to_use (YES/NO com alternativas)
6. DEFINIR input/output schemas
7. MAPEAR integration: upstream + downstream agents
8. DEFINIR quality_gates (5D ou 12LP)
9. LISTAR common_issues (problemas reais, nao hipoteticos)
10. VALIDAR contra P02/_schema.yaml
11. SALVAR dual output (.md + .yaml)

## ISO VECTORSTORE (se agent maduro)
Minimo 10 arquivos. Criar na ordem:
1. MANIFEST (capabilities index)
2. QUICK_START (como usar em 5 min)
3. PRIME (identidade completa)
4. INSTRUCTIONS (passo-a-passo detalhado)
5. ARCHITECTURE (diagramas + fluxos)
6. OUTPUT_TEMPLATE (formato de saida)
7. EXAMPLES (3+ exemplos reais)
8. ERROR_HANDLING (erros comuns + solucoes)
9. UPLOAD_KIT (como instalar/configurar)
10. SYSTEM_INSTRUCTION (system prompt do agent)

## ANTI-PATTERNS
- Agent sem when_to_use (ninguem sabe quando chamar)
- Agent sem anti-patterns (parece que faz tudo)
- Output count vago ("varias saidas" vs "22 blocks")
- Chain patterns ausente (agent isolado)

## MATURITY TIERS
- 0-3 ISOs: prototipo (nao usar em producao)
- 10 ISOs: baseline completo
- 17+ ISOs: maduro com domain coverage
- 22+ ISOs: golden (whitelabel ready)

---
*Generator v1.0 | Evidence: 31 golden agents, 2216 agent docs | 2026-03-22*