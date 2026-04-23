---
id: kc_pillar_brief_p06_schema_pt
kind: knowledge_card
pillar: P06
title: "P06 Schema — O Esqueleto da IA: Contratos Que Sustentam Tudo"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
quality: 7.1
language: pt-br
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p06, schema, input-schema, validation, contracts, type-safety, json-schema, llm-engineering]
tldr: "P06 Schema cobre os 8 kinds que definem contratos de dados para sistemas de IA — schemas de entrada, validators, interfaces, definições de tipo — a camada estrutural que previne dados inválidos de se propagar pelo seu pipeline."
source_concepts: [kc_lens_index, mentor_context, p03_pc_cex_universal]
related:
  - kc_pillar_brief_p06_schema_en
  - kc_pillar_brief_p05_output_pt
  - kc_pillar_brief_p07_evals_pt
  - kc_pillar_brief_p08_architecture_pt
  - n00_p06_kind_index
density_score: 1.0
updated: "2026-04-22"
---

# P06 Schema — O Esqueleto: Contratos Que Sustentam Tudo

## O Princípio Universal: Sistemas de IA Quebram nas Fronteiras

Aqui está a verdade estrutural sobre pipelines de IA: cada componente que chama outro componente é um ponto de falha potencial. Um LLM chamando uma ferramenta, uma ferramenta retornando dados a um agente, um agente passando contexto a um modelo downstream, um passo de pipeline escrevendo em um banco de dados — cada uma dessas transições é uma fronteira onde dados podem chegar malformados, incompletos ou do tipo errado.

Sem contratos explícitos nessas fronteiras, você está construindo sobre areia. Componentes que funcionam individualmente falham quando integrados. Bugs se manifestam tarde, longe da sua origem, tornando-os caros para diagnosticar. Sistemas se tornam frágeis a qualquer mudança no formato de output upstream.

P06 Schema é o pilar que endurece essas fronteiras. Ele fornece artefatos tipados para definir o que entra (input schemas), o que sai (validation schemas), quais tipos de dados existem no sistema (definições de tipo e enums), como os componentes se comunicam (interfaces), quais constraints sempre devem se manter (validators) e como APIs externas são documentadas (referências de API).

Essa disciplina antecede os LLMs. É a mesma lição aprendida por designers de API REST nos anos 2010, times de microsserviços nos anos 2010 e engenheiros de banco de dados antes disso: contratos explícitos nas fronteiras do sistema são o que torna sistemas complexos manuteníveis. LLMs adicionam uma nova camada — a fronteira de contrato agora inclui o próprio input e output do LLM, não apenas o código ao redor. Mas o princípio é idêntico.

Esse framework é universal. JSON Schema, Pydantic, Zod, interfaces TypeScript, specs OpenAPI — todas são implementações do mesmo princípio. Os kinds de P06 dão a você uma forma de raciocinar sobre qual tipo de contrato você precisa, independentemente da tecnologia de implementação.

### Por Que Schemas Importam Mais com LLMs do que Sem

Contratos de software tradicional são estáticos: você os define uma vez, eles não mudam a menos que você os mude explicitamente. Contratos adjacentes a LLMs têm um novo desafio: o output do LLM é probabilístico. Mesmo com uma instrução de response format perfeita (P05), há sempre alguma probabilidade de o LLM se desviar.

Isso torna a validação de input mais importante, não menos. Quando você não pode confiar plenamente que o output upstream vai conformar com a estrutura esperada, você precisa de contratos robustos em cada camada:

- Input para o LLM (o que o sistema envia ao modelo)
- Output do LLM (o que o modelo retorna ao sistema)
- Input para ferramentas (o que o LLM diz às suas ferramentas para fazer)
- Output de ferramentas (que resultados de ferramentas são retornados ao LLM)
- Comunicação agente-a-agente (o que um agente diz ao outro)

Cinco fronteiras de schema em uma única chamada de agente LLM. Cada uma delas pode propagar dados ruins se não tiver contrato.

---

## Todos os 8 Kinds em P06 — O Arsenal Completo de Schema

