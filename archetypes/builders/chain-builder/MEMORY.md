---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: chain-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p03_ch_my_chain not p03_ch_my-chain)
3. steps_count not matching actual numbered steps in body (H08 catches mismatch)
4. Including runtime orchestration (spawns, signals, agents) — belongs in workflow (P12)
5. Missing typed Input/Output on steps (each step needs explicit types)
6. Chain too fine-grained (1 step = 1 purpose, not 1 step = 1 sentence)
7. Confusing chain with chain_of_thought (chain = inter-prompt, CoT = intra-prompt)
8. Missing Data Flow diagram (S04 catches, common omission)

### Pipeline Patterns

| Pattern | Steps | Flow | Use case |
|---------|-------|------|----------|
| Extract-Transform-Load | 3 | sequential | Data processing pipelines |
| Research-Synthesize-Format | 3 | sequential | Knowledge production |
| Classify-Route-Execute | 3 | branching | Intent-based handling |
| Parallel-Merge | 2+ | parallel | Multi-perspective analysis |
| Gather-Filter-Compose | 3 | sequential | Content curation |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | chain vs workflow boundary, step granularity |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a chain, update:
- New common mistake (if encountered)
- New pipeline pattern (if discovered)
- Production counter increment
