#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Memory Update -- Dynamic builder memory with decay, prune, and append.

Called AFTER builder execution to record new observations and maintain
memory hygiene (decay old observations, prune low-confidence entries).

Decay rates by type:
  feedback:  0.00 (permanent -- corrective knowledge)
  user:      0.02 (slow decay)
  reference: 0.03 (moderate decay)
  project:   0.05 (fast decay -- project context changes)

Usage:
    python cex_memory_update.py \
      --builder agent-builder \
      --type feedback \
      --observation "Agents with 3+ tools need guidance" \
      --pattern "Add tool-selection criteria when tools > 3" \
      --evidence "5 builds: 90pct with vs 55pct without" \
      --confidence 0.8 \
      --outcome SUCCESS
"""

import argparse
import re
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import parse_frontmatter

CEX_ROOT = Path(__file__).resolve().parent.parent
BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"

# --- T05: MemoryType integration ---
try:
    from cex_memory_types import should_save
    _HAS_MEMORY_TYPES = True
except ImportError:
    _HAS_MEMORY_TYPES = False

# Decay rates per observation type (applied per update cycle)
# T05: aligned with MemoryType enum decay rates
DECAY_RATES = {
    "feedback": 0.00,   # permanent (= MemoryType.CORRECTION)
    "correction": 0.00, # T05: alias
    "user": 0.02,
    "preference": 0.01, # T05: from MemoryType
    "reference": 0.03,
    "convention": 0.02, # T05: from MemoryType
    "project": 0.05,
    "context": 0.05,    # T05: from MemoryType
}

# Thresholds
MIN_CONFIDENCE = 0.1   # Auto-prune below this
MAX_OBSERVATIONS = 20  # Cap per builder


def load_memory_file(builder_id: str) -> tuple[Path | None, str, dict | None]:
    """Load a builder's bld_memory file.

    Returns: (path, raw_content, parsed_frontmatter)
    """
    builder_path = BUILDER_DIR / builder_id
    if not builder_path.exists():
        return None, "", None

    kind_slug = builder_id.replace("-builder", "")
    memory_file = builder_path / f"bld_memory_{kind_slug}.md"
    if not memory_file.exists():
        files = list(builder_path.glob("bld_memory_*.md"))
        if not files:
            return None, "", None
        memory_file = files[0]

    try:
        content = memory_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        return memory_file, content, fm
    except (OSError, UnicodeDecodeError):
        return None, "", None


def apply_decay(content: str, fm: dict) -> tuple[str, dict, int]:
    """Apply confidence decay to existing observations.

    Scans frontmatter confidence and body observations,
    reduces confidence by type-specific decay rate.

    Returns: (updated_content, updated_fm, pruned_count)
    """
    obs_type = fm.get("memory_scope", "project")
    decay_rate = DECAY_RATES.get(obs_type, 0.03)
    pruned = 0

    if decay_rate <= 0:
        return content, fm, 0

    # Decay the main frontmatter confidence
    current_conf = float(fm.get("confidence", 0.5))
    new_conf = max(current_conf - decay_rate, 0.0)
    fm["confidence"] = round(new_conf, 3)

    if new_conf < MIN_CONFIDENCE:
        pruned += 1

    return content, fm, pruned


def append_observation(
    content: str,
    fm: dict,
    observation: str,
    pattern: str,
    evidence: str,
    confidence: float,
    outcome: str,
    obs_type: str,
    session_id: str = "",
) -> tuple[str, dict]:
    """Append a new observation to the memory file.

    T05: Uses MemoryType classifier to auto-categorize and filter duplicates.
    """
    # --- T05: Auto-classify + dedup ---
    if _HAS_MEMORY_TYPES:
        try:
            save_ok, classified = should_save(observation, content)
            if not save_ok and "duplicate" in classified.lower():
                return content, fm  # skip only true duplicates
            # Auto-classify type if not explicitly set
            if save_ok and (not obs_type or obs_type == "project"):
                obs_type = classified  # auto-classified type
        except Exception:
            pass  # fallback to raw obs_type
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S")

    # Update frontmatter metadata
    fm["updated"] = time.strftime("%Y-%m-%d")
    obs_count = fm.get("observation_count", 1)
    fm["observation_count"] = obs_count + 1

    # Update average confidence
    avg_conf = fm.get("avg_confidence", fm.get("confidence", 0.5))
    new_avg = (avg_conf * obs_count + confidence) / (obs_count + 1)
    fm["avg_confidence"] = round(new_avg, 3)

    # If new observation has higher confidence, update main observation
    if confidence > float(fm.get("confidence", 0)):
        fm["confidence"] = confidence
        fm["observation"] = observation
        fm["pattern"] = pattern
        fm["evidence"] = evidence
        fm["outcome"] = outcome

    # Build new body section
    new_section = """
## Observation ({timestamp})
- **Type**: {obs_type}
- **Confidence**: {confidence:.2f}
- **Outcome**: {outcome}
- **Session**: {session_id or 'N/A'}

**Observation**: {observation}

