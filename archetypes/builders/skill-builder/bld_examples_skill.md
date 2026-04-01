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