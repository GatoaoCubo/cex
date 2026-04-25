---
quality: 7.7
id: kc_hermes_agent_assimilation
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: N01
domain: competitive_intelligence
type: framework_analysis
source: NousResearch/hermes-agent (github, MIT, released 2026-02-25, 95.6K stars at 7 weeks)
version: 1.0.0
tags: [hermes, nous_research, agent_framework, gap_analysis, assimilation_spec]
tldr: "Complete gap analysis of Hermes Agent's 12 core primitives against CEX's 300-kind taxonomy, identifying 9 novel kinds (user_model, messaging_gateway, personality, context_file, pipeline_template, revision_loop_policy, terminal_backend, curation_nudge, hibernation_policy) and 6 partial-coverage enrichments -- all successfully assimilated in W1-W5 (2026-04-18)"
when_to_use: "When planning future framework assimilations; when evaluating which Hermes features to port deeper; when checking assimilation debt (9 kinds absorbed, upstream divergence monitoring needed)"
axioms:
  - "ALWAYS compare primitives 1:1 before declaring a gap -- 8 of Hermes' 12 primitives already had CEX equivalents; only 4 were genuinely novel"
  - "ALWAYS track assimilation debt -- absorbed kinds must be monitored for upstream divergence as Hermes evolves past v0.11.0"
  - "NEVER assimilate without typing -- every Hermes concept must map to a CEX kind with pillar, nucleus, and builder before it enters the taxonomy"
  - "NEVER port skills without governance -- Hermes' 118 untyped skills vs. CEX's 302 typed builders is an architecture decision, not a coverage gap"
updated: 2026-04-18
related:
  - p01_kc_agent
  - spec_infinite_bootstrap_loop
  - bld_memory_skill
  - agent-builder
  - cex_llm_vocabulary_whitepaper
  - procedural-memory-builder
  - self_audit_n03_builder_20260408
  - bld_knowledge_card_procedural_memory
  - bld_collaboration_agent
  - spec_n07_operational_intelligence
density_score: 1.0
---

## TL;DR

HERMES Agent (NousResearch) is a self-improving single-agent framework with a
built-in learning loop: autonomous skill creation, three-layer memory, multi-
platform messaging gateway, six terminal backends, and 118 bundled skills.
Adjacent repo `opencode-hermes-multiagent` exposes a 17-agent pipeline variant
with scenario-indexed workflows. CEX is a typed-taxonomy factory (300 kinds /
12 pillars / 7 nuclei); HERMES is a runtime-plus-skill-library. The gap is
largely in **user modeling**, **messaging surface**, **personality hot-swap**,
**terminal backend abstraction**, and **scenario-indexed pipelines**.

## Source of Truth

| Layer | Artifact |
|-------|----------|
| Main repo | github.com/NousResearch/hermes-agent |
| AGENTS.md | Single-agent codebase guide (no role taxonomy) |
| skills-catalog.md | 118 skills in 15+ categories |
| Multi-agent fork | github.com/1ilkhamov/opencode-hermes-multiagent (17 roles) |
| License | MIT |

## HERMES Core Primitives (12)

| # | Primitive | HERMES function | CEX equivalent? |
|---|-----------|----------------|-----------------|
| 1 | Agent Loop | Central orchestration | N07 + 8F pipeline |
| 2 | Skills | Procedural memory, autonomous creation + self-improvement | `skill` kind (lacks autonomous create) |
| 3 | Tools | 40+, RPC-callable from Python, toolset grouping | `toolkit`, `cli_tool`, `mcp_server` (no RPC wrapper) |
| 4 | Memory (3-layer) | Persistent + user-profile + FTS5 session search | Partial: `entity_memory`, `knowledge_index`, `memory_summary` |
| 5 | Personalities | `/personality [name]` hot-swap | **MISSING** |
| 6 | Context Files | Project-scoped .md shapes every turn | Partial: CLAUDE.md (N07 only) |
| 7 | User Model | Honcho dialectic framework, cross-session | **MISSING** |
| 8 | Sessions | Containers with /new, /reset, /compress | `session_state`, `session_backend` |
| 9 | Terminal Backends | local/Docker/SSH/Daytona/Singularity/Modal | `sandbox_config` (lacks Daytona/Modal/Singularity) |
| 10 | Messaging Gateway | TG/Discord/Slack/WhatsApp/Signal/Email single process | **MISSING** |
| 11 | Cron Scheduler | NL-driven, platform-delivery | `schedule` (no NL front) |
| 12 | ACP Adapter | Agent Communication Protocol | Mentions A2A in handoffs but no `acp_adapter` kind |

