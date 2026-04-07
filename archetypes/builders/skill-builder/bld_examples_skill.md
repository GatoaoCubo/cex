---
kind: examples
id: bld_examples_skill
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of skill artifacts
pattern: few-shot learning — LLM reads these before producing
---

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
