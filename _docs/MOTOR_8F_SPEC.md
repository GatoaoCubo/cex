# MOTOR 8F — Spec Completa
**Status**: SPEC | **Version**: 1.0.0 | **Author**: knowledge_agent | **Created**: 2026-03-28
**Quality**: 9.2 | **Source**: LLM_PIPELINE.md + TAXONOMY_LAYERS.yaml + 71 builders

---

## O Que eh o Motor 8F

O Motor 8F eh o algoritmo que recebe um **intent** (string de linguagem natural)
e produz um **execution plan** estruturado: quais builders acionar, em que ordem,
com quais dependencias, para satisfazer as 8 funcoes do LLM pipeline.

```
intent string
     |
     v
  [MOTOR 8F]
     |
     +-- PARSE    (extrai verb, object, domain, quality)
     +-- CLASSIFY (mapeia object -> kinds CEX)
     +-- FAN-OUT  (funcoes -> builders necessarios)
     +-- PLAN     (ordena por dependencia)
     +-- OUTPUT   (JSON execution plan)
     |
     v
execution_plan.json
```

---

## 1. Decomposition Algorithm

### Step 1: PARSE

Extrair 4 campos do intent string:

| Campo | Descricao | Exemplo |
|-------|-----------|---------|
| `verb` | Acao principal (infinitivo) | cria, melhora, reconstroi, analisa |
| `object` | Artefato ou entidade alvo | agente, workflow, knowledge card |
| `domain` | Dominio de aplicacao | vendas, pesquisa, marketing |
| `quality_target` | Score esperado (default 9.0) | 9.0, 9.5 |

**Regras de parse:**
- Verb: primeiro verbo imperativo encontrado. Se ausente, inferir de contexto ("agente de vendas" -> "cria")
- Object: substantivo principal apos verb. Pode ser plural ou ter qualificadores
- Domain: entidade de negocio ou contexto tecnico apos "para", "de", "em"
- Quality: extrair de numeros decimais no intent. Default: 9.0

**Exemplos:**

```
"cria agente de vendas para ML"
  -> verb: "cria", object: "agente", domain: "vendas/ML", quality: 9.0

"melhora a qualidade do knowledge card de onboarding"
  -> verb: "melhora", object: "knowledge_card", domain: "onboarding", quality: 9.0

"reconstroi o knowledge-card-builder com score 9.5"
  -> verb: "reconstroi", object: "knowledge-card-builder", domain: "meta", quality: 9.5

"cria agente E workflow de pesquisa"
  -> verb: "cria", object: ["agente", "workflow"], domain: "pesquisa", quality: 9.0
```

---

### Step 2: CLASSIFY

Mapear `object` para `kind(s)` CEX usando TAXONOMY_LAYERS.yaml:

| Object Keyword | Kind(s) Primario(s) | Pillar | Funcao |
|----------------|-------------------|--------|--------|
| agente, agent | agent | P02 | BECOME |
| sistema, agent_group | agent_card | P08 | BECOME |
| prompt, instrucao | system_prompt, instruction | P03 | BECOME/REASON |
| workflow, pipeline | workflow | P12 | COLLABORATE |
| conhecimento, knowledge | knowledge_card | P01 | INJECT |
| rag, fonte | rag_source | P01 | INJECT |
| skill, habilidade | skill | P04 | CALL |
| tool, ferramenta | cli_tool, mcp_server | P04 | CALL |
| avaliacao, eval, teste | unit_eval, e2e_eval | P07 | GOVERN |
| schema, contrato | input_schema, interface | P06 | CONSTRAIN |
| sinal, signal | signal | P12 | COLLABORATE |
| handoff | handoff | P12 | COLLABORATE |
| modelo, model | model_card | P02 | BECOME |
| regra, rule | law, runtime_rule | P08/P09 | CONSTRAIN |
| guardrail, restricao | guardrail | P11 | GOVERN |
| chain, cadeia | chain | P03 | REASON |
| router, roteamento | router | P02 | REASON |
| dag, grafo | dag | P12 | COLLABORATE |
| spawn, lancamento | spawn_config | P12 | COLLABORATE |
| iso, pacote | agent_package | P02 | BECOME |
| conector, api | connector, client | P04 | CALL |
| lens, perspectiva | lens | P02 | BECOME |
| memory, memoria | knowledge_index, session_state | P10 | INJECT |
| glossario | glossary_entry | P01 | INJECT |
| axioma | axiom | P10 | INJECT |

