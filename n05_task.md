---
mission: SCORE_REFORM
nucleus: n05
wave: M2
created: 2026-04-17
priority: HIGH
effort: sonnet
---

# N05 SCORE_REFORM M2: Score sweep 112 quality:null artifacts

## TASK

Run structural+rubric scoring on all quality:null artifacts in N05_operations/.
This uses the reformed cex_score.py (no floor, real scores 0-10).

```bash
python _tools/cex_score.py --apply --null-only N05_operations/
```

After scoring, check distribution:
```bash
grep -r "quality:" N05_operations/ --include="*.md" | grep -v "null" | grep -oP "quality: [\d.]+" | sort -t: -k2 -n | uniq -c | sort -rn | head -20
```

Report how many scored above 8.0, between 6-8, below 6.

Then commit and signal:
```bash
git add N05_operations/
git commit -m "[N05] SCORE_REFORM M2: score 112 quality:null artifacts"
python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'score_m2_complete', 9.0)"
```

## COMPLETION CRITERIA
- [ ] quality:null count in N05_operations/ = 0
- [ ] git commit [N05] SCORE_REFORM M2
- [ ] signal sent: n05 -> score_m2_complete
