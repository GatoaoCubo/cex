---
id: p01_rs_exemplary_weather_api
kind: rag_source
pillar: P01
version: "1.0.0"
created: "2023-10-15"
updated: "2023-10-15"
author: "rag-source-builder"
url: "https://api.weather.com/v3/wx/forecast/daily/5day"
domain: "weather_services"
last_checked: "2023-10-15"
quality: null
tags: [rag-source, weather_services, api]
tldr: "Reliable 5-day weather forecast API maintained by a major weather service provider."
keywords: [weather, forecast, api, daily, meteorology]
reliability: "high"
format: "api"
extraction_method: "api_call"
---

## Source Description
This source provides a reliable 5-day weather forecast API maintained by a major weather service provider. It offers detailed daily weather predictions using meteorological data. Intended for developers integrating weather data into their applications.

## Freshness Policy
- Re-check interval: 30 days
- Staleness threshold: 90 days
- Trigger: version release or major data update
- Last verified: 2023-10-15

## Extraction Notes
- Method: api_call
- Format: api
- Auth required: yes (API key)
- Known quirks: rate limits apply; high request volumes may need special arrangements

## References
- Parent domain: weather_services
- Related sources: none