# 8F Pipeline

The 8F pipeline is the universal reasoning protocol that powers every task in CEXAI. It is mandatory for all nuclei (N01-N07), for every task, with no exceptions.

8F is not a "build checklist" -- it is how CEXAI thinks. Whether researching, writing copy, building code, organizing knowledge, deploying, pricing, or orchestrating, the same 8 reasoning steps execute in sequence.

## Why 8F Exists

The user will always have a knowledge gap. Their input will be vague, incomplete, non-technical. CEXAI compensates by running 8F on every input, turning 5 words into a production-quality artifact.

## The 8 Functions

### F1 CONSTRAIN

**Purpose:** Resolve the kind, pillar, and constraints for the task.

| Input | Action |
|-------|--------|
| `.cex/kinds_meta.json` | Resolve which of the 300 [[Kinds]] matches the intent |
| `P{xx}/_schema.yaml` | Load the pillar schema for structural rules |

**Output:** `kind={kind}, pillar={pillar}, max_bytes={max}, naming={pattern}`

F1 is where intent resolution happens. The user says "make me a landing page" and F1 resolves it to `kind=landing_page, pillar=P05`.

### F2 BECOME

**Purpose:** Load the builder identity -- the specialized knowledge for producing this kind.

| Input | Action |
|-------|--------|
| `archetypes/builders/{kind}-builder/bld_model_{kind}.md` | Load builder model |
| `archetypes/builders/{kind}-builder/bld_prompt_{kind}.md` | Load builder prompt |

**Output:** `Builder loaded ({N} ISOs, 12-pillar). Identity: {role}`

Each builder has 12 ISOs (one per pillar), giving it domain-specific knowledge for every aspect of production.

### F3 INJECT

**Purpose:** Assemble context from knowledge sources.

| Input | Action |
|-------|--------|
| `P01_knowledge/library/kind/kc_{kind}.md` | Load the kind's knowledge card |
| `examples/` and `compiled/` | Search for similar existing artifacts |
| Domain KCs, brand config, memory | Load all relevant context |

**Output:** `Injected {N} knowledge sources. Template-First match: {score}%`

F3 typically loads 10+ context sources: KCs, examples, memory, brand config, and similar artifacts.

#### F3b PERSIST (sub-step, optional)

After assembling context, declare what new knowledge should be persisted:
- New entities discovered -- store as `entity_memory`
- Updated facts -- update `knowledge_card`
- Session learnings -- create `learning_record`

#### F3c GROUND (sub-step, when sources are cited)

Record provenance for each injected source:
- Source path or URL
- Retrieval confidence score
- Freshness (last updated timestamp)

### F4 REASON

**Purpose:** Plan the approach before producing.

| Input | Action |
|-------|--------|
| Context from F3 | Plan sections, approach, references |
| Construction Triad | Use Template-First if match >= 60% |

**Output:** `Plan -- {N} sections, approach: {template|hybrid|fresh}`

If the task involves subjective decisions (tone, audience, style), the Guided Decision Protocol (GDP) activates here. See [[Commands]] for `/guide`.

### F5 CALL

**Purpose:** Prepare and invoke tools for enrichment.

| Input | Action |
|-------|--------|
| Tool registry | List available tools (compile, doctor, index, signal) |
| Existing artifacts | Scan for reusable components |

**Output:** `Tools ready. {N} similar artifacts found.`

### F6 PRODUCE

**Purpose:** Generate the complete artifact.

| Input | Action |
|-------|--------|
| Builder instructions from F2 | Follow the builder's ISOs |
| Context from F3 | Apply injected knowledge |
| Plan from F4 | Follow the planned structure |

**Output:** `Draft generated ({bytes} bytes, {sections} sections)`

The artifact includes YAML frontmatter (id, kind, title, version, quality, tags) and a structured body. Density target is >= 0.85.

### F7 GOVERN

**Purpose:** Validate quality before saving.

| Input | Action |
|-------|--------|
| H01-H07 gates | 7 hard quality gates |
| 12LP checklist | 12-point checklist |
| 5D dimensions | 5 scoring dimensions (D1-D5 weighted) |

**Output:** `Score {X}/10. Gates: {pass}/{total}. 12LP: {pass}/12`

If the score is below the threshold, F7 returns to F6 for a retry (max 2 retries). Quality floor is 8.0; target is 9.0+.

#### F7b LEARN (sub-step, optional)

Capture feedback signals after scoring:
- Patterns that led to high/low scores
- Gates that commonly fail
- Quality trends over time

### F8 COLLABORATE

**Purpose:** Persist the artifact and notify the system.

| Action | Tool |
|--------|------|
| Save to correct pillar directory | Write .md file |
| Compile | `python _tools/cex_compile.py {path}` |
| Index | `python _tools/cex_index.py` |
| Commit | `git add` + `git commit` |
| Signal | `signal_writer.write_signal(nucleus, 'complete', score)` |

