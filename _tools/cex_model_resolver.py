"""
cex_model_resolver.py -- Runtime model resolution from nucleus_models.yaml.

Provides a single source of truth for model strings across all Python tools.
Replaces hardcoded model references (47 instances across 23 files).

Usage:
    from _tools.cex_model_resolver import resolve_model, get_preflight_model
    cfg = resolve_model("n03")
    # cfg = {"cli": "claude", "model": "claude-opus-4-6", "context": 1000000, ...}

    haiku = get_preflight_model("cloud")
    # haiku = {"cli": "claude", "model": "claude-haiku-4-5-20251001", ...}

    tool_model = resolve_model_for_tool("cex_intent", task_tier="light")
    # tool_model = {"cli": "claude", "model": "claude-haiku-4-5-20251001", ...}

Design:
    - Reads .cex/config/nucleus_models.yaml ONCE per process (cached).
    - Auto-detects CEX_ROOT from env var or git rev-parse.
    - Graceful fallback on any error -- never crashes.
    - ASCII-only per .claude/rules/ascii-code-rule.md.
"""

import os
import subprocess
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# Module-level cache (one YAML parse per process)
# ---------------------------------------------------------------------------

_CACHE = {
    "config": None,
    "cex_root": None,
    "loaded": False,
}

# Default fallback when YAML is missing or unparseable
_DEFAULT_NUCLEUS = {
    "cli": "claude",
    "model": "claude-opus-4-6",
    "context": 1000000,
    "flags": "",
    "mcps": "",
    "settings": "",
    "fallback_chain": [],
}

_DEFAULT_PREFLIGHT_LOCAL = {
    "cli": "ollama",
    "model": "qwen3:14b",
    "base_url": "http://localhost:11434/v1",
    "timeout_seconds": 30,
}

_DEFAULT_PREFLIGHT_CLOUD = {
    "cli": "claude",
    "model": "claude-haiku-4-5-20251001",
}

_DEFAULT_OLLAMA = {
    "base_url": "http://localhost:11434/v1",
    "embed_url": "http://localhost:11434/api/embed",
    "models": {
        "primary": "gemma4:26b",
        "heavy": "qwen3:14b",
        "light": "qwen3:8b",
    },
}


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _find_cex_root(cex_root=None):
    """Resolve CEX repository root directory.

    Priority:
    1. Explicit cex_root argument
    2. CEX_ROOT environment variable
    3. git rev-parse --show-toplevel
    4. Walk up from this file's location looking for .cex/ directory
    """
    if cex_root:
        return str(Path(cex_root).resolve())

    env_root = os.environ.get("CEX_ROOT")
    if env_root and os.path.isdir(env_root):
        return str(Path(env_root).resolve())

    # Try git rev-parse
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=5,
            cwd=os.path.dirname(os.path.abspath(__file__)),
        )
        if result.returncode == 0 and result.stdout.strip():
            return str(Path(result.stdout.strip()).resolve())
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        pass

    # Walk up from this file looking for .cex/ directory
    current = Path(__file__).resolve().parent
    for _ in range(10):
        if (current / ".cex").is_dir():
            return str(current)
        parent = current.parent
        if parent == current:
            break
        current = parent

    return ""


def _load_yaml(cex_root=None):
    """Load nucleus_models.yaml, caching the result."""
    if _CACHE["loaded"]:
        return _CACHE["config"] or {}

    if yaml is None:
        # pyyaml not available -- return empty, functions use defaults
        _CACHE["loaded"] = True
        _CACHE["config"] = {}
        return {}

    root = _find_cex_root(cex_root)
    if not root:
        _CACHE["loaded"] = True
        _CACHE["config"] = {}
        return {}

    _CACHE["cex_root"] = root
    yaml_path = os.path.join(root, ".cex", "config", "nucleus_models.yaml")

    if not os.path.isfile(yaml_path):
        _CACHE["loaded"] = True
        _CACHE["config"] = {}
        return {}

    try:
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        _CACHE["config"] = data if isinstance(data, dict) else {}
    except Exception:
        _CACHE["config"] = {}

    _CACHE["loaded"] = True
    return _CACHE["config"] or {}


def _invalidate_cache():
    """Force re-read on next call. Useful for tests."""
    _CACHE["config"] = None
    _CACHE["cex_root"] = None
    _CACHE["loaded"] = False


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def load_nucleus_models(cex_root=None):
    """Load and return the full nucleus_models.yaml as a dict.

    Auto-detects cex_root from CEX_ROOT env var or git root.
    Caches the result for the process lifetime (module-level cache).
    Returns {} on any error (graceful fallback).
    """
    return dict(_load_yaml(cex_root))