## HERMES Skill Catalog Categories (15)

apple · autonomous-ai-agents · creative · data-science · devops · email · gaming · github · leisure · mcp · media · mlops · productivity · red-teaming · research · security · smart-home · social-media · software-development

Notable skills CEX lacks as typed artifacts:
- **dogfood** — QA/bug reporting skill (we have `bugloop` but not user-facing dogfood)
- **opinionated software-dev bundle** — plan / writing-plans / TDD / systematic-debugging / subagent-driven-development / requesting-code-review
- **mcporter + native-mcp** — MCP auto-discovery + native client
- **telephony** — SMS/MMS/voice via Twilio/Bland.ai
- **hibernation + idle policy** (implicit in Daytona/Modal backends)

## OpenCode-Hermes Multi-Agent Variant (17 roles)

| Tier | Roles | Thinking Budget |
|------|-------|-----------------|
| Core | Hermes (router) | gpt-5.2-high |
| Research | @finder, @analyst, @researcher | flash / thinking-high / thinking-low |
| Planning | @architect, @planner | opus-medium / flash |
| Implementation | @coder, @editor, @fixer, @refactorer | opus-high x2, sonnet-high x2 |
| Quality | @reviewer, @tester, @debugger, @security | codex-xhigh x3, sonnet-high |
| Documentation | @documenter, @commenter | sonnet-medium, sonnet-low |
| Infrastructure | @devops, @optimizer | sonnet-medium, sonnet-high |

**Pipeline templates (scenario-indexed):**
- New Feature: finder -> analyst -> architect -> planner -> coder -> reviewer -> tester -> documenter
- New Feature + Security: + @researcher, + @security pre-tester
- Bug Fix (unknown cause): finder -> debugger -> fixer -> reviewer -> tester
- Bug Fix (known cause): finder -> fixer -> reviewer -> tester
- Refactoring: finder -> analyst -> refactorer -> reviewer -> tester
- Perf Opt: finder -> analyst -> optimizer -> reviewer -> tester
- Infra: finder -> devops -> reviewer -> tester

**Handoff rules:** full context passed · mandatory @reviewer+@tester gates · max 3 revision loops · priority security > quality > implementation.

## Gap Analysis vs CEX (300 kinds / 12 pillars)

### NOVEL — not typed in CEX (priority P1)

| Proposed kind | Pillar | Nucleus | Maps to HERMES |
|---------------|--------|---------|---------------|
| `user_model` | P10 | N04 | Honcho dialectic profile |
| `messaging_gateway` | P04 | N05 | Multi-platform unified process |
| `personality` | P02 | N03 | Hot-swap persona (`/personality`) |
| `context_file` | P03 | N03 | Project-scoped .md shaping behavior |
| `pipeline_template` | P12 | N07 | Scenario-indexed agent sequence (OpenCode-Hermes) |
| `revision_loop_policy` | P11 | N05 | Max-N-iterations-before-escalation |
| `terminal_backend` | P09 | N05 | Abstract local/Docker/SSH/Daytona/Modal/Singularity |
| `curation_nudge` | P11 | N04 | Periodic memory-persistence reminder |
| `hibernation_policy` | P09 | N05 | Idle-state serverless cost guard |

### PARTIAL — exists but needs enrichment (priority P2)

| CEX kind | Gap | Enhancement from HERMES |
|----------|-----|-------------------------|
| `skill` | No autonomous creation metadata, no agentskills.io schema | Add `auto_generated_from`, `self_improves`, `catalog_category` |
| `session_state` | No FTS5 search + LLM summarization | Add `search_backend: fts5`, `summarizer_model` |
| `sandbox_config` | Covers Docker/SSH only | Add Daytona, Modal, Singularity backends |
| `schedule` | No NL front | Add `nl_spec: "every weekday at 9am ..."` |
| `agent` | No thinking-budget tier | Add `thinking_budget: high|medium|low|xhigh` |
| `handoff` / `handoff_protocol` | No revision-loop cap | Add `max_revisions: 3`, `escalation_target` |

### ALREADY COVERED (no action)

- `toolkit`, `cli_tool`, `mcp_server` (tool system)
- `entity_memory`, `knowledge_index`, `memory_summary` (memory base)
- `reasoning_trace` (trajectory / batch-runner equivalent)
- `red_team_eval` (godmode equivalent)
- `rl_algorithm` (tinker-atropos equivalent, standalone kind)
- `audio_tool`, `stt_provider`, `tts_provider` (voice memo)

