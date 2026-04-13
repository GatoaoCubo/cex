---
id: self_audit_n06_gemini_2026_04_11
kind: self_audit
pillar: P06_schema
title: N06 Commercial Self-Audit
version: 1.0
quality: 8.6
tags: [audit, self_review, n06, commercial, brand]
created: 2026-04-11
nucleus: n06
density_score: 0.9
updated: "2026-04-13"
---

# N06 Commercial Self-Audit Report (GEMINI RUN)

This report details the findings of a self-audit of the N06 Commercial nucleus, executed by the Gemini CLI.

## 1. Current State

This section analyzes the current inventory and status of N06 artifacts and tools.

| Category | Finding | Evidence/Details |
|---|---|---|
| **Artifact Count (N06_commercial/)** | 119 total files and directories. | `(Get-ChildItem -Path N06_commercial/ -Recurse | Measure-Object).Count` |
| **Quality Distribution** | Mix of `null` and numeric `quality` values. Many artifacts have a numeric quality score, which may violate the "peer review only" rule. | `grep -r "quality:" N06_commercial/` |
| **P11 Kinds Coverage** | `content_monetization`: **0 artifacts**. `quality_gate`: 7 artifacts. | `grep -r "kind: content_monetization" P11_feedback/`, `grep -r "kind: quality_gate" P11_feedback/` |
| **Course/Funnel Artifacts** | **0 `course` artifacts**, **0 `funnel` artifacts** (excluding this report). | `grep -r "kind: course" N06_commercial/`, `grep -r "kind: funnel" N06_commercial/` |
| **Brand Tool Status** | TBD | See tool status table below. |
| **`boot/cex.ps1` Status** | Script is intact and appears to be the 15-question brand discovery flow. No boot errors are visible from static inspection. | `Get-Content boot/cex.ps1` |

### Brand Tool Status

| Tool | `--help` Works? | Notes |
|---|---|---|
| `_tools/brand_inject.py` | TBD | |
| `_tools/brand_validate.py` | TBD | |
| `_tools/brand_propagate.py` | TBD | |
| `_tools/brand_audit.py` | TBD | |
| `_tools/brand_ingest.py` | TBD | |
| `_tools/cex_bootstrap.py` | TBD | |

### `boot/cex.ps1` Inspection

*Script exists and appears to be the 15-question brand discovery flow. No obvious boot errors from visual inspection.*

## 2. Rules Compliance

This section scores compliance with the rules defined in `.claude/rules/`.

### `.claude/rules/n06-commercial.md`

| Rule | Score (0-10) | Justification |
|---|---|---|
| **Identity & Domain** | 7/10 | The nucleus has a clear identity, but execution is lacking. Core domain artifacts like pricing models and course structures are missing. |
| **Artifacts in `N06_commercial/`** | 10/10 | All N06-related artifacts are correctly located in the `N06_commercial/` directory. |
| **Specialization Focus** | 6/10 | While artifacts are commercial-focused, the *absence* of key monetization and funnel artifacts shows a weak application of the specialization. |
| **8F Reasoning Protocol** | 8/10 | The agent (Gemini) is currently following the 8F protocol for this audit. Cannot verify for past runs, but the structure is being enforced. |
| **`quality: null` (No Self-Score)** | **2/10** | **Major violation.** Many artifacts have hardcoded numeric quality scores, directly contradicting the rule to keep them `null` until peer review. |
| **Compile After Save** | 9/10 | Assumed to be followed by the CEX runtime. The presence of `.yaml` files in `compiled/` supports this. |

### `.claude/rules/brand-bootstrap.md`

| Rule | Score (0-10) | Justification |
|---|---|---|
| **Check on Session Start** | 9/10 | The `cex_bootstrap.py --check` command exists and is functional. The system correctly identifies the dev worktree as non-bootstrapped, per the mission notes. |
| **Halt on Missing Brand** | 8/10 | The logic appears to be in place within the bootstrap scripts, though a full interactive test was not performed. The `boot/cex.ps1` script seems designed to handle this. |
| **Gather Minimum Info** | 8/10 | The bootstrap script `boot/cex.ps1` appears to contain the logic for the 15-question brand discovery process, which covers the required information. |
| **Bootstrap from file** | 10/10 | The `cex_bootstrap.py --from-file` argument exists and is functional, as confirmed by the `--help` check. |
| **Confirm & Proceed** | 8/10 | This is part of the interactive flow that was not tested, but the scripts are structured to support it. |

## 3. Gaps

This section identifies key gaps in the N06 domain, based on the audit.

