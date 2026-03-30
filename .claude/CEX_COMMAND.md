# /cex — Ponto de Entrada do CEX

Quando o usuario digitar `/cex` ou quando esta session iniciar sem contexto,
execute este protocolo:

## 1. SCAN (10s)

Leia o estado real do repo:

```bash
cd C:/Users/PC/Documents/GitHub/cex

# Builders prontos
ls archetypes/builders/ | grep -v "^_"

# Fill rate dos nucleos
for n in N0*; do
  filled=$(find "$n" -name "*.md" ! -name "README.md" ! -name "NUCLEUS.md" 2>/dev/null | wc -l)
  total=$(find "$n" -type d -name "examples" | wc -l)
  echo "$n: $filled/$total"
done

# Root examples
for lp in P{01..12}_*; do
  echo "$lp: $(find "$lp/examples" -name "*.md" | wc -l) examples"
done

# Ultimo commit
git log --oneline -5
```

## 2. REPORT (dashboard)

Apresente ao usuario:

```
CEX STATUS — {data}
═══════════════════════════════════
MOLDE (Architecture v2.0)
  Nucleos:    7/7  ✅
  LPs:        84/84 ✅
  Kind dirs:  546/546 ✅
  Schemas:    84/84 ✅

BUILDERS (archetypes/builders/)
  Prontos:    {N}/78
  Pendentes:  {78-N}
  Meta:       builder-builder ✅

CONTEUDO (N01..N07 fill rate)
  N01 intelligence:  {X}/{Y}
  N02 marketing:     {X}/{Y}
  N03 engineering:   {X}/{Y}
  N04 knowledge:     {X}/{Y}
  N05 operations:    {X}/{Y}
  N06 commercial:    {X}/{Y}
  N07 admin:         {X}/{Y}

ROOT EXAMPLES (P01..P12)
  Total: {sum} across 12 pillars

ULTIMO COMMIT: {hash} {msg}
═══════════════════════════════════
```

## 3. DOCS DE REFERENCIA

Sempre aponte pro usuario antes de qualquer trabalho:

| Doc | Path | O que |
|-----|------|-------|
| INDEX | `INDEX.md` | Navigation map |
| Whitepaper | `_docs/WHITEPAPER_CEX.md` | Visao humana do CEX |
| Architecture | `_docs/ARCHITECTURE.md` | Molde inviolavel (regras) |
| CODEX | `archetypes/CODEX.md` | Biblia de meta-construcao |
| Mandamentos | `archetypes/MANDAMENTOS.md` | 10 leis |
| Taxonomy | `archetypes/TAXONOMY_LAYERS.yaml` | 78 kinds em 5 camadas |
| Variance | `archetypes/VARIANCE_ANALYSIS.md` | Que files sao universais vs especificos |
| Wave Plan | `archetypes/PHASE3_WAVE_PLAN.md` | Plano de 22 waves |
| Builder-Builder | `archetypes/builders/_builder-builder/README.md` | Como gerar novos builders |

## 4. ASK

Pergunte ao usuario:

> O que voce quer fazer?
>
> 1. **Construir builders** (Phase 3 — 74 faltam)
> 2. **Preencher conteudo** em um nucleo (N01..N07)
> 3. **Revisar/auditar** o que existe
> 4. **Expandir** a arquitetura (novos types, novos nucleos)
> 5. **Outro** — descreva

## 5. REGRAS INVIOLAVEIS (sempre ativas)

- Path = endereco: `N{XX}/P{NN}/{type}/` — nunca criar fora
- Dual output: `.md` + `compiled/.yaml` pra artefatos
- Schema inheritance: nucleo herda do root, nunca remove
- Density >= 0.8
- Quality >= 7.0
- Builder constroi, humano revisa
- CEX = diamante (produto). organization-core = workshop (infra)
