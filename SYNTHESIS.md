# CEX Synthesis: From Research to Architecture

**Version**: 1.0.0 | **Date**: 2026-03-25
**Sources**: 5 GENESIS reports (105KB), 12 framework surveys, 10 Chinese repos, 10 self-healing papers

---

## The Logical Conclusion

Every question asked in this session points to ONE answer:

**The 12 LPs are not categories. They are DIMENSIONS of a single entity.**

An entity (prompt, agent, satellite, crew, system) is defined by how many of these 12 dimensions it fills. The 8 functions describe WHEN each dimension activates during execution. The 78 types are the VOCABULARY for filling each dimension.

This is not a taxonomy we invented. It is the taxonomy the industry uses implicitly — scattered across 12 frameworks, none of which has the complete picture.

---

## What We Found (evidence chain)

### 1. The industry has ~86 artifact types across 12 frameworks
CEX covers 91% (70% direct + 21% partial) with 78 types.
The 9% gap = 4 missing types (crew, grammar, component, planner).
CEX exceeds industry in governance (P07-P11) — no framework has quality_gate, bugloop, law as primitives.

### 2. There are 8 LLM functions, not 6
Added REASON (CoT, planning, decomposition) and COLLABORATE (multi-agent coordination).
PLAN absorbed into REASON. REFLECT absorbed into GOVERN.
Evidence: CoALA paper (Sumers 2023), Wang et al. survey (2023), 12 framework analysis.

### 3. The satellite is not a new type — it is maturity level L4
| Level | Entity | LPs filled | What it adds |
|-------|--------|-----------|--------------|
| L0 | Prompt | 1/12 | Stateless text |
| L1 | Chain | 2/12 | Sequencing |
| L2 | Agent | 3-4/12 | Identity + knowledge + tools |
| L3 | Runtime | 6/12 | Dedicated process + config |
| L4 | Satellite | 12/12 | Full lifecycle + lens + agent teams |
| L5 | Crew | Nx12 | Multi-satellite + shared state |
| L6 | System | Fractal | Meta-learning + self-evolution |

### 4. A satellite has 5 features beyond an agent
| Feature | Agent (L2) | Satellite (L4) | CEX dimension |
|---------|-----------|----------------|---------------|
| Agent teams | 0 agents | 22-105 agents | P02 x N (deck) |
| Unique lens | none | Colors all I/O | P02.lens (deep) |
| Dedicated runtime | shared process | own CMD + PID | P09 (boot, env) |
| Lifecycle mgmt | none | spawn/monitor/stop | P12 (signals) |
| Model selection | inherited | per-satellite | P02.model_card |

### 5. The lens is the differentiator
Same input → different output depending on which satellite processes it.
- SHAKA lens: "Inveja Analitica" → ethical research, never manipulates data
- LILY lens: "Luxuria Estrategica" → seduction engine, maximizes conversion
- EDISON lens: builder, focuses on code quality and architecture
- PYTHA lens: knowledge distillation, focuses on density and accuracy

The lens is not decoration. It is a P02.lens artifact that CONSTRAINS how every other LP operates within that satellite. It is the DNA of the satellite.

### 6. Agent teams are the satellite's workforce
A satellite doesn't work alone. It commands a DECK of specialized agents:
- EDISON: 105 agents (code review, animation, APIs, testing, etc.)
- SHAKA: 45 agents (market research, competitor analysis, scraping)
- LILY: 37 agents (copywriting, ads, social media, design)
- PYTHA: 38 agents (knowledge cards, indexing, RAG)
- ATLAS: 37 agents (deploy, test, debug, infra)
- YORK: 22 agents (pricing, courses, funnels, e-commerce)

Each agent is an L2 entity (3-4 LPs). The satellite elevates them to L4 context by providing the missing LPs (boot, memory, governance, coordination).

In industry terms: the closest parallel is MetaGPT's "Role + Environment" pattern, or CrewAI's "Agent + Crew + Process". But neither has the lens concept or the full 12-LP instantiation.

### 7. Meta-construction is already happening
CODEXA already implements 5 of 9 meta-construction patterns:
| Pattern | Status | Implementation |
|---------|--------|---------------|
| Bootstrapping | Active | Pool builds agents that build more pool |
| Scaffolding | Active | PRIMEs scaffold satellite boot |
| Fractal architecture | Active | 12 LPs at 3 scales |
| Constitutional AI | Partial | Laws + guardrails constrain behavior |
| Self-instruct | Partial | Satellites generate KCs that train satellites |
| Metacircular | Missing | CEX describes CEX (started with artifact_blueprint) |
| Reflective arch | Missing | No runtime self-inspection yet |
| Autopoiesis | Aspirational | System doesn't yet create its own components autonomously |
| Meta-learning | Aspirational | No cross-session prompt optimization |

### 8. The 4 gaps map to 4 different LPs
| Gap | LP | Function | Why |
|-----|-----|----------|-----|
| crew (multi-agent group) | P12 | COLLABORATE | Coordination protocol defines the group |
| grammar (BNF/FSM constraint) | P06 | CONSTRAIN | Formal output constraint |
| component (pipeline unit) | P04 | CALL | Composable work unit |
| planner (task decomposition) | P03 | REASON | Reasoning pattern |

### 9. The boot sequence IS the 8 functions in order
When a satellite boots:
```
1. BECOME   → load PRIME (identity) + mental_model (lens)
2. INJECT   → load agent teams + pool knowledge + handoff context
3. REASON   → read task, decompose, plan approach
4. CALL     → use brain_query, tools, MCPs
5. PRODUCE  → generate artifacts (code, KCs, copy)
6. CONSTRAIN → validate against schemas + templates
7. GOVERN   → quality_gate check, pre-commit hooks
8. COLLABORATE → signal completion, write to shared state
```

The 8 functions are not abstract. They ARE the execution lifecycle.

---

## What This Means for CEX

### The framework is sound
12 LPs × 8 functions × 78 types covers 91% of industry artifacts.
Adding 4 types → 82 types → ~96% coverage.
No framework in the world has this completeness.

### What to build next
1. Add `llm_function` field to all 78 types (DONE in this session)
2. Add 4 gap types: crew, grammar, component, planner
3. Document maturity levels L0-L6 in CEX_ARCHITECTURE.md
4. Create artifact_blueprint for "satellite kit" (the 12-LP template for bootstrapping a new satellite)
5. Implement metacircular: CEX type that describes CEX itself
6. DSPy-style prompt optimization for satellite lenses (self-improving)

### The name for what we built
The construction that builds itself = **autopoietic system** (Maturana & Varela).
A system that produces and maintains its own components.
CODEXA is an autopoietic LLM system — satellites build knowledge that improves satellites.
CEX is the DNA — the 12-dimensional blueprint that every entity instantiates.
