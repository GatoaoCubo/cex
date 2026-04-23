---
kind: quality_gate
id: p11_qg_lens
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of lens artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Lens"
version: "1.0.0"
author: builder_agent
tags: [quality-gate, lens, perspective, P02, filter]
tldr: "Quality gate for lens artifacts: enforces declared bias, scoped focus, and explicit applies_to list."
domain: lens
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.85
related:
  - bld_architecture_lens
  - p03_ins_lens
  - p03_sp_lens_builder
  - lens-builder
  - bld_knowledge_card_lens
  - bld_schema_lens
  - bld_memory_lens
  - bld_collaboration_lens
  - bld_output_template_lens
  - p01_kc_lens
---

## Quality Gate

# Gate: Lens
## Definition
A `lens` is a perspective filter applied to artifact evaluation or routing. It amplifies certain attributes and suppresses others without executing logic. Gates here prevent lenses from claiming capabilities (which belong to agents), enforce honest bias declaration, and require a concrete `applies_to` scope so the lens is never applied indiscriminately.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p02_lens_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"lens"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | All required fields present and non-empty (`id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `perspective`, `applies_to`, `bias`, `tags`, `tldr`) | Incomplete artifact |
| H07 | `Focus` section present in body | Lens has no defined focus — unusable |
| H08 | `applies_to` is a list with >= 1 item | Lens has no target scope — unsafe to apply |
| H09 | `bias` field is explicitly declared (string value or `null` for neutral) | Hidden bias corrupts evaluations |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, states what the lens amplifies, not just its name |
| S02 | Focus narrowly scoped | 1.0 | Focus section targets one concern — not "quality in general" |
| S03 | Bias declaration honest | 1.0 | Bias names what the lens systematically over- or under-weights |
| S04 | `applies_to` types valid | 1.0 | Each item matches a known artifact `kind` in the registry |
| S05 | Interpretation criteria clear | 1.0 | Body defines what score high vs. low on this lens means |
| S06 | Weight or priority defined | 0.5 | `weight` or `priority` field present and numeric |
| S07 | Examples of lens application | 1.0 | >= 2 worked examples showing lens applied to a real artifact |
| S08 | `tags` includes `"lens"` | 0.5 | Minimum tag for routing |
| S09 | Complementary lenses referenced | 0.5 | `related` field names >= 1 lens that pairs with this one |
| S10 | No capability claims | 1.0 | Body contains no phrases like "this lens will execute", "performs", "runs" |
| S11 | Density >= 0.80 | 1.0 | No filler phrases: "provides a way to", "helps us understand", "in summary" |
| S12 | Limitations section present | 0.5 | Documents conditions where lens should not be applied |
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool + record in memory |
| >= 8.0 | PUBLISH | Commit to pool |
| >= 7.0 | REVIEW | Acceptable with documented improvement items |
| < 7.0 | REJECT | Revise and resubmit — do not publish |
| 0 (HARD fail) | REJECTED | Fix failing HARD gate(s) first |
## Bypass
Bypasses are logged and expire automatically.
| Field | Value |
|-------|-------|
| condition | Lens is experimental — `applies_to` scope cannot be confirmed until integration testing complete |
| approver | P02 domain owner |
| audit_log | Entry required in `records/governance/bypass_log.md` with gate ID, lens id, and test plan reference |
| expiry | 7 days — `applies_to` must be confirmed or lens moves to DRAFT state |
H01 and H05 cannot be bypassed under any condition.

## Examples

# Examples: lens-builder
## Golden Example
INPUT: "Create uma lens de cost para avaliar model_cards e embedding_configs"
OUTPUT:
```yaml
id: p02_lens_cost_efficiency
kind: lens
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
perspective: "cost_efficiency"
applies_to: [model_card, embedding_config, agent_card]
focus: "Pricing, token costs, and cost-per-task efficiency"
filters: [pricing, context_window, tokens_per_second, batch_size, dimensions]
bias: "Favors lower cost-per-output-token when quality is comparable"
interpretation: "Ranks artifacts by cost efficiency ratio: quality / cost. Higher = better."
weight: 0.8
priority: 1
scope: "LLM selection, agent_group model routing, embedding provider choice"
domain: "infrastructure-optimization"
quality: 8.8
tags: [lens, cost, efficiency, pricing, model-selection]
tldr: "Cost efficiency lens — evaluates artifacts by quality-to-cost ratio for infra decisions."
```
## Perspective
Evaluates artifacts through cost efficiency: what is the quality-per-dollar ratio?
Applies to model_cards (LLM pricing), embedding_configs (vector cost), agent_cards (model allocation).
## Filters
- **pricing**: input/output token costs, batch discounts, free tiers
- **context_window**: cost per context unit (larger window = fewer calls)
- **tokens_per_second**: throughput efficiency (faster = lower wall-clock cost)
- **batch_size**: bulk processing economics
- **dimensions**: embedding size vs retrieval accuracy tradeoff
## Application
1. Read the artifact's cost-related fields
2. Calculate quality-to-cost ratio where applicable
3. Compare against alternatives in the same kind
4. Flag artifacts where cost exceeds 2x the cheapest comparable option
## Limitations
- Does not evaluate quality directly (that is scoring_rubric P07)
- Ignores latency preferences (a speed lens would cover that)
- May undervalue high-cost options justified for critical tasks
## References
- LiteLLM pricing comparison
- Hugging Face MTEB leaderboard (embedding cost/quality)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p02_lens_ pattern (H02 pass)
- kind: lens (H04 pass)
- 20 frontmatter fields present (H06 pass)
- perspective non-empty string (H07 pass)
- applies_to has 3 entries (H08 pass)
- YAML parses cleanly (H01 pass)
- id == filename stem (H03 pass)
- tldr <= 160 chars, dense (S01 pass)
- tags list len >= 3, includes "lens" (S02 pass)
## Anti-Example
INPUT: "Create a cost lens"
BAD OUTPUT:
```yaml
id: cost_lens
kind: perspective
pillar: Model
perspective: Cost Analysis
applies_to: models
quality: 8.5
tags: cost
focus: Analyzing the cost of various things in great detail across many dimensions and aspects of the system to ensure we are making the most efficient choices possible
```
This is a general cost analysis document that covers everything about costs.
FAILURES:
1. id: no `p02_lens_` prefix -> H02 FAIL
2. kind: "perspective" not "lens" -> H04 FAIL
3. pillar: "Model" not "P02" -> H01 FAIL (wrong literal)
4. quality: 8.5 (not null) -> H05 FAIL
5. applies_to: string not list -> H08 FAIL
6. tags: string not list, len < 3 -> S02 FAIL
7. focus: filler prose ("great detail", "many dimensions") -> S07 FAIL
8. No body sections (Perspective, Filters, Application, Limitations) -> S03-S06 FAIL
9. perspective: natural case "Cost Analysis" instead of snake_case -> S05 FAIL
10. Missing required fields: version, created, updated, author, domain, tldr -> H06 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
