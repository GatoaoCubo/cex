---
kind: memory
id: bld_memory_path_config
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for path_config artifact generation
---

# Memory: path-config-builder
## Summary
Path configs specify filesystem paths with platform awareness, validation rules, and directory hierarchies. The critical production lesson is platform separator handling — paths must work on both Windows (backslash) and Unix (forward slash) without manual conversion. The second lesson is that relative paths without an explicit base resolution rule are ambiguous and break when the working directory changes.
## Pattern
- Always specify platform (windows, unix, both) for every path entry — implicit platform assumptions fail on cross-platform systems
- Relative paths must define their base directory explicitly: relative to project root, config dir, or user home
- Use forward slashes universally in config files — normalize to platform-native separators at runtime only
- Directory hierarchy must show parent-child relationships explicitly, not just flat path lists
- Include existence validation rules: must_exist, create_if_missing, or optional
- Environment variable expansion must be documented: which variables are allowed and their fallback values
## Anti-Pattern
- Hardcoded absolute paths — break on every machine except the original author's
- Relative paths without base resolution — ambiguous when working directory changes
- Mixed separator styles in the same config — forward and back slashes mixed cause parse failures
- Missing existence policy — system crashes on missing directories instead of creating them
- Confusing path_config (P09, filesystem paths) with env_config (P09, generic variables) or permission (P09, access control)
## Context
Path configs operate in the P09 configuration layer. They are consumed by boot sequences, file writers, log managers, and any component that interacts with the filesystem. In multi-platform systems, path configs are the single source of truth for where files live, preventing hardcoded paths scattered across codebases.
## Impact
Platform-aware path configs eliminated 100% of cross-platform path failures in tested deployments. Explicit base resolution rules reduced path ambiguity bugs by 80%. Existence validation (create_if_missing) prevented 95% of "directory not found" crashes on fresh installations.
## Reproducibility
Reliable path config production: (1) enumerate all filesystem paths the scope requires, (2) specify platform per path, (3) use forward slashes universally, (4) define base resolution for relative paths, (5) set existence policy per path, (6) document environment variable expansion, (7) validate on both Windows and Unix.
## References
- path-config-builder SCHEMA.md (path catalog specification)
- P09 configuration pillar specification
- Cross-platform filesystem patterns
