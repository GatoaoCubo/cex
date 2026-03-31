---
kind: tools
id: bld_tools_red_team_eval
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for red_team_eval production
---

# Tools: red-team-eval-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing red_team_eval artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Eval Framework CLI Tools
| Tool | Install | Key Command | Output |
|------|---------|-------------|--------|
| promptfoo | `npm install -g promptfoo` | `promptfoo redteam run` | JSON report |
| garak | `pip install garak` | `garak --model_type openai --probes {probe}` | JSONL report |
| deepeval | `pip install deepeval` | `deepeval test run test_redteam.py` | pytest output |
| patronus | `pip install patronus` | `patronus evaluate --suite adversarial` | JSON results |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions, red_team_eval kind |
| CEX Examples | P07_evals/examples/ | Real red_team_eval artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P07_red_team_eval |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| OWASP LLM Top 10 | owasp.org/www-project-top-10-for-large-language-model-applications | Vulnerability taxonomy |
| Promptfoo plugin list | promptfoo.dev/docs/red-team/plugins | Available attack plugins |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern `^p07_rt_`, attack_types non-empty
and from approved enum, target is specific, pass_criteria is measurable, body <= 2048 bytes,
quality == null, no real exploit payloads in body.
