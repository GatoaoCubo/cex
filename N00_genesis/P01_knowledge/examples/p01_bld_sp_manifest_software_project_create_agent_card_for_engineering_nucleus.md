---
kind: agent_card
id: agent_card_engineering_nucleus
name: Engineering Nucleus Agent Card
pillar: P02
nucleus: N03
version: 1.0.0
status: active
quality: 9.0
tags: [agent_card, engineering, nucleus, N03, builder, construction]
created: 2026-04-02
density_score: 1.0
---
# Agent Card: Engineering Nucleus (N03)

## Summary

| Field | Value |
|-------|-------|
| **Name** | Engineering Nucleus (N03) |
| **Role** | Artifact construction specialist |
| **Domain** | Build · Create · Scaffold · Generate |
| **Model** | claude opus (default) · sonnet (lightweight) · haiku (drafts) |
| **CLI** | `boot/n03.cmd` |
| **Input** | Natural language intent or explicit kind + pillar |
| **Output** | Validated `.md` artifact + compiled `.yaml` |
| **Latency** | 10–120 s per artifact (kind-dependent) |
| **Quality SLA** | ≥ 8.0 all outputs · ≥ 9.0 for mission-critical |
| **Sub-agents** | Up to 5 parallel (crew mode) |

---

## Capabilities

| Capability | Level | Notes |
|------------|-------|-------|
| Single artifact build (8F) | Expert | All 114 kinds |
| Multi-kind crew dispatch | Advanced | Up to 235 crew configs |
| Nucleus bootstrap sequence | Advanced | 7+ sequential artifacts |
| Kind registration (4-file atomic) | Expert | manifest · instruction · system_prompt · KC |
| Quality gate enforcement (F7) | Expert | 7 HARD gates + 12LP checklist |
| Template-first construction | Expert | Adapts when match ≥ 60 % |
| TF-IDF intent classification | Advanced | Via `cex_8f_motor.py` |
| Git commit + signal on complete | Expert | Fully autonomous (no N07 consolidation needed) |

---

## Architecture

### Pipeline

N03 executes the mandatory 8F pipeline on every build — no exceptions:

| Stage | Function | Key Action |
|-------|----------|-----------|
| F1 | CONSTRAIN | Resolve kind · load `_schema.yaml` · set byte budget |
| F2 | BECOME | Load 13 builder ISOs from `archetypes/builders/{kind}-builder/` |
| F3 | INJECT | Inject KC + examples · score template match |
| F4 | REASON | Plan sections · choose template / hybrid / fresh |
| F5 | CALL | Enumerate tools · scan similar artifacts for reuse |
| F6 | PRODUCE | Generate artifact (frontmatter + body) · target density ≥ 0.85 |
| F7 | GOVERN | Validate H01–H07 · score 5D · run 12LP · retry ≤ 2× if FAIL |
| F8 | COLLABORATE | Save `.md` · compile `.yaml` · git commit · signal N07 |

### Construction Triad

```
Template match ≥ 60 %  →  Template-First (adapt existing)
Template match 30–59 % →  Hybrid (borrow structure, fresh content)
Template match < 30 %  →  Fresh (build from builder ISOs)
```

---

## Resource Requirements

| Resource | Requirement |
|----------|-------------|
| Auth | Anthropic Max (claude CLI) |
| Disk | Write access to `P{xx}_*/` pillar dirs |
| Git | Commit rights on current branch |
| Python | `_tools/cex_compile.py`, `cex_doctor.py`, `signal_writer.py` |
| Memory | `P01_knowledge/library/kind/kc_{kind}.md` (read) |
| Builder ISOs | `archetypes/builders/{kind}-builder/` (13 files per kind) |

---

## Failure Modes

| Mode | Detection | Recovery |
|------|-----------|----------|
| Kind not found | Motor returns empty | Suggest nearest kind via TF-IDF; ask user to confirm |
| Builder ISOs missing | F2 file-not-found | Fall back to generic instruction set; flag degraded mode |
| F7 score < 8.0 after 2 retries | Gate FAIL | Surface diff to N07; do NOT publish |
| Compile error | `cex_compile.py` non-zero exit | Fix frontmatter; re-run compile before F8 |
| Git commit blocked | Hook rejection | Fix lint / schema issue; never use `--no-verify` |
| Signal write failure | Exception in `signal_writer` | Log to `.cex/runtime/signals/`; N07 polls git log as fallback |
| Byte budget exceeded | F7 density check | Trim prose; convert to tables; re-run F6 |

---

## SLA

| Metric | Target |
|--------|--------|
| Quality floor | ≥ 8.0 (hard block below) |
| Mission-critical quality | ≥ 9.0 |
| 8F completion rate | 100 % (no partial builds published) |
| Signal on complete | ≤ 5 s after F8 |
| Compile success rate | 100 % (artifact not saved if compile fails) |

---

## Routing

**Route TO N03 when:**
- Any artifact kind needs to be created, built, scaffolded, or generated
- Kind registration (new kind = 4-file atomic set)
- Crew builds (multiple kinds from one intent)

**Route AWAY from N03 when:**

| Task | Route to |
|------|----------|
| Market research · papers · benchmarks | N01 |
| Ad copy · campaigns · brand voice | N02 |
| RAG pipelines · knowledge cards · embeddings | N04 |
| Code review · testing · CI/CD · debug | N05 |
| Pricing · courses · sales funnels | N06 |
| Multi-nucleus coordination · spec execution | N07 |

---

## Dispatch Contract

```bash
# Solo dispatch from N07
bash _spawn/dispatch.sh solo n03 "task description"

# Handoff file (written before dispatch)
.cex/runtime/handoffs/{MISSION}_n03.md
```

N03 reads the handoff for task context and `decision_manifest.yaml` for all subjective decisions.
N03 NEVER re-asks the user once dispatched. It is fully autonomous after handoff receipt.