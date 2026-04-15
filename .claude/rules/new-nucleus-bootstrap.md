# New Nucleus Bootstrap

Template for bootstrapping any Nxx nucleus beyond N01-N07.
Existing nuclei **bypass** permissions (trusted); new nuclei start **scoped**
and earn trust over time.

## Checklist (9 files per new nucleus)

1. **Rule file**: `.claude/rules/n{XX}-{domain}.md` -- identity, routing, boot rules
2. **Agent card**: `N{XX}_{domain}/architecture/agent_card_n{XX}.md`
3. **System prompt**: `N{XX}_{domain}/prompts/system_prompt_{domain}.md`
4. **Agent def**: `N{XX}_{domain}/agents/agent_{domain}.md`
5. **Boot script (claude)**: `boot/n{XX}.ps1`
6. **Boot script (codex)**: `boot/n{XX}_codex.ps1`
7. **Boot script (gemini)**: `boot/n{XX}_gemini.ps1`
8. **Boot script (ollama)**: `boot/n{XX}_ollama.ps1`
9. **Permissions overlay**: `.claude/nucleus-settings/n{XX}.json` (from `_template.json`)

## Multi-runtime rule

Every feature MUST cover 4 runtimes:
- **claude**: native (skills + hooks + slash commands).
- **codex**: same skills mirrored to `.cex/skills/` (YAML + body, runtime-agnostic).
- **gemini**: same skills mirrored + MCP routing via `.mcp.json`.
- **ollama**: same skills + local model via `boot/n{XX}_ollama.ps1`.

See `_docs/specs/spec_multi_runtime_features.md` for the compatibility matrix.

## Permissions pattern

`.claude/nucleus-settings/_template.json` defines the **minimum viable**
allowlist. Copy it to `n{XX}.json`, add nucleus-specific bash patterns, done.

Existing nuclei (N01-N07) have no explicit allowlist -- they trust the global
`settings.json` which is permissive for trusted internals. New nuclei SHOULD
start restricted.

## Boot wrapper protocol (--worktree flag)

All 4 runtime wrappers (`n{XX}.ps1`, `n{XX}_codex.ps1`, `n{XX}_gemini.ps1`,
`n{XX}_ollama.ps1`) MUST accept:

```
-WorktreeDir <path>   # run nucleus inside isolated git worktree
-Task <path>          # read handoff from file (never from argv)
-AutoAccept <0|1>     # forward CEX_AUTO_ACCEPT env
```

See `boot/_shared/worktree_helpers.ps1` for the reusable functions.

## Signal contract

Every nucleus MUST emit on completion:

```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n{XX}', 'complete', 9.0)"
```

The `Stop` hook in `.claude/settings.json` does this automatically when
`CEX_NUCLEUS=n{XX}` is exported.

## Properties

| Property | Value |
|----------|-------|
| Kind | `rule` |
| Pillar | cross-cutting |
| Domain | nucleus bootstrap |
| Pipeline | 8F (F1-F8) |
| Quality target | 9.0+ |
| Density target | 0.85+ |
