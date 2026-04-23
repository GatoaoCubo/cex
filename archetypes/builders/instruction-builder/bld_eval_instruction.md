---
kind: quality_gate
id: p11_qg_instruction
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of instruction artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Instruction"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, instruction, steps, recipe, procedure, idempotency]
tldr: "Gates ensuring instruction artifacts decompose tasks into atomic verifiable steps with prerequisites, completion criteria, and rollback procedures."
domain: "instruction — step-by-step operational recipes for agent task execution"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.90
related:
  - p11_qg_handoff
  - p11_qg_input_schema
  - p11_qg_workflow
  - p11_qg_chain
  - bld_instruction_chain
  - p11_qg_agent_computer_interface
  - p10_lr_instruction_builder
  - p03_sp_instruction_builder
  - p01_kc_instruction
  - bld_examples_instruction
---

## Quality Gate

# Gate: Instruction
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: instruction` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem | `id: deploy_service` in file `restart_service.md` |
| H04 | Kind equals literal `instruction` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All required fields present | Missing: steps, prerequisites, or completion_criteria |
| H07 | Steps are numbered and count >= 2 | Single undivided step or unnumbered list |
| H08 | `idempotent` field is a boolean | Missing field or non-boolean value |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Step atomicity | 1.0 | Every step performs exactly one action and is independently verifiable | Most steps atomic; some compound | Steps are multi-action paragraphs |
| S02 | Prerequisites completeness | 1.0 | All tools, permissions, files, and env vars listed | Some prerequisites listed | No prerequisites section |
| S03 | Completion criteria | 1.0 | Each step has explicit success signal (exit code, file exists, output pattern) | Overall completion defined but not per-step | No success criteria |
| S04 | Rollback procedures | 1.0 | Undo steps defined for each destructive action | Partial rollback notes present | No rollback |
| S05 | Idempotency declaration | 0.5 | `idempotent: true/false` with explanation of why | Field present, no rationale | Field absent |
| S06 | Dependency ordering | 1.0 | Steps reference their predecessors explicitly when order matters | Steps ordered but dependencies implicit | Unordered; any sequence implied |
| S07 | Atomicity classification | 0.5 | `atomic` field classifies instruction as atomic or composable | Classification present but unexplained | Field missing |
| S08 | Error handling per step | 1.0 | Each step lists what to do on failure | Some steps have error notes | No error handling |
| S09 | Tool list | 0.5 | `tools_required` lists every CLI, SDK, or API the steps invoke | Partial tool list | No tool list |
| S10 | Distinction from action_prompt | 0.5 | No I/O prompt framing — pure procedural steps | Minimal prompt framing leakage | Reads as a prompt, not a recipe |
| S11 | Example run | 0.5 | At least one example showing input values substituted into steps | Example mentioned but sparse | No example |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to pool as golden operational runbook |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Novel procedure being executed for the first time; rollback path not yet known |
| Approver | Task owner + one peer reviewer |
| Audit trail | `bypass_reason` required; note which gates are bypassed and why |

## Examples

# Examples: instruction-builder
## Golden Example
INPUT: "Create instruction for rebuilding the Brain FAISS index"
OUTPUT:
```yaml
id: p03_ins_rebuild_brain_faiss
kind: instruction
pillar: P03
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
title: "Rebuild Brain FAISS Index"
target: "knowledge-engine agent_group or human operator"
steps_count: 6
prerequisites:
  - "Ollama running locally with nomic-embed-text model"
  - "Python 3.10+ with faiss-cpu installed"
  - "At least 2GB free disk space"
validation_method: checklist
idempotent: true
atomic: false
rollback: "Delete generated .faiss files and revert to previous index backup"
dependencies:
  - "ollama"
  - "faiss-cpu"
  - "build_indexes_ollama.py"
logging: true
domain: "knowledge"
quality: null
tags: [instruction, brain, faiss, index, rebuild]
tldr: "6-step procedure to rebuild Brain FAISS+BM25 index from pool artifacts using Ollama embeddings"
density_score: 0.90
```
## Prerequisites
- Ollama running: `ollama list` shows `nomic-embed-text`
- Python deps: `python -c "import faiss; print(faiss.__version__)"`
- Disk space: `df -h .` shows >= 2GB free
## Steps
1. Backup current index — `cp records/core/brain/*.faiss records/core/brain/backup/`
2. Verify Ollama health — `ollama list | grep nomic-embed-text`
3. Run index builder — `cd records/core/brain/mcp-organization-brain && python build_indexes_ollama.py --scope all`
4. Wait for completion — process takes ~20 minutes, outputs progress to stdout
5. Verify index size — `ls -la records/core/brain/*.faiss` (expect ~140MB)
6. Test query — `python -c "from brain_search import search; print(search('test query')[:1])"`
## Validation
- [ ] New .faiss files exist and are > 100MB
- [ ] brain_query returns results for known terms
- [ ] No error output in build log
- [ ] Index timestamp matches current date
## Rollback
Restore backup: `cp records/core/brain/backup/*.faiss records/core/brain/`
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p03_ins_ pattern (H02 pass)
- kind: instruction (H04 pass)
- 20 required fields present (H06 pass)
- body has Steps with 6 numbered items (H07 pass)
- rollback defined and atomic: false (H08 pass)
- steps_count: 6 matches actual 6 steps (S03 pass)
- Each step has one action (S04 pass)
- Prerequisites are verifiable commands (S05 pass)
- No persona/identity content (S09 pass)
## Anti-Example
INPUT: "Create instruction for deploying the API"
BAD OUTPUT:
```yaml
id: deploy-api
kind: procedure
pillar: prompt
title: Deploy
steps_count: 1
quality: 9.0
tags: [deploy]
```
You are a deployment expert. Follow these steps:
1. Deploy the API to production by running the deployment script and checking that everything works and then verifying the logs and restarting if needed.
FAILURES:
1. id: no `p03_ins_` prefix, uses hyphens -> H02 FAIL
2. kind: "procedure" not "instruction" -> H04 FAIL
3. pillar: "prompt" not "P03" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. Missing fields: version, created, updated, author, target, prerequisites, validation_method, idempotent, atomic, domain -> H06 FAIL
6. tags: only 1 item -> S02 FAIL
7. Step 1 has 4 compound actions -> S04 FAIL
8. Contains persona ("You are a deployment expert") -> S09 FAIL
9. No ## Prerequisites, ## Validation, ## Rollback sections -> S06, S07, S08 FAIL
10. steps_count: 1 but step contains multiple actions -> S03 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
