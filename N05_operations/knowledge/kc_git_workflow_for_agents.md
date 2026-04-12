---
id: kc_git_workflow_for_agents
kind: knowledge_card
title: "Git Workflow for Autonomous Agents"
version: 1.0.0
quality: null
pillar: P01
language: en
---

# Git Workflow for Autonomous Agents

## Auto-Commits
Autonomous agents should auto-commit changes with:
- Timestamp-based commit messages (`[AUTO] <timestamp>`)
- Hash-based branch tracking (`origin/feature/<hash>`)
- Automatic staging of all modified files

## Branch Strategies
Use feature branches for isolated development:
1. `git checkout -b feature/<purpose>`
2. `git push --set-upstream origin feature/<purpose>`
3. Merge with `git merge --no-ff feature/<purpose>`

## Conflict Resolution
Resolve conflicts using:
1. `git merge --no-ff` for linear history
2. `git merge --no-ff -X recursive` for complex merges
3. Manual resolution with `git mergetool`

## Commit Message Conventions
Follow conventional commits:
```
<type>(<scope>): <description>
<type>: <description>
```
Types: feat, fix, docs, style, refactor, test, chore

## Pre-Commit Hooks
Implement pre-commit checks with:
1. Linting: `husky pre-commit` with ESLint/Prettier
2. Testing: `npm test` integration
3. Type checking: `tsc --noEmit`
4. Code formatting: `prettier --write .`

## Best Practices
1. Use `git rebase -i` for history cleanup
2. Enable `core.autocrlf=true` for cross-platform consistency
3. Configure `user.name` and `user.email` for audit trails
4. Use `git diff` before committing to verify changes
```
```