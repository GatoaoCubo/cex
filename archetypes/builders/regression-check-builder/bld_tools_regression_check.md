---
kind: tools
id: bld_tools_regression_check
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for regression_check production
---

# Tools: regression-check-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing regression_check artifacts in pool | Phase 1 (check duplicates, find baseline refs) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Comparison Frameworks
| Tool | Integration | Key Capability | Docs |
|------|-------------|----------------|------|
| Braintrust | REST API + SDK | Experiment diff, LLM judges, score history | braintrustdata.com/docs |
| Promptfoo | CLI + config YAML | `--compare` flag, assertion scoring, CI integration | promptfoo.dev/docs |
| LangSmith | SDK + UI | A/B experiment comparison, evaluator runs | docs.smith.langchain.com |
| DeepEval | Python SDK + CLI | `--compare-to` baseline file, metric suites | docs.confident-ai.com |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions, regression_check kind |
| CEX Examples | P07_evals/examples/ | Real regression_check artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P07_regression_check |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern `^p07_rc_`, baseline_ref is
a concrete non-empty string, threshold is numeric, metrics non-empty, quality == null,
fail_action defined, body <= 2048 bytes.
