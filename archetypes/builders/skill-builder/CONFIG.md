---
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: skill Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_skill_{name}.md` | `p04_skill_git_commit.md` |
| Compiled YAML | `p04_skill_{name}.yaml` | `p04_skill_git_commit.yaml` |
| Builder directory | kebab-case | `skill-builder/` |
| Frontmatter fields | snake_case | `user_invocable`, `when_to_use` |
| Skill name slug | snake_case, lowercase | `git_commit`, `deploy_railway` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/P04_tools/examples/p04_skill_{name}.md`
- Compiled: `cex/P04_tools/compiled/p04_skill_{name}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 5120 bytes
- Total (frontmatter + body): ~6500 bytes
- Density: >= 0.80

## Phase Count

| Count | Status | Notes |
|-------|--------|-------|
| 1 | INVALID | Single-phase is an action_prompt, not a skill |
| 2-3 | MINIMAL | Acceptable for simple capabilities |
| 4 | CANONICAL | discover + configure + execute + validate |
| 5-6 | EXTENDED | Valid for complex skills with sub-phases |
| 7+ | REJECT | Split into sub_skills |

## Trigger Convention

| Type | Format | user_invocable |
|------|--------|---------------|
| Slash command | `/verb` or `/verb-noun` | true |
| Keyword | `"keyword phrase"` | false |
| Event | `on_{event_name}` | false |
| Agent call | `skill:{id}` | false |

## Boolean Fields
- user_invocable: true ONLY when trigger is a slash command starting with `/`
- user_invocable: false for all agent-only, event-driven, or keyword triggers

## Body Section Requirements
- Purpose: 2-4 sentences, must state WHY skill exists vs action_prompt
- Workflow Phases: one ### subsection per phase, each with Input/Action/Output
- Anti-Patterns: >= 3 named failures with avoidance strategy
- Metrics: >= 2 measurable success criteria with target values
