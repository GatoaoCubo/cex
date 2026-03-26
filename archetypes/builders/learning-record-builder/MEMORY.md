---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: learning-record-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p10_lr_my_topic not p10_lr_my-topic)
3. outcome "good" or "bad" instead of enum SUCCESS/PARTIAL/FAILURE
4. score as string "8.5" instead of float 8.5
5. Pattern section with vague advice ("be careful") instead of concrete steps
6. Anti-pattern section missing — both sides always required
7. Confusing with knowledge_card — ask "is this from experience or research?"
8. Missing context: when/where/which satellite

### Learning Domain Patterns

| Domain | Common outcomes | Key friction |
|--------|----------------|-------------|
| Orchestration | Speedup metrics, contention results | Quantifying parallel gains |
| Build | Success/failure rates, iteration counts | Separating build failure from design failure |
| Research | Source quality, coverage completeness | Measuring research thoroughness |
| Deploy | Uptime, rollback frequency | Attributing cause to correct layer |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | outcome classification, pattern concreteness |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a learning_record, update:
- New common mistake (if encountered)
- New domain pattern (if discovered)
- Production counter increment
