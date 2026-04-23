---
description: "Full lifecycle shortcut — plan+guide+spec+grid+consolidate in one. Usage: /mission <goal>"
quality: 9.0
title: "Mission"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_orchestration_nucleus
  - skill_guided_decisions
  - p01_kc_orchestration_best_practices
  - ctx_cex_new_dev_guide
  - p12_wf_orchestration_pipeline
  - dispatch
  - auto-accept-handoff
  - p02_agent_admin_orchestrator
  - p08_ac_orchestrator
  - agent_card_n07
---

# /mission — The Full Lifecycle

Shortcut that runs the entire workflow: `/plan` → `/guide` → `/spec` → `/grid` → `/consolidate`.

For granular control, run each command separately.
For "just do everything", use `/mission`.

## Phase 1: GDP — Guided Decisions (co-pilot)

Before dispatching anything, identify what SUBJECTIVE decisions this mission needs.

### Step 1: Decompose

```bash
python _tools/cex_mission.py decompose "$ARGUMENTS"
```

### Step 2: Identify Decision Points

Look at the decomposed tasks. For each, ask:
- Does this involve SUBJECTIVE choices? (tone, style, audience, positioning, layout, naming)
- Would two different humans make different choices here?
- If yes → it's a DP.

Common DPs by nucleus:

| Nucleus | Typical DPs |
|---------|------------|
| N01 | Research scope, depth, which competitors to focus on |
| N02 | Layout style, color palette, visual tone, responsive strategy |
| N03 | (rarely — mostly mechanical) |
| N04 | Documentation depth, audience level (beginner/advanced) |
| N05 | Platform choice (Railway/Vercel), scaling strategy, cost trade-offs |
| N06 | Everything — brand is 100% subjective |

### Step 3: Present DPs to user

Use the GDP format from `skill_guided_decisions.md`:

```
━━━ DP 1/4: Target Audience ━━━

Who is this for?

  1. 👩‍💻 Technical — developers who read docs
     → Best if: developer tool, API product

  2. 👔 Business — decision-makers who skim
     → Best if: SaaS, enterprise

  3. 🌱 Beginners — people learning from scratch
     → Best if: courses, tutorials, consumer app

  ★ Recommended: 2 (based on your brand: "B2B SaaS for agencies")

  [Type number or describe]: ▌
```

Present 2-3 DPs at a time. Show preview between rounds.

### Step 4: Write Decision Manifest

After all DPs are answered:

```bash
# The manifest is written to:
# .cex/runtime/decisions/decision_manifest.yaml
```

Fill in from template at `.cex/runtime/decisions/manifest_template.yaml`.
Set `status: locked`.

Show the user the Final Review DP (see skill_guided_decisions.md).

---

## Phase 2: Autonomous Execution (no more questions)

Once manifest is locked and user confirms:

### Option A: Single nucleus

```bash
bash _spawn/dispatch.sh solo n03 "task description"
```

The handoff auto-includes the manifest reference.

### Option B: Full grid (parallel)

```bash
bash _spawn/dispatch.sh grid MISSION_NAME
```

All nuclei read the same manifest. Same decisions. Consistent output.

### Option C: Sequential in-session

```bash
python _tools/cex_mission.py execute "$ARGUMENTS" --complexity standard
```

## Complexity Levels

- `minimal` — 4 artifacts: agent, system_prompt, knowledge_card, agent_card
- `standard` — 7 artifacts: + dispatch_rule, workflow, quality_gate
- `full` — 12 artifacts: + scoring_rubric, prompt_template, action_prompt, pattern, dag

## Examples

```
/mission build a landing page for our SaaS
  → GDP: 4 DPs (audience, layout, CTA style, hero message)
  → Dispatch: N02 (frontend) + N06 (copy in brand voice)

/mission create competitive analysis for our market
  → GDP: 2 DPs (which competitors, depth level)
  → Dispatch: N01 (research)

/mission launch full brand + website + pricing
  → GDP: 8-10 DPs (brand identity, audience, tone, layout, pricing model, platform)
  → Dispatch: N06 first (brand), then N02+N05+N01 parallel

/mission build a knowledge card about React patterns
  → GDP: 0 DPs (factual, no subjective choices)
  → Dispatch: N03 directly
```

## Phase 2.5: Continuous Monitoring (between waves)

