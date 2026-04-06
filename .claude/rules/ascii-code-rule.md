# Rule: ASCII-Only Executable Code

> Added 2026-04-06 after 6 boot scripts + 493 tool lines failed on Windows cp1252.

## The Rule

**All executable code MUST be ASCII-only (0x00-0x7F).**

Applies to: `.py`, `.ps1`, `.sh`, `.cmd`, `.bat`

## Why

1. Python 3 source reads UTF-8 fine, but `print()` goes to Windows terminal
2. Windows terminal defaults to cp1252 (NOT UTF-8)
3. Any non-ASCII in print/log output = `UnicodeEncodeError` crash
4. PowerShell without BOM reads scripts as ANSI = parse failure on multi-byte chars
5. Silent failures: code "works" in VS Code (UTF-8) but crashes in production terminal

## Replacement Table

| Non-ASCII | ASCII Replacement |
|-----------|-------------------|
| `--` (em-dash U+2014) | `--` |
| `-` (en-dash U+2013) | `-` |
| Smart quotes `""''` | Straight quotes `"` `'` |
| Box drawing `━│┌┐└┘` | `= \| + + + +` |
| Arrows `→←↑↓` | `->` `<-` `^` `v` |
| Checkmarks `✓✗` | `[OK]` `[FAIL]` |
| Emoji `🔴🟢📡⚔` | `[!!]` `[OK]` `[i]` `[X]` |
| PT-BR accents in code | Unaccented: `missao`, `visao`, `nao`, `acao`, `voce`, `codigo` |

## Where Non-ASCII IS Allowed

- `.md` content files (KCs, handoffs, docs) -- humans read these
- `.yaml` data values (brand config, descriptions) -- data, not code
- User-facing templates with `{{BRAND_*}}` placeholders

## Enforcement

- `python _tools/cex_sanitize.py --check --scope _tools/` in pre-commit hook
- `cex_hooks.py` validates: encoding + PS parse + YAML schema
- CI gate rejects any PR adding non-ASCII to executable files

## For LLM Builders

When generating `.py` or `.ps1` code:
- Never use emoji in print statements
- Never use em-dash in comments or strings
- Never use accented characters in variable names, comments, or output strings
- Use `ascii_safe()` wrapper if output string might contain user data
