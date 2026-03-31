# N03 Continuous Batch — Wave 5 (Final Polish + Verify)
**Autonomia Total** | **Quality 9.0+ target** | **Batch: 5/5**

## REGRAS
1. Leia `.claude/rules/n03-8f-enforcement.md` PRIMEIRO
2. Rodada final — verificar e polir

## TAREFA

### Step 1: Verificar que nenhum artefato ficou ≤8.4
```bash
python -c "
import sys; sys.path.insert(0, '_tools')
from cex_score import score_artifact
from pathlib import Path
below = []
for p in sorted(Path('.').glob('P[0-9][0-9]_*')):
    for f in sorted(p.rglob('*.md')):
        if 'compiled' in str(f) or f.name == 'README.md' or '_schema' in f.name: continue
        s, _ = score_artifact(str(f))
        if 0 < s <= 8.4: below.append((s, str(f)))
print(f'Remaining <=8.4: {len(below)}')
for s, p in sorted(below): print(f'  {s:.1f}  {p}')
"
```

### Step 2: Se restam ≤8.4, enriquecer cada um

### Step 3: Compile + Doctor final
```bash
python _tools/cex_compile.py --all
python _tools/cex_doctor.py
python -m pytest _tools/tests/ -q --tb=line
```

### Step 4: Score final report
```bash
python -c "
import sys; sys.path.insert(0, '_tools')
from cex_score import score_artifact
from pathlib import Path
scores = []
for p in sorted(Path('.').glob('P[0-9][0-9]_*')):
    for f in sorted(p.rglob('*.md')):
        if 'compiled' in str(f) or f.name == 'README.md' or '_schema' in f.name: continue
        s, _ = score_artifact(str(f))
        if s > 0: scores.append(s)
print(f'Total: {len(scores)} | Avg: {sum(scores)/len(scores):.2f} | Min: {min(scores):.1f}')
"
```

## COMMIT
```bash
git add -A
git commit -m "[N03] batch5: final polish + quality report"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'batch5_complete', 9.0)"
```
