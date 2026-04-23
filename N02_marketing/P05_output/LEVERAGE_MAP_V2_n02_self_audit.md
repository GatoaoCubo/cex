---
id: n02_leverage_map_v2_self_audit
kind: verification_report
pillar: P12
title: "N02 Marketing - LEVERAGE_MAP_V2 Self Audit"
mission: LEVERAGE_MAP_V2
nucleus: n02
date: 2026-04-15T21:35:00Z
quality: 9.0
version: 3.0
status: complete
density_score: 0.94
related:
  - n02_leverage_map_v2_codex_verification
  - n02_leverage_map_v2_verification
  - n02_leverage_map_v2_iteration2
  - n02_dr_social_publisher
  - bld_collaboration_social_publisher
  - cross_nucleus_handoffs
  - n02_self_review_2026-04-02
  - n02_tool_social_publisher
  - p12_wf_visual_frontend_marketing
  - p03_sp_social_publisher_builder
---

# N02 Marketing - LEVERAGE_MAP_V2 Self Audit

## Executive Summary

`_tools/cex_social_publisher.py` is real, small, and immediately useful for N02. It closes the narrow gap of platform-sized copy formatting for X, LinkedIn, Instagram, Threads, Bluesky, and Mastodon. It does not close autonomous publishing, measurement, or optimization.

The broader N02 stack is more wired than the raw tool suggests:

- routing and social-publishing docs already exist
- the N02 social publishing knowledge card exists
- workflow docs reference scheduled publishing and analytics checkpoints

Even with that surrounding wiring, the live executable gap remains: N02 can format posts, but still cannot run a closed-loop marketing system.

## 8F Pipeline

```text
F1 CONSTRAIN: mission=LEVERAGE_MAP_V2, nucleus=n02, scope=_tools social publisher sufficiency
F2 BECOME: loaded N02 marketing rules, agent card, ASCII rule, orchestrator rules
F3 INJECT: handoff, CLAUDE.md, existing LEVERAGE_MAP reports, N02 social-publishing docs, live _tools scan
F4 REASON: verify tool presence, inspect API, test behavior, compare against missing-capability map
F5 CALL: read files, rg scans, live formatter execution, compile, git, signal
F6 PRODUCE: canonical self-audit report with sufficiency verdict and next-build ranking
F7 GOVERN: checked tool surface, live output, and surrounding docs for overclaim risk
F8 COLLABORATE: save, compile, commit, signal completion
```

## Verification

### Tool Confirmed

Present in `_tools`:

- `_tools/cex_social_publisher.py`

Observed API:

- `--input`
- `--stdin`
- `--platforms`
- `--json`

Observed behavior:

- truncates or formats copy per platform limit
- extracts hashtags with regex
- returns per-platform JSON or human-readable output
- uses stdlib only

### API Fit For N02

Good fit:

- platform-sized copy generation
- character limit enforcement
- lightweight distribution handoff
- JSON output for downstream tooling

Not covered:

- platform API publishing
- scheduling
- engagement measurement
- A/B testing
- image generation

### Live Check

A sample stdin run succeeded, but PowerShell here-string input introduced a leading BOM marker in the returned `content` field (`\ufeff`). That is a real integration edge case for stdin mode on Windows. File-based input is cleaner; stdin should be normalized before production use.

## New Wired Tools Since V1

### Executable

| Item | Status | Notes |
|------|--------|------|
| `_tools/cex_social_publisher.py` | Wired | New formatter for platform-sized social copy |

### Supporting Wiring

| Item | Status | Notes |
|------|--------|------|
| `N02_marketing/P04_tools/social_publisher_marketing.md` | Wired | Documents a fuller social publishing workflow |
| `N02_marketing/P01_knowledge/knowledge_card_social_publishing.md` | Wired | Captures the social publishing domain model |
| `N02_marketing/P12_orchestration/dispatch_rule_social_publisher.md` | Wired | Routes social publishing work into N02 |
| `_tools/cex_8f_motor.py` | Wired | Maps `social_publisher` intent into the N02 call path |
| `_tools/cex_schema_hydrate.py` | Wired | Includes `social-publisher-builder` metadata |

### Interpretation

The repo now has both the formatter and the surrounding domain wiring. That is useful, but it is still not the same as an end-to-end publisher with scheduling, analytics, and optimization loops.

## Still Missing

### 1. A/B Test Harness

Status: not implemented as a live tool.

Why it matters:

- N02 can produce variants, but cannot automatically compare them
- without a harness, copy improvement stays manual

### 2. Analytics Aggregator

Status: not implemented as a live tool.

Why it matters:

- no unified publish -> measure -> improve loop
- platform dashboards remain external and manual

### 3. Campaign Scheduler

Status: not implemented as a live tool.

Why it matters:

- workflows and docs already describe scheduling
- the runtime tool that automates timing and dispatch is still missing

### 4. Image Generation Wrapper

Status: not implemented as a live tool.

Why it matters:

- visual channels still need manual or external design support
- Instagram and similar channels lose leverage without visual generation

## Next Iteration

Top 3 next builds for N02, prioritized:

1. `cex_ab_test_harness.py`
   - highest leverage
   - no external API dependency for an initial local version
   - unlocks copy optimization

2. `cex_analytics_aggregator.py`
   - makes performance visible
   - turns publishing into a feedback loop

3. `image_generation_wrapper.py`
   - unlocks visual campaigns
   - especially important for Instagram and short-form social

If scheduler is the next operational dependency, it follows after measurement is in place. The stack should not automate timing before it can measure results.

## Evidence Snapshot

- `_tools/cex_social_publisher.py` exists and executes
- JSON output works for multiple platforms
- platform limits are enforced
- surrounding N02 docs and routing files are present
- no live scheduler, A/B harness, or analytics tool was found in `_tools`

## Final Assessment

`cex_social_publisher.py` is sufficient for platform-sized copy formatting and insufficient for autonomous marketing operations.

Net change from the previous cycle:

- formatter gap is closed
- routing and social-publishing docs are coherent
- the main leverage gaps remain testing, analytics, scheduling, and visual generation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n02_leverage_map_v2_codex_verification]] | sibling | 0.68 |
| [[n02_leverage_map_v2_verification]] | upstream | 0.47 |
| [[n02_leverage_map_v2_iteration2]] | sibling | 0.40 |
| [[n02_dr_social_publisher]] | related | 0.36 |
| [[bld_collaboration_social_publisher]] | related | 0.32 |
| [[cross_nucleus_handoffs]] | related | 0.27 |
| [[n02_self_review_2026-04-02]] | upstream | 0.27 |
| [[n02_tool_social_publisher]] | upstream | 0.27 |
| [[p12_wf_visual_frontend_marketing]] | related | 0.24 |
| [[p03_sp_social_publisher_builder]] | upstream | 0.23 |
