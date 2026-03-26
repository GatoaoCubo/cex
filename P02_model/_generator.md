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
Schema: P02/_schema.yaml > kinds > lens

### boot_config
QUANDO USAR: Configurar inicializacao por provider (claude, cursor, codex, copilot).
Naming: `p02_boot_{{provider}}.md`
Schema: P02/_schema.yaml > kinds > boot_config

### mental_model
QUANDO USAR: Mapear routing e decisoes de um agente (decision tree, domain map).
Naming: `p02_mm_{{agent}}.yaml`
Schema: P02/_schema.yaml > kinds > mental_model

### model_card
QUANDO USAR: Documentar spec de LLM (pricing, context window, capabilities).
Naming: `p02_mc_{{model}}.md + .yaml`
Schema: P02/_schema.yaml > kinds > model_card

### router
QUANDO USAR: Definir regra de roteamento task > satellite com fallback.
Naming: `p02_rt_{{scope}}.yaml`
Schema: P02/_schema.yaml > kinds > router

### fallback_chain
QUANDO USAR: Configurar sequencia de fallback entre modelos (A > B > C).
Naming: `p02_fb_{{chain}}.yaml`
Schema: P02/_schema.yaml > kinds > fallback_chain

### iso_package
QUANDO USAR: Empacotar agente completo como bundle portable (self-contained, LLM-agnostic).
Um ISO Package e a composicao de artefatos de ~8 LPs diferentes montados como um agente completo.

**Componentes** (cada um e um artifact de um Pillar diferente):
- MANIFEST (P02 agent) — identidade e capabilities
- SYSTEM_INSTRUCTION (P03 system_prompt) — como o agente fala
- INSTRUCTIONS (P03 user_prompt) — tarefas padrao
- DOMAIN_KNOWLEDGE (P01 knowledge_card) — o que sabe
- EXAMPLES (P03 few_shot) — exemplos de I/O
- TOOLS_AND_APIS (P04 skill) — ferramentas disponiveis
- OUTPUT_TEMPLATE (P05 output_schema) — formato de saida
- ERROR_HANDLING (P11 guardrail) — o que nunca fazer
- ARCHITECTURE (P08 component_map) — como se conecta
- TESTING (P07 smoke_eval) — como validar

**Tiers**: minimal (3 files) | standard (7) | complete (10) | whitelabel (12)
Naming: `agents/{{agent_name}}/manifest.yaml` (diretorio, nao arquivo unico)
Schema: P02/_schema.yaml > kinds > iso_package

## Dual Output

Cada artefato Model tem duas versoes:

| Versao | Formato | Leitor | Onde |
|--------|---------|--------|------|
| Humana | .md com frontmatter | Desenvolvedores, revisores | `examples/` e `templates/` |
| Machine | .yaml otimizado | LLMs, pipelines, validators | `compiled/` |

### Como compilar
```bash
python _tools/cex_compile.py P02_model/examples/p02_agent_exemplo.md
# -> gera P02_model/compiled/p02_agent_exemplo.yaml
```

### O que muda no compilado
- Remove: headers decorativos, bold/italic, links, navegacao
- Mantem: identidade, regras, dados estruturados, exemplos
- Formato: YAML (definido em _schema.yaml → machine_format)

---
*Generator v1.0 | Evidence: 31 golden agents, 2216 agent docs | 2026-03-22*