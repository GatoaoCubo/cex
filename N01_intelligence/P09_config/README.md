# P09 Config — N01 Intelligence

> Analytical Envy · configuration for research pipelines and data sources

## Scope in N01
Runtime settings for intelligence gathering: scraper rate limits, API
credentials for data vendors, research pipeline schedules, analyst
tool paths. The sin lens (envy every competitor) drives aggressive
polling — so rate configs here are tuned for breadth over politeness.

## Kinds that live here
- `env_config` — env vars for research tools (API keys, endpoints)
- `rate_limit_config` — scraper throttling per data source
- `secret_config` — vendor API credentials (gitignored)
- `feature_flag` — toggle experimental research pipelines

## Related
- `tools/` — the scrapers and API clients this config governs
- `schemas/` — validation for config inputs