| Kind | Propósito | Camada | Função |
|------|-----------|--------|--------|
| `input_schema` | Contrato de dados para o que um componente aceita | Spec | CONSTRAIN |
| `validation_schema` | Contrato pós-geração aplicado pelo sistema | Spec | GOVERN |
| `validator` | Regra de validação pass/fail reutilizável | Governance | GOVERN |
| `interface` | Contrato de integração bilateral entre agentes | Spec | CONSTRAIN |
| `type_def` | Definição de tipo customizado no sistema | Spec | GOVERN |
| `enum_def` | Enumeração finita de valores válidos | Runtime | CONSTRAIN |
| `api_reference` | Documentação de API com endpoints, params, auth | Spec | INJECT |
| `edit_format` | Especificação de formato de mudança de arquivo LLM-para-host | Spec | GOVERN |

P06 tem 8 kinds — o menor pilar na taxonomia de 12 pilares. Isso é intencional: kinds de schema são fundamentais, não numerosos. Um sistema com 300 knowledge cards ainda só precisa desses 8 tipos de contratos. O que escala é o número de instâncias, não o número de kinds.

---

## Padrões Chave de Engenharia — Universais, Qualquer IA

### Padrão 1: O Firewall de Input Schema

Todo agente, ferramenta ou passo de pipeline deve ter um input schema explícito que valida dados de entrada antes de o processamento começar. Este é o padrão de firewall: dados inválidos são rejeitados na fronteira, não propagados para o core.

A estrutura canônica de um input schema:

```yaml
# input_schema.yaml
id: is_pipeline_de_pesquisa_input
kind: input_schema
target_component: research_pipeline
schema_format: pydantic
strict_mode: true
fields:
  - name: query
    type: str
    required: true
    constraints: {min_length: 3, max_length: 500}
  - name: max_fontes
    type: int
    required: false
    default: 10
    constraints: {min: 1, max: 50}
  - name: dominios_incluir
    type: list[str]
    required: false
    default: []
  - name: idioma
    type: IdiomaEnum
    required: false
    default: pt-br
example:
  query: "técnicas de context window para LLMs 2025"
  max_fontes: 15
  idioma: pt-br
```

Esse schema faz várias coisas: documenta os inputs aceitos (para que chamadores saibam o que fornecer), valida em runtime (para que inputs ruins falhem barulhentamente), habilita geração de SDK (ferramentas como FastAPI, Pydantic e OpenAPI podem gerar código de cliente diretamente daqui) e serve como documentação viva que está sempre atualizada com a implementação.

Na prática:
- Python: `pydantic.BaseModel` ou `dataclasses`
- TypeScript: `zod.z.object({...})` ou declarações `interface`
- API: schema `requestBody` do OpenAPI
- Ferramentas LangChain: campo `args_schema` em `BaseTool`
- Function calling: JSON Schema em definições de tool

**Experimente agora:** Escolha qualquer função no seu codebase que processa input de LLM ou output de tool. Escreva um modelo Pydantic (Python) ou schema Zod (TypeScript) para seus inputs. Adicione validação na entrada da função. Execute seus testes existentes — qualquer um que estava passando com dados malformados vai agora corretamente falhar.

### Padrão 2: Contratos Pré vs. Pós Geração

Esta é a distinção conceitual mais importante em P06. Existem dois tipos de contratos de output:

**Pré-geração (response_format, P05)**: o LLM VÊ isso. Ele molda o que o modelo produz. É uma instrução em nível de prompt: "formate sua resposta como JSON com esses campos."

**Pós-geração (validation_schema, P06)**: o SISTEMA APLICA isso. O LLM não vê. É um contrato técnico aplicado ao output bruto depois que o LLM terminou de gerar.

Por que você precisa dos dois?

Porque o response format diz ao LLM o que fazer, mas não garante conformidade. Um LLM sob temperatura alta, ou que foi promovido com uma tarefa complexa, pode se desviar das instruções de formato. O validation schema captura esse desvio antes que ele se propague.

```
Pedido do usuário -> prompt (com response_format) -> LLM gera -> output bruto
                                                                      |
                                                  validation_schema.validate(output_bruto)
                                                                      |
                                                             PASS: entrega output
                                                             FAIL: retry ou raise error
```