**Classificacao de verbs:**

| Verb | Builders Extras Acionados |
|------|--------------------------|
| cria | builders do kind primario |
| melhora | quality-gate-builder + builders do kind |
| reconstroi | _builder-builder + builders do kind |
| analisa | scoring-rubric-builder + unit-eval-builder |
| valida | validator-builder + quality-gate-builder |
| documenta | knowledge-card-builder + context-doc-builder |
| integra | connector-builder + interface-builder |

---

### Step 3: FAN-OUT

Para cada kind classificado, expandir para as 8 funcoes e selecionar builders:

**Regra de selecao por tier:**
- **ALWAYS** (primary): Builders sem os quais o artefato nao existe
- **IF_MENTIONED**: Builders ativados se intent menciona keywords especificas
- **OPTIONAL**: Builders que elevam qualidade mas nao sao obrigatorios

Ver Secao 2 para as Mapping Tables completas.

---

### Step 4: PLAN

Ordenar builders por dependencia:

```
Ordem obrigatoria de execucao:
1. CONSTRAIN primeiro (schemas definem o contrato)
2. BECOME segundo (identidade assume o schema)
3. INJECT terceiro (contexto popula o agente)
4. REASON quarto (logica de pensamento)
5. CALL quinto (tools disponiveis)
6. PRODUCE sexto (gera output)
7. GOVERN setimo (valida qualidade)
8. COLLABORATE ultimo (propaga resultado)

Paralelo permitido DENTRO de cada funcao.
Nunca paralelo ENTRE funcoes (a ordem das 8 eh sequencial).
```

**Regras de dependencia entre builders:**
- `validation-schema-builder` ANTES de `validator-builder` (schema antes da regra)
- `system-prompt-builder` DEPOIS de `agent-builder` (identidade antes da instrucao)
- `knowledge-card-builder` ANTES de `rag-source-builder` (conteudo antes da fonte)
- `quality-gate-builder` ANTES de `scoring-rubric-builder` (gate define o rubric)
- `signal-builder` DEPOIS de `workflow-builder` (sinal pressupoe workflow)
- `few-shot-example-builder` DEPOIS de `output-template` (exemplos seguem template)

---

### Step 5: OUTPUT

Gerar JSON execution plan (ver Schema completo na Secao 3).

---

## 2. Mapping Tables — Todos os 71 Builders

> Cada builder aparece em pelo menos 1 funcao. Builders multi-funcao aparecem
> no tier mais alto de cada funcao onde sao relevantes.

### BECOME — "Quem eu sou?"
*Configura identidade, persona, regras, modelo antes de tudo*
*Pillars: P02 (Model), P03 (Prompt)*

| Tier | Builders |
|------|---------|
| **primary** | agent-builder, system-prompt-builder, model-card-builder, boot-config-builder, agent-package-builder |
| **secondary** | mental-model-builder, router-builder, fallback-chain-builder, lens-builder, supervisor-builder* |
| **optional** | _builder-builder (meta-bootstrap apenas) |

> *supervisor-builder: manifest id=`agent-card-builder`, pillar=P08, domain=agent_card.
> Acionar quando intent menciona "agent_group" ou "sistema completo".

---

### INJECT — "O que eu sei?"
*Fornece contexto e conhecimento ao LLM antes do reasoning*
*Pillars: P01 (Knowledge), P10 (Memory)*

| Tier | Builders |
|------|---------|
| **primary** | knowledge-card-builder, rag-source-builder, context-doc-builder, few-shot-example-builder |
| **secondary** | glossary-entry-builder, embedding-config-builder, knowledge-index-builder, learning-record-builder, axiom-builder |
| **optional** | runtime-state-builder, session-state-builder, mental-model-builder (aspecto P10) |

---

### REASON — "Como penso?"
*Raciocina, planeja, decompoe antes de agir*
*Pillars: P03 (Prompt)*

| Tier | Builders |
|------|---------|
| **primary** | instruction-builder, chain-builder, prompt-template-builder |
| **secondary** | action-prompt-builder, router-builder, dag-builder |
| **optional** | supervisor-builder (planejamento de orquestracao) |

