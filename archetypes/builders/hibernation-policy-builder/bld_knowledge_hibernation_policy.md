---
kind: knowledge_card
id: bld_knowledge_card_hibernation_policy
pillar: P01
llm_function: INJECT
purpose: Linked KC pointer for hibernation_policy builder
quality: 8.0
title: "Knowledge Card Link: hibernation_policy"
version: "1.0.0"
author: n03_engineering
tags: [hibernation_policy, builder, knowledge_card]
tldr: "Linked KC pointer for hibernation_policy builder"
domain: "hibernation_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_instruction_kind
  - bld_architecture_hibernation_policy
  - bld_model_hibernation_policy
  - bld_schema_hibernation_policy
  - bld_memory_hibernation_policy
  - bld_prompt_hibernation_policy
  - bld_eval_hibernation_policy
  - bld_config_hibernation_policy
  - bld_tools_hibernation_policy
  - bld_output_hibernation_policy
---

## Primary KC
`N00_genesis/P01_knowledge/library/kind/kc_hibernation_policy.md`

Covers: idle trigger types, wake conditions, state persistence settings, backend support matrix, cost savings patterns, boundary vs related kinds.

## Related KCs to Inject at F3
| KC | Why |
|----|-----|
| `kc_terminal_backend.md` | Sibling kind -- understand WHERE code runs before declaring WHEN it sleeps |
| `kc_runtime_rule.md` | Understand active-session timeout boundary to avoid conflation |
| `kc_cost_budget.md` | Understand spend-cap boundary to avoid conflation |
| `kc_rate_limit_config.md` | Understand throughput-limit boundary to avoid conflation |

## Domain Background

| Concept | Definition | Distinction from hibernation |
|---------|-----------|------------------------------|
| Hibernation | Voluntary suspension with preserved state, on-demand wake | -- (this kind) |
| Auto-scaling | Adjust instance count based on load | Still paying for active instances |
| Spot termination | Involuntary reclamation by cloud provider | No preserved state, no voluntary |
| TTL expiry | Destroy workload after maximum age | Destruction, not suspension |

CEX hibernation_policy describes the "sleeping agent" pattern central to the HERMES serverless cost model.

## Knowledge Injection Checklist

- Verify domain facts are sourced and citable
- Validate density_score >= 0.85 (no filler content)
- Cross-reference with related KCs for consistency
- Check for outdated facts that need refresh

## Injection Pattern

```yaml
# KC injection at F3
source: verified
density: 0.85+
cross_refs: checked
freshness: current
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_retriever.py --query "{DOMAIN}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_kind]] | downstream | 0.19 |