def resolve_model(nucleus, cex_root=None):
    """Return model config for a nucleus as a dict.

    Args:
        nucleus: Nucleus identifier (e.g. "n03", "n07")
        cex_root: Optional explicit path to CEX repo root

    Returns:
        Dict with keys: cli, model, context, flags, mcps, settings, fallback_chain
        Falls back to claude-opus-4-6 / 1M context if missing.
    """
    config = _load_yaml(cex_root)
    nuc_key = nucleus.lower().strip()
    nuc_cfg = config.get(nuc_key, {})

    if not nuc_cfg or not isinstance(nuc_cfg, dict):
        return dict(_DEFAULT_NUCLEUS)

    # Check for orchestrator override via env var
    override = os.environ.get("CEX_MODEL_OVERRIDE")
    if override:
        cli = "claude"
        if override.startswith("gemini"):
            cli = "gemini"
        elif override.startswith("gpt"):
            cli = "codex"
        elif any(override.startswith(p) for p in ("llama", "qwen", "gemma", "phi")):
            cli = "ollama"
        return {
            "cli": cli,
            "model": override,
            "context": nuc_cfg.get("context", 1000000),
            "flags": nuc_cfg.get("flags", ""),
            "mcps": nuc_cfg.get("mcps", ""),
            "settings": nuc_cfg.get("settings", ""),
            "fallback_chain": nuc_cfg.get("fallback_chain", []),
        }

    return {
        "cli": nuc_cfg.get("cli", "claude"),
        "model": nuc_cfg.get("model", "claude-opus-4-6"),
        "context": nuc_cfg.get("context", 1000000),
        "flags": nuc_cfg.get("flags", ""),
        "mcps": nuc_cfg.get("mcps", ""),
        "settings": nuc_cfg.get("settings", ""),
        "fallback_chain": nuc_cfg.get("fallback_chain", []),
    }


def get_preflight_model(phase="local", cex_root=None):
    """Return model config for preflight phase.

    Args:
        phase: "local" for Ollama-based preflight, "cloud" for Haiku-based
        cex_root: Optional explicit path to CEX repo root

    Returns:
        Dict with cli, model, and phase-specific fields.
        Falls back gracefully if config missing.
    """
    config = _load_yaml(cex_root)
    preflight = config.get("preflight", {})

    if phase == "local":
        local_cfg = preflight.get("local", {})
        if not local_cfg:
            return dict(_DEFAULT_PREFLIGHT_LOCAL)
        return {
            "cli": local_cfg.get("cli", "ollama"),
            "model": local_cfg.get("model", "qwen3:14b"),
            "fallback_model": local_cfg.get("fallback_model", "qwen3:8b"),
            "base_url": local_cfg.get("base_url", "http://localhost:11434/v1"),
            "timeout_seconds": local_cfg.get("timeout_seconds", 30),
            "tasks": local_cfg.get("tasks", []),
        }

    elif phase == "cloud":
        cloud_cfg = preflight.get("cloud", {})
        if not cloud_cfg:
            return dict(_DEFAULT_PREFLIGHT_CLOUD)
        return {
            "cli": cloud_cfg.get("cli", "claude"),
            "model": cloud_cfg.get("model", "claude-haiku-4-5-20251001"),
            "tasks": cloud_cfg.get("tasks", []),
        }

    # Unknown phase -- return cloud default
    return dict(_DEFAULT_PREFLIGHT_CLOUD)


def get_ollama_config(cex_root=None):
    """Return ollama_api section from nucleus_models.yaml.

    Returns:
        Dict with keys: base_url, embed_url, models (primary/heavy/light),
        plus gpu, vram, parallel if present.
        Falls back gracefully if missing.
    """
    config = _load_yaml(cex_root)
    ollama_cfg = config.get("ollama_api", {})

    if not ollama_cfg:
        return dict(_DEFAULT_OLLAMA)

    models = ollama_cfg.get("models", {})
    return {
        "base_url": ollama_cfg.get("base_url", "http://localhost:11434/v1"),
        "embed_url": ollama_cfg.get("embed_url", "http://localhost:11434/api/embed"),
        "models": {
            "primary": models.get("primary", "gemma4:26b"),
            "heavy": models.get("heavy", "qwen3:14b"),
            "light": models.get("light", "qwen3:8b"),
        },
        "gpu": ollama_cfg.get("gpu", ""),
        "vram": ollama_cfg.get("vram", ""),
        "parallel": ollama_cfg.get("parallel", 1),
    }


def get_fallback_chain(nucleus, cex_root=None):
    """Return the ordered fallback_chain list for a nucleus.

    Args:
        nucleus: Nucleus identifier (e.g. "n03")
        cex_root: Optional explicit path to CEX repo root

    Returns:
        List of dicts, each with keys: cli, model, flags.
        Empty list if no fallback chain configured.
    """
    config = _load_yaml(cex_root)
    nuc_key = nucleus.lower().strip()
    nuc_cfg = config.get(nuc_key, {})

    if not nuc_cfg or not isinstance(nuc_cfg, dict):
        return []

    chain = nuc_cfg.get("fallback_chain", [])
    if not isinstance(chain, list):
        return []

    # Normalize entries to ensure consistent keys
    result = []
    for entry in chain:
        if isinstance(entry, dict):
            result.append({
                "cli": entry.get("cli", "claude"),
                "model": entry.get("model", ""),
                "flags": entry.get("flags", ""),
            })
    return result


