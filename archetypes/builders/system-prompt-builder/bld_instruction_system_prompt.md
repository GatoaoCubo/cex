---
id: p03_ins_system_prompt
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: System Prompt Builder Instructions
target: "system-prompt-builder agent"
phases_count: 5
prerequisites:
  - "Agent name and domain are defined"
  - "Primary use case is documented in 1-2 sentences minimum"
  - "Target audience or calling context is known"
  - "At least 3 ALWAYS rules and 3 NEVER rules can be derived from the domain"
validation_method: checklist
domain: system_prompt
quality: null
tags: [instruction, system-prompt, identity, persona, P03]
idempotent: true
atomic: false
rollback: "Delete generated system_prompt YAML file and revert to previous version"
dependencies: []
logging: true
tldr: "Build a dense system_prompt YAML that transforms a generic LLM into a focused specialist with clear identity, ALWAYS/NEVER rules, and output format."
density_score: 0.94
---

## Context

The system-prompt-builder produces a `system_prompt` artifact -- a structured YAML containing the full system message injected at the top of every LLM conversation for a specific agent. This prompt defines who the agent is, what it knows, what it must always do, what it must never do, and how it formats responses.

**Critical distinction**: a system_prompt governs agent identity and standing rules. It is NOT a task prompt (action_prompt), a step-by-step recipe (instruction), or a prompt template with variables (prompt_template). Confusing these types produces broken agents.

**Input contract**:
- `agent_name`: string -- kebab-case agent identifier (e.g. `price-analyst`, `code-reviewer`)
- `domain`: string -- the specialist domain (e.g. `pricing strategy`, `Python code review`)
- `use_case`: string -- primary purpose in 1-2 sentences
- `audience`: string -- who calls this agent (human, orchestrator, pipeline)
- `tone`: enum -- `professional` | `technical` | `conversational` | `terse`
- `always_rules`: list of strings -- minimum 3 mandatory behaviors
- `never_rules`: list of strings -- minimum 3 prohibited behaviors
- `output_format`: string -- description of expected response structure
- `knowledge_boundary`: string or null -- explicit scope limits

**Output contract**: a single `system_prompt` YAML with 19 required fields, stored at `records/system_prompts/{agent_name}.yaml`.

**Variables**:
- `{{agent_name}}` -- kebab-case agent name
- `{{domain}}` -- specialist domain label
- `{{persona_statement}}` -- 1-sentence identity declaration
- `{{always_rule_N}}` -- Nth ALWAYS rule with brief justification
- `{{never_rule_N}}` -- Nth NEVER rule with brief justification

---

## Phases

### Phase 1: Analyze Domain and Derive Persona

**Action**: Synthesize inputs into a tight persona statement and knowledge boundary.

```
persona_statement = "You are {{agent_name}}, a specialist in {{domain}}."

IF use_case mentions multiple sub-domains:
    primary_domain = most specific sub-domain
ELSE:
    primary_domain = domain

IF knowledge_boundary provided:
    use as-is
ELSE:
    derive: "You cover {{primary_domain}}. You do NOT cover {{adjacent_domains}}."
```

The persona must be specific enough to exclude adjacent domains. A code reviewer is not a code writer. A price analyst is not a sales strategist.

Verifiable exit: persona_statement is one sentence; knowledge_boundary explicitly names at least one out-of-scope area.

### Phase 2: Enumerate ALWAYS and NEVER Rules

**Action**: Expand provided rules into structured constraint objects with justifications.

```
FOR each rule in always_rules:
    always_block.append({ rule: rule_text, why: one_sentence_rationale })

FOR each rule in never_rules:
    never_block.append({ rule: rule_text, why: one_sentence_rationale })

ASSERT len(always_block) >= 3
ASSERT len(never_block) >= 3
```

Rule quality criteria:
- Rules must be actionable, not aspirational ("Always cite sources" not "Be helpful")
- NEVER rules must address real failure modes for this domain
- No duplicate intent across rules -- merge overlapping rules
- Each rule must have a distinct rationale

Verifiable exit: at least 3 ALWAYS and 3 NEVER rules each with rationale; no duplicate intents.

### Phase 3: Define Output Format and Tone

**Action**: Translate the output_format description into a precise structural spec.

```
tone_map = {
    "terse":          "Respond concisely. No filler phrases.",
    "technical":      "Use precise technical terminology. Define terms on first use.",
    "conversational": "Use plain language. Avoid jargon unless necessary.",
    "professional":   "Maintain professional register. Structure responses clearly."
}
response_preamble = tone_map[tone]

format_spec = {
    structure: output_format description,
    max_length: derive from domain complexity,
    preamble_rule: response_preamble,
    examples_required: true if domain is ambiguous else false
}
```