Essa abordagem de duas camadas é o padrão da indústria em sistemas LLM de produção. O modo "structured outputs" da OpenAI usa validação JSON Schema no backend. O uso de tools da Anthropic valida schemas de tool call. Você deve replicar isso no nível de aplicação para qualquer schema que importa.

**Experimente agora:** Veja um lugar no seu código onde você usa o output do LLM diretamente sem validação. Escreva um JSON Schema (ou modelo Pydantic) para a estrutura de output esperada. Valide a resposta do LLM contra ele antes de usar. Trate o erro de validação explicitamente.

### Padrão 3: O Padrão de Composição de Validators

Validators são atômicos: cada um testa uma única assertion. Validation schemas e output validators são compostos: eles referenciam múltiplos validators e definem como falhas se agregam.

O poder dessa separação é a reutilização. Um validator que verifica "frontmatter tem campos obrigatórios" pode ser referenciado por 50 validation schemas diferentes que se aplicam a diferentes kinds de artefatos. Mude o validator uma vez, todos os 50 schemas se beneficiam.

```yaml
# validator: verificação atômica
id: validator_qualidade_no_intervalo
check_type: business_rule
assertion: "quality é null OU quality entre 0.0 e 10.0"
severity: error
error_message: "quality deve ser null (não revisado) ou float em [0, 10]. Recebido: {value}"
applies_to: [knowledge_card, agent, prompt_template, workflow]

# validation_schema: compõe validators
id: vs_knowledge_card_padrao
validators:
  - validator_tem_frontmatter
  - validator_qualidade_no_intervalo
  - validator_kind_no_registro
  - validator_pilar_valido
  - validator_sem_secoes_vazias
on_fail: raise_first_error
```

Esse padrão é universal em bibliotecas de validação:
- Pydantic: decoradores `@validator` compõem em validação de modelo
- Zod: callbacks `.refine()` compõem em validação de schema
- JSON Schema: padrões `allOf` / `anyOf` compõem validators
- CEXAI: instâncias de kind `validator` referenciam via `validation_schema`

**Experimente agora:** Encontre uma função de validação complexa no seu codebase. Decomponha-a em assertions atômicas, cada uma testando uma coisa. Reconstrua a validação composta chamando as atômicas em sequência. Meça como os testes unitários ficam muito mais fáceis.

### Padrão 4: Contratos de Interface para Comunicação Agente-a-Agente

Quando você tem dois agentes que se comunicam — um chamando o outro, um passando dados ao outro, um lendo do output do outro — você precisa de um contrato bilateral. É isso que o kind `interface` formaliza.

A propriedade chave de uma interface vs. um input_schema: um input_schema é unilateral (define o que UM componente aceita). Uma interface é bilateral (define o contrato ENTRE dois componentes, incluindo o formato de requisição e de resposta).

```yaml
# interface: contrato bilateral de agente
id: iface_n07_para_n03_dispatch
kind: interface
parties:
  caller: n07_orchestrator
  callee: n03_engineering
request:
  fields:
    - {name: task, type: str, required: true}
    - {name: kind, type: KindEnum, required: true}
    - {name: handoff_path, type: str, required: true}
response:
  fields:
    - {name: status, type: DispatchStatusEnum, required: true}
    - {name: artifact_path, type: str, required: false}
    - {name: quality_score, type: float, required: false}
    - {name: signal_written, type: bool, required: true}
error_contract:
  timeout: 3600
  retry_policy: no_retry
  on_failure: write_failed_signal
```

Essa interface é legível por máquina. N07 pode validar sua chamada de dispatch contra ela antes de enviar. N03 pode validar a task de entrada contra ela antes de executar. Ambas as partes têm uma fonte única de verdade que previne deriva de protocolo.

---

## Deep Dive de Arquitetura — Como os Kinds de P06 se Relacionam

