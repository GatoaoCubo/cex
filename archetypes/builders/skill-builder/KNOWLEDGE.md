---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for skill production
sources: CEX schema, CODEXA skill corpus (118+ skills), LangChain tools, ReAct pattern
---

# Domain Knowledge: skill

## Foundational Concept
A skill is a reusable, phase-structured capability that an agent or user invokes via a
defined trigger. Unlike an agent (which has identity/persona) or an action_prompt (which
is just text), a skill has explicit lifecycle phases — each with named input, action, and
output — making it composable, testable, and auditable. Skills are the MOST NUMEROUS
artifact type in mature agentic systems (118+ in CODEXA alone).

## Skill vs Adjacent Types

| Type | Has identity | Has phases | Has trigger | When to use |
|------|-------------|------------|-------------|-------------|
| skill (P04) | NO | YES | YES | Reusable capability, structured workflow |
| agent (P02) | YES | NO | NO | Full persona with tools and routing |
| action_prompt (P03) | NO | NO | YES | Single-shot prompt with no internal structure |
| component (P04) | NO | NO | NO | Atomic pipeline block, no lifecycle |
| hook (P04) | NO | NO | event | Single pre/post event handler |

Rule: "does it need multiple steps with named boundaries and reuse across agents?" -> skill.

## Lifecycle Phases Pattern
The canonical skill lifecycle has 4 named phases:

| Phase | Purpose | What happens |
|-------|---------|-------------|
| discover | Find relevant context | Query brain, read files, gather inputs |
| configure | Set parameters | Validate inputs, apply defaults, check constraints |
| execute | Do the work | Core logic: transform, produce, call tools |
| validate | Verify output | Quality check, gate pass/fail, signal result |

Not all skills need all 4 phases. Minimum: 2 phases. Maximum: 6 phases.

## Trigger Patterns

| Pattern | user_invocable | Example |
|---------|---------------|---------|
| slash command | true | `/commit`, `/review-pr`, `/ship` |
| keyword match | false | "when agent detects X" |
| event-driven | false | "on file_write complete" |
| agent-invoked | false | `skill.execute("p04_skill_deploy")` |

Rule: user_invocable: true REQUIRES trigger to start with `/`.

## CEX-Specific Constraints
- id must match `^p04_skill_[a-z][a-z0-9_]+$`
- phases list in frontmatter MUST match `## Workflow Phases` subsections in body
- max_bytes: 5120 — skills are operational tools, not documentation
- quality: null (never self-score)
- No persona language in body ("You are", "I will") — skills are capability, not identity

## Anti-Patterns in Production
- **Phase soup**: phases with overlapping responsibilities — split into atomic phases
- **Identity leak**: writing "You are a deploy specialist" in skill body — that belongs in system_prompt
- **Trigger ambiguity**: trigger: "when needed" — triggers must be specific and unambiguous
- **No anti-patterns section**: every skill must document what NOT to do
- **God skill**: one skill doing 8 unrelated things — split into sub_skills

## References
- CODEXA skill corpus: `records/skills/*/SKILL.md` (118 skills)
- P04 schema: `P04_tools/_schema.yaml`
- ReAct pattern: Yao et al. 2022 (reason + act cycles map to skill phases)
- LangChain Tools: structured tool definition with name + description + run()
