---
quality: null
# TEMPLATE: System Prompt (P03 Prompt)
# Valide contra P03_prompt/_schema.yaml (types.system_prompt)
# Max 4096 bytes

id: p03_sp_[agent_slug]
kind: system_prompt
8f: F2_become
pillar: P03
title: [system_prompt_do_agente]
target_agent: [agent_name]
density_score: 1.0
updated: "2026-04-17"
related:
  - p02_agent_[name_slug]
  - p02_iso_[agent_name]
  - p07_e2e_[pipeline_slug]
  - p10_ss_[session_slug]
  - p03_sp_system-prompt-builder
  - bld_memory_system_prompt
---

<!-- Orchestrator system prompts: target <15% of context budget. -->

# System Prompt: [agent_name]

## Purpose

A system_prompt defines the behavioral identity of an LLM agent -- who it is, what rules it
follows, what output it produces, and when the task is complete. System prompts are injected
at the start of every conversation and persist for the entire session. They are distinct from
context_files (workspace rules) and personality (voice/style) -- a system prompt is the agent's
core identity contract.

## Identity

<!-- INSTRUCAO: 2-4 frases com papel, escopo e limites. -->
[voce_e_o_agente_x]. [missao_principal]. [nao_faca_y].

## Rules

<!-- INSTRUCAO: regras em imperativos curtos, auditaveis. -->
1. [regra_1]
2. [regra_2]
3. [regra_3]
4. [regra_4]

## Output Format

<!-- INSTRUCAO: formato esperado em bullets ou bloco. -->
```text
[estrutura_de_resposta]
```

## Success Criteria

<!-- INSTRUCAO: condicoes explicitas de parada. Quando a tarefa esta COMPLETA? -->
1. [criterio_mensuravel_1]
2. [criterio_mensuravel_2]
3. [criterio_mensuravel_3]

## Deviation Rules

<!-- INSTRUCAO: o que fazer quando obstaculos aparecem. -->
1. Missing input file -> search alternatives with Glob/Grep, proceed if found
2. Ambiguous requirement -> choose simpler interpretation, document assumption
3. Tool error -> retry once with adjusted params, then try alternative tool
4. Blocked after 3 attempts -> STOP. Report what was attempted and why it failed. Do NOT improvise.

## Anti-Patterns

<!-- INSTRUCAO: comportamentos proibidos. -->
- Sycophancy: never agree with user assumption without verification
- Premature claim: never say "done" without verification evidence
- Hallucinated paths: never reference files without confirming they exist
- Scope creep: never add features not requested

## Embedded Variables

<!-- INSTRUCAO: placeholders authoring-tier. -->
- Context: [contexto_relevante]
- Goal: [objetivo_do_usuario]
- Constraints: [restricoes_ativas]

## Section Authoring Guide

| Section | Purpose | Tokens budget | Required |
|---------|---------|--------------|----------|
| Identity | WHO the agent is, mission, scope boundaries | 50-100 | yes |
| Rules | Imperative, auditable behavioral rules | 100-200 | yes |
| Output Format | Expected response structure | 50-100 | yes |
| Success Criteria | Measurable task completion conditions | 50-100 | yes |
| Deviation Rules | What to do when blocked or ambiguous | 100-150 | yes |
| Anti-Patterns | Explicitly prohibited behaviors | 50-100 | recommended |
| Embedded Variables | Runtime-replaced placeholders | 30-50 | optional |

### Token Budget Guidelines

System prompts should target less than 15% of the context window budget. For a 200K context
window, this means approximately 30K tokens maximum. For a 1M context window (Opus), the
ceiling is higher but the same principle applies: system prompt is overhead, not content.

```
Context window allocation:
  System prompt:     <15%  (identity, rules, format)
  Context files:     <10%  (workspace rules)
  Injected context:  <40%  (KCs, examples, memory)
  Working space:     >35%  (reasoning, generation)
```

## Variable Injection Patterns

System prompts support three tiers of variable injection, each resolved at a different stage.

| Tier | Syntax | Resolution time | Example | Resolver |
|------|--------|----------------|---------|----------|
| Authoring-time | `[placeholder]` | When human fills the template | `[agent_name]` | Manual or /build |
| Build-time | `{{VARIABLE}}` | When builder compiles artifact | `{{BRAND_NAME}}` | `brand_inject.py` |
| Runtime | `{variable}` | When prompt is assembled for LLM call | `{user_query}` | `cex_crew_runner.py` |

### Injection Examples

```yaml
# Authoring-time: filled by builder during /build
identity: "You are [agent_name], a [role_description]."

# Build-time: resolved by brand_inject.py during compilation
greeting: "Welcome to {{BRAND_NAME}}. {{BRAND_TAGLINE}}"

# Runtime: resolved per-request by the prompt assembler
context: |
  User query: {user_query}
  Session history: {session_context}
  Available tools: {tool_descriptions}
```

## Prompt Assembly Pipeline

Shows how a system prompt template becomes a fully resolved prompt at runtime.

```
tpl_system_prompt.md (this template)
  |
  v
[Authoring] Human or /build fills [placeholders]
  |
  v
p03_sp_{agent_slug}.md (authored system prompt)
  |
  v
[Build-time] brand_inject.py resolves {{BRAND_*}} variables
  |
  v
compiled/{agent_slug}.yaml (compiled prompt with brand context)
  |
  v
[Runtime] cex_crew_runner.py injects {runtime_vars}
  |
  v
Final prompt string -> sent to LLM API
```

## Prompt Quality Checklist

- Identity section is 2-4 sentences (not a paragraph, not a single word)
- Rules use imperative mood ("Do X", "Never Y") not descriptive ("The agent should X")
- Output format includes a concrete example, not just description
- Success criteria are measurable (countable, verifiable, observable)
- Anti-patterns list real failure modes observed in testing, not generic advice
- Total prompt length stays within budget for the agent tier (see table above)
- No orphaned variables: every `[placeholder]` has a corresponding instruction
- No ambiguous scope: each rule applies to exactly one behavior

## Relationship to Other Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| `agent` | P02 | Agent defines capabilities; system_prompt defines identity |
| `context_file` | P03 | Context file = workspace rules; system_prompt = agent identity |
| `personality` | P02 | Personality = voice/style; system_prompt = core rules |
| `prompt_template` | P03 | Template = per-task prompt; system_prompt = persistent identity |
| `agent_card` | P08 | Agent card = deployment spec; system_prompt = behavioral contract |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_[name_slug]]] | upstream | 0.38 |
| [[p02_iso_[agent_name]]] | upstream | 0.34 |
| [[p07_e2e_[pipeline_slug]]] | downstream | 0.30 |
| [[p10_ss_[session_slug]]] | downstream | 0.29 |
| [[p03_sp_system-prompt-builder]] | sibling | 0.18 |
| [[bld_memory_system_prompt]] | downstream | 0.16 |
