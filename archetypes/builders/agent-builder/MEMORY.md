---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: agent-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any non-null value)
2. Using hyphens in id slug (must be underscores: p02_agent_my_agent not p02_agent_my-agent)
3. Omitting satellite field or setting to "none" (must be real satellite name or "agnostic")
4. Writing vague capabilities ("can help with tasks") instead of concrete scoped bullets
5. Forgetting iso_vectorstore section or listing fewer than 10 ISO files
6. Setting llm_function to anything other than BECOME (agent is identity, not callable)
7. capabilities_count not matching actual bullets in Architecture section
8. Mixing in system_prompt content (rules, ALWAYS/NEVER) — that belongs in system-prompt-builder
9. Omitting "NOT when" exclusions in When to Use section (mandatory boundary discipline)
10. ISO file naming errors: using kebab-case or wrong separator (must be SCREAMING_SNAKE + underscores)

### Effective Patterns
- Opening overview: "X is a {satellite} specialist in {domain}." — direct, assigns identity
- Capabilities: start each bullet with an action verb (Produce, Validate, Detect, Convert)
- ISO listing: use full path with agents/{slug}/iso_vectorstore/ prefix for clarity
- Boundary in When to Use: "NOT when: {exclusion}" — explicit beats implicit
- Satellite assignment: when unsure, use "agnostic" — never leave blank
- tools_count: count only concrete tools (brain_query, validate_artifact) — not concepts

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | vague capabilities, missing iso_vectorstore, satellite blank |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing an agent artifact, update:
- New common mistake (if encountered)
- New effective pattern (if discovered)
- Production counter increment
