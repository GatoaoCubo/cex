# CEX Architecture: 8 Functions x 12 LPs x 78 Types x 7 Maturity Levels

**Version**: 4.0.0 | **Date**: 2026-03-25

---

## The Fractal Insight

CEX is not a list of types. It is a **12-dimensional mold** that applies to ANY LLM entity at ANY scale. The same 12 LPs describe a prompt, an agent, a satellite, a crew, and the entire system. The difference is **how many LPs are filled**.

---

## 8 LLM Functions (the execution pipeline)

Every artifact serves exactly one primary function in the LLM lifecycle:

| # | Function | What it does | When in lifecycle | Primary LPs |
|---|----------|-------------|-------------------|-------------|
| 1 | **BECOME** | Set identity and persona | Boot | P02, P03 |
| 2 | **INJECT** | Provide context to LLM | Pre-generation | P01, P10 |
| 3 | **REASON** | Plan, decompose, think step-by-step | Pre-generation | P03 |
| 4 | **CALL** | Invoke tools and functions | During generation | P04 |
| 5 | **PRODUCE** | Generate text, compose pipelines | Generation | P03, P12 |
| 6 | **CONSTRAIN** | Format and structure output | Post-generation | P05, P06 |
| 7 | **GOVERN** | Evaluate, control, improve quality | Post-generation | P07, P08, P09, P11 |
| 8 | **COLLABORATE** | Coordinate between agents | Inter-agent | P12 |

These 8 functions ARE the execution pipeline. Not metadata — architecture.

---

## 12 Learning Packages (the dimensions)

| LP | Name | Question it answers | Dominant function |
|----|------|-------------------|-------------------|
| P01 | Knowledge | What does it KNOW? | INJECT |
| P02 | Model | WHO is it? | BECOME |
| P03 | Prompt | HOW does it speak? | REASON + CONSTRAIN |
| P04 | Tools | What can it USE? | CALL |
| P05 | Output | What does it DELIVER? | CONSTRAIN |
| P06 | Schema | What CONTRACTS exist? | CONSTRAIN + GOVERN |
| P07 | Evals | How to MEASURE quality? | GOVERN |
| P08 | Architecture | How does it SCALE? | BECOME + GOVERN |
| P09 | Config | How is it CONFIGURED? | GOVERN |
| P10 | Memory | What does it REMEMBER? | INJECT |
| P11 | Feedback | How does it IMPROVE? | GOVERN |
| P12 | Orchestration | How does it COORDINATE? | COLLABORATE |

---

## 7 Maturity Levels (LP completeness)

| Level | Name | LPs filled | What it gains | Industry equivalent |
|-------|------|-----------|---------------|-------------------|
| L0 | Prompt | 1/12 (P03) | Stateless text | OpenAI completion |
| L1 | Chain | 2/12 (P03+P12) | Sequencing | LangChain LCEL |
| L2 | Agent | 3-4/12 (P01+P02+P03+P06) | Identity + knowledge | LangChain Agent |
| L3 | Runtime | 6/12 (+P04+P09+boot) | Dedicated process | Devin, OpenHands |
| L4 | Satellite | 10-12/12 (all) | Full lifecycle | Actor + Microservice + Agent |
| L5 | Crew | Nx12 + shared state | Multi-agent coordination | AutoGen GroupChat, CrewAI Crew |
| L6 | System | Fractal of crews | Meta-learning, self-evolution | (no equivalent) |

### Key insight
A satellite is NOT a new type. It is an agent with ALL 12 LPs instantiated.
The evolution from agent to satellite to system is measured by LP completeness.

---

## 78 Types (the vocabulary)

12 LPs contain 78 types total. Each type has:
- **Primary LLM function** (1 of 8)
- **Layer** (content, spec, prompt, runtime, governance)
- **Max bytes** (enforced by schema)
- **Naming convention** (prefixed by LP code)

See individual `_schema.yaml` files for complete type definitions.

### Type distribution by function
| Function | Types | % | Dominant in |
|----------|-------|---|-------------|
| INJECT | 16 | 21% | P01, P10 |
| BECOME | 6 | 8% | P02, P03 |
| CONSTRAIN | 11 | 14% | P05, P06 |
| CALL | 8 | 10% | P04 |
| REASON | 7 | 9% | P03 |
| PRODUCE | 5 | 6% | P03, P12 |
| GOVERN | 22 | 28% | P07, P09, P11 |
| COLLABORATE | 3 | 4% | P12 |

---

## The Fractal at 3 Scales

```
SYSTEM (CODEXA)          = 12 LPs at system scale
  SATELLITE (EDISON)     = 12 LPs at satellite scale
    AGENT (seo_optimizer) = 3-4 LPs at agent scale
```

Same structure. Different completeness. Same 78 types available at every scale.
