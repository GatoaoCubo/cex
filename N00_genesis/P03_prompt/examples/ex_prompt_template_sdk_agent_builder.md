---
id: p03_pt_sdk_agent_builder
kind: prompt_template
8f: F6_produce
pillar: P03
title: SDK Agent Builder - Generate Agent Artifacts from Description
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
domain: building
quality: 9.2
tags: [sdk, agent-builder, code-generation, meta-construction, tool-definition]
tldr: Template para gerar MASTER_INSTRUCTIONS.md + AGENT_CONFIGURATION.json a partir de descricao natural language
when_to_use: Ao criar novo agente SDK, gerar artifacts de agente, meta-construcao automatizada
keywords: [sdk-agent, agent-builder, meta-construction, artifact-generation]
long_tails:
  - como gerar agente SDK a partir de descricao em linguagem natural
  - como criar artifacts de agente automaticamente
axioms:
  - Todo prompt precisa de PURPOSE, INPUT, EXECUTION, OUTPUT, VALIDATION
  - Placeholder text restante = artifact invalido (zero tolerance)
density_score: 0.89
related:
  - p01_kc_agent
  - bld_collaboration_agent
  - agent-builder
  - bld_tools_capability_registry
  - bld_knowledge_card_agent
  - bld_architecture_agent
  - atom_03_openai_agents_sdk
  - p03_ins_mental_model
  - bld_instruction_agent
  - p01_kc_claude_agent_sdk_patterns
---

# SDK Agent Builder Prompt

## Variables

| Var | Tipo | Descricao | Exemplo |
|-----|------|-----------|---------|
| {{DESCRIPTION}} | string | Natural language agent description (10-500 words) | "An agent that monitors stock prices" |
| {{AGENT_NAME}} | string | Override auto-generated name | competitor_research |
| {{MODEL}} | string | Model to use | gpt-4o |
| {{TEMPERATURE}} | float | Temperature | 0.7 |
| {{TOOLS}} | list | Explicit tool names | [web_search, analyze_data] |
| {{OUTPUT_DIR}} | string | Where to write files | ./my_agent/ |

## Template Body

```
Gere SDK-ready agent artifacts a partir desta descricao:

{{DESCRIPTION}}

## Phase 1: Parse Description (10s)
1. Extrair: purpose, domain, core capabilities, tool requirements
2. Inferir metadata: name (snake_case), display_name (Title Case), description (1 linha)
3. Identificar tools: BUILTIN (file_search, code_interpreter, web_search) vs CUSTOM

## Phase 2: Design Tool Schema (20s)
Para cada CUSTOM tool, gerar:
- name: snake_case, unico
- description: 10-100 chars, actionable
- parameters: array com name, type, required, enum
- returns: type + description

## Phase 3: Generate MASTER_INSTRUCTIONS.md (30s)
Sections obrigatorias:
- Identity (role + purpose)
- Core Capabilities (5+ bullets)
- Tools Available (cada tool com I/O)
- Behavior Guidelines (5+ regras)
- Response Format (template)
- Example Interactions (2+ pares concretos)

## Phase 4: Generate AGENT_CONFIGURATION.json (20s)
Schema: agent{name,display_name,description,version} + model{name,temperature,max_tokens} + tools{builtin,custom} + metadata

## Phase 5: Validate (10s)
- Tools em config == tools em instructions
- Nome consistente across files
- Zero placeholder text

## Constraints
- MUST: gerar ambos files, 2+ examples, snake_case names, behavior guidelines, JSON valido
- NEVER: placeholder text, tools sem parameters, descricoes vagas, JSON invalido
```

## Quality Gates

- Instructions: min 50 linhas, target 100+
- Examples: min 2 pares concretos (nao placeholder)
- Tool descriptions: min 20 chars, target 50+
- Behavior guidelines: min 3, target 5+
- JSON: parseable, sem syntax errors

## Examples

### Input
```yaml
description: "Agent que pesquisa concorrentes, analisa produtos e pricing, gera reports comparativos"
model: "gpt-4o"
temperature: 0.5
```

### Output (MASTER_INSTRUCTIONS.md excerpt)
```markdown
# Competitor Research Agent

## Identity
Competitive intelligence specialist para market research e competitor analysis.

## Core Capabilities
- Web search por company information
- Analise de product offerings e pricing
- Comparison reports estruturados
- Track competitor updates over time

## Tools Available
### search_competitor
Input: company_name (string), query_type (enum: general|products|pricing|news)
Output: Structured search results com sources
```

### Output (AGENT_CONFIGURATION.json excerpt)
```json
{
  "agent": {"name": "competitor_research", "display_name": "Competitor Research Agent"},
  "model": {"name": "gpt-4o", "temperature": 0.5},
  "tools": {"builtin": ["web_search"], "custom": [{"name": "search_competitor", "parameters": [...]}]}
}
```

## Semantic Bridge

- Also known as: agent generator, meta-constructor, agent factory, agent scaffold
- Keywords: agent generation, SDK, meta-construction, artifact generation, tool definition
- LangChain: AgentFactory | OpenAI: Agent Builder | Anthropic: Agent SDK | LlamaIndex: AgentWorker

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_agent]] | upstream | 0.35 |
| [[bld_collaboration_agent]] | downstream | 0.34 |
| [[agent-builder]] | upstream | 0.33 |
| [[bld_tools_capability_registry]] | downstream | 0.29 |
| [[bld_knowledge_card_agent]] | upstream | 0.28 |
| [[bld_architecture_agent]] | downstream | 0.27 |
| [[atom_03_openai_agents_sdk]] | upstream | 0.26 |
| [[p03_ins_mental_model]] | related | 0.26 |
| [[bld_instruction_agent]] | related | 0.25 |
| [[p01_kc_claude_agent_sdk_patterns]] | upstream | 0.25 |
