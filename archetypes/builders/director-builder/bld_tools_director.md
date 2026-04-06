---
kind: tools
id: bld_tools_director
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for director production
---

# Tools: director-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_mission_runner.py | Autonomous orchestration: waves -> grid -> poll -> stop -> consolidate | Runtime execution of director plan | ACTIVE |
| cex_coordinator.py | Synthesis gates between mission waves + workflow orchestration | Wave gate enforcement | ACTIVE |
| cex_signal_watch.py | Blocking signal poll: waits for builder completion, detects crashes | Signal monitoring | ACTIVE |
| _spawn/dispatch.sh | Solo and grid dispatch to nuclei (solo/grid/status/stop) | Builder dispatch | ACTIVE |
| signal_writer.py | Inter-nucleus signal emission (complete, error, retry) | Signal protocol | ACTIVE |
| cex_agent_spawn.py | Agent config validation + spawn pre-flight checks | Pre-dispatch validation | ACTIVE |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P08_architecture/_schema.yaml | Field definitions, director constraints |
| Director KC | P01_knowledge/library/kind/kc_director.md | Domain knowledge, patterns, anti-patterns |
| Runtime Handoffs | .cex/runtime/handoffs/ | Per-builder mission context files |
| Runtime Signals | .cex/runtime/signals/ | Builder completion/error signals |
| Decision Manifest | .cex/runtime/decisions/decision_manifest.yaml | GDP decisions for subjective choices |
| Nucleus Models | .cex/config/nucleus_models.yaml | Model assignments per nucleus |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated director validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == director, quality == null,
builders list >= 2 entries, dispatch_mode in enum, llm_function == ORCHESTRATE,
no task execution logic in body, wave_topology documented, fallback_per_builder complete.