## Assimilation Spec (exec plan)

### Wave 1 (P1 — 9 new kinds, highest value)

Dispatch N03 to author builders for:
1. `user_model` (P10) — dialectic cross-session user profile
2. `messaging_gateway` (P04) — multi-platform unified gateway
3. `personality` (P02) — hot-swap persona
4. `context_file` (P03) — project-scoped instruction file
5. `pipeline_template` (P12) — scenario-indexed agent sequence
6. `revision_loop_policy` (P11) — max-N retry policy
7. `terminal_backend` (P09) — execution-environment abstraction
8. `curation_nudge` (P11) — proactive memory-persistence reminder
9. `hibernation_policy` (P09) — idle-state cost guard

Each: 13-ISO builder + 1 KC + 1 sub-agent (.claude/agents/) + kinds_meta entry.
Cost estimate (N03 Opus, 1M ctx): ~9 dispatches x ~40k tokens = ~360k tokens.

### Wave 2 (P2 — enrich 6 existing kinds)

Dispatch N03 + N04 to add frontmatter fields to existing builder ISOs:
- `skill` — auto_generated_from, self_improves, catalog_category
- `session_state` — search_backend, summarizer_model
- `sandbox_config` — backend_type enum extension
- `schedule` — nl_spec free-text field
- `agent` — thinking_budget enum
- `handoff` / `handoff_protocol` — max_revisions, escalation_target

### Wave 3 (integration)

1. Update `.cex/kinds_meta.json` (+9 kinds -> 300 kinds)
2. Update `p03_pc_cex_universal.md` (prompt_compiler) — add verb/pattern rows for 9 new kinds PT+EN
3. Update `_docs/specs/spec_metaphor_dictionary.md` — add industry/canonical terms
4. Write 118-skill catalog scan — mark which map to existing CEX skills vs new
5. Update CLAUDE.md header (284 -> 300 kinds)

## Decision Points (GDP — user must confirm before Wave 1)

| DP | Question | Recommended default |
|----|----------|---------------------|
| DP1 | Assimilate all 9 P1 kinds, or cherry-pick? | All 9 (they're internally consistent) |
| DP2 | Author builders with Opus N03 or Sonnet N03? | Opus (reasoning-heavy) |
| DP3 | Grid dispatch (9 parallel) or sequential (9 solo)? | Sequential solo (budget + avoids nested quotes) |
| DP4 | Include Wave 2 enrichments in same session? | Yes (touching same builders) |
| DP5 | Add `messaging_gateway` stubs only, or full skill ports? | Stubs only (port Telegram as pilot later) |

## Industry Terms (ubiquitous language)

| HERMES term | Industry canonical | CEX term |
|-------------|-------------------|----------|
| Skill | Procedural memory / capability | `skill` kind |
| Toolset | Tool group / permission scope | `toolkit` kind |
| Context file | System prompt fragment / workspace instruction | `context_file` (proposed) |
| Personality | Persona / character card | `personality` (proposed) |
| User Model | User representation / preference model | `user_model` (proposed) |
| Gateway | Multi-platform adapter / message broker | `messaging_gateway` (proposed) |
| Session | Conversation state / thread | `session_state` kind |
| Terminal Backend | Execution environment / runtime | `terminal_backend` (proposed) |
| Nudge | Proactive notification / reminder | `curation_nudge` (proposed) |

## References

- github.com/NousResearch/hermes-agent
- github.com/1ilkhamov/opencode-hermes-multiagent
- agentskills.io (open skill standard)
- Honcho dialectic framework (user modeling)

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 |
| Nucleus | N01 |
| Domain | competitive_intelligence |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_agent]] | sibling | 0.27 |
| [[spec_infinite_bootstrap_loop]] | related | 0.23 |
| [[bld_memory_skill]] | downstream | 0.22 |
| [[agent-builder]] | downstream | 0.22 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.22 |
| [[procedural-memory-builder]] | downstream | 0.22 |
| [[self_audit_n03_builder_20260408]] | sibling | 0.22 |
| [[bld_knowledge_card_procedural_memory]] | sibling | 0.22 |
| [[bld_collaboration_agent]] | downstream | 0.21 |
| [[spec_n07_operational_intelligence]] | downstream | 0.21 |
