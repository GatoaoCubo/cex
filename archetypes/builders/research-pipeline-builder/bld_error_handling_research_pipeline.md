---
kind: error_handling
id: bld_error_handling_research_pipeline
pillar: P11
llm_function: GOVERN
purpose: Failure modes, retry logic, fallbacks, budget controls for research pipeline
---

# Error Handling: research_pipeline

## Per-Stage Failure Matrix
| Stage | Error | Severity | Recovery |
|-------|-------|----------|----------|
| S1 INTENT | Unclassifiable query | MEDIUM | Default to general research route |
| S1 INTENT | Empty query | FATAL | Return error, request clarification |
| S2 PLAN | LLM timeout on perspective generation | HIGH | Retry 2x → use 3 default perspectives |
| S2 PLAN | Too few sub-questions (<10) | LOW | Accept — still useful, just less coverage |
| S3 RETRIEVE | Source API timeout | HIGH | Try fallback source → skip source |
| S3 RETRIEVE | Source auth failure (401/403) | FATAL per source | Log + notify, skip source, continue |
| S3 RETRIEVE | Rate limit hit (429) | HIGH | Respect Retry-After, queue for later |
| S3 RETRIEVE | All sources fail for a category | HIGH | Degrade gracefully — report gap |
| S3 CRAG | Result below quality threshold | LOW | Discard result, try next source |
| S3 CRAG | All results below threshold | MEDIUM | Lower threshold 10%, retry once |
| S4 RESOLVE | Entity matching failure | LOW | Skip dedup, accept duplicates |
| S4 RESOLVE | Embedding API failure | MEDIUM | Fallback to fuzzy title matching |
| S5 SCORE | Scoring model timeout | MEDIUM | Retry 2x → assign neutral score (5.0) |
| S6 SYNTHESIZE | Domain model timeout | HIGH | Retry → try alternative model |
| S6 SYNTHESIZE | Insufficient data for domain | MEDIUM | Report "insufficient data" section |
| S7 CRITIC | Verification finds errors | NORMAL | Correct and re-verify (max 3 iters) |
| S7 CRITIC | Max iterations exceeded | LOW | Accept with warning flag |
| S7 CRITIC | Thinking model timeout | HIGH | Accept unverified with warning |

## Fallback Chains (per source category)
```yaml
inbound_fallback:
  mercadolivre: [firecrawl_direct, serper_site_search, skip]
  shopee: [firecrawl_direct, serper_site_search, skip]
  amazon: [keepa_api, firecrawl_direct, serper_site_search, skip]

search_fallback:
  serper: [brave_search, tavily, exa, skip]
  exa: [serper, tavily, skip]

outbound_fallback:
  youtube: [serper_youtube, skip]
  reddit: [serper_reddit, skip]
  reclameaqui: [firecrawl_direct, skip]
```

## Budget Controls
| Control | Trigger | Action |
|---------|---------|--------|
| Firecrawl monthly limit | credits >= firecrawl_monthly | Switch to Serper fallback |
| Firecrawl per-research | credits >= firecrawl_per_research | Stop scraping, use cached |
| Serper daily limit | queries >= serper_daily | Switch to Brave/Tavily |
| LLM cost spike | cost > 2x expected | Alert admin, continue with Flash |
| Total research cost | > budget.max_per_research | Stop retrieval, synthesize available |

## Circuit Breaker (per source)
If 3 consecutive failures for same source across researches:
1. OPEN circuit for that source
2. Log warning, skip in future researches
3. After 24h, test with 1 query (HALF-OPEN)
4. Success → CLOSE, failure → OPEN for 48h

## Degradation Strategy
| Level | Data Available | Action |
|-------|---------------|--------|
| Full | All sources responding | Normal 7-stage pipeline |
| Partial | 50-80% sources | Proceed, flag gaps in report |
| Minimal | <50% sources | Warn user, produce best-effort report |
| Failed | <20% sources | Abort, return "insufficient data" error |
