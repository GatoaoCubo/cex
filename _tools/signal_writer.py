"""CEX Signal Writer v2.0 — writes to _ops/signals/"""
import json
from datetime import datetime
from pathlib import Path

SIGNAL_DIR = Path(__file__).resolve().parent.parent / "_ops" / "signals"

def write_signal(nucleus, status="complete", quality_score=9.0, mission="", **extra):
    SIGNAL_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now()
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