---

### CALL — "Que tools uso?"
*Invoca ferramentas, APIs, CLIs, MCPs*
*Pillars: P04 (Tools)*

| Tier | Builders |
|------|---------|
| **primary** | skill-builder, mcp-server-builder, cli-tool-builder, connector-builder, scraper-builder, client-builder |
| **secondary** | hook-builder, plugin-builder, daemon-builder |
| **optional** | *(nenhum)* |

---

### PRODUCE — "O que gero?"
*Produz output final — texto, codigo, dados estruturados*
*Pillars: P05 (Output)*

| Tier | Builders |
|------|---------|
| **primary** | response-format-builder, formatter-builder, parser-builder |
| **secondary** | naming-rule-builder, action-prompt-builder |
| **optional** | chain-builder (quando chain eh o output final) |

---

### CONSTRAIN — "Esta no formato certo?"
*Valida contra schemas, regras, contratos*
*Pillars: P06 (Schema), P08 (Architecture), P09 (Config)*

| Tier | Builders |
|------|---------|
| **primary** | validator-builder, input-schema-builder, interface-builder, validation-schema-builder, type-def-builder, validator-builder-codex |
| **secondary** | invariant-builder, pattern-builder, guardrail-builder, component-map-builder, diagram-builder |
| **optional** | env-config-builder, path-config-builder, feature-flag-builder, runtime-rule-builder, permission-builder |

---

### GOVERN — "Passou no quality gate?"
*Quality gates, evals, benchmarks, feedback loops*
*Pillars: P07 (Evals), P11 (Feedback)*

| Tier | Builders |
|------|---------|
| **primary** | quality-gate-builder, scoring-rubric-builder, golden-test-builder, unit-eval-builder, e2e-eval-builder |
| **secondary** | benchmark-builder, smoke-eval-builder, lifecycle-rule-builder, optimizer-builder, bugloop-builder |
| **optional** | guardrail-builder (safety boundary), permission-builder (access control) |

---

### COLLABORATE — "Quem recebe?"
*Sinaliza, delega, propaga para proximo agente*
*Pillars: P12 (Orchestration)*

| Tier | Builders |
|------|---------|
| **primary** | signal-builder, handoff-builder, workflow-builder, spawn-config-builder, dispatch-rule-builder |
| **secondary** | dag-builder, hook-builder |
| **optional** | supervisor-builder (orquestracao de alto nivel) |

---

### Cobertura: Validacao

| Funcao | Primary | Secondary | Optional | Total |
|--------|---------|-----------|----------|-------|
| BECOME | 5 | 5 | 1 | 11 |
| INJECT | 4 | 5 | 3 | 12 |
| REASON | 3 | 3 | 1 | 7 |
| CALL | 6 | 3 | 0 | 9 |
| PRODUCE | 3 | 2 | 1 | 6 |
| CONSTRAIN | 6 | 5 | 5 | 16 |
| GOVERN | 5 | 5 | 2 | 12 |
| COLLABORATE | 5 | 2 | 1 | 8 |

> Builders multi-funcao (aparecem em >1 funcao):
> - mental-model-builder: BECOME (P02) + INJECT (P10)
> - router-builder: BECOME (P02 identity) + REASON (routing logic)
> - action-prompt-builder: REASON (planejamento) + PRODUCE (saida)
> - chain-builder: REASON (sequencia logica) + PRODUCE (output final)
> - guardrail-builder: CONSTRAIN (validacao) + GOVERN (safety gate)
> - permission-builder: CONSTRAIN (P09) + GOVERN (P11)
> - dag-builder: REASON (dependency planning) + COLLABORATE (P12)
> - hook-builder: CALL (P04 event trigger) + COLLABORATE (P12 lifecycle)
> - supervisor-builder: BECOME (agent_group spec) + REASON (orchestration planning) + COLLABORATE

> **builders_unassigned: []** — todos os 71 builders estao mapeados.

---

## 3. Plan Format — JSON Schema

