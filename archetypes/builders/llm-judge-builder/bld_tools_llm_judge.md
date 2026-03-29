---
kind: tools
id: bld_tools_llm_judge
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for llm_judge production
---

# Tools: llm-judge-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing llm_judge artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Framework Integration References
| Framework | Integration Point | Scale Convention | Status |
|-----------|------------------|-----------------|--------|
| Braintrust | scorer() function — returns {score, metadata} | 0.0-1.0 continuous | ACTIVE |
| DeepEval | GEval metric — evaluation_steps + LLMTestCase | 0.0-1.0 normalized | ACTIVE |
| RAGAS | faithfulness, answer_relevancy, context_precision | 0.0-1.0 per metric | ACTIVE |
| Promptfoo | llm-rubric assert type — value = rubric string | pass/fail or score | ACTIVE |
| OpenAI Evals | model-graded-closedqa, model-graded-fact | pass/fail | ACTIVE |
| Custom | Direct judge prompt via completions API | any declared scale | ACTIVE |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions, llm_judge kind |
| CEX Examples | P07_evals/examples/ | Real llm_judge artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P07_llm_judge |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Model Reference (judge_model selection)
| Model ID | Provider | Recommended for |
|----------|----------|----------------|
| gpt-4o | OpenAI | General quality, factual accuracy |
| gpt-4o-mini | OpenAI | High-volume, cost-sensitive evals |
| claude-3-5-sonnet-20241022 | Anthropic | Nuanced criteria, long contexts |
| claude-3-haiku-20240307 | Anthropic | Fast low-cost screening judges |
| gemini-1.5-pro | Google | Multimodal evals, cross-family bias reduction |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern `p07_judge_`, criteria list
matches body sections, scale has anchors, few_shot scores within scale range,
body <= 2048 bytes, quality == null, judge_model is a concrete identifier.
