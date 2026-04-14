---
id: p11_qg_chain
kind: quality_gate
pillar: P11
title: "Gate: chain"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "prompt pipeline design — sequential LLM call chains with typed data flow between steps"
quality: 9.0
tags: [quality-gate, chain, P03, prompt-pipeline, sequential, data-flow]
tldr: "Pass/fail gate for chain artifacts: step atomicity, typed data flow, error handling strategy, and pipeline completeness."
density_score: 0.91
llm_function: GOVERN
---
# Gate: chain
## Definition
| Field | Value |
|---|---|
| metric | chain artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: chain` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | `id: my_chain` but file is `other_chain.md` |
| H04 | Kind equals literal `chain` | `kind: workflow` or `kind: pipeline` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `steps`, `input_schema`, or `output_schema` |
| H07 | Chain has at least two steps | Single-step chain is a prompt, not a chain |
| H08 | Each step has an explicit output type | Step output typed as `any` or unspecified |
| H09 | Error handling strategy declared | `error_handling` field absent; must be one of: fail_fast, skip, retry, fallback |
| H10 | No step references a runtime executor | Step contains orchestration logic (loops, parallelism) — chain is prompts only |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Step atomicity | 1.0 | Each step is one LLM call; no compound logic bundled in a single step |
| Data flow explicitness | 1.0 | Each step declares which prior step's output it consumes |
| Type coverage | 1.0 | All input/output types are concrete (string, number, list[string], not `any`) |
| Error handling granularity | 1.0 | Error strategy defined per-step or with justified global default |
| Context passing efficiency | 0.5 | Passes only required fields to each step, not entire prior context |
| Step naming clarity | 0.5 | Step names describe the LLM task (extract_entities not step_2) |
| Branching documentation | 1.0 | Conditional branches have explicit conditions and merge points documented |
| Prompt boundaries | 1.0 | No step bleeds workflow logic (loops, state management) into prompt text |
| Input schema completeness | 0.5 | Input schema covers all fields consumed by first step |
| Output schema alignment | 0.5 | Output schema matches the final step's declared output type |
| Domain specificity | 1.0 | Step prompts and transforms specific to the declared domain problem |
| Testability | 1.0 | Each step can be unit-tested with mock input/output independently |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Proof-of-concept chain during active research spike, not intended for production use |
| approver | Lead author acknowledgment in artifact comment block |
| audit_trail | Bypass reason and spike ticket ID recorded in frontmatter comment |
| expiry | 48h — spike chains must either reach >= 7.0 or be deleted |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |
