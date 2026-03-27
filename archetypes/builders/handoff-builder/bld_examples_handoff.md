---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of handoff artifacts
pattern: few-shot learning for delegation instruction packaging
---

# Examples: handoff-builder

## Golden Example

INPUT: "Create handoff for edison to build 3 archetype builders in wave 19"

OUTPUT (`p12_ho_wave19_builders.md`):
```yaml
---
id: p12_ho_wave19_builders
kind: handoff
lp: P12
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "stella"
satellite: "edison"
mission: "wave19"
autonomy: "full"
quality_target: 9.0
domain: "orchestration"
quality: null
tags: [handoff, edison, wave19, builders, archetype]
tldr: "Edison builds 3 archetype builders (session-state, dag, handoff) with 13 ISO each"
dependencies: []
seeds: [builder, archetype, session_state, dag, handoff, P10, P12]
agent: "builder-builder"
batch: "batch_06"
wave: 19
keywords: [wave19, builders, archetype, edison]
linked_artifacts:
  primary: "archetypes/builders/"
  related: ["archetypes/builders/_builder-builder/", "archetypes/SEED_BANK.yaml"]
---
```

# EDISON — WAVE19: Build 3 Builders
**Full Autonomy** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## Context
Wave 19 requires 3 new archetype builders for types session_state (P10),
dag (P12), and handoff (P12). Each builder follows the 13-ISO pattern
established by _builder-builder. Reference builders: signal-builder, workflow-builder.

## Tasks
### Step 1: Read References
Read _builder-builder/BUILDER_NORMS.md, signal-builder/, and workflow-builder/.

### Step 2: Build session-state-builder
Create 13 ISO files in archetypes/builders/session-state-builder/.

### Step 3: Commit session-state-builder
Run: git add archetypes/builders/session-state-builder/ && git commit

### Step 4: Build dag-builder
Create 13 ISO files in archetypes/builders/dag-builder/.

### Step 5: Commit dag-builder
Run: git add archetypes/builders/dag-builder/ && git commit

### Step 6: Build handoff-builder
Create 13 ISO files in archetypes/builders/handoff-builder/.

### Step 7: Commit handoff-builder
Run: git add archetypes/builders/handoff-builder/ && git commit

## Scope Fence
- SOMENTE: archetypes/builders/session-state-builder/, archetypes/builders/dag-builder/, archetypes/builders/handoff-builder/
- NAO TOQUE: archetypes/builders/_builder-builder/, archetypes/builders/signal-builder/, P12_orchestration/_schema.yaml

## Commit
```bash
git add archetypes/builders/session-state-builder/
git commit -m "archetype: session-state-builder -- 13 ISO (P10, Wave 19)"
git add archetypes/builders/dag-builder/
git commit -m "archetype: dag-builder -- 13 ISO (P12, Wave 19)"
git add archetypes/builders/handoff-builder/
git commit -m "archetype: handoff-builder -- 13 ISO (P12, Wave 19)"
```

## Signal
```bash
python -c "from records.core.python.signal_writer import write_signal; write_signal('edison', 'complete', 9.0)"
```

WHY GOLDEN: filename `p12_ho_*`, 19+ frontmatter fields, all 5 body sections, specific tasks, SOMENTE+NAO TOQUE, exact git commands, signal mechanism, no prompt/event/routing drift.

## Anti-Example

BAD OUTPUT (`p03_ap_build_stuff.md`):
```yaml
---
id: p03_ap_build_stuff
kind: action_prompt
lp: P03
persona: "You are a helpful builder"
response_format: "markdown"
---

Build some archetype builders. Use your best judgment.
Make sure they are good quality. Commit when done.
Try to finish everything today if possible.
```

FAILURES:
1. wrong kind: `action_prompt` instead of `handoff` (H02)
2. wrong pillar: `P03` instead of `P12` (H01)
3. wrong id prefix: `p03_ap_` instead of `p12_ho_` (H01)
4. contains `persona`: prompt engineering -> action_prompt drift (H08)
5. contains `response_format`: prompt constraint -> action_prompt drift (H08)
6. missing required fields: `satellite`, `mission`, `autonomy`, `quality_target`, `quality`, `tags`, `tldr` (H03)
7. vague tasks: "Build some archetype builders" is not specific (H09)
8. no scope fence section: missing SOMENTE/NAO TOQUE (H10)
9. no commit section: missing exact git commands (H10)
10. no signal section: missing completion mechanism (H10)
