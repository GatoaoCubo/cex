---
description: "Show full CEX system status. Usage: /status"
---

# /status — System Health Dashboard

## Steps

1. Run system test (quick mode):
   ```bash
   python _tools/cex_system_test.py --quick
   ```
2. Check quality distribution:
   ```bash
   grep -r "^quality:" N0*/ --include="*.md" | sed 's/.*quality: //' | sort | uniq -c | sort -k2 -n
   ```
3. Check for quality:null remnants:
   ```bash
   grep -r "^quality: null" N0*/ --include="*.md" | wc -l
   ```
4. Recent signals:
   ```bash
   ls -lt .cex/runtime/signals/ | head -10
   ```
5. Recent learning records:
   ```bash
   ls -lt .cex/learning_records/ | head -10
   ```
6. Git status:
   ```bash
   git log --oneline -5
   git status --short
   ```
7. Report summary as a formatted table.
