---
quality: 8.3
quality: 7.8
id: kc_context_file
kind: knowledge_card
8f: F3_inject
title: "context_file -- Workspace Instruction Auto-Injection"
version: 1.0.0
pillar: P01
language: English
tags: [context_file, p03, hermes_origin, workspace_instructions, injection, claude_md, agents_md]
tldr: "Project-scoped static instruction file auto-injected into agent context at a configurable injection point"
when_to_use: "When a workspace, nucleus, or session needs standing behavioral rules loaded into every agent turn"
density_score: 0.95
related:
  - p01_kc_dispatch_rule
  - p01_kc_session_state
  - bld_schema_dispatch_rule
  - p03_sp_session_state_builder
  - bld_memory_session_state
  - bld_knowledge_card_system_prompt
  - p06_is_quality_audit
  - p10_lr_session_backend_builder
  - p01_kc_session_backend
  - bld_collaboration_memory_scope
updated: "2026-04-22"
---

# context_file

## Definition
A `context_file` is a project-scoped, static instruction file automatically injected into every agent
context window at a configurable injection point (session_start, every_turn, or f3_inject). It
implements the HERMES CLAUDE.md / AGENTS.md pattern: standing behavioral rules for a workspace,
nucleus, or session that shape every agent turn without requiring manual prompt construction.

## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 |
| Format | YAML (frontmatter) + Markdown (body) |
| Naming | `{{scope}}_context.md` |
| ID regex | `^ctx_[a-z][a-z0-9_]+$` |
| Max body bytes | 8192 |
| llm_function | INJECT |
| Scope enum | `workspace`, `nucleus`, `session`, `global` |
| Injection enum | `session_start`, `every_turn`, `f3_inject` |
| Inheritance | parent context_file IDs in `inheritance_chain` |
| Priority | integer; 0 = highest; lower number loads first |
| Origin | NousResearch/hermes-agent (CLAUDE.md / AGENTS.md) |

## Required Frontmatter
| Field | Type | Notes |
|-------|------|-------|
| id | string | `ctx_{{scope_slug}}` -- unique per scope |
| kind | literal | `context_file` |
| pillar | literal | `P03` |
| title | string | Human-readable scope description |
| scope | enum | workspace \| nucleus \| session \| global |
| injection_point | enum | session_start \| every_turn \| f3_inject |
| inheritance_chain | list | Parent IDs; empty = root context_file |
| max_bytes | integer | Body size budget (default 8192) |
| priority | integer | Load order: 0 = highest; higher number = lower priority |
| applies_to_nuclei | list | `[all]` or explicit nucleus IDs |
| version | semver | Artifact version |
| quality | null | Always null -- never self-score |
| tags | list | Min 3; include `hermes_origin` and scope name |

## Scope Model
| Scope | Coverage | Example |
|-------|---------|---------|
| `global` | All sessions, all nuclei, all workspaces | CEX-wide coding standards |
| `workspace` | All nuclei within one project directory | Per-repo CLAUDE.md rules |
| `nucleus` | One nucleus across all its sessions | N03 build conventions |
| `session` | Current session only; auto-expires on close | Sprint-specific context |

## Injection Points
| Point | When injected | Cost |
|-------|--------------|------|
| `session_start` | Once at session open; persists in context | Pays once per session |
| `every_turn` | Re-injected at each user message | Reliable but token-expensive |
| `f3_inject` | Loaded explicitly during F3 INJECT step of 8F | On-demand via pipeline |

## Inheritance Model
Context files form a chain: child extends parent, overriding only what it specifies.
```
global_context.md          (priority: 0, applies_to_nuclei: [all])
  |
  +-- workspace_context.md (priority: 1, applies_to_nuclei: [all])
        |
        +-- nucleus_context.md  (priority: 2, applies_to_nuclei: [n03])
              |
              +-- session_context.md  (priority: 3, scope: session)
```
Higher priority number = loaded later; later rules win on conflict.

