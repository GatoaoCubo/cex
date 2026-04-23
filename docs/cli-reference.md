# CLI Reference

These commands are available inside a Claude Code session with CEX loaded. Type them directly in the chat.

## Slash commands

| Command | Description | Example |
|---------|-------------|---------|
| `/build` | Build one artifact via 8F pipeline | `/build knowledge card about microservices` |
| `/mission` | Full lifecycle: plan + guide + spec + grid + consolidate | `/mission onboarding flow for customers` |
| `/plan` | Decompose goal into tasks, nuclei, dependencies | `/plan customer support chatbot` |
| `/guide` | Co-pilot mode: ask subjective questions before building | `/guide landing page for my product` |
| `/spec` | Create spec blueprint from plan + decisions | `/spec onboarding_flow` |
| `/grid` | Dispatch nuclei autonomously (up to 6 parallel) | `/grid BRAND_LAUNCH` |
| `/dispatch` | Send task to a specific nucleus | `/dispatch n03 build agent card` |
| `/validate` | Check artifact quality against gates | `/validate all` |
| `/status` | System health: running nuclei, signals, artifacts | `/status` |
| `/cex-doctor` | Full diagnostics: builders, schemas, files | `/cex-doctor` |
| `/consolidate` | Post-dispatch: verify, stop, commit | `/consolidate` |
| `/evolve` | Autonomous improvement loop for low-quality artifacts | `/evolve all` |
| `/mentor` | Vocabulary navigator for CEX terminology | `/mentor what is a builder?` |
| `/crew` | Manage multi-role teams with handoffs | `/crew list` |

## Command-line tools

These run from your terminal, outside of Claude Code:

```bash
# Build + Quality
python _tools/cex_8f_runner.py "intent" --kind <kind> --execute    # Full 8F build
python _tools/cex_doctor.py                                        # Health check (301 builders)
python _tools/cex_compile.py <path>                                # Compile .md to .yaml
python _tools/cex_compile.py --all                                 # Compile everything
python _tools/cex_score.py <path> --apply                          # Score an artifact
python _tools/cex_evolve.py sweep --target 9.0                     # Batch improvement
python _tools/cex_system_test.py                                   # Full system validation (54 tests)
python _tools/cex_sanitize.py --check --scope _tools/              # ASCII compliance

# Dispatch + Grid
bash _spawn/dispatch.sh solo n03 "task"                            # Dispatch one nucleus
bash _spawn/dispatch.sh grid MISSION                               # Dispatch grid (up to 6)
bash _spawn/dispatch.sh status                                     # Monitor running nuclei
bash _spawn/dispatch.sh stop                                       # Stop my session's nuclei
bash _spawn/dispatch.sh stop --dry-run                             # Preview what would stop

# Composable Crews
python _tools/cex_crew.py list                                     # List all registered crews
python _tools/cex_crew.py show <name>                              # Inspect resolved plan
python _tools/cex_crew.py run <name> --charter <path>              # Dry-run crew
python _tools/cex_crew.py run <name> --charter <path> --execute    # Real crew execution

# Discovery + Retrieval
python _tools/cex_run.py --discover "query"                        # Find relevant builders
python _tools/cex_retriever.py --query "topic" --top 10            # TF-IDF artifact search
python _tools/cex_query.py "keyword"                               # Builder discovery
python _tools/cex_batch.py intents.txt --max 5                     # Batch processing
```
