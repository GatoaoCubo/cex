---
kind: quality_gate
id: p11_qg_chain
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of chain artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: chain"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, chain, P03, prompt-pipeline, sequential, data-flow]
tldr: "Pass/fail gate for chain artifacts: step atomicity, typed data flow, error handling strategy, and pipeline completeness."
domain: "prompt pipeline design — sequential LLM call chains with typed data flow between steps"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.91
related:
  - bld_architecture_chain
  - p10_lr_chain_builder
  - bld_examples_chain
  - p01_kc_chain
  - bld_instruction_chain
  - p03_sp_chain_builder
  - p03_ch_{{PIPELINE_SLUG}}
  - chain-builder
  - bld_knowledge_card_chain
  - p12_wf_builder_8f_pipeline
---

## Quality Gate

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

## Examples

# Examples: chain-builder
## Golden Example
INPUT: "Create a prompt chain for research-to-knowledge-card pipeline"
OUTPUT:
```yaml
id: p03_ch_research_to_kc
kind: chain
pillar: P03
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
title: "Research to Knowledge Card Pipeline"
steps_count: 3
flow: sequential
input_format: "topic name + domain string"
output_format: "knowledge_card markdown artifact"
context_passing: filtered
error_strategy: fail_fast
domain: "knowledge"
quality: null
tags: [chain, knowledge, research, distillation]
tldr: "3-step chain: gather sources, extract facts, compose KC with density >= 0.80"
density_score: 0.88
```
## Purpose
Transforms a raw topic into a production-ready knowledge_card by chaining three
prompt steps: source gathering, fact extraction, and KC composition. Each step
narrows scope — from broad research to atomic distilled facts.
## Steps
### Step 1: Gather Sources
- **Input**: topic name (string), domain (string)
- **Prompt**: Search for authoritative sources on `{{topic}}` in `{{domain}}`. Return 3-5 URLs with one-line summaries.
- **Output**: list of {url, summary} objects (JSON)
### Step 2: Extract Facts
- **Input**: list of {url, summary} from Step 1
- **Prompt**: For each source, extract 5-10 atomic facts as bullets <= 80 chars. Remove opinions and filler.
- **Output**: deduplicated fact list (markdown bullets)
### Step 3: Compose KC
- **Input**: fact list from Step 2, original topic/domain
- **Prompt**: Compose a knowledge_card following P01 schema. Fill all required fields. density >= 0.80.
- **Output**: complete knowledge_card artifact (YAML frontmatter + markdown body)
## Data Flow
```text
[topic, domain] --string--> Gather --JSON--> Extract --bullets--> Compose --KC.md-->
```
Context passing: filtered — each step receives only its direct input, not full history.
## Error Handling
- **Strategy**: fail_fast
- **On failure at step N**: halt chain, return partial output with error context
- **Retry policy**: none (source quality issues require human intervention)
## References
- P01_knowledge/_schema.yaml (KC field definitions)
- archetypes/builders/knowledge-card-builder/ (downstream consumer)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p03_ch_ pattern (H02 pass)
- kind: chain (H04 pass)
- 19 required fields present (H06 pass)
- body has Purpose + Steps + Data Flow + Error Handling (H07 pass)
- steps_count: 3 matches actual 3 steps (H08 pass)
- Each step has Input/Prompt/Output (S03 pass)
- Data flow diagram present and matches steps (S04 pass)
- No runtime orchestration in body (S08 pass)
- No filler phrases (S10 pass)
## Anti-Example
INPUT: "Create a chain for content processing"
BAD OUTPUT:
```yaml
id: content_chain
kind: prompt
pillar: prompt
title: Content Chain
steps_count: 5
quality: 9.0
tags: [content]
```
This chain processes content through multiple steps. First, we gather the content.
Then we process it. Finally, we output the result.
## Steps
1. Get content
2. Process content
3. Output result
FAILURES:
1. id: no `p03_ch_` prefix -> H02 FAIL
2. kind: "prompt" not "chain" -> H04 FAIL
3. pillar: "prompt" not "P03" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. Missing fields: version, created, updated, author, flow, input_format, output_format, domain -> H06 FAIL
6. tags: only 1 item, missing "chain" -> S02 FAIL
7. Steps lack Input/Prompt/Output structure -> S03 FAIL
8. No Data Flow diagram -> S04 FAIL
9. No Error Handling section -> S06 FAIL
10. Body is filler prose ("This chain processes...") -> S10 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
