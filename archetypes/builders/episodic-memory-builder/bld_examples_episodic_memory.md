---
kind: examples
id: bld_examples_episodic_memory
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of episodic_memory artifacts
quality: null
title: "Examples Episodic Memory"
version: "1.0.0"
author: n03_builder
tags: [episodic_memory, builder, examples]
tldr: "Golden and anti-examples for episodic_memory construction."
domain: "episodic memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Examples: episodic-memory-builder

## Golden Example
INPUT: "Create episodic memory store for N07 orchestration sessions"
OUTPUT:
```yaml
id: p10_ep_n07_orchestration
kind: episodic_memory
pillar: P10
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
owner: "n07"
episode_schema:
  timestamp: "datetime"
  context: "string"
  mission: "string"
  nuclei_dispatched: "list[string]"
  outcome: "string"
  quality_scores: "list[float]"
  retrieval_keys: "list[string]"
  confidence: "float"
retrieval_method: hybrid
episode_count: 200
decay_policy:
  method: time
  rate: "90 days -- orchestration context stays relevant for 3 months"
retrieval_keys: [mission_name, nucleus, kind, outcome]
index_method: hybrid
promotion_sources: [p10_wm_n07_mission_runner]
quality: null
tags: [episodic_memory, n07, orchestration, P10]
tldr: "N07 orchestration episodic store: 200 episodes, 90-day decay, hybrid retrieval by mission/nucleus/kind."
description: "Episodic store for N07 mission orchestration sessions -- enables recall of past dispatch patterns."
```

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches `^p10_ep_` (H02 pass)
- episode_schema has timestamp + 7 fields (H06 pass)
- retrieval_method: hybrid (H07 pass)
- episode_count: 200 (H08 pass)
- decay_policy declared (H09 pass)
- owner: n07 (H10 pass)

## Anti-Example
BAD OUTPUT:
```yaml
id: n07-history
kind: history
owner: n07
episodes: unlimited
decay: none
quality: 8.0
```
FAILURES:
1. id: "n07-history" has hyphen, no `p10_ep_` prefix -> H02 FAIL
2. kind: "history" not "episodic_memory" -> H04 FAIL
3. quality: 8.0 (not null) -> H05 FAIL
4. episode_schema missing entirely -> H06 FAIL
5. episodes: unlimited -- no count limit -> H08 FAIL
6. decay: none -- no policy -> H09 FAIL
7. Missing retrieval_method, tags, tldr, version, pillar -> H multiple FAIL
