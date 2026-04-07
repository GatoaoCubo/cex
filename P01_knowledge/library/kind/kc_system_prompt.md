---
id: p01_kc_system_prompt
kind: knowledge_card
type: kind
pillar: P03
title: "System Prompt — Deep Knowledge for system_prompt"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: system_prompt
quality: 9.1
tags: [system_prompt, P03, BECOME, kind-kc]
tldr: "Identity-defining prompt read first by the LLM, establishing persona, rules, output format, and behavioral boundaries"
when_to_use: "Building, reviewing, or reasoning about system_prompt artifacts"
keywords: [identity, persona, system-message]
feeds_kinds: [system_prompt]
density_score: null
---

# System Prompt

## Spec
```yaml
kind: system_prompt
pillar: P03
llm_function: BECOME
max_bytes: 4096
naming: p03_sp_{{agent}}.md
core: true
```

## What It Is
A system prompt is the identity-defining text read first by the LLM at the start of every conversation. It establishes who the agent is, what rules it follows, what format it outputs, and what it must never do. The LLM "becomes" this persona. It is NOT an action_prompt (task-specific, disposable) nor an instruction (step-by-step procedure). A system prompt is persistent, loaded at boot, and shapes all subsequent behavior.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `SystemMessage` in `ChatPromptTemplate` | First message in the messages list sets agent identity |
| LlamaIndex | System prompt in `LLM` / `ChatEngine` config | `chat_engine = index.as_chat_engine(system_prompt="...")` |
| CrewAI | `Agent(role=..., goal=..., backstory=...)` | Role+goal+backstory compose the effective system prompt |
| DSPy | `Signature` docstring + module-level instructions | Docstring shapes the module's behavioral framing |
| Haystack | `PromptBuilder` system template section | System section in the Jinja2 template for generators |
| OpenAI | `system` role message / `Assistant.instructions` | `{"role": "system", "content": "..."}` in Messages API |
| Anthropic | `system` parameter in Messages API | Top-level `system` field, read before all user messages |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| persona | string | required | Detailed = consistent voice but longer context cost |
| rules | list[str] | [] | More rules = safer but more constrained creativity |
| output_format | string | "flexible" | Fixed format = parseable but rigid; flexible = natural |
| forbidden | list[str] | [] | More forbidden topics = safer but may refuse valid queries |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Minimal identity | General-purpose assistant | "You are a helpful assistant. Be concise." |
| Domain expert persona | Specialized agent | "You are a senior e-commerce analyst. Focus on Brazilian marketplaces." |
| Guardrailed persona | Safety-critical applications | Persona + explicit forbidden topics + output constraints |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Task instructions in system prompt | Bloats identity with disposable content; changes per request | Keep tasks in action_prompt; system_prompt is static identity only |
| No output format guidance | Model outputs vary wildly between calls | Add explicit output format section to system prompt |
| Copy-paste system prompts across agents | Agents lose distinct identity; routing becomes meaningless | Customize persona, rules, and domain per agent |

## Integration Graph
```
[mental_model] --> [system_prompt] --> [action_prompt]
                        |
               [constraint_spec, instruction]
```

## Decision Tree
- IF building a persistent agent THEN system_prompt is mandatory
- IF agent is one-shot/ephemeral THEN minimal system_prompt or none
- IF output must be structured THEN include output_format in system_prompt
- IF domain is specialized THEN include domain expertise in persona
- DEFAULT: Persona + rules + output format, under 2000 tokens

## Quality Criteria
- GOOD: Clear persona, explicit rules, output format defined, under 4096 bytes
- GREAT: Persona matches domain; rules are testable; includes few-shot example reference
- FAIL: Mixed with task instructions; no persona; contradictory rules; >4096 bytes

## Production Reference: OpenClaude (Claude Code CLI)
OpenClaude's system prompt architecture (prompts.ts, 914 lines) reveals production patterns:

| Section | Purpose | CEX Equivalent |
|---------|---------|----------------|
| Identity | "You are an interactive agent..." | p03_sp_cex_core_identity |
| System | Tool results, hooks, context limits | Part of identity |
| Doing Tasks | No gold-plating, read before edit, verify | p03_ins_doing_tasks |
| Actions | Reversibility, blast radius, confirmation | p03_ins_action_protocol |
| Using Your Tools | Dedicated tools over Bash, parallel calls | Part of identity |
| Tone and Style | No emojis, file:line references, concise | Part of identity |
| Output Efficiency | Lead with answer, skip filler | Part of identity |
| Session-specific | Agent tools, verification contract, skills | Dynamic per-nucleus |
| Environment | CWD, platform, git status, model info | {{ENV_INFO}} runtime var |

**Key architectural insight**: Static sections (Identity through Output Efficiency) are
cache-shared across sessions. Dynamic sections (Session-specific, Environment) are
per-session and separated by a `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` marker.
CEX equivalent: {{INCLUDE}} directives for static, runtime vars for dynamic.

**New anti-pattern discovered**: "Verification avoidance" — agents narrate what they
would test instead of actually running tests. Counter: require Command run blocks in
every verification check (see p03_sp_verification_agent).

## Production Reference: OpenClaude Agent Types
Three built-in agent system prompts with role constraints:
- **Explore agent**: READ-ONLY, fast (haiku model), omits project rules
- **Plan agent**: READ-ONLY, deep (inherit model), produces Critical Files list
- **Verification agent**: READ-ONLY, adversarial, produces VERDICT enum

Pattern: All three are read-only by design. Write access is only for the main agent.
Sub-agents that verify or plan should NEVER have write tools.
