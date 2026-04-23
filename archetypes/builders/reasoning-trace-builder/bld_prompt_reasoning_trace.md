---
id: p03_ins_reasoning_trace_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: instruction-builder
title: Reasoning Trace Builder Instructions
target: reasoning-trace-builder agent
phases_count: 3
prerequisites:
  - Agent name or agent_group identifier is known
  - Intent or decision question is defined
  - Evidence sources are available (metrics, prior results, file references)
  - Timestamp or timing data is available
validation_method: checklist
domain: reasoning_trace
quality: 9.0
tags: [instruction, reasoning_trace, cognition, P03]
idempotent: true
atomic: true
rollback: "Discard trace and regenerate — traces are append-only records"
dependencies: []
logging: true
tldr: Produce a structured YAML reasoning trace capturing step-evidence-confidence chains, rejected alternatives, and conclusion — under 8192 bytes, human-auditable, no execution instructions included.
density_score: 0.86
llm_function: REASON
related:
  - bld_knowledge_card_reasoning_trace
  - bld_collaboration_reasoning_trace
  - p03_sp_reasoning_trace_builder
  - bld_schema_reasoning_trace
  - reasoning-trace-builder
  - p01_kc_reasoning_trace
  - p11_qg_reasoning_trace
  - bld_config_reasoning_trace
  - bld_architecture_reasoning_trace
  - bld_output_template_reasoning_trace
