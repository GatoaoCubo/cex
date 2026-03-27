---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of interface artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: interface-builder

## Golden Example

INPUT: "Define o contrato entre SHAKA (pesquisa) e LILY (marketing) para entrega de research results"

OUTPUT:

```yaml
---
id: p06_iface_research_to_marketing
kind: interface
pillar: P06
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
contract: "Research results delivery from SHAKA to LILY"
provider: "SHAKA"
consumer: "LILY"
methods:
  - name: "get_research_summary"
    input: {topic: string, max_sources: integer}
    output: {summary: string, sources: list, confidence: float}
    description: "Returns distilled research summary with sources and confidence score"
  - name: "get_competitor_data"
    input: {competitor_name: string, marketplace: string}
    output: {pricing: object, listings: list, rating: float}
    description: "Returns structured competitor data for a specific marketplace"
backward_compatible: true
deprecation: null
mock:
  enabled: true
  example_payloads:
    - method: "get_research_summary"
      input: {topic: "decoracao minimalista", max_sources: 5}
      output: {summary: "Tendencia crescente em 2026...", sources: ["url1", "url2"], confidence: 0.87}
domain: "satellite-integration"
quality: null
tags: [interface, shaka, lily, research, marketing, satellite-integration]
tldr: "Bilateral contract for SHAKA to deliver research results to LILY marketing workflows."
density_score: 0.91
---
```

## Contract Definition
SHAKA (research satellite) provides structured research data to LILY (marketing satellite).
LILY calls methods to get research summaries and competitor data for marketing campaigns.

## Methods

| # | Name | Input | Output | Description |
|---|------|-------|--------|-------------|
| 1 | get_research_summary | {topic, max_sources} | {summary, sources, confidence} | Distilled research with sources |
| 2 | get_competitor_data | {competitor_name, marketplace} | {pricing, listings, rating} | Structured competitor intel |

## Versioning
- **Version**: 1.0.0
- **Backward compatible**: yes
- **Changes from previous**: initial release
- **Migration notes**: none

## Mock Specification
```json
{
  "method": "get_research_summary",
  "input": {"topic": "decoracao minimalista", "max_sources": 5},
  "output": {"summary": "Tendencia crescente em 2026...", "sources": ["url1", "url2"], "confidence": 0.87}
}
```

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p06_iface_ pattern (H02 pass)
- kind: interface (H04 pass)
- 15+ required fields present (H06 pass)
- methods has 2 entries with name/input/output/description (H07 pass)
- backward_compatible is boolean (H08 pass)
- provider and consumer specified (H09 pass)
- tldr <= 160 chars, dense (S01 pass)
- tags list len >= 3, includes "interface" (S02 pass)
- YAML parses cleanly (H01 pass)

---

## Anti-Example

INPUT: "Interface entre SHAKA e LILY"

BAD OUTPUT:

```yaml
---
id: shaka_lily_interface
kind: integration
pillar: Schema
contract: SHAKA-LILY
methods: "get data from SHAKA"
backward_compatible: maybe
quality: 9.0
tags: interface
---
```

SHAKA sends data to LILY when needed.

FAILURES:
1. id: no `p06_iface_` prefix -> H02 FAIL
2. kind: "integration" not "interface" -> H04 FAIL
3. pillar: "Schema" not "P06" -> H03 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. methods: string instead of list[object] -> H07 FAIL
6. backward_compatible: "maybe" not boolean -> H08 FAIL
7. provider/consumer: missing -> H09 FAIL
8. tags: string not list, len < 3 -> S02 FAIL
9. contract: not descriptive -> S05 FAIL
10. body: filler prose ("when needed") -> S07 FAIL
