---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for instruction production
sources: runbook engineering, SRE playbooks, IEC 62443, distilled from 5 production instruction prompts
---

# Domain Knowledge: instruction

## Foundational Concept
Instructions are operational recipes transforming a defined start state into an end state. From SRE runbooks and SOPs. Each step: atomic (one action), verifiable, reversible.

## 1. The 7-Section Structure

| Section | Purpose | % of Doc |
|---------|---------|----------|
| Title + Audience | Who + what | 2-3% |
| Context | Background, I/O contracts | 15-20% |
| Task | Objective, success criteria | 8-12% |
| Approach | Phased execution + pseudocode | 40-50% |
| Constraints | Quality gates, limits | 8-12% |
| Examples | Complete I/O demo | 10-15% |
| Output Template | Exact deliverable format | 5-10% |

Approach dominates (40-50%). Instructions are primarily about HOW.

## 2. Input/Output Contracts

```
INPUT:  $topic (required) - "Example value"
        $audience (required) - "Description"
        $options (optional) - default_value
OUTPUT: $deliverable (object)
        $artifacts (array)
```
- Every variable: type hint + required/optional + defaults
- Use `$variable_name` convention for phase references
- Without contracts, LLM guesses formats inconsistently

## 3. Phase Structure (3-5 Phases)

Universal pattern: `Analyze -> Generate -> Validate`
- Phase 1: analyze inputs, determine approach
- Middle: generate content
- Final: validate quality, format output

```python
def phase_name($input, $config):
    """One-line description."""
    result = process($input)
    if condition: approach = "variant_a"
    else: approach = "variant_b"
    return {"output": result}
```
Pseudocode guides LLM reasoning, not execution. Descriptive names, clear conditions.

## 4. Quality Gates

| Gate | Typical Threshold |
|------|------------------|
| Overall score | >= 7.0 |
| Section completeness | 100% required |
| Example count | >= 1 |
| Open variables/section | >= 2 |

Quantified, not aspirational. "Ensure high quality" is unenforceable.

## 5. Size Observations

| Metric | Sweet Spot | Range |
|--------|-----------|-------|
| Total lines | 200-350 | 150-500 |
| Body tokens | 3,000-3,500 | 2,500-4,500 |
| Phases | 4-5 | 3-5 |
| Input vars | 4-5 | 3-6 |
| Max body bytes | 4,096 | - |

Dense and focused. Padding with verbose explanations wastes attention weight.

## 6. Metacognition

- End with explicit "Does / Does NOT" block
- Include chaining: `[upstream] -> THIS -> [downstream]`
- Prevents scope creep, provides routing info

## 7. Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| No input contract | Define every var with type + required/optional |
| Compound steps | One action per step |
| Prose output description | Literal template with {{variables}} |
| Missing validation | Checklist with numeric thresholds |
| No examples | At least 1 complete I/O example |
| Mixing identity with task | Identity=system_prompt, Task=instruction |

## Key Principles
- One action per step; compound steps cause ambiguous failures
- Verifiable prerequisites ("Python 3.10+" not "environment ready")
- Idempotent when possible; explicit rollback when not
- No persona: instructions say WHAT, not WHO

## Boundary

| Type | Why NOT instruction |
|------|---------------------|
| action_prompt | Has I/O spec, no prerequisites |
| system_prompt | Defines WHO, not HOW |
| workflow | Coordinates agents, not single-agent steps |
| skill | Has lifecycle phases, not just steps |
| handoff | Coordination artifact, not execution recipe |
