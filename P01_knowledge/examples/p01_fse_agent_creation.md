---
id: p01_fse_agent_creation
type: few_shot_example
input: criar agente de SEO para marketplace
output: agent spec com README + 9 ISO files + handoff dispatch via EDISON
quality: 9.0
---

# Few-Shot: Agent Creation via CODEXA

## Input

```
"criar agente de SEO para marketplace"
```

## Classification

```yaml
operation: agent_create
domain: SEO
context: marketplace
satellite_assigned: lily
```

## Execution Chain

1. CODEXA classifica intent -> `agent_create`
2. Escreve handoff: `.claude/handoffs/codexa_agent_create.md`
3. Spawna EDISON: `spawn_solo.ps1 -sat edison -task "Read handoff"`
4. EDISON executa HOP_EDISON_004 (Agent Builder)
5. QA valida via 12LP scan

## Output

```yaml
agent_name: seo_marketplace
path: records/agents/seo_marketplace/
files:
  - README.md
  - iso_vectorstore/ISO_LILY_088_MANIFEST.md
  - iso_vectorstore/ISO_LILY_089_INSTRUCTIONS.md
  - iso_vectorstore/ISO_LILY_090_ARCHITECTURE.md
  - iso_vectorstore/ISO_LILY_091_ERROR_HANDLING.md