def resolve_model_for_tool(tool_name, task_tier="standard", cex_root=None):
    """Resolve model config for a Python tool based on its task tier.

    This replaces hardcoded model strings in tools like cex_intent.py,
    cex_translate.py, cex_fts5_search.py, etc.

    Args:
        tool_name: Name of the calling tool (for logging/audit, not routing)
        task_tier: One of "light", "standard", "heavy"
            - "light"    -> preflight cloud model (haiku -- cheap, fast)
            - "standard" -> N03's model (engineering tier)
            - "heavy"    -> N07's model (opus tier, max reasoning)

    Returns:
        Dict with keys: cli, model, context (minimum viable fields for tool use)
    """
    if task_tier == "light":
        cfg = get_preflight_model("cloud", cex_root=cex_root)
        return {
            "cli": cfg.get("cli", "claude"),
            "model": cfg.get("model", "claude-haiku-4-5-20251001"),
            "context": 200000,
        }

    elif task_tier == "heavy":
        cfg = resolve_model("n07", cex_root=cex_root)
        return {
            "cli": cfg.get("cli", "claude"),
            "model": cfg.get("model", "claude-opus-4-6"),
            "context": cfg.get("context", 1000000),
        }

    else:  # "standard" or any unrecognized tier
        cfg = resolve_model("n03", cex_root=cex_root)
        return {
            "cli": cfg.get("cli", "claude"),
            "model": cfg.get("model", "claude-opus-4-6"),
            "context": cfg.get("context", 1000000),
        }


def get_model_string(nucleus, cex_root=None):
    """Convenience: return just the model string for a nucleus.

    Equivalent to resolve_model(nucleus)["model"] but shorter for callers
    that only need the model identifier.
    """
    return resolve_model(nucleus, cex_root=cex_root)["model"]


def get_cli(nucleus, cex_root=None):
    """Convenience: return just the CLI name for a nucleus."""
    return resolve_model(nucleus, cex_root=cex_root)["cli"]


# ---------------------------------------------------------------------------
# __main__ -- debug utility: print resolved config for all nuclei
# ---------------------------------------------------------------------------

def _print_table():
    """Print resolved model configuration for all nuclei and special sections."""
    config = load_nucleus_models()
    if not config:
        print("[WARN] Could not load nucleus_models.yaml")
        print("  Checked: CEX_ROOT env, git root, parent walk")
        print("  All functions will return defaults (claude-opus-4-6)")
        return

    nuclei = ["n01", "n02", "n03", "n04", "n05", "n06", "n07"]

    print("=" * 72)
    print("CEX Model Resolver -- Runtime Configuration")
    print("=" * 72)
    print("")

    # Nucleus table
    print("NUCLEI:")
    print("-" * 72)
    fmt = "  {:<5} | {:<8} | {:<30} | {:>9} | fallback: {}"
    print(fmt.format("NUC", "CLI", "MODEL", "CONTEXT", "CHAIN_LEN"))
    print("  " + "-" * 68)

    for nuc in nuclei:
        cfg = resolve_model(nuc)
        chain = get_fallback_chain(nuc)
        print(fmt.format(
            nuc.upper(),
            cfg["cli"],
            cfg["model"],
            cfg["context"],
            len(chain),
        ))

    print("")

    # Preflight
    print("PREFLIGHT:")
    print("-" * 72)
    local = get_preflight_model("local")
    cloud = get_preflight_model("cloud")
    print("  local:  cli={}, model={}, url={}".format(
        local.get("cli"), local.get("model"), local.get("base_url", "n/a")))
    print("  cloud:  cli={}, model={}".format(
        cloud.get("cli"), cloud.get("model")))

    print("")

    # Ollama
    print("OLLAMA API:")
    print("-" * 72)
    ollama = get_ollama_config()
    print("  base_url:  {}".format(ollama["base_url"]))
    print("  embed_url: {}".format(ollama["embed_url"]))
    print("  primary:   {}".format(ollama["models"]["primary"]))
    print("  heavy:     {}".format(ollama["models"]["heavy"]))
    print("  light:     {}".format(ollama["models"]["light"]))
    print("  parallel:  {}".format(ollama.get("parallel", 1)))

    print("")

    # Tool tier resolution
    print("TOOL TIERS (resolve_model_for_tool):")
    print("-" * 72)
    for tier in ("light", "standard", "heavy"):
        cfg = resolve_model_for_tool("__debug__", task_tier=tier)
        print("  {:<10} -> {} / {}".format(tier, cfg["cli"], cfg["model"]))

    print("")
    print("=" * 72)


if __name__ == "__main__":
    _print_table()
