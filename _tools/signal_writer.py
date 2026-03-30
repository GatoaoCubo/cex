"""CEX Signal Writer -- Completion signals for nucleus builders."""
import json
from datetime import datetime
from pathlib import Path

SIGNAL_DIR = Path(__file__).resolve().parent.parent / ".cex_signals"

def write_signal(nucleus, status="complete", quality_score=9.0, **extra):
    SIGNAL_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now()
    signal = {
        "nucleus": nucleus,
        "status": status,
        "quality_score": quality_score,
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
    if len(sys.argv) >= 2:
        write_signal(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "complete",
                     float(sys.argv[3]) if len(sys.argv) > 3 else 9.0)