After EVERY dispatch, N07 IMMEDIATELY starts a Monitor:

```python
# Archive stale signals from prior waves
# mv .cex/runtime/signals/signal_n0*.json .cex/runtime/signals/archive/

Monitor(
  description="Wave N dispatch health",
  persistent=True,
  timeout_ms=3600000,
  command="""
cd /c/Users/CEX/Documents/GitHub/cex
NUCLEI="n03 n04"  # <-- dispatched nuclei for this wave
echo "[MONITOR] Started: watching $NUCLEI"
while true; do
  for nuc in $NUCLEI; do
    NUC_UPPER=$(echo $nuc | tr 'a-z' 'A-Z')
    COMMITS=$(git log --oneline --since="90 seconds ago" --all 2>/dev/null | grep -c "\\[$NUC_UPPER\\]" || true)
    if [ "$COMMITS" -gt 0 ]; then
      MSG=$(git log --oneline --since="90 seconds ago" --all 2>/dev/null | grep "\\[$NUC_UPPER\\]" | head -1)
      echo "[MONITOR] $NUC_UPPER committed: $MSG"
    fi
    SIG=$(ls .cex/runtime/signals/signal_${nuc}_*.json 2>/dev/null | wc -l || true)
    if [ "$SIG" -gt 0 ]; then
      echo "[MONITOR] $NUC_UPPER COMPLETE (signal)"
    fi
  done
  # Count completions
  DONE=0
  for nuc in $NUCLEI; do
    SIG=$(ls .cex/runtime/signals/signal_${nuc}_*.json 2>/dev/null | wc -l || true)
    [ "$SIG" -gt 0 ] && DONE=$((DONE + 1))
  done
  TOTAL=$(echo $NUCLEI | wc -w)
  if [ "$DONE" -ge "$TOTAL" ]; then
    echo "[MONITOR] ALL $TOTAL NUCLEI COMPLETE -- ready for /consolidate"
    break
  fi
  sleep 60
done
"""
)
```

**N07 keeps working** between monitor notifications:
- Write handoffs for next wave
- Audit existing artifacts
- Update memory, specs, plans
- Run doctor checks

**On "ALL COMPLETE" notification**: immediately consolidate, then dispatch next wave.

**Multi-wave continuous flow:**
```
Wave 1: dispatch -> Monitor -> [N07 works] -> ALL COMPLETE notification
  -> /consolidate -> archive signals
Wave 2: dispatch -> Monitor -> [N07 works] -> ALL COMPLETE notification
  -> /consolidate -> archive signals
Wave N: dispatch -> Monitor -> [N07 works] -> ALL COMPLETE notification
  -> final /consolidate
```

N07 NEVER goes idle. Monitor handles the waiting. N07 handles the working.

---

## Phase 3: Post-Execution (auto-consolidate)

After all nuclei signal complete (detected by Monitor):

```bash
# 1. Stop completed processes
bash _spawn/dispatch.sh stop

# 2. Check what landed
git log --oneline -10

# 3. Compile everything
python _tools/cex_compile.py --all

# 4. AutoResearch: evolve all new/low artifacts (AUTOMATIC)
# This is the Karpathy loop: score -> improve -> keep/discard
python _tools/cex_evolve.py sweep --target 8.5 --max-rounds 2

# 5. Doctor check
python _tools/cex_doctor.py

# 6. Commit consolidation
git add -A && git commit -m "[N07] consolidate: mission complete"
```

The evolve sweep runs **automatically** -- user doesn't need to know about it.
It catches quality:null artifacts, improves what it can, scores everything.
Show user what was produced. Highlight any `auto_filled` decisions for review.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_orchestration_nucleus]] | related | 0.45 |
| [[skill_guided_decisions]] | related | 0.43 |
| [[p01_kc_orchestration_best_practices]] | related | 0.40 |
| [[ctx_cex_new_dev_guide]] | related | 0.38 |
| [[p12_wf_orchestration_pipeline]] | related | 0.36 |
| [[dispatch]] | related | 0.33 |
| [[auto-accept-handoff]] | related | 0.33 |
| [[p02_agent_admin_orchestrator]] | related | 0.32 |
| [[p08_ac_orchestrator]] | related | 0.32 |
| [[agent_card_n07]] | related | 0.31 |
