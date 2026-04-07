---
description: "System health dashboard. Usage: /status"
---

# /status

Run these diagnostics and report a summary:

```bash
python _tools/cex_doctor.py          # Builder health (119 checks)
python _tools/cex_flywheel_audit.py  # Doc vs practice (109 wires)
python _tools/cex_sanitize.py --check --scope _tools/  # ASCII compliance
python _tools/cex_release_check.py   # Release gate (28 checks)
bash _spawn/dispatch.sh status       # Running nuclei
```

Report format:
```
Doctor:   X PASS / Y WARN / Z FAIL
Flywheel: X% (WIRED/BROKEN/PHANTOM)
ASCII:    X issues
Release:  X/28 checks
Nuclei:   X running
```