```json
{
  "$schema": "https://cex.dev/schemas/execution_plan/v1",
  "intent": "string — intent original sem alteracao",
  "parsed": {
    "verb": "string — acao principal extraida",
    "object": "string | string[] — artefato(s) alvo",
    "domain": "string — dominio de aplicacao",
    "quality": "number — score alvo (default: 9.0)",
    "multi_object": "boolean — true se object eh array"
  },
  "classified_kinds": [
    {
      "object": "string",
      "kind": "string — kind CEX do TAXONOMY_LAYERS.yaml",
      "pillar": "string — P01..P12",
      "primary_function": "string — BECOME|INJECT|REASON|CALL|PRODUCE|CONSTRAIN|GOVERN|COLLABORATE"
    }
  ],
  "functions": [
    {
      "name": "string — BECOME|INJECT|REASON|CALL|PRODUCE|CONSTRAIN|GOVERN|COLLABORATE",
      "position": "number — 1..8 (ordem do pipeline)",
      "builders": [
        {
          "id": "string — nome do builder (ex: agent-builder)",
          "tier": "string — primary|secondary|optional",
          "active": "boolean — true se deve ser acionado neste plan",
          "reason": "string — por que foi selecionado"
        }
      ],
      "deps": "string[] — nomes de funcoes que devem completar antes",
      "parallel": "boolean — true se builders desta funcao rodam em paralelo",
      "estimated_tokens": "number"
    }
  ],
  "total_builders": "number — builders com active:true",
  "estimated_tokens": "number — soma de estimated_tokens de todas as funcoes",
  "warnings": "string[] — edge cases detectados"
}
```

**Exemplo completo — "cria agente de vendas para ML":**

