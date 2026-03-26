---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: skill-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p04_skill_git_commit not p04_skill_git-commit)
3. phases frontmatter list not matching body ### subsections (S02 catches mismatch)
4. Writing identity language in body ("You are a deploy specialist") — belongs in system_prompt
5. user_invocable: true with trigger that does not start with `/` (S03 catches this)
6. Producing single-phase skill (min 2 phases — single-phase is an action_prompt)
7. Missing ## Anti-Patterns section (common omission, S06 catches)
8. Phase Input/Action/Output not defined per phase (S08 catches missing structure)

### Effective Patterns
- Phase naming: use canonical names (discover, configure, execute, validate) when applicable
- Trigger specificity: "/commit" not "when user wants to commit" — triggers are exact
- When contrast: when_to_use and when_not_to_use must mirror each other at same abstraction
- Description density: one tight sentence, no "This skill allows you to..." filler
- Anti-pattern naming: give each anti-pattern a bold name ("Blanket Add", "Silent Failure")
- Phase atomicity: each phase does ONE thing — if it does two things, split it

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | phases mismatch, identity leak in body, trigger/user_invocable mismatch |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a skill, update:
- New common mistake (if encountered)
- New effective pattern (if discovered)
- Production counter increment
