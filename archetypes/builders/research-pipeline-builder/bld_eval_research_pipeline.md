---
kind: quality_gate
id: p11_qg_research_pipeline
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of research pipeline configs
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Gate: research_pipeline"
version: 1.0.0
author: n03_engineering
tags: [quality-gate, research-pipeline, P11, STORM, CRAG, CRITIC, governance]
tldr: "Gates for research pipeline artifacts — 7-stage completeness, source diversity, CRAG thresholds, CRITIC verification, budget controls."
domain: research_pipeline
created: 2026-03-31
updated: 2026-03-31
density_score: 1.0
related:
  - bld_examples_research_pipeline
  - p02_agent_research_pipeline_intelligence
  - tpl_research_pipeline
  - bld_instruction_research_pipeline
  - p03_sp_research_pipeline_builder
  - ex_research_pipeline_ecommerce_br
  - p04_rp_marketing_nucleus
  - bld_output_template_research_pipeline
  - n01_tool_research_pipeline
  - p11_qg_social_publisher
---

## Quality Gate

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

## Examples

# Examples: research-pipeline-builder

## Golden Example — E-commerce BR (CODEXA)
INPUT: "Create research pipeline config for Brazilian pet e-commerce marketplace intelligence"
OUTPUT:
```yaml
identity:
  empresa: "CODEXA"
  nicho: pet_ecommerce
  idioma: pt-BR
  pais: BR
sources:
  inbound: [mercadolivre, shopee, amazon_br, magalu, americanas, casas_bahia, shein, temu]
  outbound: [youtube, reddit, reclameaqui]
  search: [serper, exa, gemini_search, openai_search]
  trends: [pytrends, keepa]
  rag: [local_docs]
storm_perspectives:
  - {role: buyer, focus: "preco frete reviews confianca"}
  - {role: seller, focus: "positioning pricing quality listing"}
  - {role: analyst, focus: "tendencias volume sazonalidade crescimento"}
  - {role: marketer, focus: "keywords SEO content-gaps social-proof"}
  - {role: consumer_researcher, focus: "pain-points necessidades sentimento"}
multi_model:
  extraction: gemini-2.5-flash
  reasoning: gpt-5-mini
  social: gemini-2.5-flash
  critic: o4-mini
budget:
  firecrawl_monthly: 3000
  firecrawl_per_research: 10
  serper_daily: 100
output:
  formats: [html, pptx, json]
  idioma: pt-BR
  template: consulting
quality:
  crag_min_score: 0.7
  critic_max_iterations: 3
  final_min_score: 8.0
```
WHY GOOD: All source categories covered, STORM perspectives costmized to niche, budget caps defined, multi-model routing by task, quality gates explicit.

## Anti-Example — Single Source Research
```python
# BAD: single source, no quality gate, no verification
results = google_search(query)  # only 1 source
report = gpt4(f"analyze: {results}")  # no CRAG scoring
return report  # no CRITIC verification
```
WHY BAD: Single source (no STORM), no quality gate (no CRAG), no verification (no CRITIC), no budget control, no config.

## Golden Example — SaaS Global
```yaml
identity: { empresa: "TechCo", nicho: saas_analytics, idioma: en, pais: US }
sources:
  inbound: [g2, capterra, producthunt, crunchbase]
  outbound: [youtube, reddit, hackernews, twitter]
  search: [serper, exa, tavily]
  trends: [pytrends]
  rag: [internal_wiki, confluence]
storm_perspectives:
  - {role: buyer, focus: "pricing features integrations support"}
  - {role: competitor, focus: "market-share roadmap funding team-size"}
  - {role: analyst, focus: "TAM growth-rate churn-rate ARR"}
  - {role: developer, focus: "API docs SDK ease-of-integration"}
  - {role: reviewer, focus: "NPS satisfaction complaints switching-cost"}
multi_model:
  extraction: gemini-2.5-flash
  reasoning: claude-sonnet
  critic: o4-mini
budget:
  serper_daily: 50
  exa_monthly: 1000
quality: { crag_min_score: 0.7, critic_max_iterations: 3, final_min_score: 8.0 }
```
WHY GOOD: SaaS-specific sources (G2, Capterra), developer perspective, different model choices, apownte budget for SaaS research volume.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
