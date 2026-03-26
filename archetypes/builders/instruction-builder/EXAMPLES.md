---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of instruction artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: instruction-builder

## Golden Example

INPUT: "Create instruction for rebuilding the Brain FAISS index"

OUTPUT:
```yaml
---
id: p03_ins_rebuild_brain_faiss
kind: instruction
pillar: P03
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
title: "Rebuild Brain FAISS Index"
target: "PYTHA satellite or human operator"
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
---
```

## Prerequisites
- Ollama running: `ollama list` shows `nomic-embed-text`
- Python deps: `python -c "import faiss; print(faiss.__version__)"`
- Disk space: `df -h .` shows >= 2GB free

## Steps
1. Backup current index — `cp records/core/brain/*.faiss records/core/brain/backup/`
2. Verify Ollama health — `ollama list | grep nomic-embed-text`
3. Run index builder — `cd records/core/brain/mcp-codexa-brain && python build_indexes_ollama.py --scope all`
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
---
id: deploy-api
kind: procedure
pillar: prompt
title: Deploy
steps_count: 1
quality: 9.0
tags: [deploy]
---
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
