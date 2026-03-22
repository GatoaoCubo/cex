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

## TIPOS ADICIONAIS

### lens
QUANDO USAR: Definir perspectiva especializada sobre dominio (ex: lens de seguranca, lens de UX).
Naming: `p02_lens_{{perspective}}.md + .yaml`
Schema: P02/_schema.yaml > types > lens

### boot_config
QUANDO USAR: Configurar inicializacao por provider (claude, cursor, codex, copilot).
Naming: `p02_boot_{{provider}}.md`
Schema: P02/_schema.yaml > types > boot_config

### mental_model
QUANDO USAR: Mapear routing e decisoes de um agente (decision tree, domain map).
Naming: `p02_mm_{{agent}}.yaml`
Schema: P02/_schema.yaml > types > mental_model

### model_card
QUANDO USAR: Documentar spec de LLM (pricing, context window, capabilities).
Naming: `p02_mc_{{model}}.md + .yaml`
Schema: P02/_schema.yaml > types > model_card

### router
QUANDO USAR: Definir regra de roteamento task > satellite com fallback.
Naming: `p02_rt_{{scope}}.yaml`
Schema: P02/_schema.yaml > types > router

### fallback_chain
QUANDO USAR: Configurar sequencia de fallback entre modelos (A > B > C).
Naming: `p02_fb_{{chain}}.yaml`
Schema: P02/_schema.yaml > types > fallback_chain

---
*Generator v1.0 | Evidence: 31 golden agents, 2216 agent docs | 2026-03-22*