# 02 -- Build Artifact via CLI

**Difficulty:** Beginner

## What it does

Shows how to use the CEX CLI (`/build` command) to produce a `knowledge_card`
artifact. No Python needed -- just a Claude Code session.

## How to run

Start Claude Code in the CEX repo and type:

```
/build knowledge_card about API rate limiting best practices
```

The 8F pipeline runs automatically:
1. F1 CONSTRAIN -- resolves kind=knowledge_card, pillar=P01
2. F2 BECOME -- loads the knowledge-card-builder (12 ISOs)
3. F3 INJECT -- pulls related KCs, examples, brand context
4. F4 REASON -- plans sections and density target
5. F6 PRODUCE -- generates the artifact with frontmatter
6. F7 GOVERN -- validates against quality gate (target >= 8.0)
7. F8 COLLABORATE -- saves, compiles, commits, signals

## Expected artifact structure

See `expected_output.md` for a complete example. The key elements:

```yaml
---
id: kc_api_rate_limiting
kind: knowledge_card
pillar: P01
nucleus: n04
title: "API Rate Limiting Best Practices"
version: "1.0.0"
quality: null          # peer-review assigns, never self-score
tags: [api, rate-limiting, backend]
---
```

The body follows the knowledge_card schema: Summary, Core Concepts,
Implementation, References.

## Programmatic equivalent

```python
from cex_sdk import CEXAgent

agent = CEXAgent(nucleus="n04", kind="knowledge_card")
result = agent.build("API rate limiting best practices")
print(result.artifact)
```
