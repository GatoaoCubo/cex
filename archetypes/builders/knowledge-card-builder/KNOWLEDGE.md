---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for knowledge_card production
sources: validate_kc.py v2.0 + _schema.yaml v4.0 + 63 real examples
---

# Domain Knowledge: knowledge_card

## Foundational Concept
Knowledge cards are ATOMIC SEARCHABLE FACTS — the smallest unit of knowledge
in a retrieval system. Each card answers ONE question about ONE topic.
Density > 0.80 means >80% of content is concrete data (no filler, no narrative).

## Anatomy of an Effective Knowledge Card

### Frontmatter: The Retrieval Surface
The frontmatter is NOT metadata — it IS the retrieval surface. Search engines
(BM25 keyword + FAISS vector) match against `tldr`, `tags`, `keywords`, and
`long_tails`. A card with perfect body content but poor frontmatter is invisible.

| Field | Retrieval Role | Pattern |
|-------|---------------|---------|
| tldr | Primary match signal (BM25 + embedding) | Specific data: "Execute CLI via subprocess with Pydantic, retry 3x, JSONL parse" NOT "How to use CLI" |
| tags | Faceted filtering, cluster grouping | 3-7 tags, mix domain + technique + scope |
| keywords | BM25 exact match boost | 2-5 terms the user would literally type |
| long_tails | Semantic search (embedding similarity) | Full phrases: "how to handle concurrent token refresh in multi-request scenarios" |
| when_to_use | Agent activation trigger | "When setting up monitoring for API usage" — specific context, not "when needed" |

### Body: Dense Information, Not Prose
The body delivers facts. Every line should teach something concrete.

**Density hierarchy** (most to least information per token):
1. Tables — structured comparisons, specs, mappings
2. Code blocks — algorithms, config, implementation patterns
3. Bullet lists — facts, rules, steps
4. ASCII diagrams — flows, state machines, architectures
5. Short paragraphs — only for context that tables cannot express

**Effective body sections** (from high-scoring cards):
- **Overview/Summary** — 2-3 sentences, dense context (not a repeat of tldr)
- **Classification tables** — categorize with concrete examples per row
- **Pattern descriptions** — name + when-to-use + code/config + tradeoffs
- **Anti-patterns** — what fails and WHY it fails (not just "don't do X")
- **References** — source URLs, related cards, commit hashes

### Semantic Bridge (for retrieval diversity)
A section mapping the card's concepts to equivalent terminology across
frameworks and industries. Enables cross-domain retrieval:

```markdown
## Semantic Bridge
**Also known as**: [synonyms from other frameworks]
**Keywords**: [terms users in other ecosystems would search]

| Framework | Equivalent Term |
|-----------|----------------|
| LangChain | Document / TextChunk |
| Industry  | RAG Document |
```

## Density: The Critical Quality Gate

```
density = (data_lines) / (total_non_empty_lines)
data_line = bullet, table row, code line, yaml value
non_data_line = heading, empty prose, transition sentence
Target: >= 0.80 (ideally 0.85-0.95)
```

**If density < 0.80**: The card fails regardless of other quality dimensions.
Density is the prerequisite gate — evaluate it first.

### Density killers (from real low-scoring cards)
- Transition sentences: "Let's now look at..." "In the following section..."
- Restating the title in the body: "This knowledge card covers..."
- Generic QA pairs: "Q: What is X? A: X is a knowledge card about X"
- Filler propositions that restate frontmatter fields
- Auto-generated boilerplate (changelog stubs, empty templates)

### Density maximizers (from real high-scoring cards)
- Every table row contains a unique fact with concrete example
- Code blocks show actual implementation, not pseudocode
- Bullets start with the fact, not the context
- Anti-patterns include WHY it fails and a concrete alternative
- Numbers, metrics, thresholds instead of qualitative descriptions

## Optimal Size: 50-120 Lines

Analysis of high-scoring cards (>= 8.5):
- **50-80 lines**: Focused single-concept cards score highest on density
- **80-120 lines**: Multi-pattern cards with tables and code, still dense
- **120-200 lines**: Acceptable for comprehensive reference cards
- **200+ lines**: Almost always suffer density degradation — split into 2 cards

Body size constraint: <= 5120 bytes. Cards exceeding this are verbose.

## Tags and Keywords: Retrieval Engineering

