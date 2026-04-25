---
id: bld_qg_domain_vocabulary
kind: quality_gate
pillar: P11
llm_function: GOVERN
version: 1.0.0
quality: 8.3
tags: [domain_vocabulary, quality-gate, ubiquitous-language]
title: "Quality Gate: domain_vocabulary"
tldr: "Domain Vocabulary feedback: quality gate with scoring dimensions and pass/fail criteria"
density_score: 1.0
updated: "2026-04-17"
related:
  - p11_qg_glossary_entry
  - bld_instruction_glossary_entry
  - bld_examples_glossary_entry
  - p11_qg_agent_computer_interface
  - p11_qg_citation
  - p08_qg_capability_registry
  - p11_qg_creation_artifacts
  - bld_collaboration_glossary_entry
  - p01_kc_glossary_entry
  - p11_qg_context_window_config
---

## Quality Gate

# Quality Gate: domain_vocabulary
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | id matches `^dv_[a-z][a-z0-9_]+_vocabulary$` | Wrong pattern |
| H03 | kind == "domain_vocabulary" | Wrong kind |
| H04 | quality == null | Non-null value |
| H05 | bounded_context present and non-empty | Missing |
| H06 | governed_agents list non-empty | Empty or absent |
| H07 | term_count >= 3 | Fewer than 3 terms |
| H08 | Each term has definition + status | Missing required fields |
| H09 | No terms with status=deprecated missing replaced_by | Deprecated term without replacement |
| H10 | Total file size <= 5120 bytes | Exceeds max_bytes |

## SOFT Scoring
| ID | Dimension | Weight | 10pts | 5pts | 0pts |
|----|-----------|--------|-------|------|------|
| S01 | Anti-patterns per term | 1.0 | All terms have anti_patterns | >50% have anti_patterns | <50% |
| S02 | Industry standard references | 0.8 | All terms reference standard or "CEX-internal" | Some referenced | None |
| S03 | Term lifecycle completeness | 0.8 | proposed+active+deprecated all used | Only active | Only active |
| S04 | Loading instructions | 0.6 | F2b SPEAK instructions present | Partial | Absent |
| S05 | Deprecated terms documented | 0.8 | Table with old + new + date | Old+new, no date | No table |

## Score Tiers
| Score | Action |
|-------|--------|
| >= 9.0 | Publish; load at F2b SPEAK in governed agents |
| >= 7.0 | Use; add anti_patterns for low-coverage terms |
| < 7.0 | Return: add anti_patterns, industry refs, lifecycle |

## Examples

# Examples: domain_vocabulary
## Example 1: E-commerce Sales Vocabulary
```yaml
id: dv_sales_vocabulary
kind: domain_vocabulary
pillar: P01
title: "Sales Domain Vocabulary"
bounded_context: sales
governed_agents: [n01-intelligence, n06-commercial]
term_count: 4
quality: null
tags: [sales, vocabulary, ubiquitous-language]
```
Terms:
- Order: confirmed purchase with payment intent (NOT "cart" or "basket")
- Customer: person with active purchase history (NOT "user" or "client")
- Discount: price reduction with business rule (NOT "promo" or "deal")
- Fulfillment: physical/digital delivery process (NOT "shipping" alone)

## Example 2: CEX Core Vocabulary (partial)
```yaml
id: dv_cex_core_vocabulary
kind: domain_vocabulary
pillar: P01
title: "CEX Core Vocabulary"
bounded_context: cex-system
governed_agents: [n00-genesis, n07-orchestrator]
term_count: 6
quality: null
tags: [cex, vocabulary, core, ubiquitous-language]
```
Terms:
- kind: atomic artifact type (NOT "type" or "category")
- pillar: P01-P12 domain grouping (NOT "module" or "section")
- nucleus: N00-N07 operational agent (NOT "team" or "service")
- 8F: 8-function reasoning pipeline (NOT "workflow" or "checklist")

## Anti-example (WRONG)
```yaml
id: global_glossary        # WRONG: too broad, not scoped to BC
kind: domain_vocabulary    # WRONG intent: this would be a glossary or ontology
bounded_context: all       # WRONG: must be single BC
# Only 1 term            # WRONG: min 3 required
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
