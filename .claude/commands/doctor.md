---
description: "Run full health check. Usage: /doctor"
---

# /doctor — Full Health Check

## Steps

1. Builder health:
   ```bash
   python _tools/cex_doctor.py
   ```
2. Artifact validation:
   ```bash
   python _tools/cex_hooks.py validate-all
   ```
3. Compilation:
   ```bash
   python _tools/cex_compile.py --all
   ```
4. Feedback report:
   ```bash
   python _tools/cex_feedback.py
   ```
5. Report: doctor results, hook errors, compile status, feedback summary.
