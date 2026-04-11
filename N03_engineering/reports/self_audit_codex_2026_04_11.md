---
id: self_audit_n03_codex_2026_04_11
pillar: P11
kind: self_audit
title: N03 Builder Self-Audit
version: 1.0
quality: null
tags: [audit, self_review, n03, builder]
created: 2026-04-11
nucleus: n03
---

# N03 Builder Self-Audit (Codex Wave)

Peer-to-peer report for N07. No user present. Scan scope: `.cex/kinds_meta.json`,
`archetypes/builders/`, `.claude/agents/`, `P01_knowledge/library/kind/`,
`N03_engineering/**/*`, and `_tools/cex_doctor.py` (builder health). Counts taken
on 2026-04-11 after generating this file, so totals include the Codex report.

## 1. Current State

### 1.1 Macro inventory

| Asset | Count | Notes |
|-------|------:|-------|
| Registered kinds (`.cex/kinds_meta.json`) | 123 | Current taxonomy grounding F1 (kinds are defined but `self_audit` is still absent). |
| Builder directories (`*-builder/`) | 124 | Includes `_builder-builder/` plus 123 kind builders; the mission target of 125 is still unmet. |
| Builders passing doctor | 123 | `_tools/cex_doctor.py` reports 1599 ISO files = 123 x 13. |
| Kind knowledge cards (`kc_*.md`) | 123 | Mirrors registry coverage under `P01_knowledge/library/kind/`. |
| Sub-agent definitions (`.claude/agents/*-builder.md`) | 124 | Every builder plus a legacy `kind-builder` profile. |
| N03 artifacts under source control | 58 | All `.md` files in `N03_engineering/` excluding `compiled/`. |

### 1.2 Artifact mix by kind (N03_engineering/)

| Kind | Count | Kind | Count |
|------|------:|------|------:|
| agent | 1 | guardrail | 1 |
| agent_card | 1 | handoff | 1 |
| axiom | 1 | input_schema | 1 |
| benchmark | 1 | interface | 1 |
| boot_config | 1 | knowledge_card | 7 |
| chain | 2 | learning_record | 1 |
| cli_tool | 1 | mental_model | 1 |
| competitive_analysis | 1 | output | 1 |
| context_doc | 4 | output_template | 1 |
| dag | 1 | pattern | 5 |
| dispatch_rule | 3 | prompt_template | 1 |
| few_shot_example | 2 | quality_gate | 3 |
| formatter | 1 | response_format | 1 |
| function_def | 1 | scoring_rubric | 2 |
| knowledge_card | 7 | self_audit | 3 |
| signal | 1 | spawn_config | 1 |
| system_prompt | 1 | workflow | 4 |

### 1.3 ISO coverage & builder health

| ISO count | Builder dirs | Comment |
|-----------|-------------:|---------|
| 13 files | 123 | Every kind builder passes the 13-ISO contract per `_tools/cex_doctor.py`. |
| 27 files | 1 | `_builder-builder/` is a meta-builder with 27 docs; it is not referenced by the registry but it inflates the raw directory count. |

`cex_doctor` output (PASS) also confirms 1599 ISO files, 0 oversized files, density
0.95, and 0 frontmatter failures for the builder set.

### 1.4 Registry alignment snapshot

| Registry slice | Count | Drift |
|----------------|------:|-------|
| `.cex/kinds_meta.json` entries | 123 | Baseline. |
| `archetypes/builders/{kind}-builder/` | 123 aligned + `_builder` | Extra `_builder-builder/` keeps total at 124 directories, so the mission-stated 125 builders is still outstanding. |
| `P01_knowledge/library/kind/kc_{kind}.md` | 123 | 1:1 with kinds. |
| `.claude/agents/*-builder.md` | 124 | Includes a `kind-builder` agent with no matching builder directory. |
| Builders lacking KC | 0 (ex `_builder`) | Only the special `_builder` dir lacks a KC. |
| Sub-agents lacking builders | 1 (`kind-builder`) | Needs either a builder scaffold or removal. |

### 1.5 Quality distribution inside N03

