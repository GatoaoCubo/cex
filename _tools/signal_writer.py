"""CEX Signal Writer v2.1 — writes to .cex/runtime/signals/ with validation"""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

SIGNAL_DIR = Path(__file__).resolve().parent.parent / ".cex" / "runtime" / "signals"
VALID_NUCLEI = {"n01", "n02", "n03", "n04", "n05", "n06", "n07"}

def write_signal(nucleus, status="complete", quality_score=9.0, mission="", **extra):
    nucleus = nucleus.lower()
    if nucleus not in VALID_NUCLEI:
        raise ValueError(f"Invalid nucleus '{nucleus}'. Must be one of: {sorted(VALID_NUCLEI)}")
    if not isinstance(quality_score, (int, float)) or not (0 <= quality_score <= 10):
        raise ValueError(f"quality_score must be 0-10, got {quality_score}")
    if not re.match(r'^[a-z_]+$', status):
        raise ValueError(f"Invalid status '{status}'. Must be lowercase alpha/underscore.")
    SIGNAL_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    signal = {
        "nucleus": nucleus,
        "status": status,
        "quality_score": quality_score,
        "mission": mission,
        "timestamp": now.isoformat(),
        **extra,
    }
    filename = f"signal_{nucleus}_{now.strftime('%Y%m%d_%H%M%S')}.json"
    path = SIGNAL_DIR / filename
    path.write_text(json.dumps(signal, indent=2), encoding="utf-8")
    print(f"[SIGNAL] {nucleus} -> {status} (score: {quality_score})")
    return str(path)

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    write_signal(
        args[0] if len(args) > 0 else "n03",
        args[1] if len(args) > 1 else "complete",
        float(args[2]) if len(args) > 2 else 9.0,
        args[3] if len(args) > 3 else "",
    )
