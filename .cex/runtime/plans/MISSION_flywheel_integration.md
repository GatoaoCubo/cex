---
id: mission_flywheel_integration
kind: mission_plan
version: 1.0.0
created: 2026-04-05
status: REVIEW
author: n07-orchestrator
title: "Flywheel Integration: Wire New SDK Modules into Existing Runtime"
quality: null
waves: 4
tasks: 12
estimated_tokens: ~60K
---

# MISSION: Flywheel Integration

> **Goal**: Wire the 8 new SDK modules (from OpenClaude assimilation) into
> the existing runtime so they actually DO something. Currently they import
> cleanly (101/101 audit) but nothing in the pipeline calls them yet.

## Current State (Doc vs Practice)

| Module | Import | Wired Into | Status |
|--------|--------|-----------|--------|
| `cex_token_budget` | OK | `crew_runner.count_tokens()` only | PARTIAL -- not in 8f_runner |
| `cex_memory_types` | OK | NOWHERE | IDLE |
| `cex_memory_age` | OK | NOWHERE | IDLE |
| `cex_gdp` | OK | NOWHERE | IDLE |
| `cex_router` | OK | NOWHERE | IDLE |
| `cex_skill_loader` | OK | NOWHERE (crew_runner reads ISOs manually via glob) | IDLE |
| `cex_agent_spawn` | OK | NOWHERE | IDLE |
| `cex_coordinator` | OK | NOWHERE (mission_runner runs raw subprocess waves) | IDLE |

**Translation**: We built 8 engines but never connected them to the car.

---

## Wave 0: PREP (no code changes, diagnostic only)

| # | Task | What | Risk |
|---|------|------|------|
| T00 | Snapshot | `git stash` baseline + run `cex_flywheel_audit.py audit` | none |

**Gate**: 101/101 WIRED baseline confirmed.

---

## Wave 1: CORE WIRING (no behavior change, additive only)

These 4 wires replace manual implementations with the new modules.
**Backward compat**: old code paths remain as fallback (`try/except`).

| # | Task | File | Change | Fallback |
|---|------|------|--------|----------|
| T01 | Wire SkillLoader into crew_runner | `cex_crew_runner.py` | Replace `load_builder_context()` glob-walk with `SkillLoader.load_builder()` | If SkillLoader fails, fall back to existing glob |
| T02 | Wire Router into crew_runner | `cex_crew_runner.py` | Replace `_resolve_model()` env-var lookup with `CexRouter.resolve_nucleus()` | If Router fails, keep existing `LLM_MODEL` env fallback |
| T03 | Wire GDP into 8f_runner | `cex_8f_runner.py` | At F4 REASON start, call `GDPEnforcer.get_pending()`. If unresolved USER-scope decisions exist for this kind, raise `NeedsUserDecision` instead of proceeding | If GDP import fails, skip (current behavior = no check) |
| T04 | Wire token_budget into 8f_runner | `cex_8f_runner.py` | At F1 CONSTRAIN, call `count_tokens(prompt)` and set `state.token_budget`. At F6 PRODUCE, warn if output exceeds budget | If import fails, skip (current = no budget awareness) |

**Gate**: Run `cex_flywheel_audit.py wires` + `python _tools/cex_8f_runner.py --help` (no crash).

### T01 Detail: SkillLoader into crew_runner

```
CURRENT (crew_runner line 207-228):
  load_builder_context() -> glob bld_*.md -> sort -> read -> concat

PROPOSED:
  def load_builder_context(builder_id, builder_dir=BUILDER_DIR):
      try:
          from cex_skill_loader import SkillLoader
          sl = SkillLoader()
          isos = sl.load_builder(builder_id.replace("-builder",""))
          # SkillLoader returns BuilderISO objects with .get_prompt()
          return "\n\n".join(iso.get_prompt() for iso in isos)
      except Exception:
          # FALLBACK: original glob implementation
          <existing code unchanged>
```

**Why**: SkillLoader already handles 13 ISOs, sort order, frontmatter parse, shared skills injection, conditional activation. The glob does none of that.

### T02 Detail: Router into crew_runner

```
CURRENT (crew_runner line 566-573):
  _resolve_model() -> builder.get("model", LLM_MODEL)

PROPOSED:
  def _resolve_model(self, builder):
      try:
          from cex_router import CexRouter
          router = CexRouter()
          nucleus = os.environ.get("CEX_NUCLEUS", "n03")
          resolved = router.resolve_nucleus(nucleus)
          return resolved["model"], resolved.get("max_tokens", LLM_MAX_TOKENS)
      except Exception:
          # FALLBACK: existing env-var behavior
          model = builder.get("model", LLM_MODEL)
          max_tokens = builder.get("model_max_tokens", LLM_MAX_TOKENS)
          return model, max_tokens
```

