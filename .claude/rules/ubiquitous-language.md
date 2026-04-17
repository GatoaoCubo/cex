# Ubiquitous Language Protocol

**Mandatory for ALL nuclei (N01-N07). Every artifact. Every output. No exceptions.**

This rule governs HOW nuclei communicate -- with each other, with tools, and in artifacts.
Just as 8F governs HOW nuclei think, Ubiquitous Language governs HOW nuclei speak.

## The Problem This Solves

Without a shared canonical vocabulary:
- Nuclei invent synonyms for the same concept (semantic drift)
- Artifacts become human-readable but machine-ambiguous
- Cross-nucleus references break (N01 says "research card", N04 says "knowledge_card")
- The 257-kind taxonomy erodes into free-form description
- LLM-to-LLM communication accumulates translation overhead

**CEX is infrastructure for LLMs, not documentation for humans.**
Every term in every artifact must map to a canonical vocabulary entry.
Human-readable analogies live in the metaphor dictionary. Artifacts use industry terms.

## The Rule (3 layers)

### Layer 1: Controlled Vocabulary per Nucleus

Every nucleus maintains a controlled vocabulary KC:
  `N0X_{domain}/P01_knowledge/kc_{domain}_vocabulary.md`

This KC maps:
1. CEX canonical terms -> industry standard definitions
2. Domain-specific terms -> how they apply in this nucleus's context
3. Anti-patterns: terms to NEVER use (and what to use instead)

This is not documentation -- it is the nucleus's LANGUAGE MODEL.
Before generating any artifact, the nucleus loads this KC (F3 INJECT).

### Layer 2: F2b SPEAK (new 8F sub-step)

Insert after F2 BECOME, before F3 INJECT:

```
F2b SPEAK
  Load: N0X_{domain}/P01_knowledge/kc_{domain}_vocabulary.md
  Load: _docs/specs/spec_metaphor_dictionary.md (Industry term column)
  Enforce: ALL output from F3-F8 uses controlled vocabulary only
  Output: "F2b: Vocabulary loaded ({N} terms). Drift prevention: active."
```

If the vocabulary KC does not exist yet: create it as the FIRST artifact of the session.
A nucleus that speaks without a vocabulary is generating untyped output.

### Layer 3: Artifact Output Enforcement

Every artifact must satisfy:
- Field names in frontmatter: snake_case, from the 257-kind taxonomy
- Body headings: match pillar domain vocabulary (P01=knowledge terms, P06=schema terms, etc.)
- No invented synonyms: if "knowledge_card" exists as a kind, NEVER write "research card" or "intel doc"
- Cross-references: always use canonical path + kind name (not colloquial description)

## The Vocabulary KC Structure

```markdown
---
id: kc_{domain}_vocabulary
kind: knowledge_card
pillar: P01
nucleus: N0X
domain: {domain}
type: controlled_vocabulary
---

## Canonical Terms

| Term | Definition | Domain Application | Anti-pattern |
|------|-----------|-------------------|-------------|
| {term} | {industry definition} | {how N0X uses it} | {what NOT to say} |

## Cross-Nucleus Shared Terms (DO NOT REDEFINE)

These terms are defined in N00_genesis and must not be redefined in nucleus KCs:
- 8F pipeline (F1-F8): canonical reasoning protocol
- kind: atomic artifact type from the 257-kind taxonomy
- pillar: P01-P12 domain grouping
- nucleus: N00-N07 operational agent
- quality_gate: F7 GOVERN validation
- signal: F8 COLLABORATE completion notification

## Domain-Specific Extensions

Terms that N0X introduces (not in N00_genesis):
| New Term | Definition | Maps to Industry Standard |
|----------|-----------|--------------------------|
```

## Automatic Transmutation (User-Transparent Layer)

The user NEVER needs to know "ubiquitous language" or CEX vocabulary.
The system transmutes user tokens into canonical terms automatically via:

