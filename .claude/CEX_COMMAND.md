# /cex -- CEX Entry Point

When the user types `/cex` or a session starts without context, run this protocol.

## 1. SCAN (10s)

Read the real repo state:

```bash
# Builders ready
ls archetypes/builders/ | grep -v "^_"

# Fill rate per nucleus
for n in N0*; do
  filled=$(find "$n" -name "*.md" ! -name "README.md" ! -name "NUCLEUS.md" 2>/dev/null | wc -l)
  total=$(find "$n" -type d -name "examples" | wc -l)
  echo "$n: $filled/$total"
done

# Root examples
for lp in P{01..12}_*; do
  echo "$lp: $(find "$lp/examples" -name "*.md" | wc -l) examples"
done

# Last commit
git log --oneline -5
```

## 2. REPORT (dashboard)

Present to the user:

```
CEX STATUS -- {date}
===================================
ARCHITECTURE
  Nuclei:     8 (N00 archetype + N01-N07 operational)
  Pillars:    12 (P01-P12)
  Kinds:      257
  Schemas:    12/12

BUILDERS (archetypes/builders/)
  Ready:      259
  ISOs:       3,381 (13 per builder)
  Meta:       builder-builder [OK]

CONTENT (N01..N07 fill rate)
  N01 intelligence:  {X}/{Y}
  N02 marketing:     {X}/{Y}
  N03 engineering:   {X}/{Y}
  N04 knowledge:     {X}/{Y}
  N05 operations:    {X}/{Y}
  N06 commercial:    {X}/{Y}
  N07 admin:         {X}/{Y}

ROOT EXAMPLES (P01..P12)
  Total: {sum} across 12 pillars

LAST COMMIT: {hash} {msg}
===================================
```

## 3. REFERENCE DOCS

Always point the user to these before starting work:

| Doc | Path | What |
|-----|------|------|
| INDEX | `INDEX.md` | Navigation map |
| Whitepaper | `_docs/WHITEPAPER_CEX.md` | Human-readable vision |
| Architecture | `_docs/ARCHITECTURE.md` | Inviolable structure (rules) |
| CODEX | `archetypes/CODEX.md` | Meta-construction bible |
| Mandamentos | `archetypes/MANDAMENTOS.md` | 10 immutable laws |
| Taxonomy | `archetypes/TAXONOMY_LAYERS.yaml` | Kinds registry |
| Variance | `archetypes/VARIANCE_ANALYSIS.md` | Universal vs specific files |
| Wave Plan | `archetypes/PHASE3_WAVE_PLAN.md` | Wave execution plan |
| Builder-Builder | `archetypes/builders/_builder-builder/README.md` | How to generate new builders |

## 4. ASK

Ask the user:

> What do you want to do?
>
> 1. **Build artifacts** (run `/build` or `/mission`)
> 2. **Fill content** in a nucleus (N01..N07)
> 3. **Review/audit** what exists (`/cex-doctor`)
> 4. **Expand** architecture (new kinds, new nuclei)
> 5. **Other** -- describe

## 5. INVIOLABLE RULES (always active)

- Path = address: `N{XX}/P{NN}/{kind}/` -- never create outside
- Dual output: `.md` + `compiled/.yaml` for artifacts
- Schema inheritance: nucleus inherits from root, never removes
- Density >= 0.8
- Quality >= 8.0 (published), >= 7.0 (experimental)
- Builder builds, human reviews, peer-reviewed quality
- CEX = product (diamond). Brand configs = workshop (infra).