Verifiable exit: format_spec has structure, max_length, and preamble_rule populated.

### Phase 4: Compose system_prompt YAML

**Action**: Assemble all resolved values into the 19-field YAML structure.

Required fields in order:
1. `id` -- `system_prompt_{{agent_name}}`
2. `kind` -- `system_prompt`
3. `pillar` -- `P03`
4. `version` -- `1.0.0`
5. `agent` -- `{{agent_name}}`
6. `domain` -- `{{domain}}`
7. `persona` -- `{{persona_statement}}`
8. `tone` -- `{{tone}}`
9. `knowledge_boundary` -- scoped string
10. `always` -- list of rule objects (rule + why), min 3
11. `never` -- list of rule objects (rule + why), min 3
12. `output_format` -- `{{format_spec.structure}}`
13. `max_response_length` -- integer (tokens or words)
14. `examples_required` -- boolean
15. `audience` -- `{{audience}}`
16. `safety_level` -- `standard` | `strict` | `minimal`
17. `version_notes` -- string
18. `created` -- ISO date
19. `updated` -- ISO date

Verifiable exit: YAML parses cleanly; all 19 fields present; always and never each have >= 3 items.

### Phase 5: Validate Against Quality Gates

**Action**: Run 8 HARD gates before emitting; log 12 SOFT gates as warnings.

```
HARD gates (all must pass):
  H1: persona is a single declarative sentence
  H2: knowledge_boundary names at least one out-of-scope area
  H3: always block has >= 3 rules, each with a rationale
  H4: never block has >= 3 rules, each with a rationale
  H5: no ALWAYS rule contradicts a NEVER rule
  H6: output_format is specific (not generic filler)
  H7: all 19 YAML fields are present
  H8: tone matches one of the four valid enum values

SOFT gates (log warnings, do not block):
  S1-S4: rules are actionable, not aspirational (4 rule samples)
  S5-S8: no duplicate intent across rules (4 checks)
  S9: knowledge_boundary is 1-2 sentences
  S10: max_response_length is reasonable for domain
  S11: version_notes is informative
  S12: examples_required is true for ambiguous domains
```

Verifiable exit: 8/8 HARD gates pass.

---

## Output Contract

```yaml
id: system_prompt_{{agent_name}}
kind: system_prompt
pillar: P03
version: 1.0.0
agent: {{agent_name}}
domain: "{{domain}}"
persona: "{{persona_statement}}"
tone: {{tone}}
knowledge_boundary: "{{knowledge_boundary}}"
always:
  - rule: "{{always_rule_1}}"
    why: "{{always_rule_1_rationale}}"
  - rule: "{{always_rule_2}}"
    why: "{{always_rule_2_rationale}}"
  - rule: "{{always_rule_3}}"
    why: "{{always_rule_3_rationale}}"
never:
  - rule: "{{never_rule_1}}"
    why: "{{never_rule_1_rationale}}"
  - rule: "{{never_rule_2}}"
    why: "{{never_rule_2_rationale}}"
  - rule: "{{never_rule_3}}"
    why: "{{never_rule_3_rationale}}"
output_format: "{{format_spec_structure}}"
max_response_length: {{max_response_length}}
examples_required: {{examples_required}}
audience: "{{audience}}"
safety_level: {{safety_level}}
version_notes: "{{version_notes}}"
created: "{{created}}"
updated: "{{updated}}"
```

---

## Validation

- [ ] H1: persona is a single declarative sentence
- [ ] H2: knowledge_boundary names at least one out-of-scope area
- [ ] H3: always block has >= 3 rules with rationales
- [ ] H4: never block has >= 3 rules with rationales
- [ ] H5: no ALWAYS rule contradicts a NEVER rule
- [ ] H6: output_format is specific and structural
- [ ] H7: all 19 YAML fields are present
- [ ] H8: tone is one of professional, technical, conversational, terse

---

## Metacognition

**Does**:
- Produce a single reusable system_prompt YAML per agent
- Enforce rule quality (actionable, distinct, with rationale)
- Explicitly scope the knowledge boundary to prevent domain bleed
- Validate 8 HARD gates before emitting

**Does NOT**:
- Write task-specific prompts (action_prompt handles per-task instructions)
- Produce step-by-step execution recipes (instruction handles that)
- Generate prompt templates with runtime variables (prompt_template handles that)
- Make the agent capable of things its underlying model cannot do

**Chaining**: system-prompt-builder output is the identity layer consumed by all other P03 builders. Build system_prompt first, then action_prompt, then prompt_template for a complete agent definition.
