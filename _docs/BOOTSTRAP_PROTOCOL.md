# CEX Bootstrap Protocol: Sin-Driven Self-Improvement

## The Loop

Every nucleus improves itself through its sin. The sin is not decoration --
it is the **drive function** that determines WHAT to seek, HOW to evaluate,
and WHEN to stop (never -- each sin is insatiable).

```
          SCAN                JUDGE               BUILD
   +----------------+   +----------------+   +----------------+
   | Sin asks its   |-->| Compare vs     |-->| 8F Runner      |
   | lens question  |   | genesis mold   |   | produces new   |
   +----------------+   +----------------+   +----------------+
          ^                                         |
          |            VALIDATE                     |
          |     +----------------+                  |
          +-----| Doctor + QG   |<------------------+
                | gates check   |
                +----------------+
```

## 3 Hydration Levels

| Level | Name | Files | Mechanism |
|-------|------|-------|-----------|
| L1 | SKELETON | 56 | 7 core kinds, LLM from seeds (DONE) |
| L2 | VERTICAL | ~106 | +50 domain kinds, sin-driven expansion |
| L3 | DEEP | ~200+ | Real research, cross-nucleus wiring, quality spiral |

## Per-Nucleus Bootstrap

### N01 SHAKA -- ENVY Bootstrap
```
SCAN:  "What do competitors/frameworks know that CEX doesn't?"
       Read: competitor repos, framework docs, arxiv papers
       Tool: Firecrawl MCP -> scrape -> distill
JUDGE: Compare scraped knowledge vs existing KCs. Gap = what they have, we don't.
BUILD: KC-Source (raw) -> KC-Domain (distilled) -> feed relevant nucleus via feeds_kinds
CYCLE: Every KC reveals 3+ new gaps -> infinite ENVY
```
Extra kinds: rag_source, embedding_config, scraper, research_brief, few_shot_example, prompt_template, scoring_rubric
Output: Knowledge that feeds ALL other nuclei

### N02 LILY -- LUST Bootstrap
```
SCAN:  "What desire does the customer not yet know they have?"
       Read: top-performing ads, conversion data, copywriting frameworks
JUDGE: Compare current templates vs best-in-class. Gap = patterns we lack.
BUILD: prompt_template (hook) -> few_shot_example (golden+anti) -> persona_prompt (voice)
CYCLE: Each template reveals new audience segments -> infinite LUST
```
Extra kinds: prompt_template, persona_prompt, action_prompt, few_shot_example, response_format, scoring_rubric, learning_record
Output: Copy templates and conversion patterns

### N03 EDISON -- PRIDE Bootstrap
```
SCAN:  "Is this the best artifact anyone has ever produced?"
       Run: cex_doctor.py on ALL artifacts. Score: 5D per artifact.
JUDGE: Below 8.0 = unworthy. Below 9.5 = room for improvement.
BUILD: Read artifact + builder ISOs -> identify weakness -> rebuild via 8F -> keep best
CYCLE: Raising bar to 9.5 reveals flaws at higher resolution -> infinite PRIDE
```
Extra kinds: pattern, scoring_rubric, interface, skill, tool_definition, boot_config, response_format, learning_record
Output: Higher quality across ALL nuclei (PRIDE serves everyone)

### N04 PYTHA -- GLUTTONY Bootstrap
```
SCAN:  "What knowledge exists that I haven't consumed and structured?"
       Glob all .md -> extract frontmatter -> build cross-reference map
JUDGE: Orphan artifacts, knowledge islands, coverage gaps
BUILD: Missing KC -> wire feeds_kinds -> update index -> create chunk_strategy
CYCLE: Each indexed KC reveals 3 adjacent topics -> infinite GLUTTONY
```
Extra kinds: chunk_strategy, retriever_config, brain_index, embedding_config, rag_source, learning_record, scoring_rubric
Output: Complete knowledge graph connecting all nuclei