```
User input (any language, any metaphor)
    |
    v
cex_intent_resolver.py           -- Python-first, 0 tokens, maps phrase -> {kind, pillar, nucleus, verb}
    |
    v
p03_pc_cex_universal.md          -- 257 kinds x PT+EN bilingual pattern table (the prompt compiler)
N00_genesis/P03_prompt/layers/   -- loaded by EVERY nucleus at F1 CONSTRAIN
    |
    v
Canonical {kind, pillar, nucleus, verb} tuple
    |
    v
kc_{domain}_vocabulary.md        -- nucleus-specific overlay: domain extensions + anti-patterns
    |
    v
Artifact generated in ubiquitous language (the user sees the output, not the vocabulary)
```

This is the correct architecture:
- Layer 0: `cex_intent_resolver.py` -- deterministic, token-free pre-filter
- Layer 1: `p03_pc_cex_universal.md` -- universal vocabulary (257 kinds, N00_genesis)
- Layer 2: `kc_{domain}_vocabulary.md` -- per-nucleus domain overlay

The prompt_compiler (kind=`prompt_compiler`) IS the ubiquitous language enforcement mechanism.
It should be loaded at F1 CONSTRAIN by EVERY nucleus, not just N07.
Every nucleus that does NOT load it is operating without vocabulary enforcement.

**Hydration rule:** each nucleus's boot config and agent_card must explicitly reference:
  `N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md`
as a mandatory context source alongside their domain vocabulary KC.

## Source of Truth Hierarchy

When a term conflict occurs:
1. `p03_pc_cex_universal.md` (prompt_compiler kind) -- HIGHEST authority (257 kinds, PT+EN)
2. `spec_metaphor_dictionary.md` (Industry term column) -- human-readable reference
3. `N00_genesis/P01_knowledge/kc_*.md` -- canonical definitions
4. `N0X_{domain}/P01_knowledge/kc_{domain}_vocabulary.md` -- domain extensions
5. 257-kind taxonomy in `.cex/kinds_meta.json` -- kind names

If a term does not appear in any of the above: it is NOT canonical.
Either find the correct term or add it to the prompt_compiler first.

## LLM-to-LLM Communication Principle

When N07 writes a handoff to N03, N03 reads it WITHOUT human context.
Every term must be self-defining via the controlled vocabulary.

BAD handoff language:
  "build a research card for the competitor scan"

GOOD handoff language:
  "produce kind=knowledge_card, pillar=P01, domain=competitive-intelligence,
   nucleus=N01, triggering intent=competitor_scan"

The good version is unambiguous to ANY LLM, ANY runtime (Claude/Codex/Gemini/Ollama).
This is the interoperability contract.

## Enforcement

1. F2b SPEAK (mandatory load before any artifact generation)
2. F7 GOVERN validates: no undeclared terms in artifact body/frontmatter
3. Pre-commit hook: `cex_hooks.py` checks for non-canonical kind/pillar references
4. Doctor check: `cex_doctor.py --vocab` verifies vocabulary KC exists per nucleus

## Connection to 8F

```
F1 CONSTRAIN  -- resolve kind/pillar from canonical taxonomy (vocabulary layer: kinds_meta.json)
F2 BECOME     -- load builder ISOs (builder vocabulary: 13 ISOs per kind)
F2b SPEAK     -- load controlled vocabulary KC (domain language layer: THIS RULE)
F3 INJECT     -- assemble context using canonical references
F4 REASON     -- plan using industry terms (no invented metaphors)
F5 CALL       -- call tools by canonical name (not alias)
F6 PRODUCE    -- generate artifact in ubiquitous language
F7 GOVERN     -- validate: vocabulary compliance + quality gates
F8 COLLABORATE-- signal using canonical nucleus/kind/score format
```

F2b SPEAK is the LANGUAGE LAYER between identity (F2) and knowledge injection (F3).
It ensures that all context assembled in F3 is interpreted through the correct vocabulary.

## Properties

| Property | Value |
|----------|-------|
| Kind | rule |
| Pillar | cross-cutting |
| Domain | LLM-to-LLM interoperability |
| Applies to | ALL nuclei N01-N07 |
| Source | Eric Evans, DDD 2003 (ubiquitous language) |
| Industry equivalents | shared ontology, canonical data model, agent communication language |
| Quality target | 100% (zero vocabulary drift tolerance) |
