---
kind: knowledge_card
id: bld_knowledge_card_context_file
pillar: P03
llm_function: INJECT
purpose: Domain knowledge for context_file production -- atomic searchable facts
sources: context-file-builder MANIFEST.md + SCHEMA.md + HERMES assimilation spec
quality: 9.1
title: "Knowledge Card: context_file"
version: "1.0.0"
author: n03_builder
tags: [context_file, builder, knowledge_card, hermes_origin, workspace_instructions]
tldr: "Domain knowledge for context_file: scope taxonomy, injection strategies, inheritance model, byte budgets, HERMES origin."
domain: "workspace instruction auto-injection"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.93
related:
  - bld_knowledge_card_system_prompt
  - p03_sp_system-prompt-builder
  - p01_kc_context_doc
  - bld_memory_system_prompt
  - bld_knowledge_card_context_doc
  - p01_kc_dispatch_rule
  - bld_knowledge_card_dispatch_rule
  - spec_infinite_bootstrap_loop
  - bld_knowledge_card_agent
  - bld_collaboration_memory_scope
---

# Domain Knowledge: context_file

## Executive Summary
Context files are the ambient instruction layer: static, project-scoped behavioral rules that
auto-inject into every agent turn for a defined scope (workspace/nucleus/session/global). They
implement HERMES CLAUDE.md / AGENTS.md pattern, elevating ad-hoc workspace files to first-class
CEX artifacts with scope taxonomy, inheritance chains, injection-point control, and priority
ordering. Unlike system_prompts (agent identity, loaded once at BECOME), context_files are
instructions, not identity -- they shape what the agent does, not who it is.

## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 |
| Format | YAML (frontmatter) + Markdown (body) |
| Naming | `{{scope}}_context.md` (e.g., `workspace_context.md`) |
| ID regex | `^ctx_[a-z][a-z0-9_]+$` |
| Max body bytes | 8192 |
| llm_function | INJECT |
| Origin | NousResearch/hermes-agent (CLAUDE.md / AGENTS.md) |

## Scope Model
| Scope | Narrowness | Auto-expires? | Use when |
|-------|-----------|--------------|---------|
| `global` | broadest | never | Universal standards across all CEX instances |
| `workspace` | per-repo | never | CLAUDE.md equivalent; repo-specific conventions |
| `nucleus` | per-nucleus | never | N03 build rules, N01 research conventions |
| `session` | per-session | yes (on close) | Sprint context, temporary overrides |
Rule: narrower scope overrides broader scope on rule conflict.

## Injection Points
| Point | Behavior | Token cost model |
|-------|---------|-----------------|
| `session_start` | Injected once; persists entire session | Pay once; safe default |
| `every_turn` | Re-injected at each message | N x cost; compliance-critical only |
| `f3_inject` | On-demand during F3 INJECT of 8F | Zero cost until called |

## Inheritance Model
Context files form a priority stack. Child inherits parent; overrides on conflict.
```
global_context  (priority: 0)  --inherits--> none (root)
workspace_ctx   (priority: 1)  --inherits--> [global_ctx]
nucleus_ctx     (priority: 2)  --inherits--> [workspace_ctx, global_ctx]
session_ctx     (priority: 3)  --inherits--> [nucleus_ctx, workspace_ctx, global_ctx]
```
Lower priority number = loads earlier; later (higher number) wins conflicts in same scope.

## Patterns
| Pattern | Rule |
|---------|------|
| Instructions only | Body = behavioral rules; facts go in knowledge_card, identity in system_prompt |
| Static content | No `{{vars}}`; static instructions that auto-apply without instantiation |
| Scope narrowing | Child extends parent; never duplicate parent rules in child |
| Byte budget first | Trim lower-priority rules before exceeding max_bytes |
| session_start default | Unless compliance-critical (every_turn) or pipeline-specific (f3_inject) |
| hermes_origin tag | Always include -- traces provenance to NousResearch/hermes-agent |

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Facts in context_file | Facts belong in knowledge_card; mixing inflates tokens and confuses retrieval |
| `{{vars}}` in body | Context files are static; use prompt_template for parameterized content |
| Duplicating parent rules | Child should override only; duplication causes drift when parent updates |
| Body over max_bytes | Harness silently truncates; critical rules get cut without warning |
| Scope: session + every_turn | Doubly expensive: per-turn AND temporary; avoid unless justified |
| Missing hermes_origin tag | Breaks HERMES assimilation provenance chain |
| scope mismatch | workspace-scoped rule put in global file = applies everywhere unnecessarily |

## Boundaries
| context_file IS | context_file IS NOT |
|-----------------|---------------------|
| Static ambient instructions for a scope | `system_prompt` -- agent identity (BECOME, not INJECT) |
| Auto-injected by harness per injection_point | `knowledge_card` -- facts, not behavioral rules |
| Inheritance-aware scope stack | `prompt_template` -- parameterized, requires instantiation |
| HERMES CLAUDE.md / AGENTS.md pattern | `instruction` -- task-scoped procedural recipe |

## Application
1. Choose scope: workspace for repo-level, nucleus for builder-level, session for sprint/temp
2. Select injection_point: session_start (default), every_turn (compliance), f3_inject (pipeline)
3. Build inheritance_chain: list parent IDs from broadest to narrowest
4. Author body: instructions only -- ALWAYS/NEVER rules, standing conventions, ambient constraints
5. Set priority (0 = most authoritative); applies_to_nuclei: [all] or specific IDs
6. Verify: body <= max_bytes, quality: null, id matches regex, no vars or facts in body

## References
- HERMES assimilation spec: `_docs/compiled/spec_hermes_assimilation.yaml`
- N03 8F rules: `.claude/rules/8f-reasoning.md`
- context_file schema: `archetypes/builders/context-file-builder/bld_schema_context_file.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_system_prompt]] | sibling | 0.25 |
| [[p03_sp_system-prompt-builder]] | related | 0.23 |
| [[p01_kc_context_doc]] | sibling | 0.20 |
| [[bld_memory_system_prompt]] | downstream | 0.20 |
| [[bld_knowledge_card_context_doc]] | sibling | 0.20 |
| [[p01_kc_dispatch_rule]] | sibling | 0.20 |
| [[bld_knowledge_card_dispatch_rule]] | sibling | 0.20 |
| [[spec_infinite_bootstrap_loop]] | related | 0.19 |
| [[bld_knowledge_card_agent]] | sibling | 0.19 |
| [[bld_collaboration_memory_scope]] | downstream | 0.19 |