---
## Context
The reasoning-trace-builder produces `reasoning_trace` artifacts — structured YAML records
capturing the complete chain-of-thought behind an agent's decision. A reasoning trace answers
exactly: what was considered, what evidence existed, how confident the agent was at each step,
what alternatives were rejected and why, and what conclusion was reached. Traces are consumed
by human auditors and feedback loops; they are not instructions, system prompts, or workflows.
**Input contract**:
- `{{agent}}`: name of the agent whose reasoning is being traced (e.g. `research-agent`, `build-sat`)
- `{{intent}}`: the decision question or goal being reasoned about (e.g. `select embedding model`)
- `{{evidence_sources}}`: available data, metrics, prior results, or file references
- `{{timestamp}}`: ISO 8601 datetime of the reasoning session
- `{{alternatives}}`: optional list of paths considered but not chosen
**Output contract**: A single `reasoning_trace` YAML file named `p03_rt_{{agent}}_{{timestamp}}.yaml`,
under 8192 bytes, with required fields and step-evidence-confidence chains. No execution
instructions, no tool calls, no workflow logic.
**Boundaries**:
- A reasoning trace is a decision record — one decision chain, one trace, one file.
- Execution instructions belong in an instruction artifact.
- Agent identity and persona belong in a system_prompt artifact.
- Multi-step workflows and DAGs are not reasoning traces.
- Evidence must be concrete and referenceable, not vague assertions.
## Phases
### Phase 1: Classify
**Primary action**: Confirm this is a decision record and determine the minimum required
trace structure before writing any YAML.
```
INPUT: agent, intent, evidence_sources, timestamp, alternatives
1. Confirm this is a decision record, not an instruction or workflow:
   Is it recording WHY a decision was made?                    -> reasoning_trace
   Is it telling an agent WHAT to do next?                     -> NOT a reasoning_trace
   Is it defining HOW steps connect?                           -> NOT a reasoning_trace
2. Validate agent identifier:
   Must be non-empty string, lowercase slug preferred
   Must match a known agent or agent_group in the system
3. Validate intent:
   Must be a clear decision question or goal statement
   Must be specific enough to evaluate alternatives against
   Examples: "select embedding model for P01 retriever", "choose chunking strategy"
4. Inventory evidence sources:
   List all available data: metrics, benchmarks, prior results, file paths
   Flag any step that lacks evidence — mark as "assertion" not "reasoned"
   Require minimum 1 evidence source per step
5. Identify alternatives:
   List all paths considered (chosen + rejected)
   For each rejected alternative, require a rejection reason
   If no alternatives exist, flag the trace as "single-path" (lower audit value)
OUTPUT: validated_agent, validated_intent, evidence_inventory, alternatives_list
```
Verification: `validated_agent` is non-empty slug. `validated_intent` is specific.
Each step has at least one evidence source. Alternatives list is populated.
### Phase 2: Compose
**Primary action**: Assemble the structured YAML trace with step-evidence-confidence
chains, rejected alternatives, and conclusion.
```
INPUT: validated_agent, validated_intent, evidence_inventory, alternatives_list, timestamp
1. Set filename: p03_rt_{{agent}}_{{timestamp}}.yaml
2. Assemble frontmatter:
   id: p03_rt_{{agent}}_{{timestamp}}
   kind: reasoning_trace
   pillar: P03
   agent: {{agent}}
   intent: {{intent}}
   timestamp: {{timestamp}}
   quality: null
3. Compose step chain (ordered list):
   For each reasoning step:
     step: sequential integer (1, 2, 3...)
     thought: what the agent considered at this point
     evidence: concrete data supporting or refuting the thought
     confidence: 0.0-1.0 score for this specific step
   Rules:
     - Steps must be in chronological/logical order
     - Each step must have non-empty thought AND evidence
     - Confidence must be calibrated: 0.0-0.3 (low), 0.3-0.7 (medium), 0.7-1.0 (high)
     - A step with no evidence gets confidence capped at 0.3
4. Compose alternatives_rejected:
   For each rejected path:
     alternative: description of the rejected option
     reason: why it was rejected (evidence-based)
   At least 1 rejected alternative required for a complete trace
5. Compose conclusion:
   One-paragraph summary of the final decision
   Must reference the strongest evidence from the step chain
6. Compute overall confidence:
   Geometric mean of all step confidences (penalizes weak links)
   Round to 2 decimal places
7. Add duration_ms if timing data available
8. Size check:
   Estimate YAML byte count
   If > 8192 bytes: compress thought/evidence text (keep meaning, reduce words)
   until size <= 8192 bytes
OUTPUT: reasoning_trace YAML content (assembled, not yet validated)
```
Verification: all required fields present. Step chain is ordered. Each step has
thought + evidence + confidence. At least 1 rejected alternative. Size <= 8192 bytes.
### Phase 3: Validate
**Primary action**: Run all quality gates against the assembled YAML and output the
final file only if all HARD gates pass.
```
INPUT: reasoning_trace YAML content
1. HARD quality gates (all must pass):
   HARD_1: id matches pattern ^p03_rt_[a-z][a-z0-9_]+_\d{8}T\d{6}$
   HARD_2: kind == "reasoning_trace"
   HARD_3: agent is non-empty string
   HARD_4: intent is non-empty string
   HARD_5: steps is non-empty list with >= 2 entries
   HARD_6: each step has thought, evidence, confidence fields
   HARD_7: confidence values are in range 0.0-1.0
   HARD_8: conclusion is non-empty string
   HARD_9: alternatives_rejected is non-empty list with >= 1 entry
   HARD_10: quality == null
   HARD_11: timestamp is valid ISO 8601
   HARD_12: total YAML size <= 8192 bytes
   HARD_13: YAML parses without syntax errors
2. Scope check:
   Verify trace contains NO execution instructions
   Verify trace contains NO workflow step definitions
   Verify trace contains NO tool call definitions
3. If all HARD gates pass: emit file
   If any HARD gate fails: return to Phase 2 with failure reasons
OUTPUT: validated reasoning_trace YAML file
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_reasoning_trace]] | upstream | 0.56 |
| [[bld_collaboration_reasoning_trace]] | upstream | 0.52 |
| [[p03_sp_reasoning_trace_builder]] | related | 0.51 |
| [[bld_schema_reasoning_trace]] | downstream | 0.51 |
| [[reasoning-trace-builder]] | related | 0.49 |
| [[p01_kc_reasoning_trace]] | related | 0.47 |
| [[p11_qg_reasoning_trace]] | downstream | 0.47 |
| [[bld_config_reasoning_trace]] | downstream | 0.45 |
| [[bld_architecture_reasoning_trace]] | downstream | 0.45 |
| [[bld_output_template_reasoning_trace]] | downstream | 0.45 |
