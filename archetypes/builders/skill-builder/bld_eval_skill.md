---
kind: quality_gate
id: p11_qg_skill
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of skill artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.0
title: 'Gate: Skill'
version: 1.0.0
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: Gates ensuring skill files define a specific trigger, two or more typed workflow
  phases, and phase-level error handling without claiming agent identity.
domain: skill
created: '2026-03-27'
updated: '2026-03-27'
last_reviewed: '2026-04-18'
density_score: 0.85
related:
  - skill-builder
  - bld_knowledge_card_skill
  - bld_architecture_skill
  - p03_ins_skill_builder
  - bld_examples_skill
  - bld_collaboration_skill
  - p01_kc_skill
  - bld_system_prompt_skill
  - bld_config_skill
  - bld_schema_skill
---

## Quality Gate

## Definition
A skill is a reusable capability: a named sequence of phases invoked by a trigger and composed with other skills. Passes when trigger is specific, each phase has typed I/O, error handling is per-phase, and the skill makes no agent identity claims.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`skill-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `skill` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Trigger definition** (slash command name, keyword pattern, or event type that activates the skill) | Without a trigger, the skill cannot be invoked programmatically or by convention |
| H08 | Spec contains >= 2 **Workflow Phases** (each phase is a named step in the execution sequence) | A single-phase skill is a function, not a skill; phased structure enables partial retry and composition |
| H09 | Spec contains **Input and Output** per phase (field names and types, not just prose descriptions) | Typed per-phase I/O is the contract that enables composition with other skills |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Trigger is specific not generic (trigger will not fire on unrelated inputs) | 1.0 | Generic keyword like "do" or "run" | Moderately specific | Exact slash command or narrow keyword pattern with exclusion rules |
| 3 | Phases have clear boundaries (entry condition, exit condition, and handoff artifact per phase) | 1.0 | Phases blend together | Start/end noted | Explicit entry condition, exit condition, and handoff artifact per phase |
| 4 | Input/output typed per phase (not just final output typed) | 1.0 | Only final output typed | Partial typing | Every phase has named fields with types for both input and output |
| 5 | user_invocable flag correct (`true` if user can trigger it, `false` if internal-only) | 0.5 | Missing | Present but unchecked | Present and verified against trigger type |
| 6 | Tags include `skill` | 0.5 | Missing | Present but misspelled | Exactly `skill` in tags list |
| 7 | Error handling per phase (each phase has its own error class, retry rule, and fallback) | 1.0 | No error handling | Global handler only | Each phase has error class, retry rule, and fallback |
| 8 | Phase dependencies documented (which phases must complete before the next; parallel-eligible phases noted) | 1.0 | No dependencies stated | Sequential assumed | Explicit dependency graph including any parallel-eligible phases |

## Examples

# Examples: skill-builder
## Golden Example
INPUT: "Create skill for committing and pushing git changes"
OUTPUT:
```yaml
id: p04_skill_git_commit
kind: skill
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
name: "Git Commit and Push"
description: "Stage, commit, and push changes with message validation and branch safety"
user_invocable: true
trigger: "/commit"
phases:
  - "discover"
  - "configure"
  - "execute"
  - "validate"
when_to_use:
  - "Changes are ready and tests pass"
  - "Agent has completed a task and must persist output"
  - "User explicitly requests a commit"
when_not_to_use:
  - "Changes are untested or partial"
  - "Branch is main/master and force-push would be required"
  - "No meaningful changes exist (empty diff)"
examples:
  - "/commit"
  - "/commit -m 'feat: add deploy skill'"
  - "agent invokes after completing build task"