### N05 ATLAS -- WRATH Bootstrap
```
SCAN:  "Why isn't this running RIGHT NOW?"
       Try: execute each workflow. Test: dispatch_rules route? Signals fire?
JUDGE: Failure = target. Slow = optimize. Manual = automate.
BUILD: spawn_config (launch) -> signal (report) -> checkpoint (resume) -> health_check (detect)
CYCLE: Fixing one failure reveals the next bottleneck -> infinite WRATH
```
Extra kinds: spawn_config, signal, checkpoint, deploy_config, env_config, health_check, retry_policy, pipeline
Output: Operational infrastructure making everything runnable

### N06 YORK -- GREED Bootstrap
```
SCAN:  "What value exists here that nobody is capturing?"
       Audit: 99 kinds -- which are teachable? What would someone pay?
JUDGE: Value uncaptured = money on table. Knowledge unpackaged = wasted.
BUILD: Course outline -> pricing tier -> sales template -> delivery schedule
CYCLE: Each course reveals adjacent products -> infinite GREED
```
Extra kinds: few_shot_example, scoring_rubric, schedule, prompt_template, learning_record, response_format
Output: Monetization layer capturing value from ALL nuclei

### N07 STELLA -- SLOTH Bootstrap
```
SCAN:  "Who should do this instead of me?"
       Monitor: manual intervention? Low confidence routes? Common unautomated patterns?
JUDGE: Manual = failure. Low confidence = needs keywords. Common = missing DAG.
BUILD: dispatch_rule (keywords) -> DAG (multi-nucleus) -> handoff -> signal
CYCLE: Automating one decision reveals more manual steps -> infinite SLOTH
```
Extra kinds: dag, handoff, signal, spawn_config, dispatch_rule, retry_policy, health_check
Output: Frictionless orchestration routing everything automatically

## Sin Flywheel (Cross-Nucleus Synergy)

```
ENVY researches    --> GLUTTONY indexes
GLUTTONY indexes   --> PRIDE rebuilds
PRIDE rebuilds     --> WRATH tests
WRATH tests        --> LUST markets
LUST markets       --> GREED monetizes
GREED monetizes    --> SLOTH orchestrates
SLOTH orchestrates --> ENVY researches (loop)
```

Each nucleus's output is another's input. The system improves by spinning the flywheel.

## Bootstrap Tool: cex_bootstrap.py

```
Usage: python _tools/cex_bootstrap.py --nucleus N01 --level 2
       python _tools/cex_bootstrap.py --all --level 2
       python _tools/cex_bootstrap.py --nucleus N03 --level 3 --target 9.0

Flags:
  --nucleus N{XX}   Target nucleus (or --all)
  --level 1|2|3     Hydration depth
  --target 8.0      Minimum quality score (PRIDE loop stops here)
  --dry-run         Preview without LLM calls
  --kinds K1 K2     Override: only build these kinds
```

## Bootstrap Execution Order

```
Phase A: VERTICAL EXPANSION (Level 2)
  A1: N03 PRIDE expands itself (+8 kinds)     -- reference quality
  A2: N04 GLUTTONY expands (+7 kinds)         -- knowledge base
  A3: N01 ENVY expands (+7 kinds)             -- research infra
  A4: N05 WRATH expands (+8 kinds)            -- ops infra
  A5: N07 SLOTH expands (+7 kinds)            -- routing infra
  A6: N02 LUST + N06 GREED expand (+13 kinds) -- output layer

Phase B: DEEP HYDRATION (Level 3)
  B1: ENVY scans real sources (Firecrawl)
  B2: GLUTTONY indexes everything
  B3: PRIDE rebuilds below 8.0
  B4: WRATH tests all workflows
  B5: LUST generates from patterns
  B6: GREED packages value
  B7: SLOTH optimizes routing

Phase C: QUALITY SPIRAL (Level 3+)
  C1: Doctor scores all artifacts
  C2: PRIDE rebuilds anything below target
  C3: GLUTTONY re-indexes
  C4: Repeat until target met
```
