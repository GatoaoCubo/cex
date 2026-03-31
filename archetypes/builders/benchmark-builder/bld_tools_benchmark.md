---
kind: tools
id: bld_tools_benchmark
pillar: P04
llm_function: CALL
purpose: Tools available for benchmark production
---

# Tools: benchmark-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing benchmarks | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions for benchmark |
| CEX Examples | P07_evals/examples/ | Existing benchmark artifacts |
| Model Cards | P02_model/examples/ | Performance specs (latency, cost, TPS) |
| SEED_BANK | archetypes/SEED_BANK.yaml | P07_benchmark seeds |
| Anthropic API | https://docs.anthropic.com | Model performance data |
| LiteLLM | https://docs.litellm.ai | Cross-provider latency/cost data |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
- [ ] YAML parses
- [ ] id matches p07_bm_ prefix
- [ ] iterations >= 10, warmup >= 1
- [ ] percentiles include p50 + p95
- [ ] baseline and target are numeric with same unit
- [ ] direction is explicit
