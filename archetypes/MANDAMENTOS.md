# 10 Mandamentos do CEX

---

1. TODA informacao = Record denso (max 4KB)
2. TODO Record = dual output (.md humano + compiled/.yaml maquina)
3. TODO Record = frontmatter YAML (kind, pillar, id, title, keywords 3+, bullets 3+)
4. NUNCA prosa > 3 linhas (force bullets)
5. NUNCA score < 7.0 (rejeita ou refaz)
6. SEMPRE scout antes de criar (evita duplicata)
7. SEMPRE validar contra _schema.yaml do pillar
8. P01-P12 root schemas = read-only (so builders escrevem)
9. Nuclei sao independentes (nunca dependem uns dos outros)
10. CADA ciclo melhora o anterior (flywheel: CREATE>INDEX>USE>IMPROVE)

---

## Density Score

density = tokens_uteis / tokens_total
REGRA: density >= 0.8

Proibido: prosa corrida, campos TBD, paragrafos sem info, headers vazios

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