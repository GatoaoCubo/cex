# 8F Runner Architecture -- Hydrated Plan

**Version**: 2.0.0 | **Date**: 2026-03-29
**Status**: HYDRATED | **Supersedes**: v1.0

---

## 1. WHAT EXISTS TODAY (Honesty)

### cex_intent.py (533 loc)
Composes 1 monolithic prompt. ZERO intermediate processing.
The 8F are LABELS, not steps. The LLM receives everything at once.

### cex_crew_runner.py (650 loc)
Iterates functions by position, has retry + quality gate.
BUT: each function = run these builders. No accumulated state.
No structural validation in F7. No constraints from F1.

### cex_8f_motor.py (900 loc)
PARSE > CLASSIFY > FAN-OUT > PLAN > OUTPUT. Produces JSON plan.
DOES NOT CHANGE.

---

## 2. KEY DIFFERENCE

TODAY: load ALL ISOs -> compose 1 prompt -> 1 LLM call -> done

RUNNER:
  F1 load constraints (schema + bld_schema + bld_config)
  F2 load identity (bld_system_prompt + bld_manifest)
  F3 load knowledge (KC library + bld_knowledge_card + bld_examples + bld_memory + bld_architecture)
  F4 LLM plans (CoT: which fields, which decisions) [HAIKU]
  F5 tools if needed (duplicate detection)
  F6 LLM generates with F1-F5 STRUCTURED (bld_instruction + bld_output_template) [SONNET]
  F7 validates (hard gates extracted from bld_quality_gate + schema constraints)
  F8 saves + compiles (bld_collaboration for handoff)

Each F produces a dict that the next one CONSUMES. State ACCUMULATES.

---

## 3. RunState (accumulated state)

```python
@dataclass
class RunState:
    intent: str
    kind: str
    pillar: str
    builder_dir: Path

    # F1 output
    constraints: dict  # {max_bytes, frontmatter_required[], id_pattern, quality_min, naming, config_rules[]}
    # F2 output
    identity: dict     # {system_prompt, builder_name, domain, pillar_boundary}
    # F3 output
    knowledge: dict    # {kc_builder, kc_domains[], few_shots, memory, architecture}
    # F4 output
    reasoning: dict    # {plan, decisions[], model_used}
    # F5 output
    tool_results: dict # {existing_artifacts[], tools_available[]}
    # F6 output
    artifact: str      # raw markdown (frontmatter + body)
    # F7 output
    verdict: dict      # {passed, hard_gates[], issues[], feedback, retries}
    # F8 output
    result: dict       # {path, compiled, committed}
```

---

## 4. ISO -> FUNCTION (Exact Mapping)

Each ISO is read in ONE function. None read twice.

| ISO File | Function | What it extracts |
|----------|----------|-----------------|
| bld_schema | F1 CONSTRAIN | id pattern, field types, output contract |
| bld_config | F1 CONSTRAIN | naming rules, paths, size limits |
| bld_manifest | F2 BECOME | builder name, domain |
| bld_system_prompt | F2 BECOME | persona, identity, rules |
| bld_knowledge_card | F3 INJECT | builder-specific knowledge |
| bld_examples | F3 INJECT | few-shot references |
| bld_memory | F3 INJECT | persistent learnings |
| bld_architecture | F3 INJECT | patterns, dependencies, boundary |
| bld_tools | F5 CALL | available tools list |
| bld_instruction | F6 PRODUCE | step-by-step generation process |
| bld_output_template | F6 PRODUCE | expected output structure |
| bld_quality_gate | F7 GOVERN | hard gates + soft scoring |
| bld_collaboration | F8 COLLABORATE | crew roles, handoff protocol |

---

## 5. PSEUDOCODE PER FUNCTION

### F1 CONSTRAIN (0 LLM calls)
```
load _schema.yaml -> kind constraints (max_bytes, frontmatter_required)
load bld_schema -> extract id_pattern regex from body
load bld_config -> extract naming rules, paths
OUTPUT: state.constraints
```

### F2 BECOME (0 LLM calls)
```
load bld_system_prompt -> strip frontmatter, keep body (persona)
load bld_manifest -> extract title, domain from frontmatter
load _schema.yaml -> kind boundary description
OUTPUT: state.identity
```

### F3 INJECT (0 LLM calls)
```
load bld_knowledge_card -> builder-specific knowledge
lookup KC-Domains from library via feeds_kinds
load bld_examples -> few-shot reference
load bld_memory -> past learnings
load bld_architecture -> patterns, dependencies
OUTPUT: state.knowledge
```

### F4 REASON (1 LLM call - haiku ~$0.001)
```
compose prompt: identity + constraints + knowledge + intent
ask LLM: plan the artifact (fields, decisions, tradeoffs)
OUTPUT: state.reasoning = {plan, decisions[], model_used}
DRY-RUN: saves prompt string instead of calling LLM
```

### F5 CALL (0 LLM calls, v1)
```
load bld_tools -> parse tools table
scan existing artifacts of same kind (duplicate detection)
OUTPUT: state.tool_results = {existing_artifacts[], tools_available[]}
```

