---
description: "Full lifecycle shortcut — plan+guide+spec+grid+consolidate in one. Usage: /mission <goal>"
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

## Post-Execution

After all nuclei signal complete:

```bash
bash _spawn/dispatch.sh status
python _tools/cex_doctor.py
```

Show user what was produced. Highlight any `auto_filled` decisions for review.