**Output:** `Saved {path}. Compiled. Committed. Signal sent.`

## 8F Trace Output

Every build shows the 8F trace as evidence of the pipeline execution:

```
=== 8F PIPELINE ===
F1 CONSTRAIN: kind=agent, pillar=P02, max=5120B
F2 BECOME: agent-builder loaded (12 ISOs)
F3 INJECT: kc_agent.md + 2 examples. Match: 72%
F4 REASON: 4 sections, approach=template (adapt from match)
F5 CALL: compile+doctor+index ready. 3 similar found.
F6 PRODUCE: 3,200 bytes, 4 sections, density=0.88
F7 GOVERN: 9.0/10. Gates: 7/7. 12LP: 12/12
F8 COLLABORATE: saved P02/agent_x.md. Compiled. Committed.
===================
```

## Example: "make me a landing page"

This walkthrough shows how 5 words of user input become a production-ready artifact.

```
User: "make me a landing page"  (5 words, zero spec)

F1 CONSTRAIN  --> kind=landing_page, pillar=P05, schema loaded, constraints set
F2 BECOME     --> landing-page-builder loaded (12 ISOs), sin lens injected
F3 INJECT     --> 10 context sources: KC, examples, memory, brand, similar artifacts
F4 REASON     --> plan: 12 sections, mobile-first, Tailwind, conversion-optimized
F5 CALL       --> tools executed, references fetched, sub-agents if needed
F6 PRODUCE    --> complete HTML page (responsive, dark mode, SEO, a11y)
F7 GOVERN     --> quality gate: 7 HARD gates, retry if < 8.0
F8 COLLABORATE--> saved, compiled, committed, signaled

Output: production-ready landing page
```

The 8F pipeline is the force multiplier that makes CEXAI outperform raw LLM calls. 5 words in, professional artifact out.

## 8F by Nucleus

8F is the same protocol everywhere -- the domain content changes per nucleus.

### N07 Orchestrator -- "/mission build CRM"

```
F1 CONSTRAIN --> scope: what kind of CRM? what nuclei needed? what wave structure?
F2 BECOME    --> Orchestrating Sloth lens: ruthless quality, precise dispatch
F3 INJECT    --> load mission plans, decision manifest, signal history
F4 REASON    --> plan: 3 waves, 5 nuclei, dependency graph
F5 CALL      --> provider discovery, agent spawn validation, PID tracking
F6 PRODUCE   --> write handoffs + mission plan + wave schedule
F7 GOVERN    --> validate: all handoffs have frontmatter? all nuclei have boot scripts?
F8 COLLABORATE --> dispatch grid, monitor signals, consolidate on completion
```

### N01 Intelligence -- "research competitor pricing"

```
F1 CONSTRAIN --> kind=knowledge_card, pillar=P01, domain=competitor pricing
F2 BECOME    --> Analytical Envy lens: insatiable data hunger
F3 INJECT    --> load KCs on pricing, market data, existing competitor intel
F4 REASON    --> plan: 6 competitors, 3 pricing dimensions, source map
F5 CALL      --> retriever finds existing pricing KCs, query discovers related builders
F6 PRODUCE   --> structured intelligence brief with pricing tables + sources
F7 GOVERN    --> validate: sources cited? data density >= 0.85? no speculation?
F8 COLLABORATE --> save to N01_intelligence/, compile, signal N07
```

### N02 Marketing -- "write ad copy for campaign"

```
F1 CONSTRAIN --> kind=prompt_template, pillar=P03, domain=ad copy
F2 BECOME    --> Creative Lust lens: seductive, irresistible prose
F3 INJECT    --> load brand voice, audience persona, past campaign KCs
F4 REASON    --> plan: 3 ad variants (urgency, FOMO, value), A/B structure
F5 CALL      --> brand config loaded, memory recalls past conversion data
F6 PRODUCE   --> 3 ad copy variants with hooks, CTAs, and character limits
F7 GOVERN    --> validate: brand voice match? CTA present? within platform limits?
F8 COLLABORATE --> save to N02_marketing/, compile, signal N07
```

## Anti-Patterns

These are blocked behaviors that violate the 8F protocol:

1. **Processing a task without 8F trace** -- every task, not just builds
2. **Skipping F7 validation** -- quality governance is never optional
3. **Saving without F8** -- compile + commit + signal are mandatory
4. **"I'll just do a quick..."** -- every task goes through 8F
5. **Dispatching without F1 and F4** -- scope and plan must exist before execution

## Related Pages

- [[Architecture]] -- How nuclei and pillars organize the system
- [[Kinds]] -- The 300 artifact types that F1 CONSTRAIN resolves to
- [[Commands]] -- `/build` and `/mission` trigger 8F
- [[Contributing]] -- 8F is mandatory for all contributed artifacts
