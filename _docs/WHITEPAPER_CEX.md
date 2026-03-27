# CEX: A Relational Model for AI Knowledge

**Technical Whitepaper v2.0** | March 2026

*For developers, data architects, and AI engineers who understand why databases needed SQL -- and why AI codebases need the same revolution.*

---

## Abstract

Every AI framework solves execution: how to run chains, orchestrate agents, call tools. None solves organization: how to structure, discover, validate, and govern the knowledge that feeds those systems. CEX proposes a relational model for AI knowledge -- a typed, indexed, governed taxonomy that does for LLM artifacts what SQL did for data in 1970.

---

## 1. The Problem: AI Knowledge is Unstructured

Before SQL (1970): IBM used IMS, Honeywell used IDS. Each vendor had proprietary formats. Moving data meant rewriting everything.

After SQL: One relational model. Tables, rows, columns. Constraints. Any database, same grammar.

**AI knowledge in 2026 is where data was in 1969.**

> **Thesis**: AI knowledge is a database design problem disguised as a coding problem. The industry treats knowledge as STRING. CEX treats it as TYPED TABLE.

---

## 2. The 8 Functions: An Empirical Discovery

337 artifacts audited across 12 production frameworks (LangChain, CrewAI, DSPy, AutoGen, Haystack, LlamaIndex, Guidance, Instructor, Outlines, LMQL, LangGraph, Semantic Kernel).

| # | Function | Question | SQL Equivalent |
|---|----------|----------|----------------|
| 1 | BECOME | Who am I? | CREATE TABLE |
| 2 | INJECT | What do I know? | INSERT |
| 3 | REASON | How do I think? | WHERE clause |
| 4 | CALL | What tools? | Stored procedure |
| 5 | PRODUCE | What output? | SELECT result |
| 6 | CONSTRAIN | What rules? | CHECK + FK |
| 7 | GOVERN | Good enough? | EXPLAIN + AUDIT |
| 8 | COLLABORATE | Who next? | JOIN + FEDERATE |

**Coverage**: 319/337 artifacts (94.7%) map to 8 functions. 18 orphans = infra (CI/CD, README). Zero AI artifacts outside the 8.

**Isomorphism**: Maps 1:1 to Shannon (1948), OODA Loop, compiler architecture, and neuroscience models. Four independent domains, same 8 blocks.

**No 9th survives**: LEARN = GOVERN subset. REMEMBER = INJECT subset. ADAPT = REASON subset.

---

## 3. The Taxonomy: 78 Types in 12 Pillars

| Group | Pillars | Functions |
|-------|---------|-----------|
| CORE | P01 Knowledge, P02 Model, P03 Prompt, P04 Tools | BECOME, INJECT, REASON, CALL |
| QUALITY | P05 Output, P06 Schema, P07 Evals, P08 Architecture | PRODUCE, CONSTRAIN, GOVERN |
| SCALE | P09 Config, P10 Memory, P11 Feedback, P12 Orchestration | GOVERN, COLLABORATE |

### SQL Mapping

| SQL | CEX | Implementation |
|-----|-----|----------------|
| DATABASE | Repository | Git repo |
| SCHEMA | Pillar (P01-P12) | Directories |
| TABLE | Kind (78 types) | `_schema.yaml` |
| COLUMN | Frontmatter field | YAML header |
| ROW | Instance | One `.md` file |
| PRIMARY KEY | `id` field | == filename stem |
| FOREIGN KEY | `references[]` | Artifact ID array |
| INDEX | Naming convention | `{layer}_{kind}_{topic}.{ext}` |
| VIEW | `compiled/` | Materialized `.yaml` |
| CHECK | `max_bytes`, `density` | Pre-commit |
| STORED PROC | Builder (13 files) | Factory per kind |
| INFO_SCHEMA | `_schema.yaml` | Metadata of metadata |

### Normal Forms

- **1NF**: Each file = one atomic purpose
- **2NF**: Every field depends on complete identity
- **3NF**: Zero derivable redundancy. `density >= 0.80` IS normalization

---

## 4. Naming Convention as Index

Without index: `find -name "*.md"` = 4,264 results. O(n). Full scan.

With index: `find -name "bld_*_agent*"` = 13 results. O(1). Direct lookup. **23x fewer reads.**

### Grammar

```
{layer}_{kind}_{topic}.{ext}
```

- `layer`: `bld_` (builder), `tpl_` (template), `ex_` (example)
- `kind`: 1 of 78 types (full words, zero abbreviation)
- `topic`: domain subject
- Rules: Max 50 chars. snake_case. ASCII. id == stem.

Fractal: same grammar at L0 (builders), L1 (schemas), L2 (instances).

---

## 5. The Compilation Pipeline

### The Bottleneck

Human gives 9 tokens (7% coverage). LLM needs 8 dimensions (100%). Gap: 93%.

### 5 Phases

```
INTENT -> CAPTURE -> DECOMPOSE -> HYDRATE -> COMPILE -> ENVELOPE -> PROMPT
(9 tok)                                                           (450+ tok)
```

Amplification: 50:1 to 150:1.

### Hybrid Engine

| Phase | Engine | Cost | Deterministic |
|-------|--------|------|---------------|
| CAPTURE | Python | $0 | Yes |
| DECOMPOSE | LLM micro | ~$0.001 | No |
| HYDRATE | Python+SQLite | $0 | Yes |
| COMPILE | Python+Jinja2 | $0 | Yes |
| ENVELOPE | Python | $0 | Yes |

80% deterministic. Cost reduction: ~90% vs full LLM.

---

## 6. Governance Without Runtime

| Layer | Mechanism | Universal |
|-------|-----------|-----------|
| LAW | `CODEX.md` + `_schema.yaml` | Read-dependent |
| GATE | Pre-commit hook (7 checks) | Yes (blocks all) |
| GUARD | `cex_doctor.py` | On-demand |

FK integrity: `references[]` validated at commit. `cex doctor --cascade` shows deletion impact.

---

## 7. Builders: Stored Procedures

70 builders x 13 files = 910 stored procedures. Self-referential: the system bootstraps itself. system-prompt-builder follows schemas from validation-schema-builder, built by instruction-builder.

---

## 8. An LLM's Perspective

In unstructured repos: grep, trial and error, full table scan per query. In CEX: `find -name "bld_*_agent*"` = 13 exact files. Naming IS index. Frontmatter IS schema. `references[]` IS FK graph. 23x fewer reads. Lower cost. Higher accuracy. Reproducible.

> If SQL made data accessible to any program, CEX makes knowledge accessible to any model.

---

## 9. Industry Coverage

337 artifacts from 12 frameworks: 94.7% mapped to CEX's 78 kinds. Zero AI artifacts outside the 8 functions.

---

## 10. Complementary, Not Competing

CEX organizes what AI knows. LangChain/CrewAI execute what AI does. Different layers. Complementary.

---

## References

1. Codd (1970). A Relational Model of Data. *CACM*.
2. Shannon (1948). A Mathematical Theory of Communication.
3. Boyd (1996). OODA Loop.
4. Wei et al. (2022). Chain-of-Thought Prompting. *NeurIPS*.
5. Yao et al. (2022). ReAct. *ICLR*.
6. Khattab et al. (2023). DSPy. *arXiv*.
7. SQLite Consortium. Most deployed database engine.
8. Anthropic (2024-2026). Claude System Prompt Best Practices.

---

*CEX v2.0 -- "SQL organized data. CEX organizes intelligence."*
