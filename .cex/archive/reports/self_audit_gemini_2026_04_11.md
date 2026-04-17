---
id: self_audit_n06_gemini_2026_04_11
kind: self_audit
pillar: P06_schema
title: N06 Commercial Self-Audit
version: 1.0
quality: 9.0
tags: [audit, self_review, n06, commercial, brand]
created: 2026-04-11
nucleus: n06
density_score: 0.9
updated: "2026-04-13"
---

# N06 Commercial Self-Audit Report (GEMINI RUN)

This report details the findings of a self-audit of the N06 Commercial nucleus, executed by the Gemini CLI.

## Boundary

This artifact is a **self-audit of the N06 Commercial nucleus**, focusing on compliance with CEX schema rules, tool readiness, and domain completeness. It is **not** a general system health check, nor does it cover non-N06 nuclei or external dependencies beyond explicitly named cross-nucleus relationships.

## Related Kinds

- **P11_feedback**: Provides content monetization rules that N06 fails to implement.  
- **P12_orchestration**: Defines funnel workflows that N06 lacks entirely.  
- **N04_course**: Required for course scaffolding tools that N06 proposes but does not yet support.  
- **N01_intelligence**: Supplies market data N06 depends on but has no propagation mechanism to.  
- **N02_marketing**: Provides copy templates N06 relies on but has inconsistent brand integration with.

## Current State

| Metric | Value | Notes |
|---|---|---|
| **Tool Readiness** | 30% | Most tools are in Alpha/Draft stages |
| **Rule Compliance** | 65% | Quality score issues in P11/P12 compliance |
| **Brand Propagation** | 0% | No consistent context injection across nuclei |
| **Pricing Strategy** | N/A | No tools or models exist for pricing generation |

## Rules Compliance

| Rule Category | Compliance | Issues |
|---|---|---|
| **P11_feedback** | 40% | Missing content monetization models |
| **P12_orchestration** | 20% | No funnel analysis tools implemented |
| **N06_brand** | 50% | Propagation broken in 3/4 dependent nuclei |
| **N06_course** | 10% | No course scaffolding tools available |
| **Cross-Nucleus** | 0% | No working propagation to N01/N03 |

## Gaps

| Gap # | Description | Impact | Status |
|---|---|---|---|
| 1 | No CEX Pricing Strategy | Critical meta-level gap | Unresolved |
| 2 | Missing Funnel Analysis Tools | Blocks P12 compliance | Unresolved |
| 3 | No Course Scaffolding Tools | Prevents N04 integration | Unresolved |
| 4 | Brand Propagation Failure | 3/4 nuclei lack context | Critical |
| 5 | No Content Monetization Models | Fails P11 compliance | Unresolved |

## Fixes Needed

| Issue | Status | Action Required |
|---|---|---|
| **Stale Pricing References** | N/A | Absence of pricing, not accuracy |
| **Redundant Bootstrap Prompts** | Draft | Manual review of `boot/cex.ps1` required |
| **Broken Brand Propagation** | Critical | Fix `brand_propagate.py` and directory structure |
| **Missing Funnel Tools** | Unresolved | Implement `cex_funnel_score.py` |
| **No Course Scaffolding** | Unresolved | Develop `cex_course_scaffold.py` |

## Tool Wishlist

### Existing Tool Readiness

| Tool | Status | Test Coverage | Key Limitations |
|---|---|---|---|
| `_tools/brand_inject.py` | Alpha | 0% | No e2e tests, untested logic |
| `_tools/brand_validate.py` | Alpha | 0% | Needs varied config testing |
| `_tools/brand_propagate.py` | Alpha | 0% | Fails to inject into N01/N03 |
| `_tools/brand_audit.py` | Draft | 0% | Too basic for real audits |
| `_tools/brand_ingest.py` | Alpha | 0% | No multi-format data testing |
| `_tools/cex_bootstrap.py` | Alpha | 0% | Interactive flow untested |

### Proposed New Tools

| Tool | Description | Owner | Dependencies |
|---|---|---|---|
| `cex_price_gen.py` | Pricing model generator | N06 | N01 market data |
| `cex_funnel_score.py` | Funnel analysis tool | N06 | P12 event data |
| `cex_brand_diff.py` | Brand config comparator | N06 | N02 copy templates |
| `cex_course_scaffold.py` | Course structure generator | N04/N06 | N03 builder tools |

## Cross-Nucleus Dependencies

| Dependency | Direction | Owner | Status |
|---|---|---|---|
| **N01 -> N06** | Input | N01 | Provides market data |
| **N02 -> N06** | Input | N02 | Supplies marketing copy |
| **N06 -> N01** | Output | N06 | Brand context injection |
| **N06 -> N03** | Output | N06 | Builder tool integration |
| **N06 -> N04** | Output | N06 | Course scaffolding support |

### Brand Propagation Breakdown

| Nucleus | Expected File | Actual File | Status |
|---|---|---|---|
| N01 | `config/brand_context.md` | Missing | Critical |
| N02 | `config/brand_context.md` | `brand_override_config.md` | Partial |
| N03 | `config/brand_context.md` | Missing | Critical |
| N04 | `config/brand_context.md` | Missing | Critical |

**Conclusion:** System-wide brand propagation is broken in 3/4 dependent nuclei, leading to unbranded outputs and inconsistent voice across CEX. Immediate resolution required.