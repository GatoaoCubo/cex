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
### Phase 1: discover
**Input**: working directory, optional commit message flag
**Action**: run `git status` and `git diff` to inspect staged/unstaged changes
**Output**: change summary, list of modified files, current branch name
### Phase 2: configure
**Input**: change summary, branch name, optional -m flag
**Action**: validate branch not protected, draft commit message if not provided, check for secrets in diff
**Output**: validated commit message, confirmed safe branch, staged file list
### Phase 3: execute
**Input**: validated commit message, staged file list
**Action**: run `git add` for specific files, run `git commit -m`, run `git push`
**Output**: commit SHA, push confirmation, remote URL
### Phase 4: validate
**Input**: commit SHA, push output
**Action**: verify commit appears in `git log`, verify remote reflects push
**Output**: success signal with SHA, or error signal with failure reason
## Anti-Patterns
- **Blanket add**: `git add -A` or `git add .` without reviewing files — may include secrets or binaries
- **Force push to main**: never use `--force` on protected branches — check branch name first
- **Silent failure**: swallowing push errors without signaling — always emit error signal on failure
## Metrics
- Commit success rate: >= 98% of invocations result in committed SHA
- Secret leak rate: 0% (configure phase must detect secrets before execute)
- Phase duration: discover < 2s, configure < 1s, execute < 5s, validate < 2s
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_skill_ pattern (H02 pass)
- kind: skill (H04 pass)
- 19 required+optional fields present (H06 pass)
- body has Purpose + Workflow Phases + Anti-Patterns + Metrics (H07 pass)
- phases list matches 4 body subsections exactly (H08 pass)
- user_invocable: true with trigger "/commit" (S03 pass)
- when_to_use and when_not_to_use parallel structure (S04 pass)
- No identity language in body (S05 pass)
- 3 anti-patterns named with avoidance (S06 pass)
- 3 metrics with measurable targets (S07 pass)
- description <= 120 chars (S01 pass)
## Anti-Example
INPUT: "Create skill for deploying code"
BAD OUTPUT:
```yaml
id: deploy_skill
kind: tool
pillar: tools
name: Deploy
trigger: deploy
quality: 8.0
```
You are a deploy specialist. You deploy code to production.
Run the deploy command when asked.
FAILURES:
1. id: no `p04_skill_` prefix, uses hyphen — H02 FAIL
2. kind: "tool" not "skill" — H04 FAIL
3. pillar: "tools" not "P04" — H06 FAIL
4. quality: 8.0 (not null) — H05 FAIL