```
P02 MODEL
  agent_def (define o que é um agente)
      |
      v
P06 SCHEMA: CAMADA DE DEFINIÇÃO
  enum_def <------ (conjuntos de valores finitos que type_def usa)
      |
      v
  type_def <------ (tipos customizados: KindEnum, NucleusId, QualityScore)
      |
      v
  input_schema <--- (o que o agente aceita: valida chamadores)
      |
      v
  interface <------ (bilateral: contrato request + response entre 2 agentes)

P05 OUTPUT: gera dados
      |
      v
P06 SCHEMA: CAMADA DE VALIDAÇÃO
  validator <------ (assertions atômicas: uma verificação, pass/fail)
      |
      v
  validation_schema <- (composto: referencia múltiplos validators)
      |
      v
  api_reference <-- (documenta tudo acima para consumidores externos)
```

A camada de definição (enums, tipos, input schemas, interfaces) roda ANTES do processamento — ela constrainge o que entra no sistema. A camada de validação (validators, validation schemas) roda DEPOIS da geração — ela audita o que o sistema produziu. Ambas as camadas referenciam as mesmas definições de tipo, criando um sistema de tipos coerente por todo o pipeline.

---

## Exemplos Reais do N00_genesis

**Input Schema na prática** (`N00_genesis/P06_schema/kind_input_schema/kind_manifest_n00.md`):
```yaml
id: input_schema_cex_8f_runner
kind: input_schema
target_component: cex_8f_runner
schema_format: pydantic
strict_mode: true
fields:
  - {name: intent, type: str, required: true}
  - {name: kind, type: NucleusId, required: false}
  - {name: execute, type: bool, required: false, default: false}
```
Esse schema é o portão de entrada para o motor de build do CEXAI. Qualquer chamada a `cex_8f_runner` com `intent` ausente ou `kind` inválido é rejeitada na fronteira, não dentro do motor.

**Validator para integridade estrutural** (`N00_genesis/P06_schema/kind_validator/kind_manifest_n00.md`):
```yaml
id: validator_tem_frontmatter
check_type: structural
assertion: "Artefato tem campos id, kind, pillar, nucleus, title, version, quality"
severity: error
error_message: "Campo obrigatório de frontmatter ausente: {field}"
applies_to: [knowledge_card, agent, prompt_template, workflow]
```
Esse único validator é referenciado por dezenas de validation schemas. Ele enforça o contrato de frontmatter em todos os tipos de artefatos.

**Schema de registro de parceiros** (`N00_genesis/P06_schema/ex_input_schema_partner_registration.md`):
Um input schema completo para um endpoint de registro de API de parceiros, com campos para nome da empresa, email de contato, seleção de tier de API, URL de webhook e validação de assinatura — demonstrando como os kinds de P06 escalam para contratos de API de produção.

**Interface de tabelas Supabase** (`N00_genesis/P06_schema/ex_interface_supabase_tables.md`):
Uma interface definindo o contrato entre um agente de IA e um backend de banco de dados Supabase — schemas de requisição para queries, schemas de resposta para result sets, contratos de erro para falhas de conexão e políticas de retry.

---

## Anti-Padrões — Os Erros Universais

### Anti-Padrão 1: Duck-Typing de Outputs de LLM

Acessar campos de output do LLM sem validação: `resultado["resumo"]` quando você não tem garantia de que `resumo` está na resposta. Isso falha silenciosamente com `KeyError` ou `None` no código downstream, geralmente no pior momento possível em produção.

**Solução**: defina um `validation_schema` para toda estrutura de output de LLM do qual seu código depende. Valide antes de acessar campos. Falhe barulhentamente no passo de validação, não silenciosamente no passo de acesso.

### Anti-Padrão 2: Usar Strings como Identificadores Sem Tipo Seguro

Passar strings como `"n03"`, `"landing_page"`, `"P05"` sem validação. Um único erro de digitação — `"landing-page"` vs. `"landing_page"` — causa uma falha na camada de dispatch que é dolorosa de rastrear.

**Solução**: defina `enum_def` para todo conjunto finito de valores válidos no seu sistema. `NucleusEnum`, `KindEnum`, `PillarEnum`. Valide todos os identificadores nas fronteiras de input usando esses enums.

### Anti-Padrão 3: Suposições de Interface Não Declaradas

Dois componentes que se comunicam mas nunca escreveram o contrato. "Funciona porque sei o que N03 espera." Isso quebra assim que N03 muda seu formato esperado e a mudança não é comunicada aos chamadores.

