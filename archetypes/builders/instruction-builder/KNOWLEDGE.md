---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for instruction production
sources: runbook engineering, SRE playbooks, IEC 62443, distilled from 5 production instruction prompts
---

# Domain Knowledge: instruction

## Foundational Concept
Instructions are operational recipes — step-by-step procedures that transform a
defined starting state into a defined ending state. The concept draws from SRE
runbooks, manufacturing SOPs, and military operations orders. Key principle:
each step must be atomic (one action), verifiable (can confirm completion),
and reversible (can undo if needed).

## Patterns Distilled from Production Instructions

### 1. The 7-Section Structure That Works

All 5 production instructions follow an identical macro-structure, regardless of domain
(education, knowledge management, photography, teaching, course design):

| Section | Purpose | % of Document |
|---------|---------|---------------|
| **Title + Audience** | Who this is for and what it does | 2-3% |
| **Context** | Background, prerequisites, input/output contracts | 15-20% |
| **Task** | Primary objective, success criteria | 8-12% |
| **Approach** | Phased execution with pseudocode | 40-50% |
| **Constraints** | Quality gates, iteration rules, hard limits | 8-12% |
| **Examples** | Complete input/output demonstration | 10-15% |
| **Output Template** | Exact format of the deliverable | 5-10% |

**Key insight**: The Approach section dominates (40-50%). Instructions are primarily
about HOW, with supporting sections providing the WHAT and WHY.

### 2. Input/Output Contracts — The Most Critical Pattern

Every production instruction defines explicit contracts at the top of its context section.
This is the single most important pattern for executable instructions.

**Input contract format**:
```
INPUT:  $topic (required) - "Example value here"
        $audience (required) - "Description of expected input"
        $options (optional) - default_value
```

**Output contract format**:
```
OUTPUT: $deliverable (object)
        $artifacts (array)
        $quality_report (object)
```

**What makes contracts effective**:
- Every variable has a type hint (string, array, object, enum)
- Required vs optional is explicit
- Defaults are provided for optional fields
- Example values appear inline (not in a separate section)
- Contracts use `$variable_name` convention for easy reference in phases

**Anti-pattern**: Instructions without input contracts produce inconsistent results.
The LLM guesses what format inputs should take and may hallucinate defaults.

### 3. Phase Structure — 3 to 5 Phases with Pseudocode

Production instructions use 3-5 numbered phases. Each phase is a Python-style function
with docstring, parameters, and return value.

**Observed phase counts**:
| Instruction Domain | Phases | Pattern |
|-------------------|--------|---------|
| Knowledge card building | 5 | Process → Format → Link → Validate → Store |
| Workbook creation | 5 | Plan → Theory → Exercises → Reflection → Answer Key |
| Photography prompts | 3 | Define scenes → Generate prompts → Validate coverage |
| Lesson delivery | 5 | Analyze context → WHEN → HOW → WHAT → Exercise |
| Curriculum design | 4 | Scope → Learning path → Modules → Duration |

**Universal phase pattern**: `Analyze → Generate → Validate`
- **Phase 1** always analyzes inputs and determines approach
- **Middle phases** generate the actual content
- **Final phase** validates quality and formats output

**Pseudocode format that works**:
```python
def phase_name($input_variable, $config):
    """
    One-line description of what this phase does.
    """
    # Step-by-step logic
    result = process($input_variable)

    # Decision point with clear conditions
    if condition_a:
        approach = "variant_a"
    else:
        approach = "variant_b"

    return {
        "output_field": result,
        "next_phase_input": derived_value
    }
```

**Critical**: Pseudocode is for guiding the LLM's reasoning, not for execution.
Use descriptive function names, clear conditions, and explicit return structures.
Avoid complex algorithms — the LLM fills in implementation details.

### 4. Template-Driven Output — Structure Over Prose

Every production instruction includes a complete output template with placeholder
variables. This is what makes outputs consistent across executions.

**Template format**:
```markdown
# {{TITLE}}

## Section 1
| Field | Value |
|-------|-------|
| **Key** | {{VARIABLE_1}} |
| **Key** | {{VARIABLE_2}} |

## Section 2
{{CONTENT_BLOCK}}

## Validation
- [ ] {{CHECKLIST_ITEM_1}}
- [ ] {{CHECKLIST_ITEM_2}}
```

**What makes templates effective**:
- `{{DOUBLE_BRACES}}` for variables the LLM fills in
- `[SQUARE_BRACKETS]` for open variables where the LLM exercises judgment
- Tables for structured data (never prose for tabular information)
- Checklists for validation (checkboxes, not paragraphs)
- Explicit section headers matching the phase outputs

**Anti-pattern**: Instructions that describe output in prose ("return a document with...")
produce wildly different formats on each run. Always include a literal template.

### 5. Quality Gates — Quantified, Not Aspirational

All production instructions include validation with numeric thresholds:

**Effective quality gate format (YAML)**:
```yaml
validation:
  structure:
    rule: "All required sections present"
    check: "Count section headers against expected list"

  content:
    rule: "Minimum content density per section"
    check: "No section is empty or placeholder-only"

  accuracy:
    rule: "Claims are verifiable"
    check: "At least 2 concrete numbers/benchmarks included"

  format:
    rule: "Output matches template exactly"
    tolerance: "Section order may vary, but all must be present"
```

