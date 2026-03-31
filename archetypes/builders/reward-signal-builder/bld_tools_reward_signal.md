---
kind: tools
id: bld_tools_reward_signal
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for reward_signal production
---

# Tools: reward-signal-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing reward_signal artifacts in pool | Phase 1 (check duplicates, find calibration references) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
| reward_bench_eval | Evaluate LLM-judge reliability against human ground truth | Phase 1 (model selection) | [EXTERNAL] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P11_feedback/_schema.yaml | Field definitions, reward_signal kind |
| CEX Examples | P11_feedback/examples/ | Real reward_signal artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P11_reward_signal |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| RewardBench | huggingface.co/datasets/allenai/reward-bench | Benchmark for reward model calibration |
## Calibration References
| Signal type | Calibration method | Key metric |
|------------|-------------------|------------|
| scalar | Compare LLM-judge scores against human ratings on 100-sample holdout | Spearman correlation >= 0.75 |
| preference | Agreement rate between model and human on preference pairs | >= 70% agreement |
| critique | Human evaluation of critique quality and revision improvement | Improvement rate >= 60% |
| comparative | Kendall's tau between model ranking and human ranking | >= 0.65 |
| implicit | Correlation of implicit signal with explicit human rating | >= 0.60 |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, signal_type enum value,
baseline within scale range, body <= 2048 bytes, quality == null, >= 2 criteria with weights,
Application section present with named improvement loop.
