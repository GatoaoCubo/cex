---
id: bld_memory_canary_config
kind: knowledge_card
pillar: P10
title: "Memory: canary_config Builder Patterns"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: canary_config
quality: 8.1
tags: [memory, canary_config, P09, builder, progressive_delivery]
llm_function: INJECT
tldr: "Recalled patterns and corrections for canary_config builder sessions."
density_score: 0.87
related:
  - p01_kc_cicd_llm_pipeline
  - bld_architecture_feature_flag
  - bld_architecture_canary_config
  - bld_knowledge_canary_config
  - bld_model_canary_config
  - bld_prompt_canary_config
  - bld_schema_canary_config
  - bld_config_canary_config
  - bld_memory_feature_flag
  - bld_memory_ab_test_config
---

# Memory: canary_config Builder

## Persistent Patterns
| Pattern | Frequency | Note |
|---------|-----------|------|
| Start with 5% or less initial traffic | HIGH | Risk management |
| Always define rollback trigger | HIGH | Gate H07 |
| stages_count must match list | HIGH | Gate H06 |
| Last stage must be 100% | HIGH | Completion gate H08 |

## Common Corrections
| Mistake | Correction |
|---------|-----------|
| User conflates with feature_flag | Teach: feature_flag is boolean; canary is traffic % |
| User conflates with ab_test_config | Teach: A/B uses statistics; canary uses metric threshold |
| User starts at 50% | Redirect: start at 5%; risk is proportional to traffic exposed |
| No rollback trigger | Block: add error_rate or latency threshold |
| Provider not specified | Default to argo_rollouts; ask user to confirm |

## Memory Persistence Checklist

- Verify memory type matches taxonomy (entity, episodic, procedural, working)
- Validate retention policy aligns with data lifecycle rules
- Cross-reference with memory_scope for boundary correctness
- Check for stale entries that need decay or pruning

## Memory Pattern

```yaml
# Memory lifecycle
type: classified
retention: defined
scope: bounded
decay: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_memory_update.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cicd_llm_pipeline]] | sibling | 0.21 |
| [[bld_architecture_feature_flag]] | upstream | 0.16 |
