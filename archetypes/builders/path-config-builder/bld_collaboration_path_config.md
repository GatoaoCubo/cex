---
kind: collaboration
id: bld_collaboration_path_config
pillar: P09
llm_function: COLLABORATE
purpose: How path-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: path-config-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what filesystem paths does this scope need, on which platforms, with what defaults?"
I define directories, file locations, path resolution rules, and platform-specific separators. I do NOT handle generic environment variables (env-config-builder), access control (permission-builder), or on/off toggles (feature-flag-builder).

## Crew Compositions

### Crew: "System Configuration Bootstrap"
```
  1. path-config-builder  -> "defines all filesystem paths the system needs"
  2. env-config-builder   -> "defines environment variables that reference those paths"
  3. permission-builder   -> "defines who can read/write each path"
```

### Crew: "Plugin Deployment Setup"
```
  1. plugin-builder       -> "defines the plugin and its required directories"
  2. path-config-builder  -> "specifies install path, config path, log path per platform"
  3. boot-config-builder  -> "wires path config into system startup sequence"
```

### Crew: "Data Pipeline Setup"
```
  1. path-config-builder  -> "input/output/staging/cache directory structure"
  2. env-config-builder   -> "env vars for pipeline configuration"
  3. runtime-rule-builder -> "timeout and retry rules for pipeline steps"
```

## Handoff Protocol

### I Receive
- seeds: scope name, target platforms (Windows/Linux/Mac), directory types needed (workspace/logs/config/cache)
- optional: existing directory structure to document, relative vs absolute preference

### I Produce
- path_config artifact (Markdown, max 4KB)
- committed to: `cex/P09/examples/p09_path_{scope}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- plugin-builder: declares what directories a plugin requires before I specify them

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| env-config-builder | references my paths as values for environment variables |
| permission-builder | applies access rules to paths I defined |
| boot-config-builder | uses my paths during system startup sequence |
| daemon-builder | needs log_dir, pid file, and working directory paths |
