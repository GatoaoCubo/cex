---
id: p03_prompt_version
kind: prompt_version
pillar: P03
version: 1.0.0
title: "Template — Prompt Version"
tags: [template, prompt, version, evolution, regression]
tldr: "Tracks prompt evolution with version numbering, change log, A/B test results, and rollback instructions. Prevents prompt regression."
quality: 9.0
domain: "prompt engineering"
density_score: 0.8
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
related:
  - p07_regression_check
  - bld_collaboration_prompt_version
  - bld_knowledge_card_prompt_version
  - prompt-version-builder
  - p01_kc_prompt_version
  - p01_kc_prompt_evolution
  - bld_examples_prompt_version
  - p10_lr_prompt_version_builder
  - kc_model_registry
  - p07_regcheck_latency_baseline
---

# Prompt Version: [PROMPT_ID] v[X.Y.Z]

## Version History

| Version | Date | Change | Impact |
|---------|------|--------|--------|
| 1.0.0 | [YYYY-MM-DD] | Initial release | Baseline |
| 1.1.0 | [YYYY-MM-DD] | [CHANGE_DESCRIPTION] | [METRIC_DELTA] |
| 1.2.0 | [YYYY-MM-DD] | [CHANGE_DESCRIPTION] | [METRIC_DELTA] |

## Current Version: v[X.Y.Z]

### System Prompt
```
[CURRENT_SYSTEM_PROMPT_TEXT]
```

### Key Parameters
| Parameter | Value | Previous | Reason for Change |
|-----------|-------|----------|--------------------|
| temperature | [0.0-1.0] | [PREV] | [WHY] |
| max_tokens | [N] | [PREV] | [WHY] |
| model | [MODEL] | [PREV] | [WHY] |

## Change Log (v[X.Y.Z])
- **What changed**: [DESCRIPTION of prompt modification]
- **Why**: [HYPOTHESIS — what problem this solves]
- **Evidence**: [A/B test results, quality score delta, user feedback]

## Evaluation Metrics

| Metric | v[PREV] | v[CURRENT] | Delta |
|--------|---------|------------|-------|
| Quality score | [N.N] | [N.N] | [+/-] |
| Gate pass rate | [N%] | [N%] | [+/-] |
| Retry rate | [N%] | [N%] | [+/-] |
| Latency (p50) | [Nms] | [Nms] | [+/-] |

## Rollback
If regression detected:
1. Revert to v[PREV]: `git checkout [COMMIT] -- [PROMPT_FILE]`
2. Redeploy: [DEPLOY_COMMAND]
3. Monitor: Check metrics for 24h
4. Document: Add regression note to version history

## Quality Gate
- [ ] Version follows semver (major.minor.patch)
- [ ] Change log explains WHAT and WHY
- [ ] At least 1 metric tracked between versions
- [ ] Rollback procedure documented

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_regression_check]] | downstream | 0.29 |
| [[bld_collaboration_prompt_version]] | downstream | 0.27 |
| [[bld_knowledge_card_prompt_version]] | related | 0.27 |
| [[prompt-version-builder]] | related | 0.25 |
| [[p01_kc_prompt_version]] | related | 0.23 |
| [[p01_kc_prompt_evolution]] | upstream | 0.22 |
| [[bld_examples_prompt_version]] | downstream | 0.22 |
| [[p10_lr_prompt_version_builder]] | downstream | 0.20 |
| [[kc_model_registry]] | upstream | 0.17 |
| [[p07_regcheck_latency_baseline]] | downstream | 0.17 |
