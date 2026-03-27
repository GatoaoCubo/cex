---
id: p01_fse_agent_creation
kind: few_shot_example
input: "criar agente de SEO para marketplace"
output: "agent spec + 10 ISO files + handoff dispatch via EDISON"
quality: 9.0
---

# Few-Shot: Agent Creation

## Input
```
"criar agente de SEO para marketplace"
```

## Output
```yaml
operation: agent_create
domain: SEO
context: marketplace
satellite: edison
result:
  agent_name: seo_marketplace
  path: records/agents/seo_marketplace/
  files_created: 10
  iso_tier: standard
```

## Why It Works
- CODEXA classifies intent via verb+object pattern ("criar" + "agente")
- Domain mapping routes SEO/marketing to LILY satellite for spec, EDISON for build
- HOP_EDISON_004 (Agent Builder) scaffold guarantees 10-file ISO standard tier
- Quality gate validates 12LP compliance before pool promotion