**Why**: Router reads `router_config.yaml`, handles provider fallback chains (anthropic -> google -> openai), checks API key presence. Current code is blind.

### T03 Detail: GDP into 8f_runner

```
CURRENT (8f_runner F4 REASON, line ~505):
  _f4_reason() -> LLM plans artifact, no user gate

PROPOSED:
  def _f4_reason(self):
      # GDP gate: check for unresolved user decisions
      try:
          from cex_gdp import GDPEnforcer, NeedsUserDecision
          gdp = GDPEnforcer()
          pending = gdp.get_pending()
          for d in pending:
              if d.kind == self.state.kind or d.scope.value == "GLOBAL":
                  raise NeedsUserDecision(d)
      except NeedsUserDecision:
          raise  # propagate to caller
      except Exception:
          pass  # GDP not available, proceed
      # ... existing F4 logic unchanged ...
```

**Why**: This is the GDP rule -- "subjective decisions ask user first". Without this wire, 8F ignores pending decisions entirely.

### T04 Detail: token_budget into 8f_runner

```
CURRENT: no token awareness anywhere in 8f_runner

PROPOSED (F1 CONSTRAIN):
  try:
      from cex_token_budget import count_tokens, allocate_budget
      budget = allocate_budget(model=self.state.model)
      self.state.token_budget = budget
  except: pass

PROPOSED (F6 PRODUCE, after output):
  if hasattr(self.state, 'token_budget') and self.state.token_budget:
      used = count_tokens(output_text)
      if used > self.state.token_budget.output_limit:
          self._log("F6", f"WARNING: output {used} tokens exceeds budget {self.state.token_budget.output_limit}")
```

---

## Wave 2: MEMORY ENRICHMENT

| # | Task | File | Change |
|---|------|------|--------|
| T05 | Wire memory_types into memory_update | `cex_memory_update.py` | Use `MemoryType` enum + `should_save()` classifier instead of raw string types |
| T06 | Wire memory_age into memory_select | `cex_memory_select.py` | Use `memory_freshness_caveat()` + `format_recalled_memory()` for age-aware ranking |
| T07 | Wire memory_types+age into crew_runner | `cex_crew_runner.py` | Enrich memory injection block with type labels + freshness caveats |

**Gate**: Run `python _tools/cex_memory_update.py --help` + `python _tools/cex_memory_select.py --help` (no crash).

### T05 Detail

```
CURRENT (memory_update line 84-89):
  obs_type = fm.get("memory_scope", "project")
  decay_rate = DECAY_RATES.get(obs_type, 0.03)  # hardcoded dict

PROPOSED:
  from cex_memory_types import MemoryType, should_save, parse_memory_type
  # Auto-classify if user didn't specify
  if not explicit_type:
      should, classified = should_save(observation, existing_context)
      if not should: return  # skip duplicate/trivial
      obs_type = classified
  else:
      obs_type = parse_memory_type(explicit_type)
  # Use enum's built-in decay rate
  decay_rate = {
      MemoryType.CORRECTION: 0.00,
      MemoryType.PREFERENCE: 0.01,
      MemoryType.CONVENTION: 0.02,
      MemoryType.CONTEXT: 0.05,
  }[obs_type]
```

### T06 Detail

```
CURRENT (memory_select line 181-192):
  score = overlap * h.confidence  # no age factor

PROPOSED:
  from cex_memory_age import memory_age_days, memory_freshness_caveat
  age = memory_age_days(path.stat().st_mtime)
  age_penalty = max(0.5, 1.0 - (age / 365))  # linear decay over 1yr
  score = overlap * h.confidence * age_penalty
  # Add freshness caveat to output
  caveat = memory_freshness_caveat(path.stat().st_mtime)
```

---

## Wave 3: ORCHESTRATION

| # | Task | File | Change |
|---|------|------|--------|
| T08 | Wire Coordinator into mission_runner | `cex_mission_runner.py` | Add synthesis gate between waves using `CexCoordinator.synthesize()` |
| T09 | Wire agent_spawn into dispatch.sh | `_spawn/dispatch.sh` | Before subprocess launch, call `cex_agent_spawn.py --validate` to pre-check agent config |

**Gate**: Run `python _tools/cex_mission_runner.py --help` (no crash) + dispatch.sh solo mode test.

### T08 Detail

