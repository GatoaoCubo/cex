---
kind: tools
id: bld_tools_conformity_assessment
pillar: P04
llm_function: CALL
purpose: Production, validation, and external reference tools for conformity assessment builds
quality: 9.2
title: "Conformity Assessment Builder -- Tools"
version: "1.0.0"
author: wave7_n05
tags: [conformity_assessment, builder, tools]
tldr: "CEX production tools + validation tools + external EU AI Act references for Annex-IV builds"
domain: "conformity_assessment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

# Conformity Assessment Builder -- Tools

## Production Tools

Tools called during 8F pipeline to produce and finalize the artifact.

| Tool | Command | 8F Stage | Purpose |
|------|---------|---------|---------|
| cex_compile.py | python _tools/cex_compile.py P11_govern/p11_ca_SYSTEM.md | F8 | Compile .md to .yaml registry entry |
| cex_score.py | python _tools/cex_score.py --apply P11_govern/p11_ca_SYSTEM.md | F7 | Apply peer-review quality score |
| cex_doctor.py | python _tools/cex_doctor.py --file P11_govern/p11_ca_SYSTEM.md | F7 | Health check on artifact structure |
| signal_writer | python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0)" | F8 | Send completion signal to N07 |
| cex_sanitize.py | python _tools/cex_sanitize.py --check --scope P11_govern/p11_ca_SYSTEM.md | F8 | Verify ASCII-only compliance |

## Validation Tools

Tools that enforce quality gates and schema compliance.

| Tool | Command | Gate | Purpose |
|------|---------|------|---------|
| cex_schema_hydrate.py | python _tools/cex_schema_hydrate.py --kind conformity_assessment | H03 | Validate kind field matches schema |
| cex_hooks.py | python _tools/cex_hooks.py pre-commit | H01 | Pre-commit frontmatter validation |
| cex_retriever.py | python _tools/cex_retriever.py --kind conformity_assessment --query "high-risk AI triage" | F5 | Find similar existing artifacts |
| cex_memory_select.py | python _tools/cex_memory_select.py --query "EU AI Act conformity assessment" | F3 | Load relevant memory for injection |
| cex_memory_update.py | python _tools/cex_memory_update.py --kind correction --source conformity_assessment | F8 | Record new learning after build |

## Regex Validation Tools (inline)

| Check | Pattern | Used At |
|-------|---------|---------|
| ID pattern | ^p11_ca_[a-z0-9_]+$ | H02 gate |
| Kind field | ^conformity_assessment$ | H03 gate |
| Date format | ^\d{4}-\d{2}-\d{2}$ | Schema validation |
| EU AI Act citation | EU AI Act (Art\. \d+|Annex [IVX]+) | D02 scoring |
| Unfilled placeholder | \{\{[A-Z_]+\}\} | F7 GOVERN (must be zero in final artifact) |
| Aug-2026 flag | \[AUG-2026-DEADLINE\] | D05 auditability |
| Non-ASCII | [^\x00-\x7F] | cex_sanitize.py check |

## External References

Official regulatory sources used as ground truth for content accuracy.

| Reference | URL / Citation | Used For |
|-----------|---------------|---------|
| EU AI Act full text | EUR-Lex 2024/1689 | All article and annex citations |
| Annex IV (technical doc requirements) | EU AI Act, Annex IV | Section structure |
| Annex III (high-risk categories) | EU AI Act, Annex III | Category determination |
| Article 9 (RMS) | EU AI Act, Art. 9 | RMS process requirements |
| Article 10 (data governance) | EU AI Act, Art. 10 | Data governance requirements |
| Article 14 (human oversight) | EU AI Act, Art. 14 | Human oversight measures |
| Article 43 (conformity procedure) | EU AI Act, Art. 43 | Procedure selection |
| Article 47 (declaration of conformity) | EU AI Act, Art. 47 | DoC reference |
| Article 72 (post-market monitoring) | EU AI Act, Art. 72 | PMM plan requirements |
| Article 73 (serious incident reporting) | EU AI Act, Art. 73 | SIR procedure |
| NIST AI RMF | https://airc.nist.gov/RMF | Supplementary risk framework |
| ISO/IEC 42001:2023 | ISO standard | AI management system |
| ISO 31000:2018 | ISO standard | Risk management principles |
| ISO/IEC 27001:2022 | ISO standard | Information security (Art. 15 cybersecurity) |

## Tool Execution Order (F5 CALL)

```
1. cex_memory_select.py       -- load relevant memory (F3, before COMPOSE)
2. cex_retriever.py           -- find similar artifacts (F5)
3. cex_schema_hydrate.py      -- validate schema constraints (F5)
4. [F6 PRODUCE -- artifact generated]
5. cex_compile.py             -- compile artifact (post-F6)
6. cex_doctor.py              -- structural health check (F7)
7. cex_score.py --apply       -- quality scoring (F7)
8. cex_sanitize.py --check    -- ASCII compliance check (pre-F8)
9. signal_writer               -- send completion signal (F8)
10. cex_memory_update.py      -- record learnings (F8)
```

## Tool Failure Handling

| Tool | Failure Mode | Recovery |
|------|-------------|---------|
| cex_compile.py | Frontmatter parse error | Fix frontmatter; re-run compile |
| cex_score.py | Score < 8.0 | Return to F6; address lowest-scoring D dimension first |
| cex_doctor.py | Missing required sections | Identify missing section; add content; re-run |
| cex_sanitize.py | Non-ASCII detected | Run --fix mode; verify no semantic change; re-check |
| signal_writer | Import error | Check _tools/ path; fallback: write .json to .cex/runtime/signals/ |
| cex_retriever.py | No results | Proceed without similar artifacts; note at F3 |

## Git Integration

```bash
# Stage and commit conformity assessment artifact
git add P11_govern/p11_ca_SYSTEM.md
git commit -m "[N03] conformity_assessment: medical_triage_system v1.0.0 (score: 9.0/10)"

# Verify commit
git log --oneline -1
```

## Debug Commands

| Purpose | Command |
|---------|---------|
| Check artifact word count | wc -w P11_govern/p11_ca_SYSTEM.md |
| Verify no placeholders remain | python -c "import re,sys; txt=open('P11_govern/p11_ca_SYSTEM.md').read(); sys.exit(1 if re.search(r'\{\{', txt) else 0)" |
| Check byte size | wc -c P11_govern/p11_ca_SYSTEM.md |
| Verify ASCII only | python _tools/cex_sanitize.py --check --scope P11_govern/p11_ca_SYSTEM.md |
| List all conformity artifacts | ls P11_govern/p11_ca_*.md |
