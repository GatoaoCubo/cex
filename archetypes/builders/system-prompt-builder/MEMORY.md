---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: system-prompt-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p03_sp_my_agent not p03_sp_my-agent)
3. rules_count not matching actual numbered rules in body (S03 catches mismatch)
4. Writing generic identity ("helpful assistant") instead of domain-specific persona
5. Mixing task instructions into system_prompt (belongs in action_prompt or instruction)
6. Forgetting knowledge_boundary field (required — what agent does NOT know)
7. Rules as soft guidance ("try to be concise") instead of binary ALWAYS/NEVER
8. Missing ## Output Format section (common omission, S06 catches)

### Effective Patterns
- Opening pattern: "You are {name}, a {domain} specialist." — short, direct
- Rule justification: "ALWAYS X — Y" where Y is <= 10 words
- Boundary statement: "I build X. I do NOT build: A, B, C." — explicit exclusion list
- Knowledge boundary: "Knows: {list}. Does NOT know: {list}." — symmetric pair
- Identity density: 2-4 sentences max (more = less compliance from LLM)

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | generic identity, rule count mismatch, missing boundary |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a system_prompt, update:
- New common mistake (if encountered)
- New effective pattern (if discovered)
- Production counter increment
