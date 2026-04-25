---
id: p01_kc_plugin_marketplace
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Claude Plugin Marketplace — .claude-plugin/ Distribution Structure"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: plugin_distribution
quality: 9.1
tags: [claude-plugin, marketplace, distribution, plugin-json, skill-packaging]
tldr: ".claude-plugin/ with marketplace.json (registry) and plugin.json (manifest) defines skill distribution via Claude Code Marketplace"
when_to_use: "Package skills for public distribution or install third-party plugins via Claude Code"
keywords: [claude-plugin, marketplace-json, plugin-json, skill-distribution]
long_tails:
  - "How to publish skills on the Claude Code Marketplace"
  - "What is the directory structure for distributing Claude plugins"
axioms:
  - "ALWAYS sync version between marketplace.json and plugin.json"
  - "NEVER omit keywords in plugin.json (hurts discoverability)"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://github.com/kepano/obsidian-skills"
related:
  - bld_collaboration_plugin
  - bld_architecture_plugin
  - plugin-builder
  - bld_tools_plugin
  - bld_memory_plugin
  - p01_kc_plugin
  - p11_qg_plugin
  - bld_config_plugin
  - bld_schema_plugin
  - bld_collaboration_marketplace_app_manifest
---

## Summary

The `.claude-plugin/` directory at the repository root defines metadata for skill distribution via Claude Code Marketplace.
Two complementary JSON files: `marketplace.json` (registry entry for discovery) and `plugin.json` (manifest for installation).
A single repo can contain multiple plugins via the `plugins[]` array.
Installation: `/plugin marketplace add {owner}/{repo}` followed by `/plugin install {name}@{repo}`.

## Spec

| File | Field | Type | Description |
|------|-------|------|-------------|
| marketplace.json | name | string | Repo slug, kebab-case |
| marketplace.json | owner.name | string | Author name |
| marketplace.json | owner.url | string | Author URL (optional) |
| marketplace.json | plugins[] | array | Plugins in this repo |
| marketplace.json | plugins[].name | string | Ref for install |
| marketplace.json | plugins[].source | string | Path in repo ("./" = root) |
| marketplace.json | plugins[].version | semver | Sync with plugin.json |
| plugin.json | name | string | Must match plugins[].name |
| plugin.json | description | string | Shown in `/plugin info` |
| plugin.json | keywords | string[] | Marketplace search |
| plugin.json | repository | url | GitHub repo URL |
| plugin.json | license | string | SPDX identifier (e.g. MIT) |

Synchronized semver versioning: patch (1.0.1->1.0.2) for skill fixes, minor (1.0->1.1) for new skills, major (1.x->2.0) for breaking structural changes. Both files must have the same version.

## Patterns

| Trigger | Action |
|---------|--------|
| Distribute skills externally | Create .claude-plugin/ with both JSONs |
| Repo with multiple skill sets | One entry per set in the plugins[] array |
| Update plugin version | Increment in BOTH files simultaneously |
| Maximize discoverability | Descriptive and specific keywords in plugin.json |
| Consume third-party plugin | `/plugin marketplace add` + `/plugin install` |
| Internal skills migrating to public | Add .claude-plugin/ without changing structure |

## Code

<!-- lang: json | purpose: complete .claude-plugin/ structure -->
```bash
# Complete structure of a distributable plugin
repo-root/
  .claude-plugin/
    marketplace.json      # Registry entry (discovery)
    plugin.json           # Plugin manifest (install metadata)
  skills/
    my-skill/
      SKILL.md            # Skill definition (mandatory frontmatter)
      references/
        *.md
  README.md
  LICENSE
```

```json
{
  "name": "my-skills",
  "owner": {"name": "Author", "url": "https://example.com"},
  "plugins": [{
    "name": "toolkit",
    "source": "./",
    "description": "Productivity skills for Claude Code",
    "version": "1.2.0"
  }]
}
```

```bash
# Installation
/plugin marketplace add author/my-skills
/plugin install toolkit@my-skills
# Format: {plugin.json:name}@{marketplace.json:name}
```

## Anti-Patterns

- Version mismatch between marketplace.json and plugin.json (install breaks)
- Omitting keywords (plugin invisible in marketplace search)
- plugin.json without license (blocks enterprise/corporate adoption)
- Plugin name different between the two files (invalid reference)
- Source path pointing to nonexistent directory in the repo

## References

- source: https://github.com/kepano/obsidian-skills
- source: https://docs.anthropic.com/en/docs/claude-code
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_plugin]] | downstream | 0.47 |
| [[bld_architecture_plugin]] | downstream | 0.43 |
| [[plugin-builder]] | downstream | 0.42 |
| [[bld_tools_plugin]] | downstream | 0.42 |
| [[bld_memory_plugin]] | downstream | 0.41 |
| [[p01_kc_plugin]] | sibling | 0.41 |
| [[p11_qg_plugin]] | downstream | 0.40 |
| [[bld_config_plugin]] | downstream | 0.37 |
| [[bld_schema_plugin]] | downstream | 0.36 |
| [[bld_collaboration_marketplace_app_manifest]] | downstream | 0.34 |