**Solução**: escreva um artefato `interface` para cada canal de comunicação agente-a-agente no seu sistema. Torne-o a fonte de verdade. Quando você mudar a interface, atualize o artefato e notifique todos os chamadores.

### Anti-Padrão 4: Validators Monolíticos

Uma única função de validação que verifica 20 coisas. Quando ela falha, você recebe um erro críptico e nenhuma forma de saber qual das 20 verificações falhou. Quando você quer reutilizar uma das 20 verificações em contexto diferente, não consegue.

**Solução**: um `validator` por assertion. Componha-os em `validation_schema`. Cada validator atômico tem um ID descritivo e uma mensagem de erro clara.

### Anti-Padrão 5: Deriva de Schema

Input schemas e definições de tipo que são escritos uma vez e nunca atualizados conforme o sistema evolui. Depois de 6 meses, o schema e o código estão fora de sincronia — o schema diz que `campo_x` é obrigatório, mas o código na verdade o ignora. O schema diz `type: int`, mas o código agora também trata strings.

**Solução**: trate schemas como documentos vivos. Adicione números de versão de schema. Quando o sistema muda, atualize o schema primeiro (desenvolvimento schema-first). Use ferramentas de geração de código para derivar implementação do schema onde possível.

---

## Conexões Entre Pilares

| Pilar | Relação com P06 |
|-------|-----------------|
| **P05 Output** | `response_format` (P05) constrainge a geração; `validation_schema` (P06) valida após a geração — são complementares, não alternativas |
| **P02 Model** | Definições de agente (P02) referenciam input schemas (P06) para documentar quais inputs eles aceitam — P06 torna agentes P02 chamáveis |
| **P04 Tools** | Definições de tool (P04) incluem function schemas (JSON Schema) — estas são instâncias de input_schema P06 para parâmetros de tool |
| **P07 Evals** | Eval datasets (P07) são validados contra validation schemas (P06) para garantir que casos de teste são bem-formados antes de rodar avaliações |
| **P08 Architecture** | Component maps (P08) referenciam interfaces (P06) — o diagrama de arquitetura descreve o que conecta; a interface define como |
| **P11 Feedback** | Quality gates (P11) referenciam validators (P06) para verificações estruturais — P06 define as regras, P11 as enforça como portões de pipeline |

### A Sinergia P06-P07

Validação de schema (P06) e avaliação (P07) tratam de dimensões diferentes de qualidade:

- **P06 Schema**: pass/fail binário — os dados conformam com o contrato ou não conformam. Sem crédito parcial.
- **P07 Evals**: pontuação graduada — mede o quão bom o output é em múltiplas dimensões. Crédito parcial, critérios ponderados.

Você precisa de ambos. Uma resposta pode ser estruturalmente válida (passa na validação P06) mas semanticamente pobre (pontua 4/10 no rubric P07). Uma resposta pode falhar na validação P06 (campo obrigatório ausente) mas conter conteúdo brilhante.

Execute a validação P06 primeiro (é barata e rápida). Apenas execute a avaliação P07 em respostas que passam no P06 (cara, usa chamadas de LLM ou revisão humana).

---

## Artefatos Relacionados

| Artefato | Relação | Score |
|----------|---------|-------|
| [[kc_pillar_brief_p06_schema_en]] | irmão (EN) | 1.0 |
| [[kc_pillar_brief_p05_output_pt]] | upstream | 0.72 |
| [[kc_pillar_brief_p07_evals_pt]] | downstream | 0.65 |
| [[kc_pillar_brief_p08_architecture_pt]] | relacionado | 0.58 |
| [[n00_p06_kind_index]] | fonte | 0.55 |
| [[n00_input_schema_manifest]] | relacionado | 0.52 |
| [[n00_validator_manifest]] | relacionado | 0.49 |
| [[ex_input_schema_partner_registration]] | exemplo | 0.44 |
| [[ex_interface_supabase_tables]] | exemplo | 0.42 |
| [[kc_pillar_brief_p04_tools_pt]] | upstream | 0.38 |
