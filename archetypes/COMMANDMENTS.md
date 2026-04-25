# The 10 Commandments of CEX

---

1. ALL information = Dense Record (max 4KB)
2. EVERY Record = dual output (.md for humans + compiled/.yaml for machines)
3. EVERY Record = YAML frontmatter (kind, pillar, id, title, keywords 3+, bullets 3+)
4. NEVER prose longer than 3 lines (force bullets)
5. NEVER score < 7.0 (reject or redo)
6. ALWAYS scout before creating (prevent duplicates)
7. ALWAYS validate against the pillar's _schema.yaml
8. P01-P12 root schemas = read-only (only builders write)
9. Nuclei are independent (never depend on each other)
10. EVERY cycle improves the previous one (flywheel: CREATE > INDEX > USE > IMPROVE)

---

## Density Score

density = useful_tokens / total_tokens
RULE: density >= 0.8

Forbidden: running prose, TBD fields, paragraphs with no information, empty headers

---

## Vocabulary

| Term | Meaning |
|------|---------|
| kind | Shape of artifact (78: knowledge_card, agent, skill...) |
| pillar | Knowledge pillar (12: P01 Knowledge ... P12 Orchestration) |
| nucleus | Company department (7: N01 Intelligence ... N07 Admin) |
| function | LLM operation (8: BECOME ... COLLABORATE) |
| builder | Factory that creates 1 kind (13 ISO files) |
| compiled | Machine-readable output (.yaml/.json) |
| golden | Artifact with quality >= 9.5 |

---
*v2.0 | 2026-03-26*