**Pattern**: {pattern}

**Evidence**: {evidence}
"""

    # Append to body
    content = content.rstrip() + "\n" + new_section

    return content, fm


def rebuild_frontmatter(content: str, fm: dict) -> str:
    """Rebuild the file with updated frontmatter."""
    # Find body after frontmatter
    body = ""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            body = content[end + 3:].lstrip("\n")

    # Reconstruct frontmatter
    import yaml
    fm_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)

    return f"---\n{fm_str}---\n{body}"


def prune_low_confidence(content: str, fm: dict) -> tuple[str, dict, int]:
    """Remove observations with confidence below MIN_CONFIDENCE.

    Also enforces MAX_OBSERVATIONS cap.
    """
    pruned = 0

    # Count observation sections in body
    body_match = re.match(r'^---\n.*?\n---\s*', content, re.DOTALL)
    if not body_match:
        return content, fm, 0

    body = content[body_match.end():]
    header = content[:body_match.end()]

    # Split body into sections
    sections = re.split(r'(?=\n## Observation \()', body)
    kept_sections = []

    for section in sections:
        # Check if this is an observation section with confidence
        conf_match = re.search(r'\*\*Confidence\*\*:\s*(\d+\.?\d*)', section)
        if conf_match:
            conf = float(conf_match.group(1))
            if conf < MIN_CONFIDENCE:
                pruned += 1
                continue
        kept_sections.append(section)

    # Enforce MAX_OBSERVATIONS (keep most recent)
    obs_sections = [s for s in kept_sections if s.strip().startswith("## Observation")]
    non_obs = [s for s in kept_sections if not s.strip().startswith("## Observation")]

    if len(obs_sections) > MAX_OBSERVATIONS:
        pruned += len(obs_sections) - MAX_OBSERVATIONS
        obs_sections = obs_sections[-MAX_OBSERVATIONS:]

    new_body = "\n".join(non_obs + obs_sections)
    fm["observation_count"] = len(obs_sections) + 1  # +1 for the main frontmatter obs

    return header + new_body, fm, pruned


def update_builder_memory(
    builder_id: str,
    obs_type: str,
    observation: str,
    pattern: str = "",
    evidence: str = "",
    confidence: float = 0.5,
    outcome: str = "UNKNOWN",
    session_id: str = "",
) -> dict:
    """Full memory update cycle: load -> decay -> prune -> append -> save.

    Returns: summary dict with counts and status.
    """
    path, content, fm = load_memory_file(builder_id)
    if not path or not fm:
        return {"status": "error", "reason": f"No memory file for {builder_id}"}

    # 1. Apply decay
    content, fm, decay_pruned = apply_decay(content, fm)

    # 2. Prune low confidence
    content, fm, low_pruned = prune_low_confidence(content, fm)

    # 3. Append new observation
    content, fm = append_observation(
        content, fm, observation, pattern, evidence,
        confidence, outcome, obs_type, session_id,
    )

    # 4. Rebuild and save
    try:
        updated = rebuild_frontmatter(content, fm)
        path.write_text(updated, encoding="utf-8")
    except Exception as e:
        return {"status": "error", "reason": str(e)}

    return {
        "status": "ok",
        "builder_id": builder_id,
        "path": str(path),
        "decay_pruned": decay_pruned,
        "low_pruned": low_pruned,
        "observation_count": fm.get("observation_count", 1),
        "avg_confidence": fm.get("avg_confidence", confidence),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="CEX Memory Update -- dynamic builder memory")
    parser.add_argument("--builder", "-b", required=True, help="Builder ID (e.g. agent-builder)")
    parser.add_argument("--type", "-t", required=True,
                        choices=["feedback", "user", "reference", "project"],
                        help="Observation type")
    parser.add_argument("--observation", "-o", required=True, help="What was observed")
    parser.add_argument("--pattern", "-p", default="", help="Recommended pattern")
    parser.add_argument("--evidence", "-e", default="", help="Supporting evidence")
    parser.add_argument("--confidence", "-c", type=float, default=0.5, help="Confidence 0.0-1.0")
    parser.add_argument("--outcome", default="UNKNOWN",
                        choices=["SUCCESS", "PARTIAL", "FAILURE", "UNKNOWN"],
                        help="Outcome of the observation")
    parser.add_argument("--session-id", default="", help="Session identifier")
    args = parser.parse_args()

    result = update_builder_memory(
        builder_id=args.builder,
        obs_type=args.type,
        observation=args.observation,
        pattern=args.pattern,
        evidence=args.evidence,
        confidence=args.confidence,
        outcome=args.outcome,
        session_id=args.session_id,
    )

    if result["status"] == "ok":
        print(f"  Memory updated: {result['path']}")
        print(f"  Observations: {result['observation_count']}")
        print(f"  Avg confidence: {result['avg_confidence']:.2f}")
        print(f"  Decay pruned: {result['decay_pruned']}, Low pruned: {result['low_pruned']}")
    else:
        print(f"  ERROR: {result['reason']}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