**Tags** power categorical/faceted search:
- Mix abstraction levels: `[auth, jwt, mutex, concurrent, frontend]`
- Include domain AND technique: `[execution, error-handling, circuit-breaker]`
- 3-7 tags. Fewer = low recall. More = noise.

**Keywords** boost BM25 exact match:
- Terms the user would literally type in a search box
- Include abbreviations and full forms: `["jwt", "json web token"]`

**Long_tails** boost semantic/vector search:
- Complete phrases (5-15 words) that describe the use case
- Written as natural language questions or scenarios
- Example: "how to prevent thundering herd on concurrent token refresh"

## Axioms: Distilled Decision Rules

Axioms are IF/THEN/ALWAYS/NEVER rules extracted from experience.
They compress complex knowledge into actionable directives.

**Well-formed axioms** (from 9.0+ cards):
- `ALWAYS score each dimension independently (no halo effect)`
- `NEVER give 10.0 without concrete evidence across all dimensions`
- `IF density < 1.0 THEN entire evaluation is invalid (rewrite first)`
- `SE score total < 7.0 THEN rewrite before submitting`

**Weak axioms** (from < 8.0 cards):
- `Try to keep things organized` (vague, no condition)
- `Be careful with errors` (no specific action)
- `Consider performance` (no threshold, no consequence)

Pattern: `CONDITION -> ACTION -> CONSEQUENCE`

## Two Body Structures

### domain_kc (external knowledge)
For real-world topics: technologies, patterns, APIs, protocols.
Sections: Quick Reference, Key Concepts, Strategy Phases, Golden Rules, Flow, Comparativo, References.

### meta_kc (system-internal knowledge)
For internal system topics: architecture, patterns, processes.
Sections: Executive Summary, Spec Table, Patterns, Anti-Patterns, Application, References.

## Quality Tiers

| Tier | Score | Requirements |
|------|-------|-------------|
| GOLDEN | >= 9.5 | All 10 HARD + 95% of 20 SOFT gates |
| PUBLISH | >= 8.0 | All 10 HARD + 80% SOFT |
| ACCEPTABLE | >= 7.0 | All 10 HARD + 70% SOFT |
| NEEDS_WORK | < 7.0 | All HARD pass, SOFT insufficient |
| REJECTED | — | Any HARD gate fails |

## Scoring Dimensions (5 x 2 pts = 10 max)

| Dim | Name | 2.0 Criteria |
|-----|------|-------------|
| D1 | Frontmatter | 15 fields filled, specific tldr with data |
| D2 | Density | >= 0.90, numeric metrics, zero padding |
| D3 | Axioms | 4+ ALWAYS/NEVER/IF-THEN with clear conditions |
| D4 | Structure | 6 sections, ASCII diagram, concepts < 80 chars |
| D5 | Format | Body <= 4KB, zero repetition, real comparisons |

**Evaluate D2 first** — it is the prerequisite for all other dimensions.

## Anti-Patterns (from real low-scoring cards)

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| Vague tldr | "KC about agent execution" | Add specifics: model, method, metrics |
| No tags | Empty or single tag | 3-7 tags mixing domain + technique |
| Prose body | Paragraphs explaining concepts | Convert to tables, bullets, code |
| No examples | Abstract rules without concrete cases | Add code, config, or data samples |
| Template residue | "[PLACEHOLDER]", "Untitled Knowledge Card" | Fill or remove every placeholder |
| Frontmatter echo | Body repeats what frontmatter says | Body adds depth, not repetition |
| Auto-generated QA | "Q: What is X? A: X is about X" | Remove or write genuine QA pairs |
| Missing anti-patterns | Only positive patterns documented | Every pattern implies a failure mode |
| No when_to_use | Reader cannot judge relevance | Specific context: file types, scenarios |
| Giant monolith | 300+ lines, mixed topics | Split into focused atomic cards |

## Key Differences from Other Artifact Types

| Aspect | knowledge_card | model_card | learning_record |
|--------|---------------|------------|-----------------|
| Source | External research | LLM specs | Internal experience |
| Purpose | Atomic fact | Model capabilities/cost | What worked/failed |
| Size limit | 5120 bytes | 4096 bytes | 3072 bytes |
| Density gate | >= 0.80 | >= 0.85 | >= 0.80 |
| Body variants | 2 (domain/meta) | 1 fixed | 1 fixed |
| quality field | null (never self-score) | null | null |