## Patterns
| Pattern | Rule |
|---------|------|
| Scope narrowing | Each child scope narrows coverage; global -> workspace -> nucleus -> session |
| Instruction-only body | Body contains behavioral rules, never facts or knowledge (use knowledge_card for facts) |
| Static content | No `{{vars}}` -- context_files are static (use prompt_template for parameterized) |
| Byte budget awareness | Body must fit within `max_bytes`; trim with priority: cut lower-priority rules first |
| Inheritance over duplication | If a rule applies at workspace scope, do not repeat it in nucleus scope |
| Priority 0 = most authoritative | Lowest number loads first; higher-priority context wins on conflict |

## Boundaries
| context_file IS | context_file IS NOT |
|-----------------|---------------------|
| Project-scoped static instructions | `system_prompt` -- agent-level identity (loaded at BECOME, not INJECT) |
| Auto-injected per injection_point | `knowledge_card` -- facts; context_file is behavioral rules |
| Scope-aware with inheritance chain | `prompt_template` -- parameterized with vars; context_file is static |
| Ambient standing rules for a scope | `instruction` -- task-scoped procedural recipe |
| HERMES CLAUDE.md / AGENTS.md pattern | `action_prompt` -- single-shot user task execution |

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Putting facts in context_file | Facts belong in knowledge_card; mixing concerns reduces retrievability |
| Using `{{vars}}` in body | context_file is static; use prompt_template for parameterized content |
| Priority conflicts unresolved | Two same-priority context_files for same scope create unpredictable merge order |
| Body exceeding max_bytes | Harness truncates oversize files; critical rules get cut silently |
| Duplicating parent chain rules | Child should override only; duplication wastes tokens and invites drift |
| scope: session with every_turn injection | Re-injects per turn AND expires on close; doubles cost for temporary context |

## Application
1. Decide scope: is this global, workspace, nucleus, or session?
2. Set injection_point: session_start for stable rules, every_turn for critical compliance, f3_inject for on-demand
3. Build inheritance_chain: list parent context_file IDs this one inherits from
4. Write body: instructions only -- no facts, no `{{vars}}`, no procedural recipes
5. Set priority: 0 for most authoritative; increment for each scope narrowing
6. Set applies_to_nuclei: [all] for cross-nucleus; specific list for nucleus-scoped
7. Verify body <= max_bytes; validate frontmatter parses cleanly; quality: null

## Origin
NousResearch/hermes-agent introduced `CLAUDE.md` (workspace instructions) and `AGENTS.md`
(multi-agent coordination instructions) as files auto-injected into every conversation context.
CEX elevates this to a first-class artifact kind with scope taxonomy, inheritance chains,
injection-point control, and priority ordering.

## Builder
`archetypes/builders/context-file-builder/`
`python _tools/cex_8f_runner.py "create workspace context for N03" --kind context_file --execute`

## Related Kinds
- `system_prompt` (P03) -- agent identity; loads before context_file in the BECOME stage
- `knowledge_card` (P01) -- domain facts injected alongside context files at F3 INJECT
- `prompt_template` (P03) -- parameterized instructions; context_file is static equivalent
- `instruction` (P03) -- task-scoped recipe; context_file is ambient scope-level rules
- `agent` (P02) -- definition that references which context_files to load
- `memory_scope` (P10) -- where session context_file lifespan intersects with memory model

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_dispatch_rule]] | sibling | 0.23 |
| [[p01_kc_session_state]] | sibling | 0.22 |
| [[bld_schema_dispatch_rule]] | downstream | 0.22 |
| [[p03_sp_session_state_builder]] | downstream | 0.21 |
| [[bld_memory_session_state]] | downstream | 0.21 |
| [[bld_knowledge_card_system_prompt]] | sibling | 0.21 |
| [[p06_is_quality_audit]] | downstream | 0.20 |
| [[p10_lr_session_backend_builder]] | downstream | 0.20 |
| [[p01_kc_session_backend]] | sibling | 0.19 |
| [[bld_collaboration_memory_scope]] | downstream | 0.19 |