```
CURRENT (mission_runner, between waves):
  # raw: finish wave N -> start wave N+1, no synthesis

PROPOSED:
  from cex_coordinator import CexCoordinator
  coord = CexCoordinator(mission_id=mission_id)
  # After each wave completes:
  results = collect_wave_signals(wave_n)
  synthesis = coord.synthesize(results)
  if not synthesis.passed:
      print(f"Synthesis gate FAILED: {synthesis.issues}")
      # Retry wave or abort
  # Proceed to wave N+1
```

### T09 Detail

```
CURRENT (dispatch.sh solo):
  exec claude --model $MODEL -p "..." 

PROPOSED (add pre-flight):
  python _tools/cex_agent_spawn.py --validate --kind $KIND --nucleus $NUCLEUS
  if [ $? -ne 0 ]; then echo "Agent validation failed"; exit 1; fi
  exec claude --model $MODEL -p "..."
```

---

## Wave 4: REVERSE COMPILER + NEW KIND

| # | Task | File | Change |
|---|------|------|--------|
| T10 | Extend cex_compile.py with reverse-path targets | `cex_compile.py` | Add `--target` flag: `cursorrules`, `claude-md`, `customgpt`, `mcp` |
| T11 | Create memory_type builder | `archetypes/builders/memory-type-builder/` | 13 ISOs for the new kind (115th) |
| T12 | End-to-end smoke test | `cex_flywheel_audit.py` | Add E2E section: real intent through full pipeline |

**Gate**: `cex_compile.py --target claude-md` produces valid CLAUDE.md from CEX artifacts.

### T10 Detail: Reverse Compiler

```
CURRENT: cex_compile.py goes .md examples -> compiled YAML (inward)
PROPOSED: add outward path: compiled YAML -> target format

Targets:
  --target cursorrules   -> .cursorrules (flat markdown rules file)
  --target claude-md     -> CLAUDE.md (structured project context)
  --target customgpt     -> JSON for OpenAI GPT Builder
  --target mcp           -> MCP server tool definitions
  --target prompts-ts    -> TypeScript prompts.ts (like OpenClaude)

Each target has a renderer that:
  1. Reads compiled artifacts from P03, P04, P08, P11
  2. Reads brand config
  3. Reads active builder ISOs
  4. Renders into target format
```

---

## Dependency Graph

```
Wave 0 (T00: snapshot)
  |
  v
Wave 1 (T01 + T02 + T03 + T04) -- all independent, parallel
  |
  v
Wave 2 (T05 + T06 independent, T07 depends on T05+T06)
  |
  v
Wave 3 (T08 + T09 independent)
  |
  v
Wave 4 (T10 + T11 independent, T12 depends on all above)
```

## GDP Decisions Needed (USER scope)

| # | Decision | Options | Default |
|---|----------|---------|---------|
| D1 | SkillLoader fallback strategy | `try/except` (graceful) vs `require` (hard fail) | `try/except` |
| D2 | GDP blocking behavior | `raise` (halt pipeline) vs `warn` (log and continue) | `raise` (spec says GDP before dispatch) |
| D3 | Memory age penalty curve | `linear` vs `exponential` vs `step` | `linear` (simplest) |
| D4 | Reverse compiler first target | `claude-md` vs `cursorrules` vs `customgpt` | `claude-md` (we eat our own dogfood) |

---

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| crew_runner regression | HIGH (all builds break) | Every wire wrapped in try/except with fallback to current behavior |
| 8f_runner GDP blocks on pending decisions | MED (pipeline halts) | `--no-gdp` flag to bypass in CI/batch |
| SkillLoader sort order != glob sort order | LOW (different ISO order in prompt) | Compare output of both paths in T01 |
| Router needs API keys at import time | MED (fails in offline dev) | Router already has `is_configured()` check + fallback |

## Estimated Effort

| Wave | Tasks | Complexity | Est. Lines Changed |
|------|-------|-----------|-------------------|
| W0 | 1 | trivial | 0 |
| W1 | 4 | medium (surgical edits in 2 files) | ~120 lines |
| W2 | 3 | medium (surgical edits in 3 files) | ~80 lines |
| W3 | 2 | medium-high (orchestration logic) | ~100 lines |
| W4 | 3 | high (new module + new builder) | ~400 lines |
| **TOTAL** | **13** | | **~700 lines** |

## Acceptance Criteria

1. `cex_flywheel_audit.py audit` still 101/101 WIRED after all waves
2. `cex_8f_runner.py --execute --kind agent --intent "cria agente de vendas"` uses Router+SkillLoader+GDP
3. `cex_memory_select.py --query "..." --builder agent-builder` returns age-weighted results
4. `cex_mission_runner.py` inserts synthesis gates between waves
5. `cex_compile.py --target claude-md` produces readable output
6. No existing test regressions (cex_system_test.py, cex_doctor.py)
