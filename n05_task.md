# Handoff: N05 — Build cex_preflight.py

## Mission: PREFLIGHT

**Priority**: HIGH
**Nucleus**: N05 (Operations)
**Dispatched by**: N07 (2026-04-13)

## Objective

Build `_tools/cex_preflight.py` — a pre-compilation tool that runs BEFORE nucleus boot using cheap/local models (Ollama qwen3:8b/14b or Claude Haiku) to assemble minimal, surgical context. This reduces token consumption on the main model (Sonnet/Opus) by 60-70%.

## DECISIONS (from user)

See: `.cex/config/nucleus_models.yaml` → `preflight:` section for all config.

Key decisions:
- Strategy: `hybrid` (local Ollama first, Haiku cloud fallback)
- Local models: qwen3:14b primary, qwen3:8b fallback
- Cloud model: claude-haiku-4-5-20251001
- Target: reduce ~50K tokens/call → ~15K tokens/call
- Output: `.cex/cache/preflight/{nucleus}_{task_hash}.json`

## Context (pre-loaded for you)

Your agent card: `N05_operations/` (your home directory)

## Relevant artifacts (READ these before producing)

1. `.cex/config/nucleus_models.yaml` — full config including new `preflight:` section
2. `_tools/cex_retriever.py` — TF-IDF retriever, you'll call this for artifact similarity
3. `_tools/cex_prompt_cache.py` — existing ISO cache, preflight extends this concept
4. `_tools/cex_skill_loader.py` — loads 13 ISOs per builder, preflight selects top-K
5. `_tools/cex_token_budget.py` — token counting, preflight uses this for budget enforcement
6. `_tools/cex_memory_select.py` — memory relevance selection
7. `_tools/cex_crew_runner.py` — prompt composer, preflight output feeds into this
8. `_tools/cex_shared.py` — shared utilities (parse_frontmatter, etc.)

## Architecture

```
cex_preflight.py
│
├── Phase 1: LOCAL (Ollama, $0 cost)
│   ├── scan_task(handoff_text) → extract kind, pillar, domain
│   ├── rank_isos(kind, task) → score 13 ISOs, return top 5
│   │   Uses: cex_skill_loader.get_skill_loader().load_builder(kind)
│   │   Ranking: TF-IDF similarity between task description and ISO content
│   ├── select_kcs(kind, domain) → top 3 most relevant KCs
│   │   Uses: cex_retriever --query "{task}" --kind {kind} --top-k 3
│   ├── dedup_context(isos + kcs + memory) → remove redundant content
│   └── count_tokens(compiled_context) → verify under budget
│       Uses: cex_token_budget.count_tokens()
│
├── Phase 2: CLOUD (Haiku, cheap — only if local uncertain)
│   ├── semantic_rerank(candidates, task) → LLM-scored relevance 0-1
│   ├── compress_verbose(long_context) → dense summary
│   └── score_confidence(compiled) → is this good enough? (>0.7 = ship it)
│
└── Output: .cex/cache/preflight/{nucleus}_{hash}.json
    {
      "nucleus": "n03",
      "kind": "agent",
      "task_hash": "a1b2c3",
      "compiled_at": "2026-04-13T...",
      "selected_isos": ["bld_manifest_agent.md", "bld_instruction_agent.md", ...],
      "selected_kcs": ["kc_agent.md"],
      "context_tokens": 14200,
      "original_tokens": 48000,
      "reduction_pct": 70.4,
      "strategy_used": "local",  // or "cloud" or "hybrid"
      "compiled_prompt": "... assembled context string ..."
    }
```

## CLI Interface

```bash
# Pre-compile context for a nucleus task
python _tools/cex_preflight.py --nucleus n03 --task "build agent for sales"

# Pre-compile from handoff file
python _tools/cex_preflight.py --handoff .cex/runtime/handoffs/MISSION_n03.md

# Pre-compile all handoffs in a mission
python _tools/cex_preflight.py --mission PREFLIGHT

# Show cache stats
python _tools/cex_preflight.py --stats

# Clear cache
python _tools/cex_preflight.py --clean

# Dry-run (show what would be selected, no LLM calls)
python _tools/cex_preflight.py --nucleus n03 --task "build agent" --dry-run
```

## Integration with Existing Tools

1. **cex_skill_loader.py**: Call `get_skill_loader().load_builder(kind)` to get all 13 ISOs, then rank them
2. **cex_retriever.py**: Call as subprocess `python _tools/cex_retriever.py --query "{task}" --top-k 5 --json` for KC selection
3. **cex_token_budget.py**: Import `count_tokens()` for accurate token counting
4. **cex_prompt_cache.py**: Check cache first — if preflight cache exists and is fresh, skip recomputation
5. **Ollama API**: Use OpenAI-compatible endpoint at `http://localhost:11434/v1` (config in YAML)
6. **Haiku fallback**: Use `anthropic` SDK or `claude` CLI with `--model claude-haiku-4-5-20251001`

## Ollama Integration Pattern

```python
# Read config from nucleus_models.yaml
import yaml
config = yaml.safe_load(open(".cex/config/nucleus_models.yaml"))
preflight_cfg = config["preflight"]
ollama_cfg = preflight_cfg["local"]

# Call via OpenAI SDK (already proven pattern in cex_evolve.py)
from openai import OpenAI
client = OpenAI(base_url=ollama_cfg["base_url"], api_key="ollama")
response = client.chat.completions.create(
    model=ollama_cfg["model"],
    messages=[{"role": "user", "content": ranking_prompt}],
    temperature=0.1
)
```

## Haiku Fallback Pattern

```python
# Only used when local model confidence < 0.7
import anthropic
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[{"role": "user", "content": rerank_prompt}]
)
```

## Quality Gates

- [ ] ASCII-only code (see `.claude/rules/ascii-code-rule.md`)
- [ ] `--dry-run` works without any LLM (pure file I/O + TF-IDF)
- [ ] Graceful fallback: Ollama offline → Haiku. Haiku offline → return all ISOs (no crash)
- [ ] Token count in output matches cex_token_budget.py count
- [ ] Cache invalidation: if ISO mtime > compiled_at, recompute
- [ ] Loads config from YAML only, zero hardcoded models
- [ ] Exit codes: 0=success, 1=error, 2=cache stale
- [ ] Works on Windows (Path handling, no Unix-only calls)

## Expected Output

1. **File**: `_tools/cex_preflight.py` (~300-500 lines)
2. **Kind**: cli_tool
3. **Frontmatter**: standard (docstring header with usage)
4. **Tests**: at minimum `--dry-run` and `--stats` must work without Ollama running

## After Completion

```bash
python _tools/cex_compile.py _tools/cex_preflight.py
git add _tools/cex_preflight.py
git commit -m "[N05] cex_preflight.py: hybrid local/cloud context pre-compiler"
```

Signal: `python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'complete', 9.0)"`