```json
{
  "intent": "cria agente de vendas para ML",
  "parsed": {
    "verb": "cria",
    "object": "agente",
    "domain": "vendas/ML",
    "quality": 9.0,
    "multi_object": false
  },
  "classified_kinds": [
    {
      "object": "agente",
      "kind": "agent",
      "pillar": "P02",
      "primary_function": "BECOME"
    }
  ],
  "functions": [
    {
      "name": "CONSTRAIN",
      "position": 1,
      "builders": [
        {"id": "input-schema-builder", "tier": "primary", "active": true, "reason": "define contrato de entrada do agente"},
        {"id": "interface-builder", "tier": "primary", "active": true, "reason": "define interface com outros sistemas"},
        {"id": "validator-builder", "tier": "primary", "active": true, "reason": "valida conformidade do agente"}
      ],
      "deps": [],
      "parallel": true,
      "estimated_tokens": 8000
    },
    {
      "name": "BECOME",
      "position": 2,
      "builders": [
        {"id": "agent-builder", "tier": "primary", "active": true, "reason": "constroi definicao do agente"},
        {"id": "system-prompt-builder", "tier": "primary", "active": true, "reason": "escreve identidade e regras"},
        {"id": "model-card-builder", "tier": "primary", "active": true, "reason": "seleciona modelo LLM adequado"},
        {"id": "agent-package-builder", "tier": "primary", "active": true, "reason": "empacota agente para deploy"},
        {"id": "boot-config-builder", "tier": "primary", "active": false, "reason": "nao mencionado no intent"},
        {"id": "mental-model-builder", "tier": "secondary", "active": true, "reason": "mapa de routing para agente de vendas"},
        {"id": "router-builder", "tier": "secondary", "active": false, "reason": "sem routing complexo mencionado"}
      ],
      "deps": ["CONSTRAIN"],
      "parallel": true,
      "estimated_tokens": 16000
    },
    {
      "name": "INJECT",
      "position": 3,
      "builders": [
        {"id": "knowledge-card-builder", "tier": "primary", "active": true, "reason": "conhecimento de vendas e ML"},
        {"id": "context-doc-builder", "tier": "primary", "active": true, "reason": "contexto do dominio de vendas"},
        {"id": "few-shot-example-builder", "tier": "primary", "active": true, "reason": "exemplos de interacao"},
        {"id": "rag-source-builder", "tier": "primary", "active": false, "reason": "sem fonte RAG externa mencionada"}
      ],
      "deps": ["BECOME"],
      "parallel": true,
      "estimated_tokens": 12000
    },
    {
      "name": "REASON",
      "position": 4,
      "builders": [
        {"id": "instruction-builder", "tier": "primary", "active": true, "reason": "instrucoes operacionais do agente"},
        {"id": "chain-builder", "tier": "primary", "active": false, "reason": "sem chain de prompts mencionada"},
        {"id": "prompt-template-builder", "tier": "primary", "active": true, "reason": "template de acao para vendas"}
      ],
      "deps": ["INJECT"],
      "parallel": true,
      "estimated_tokens": 6000
    },
    {
      "name": "CALL",
      "position": 5,
      "builders": [
        {"id": "skill-builder", "tier": "primary", "active": true, "reason": "skills de busca e CRM"},
        {"id": "mcp-server-builder", "tier": "primary", "active": false, "reason": "sem MCP especifico mencionado"},
        {"id": "connector-builder", "tier": "primary", "active": false, "reason": "sem integracao externa mencionada"}
      ],
      "deps": ["REASON"],
      "parallel": true,
      "estimated_tokens": 4000
    },
    {
      "name": "PRODUCE",
      "position": 6,
      "builders": [
        {"id": "response-format-builder", "tier": "primary", "active": true, "reason": "formato de resposta do agente"},
        {"id": "formatter-builder", "tier": "primary", "active": false, "reason": "sem formatacao especial mencionada"},
        {"id": "parser-builder", "tier": "primary", "active": false, "reason": "sem parsing de saida mencionado"}
      ],
      "deps": ["CALL"],
      "parallel": true,
      "estimated_tokens": 3000
    },
    {
      "name": "GOVERN",
      "position": 7,
      "builders": [
        {"id": "quality-gate-builder", "tier": "primary", "active": true, "reason": "gates obrigatorios para agente"},
        {"id": "scoring-rubric-builder", "tier": "primary", "active": true, "reason": "rubric para score 9.0+"},
        {"id": "unit-eval-builder", "tier": "primary", "active": true, "reason": "testes unitarios do agente"},
        {"id": "golden-test-builder", "tier": "primary", "active": true, "reason": "golden case de vendas"},
        {"id": "smoke-eval-builder", "tier": "secondary", "active": true, "reason": "sanidade rapida pre-deploy"}
      ],
      "deps": ["PRODUCE"],
      "parallel": true,
      "estimated_tokens": 8000
    },
    {
      "name": "COLLABORATE",
      "position": 8,
      "builders": [
        {"id": "signal-builder", "tier": "primary", "active": true, "reason": "signal de completion do agente"},
        {"id": "handoff-builder", "tier": "primary", "active": true, "reason": "handoff para proximo passo"},
        {"id": "dispatch-rule-builder", "tier": "primary", "active": false, "reason": "sem routing policy mencionada"},
        {"id": "workflow-builder", "tier": "primary", "active": false, "reason": "sem workflow multi-step mencionado"}
      ],
      "deps": ["GOVERN"],
      "parallel": true,
      "estimated_tokens": 4000
    }
  ],
  "total_builders": 16,
  "estimated_tokens": 61000,
  "warnings": []
}
```

---

## 4. Edge Cases

### 4.1 Intent com Multiplos Objects

**Trigger**: `object` eh array (ex: "cria agente E workflow de pesquisa")

**Algoritmo:**
1. Parse retorna `multi_object: true`, `object: ["agente", "workflow"]`
2. CLASSIFY roda para cada object independentemente
3. FAN-OUT faz UNION dos builders de todos os objects por funcao
4. Builders duplicados (mesmo builder em ambos os objects) sao deduplicados
5. `estimated_tokens` multiplicado por fator 1.6x (overhead de contexto compartilhado)

**Plan diferencial:**
- BECOME: agent-builder + system-prompt-builder + workflow-builder (P12, BECOME aspecto)
- COLLABORATE: workflow-builder (P12, primary) — ja ativo por workflow object
- Warning: `"multi_object: complexidade aumenta 60%. Considere splits em 2 plans."`

---

### 4.2 Intent sem Domain Claro

**Trigger**: `domain` eh vazio ou generico (ex: "melhora a qualidade")

**Algoritmo:**
1. Parse retorna `domain: "generic"` e `verb: "melhora"`
2. CLASSIFY nao consegue mapear object especifico — retorna kind `quality_gate`
3. FAN-OUT ativa predominantemente funcao GOVERN
4. Verb "melhora" aciona quality-gate-builder + scoring-rubric-builder sempre
5. Warning: `"domain nao identificado — plan focado em GOVERN. Especifique o artefato alvo."`

