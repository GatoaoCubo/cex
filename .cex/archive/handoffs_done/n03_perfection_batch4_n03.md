# N03 Continuous Batch — Wave 4 (Next 30: score 8.4)
**Autonomia Total** | **Quality 9.0+ target** | **Batch: 4/5**

## REGRAS
1. Leia `.claude/rules/n03-8f-enforcement.md` PRIMEIRO
2. `python _tools/cex_score.py P{05..12}_*/templates/*.md P{05..12}_*/examples/*.md` — find ≤8.4
3. Para cada: leia → enriqueça body → salve
4. Mantenha frontmatter válido. quality: null (NUNCA auto-score)

## TAREFA
Scan e enriqueça TODOS templates/examples em P05-P12 com score ≤ 8.4.

Comando para descobrir:
```bash
python -c "
import sys; sys.path.insert(0, '_tools')
from cex_score import score_artifact
from pathlib import Path
for p in sorted(Path('.').glob('P[0-9][0-9]_*')):
    for f in sorted(p.rglob('*.md')):
        if 'compiled' in str(f) or f.name == 'README.md' or '_schema' in f.name: continue
        s, _ = score_artifact(str(f))
        if 0 < s <= 8.4: print(f'{s:.1f}  {f}')
"
```

Enriqueça até 15 artefatos neste batch. Para cada:
- Adicionar `tldr:`, `tags:`, `density_score:` no frontmatter se ausentes
- Expandir body com conteúdo real
- Garantir ≥5 seções ##, ≥1 tabela ou code block

## COMMIT
```bash
git add -A
git commit -m "[N03] batch4: enrich P05-P12 templates (target 8.8+)"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'batch4_complete', 9.0)"
```
