---
kind: config
id: bld_config_scoring_rubric
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for scoring_rubric production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: scoring_rubric Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_sr_{framework_slug}.md | p07_sr_5d_knowledge_card.md |
| Builder dir | kebab-case | scoring-rubric-builder/ |
| Fields | snake_case | dimensions_count, threshold_golden |
| Framework names | descriptive slug | 5d, 12lp, kc_quality |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P07_evals/examples/p07_sr_{framework_slug}.md
- Compiled: cex/P07_evals/compiled/p07_sr_{framework_slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 5120 bytes
- Density: >= 0.80
- Dimensions: >= 3 (no upper limit, but 3-8 recommended)
## Weight Policy
- All dimension weights MUST sum to exactly 100%
- Integer percentages preferred (25%, 20%, 15%)
- No dimension below 5% (too small to matter)
- No dimension above 40% (avoid single-dimension dominance)
