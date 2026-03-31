---
id: p01_fse_agent_creation
kind: few_shot_example
input: "criar agente de SEO para marketplace"
output: "agent spec + 10 ISO files + handoff dispatch via builder_agent"
quality: 9.0
---
tldr: "Shows how to create an agent artifact using the 8F pipeline with a concrete input-output pair."
quality: null
tldr: "Shows how to create an agent artifact using the 8F pipeline with a concrete input-output pair."
quality: null
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
agent_node: edison
result:
  agent_name: seo_marketplace
  path: records/agents/seo_marketplace/
  files_created: 10
  iso_tier: standard
```

## Why It Works
- organization classifies intent via verb+object pattern ("criar" + "agente")
- Domain mapping routes SEO/marketing to marketing_agent agent_node for spec, builder_agent for build
- HOP_builder_agent_004 (Agent Builder) scaffold guarantees 10-file ISO standard tier
- Quality gate validates 12LP compliance before pool promotion
