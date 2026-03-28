---
kind: config
id: bld_config_lifecycle_rule
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for lifecycle_rule production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: lifecycle_rule Production Rules

## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p11_lc_{rule_slug}.yaml | p11_lc_kc_freshness.yaml |
| Builder dir | kebab-case | lifecycle-rule-builder/ |
| Fields | snake_case | freshness_days, review_cycle |

Rule: id MUST equal filename stem.

## File Paths
- Output: cex/P11_feedback/examples/p11_lc_{rule_slug}.yaml
- Compiled: cex/P11_feedback/compiled/p11_lc_{rule_slug}.yaml

## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80

## Freshness Ranges by Domain Volatility
| Volatility | freshness_days | Example domains |
|------------|---------------|-----------------|
| High | 30-60 | model_card (pricing changes), scraper (site structure) |
| Medium | 60-120 | knowledge_card (domain facts), agent (capabilities) |
| Low | 120-365 | law (architectural rules), pattern (design patterns) |
| Stable | 365+ | interface (contracts), type_def (schemas) |

## Review Cycle Selection
| Artifact churn rate | Recommended cycle |
|--------------------|-------------------|
| Daily updates | weekly |
| Weekly updates | monthly |
| Monthly updates | quarterly |
| Rarely changes | yearly |
