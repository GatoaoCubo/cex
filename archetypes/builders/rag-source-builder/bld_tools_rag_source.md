---
kind: tools
id: bld_tools_rag_source
pillar: P04
llm_function: CALL
version: 1.0.0
---

# Tools: rag-source-builder
## Primary Tools
### brain_query
**Purpose**: Check for existing rag_sources before creating a new one (duplicate prevention).
**When**: Phase 1 DISCOVER, before composing.
**Call**: `brain_query("rag_source {domain} {url_domain_keyword}")`
**Interpret**: If results contain a rag_source with same URL or near-identical domain+source, surface it to user before proceeding.
### validate_artifact.py [PLANNED]
**Purpose**: Automated gate checking against QUALITY_GATES.md.
**When**: Phase 3 VALIDATE.
**Call**: `python validate_artifact.py --kind rag_source --file p01_rs_{slug}.md`
**Status**: PLANNED — not yet implemented. Use manual validation against QUALITY_GATES.md in the interim.
## Data Sources
| Source | Path | Use |
|--------|------|-----|
| Kind schema | P01_knowledge/_schema.yaml | Required fields, constraints, naming rules |
| Existing rag_sources | P01_knowledge/examples/p01_rs_*.md | Duplicate check, style reference |
| CEX domain taxonomy | records/domains/ [PLANNED] | Validate domain value |
## Interim Validation (until validate_artifact.py ships)
1. Parse frontmatter manually — confirm all required fields present
2. Check id pattern with regex: `^p01_rs_[a-z][a-z0-9_]+$`
3. Count body bytes: `wc -c p01_rs_{slug}.md` (must be <= 1024)
4. Verify URL format: starts with https:// or http://
5. Confirm quality == null (not string "null")
## URL Validation Heuristic
Valid URL checklist:
- Starts with https:// (preferred) or http://
- Contains at least one dot in domain
- No spaces, no angle brackets
- No localhost or 127.0.0.1 (external sources only)
