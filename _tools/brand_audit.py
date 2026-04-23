# -*- coding: utf-8 -*-
"""brand_audit.py -- Score brand consistency across CEX artifacts.

Scans all artifacts referencing brand variables and scores consistency
across 6 dimensions. Uses brand_config.yaml as reference.

Usage:
    python _tools/brand_audit.py [--config path] [--json] [--verbose]
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml", "-q"])
    import yaml

ROOT = Path(__file__).resolve().parent.parent
BRAND_CONFIG = ROOT / ".cex" / "brand" / "brand_config.yaml"

WEIGHTS = {
    "archetype_alignment": 0.25,
    "voice_consistency": 0.20,
    "visual_coherence": 0.20,
    "positioning_clarity": 0.15,
    "narrative_integrity": 0.10,
    "config_completeness": 0.10,
}


def load_brand_config(path: Path = BRAND_CONFIG) -> dict:
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def is_placeholder(value) -> bool:
    if value is None:
        return True
    s = str(value)
    return s.startswith("{{") and s.endswith("}}")


def scan_brand_references(root: Path) -> dict:
    """Scan .md files for {{BRAND_*}} references and resolved brand values."""
    refs = defaultdict(list)
    brand_pattern = re.compile(r"\{\{(BRAND_[A-Z_]+)\}\}")
    skip = {".git", "node_modules", ".cex", "_tools", "compiled"}

    for md in root.rglob("*.md"):
        if any(s in md.parts for s in skip):
            continue
        try:
            content = md.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue
        matches = brand_pattern.findall(content)
        if matches:
            refs[str(md.relative_to(root))] = list(set(matches))
    return dict(refs)


def score_config_completeness(config: dict) -> tuple:
    """Score brand_config completeness (0-1)."""
    required = [
        ("identity", "BRAND_NAME"), ("identity", "BRAND_TAGLINE"),
        ("identity", "BRAND_MISSION"), ("identity", "BRAND_VALUES"),
        ("archetype", "BRAND_ARCHETYPE"),
        ("voice", "BRAND_VOICE_TONE"), ("voice", "BRAND_VOICE_FORMALITY"),
        ("audience", "BRAND_ICP"), ("audience", "BRAND_TRANSFORMATION"),
        ("visual", "BRAND_COLORS"),
        ("positioning", "BRAND_CATEGORY"), ("positioning", "BRAND_UVP"),
        ("monetization", "BRAND_PRICING_MODEL"),
    ]
    filled = 0
    issues = []
    for section, field in required:
        if section in config and field in config[section]:
            val = config[section][field]
            if not is_placeholder(val):
                filled += 1
            else:
                issues.append(f"{field} is placeholder")
        else:
            issues.append(f"{field} missing")

    return filled / len(required), issues


def score_archetype_alignment(config: dict) -> tuple:
    """Score archetype consistency."""
    arch = config.get("archetype", {})
    issues = []
    score = 0.0

    if "BRAND_ARCHETYPE" in arch and not is_placeholder(arch["BRAND_ARCHETYPE"]):
        valid = {"creator", "hero", "sage", "explorer", "rebel", "magician",
                 "lover", "caregiver", "jester", "ruler", "innocent", "everyman"}
        if arch["BRAND_ARCHETYPE"].lower() in valid:
            score += 0.5
        else:
            issues.append(f"Invalid archetype: {arch['BRAND_ARCHETYPE']}")

        if "BRAND_PERSONALITY" in arch and not is_placeholder(arch.get("BRAND_PERSONALITY")):
            traits = arch["BRAND_PERSONALITY"]
            if isinstance(traits, list) and len(traits) >= 3:
                score += 0.3
            else:
                issues.append("Need 3+ personality traits")

        if "BRAND_ARCHETYPE_SHADOW" in arch and not is_placeholder(arch.get("BRAND_ARCHETYPE_SHADOW")):
            score += 0.2
        else:
            issues.append("No shadow archetype defined")
    else:
        issues.append("No archetype defined")

    return score, issues


def score_voice_consistency(config: dict) -> tuple:
    """Score voice dimension completeness."""
    voice = config.get("voice", {})
    issues = []
    dims_filled = 0
    dims_total = 5

    for dim in ["BRAND_VOICE_FORMALITY", "BRAND_VOICE_ENTHUSIASM", "BRAND_VOICE_HUMOR",
                "BRAND_VOICE_WARMTH", "BRAND_VOICE_AUTHORITY"]:
        val = voice.get(dim)
        if val is not None and not is_placeholder(val) and isinstance(val, int) and 1 <= val <= 5:
            dims_filled += 1
        else:
            issues.append(f"{dim} not scored (1-5)")

    score = dims_filled / dims_total
    if voice.get("BRAND_VOICE_DO") and isinstance(voice["BRAND_VOICE_DO"], list):
        if len([d for d in voice["BRAND_VOICE_DO"] if not is_placeholder(d)]) >= 3:
            score = min(1.0, score + 0.1)

    return score, issues


def score_visual_coherence(config: dict) -> tuple:
    """Score visual identity completeness."""
    visual = config.get("visual", {})
    colors = visual.get("BRAND_COLORS", {})
    issues = []
    score = 0.0

    hex_pat = re.compile(r"^#[0-9a-fA-F]{6}$")
    required_colors = ["primary", "secondary", "accent"]
    for c in required_colors:
        val = colors.get(c, "")
        if val and not is_placeholder(val) and hex_pat.match(str(val)):
            score += 0.2
        else:
            issues.append(f"BRAND_COLORS.{c} invalid or missing")

    fonts = visual.get("BRAND_FONTS", {})
    if isinstance(fonts, dict) and any(not is_placeholder(v) for v in fonts.values()):
        score += 0.2
    else:
        issues.append("No fonts defined")

    if visual.get("BRAND_STYLE") and not is_placeholder(visual.get("BRAND_STYLE")):
        score += 0.2

    return min(1.0, score), issues


def score_positioning_clarity(config: dict) -> tuple:
    """Score positioning completeness."""
    pos = config.get("positioning", {})
    issues = []
    score = 0.0

    if pos.get("BRAND_CATEGORY") and not is_placeholder(pos.get("BRAND_CATEGORY")):
        score += 0.3
    else:
        issues.append("No category defined")

    uvp = pos.get("BRAND_UVP", "")
    if uvp and not is_placeholder(uvp) and len(str(uvp)) >= 20:
        score += 0.4
    else:
        issues.append("UVP missing or too short")

    if pos.get("BRAND_DIFFERENTIATOR") and not is_placeholder(pos.get("BRAND_DIFFERENTIATOR")):
        score += 0.3
    else:
        issues.append("No differentiator defined")

    return score, issues


def score_narrative_integrity(config: dict) -> tuple:
    """Score narrative completeness."""
    identity = config.get("identity", {})
    audience = config.get("audience", {})
    issues = []
    score = 0.0

    if identity.get("BRAND_STORY") and not is_placeholder(identity.get("BRAND_STORY")):
        if len(str(identity["BRAND_STORY"])) >= 200:
            score += 0.4
        else:
            issues.append("BRAND_STORY too short (need 200+ chars)")
    else:
        issues.append("No brand story")

    if identity.get("BRAND_MISSION") and not is_placeholder(identity.get("BRAND_MISSION")):
        score += 0.3
    else:
        issues.append("No mission statement")

    transform = audience.get("BRAND_TRANSFORMATION", "")
    if transform and not is_placeholder(transform):
        if re.match(r"From .+ to .+ through .+", str(transform), re.IGNORECASE):
            score += 0.3
        else:
            issues.append("Transformation arc doesn't follow From/To/Through pattern")
    else:
        issues.append("No transformation arc")

    return score, issues


def audit(config: dict) -> dict:
    """Run full brand audit."""
    dimensions = {}

    score_fns = {
        "archetype_alignment": score_archetype_alignment,
        "voice_consistency": score_voice_consistency,
        "visual_coherence": score_visual_coherence,
        "positioning_clarity": score_positioning_clarity,
        "narrative_integrity": score_narrative_integrity,
        "config_completeness": score_config_completeness,
    }

    overall = 0.0
    for dim, fn in score_fns.items():
        score, issues = fn(config)
        dimensions[dim] = {"score": round(score, 2), "issues": issues}
        overall += score * WEIGHTS[dim]

    # Rating
    if overall >= 0.95:
        rating = "Excellent"
    elif overall >= 0.85:
        rating = "Healthy"
    elif overall >= 0.70:
        rating = "Needs Work"
    else:
        rating = "Critical"

    brand_name = config.get("identity", {}).get("BRAND_NAME", "unknown")

    return {
        "brand": brand_name,
        "overall_score": round(overall, 3),
        "rating": rating,
        "dimensions": dimensions,
        "references": scan_brand_references(ROOT),
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Audit brand consistency")
    parser.add_argument("--config", default=str(BRAND_CONFIG))
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    config = load_brand_config(Path(args.config))
    if not config:
        print(f"[FAIL] No brand_config at {args.config}")
        sys.exit(1)

    result = audit(config)

    if args.json:
        import json

        # Don't include references in JSON unless verbose
        if not args.verbose:
            result.pop("references", None)
        print(json.dumps(result, indent=2))
    else:
        print(f"[AUDIT] Brand Audit: {result['brand']}")
        print(f"   Overall: {result['overall_score']:.3f} -- {result['rating']}")
        print()
        for dim, info in result["dimensions"].items():
            w = WEIGHTS[dim]
            emoji = "[OK]" if info["score"] >= 0.85 else ("[WARN]" if info["score"] >= 0.5 else "[FAIL]")
            print(f"  {emoji} {dim} (x{w}): {info['score']:.2f}")
            if args.verbose and info["issues"]:
                for issue in info["issues"]:
                    print(f"     -> {issue}")

        refs = result.get("references", {})
        if refs:
            print(f"\n  [REF] {len(refs)} files reference {{{{BRAND_*}}}} variables")


if __name__ == "__main__":
    main()