### F6 PRODUCE (1 LLM call - sonnet/opus ~$0.02)
```
compose STRUCTURED prompt with labeled sections:
  # IDENTITY (from F2: state.identity.system_prompt)
  # CONSTRAINTS (from F1: max_bytes, id_pattern, required fields)
  # KNOWLEDGE (from F3: KC domains + builder KC + architecture)
  # EXAMPLES (from F3: few_shots)
  # PLAN (from F4: reasoning plan)
  # INSTRUCTION (bld_instruction body -- step-by-step process)
  # TEMPLATE (bld_output_template body -- fill this structure)
  # TASK (user intent + "set quality: null")
  # RETRY FEEDBACK (from F7, if retrying)
call LLM (sonnet for standard, opus for complex)
OUTPUT: state.artifact = raw markdown
DRY-RUN: saves full assembled prompt as state.artifact
```

### F7 GOVERN (0 LLM calls, structural validation)
```
load bld_quality_gate -> parse hard gates table
validate against state.constraints:
  H01: frontmatter parses as YAML?
  H02: id matches state.constraints.id_pattern?
  H03: kind == state.kind?
  H04: quality == null? (never self-score)
  H05: all frontmatter_required fields present?
  H06: body size <= state.constraints.max_bytes?
if ANY gate fails AND retries < 2:
  state.verdict.feedback = specific issues
  return to F6 (retry with feedback injected)
if fails 2x: save as draft + issues report
OUTPUT: state.verdict = {passed, hard_gates[], issues[], feedback, retries}
```

### F8 COLLABORATE (0 LLM calls)
```
if dry_run: save prompt to output_dir, return
determine path from constraints.naming + user topic slug
save artifact to P{XX}/examples/{filename}
run cex_compile on file -> P{XX}/compiled/
OUTPUT: state.result = {path, compiled, committed}
```

---

## 6. LLM CALLS - COST

| Case | F4 | F6 | F7 | Total | Cost |
|------|----|----|----|----|-------|
| dry-run | prompt | prompt | struct | 0 calls | free |
| simple | skip | 1x sonnet | struct | 1 call | ~$0.02 |
| medium | 1x haiku | 1x sonnet | struct | 2 calls | ~$0.03 |
| complex | 1x haiku | 1x opus | judge | 3-4 calls | ~$0.15 |
| retry | - | +1x sonnet | +1 struct | +1 call | +$0.02 |

---

## 7. CLI

```
python cex_8f_runner.py "create chunk config"              # dry-run default
python cex_8f_runner.py "create chunk config" --execute     # with LLM
python cex_8f_runner.py --kind chunk_strategy --execute      # skip classify
python cex_8f_runner.py "create agent" --step 3             # stop at F3
python cex_8f_runner.py "create agent" --verbose            # per-F timing
python cex_8f_runner.py --list-kinds                         # 300 kinds
```

---

## 8. EDGE CASES

| Case | Behavior |
|------|----------|
| kind=generic | Warn, suggest --kind |
| Builder dir missing | Abort with list |
| ISO file missing | Skip with warning |
| No KC match | Use bld_knowledge_card only |
| F7 fails 2x | Save as draft + issues |
| LLM API error | Retry 1x, then save prompt |
| artifact > max_bytes | F7 catches, F6 retries |
| quality != null | F7 catches, F6 retries |
| Multi-kind | Sequential F1-F8 per kind |

---

## 9. RELATIONSHIP WITH TOOLS (19)

| Tool | Status |
|------|--------|
| cex_8f_motor.py | DOES NOT CHANGE (internal import) |
| cex_crew_runner.py | DEPRECATED by runner |
| cex_intent.py | DEPRECATED by runner |
| cex_pipeline.py | COEXISTS (batch) |
| cex_forge.py | COEXISTS (simple) |
| cex_compile.py | DOES NOT CHANGE (F8 uses it) |
| cex_doctor.py | DOES NOT CHANGE (audit) |
| 12 others | DO NOT CHANGE |

Runner IMPORTS: motor (parse, classify, fan_out, kc_library), intent (execute_prompt)

---

## 10. IMPLEMENTATION WAVES

### Wave 1: Core Skeleton (1 builder_agent, ~45 min)
- RunState dataclass
- EightFRunner: f1, f2, f3, f6, f8 (lookup + produce + save)
- Helpers: load_iso, strip_frontmatter, extract_frontmatter_dict
- CLI: argparse (--dry-run, --execute, --kind, --list-kinds, --verbose, --step, --output-dir)
- Test: dry-run chunk_strategy shows correct F6 prompt with all sections

### Wave 2: Intelligence (1 builder_agent, ~30 min)
- f4_reason() with LLM planning call (haiku)
- f7_govern() with 6 hard gates (yaml, id_pattern, kind, quality, required, size)
- Retry loop: F7 fail -> F6 retry with feedback (max 2)
- Test: execute generates valid artifact; F7 rejects bad frontmatter

### Wave 3: Polish + Proof (1 builder_agent, ~30 min)
- f5_call() with duplicate detection
- --verbose timing per function, --step N flag
- Multi-kind sequential execution
- Generate 3 real artifacts: chunk_strategy, agent, eval_dataset
- Write _docs/proof/8F_RUNNER_PROOF.md with metrics

### TOTAL: ~1h45 | 3 sequential waves
### DEPS: PyYAML + anthropic (optional, only for --execute)

---

## 11. SUCCESS METRICS

| Metric | Target |
|--------|--------|
| dry-run has all 6 structured sections | PASS |
| execute passes 6 hard gates | PASS |
| F1 constraints visible in F6 prompt | visible |
| F3 KC content visible in F6 prompt | visible |
| F7 catches bad frontmatter | reject + retry |
| F7->F6 retry fixes issue | 2nd attempt pass |
| verbose shows timing | ms per F |
| 3 proofs valid | doctor PASS |
