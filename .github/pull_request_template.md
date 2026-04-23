## Summary

<!-- 1-3 bullet points: what changed and why -->

## Artifact Changes

| Action | Path | Kind |
|--------|------|------|
| CREATE/EDIT | `path/to/file.md` | `kind_name` |

## Checklist

- [ ] `python _tools/cex_doctor.py` returns 0 FAIL
- [ ] All new artifacts have `quality: null` in frontmatter
- [ ] No non-ASCII in code files (`.py`, `.ps1`, `.sh`)
- [ ] Builder has at least 4 ISOs (bld_knowledge, bld_model, bld_prompt, bld_eval)
- [ ] No secrets, API keys, or `.env` content in any file

## Test Plan

<!-- How did you verify this works? -->

---
Generated with [CEXAI](https://github.com/GatoaoCubo/cex)
