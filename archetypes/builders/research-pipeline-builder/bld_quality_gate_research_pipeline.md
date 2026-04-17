---
id: p11_qg_research_pipeline
kind: quality_gate
pillar: P11
title: "Gate: research_pipeline"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: research_pipeline
quality: 9.1
tags: [quality-gate, research-pipeline, P11, STORM, CRAG, CRITIC, governance]
tldr: "Gates for research pipeline artifacts — 7-stage completeness, source diversity, CRAG thresholds, CRITIC verification, budget controls."
density_score: 1.0
llm_function: GOVERN
---
# Gate: research_pipeline

## Definition
| Field | Value |
|-------|-------|
| Kind | research_pipeline (cli_tool/workflow instances) |
| Pillar | P04 (tools) |
| Function | CALL (research automation) |
| Threshold | 8.0 minimum |

## HARD Gates (fail = reject)
| # | Gate | Check |
|---|------|-------|
| H1 | 7-stage complete | All 7 stages documented (INTENT through VERIFY) |
| H2 | Source diversity | At least 2 source categories populated (inbound + search minimum) |
| H3 | STORM perspectives | At least 3 perspectives defined with role + focus |
| H4 | CRAG threshold | crag_min_score defined (0.0-1.0, default 0.7) |
| H5 | CRITIC defined | critic_max_iterations defined, critic model is thinking model |
| H6 | Zero secrets | No API keys in plaintext — only ENV_VAR references |
| H7 | Budget controls | At least 1 budget cap defined (monthly or per-research) |
| H8 | Multi-model routing | At least extraction + reasoning + critic models specified |

## SOFT Gates (warn, don't reject)
| # | Gate | Check | Weight |
|---|------|-------|--------|
| S1 | 5+ perspectives | STORM has 5+ expert angles | 0.8 |
| S2 | Fallback chains | Each source has primary → fallback | 0.9 |
| S3 | Entity resolution | Dedup strategy documented | 0.7 |
| S4 | Marketplace schemas | Extraction fields per inbound source | 0.6 |
| S5 | Output formats | 2+ output formats (html + json minimum) | 0.5 |
| S6 | Gartner scoring | 7-dimension scoring documented | 0.7 |
| S7 | Rate limits | Per-source rate limits documented | 0.6 |
| S8 | Country-agnostic | No hardcoded country/marketplace names | 0.8 |

## CRAG Quality Gate (per-source, at runtime)
| Source Category | Min Score | Fallback |
|----------------|----------|----------|
| Inbound (marketplace) | 0.7 | Try next marketplace → Serper → skip |
| Search (web) | 0.6 | Try next search engine → skip |
| Outbound (social) | 0.5 | Lower threshold — social data is noisy |
| Trends | 0.4 | Trend data is directional, not precise |
| RAG (internal) | 0.8 | Internal docs should be high quality |

## Scoring Formula
```
score = (HARD_pass / 8) * 6.0 + (SOFT_weighted / max_weight) * 4.0
```

## Quality Tiers
| Tier | Score | Meaning |
|------|-------|---------|
| REJECT | < 8.0 | Missing stages, no quality gates, or security violation |
| PUBLISH | 8.0-8.9 | Pipeline complete, CRAG+CRITIC defined, budget controlled |
| EXEMPLARY | 9.0+ | Full source catalog, fallback chains, Gartner scoring |

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Flag for review |
| < 7.0  | REJECT | Rework required |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental research_pipeline artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |
