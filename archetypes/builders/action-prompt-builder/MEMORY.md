---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: action-prompt-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p03_ap_my_task not p03_ap_my-task)
3. Action as noun phrase ("data extraction") instead of verb phrase ("Extract data from")
4. Vague input_required ("some data") instead of typed ("scrape_data: JSON object")
5. Empty edge_cases list (H07 requires >= 2)
6. Including persona text ("You are an expert...") — belongs in system_prompt
7. Writing detailed recipe with prerequisites — that is instruction territory
8. output_expected as vague text ("good results") instead of structured format

### I/O Contract Patterns
- Input table: `| Item | Type | Format | Required |` — structured and scannable
- Output example: include concrete JSON/YAML sample, not just description
- Validation criteria: verifiable checks tied to output fields
- Edge case format: "{{scenario}} -> {{field}}: {{handling}}" (e.g., "Missing price -> price_brl: null")

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | noun-phrase actions, vague I/O, empty edge_cases |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing an action_prompt, update:
- New common mistake (if encountered)
- New I/O contract pattern (if discovered)
- Production counter increment