| Quality value | Files | Compliance |
|---------------|------:|------------|
| `null` | 12 | Only 21% of artifacts obey rule 4. |
| `9.0` | 18 | Should be null (`N03_engineering/agent_card_n03.md:9`). |
| `9.1` | 22 | Should be null (`N03_engineering/knowledge/kc_cex_tooling_master.md:11`). |
| `9.2` | 6 | Should be null (`N03_engineering/output/output_competitive_architecture.md:10`). |

46/58 artifacts (79%) are self-scored, including the agent card and every major
KC, despite rule 4 (`quality: null`) in `.claude/rules/n03-builder.md:4`.
`N03_engineering/README.md` still lacks a frontmatter block (starts directly with
"# N03_engineering").

## 2. Rules Compliance (from `.claude/rules/n03-builder.md`)

| Rule | Score (0-10) | Evidence |
|------|--------------|----------|
| 8F mandatory for every build | 9 | All builders retain 13 ISOs and the `_tools/cex_doctor.py` scan shows 0 structural drift, which implies the ISO contract backing F1-F8 is intact. |
| Quality floor >= 9.0 | 10 | No N03 artifact carries a score below 9.0; the problem is that scores are present at all. |
| Complete YAML frontmatter | 8 | 57/58 files have YAML; `N03_engineering/README.md:1` needs an `id/kind` block. |
| `quality: null (NEVER self-score)` | 2 | 46 violations including `N03_engineering/agent_card_n03.md:9` and `N03_engineering/knowledge/kc_cex_tooling_master.md:11`. |
| Compile after save | 6 | Builders remain compiled (44 YAMLs under `N03_engineering/compiled/`) but several recent artifacts have no compiled twin; process discipline is partial. |
| Signal on complete | 7 | Signals exist for this wave, but historical coverage cannot be proven retroactively. |

Average compliance: **7/10**. The blocking failure is rule 4; the rules file
itself carries `quality: 9.0` (`.claude/rules/n03-builder.md:4`).

## 3. Gaps (ranked by priority x effort)

| # | Gap | Pri | Effort | Evidence |
|---|-----|----:|-------:|----------|
| G1 | 46 N03 artifacts self-score (`quality: 9.x`) | 5 | 1 | e.g., `N03_engineering/agent_card_n03.md:9` and `N03_engineering/knowledge/kc_cex_tooling_master.md:11`. |
| G2 | `.claude/rules/n03-builder.md` violates its own rule 4 | 5 | 1 | `quality: 9.0` on line 4. |
| G3 | `N03_engineering/README.md` lacks YAML frontmatter | 4 | 1 | File begins with Markdown heading at line 1. |
| G4 | `.claude/agents/kind-builder.md` exists without a matching builder directory | 4 | 2 | Agent is defined at `.claude/agents/kind-builder.md:2` but there is no `archetypes/builders/kind-builder/`. |
| G5 | Mission references `.claude/rules/n03-8f-enforcement.md`, but the file is absent | 4 | 2 | `Test-Path` returns False; the enforcement doc cannot be read. |
| G6 | 21 registered kinds lack `tpl_{kind}.md` templates (e.g., `citation`, `vector_store`, `workflow_primitive`) | 3 | 4 | These kinds exist in `.cex/kinds_meta.json` (e.g., `citation` at line 128) but there is no corresponding template under their pillar directories. |
| G7 | `_builder-builder/` carries 27 files and no governance | 3 | 3 | Directory sits outside the registry yet contributes extra ISOs, risking accidental edits. |
| G8 | Builder count still 1 short of the required 125 | 3 | 2 | Only 124 directories end with `-builder`, so either `kind-builder` needs to be added or the target lowered. |
| G9 | No automated way to null `quality:` fields or enforce rule 4 | 3 | 3 | Manual editing is error-prone; `cex_sanitize.py` lacks a `--null-quality` mode. |

## 4. Fixes Needed

