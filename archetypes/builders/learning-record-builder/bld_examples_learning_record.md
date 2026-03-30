---
kind: examples
id: bld_examples_learning_record
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of learning_record artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: learning-record-builder
## Golden Example
INPUT: "Document the learning from continuous batching achieving 1.6x speedup with 3 agent_nodes"
OUTPUT:
```yaml
id: p10_lr_continuous_batching_speedup
kind: learning_record
pillar: P10
version: "1.0.0"
created: "2026-03-05"
updated: "2026-03-05"
author: "builder"
domain: "orchestration"
quality: null
tags: [learning, continuous-batching, speedup, orchestration, multi-agent_node]
tldr: "Continuous batching with 3 sats achieved 1.6x speedup; task complexity drives speed, not model tier"
topic: "Continuous batching multi-agent_node performance"
outcome: SUCCESS
score: 9.0
context: "ISOFIX mission, 7 batches across researcher+builder+knowledge-engine, 2026-03-05"
agent_node: "orchestrator"
reproducibility: HIGH
impact: "1.6x throughput increase, zero git lock contention at 3 agent_nodes"
timestamp: "2026-03-05T14:30:00Z"
dependencies: []
keywords: [batching, parallel, throughput, spawn, grid]
linked_artifacts:
  primary: null
  related: [p12_spawn_grid, p08_pat_continuous_batching]
```
## Summary
Continuous batching with 3 agent_nodes (researcher+builder+knowledge-engine) achieved 1.6x speedup over sequential execution. Speed was driven by task complexity, not model tier — opus finished faster than sonnet on simpler tasks. Zero git lock contention observed.
## Pattern
- Use spawn_grid.ps1 with -mode continuous for >6 tasks
- Name handoffs as {MISSION}_batch_{N}_{DOMAIN}.md for queue management
- Limit to 3 concurrent agent_nodes (RAM ceiling at 4+)
- Let queue auto-refill slots as agent_nodes complete
## Anti-Pattern
- Running >3 agent_nodes causes BSOD risk (RAM exhaustion)
- Assuming opus is slower than sonnet — speed depends on task, not model
- Manual slot management instead of auto-refill wastes idle time
## Context
- Environment: Windows 10 Pro, 32GB RAM, 3 Claude Code terminals
- Satellite: orchestrator orchestrating researcher+builder+knowledge-engine
- Timing: 2026-03-05, ISOFIX mission, 7 sequential batches
- Constraints: max 3 terminals (BSOD prevention), 5s spawn delay
## Impact
- 1.6x throughput vs sequential single-agent_node execution
- Zero git lock contention across 3 concurrent committers
- Queue auto-refill eliminated idle time between waves
## Reproducibility
- Conditions: 3 agent_nodes, >6 tasks, independent work units
- Confidence: HIGH (tested on ISOFIX 7/7 and CBTEST mixed)
- Caveats: tasks must be independent; shared file edits cause conflicts
## References
- records/skills/continuous_batching/SKILL.md
- spawn_grid.ps1 -mode continuous
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p10_lr_ pattern (H02 pass)
- kind: learning_record (H04 pass)
- 22 fields present including all 15 required (H06 pass)
- outcome: SUCCESS (H09 pass, enum valid)
- score: 9.0 (S02 pass, float in range)
- Pattern has 4 concrete steps (S03 pass)
- Anti-Pattern has 3 specific failures (S04 pass)
- All 7 body sections present (S08 pass)
- density high, no filler (S09 pass)
## Anti-Example
INPUT: "Document what we learned about batching"
BAD OUTPUT:
```yaml
id: batching_learning
kind: learning
quality: 8.5
topic: batching
outcome: good
score: "high"
tags: batching
We learned a lot about batching. It was really useful and helped us be more productive.
Overall, the experience was positive and we recommend using it in the future.
In summary, batching works well when done correctly.
```
FAILURES:
1. id: no `p10_lr_` prefix -> H02 FAIL
2. kind: "learning" not "learning_record" -> H04 FAIL
3. quality: 8.5 (self-assigned) -> H05 FAIL
4. outcome: "good" not in enum [SUCCESS, PARTIAL, FAILURE] -> H09 FAIL
5. score: "high" is string not float -> S02 FAIL
6. tags: string not list -> H07 FAIL
7. Missing required fields: pillar, version, created, updated, author, domain, context, tldr -> H06 FAIL