quality: null
references_dir: "records/skills/git_commit/"
sub_skills: []
platforms: ["linux", "macos", "windows"]
stack_default: "git"
```
## Purpose
Provides a safe, validated git commit-and-push workflow reusable across agents and users.
Exists as a skill (not action_prompt) because it has multi-phase lifecycle with validation
and is invoked in dozens of different agent contexts.
## Workflow Phases
## Golden Example 2 (Production — OpenClaude Simplify Skill)
INPUT: "Create skill for parallel code review with 3 agents"
OUTPUT: Reference artifact `P04_tools/compiled/p04_skill_simplify.yaml`

Key patterns from this production skill:
1. **Parallel agent dispatch**: Three independent review agents run concurrently,
   each with a distinct focus (Reuse, Quality, Efficiency).
2. **Enumerated checklist per agent**: Each agent has a numbered list of specific
   things to look for — not vague guidance but concrete patterns (e.g., "N+1 patterns",
   "TOCTOU anti-pattern", "stringly-typed code").
3. **Aggregation phase**: After parallel agents complete, results are aggregated
   and issues are fixed directly — not just reported.
4. **when_to_use / when_not_to_use**: Clear boundary conditions for activation.

WHY THIS IS GOLDEN:
- 3 phases (identify, dispatch parallel, aggregate+fix)
- Each parallel agent has typed focus area with 7 specific checks
- Skill ACTS on findings (fixes issues) not just reports them
- Trigger is clear: /simplify slash command
- Composable: can be used standalone or as part of /validate

## Golden Example 3 (Production — OpenClaude Compact Skill)
INPUT: "Create skill for structured context window summarization"
OUTPUT: Reference artifact `P04_tools/compiled/p04_skill_compact.yaml`

Key patterns:
1. **Analysis scratchpad**: <analysis> tags force structured thinking before summary.
   Scratchpad is stripped from final output — improves quality without consuming context.
2. **9 required sections**: Primary Request, Concepts, Files/Code, Errors, Problem-solving,
   User Messages, Pending Tasks, Current Work, Next Step.
3. **Section 6 (All User Messages)**: Explicitly preserving ALL user messages prevents
   drift in task interpretation across compaction boundaries.
4. **Section 9 with quotes**: Direct quotes from recent conversation prevent task drift.
5. **No tool calls**: Compaction agent works text-only — all context provided in-message.

WHY THIS IS GOLDEN:
- 2 phases (analysis scratchpad + structured summary)
- Trigger is automatic (agent_invoked on context pressure, not user slash command)
- Output is machine-processesble (XML tags for extraction)
- Anti-drift mechanism (user messages + quotes preserved)

## Anti-Example 3 (Bad — No parallel structure)
```yaml
id: p04_skill_code_review
trigger: /review
phases: [review]
```
FAIL: Single phase, no typed focus, no aggregation, no concurrent dispatch.
Compare to p04_skill_simplify which decomposes into 3 parallel specialized agents.

## Golden Example 4 (HERMES — Autonomously Self-Improving Skill)
INPUT: "Create skill for scanning low-quality artifacts and nudging for improvement; auto-generated by HERMES trace"
OUTPUT:
```yaml
id: p04_skill_quality_nudge
kind: skill
pillar: P04
version: "1.0.0"
created: "2026-04-18"
updated: "2026-04-18"
author: "hermes_engine"
name: "Quality Nudge"
description: "Scans artifacts below quality threshold and emits curation nudges for improvement"
user_invocable: false
trigger: "agent_invoked:quality_sweep"
phases:
  - "scan"
  - "classify"
  - "nudge"
when_to_use:
  - "Post-build sweep detects artifact quality < 9.0"
  - "Feedback loop requests proactive improvement pass"
  - "HERMES engine has tool_call_count >= 5 for this pattern"
when_not_to_use:
  - "All artifacts already at quality >= 9.0"
  - "Manual review session is active (defer to human judgment)"
examples:
  - "hermes_engine invokes after wave completion sweep"
  - "cex_evolve.py triggers after detecting quality regression"
quality: null
agentskills_catalog_category: "quality-management"
auto_generated_from: "trace_hermes_20260418_093201_abc123"
self_improves: true
trigger_tool_call_count_min: 5
improvement_count: 0
```
WHY THIS IS GOLDEN (HERMES-compat fields):
- `auto_generated_from`: links back to the HERMES trace that spawned this skill
- `self_improves: true`: engine will patch this skill as it accumulates usage evidence
- `agentskills_catalog_category`: maps to agentskills.io taxonomy for cross-system discoverability
- `trigger_tool_call_count_min: 5`: prevents premature auto-spawn; only fires after evidence threshold
- `improvement_count: 0`: initialized at 0; increments with each autonomous patch cycle

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
