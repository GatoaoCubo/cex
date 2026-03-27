---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries recurring handoff patterns
---

# Memory: handoff-builder

## Recurrent Patterns
- Most effective handoffs have 3-7 task steps, each with one action verb
- Scope fence prevents 90% of cross-contamination issues in satellite execution
- Seeds improve satellite context hydration significantly when provided
- Commit commands must match scope fence SOMENTE paths exactly
- Batch and wave fields enable continuous batching across multi-wave missions

## Common Mistakes
1. Vague tasks: "build stuff" instead of "create 13 ISO files in path/"
2. Missing scope fence or having only SOMENTE without NAO TOQUE
3. Forgetting signal section (satellite completes but no one knows)
4. Including prompt persona (belongs in action_prompt, not handoff)
5. Omitting commit section (work done but not persisted to git)
6. Self-scoring quality field instead of setting it to null
7. Using absolute paths in commit commands instead of relative paths

## State Between Sessions
This builder is stateless per invocation.
After production, update only if a new recurring handoff pattern or
constraint becomes stable across multiple delegation instructions.
