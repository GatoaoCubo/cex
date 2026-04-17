---
kind: examples
id: bld_examples_chain
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of chain artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Examples Chain"
version: "1.0.0"
author: n03_builder
tags: [chain, builder, examples]
tldr: "Golden and anti-examples for chain construction, demonstrating ideal structure and common pitfalls."
domain: "chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: chain-builder
## Golden Example
INPUT: "Create a prompt chain for research-to-knowledge-card pipeline"
OUTPUT:
```yaml
id: p03_ch_research_to_kc
kind: chain
pillar: P03
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
title: "Research to Knowledge Card Pipeline"
steps_count: 3
flow: sequential
input_format: "topic name + domain string"
output_format: "knowledge_card markdown artifact"
context_passing: filtered
error_strategy: fail_fast
domain: "knowledge"
quality: null
tags: [chain, knowledge, research, distillation]
tldr: "3-step chain: gather sources, extract facts, compose KC with density >= 0.80"
density_score: 0.88
```
## Purpose
Transforms a raw topic into a production-ready knowledge_card by chaining three
prompt steps: source gathering, fact extraction, and KC composition. Each step
narrows scope — from broad research to atomic distilled facts.
## Steps
### Step 1: Gather Sources
- **Input**: topic name (string), domain (string)
- **Prompt**: Search for authoritative sources on `{{topic}}` in `{{domain}}`. Return 3-5 URLs with one-line summaries.
- **Output**: list of {url, summary} objects (JSON)
### Step 2: Extract Facts
- **Input**: list of {url, summary} from Step 1
- **Prompt**: For each source, extract 5-10 atomic facts as bullets <= 80 chars. Remove opinions and filler.
- **Output**: deduplicated fact list (markdown bullets)
### Step 3: Compose KC
- **Input**: fact list from Step 2, original topic/domain
- **Prompt**: Compose a knowledge_card following P01 schema. Fill all required fields. density >= 0.80.
- **Output**: complete knowledge_card artifact (YAML frontmatter + markdown body)
## Data Flow
```text
[topic, domain] --string--> Gather --JSON--> Extract --bullets--> Compose --KC.md-->
```
Context passing: filtered — each step receives only its direct input, not full history.
## Error Handling
- **Strategy**: fail_fast
- **On failure at step N**: halt chain, return partial output with error context
- **Retry policy**: none (source quality issues require human intervention)
## References
- P01_knowledge/_schema.yaml (KC field definitions)
- archetypes/builders/knowledge-card-builder/ (downstream consumer)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p03_ch_ pattern (H02 pass)
- kind: chain (H04 pass)
- 19 required fields present (H06 pass)
- body has Purpose + Steps + Data Flow + Error Handling (H07 pass)
- steps_count: 3 matches actual 3 steps (H08 pass)
- Each step has Input/Prompt/Output (S03 pass)
- Data flow diagram present and matches steps (S04 pass)
- No runtime orchestration in body (S08 pass)
- No filler phrases (S10 pass)
## Anti-Example
INPUT: "Create a chain for content processing"
BAD OUTPUT:
```yaml
id: content_chain
kind: prompt
pillar: prompt
title: Content Chain
steps_count: 5
quality: 9.0
tags: [content]
```
This chain processes content through multiple steps. First, we gather the content.
Then we process it. Finally, we output the result.
## Steps
1. Get content
2. Process content
3. Output result
FAILURES:
1. id: no `p03_ch_` prefix -> H02 FAIL
2. kind: "prompt" not "chain" -> H04 FAIL
3. pillar: "prompt" not "P03" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. Missing fields: version, created, updated, author, flow, input_format, output_format, domain -> H06 FAIL
6. tags: only 1 item, missing "chain" -> S02 FAIL
7. Steps lack Input/Prompt/Output structure -> S03 FAIL
8. No Data Flow diagram -> S04 FAIL
9. No Error Handling section -> S06 FAIL
10. Body is filler prose ("This chain processes...") -> S10 FAIL
