# 10 Mandamentos do CEX

---

1. TODA informacao = Record denso (max 4KB, ~1000 tokens)
2. TODO Record = dual output (.md humano + .yaml LLM)
3. TODO Record = metadata densa (keywords 3+, bullets 3+, axioms 1+)
4. NUNCA prosa > 3 linhas (force bullets)
5. NUNCA score < 7.0 no brain (rejeita ou refaz)
6. SEMPRE scout antes de criar (evita duplicata)
7. SEMPRE validar contra _schema.yaml do LP
8. BRAIN (P01-P12 root) = read-only (so Edison+Pytha escrevem)
9. SATELLITES = independentes (nunca dependem uns dos outros)
10. CADA ciclo melhora o anterior (flywheel: CREATE>INDEX>USE>IMPROVE)

---

## Density Score

density = tokens_uteis / tokens_total
REGRA: density >= 0.8

Proibido: prosa corrida, campos TBD, paragrafos sem info, headers vazios

---
*v1.0 | 2026-03-22*