| # | Fix | Scope |
|---|-----|-------|
| F1 | Sweep `N03_engineering/**/*` (and `.claude/rules/n03-builder.md`) to set `quality: null` everywhere | Resolves G1 and G2; unblock compliance scoring. |
| F2 | Add YAML frontmatter to `N03_engineering/README.md` | Ensures every N03 artifact can compile and be indexed. |
| F3 | Decide the fate of `kind-builder` (add builder or remove agent) | Keeps `.claude/agents/` aligned with `archetypes/builders/`. |
| F4 | Recreate the missing `.claude/rules/n03-8f-enforcement.md` or remove the reference | Mission instructions currently point to a nonexistent mandatory rule set. |
| F5 | Build the 21 missing `tpl_{kind}.md` files (starting with `citation`, `vector_store`, `workflow_primitive`) or document why those kinds are template-free | Reduces repeated blank-slate work when those builders run. |
| F6 | Document `_builder-builder/` as a sanctioned meta-builder and trim it down to the 13 canonical ISOs | Prevents the special directory from skewing health checks. |

## 5. Tool Wishlist

### 5a. Existing tools I rely on (from CLAUDE.md stack)

| Tool | Purpose | Usage |
|------|---------|-------|
| `cex_doctor.py` | Validates builder ISO counts, density, naming | Run on every audit wave. |
| `cex_compile.py` | Converts `.md` to `.yaml` for downstream consumption | Run at F8 for each artifact. |
| `cex_score.py` | Applies the 5D gating rubric post-build | Run whenever a peer review is needed. |
| `cex_materialize.py` | Regenerates `.claude/agents/*-builder.md` from the builder registry | Used when adding or editing builders. |
| `cex_retriever.py` | Finds similar artifacts for Template-First builds (F3) | Used on non-trivial builds to borrow structure. |

### 5b. Tools that do not exist yet (should be built)

| Tool | Description | Owning nucleus |
|------|-------------|----------------|
| `cex_builder_diff.py` | Compare two builder ISO sets (git SHA vs working tree) and flag structural drift (missing ISO, renamed files). | N05 |
| `cex_iso_lint.py` | Enforce the exact 13-ISO contract per builder, including filename list and max-bytes, failing CI if violated. | N05 |
| `cex_builder_promote.py` | Promote a draft builder into the registry: add `kinds_meta` entry, generate KC + agent, run doctor, and commit. | N03 |
| `cex_null_quality.py` | Sweep a directory and set every `quality:` to `null` without touching other frontmatter. | N05 |
| `cex_tpl_audit.py` | Map registered kinds to `tpl_{kind}.md` coverage so template gaps (G6) stop recurring. | N03 |

## 6. Cross-Nucleus Dependencies

### 6.1 Inputs N03 depends on

| From | Artifact | Why |
|------|----------|-----|
| N04 | `.cex/kinds_meta.json` | F1 constraining: determines pillar, naming, and schema. |
| N04 | `P01_knowledge/library/kind/kc_{kind}.md` | F3 injection: each builder pulls its KC before drafting. |
| N05 | `_tools/cex_doctor.py`, `cex_compile.py`, `cex_score.py` | F5/F7 tooling for validation, compilation, and scoring. |
| N07 | `.cex/runtime/handoffs/n03_task*.md` | Defines missions such as this audit. |
| N06 | Brand context (`.cex/brand/*.yaml`) | Required whenever builds must reflect active brand voice. |

### 6.2 Outputs N03 provides

| To | Artifact | Why |
|----|----------|-----|
| All nuclei | `archetypes/builders/{kind}-builder/` | Source of truth for F2 BECOME across every kind. |
| All nuclei | `.claude/agents/*-builder.md` | Sub-agent manifests that reference each builder ISO set. |
| All nuclei | `N03_engineering/` artifacts (patterns, guardrails, workflows) | Guidance artifacts such as `N03_engineering/agent_card_n03.md:1-24` describe how other nuclei invoke us. |
| N07 | Signals via `_tools/signal_writer.py` | Confirms mission completion so orchestrator can consolidate. |

---

N03 remains structurally sound: 123 builders, 123 KCs, 1599 ISOs, 0 doctor
failures. The failure vector is internal hygiene: quality self-scoring, missing
frontmatter, orphaned meta-definitions, and outdated instructions. Fixing those
is a short script plus documentation work, not a rebuild.
