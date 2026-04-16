---
kind: config
id: bld_config_press_release
pillar: P09
llm_function: CONSTRAIN
purpose: Runtime configuration for the press_release builder including naming, paths, limits, and hooks
quality: 9.1
title: "Press Release Builder Config"
version: "1.0.0"
author: n02_wave6
tags: [press_release, builder, config]
tldr: "Naming convention, artifact paths, byte/turn limits, and hook configuration for press_release builder"
domain: "press_release construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention

| Property | Value |
|---|---|
| Pattern | p05_pr_{{name}}.md |
| Pillar prefix | p05 |
| Kind segment | pr |
| Name segment | lowercase, underscores, alphanumeric only |
| Extension | .md |

### Examples

| Announcement type | Filename |
|---|---|
| SaaS product launch | p05_pr_saas_launch_q2_2026.md |
| Series A funding | p05_pr_series_a_funding.md |
| Executive appointment | p05_pr_coo_appointment_jane_doe.md |
| Partnership announcement | p05_pr_partnership_acme_beta.md |
| Award recognition | p05_pr_gartner_cool_vendor_2026.md |

### Invalid filenames

| Invalid | Reason |
|---|---|
| pr_launch.md | Missing p05 pillar prefix |
| p05_saas_launch.md | Missing "pr_" kind segment |
| p05_pr_SaaS_Launch.md | Uppercase letters not permitted |
| p05_pr_launch.docx | Wrong extension (must be .md) |

## Paths

| Path | Purpose |
|---|---|
| /artifacts/p05/press_releases/ | Primary artifact storage |
| /archetypes/builders/press-release-builder/ | Builder ISOs (this directory) |
| /archetypes/builders/compiled/ | Compiled YAML versions |
| /.cex/cache/press_release/ | Prompt cache for builder context |

## Limits

| Parameter | Value | Reason |
|---|---|---|
| max_bytes | 4096 | Wire service submission limits; boilerplate constraint |
| max_turns | 5 | Research (1) + compose (2) + validate (1) + revise (1) |
| effort_level | 3 | Medium-high effort: AP compliance requires attention |
| min_words | 300 | Minimum body content for journalist credibility |
| max_words | 500 | Wire service attention span; enforced at D01 soft scoring |
| max_headline_chars | 80 | H04 hard gate; email subject line compatibility |
| max_lede_words | 35 | H06 hard gate; AP style lede convention |

## Hooks

| Hook | Value | Notes |
|---|---|---|
| pre_build | null | No pre-build action required |
| post_build | cex_compile.py | Compile .md to .yaml after save |
| on_error | null | Errors surface to user; no auto-recovery |
| on_quality_fail | return_to_f6 | If score < 7.0, return to PRODUCE phase (max 2 retries) |
| on_embargo_present | log_embargo_date | Log embargo date to .cex/runtime/embargoes.log |

## Embargo Log Format

When an embargo date is present, append the following record to
`.cex/runtime/embargoes.log` at build time:

```
{artifact_id} | {embargo_date} | {embargo_time} | {embargo_timezone} | built:{created}
```

Example:
```
p05_pr_series_a_funding | 2026-04-21 | 09:00 | EDT | built:2026-04-14
```

This allows N07 to monitor upcoming embargo lifts and trigger distribution
workflows automatically.