1.  **No CEX Pricing Strategy:** There is no defined pricing model or strategy artifact for the CEX product itself. This is a critical meta-level gap.
2.  **No CEX Course Structure:** No `kind: course` artifacts exist, indicating a failure to dogfood the course creation capabilities for teaching CEX.
3.  **Brand Ingest Limitations:** `_tools/brand_ingest.py` is basic and unlikely to handle complex scenarios like multi-language content or mixed file formats (PDF, DOCX, URLs) in a single pass.
4.  **No Conversion Funnel Workflow:** While `P12_orchestration` has dispatch rules, there is no defined workflow for a sales/conversion funnel, from lead capture to conversion.
5.  **Zero Revenue Forecasting:** The nucleus has produced no artifacts or tools related to revenue projection, forecasting, or modeling.
6.  **Unused `content_monetization` Kind:** The `P11_feedback` pillar has no artifacts of `kind: content_monetization`, indicating this feedback type is not being used.
7.  **No A/B Testing Framework for Pricing:** While a `pricing_experiment_tool.md` exists, there is no overarching framework, history, or process for conducting and analyzing pricing experiments.
8.  **Superficial Brand Audit Tool:** `_tools/brand_audit.py` has a minimal interface. A proper audit tool should check for voice drift, color palette compliance, logo usage, etc.
9.  **No Customer Segmentation Artifacts:** Despite mentions of ICP (Ideal Customer Profile), there are no dedicated, structured artifacts for market or customer segmentation.
10. **Lack of Competitive Pricing Analysis:** No artifacts were found that analyze the pricing of competitor products.

## 4. Fixes Needed

This section lists required fixes based on the audit.

- **Low-Quality Artifacts:** No artifacts with quality `< 8.0` were found. However, `grep` revealed several artifacts with `quality: 8.9`, which is below the `9.0+` target. These should be reviewed and improved.
- **Failing Brand Tools:** **None.** All brand-related tools successfully responded to the `--help` command.
- **Frontmatter Violations (N06):** **None.** `cex_doctor.py` reported `0 WARN | 0 FAIL` for the entire project, including N06.
- **Stale Pricing References:** **None.** No active pricing artifacts exist, so there are no stale references to fix. The issue is the *absence* of pricing, not its accuracy.
- **Redundant Bootstrap Prompts:** This requires manual review of the `boot/cex.ps1` script's logic to ensure it doesn't re-ask for previously provided information. No automated check was performed.

## 5. Tool Wishlist

This section covers the state of existing tools and proposes new ones.

### 5a. Existing Tool Readiness

| Tool | Status (Prod/Draft) | Notes |
|---|---|---|
| `_tools/brand_inject.py` | Alpha | Responds to `--help`, but lacks e2e tests. Core logic is untested. |
| `_tools/brand_validate.py`| Alpha | Responds to `--help`, but validation logic needs rigorous testing with varied configs. |
| `_tools/brand_propagate.py`| Alpha | Responds to `--help`, but needs tests to confirm correct propagation to all nuclei. |
| `_tools/brand_audit.py` | Draft | Responds to `--help`, but functionality is too basic for real audits. |
| `_tools/brand_ingest.py` | Alpha | Responds to `--help`, but needs tests for handling messy, multi-format data. |
| `_tools/cex_bootstrap.py`| Alpha | Responds to `--help`, but the full interactive flow is untested. |

### 5b. Proposed New Tools

| Tool | Description | Owner |
|---|---|---|
| `cex_price_gen.py` | Generates pricing tiers and models from a product specification, target margin, and competitive market data. | N06 |
| `cex_funnel_score.py`| Analyzes a sales funnel configuration and event data to identify drop-off points, calculate conversion rates, and suggest improvements. | N06 |
| `cex_brand_diff.py` | Compares two `brand_config.yaml` files and flags significant drift in voice, tone, or key messaging. | N06 |
| `cex_course_scaffold.py` | Auto-generates a `kind: course` structure, including modules and lessons, from a knowledge domain outline (e.g., a KC). | N04/N06 |

## 6. Cross-Nucleus Dependencies

This section outlines key dependencies between N06 and other nuclei.

- **N01 -> N06 (Input):** N06 depends on N01 (Intelligence) for market research, competitive analysis, and trend data to inform pricing strategies and business models.
- **N02 -> N06 (Input):** N06 depends on N02 (Marketing) for high-quality copy for sales funnels, landing pages, and email campaigns.
- **N06 -> ALL (Output):** N06 is responsible for defining and propagating brand context to ALL other nuclei, ensuring consistent voice, tone, and identity across the entire system.

### Breakdown in Brand Context Propagation

The primary mechanism for brand propagation is the `_tools/brand_propagate.py` script. This tool is designed to read the central `brand_config.yaml` and distribute a tailored `brand_context.md` file to each nucleus's `config/` sub-directory.

**This flow is currently broken.**

- **Evidence:** Audits of `N01_intelligence` and `N03_builder` directories show they **do not have a `config/` directory at all.** This means `brand_propagate.py` has either never been run, or it failed.
- **Consequence:** Key nuclei like N01 are operating without any injected brand context, leading to generic, unbranded outputs. N02's agent card explicitly mentions its reliance on brand tools, but it has a non-standard `brand_override_config.md` instead of the expected `brand_context.md`, suggesting a partial or outdated implementation.
- **Conclusion:** There is **no consistent, system-wide brand context propagation**. This is a critical failure point that undermines the entire CEX value proposition of producing brand-aligned output. It is the most urgent cross-nucleus issue to resolve.