**Builders ativos (minimo):**
- GOVERN: quality-gate-builder (primary), scoring-rubric-builder (primary), benchmark-builder (secondary)
- CONSTRAIN: validator-builder (primary) — sempre ativo para validar output
- COLLABORATE: signal-builder (primary) — signal de completion

---

### 4.3 Intent Meta (Reconstroi o Builder)

**Trigger**: object eh um builder CEX (ex: "reconstroi o knowledge-card-builder")

**Algoritmo:**
1. Parse retorna `object: "knowledge-card-builder"`, `domain: "meta"`, `verb: "reconstroi"`
2. CLASSIFY mapeia para kind especial `type_builder` (meta-kind)
3. FAN-OUT ativa _builder-builder como primary em BECOME
4. Builders do tipo original (knowledge-card) ficam como secondary em INJECT
5. Warning: `"intent meta detectado — ativando _builder-builder. Pipeline de 13 files."`

**Builders ativos (meta-plan):**
- BECOME: _builder-builder (primary), agent-builder (secondary — para MANIFEST.md)
- INJECT: knowledge-card-builder (secondary — conteudo de referencia)
- CONSTRAIN: validator-builder (primary), input-schema-builder (primary)
- GOVERN: quality-gate-builder (primary), golden-test-builder (primary)
- COLLABORATE: signal-builder (primary)

**Nota**: Em intent meta, o OUTPUT nao eh um artefato do kind, mas 13 arquivos de builder.
`estimated_tokens` multiplica por 13x (um contexto por arquivo gerado).

---

## 5. Regras de Ativacao por Keyword

Palavras no intent que ativam builders secundarios/opcionais:

| Keyword no Intent | Builders Ativados |
|------------------|------------------|
| "com memoria", "lembra" | knowledge-index-builder, learning-record-builder |
| "com RAG", "base de conhecimento" | rag-source-builder, embedding-config-builder |
| "com fallback", "resiliente" | fallback-chain-builder, runtime-rule-builder |
| "para agent_group", "sistema completo" | supervisor-builder (agent-card), spawn-config-builder |
| "com scraping", "extrai dados" | scraper-builder, parser-builder |
| "com API", "integra com" | connector-builder, client-builder, interface-builder |
| "com CLI", "linha de comando" | cli-tool-builder |
| "com MCP" | mcp-server-builder |
| "com dag", "dependencias" | dag-builder |
| "com hooks", "pre/pos" | hook-builder |
| "com permissoes", "acesso" | permission-builder |
| "com feature flags" | feature-flag-builder |
| "com benchmark" | benchmark-builder |
| "com e2e" | e2e-eval-builder |
| "golden test", "caso de referencia" | golden-test-builder |
| "multilingue", "multilingual" | glossary-entry-builder |
| "com axiomas", "inviolavel" | axiom-builder, invariant-builder |
| "com lens", "perspectiva" | lens-builder |
| "com daemon", "background" | daemon-builder |
| "com plugin" | plugin-builder |
| "isola", "portavel" | agent-package-builder |
| "otimiza", "melhora continua" | optimizer-builder, bugloop-builder |
| "session", "estado efemero" | session-state-builder |
| "diagram", "arquitetura visual" | diagram-builder |
| "componentes", "mapa" | component-map-builder |
| "pattern, reutilizavel" | pattern-builder |

---

## 6. Estimativa de Tokens por Builder

| Builder Complexity | Builders | Tokens Estimados |
|-------------------|----------|-----------------|
| Simple | signal-builder, dispatch-rule-builder, env-config-builder, session-state-builder, naming-rule-builder | ~2,000 |
| Medium | knowledge-card-builder, quality-gate-builder, skill-builder, instruction-builder, hook-builder | ~4,000 |
| Complex | agent-builder, workflow-builder, model-card-builder, agent-package-builder, e2e-eval-builder | ~8,000 |
| Meta | _builder-builder (13 files) | ~40,000 |

Formula: `estimated_tokens = sum(active_builders * complexity_tokens) * 1.2 (overhead)`

---

*MOTOR_8F_SPEC.md — knowledge_agent Wave 6A | CEX v1.0.0 | 2026-03-28*
