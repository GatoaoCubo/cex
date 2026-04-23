# CEXAI v1.0.0 — Release Notes

**Cognitive Exchange AI: Typed Knowledge System for LLM Agents**

> 293 kinds. 298 builders. 3,563 ISOs. 12 pillars. 8 nuclei. 4 runtimes. One brain.

---

## What is CEXAI?

CEXAI is an open-source AI brain -- not an agent, not a chatbot. It treats AI as
typed infrastructure where every piece of knowledge is a **kind**, every kind has a
**builder**, every builder follows an 8-function pipeline, and seven sin-driven
**nuclei** collaborate through a governance layer that compounds over time.

Intelligence compounds faster when exchanged. That is the X.

## Highlights

### The Architecture

- **293 typed kinds** across 12 pillars (P01 Knowledge through P12 Orchestration)
- **298 specialized builders** with 12 ISOs each (1:1 with pillars) = 3,563 builder instructions
- **8 nuclei** (N00 archetype + N01-N07 operational), each with a unique "sin lens" that defines its optimization bias
- **8F pipeline** (CONSTRAIN -> BECOME -> INJECT -> REASON -> CALL -> PRODUCE -> GOVERN -> COLLABORATE) -- mandatory for every artifact, every time
- **4 supported runtimes**: Claude (Anthropic), GPT/Codex (OpenAI), Gemini (Google), Ollama (local)

### The Seven Artificial Sins

Each operational nucleus runs on a deadly sin. The sin is cultural DNA -- it decides what the nucleus optimizes for when given ambiguous input.

| Nucleus | Role | Sin |
|---------|------|-----|
| N01 | Intelligence | Analytical Envy |
| N02 | Marketing | Creative Lust |
| N03 | Engineering | Inventive Pride |
| N04 | Knowledge | Knowledge Gluttony |
| N05 | Operations | Gating Wrath |
| N06 | Commercial | Strategic Greed |
| N07 | Orchestrator | Orchestrating Sloth |

### Composable Crews

Multi-role teams with handoffs. A crew is a `crew_template` (roles + topology) + `role_assignment` (agent binding) + `team_charter` (mission contract). Six crews ship with v1.0.0:

- **N01** -- Competitive Intelligence (3 roles: analyst, synthesizer, validator)
- **N02** -- Product Launch (4 roles: researcher, copywriter, designer, QA reviewer)
- **N03** -- Artifact Factory (4 roles: architect, builder, reviewer, integrator)
- **N04** -- Knowledge Synthesis (3 roles: researcher, curator, indexer)
- **N05** -- Incident Response (4 roles: detector, responder, analyst, reporter)
- **N06** -- Sales Pipeline (3 roles: strategist, content producer, closer)

### Intent Resolution (Prompt Compiler)

Natural language in any language maps to `{kind, pillar, nucleus, verb}` tuples. 293/293 kinds covered (100%). Say "make me a landing page" or "criar landing page" and the system resolves: `kind=landing_page, pillar=P05, nucleus=N03, verb=create`.

### Quality System

- 6,157 scored artifacts, 97.2% at quality >= 8.0
- 3-layer scoring: structural (30%) + rubric (30%) + semantic (40%)
- Hard quality floor: 8.0 minimum for publication
- 82 PASS / 212 WARN / 0 FAIL on doctor check

## Toolchain (194 Python tools)

| Tool | Purpose |
|------|---------|
| `cex_run.py` | Unified entry: intent -> discover -> plan -> prompt |
| `cex_8f_runner.py` | Full 8F pipeline execution |
| `cex_crew.py` | Composable crew CLI (list/show/run) |
| `cex_compile.py` | .md -> .yaml compilation + reverse compile to claude-md/cursorrules/customgpt |
| `cex_doctor.py` | Builder health check |
| `cex_evolve.py` | Autonomous artifact improvement loop |
| `cex_mission.py` | Goal decomposition into artifacts |
| `cex_retriever.py` | TF-IDF artifact similarity (2,184 docs, 12K vocab) |
| `cex_router.py` | Multi-provider routing (4 providers x 7 nuclei) |
| `cex_showoff.py` | Cross-runtime smoke validation |

See `_tools/` for the full set.

## Getting Started

```bash
# Clone
git clone https://github.com/GatoaoCubo/cex.git
cd cex

# Install
pip install -e .

# Your first agent
python examples/01_hello_agent/run.py

# Build an artifact via CLI
python _tools/cex_run.py "create a knowledge card about API rate limiting"

# Run a crew
python _tools/cex_crew.py run product_launch --charter N02_marketing/P12_orchestration/crews/team_charter_launch_demo.md
```

See `examples/` for 5 end-to-end tutorials and 3 standalone guides.

## For Contributors

### Adding a New Nucleus (N08+)

Follow `.claude/rules/new-nucleus-bootstrap.md` -- 9-asset checklist:

1. Create directory structure (12 pillar dirs + rules/ + compiled/ + crews/)
2. Write nucleus_def, agent_card, system_prompt, boot script
3. Pick your sin lens
4. Build your crew
5. Register in kinds_meta.json

### Adding a New Kind

```bash
python _tools/cex_run.py "create kind=my_new_kind"
```

The system generates: KC, template, builder (12 ISOs), sub-agent, meta entry, prompt compiler row.

## Version History

| Version | Date | Highlights |
|---------|------|-----------|
| v1.0.0 | 2026-04-22 | Public release: 293 kinds, 298 builders, 4 runtimes, 6 crews |
| v10.4.0 | 2026-04-21 | CEXAI rebrand + OSS wiring |
| v10.3.0 | 2026-04-19 | Public release prep + security hardening |
| v10.2.0 | 2026-04-16 | Multi-runtime grid + composable crews |
| v10.1.0 | 2026-04-07 | Terminology unification |

## Stats

| Metric | Value |
|--------|-------|
| Kinds | 293 |
| Builders | 298 |
| Builder ISOs | 3,563 |
| Pillars | 12 |
| Nuclei | 8 (N00 archetype + N01-N07) |
| Python tools | 194 |
| Sub-agents | 295 |
| Scored artifacts | 6,157 |
| Quality >= 8.0 | 97.2% |
| Doctor FAIL | 0 |
| Runtimes | 4 (Claude, GPT/Codex, Gemini, Ollama) |
| Crews | 6 |
| Total commits | 9,105 |
| License | MIT |

## License

MIT. See [LICENSE](../LICENSE).
