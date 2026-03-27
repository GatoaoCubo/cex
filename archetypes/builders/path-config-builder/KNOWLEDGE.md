---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for path_config production
sources: XDG Base Directory, filesystem conventions, platform standards
---

# Domain Knowledge: path_config

## Foundational Concept
A path_config artifact defines the FILESYSTEM PATH CONTRACT for a system scope. It catalogs
every directory and file path needed: name, type (dir/file), platform support, default value,
whether required, and resolution strategy. Path configs follow the XDG Base Directory
Specification and platform-specific conventions — paths that vary between platforms or
deployments should be configurable, not hardcoded.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| XDG Base Directory Spec | Standard dirs: DATA, CONFIG, CACHE, STATE, RUNTIME | path_config maps to XDG categories |
| Windows Known Folders | AppData, ProgramData, Temp | path_config covers Windows-specific paths |
| Python pathlib | Cross-platform path manipulation | path_config defines paths; pathlib resolves them |
| Docker volumes | Mount points for persistent data | path_config maps to volume mount specs |

## Key Patterns
- Platform normalization: define with forward slashes, resolve per-platform at runtime
- Directory hierarchy: base_dir -> {data, config, cache, logs, temp} (tree structure)
- Expandable vars: {{HOME}}, {{APPDATA}}, {{USER}} resolved at runtime
- Required vs optional: required paths block startup if missing; optional created on demand
- Path types: dir (directory), file (specific file), glob (pattern match)
- Relative vs absolute: prefer relative to base_dir; absolute only for system-level paths

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT path_config |
|------|------------|--------------------------|
| env_config | System environment variables | env_config is all variables; path_config is filesystem only |
| permission | Access control rules (read/write/execute) | Permission controls WHO can access; path defines WHERE |
| feature_flag | On/off toggle with rollout | Feature flag is logic; path is location |
| runtime_rule | Timeouts, retries, limits | Runtime rule is behavior; path is filesystem structure |
| boot_config | Per-provider startup config | Boot config is provider-specific; path is generic |

## References
- XDG Base Directory Specification (specifications.freedesktop.org)
- Python pathlib documentation
- Windows Known Folder IDs (MSDN)