**Observed thresholds across production instructions**:
| Gate | Typical Threshold | Range |
|------|------------------|-------|
| Overall quality score | >= 7.0 | 7.0-9.0 |
| Section completeness | 100% required sections | - |
| Example count | >= 1 | 1-3 |
| Open variables per section | >= 2 | 2-5 |
| Duration estimate accuracy | +/- 10% of target | 10-15% |

**Anti-pattern**: Quality gates that say "ensure high quality" without numbers.
If you can't measure it, you can't enforce it.

### 6. Layered Complexity — Adapt Depth to Audience

3 of 5 production instructions implement audience-level adaptation:

**Pattern: template variants by level**:
```python
templates = {
    "beginner": {
        "language": "Simple, step-by-step, no jargon",
        "depth": "Guided tutorials, fill-in-the-blank",
        "examples": "Screenshots, numbered steps"
    },
    "intermediate": {
        "language": "Technical with context",
        "depth": "Application, analysis, comparison",
        "examples": "Diagrams, workflows"
    },
    "advanced": {
        "language": "Technical, code-oriented",
        "depth": "Building, debugging, extending",
        "examples": "Code samples, architecture decisions"
    }
}
```

**Key insight**: The same instruction handles multiple audiences by parameterizing
depth and language, not by writing separate instructions.

**Content ratio pattern** (from teaching instruction):
| Section | Time Allocation |
|---------|----------------|
| Context / When to use | 20% |
| Practical steps / How | 50% |
| Technical depth / What | 30% |

### 7. Metacognition Section — What This Does and Does NOT Do

4 of 5 production instructions end with an explicit metacognition block:

```markdown
## What This Instruction Does Well
- [Strength 1]
- [Strength 2]

## What This Instruction Does NOT Do
- Does NOT [adjacent task] (use [other_instruction] instead)
- Does NOT [out-of-scope action] (delegate to [other_agent])

## Chaining
[upstream_instruction] -> THIS -> [downstream_instruction]
                                -> [alternative_downstream]
```

**Why this matters**: It prevents scope creep during execution and provides routing
information for orchestrators that chain multiple instructions together.

### 8. Practical Size Observations

| Metric | Observed Range | Sweet Spot |
|--------|---------------|------------|
| Total lines | 480-1000 | 500-700 |
| Total tokens | 3,200-10,400 | 4,000-6,000 |
| Phases count | 3-5 | 4-5 |
| Input variables | 3-6 | 4-5 |
| Output variables | 2-5 | 3-4 |
| Examples (complete) | 1-3 | 1-2 |
| Max body bytes (schema limit) | - | 4,096 |

**Why 500-700 lines works best**:
- Under 500: phases are too thin, missing edge cases
- 500-700: each phase has enough pseudocode + templates for consistent execution
- Over 700: usually means heavy example sections (useful for complex outputs like
  20-scene photography prompts, but most instructions don't need this)

### 9. Anti-Patterns from Real Evidence

| Anti-Pattern | Why It Fails | Better Approach |
|--------------|-------------|-----------------|
| No input contract | LLM guesses input format, inconsistent results | Define every variable with type + required/optional |
| Compound steps | "Analyze input, generate output, and validate" is three actions | One action per phase step |
| Prose output description | "Return a comprehensive document" produces different formats each time | Include literal template with {{variables}} |
| Missing validation | No way to verify if instruction succeeded | Add checklist with numeric thresholds |
| No examples | LLM has no calibration for expected quality | Include at least 1 complete input/output example |
| Vague prerequisites | "Environment ready" is unverifiable | "Python 3.10+ installed, API key in env" is verifiable |
| Missing chaining info | Orchestrator doesn't know what comes next | Add upstream/downstream instruction references |
| Mixing identity with task | Instruction defines WHO the agent is alongside WHAT to do | Identity = system prompt, Task = instruction |

## Industry Implementations

| Source | What it defines | Alignment |
|--------|----------------|-----------|
| SRE Runbooks (Google) | Step-by-step incident response | Direct: numbered steps + validation |
| Ansible Playbooks | Declarative task sequences | Informs: idempotent + atomic fields |
| GitHub Actions workflows | Sequential job steps | Informs: prerequisites + dependencies |
| IEC 62443 procedures | Industrial control system SOPs | Informs: rollback + safety |
| Kubernetes operators | Reconciliation loops | Informs: idempotent re-execution |

## Key Principles (Industry + Evidence)

- **One action per step**: compound steps cause ambiguous failures
- **Verifiable prerequisites**: "Python 3.10+ installed" not "environment ready"
- **Idempotent when possible**: re-running should produce same result
- **Explicit rollback**: if atomic: false, every step needs an undo
- **Validation at end**: checklist of verifiable outcomes
- **Dependencies upfront**: tools, files, services, permissions listed before steps
- **No persona**: instructions say WHAT to do, not WHO you are

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT instruction |
|------|------------|--------------------------|
| action_prompt | Conversational task prompt with I/O | Has input/output spec, no prerequisites |
| system_prompt | Agent identity and rules | Defines WHO, not HOW |
| workflow | Multi-agent orchestration | Coordinates agents, not single-agent steps |
| skill | Reusable capability with trigger | Has lifecycle phases, not just steps |
| handoff | Dispatch instruction to another agent | Coordination artifact, not execution recipe |

## References
- Google SRE Book: Chapter 14 — Managing Incidents
- Ansible docs: Playbook best practices
- IEC 62443: Industrial automation security procedures
- Distilled from 5 production instructions: workbook creation, knowledge card building, brand photography prompts, lesson delivery framework, curriculum design
