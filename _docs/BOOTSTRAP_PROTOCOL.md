# CEX Bootstrap Protocol: Drive-Based Self-Improvement

## The Loop

Every nucleus improves itself through its {{DRIVE}}. The drive determines
WHAT to seek, HOW to evaluate, and WHEN to iterate.

```
          SCAN                JUDGE               BUILD
   +----------------+   +----------------+   +----------------+
   | Drive asks its |-->| Compare vs     |-->| 8F Runner      |
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
| L1 | SKELETON | ~56 | 7 core kinds per nucleus via 8F Runner + seeds |
| L2 | VERTICAL | ~106 | +50 domain kinds, drive-based expansion |
| L3 | DEEP | ~200+ | Real research, cross-nucleus wiring, quality spiral |

## Per-Nucleus Bootstrap

### N01 -- Research Bootstrap
```
SCAN:  "{{LENS_QUESTION}}" -- What do competitors know that we don't?
       Read: competitor repos, framework docs, papers
       Tool: {{MCPS}} (web scraping, search)
JUDGE: Compare scraped knowledge vs existing KCs. Gap = what they have, we don't.
BUILD: KC-Source (raw) -> KC-Domain (distilled) -> feed relevant nucleus
CYCLE: Every KC reveals new gaps -> continuous improvement
```
Extra kinds: rag_source, embedding_config, few_shot_example, scoring_rubric, prompt_template

### N02 -- Marketing Bootstrap
```
SCAN:  "{{LENS_QUESTION}}" -- What converts best?
       Read: top-performing ads, conversion data, copywriting frameworks
JUDGE: Compare current templates vs best-in-class. Gap = patterns missing.
BUILD: prompt_template (hook) -> few_shot_example (golden+anti) -> persona_prompt
CYCLE: Each template reveals new audience segments
```
Extra kinds: prompt_template, persona_prompt, action_prompt, few_shot_example, response_format

### N03 -- Engineering Bootstrap
```
SCAN:  "{{LENS_QUESTION}}" -- Is this the best artifact possible?
       Run: cex_doctor.py on ALL artifacts. Score: 5D per artifact.
JUDGE: Below 8.0 = rebuild. Below 9.5 = room for improvement.
BUILD: Read artifact + builder ISOs -> identify weakness -> rebuild via 8F
CYCLE: Raising bar reveals flaws at higher resolution
```
Extra kinds: pattern, scoring_rubric, interface, skill, boot_config, response_format, learning_record

### N04 -- Knowledge Bootstrap
```
SCAN:  "{{LENS_QUESTION}}" -- What knowledge is unstructured?
       Glob all .md -> extract frontmatter -> build cross-reference map
JUDGE: Orphan artifacts, knowledge islands, coverage gaps
BUILD: Missing KC -> wire feeds_kinds -> update index -> chunk_strategy
CYCLE: Each indexed KC reveals adjacent topics
```
Extra kinds: chunk_strategy, retriever_config, embedding_config, rag_source, learning_record

### N05 -- Operations Bootstrap
```
SCAN:  "{{LENS_QUESTION}}" -- Why isn't this running?
       Try: execute each workflow. Test: dispatch_rules route? Signals fire?
JUDGE: Failure = fix. Slow = optimize. Manual = automate.
BUILD: spawn_config (launch) -> signal (report) -> checkpoint (resume) -> health_check
CYCLE: Fixing one bottleneck reveals the next
```
Extra kinds: spawn_config, signal, checkpoint, deploy_config, env_config, health_check, retry_policy

### N06 -- Commercial Bootstrap
```
SCAN:  "{{LENS_QUESTION}}" -- What value is uncaptured?
       Audit: all kinds -- which are teachable? What would someone pay?
JUDGE: Value uncaptured = opportunity. Knowledge unpackaged = waste.
BUILD: Course outline -> pricing tier -> sales template -> schedule
CYCLE: Each product reveals adjacent products
```
Extra kinds: few_shot_example, scoring_rubric, schedule, prompt_template, learning_record

### N07 -- Administration Bootstrap
```
SCAN:  "{{LENS_QUESTION}}" -- What requires manual intervention?
       Monitor: routing decisions, confidence levels, common patterns
JUDGE: Manual = failure. Low confidence = needs keywords. Common = needs DAG.
BUILD: dispatch_rule (keywords) -> DAG (multi-nucleus) -> handoff -> signal
CYCLE: Automating one decision reveals more manual steps
```
Extra kinds: dag, handoff, signal, spawn_config, dispatch_rule, retry_policy, health_check

## Domain Flywheel (Cross-Nucleus Synergy)

```
Research        --> Knowledge indexes
Knowledge       --> Engineering rebuilds
Engineering     --> Operations tests
Operations      --> Marketing promotes
Marketing       --> Commercial monetizes
Commercial      --> Administration orchestrates
Administration  --> Research discovers (loop)
```

Each nucleus's output feeds another. The system improves by spinning the flywheel.

## Bootstrap Commands

```bash
# Fill seeds first
# Edit _seeds/seed_n{01-07}.txt with your agent names, drives, concepts

# Level 1: Build skeleton (7 core kinds per nucleus)
bash _tools/build_all_nuclei.sh

# Level 2: Expand with domain kinds
python _tools/cex_bootstrap.py --all --level 2

# Level 2: Expand single nucleus
python _tools/cex_bootstrap.py --nucleus N03 --level 2

# Dry-run preview
python _tools/cex_bootstrap.py --all --level 2 --dry-run

# Level 3: Quality spiral
python _tools/cex_bootstrap.py --nucleus N03 --level 3 --target 9.0
```

## Execution Order

```
Phase A: VERTICAL (Level 2)
  A1: N03 Engineering expands (+7 kinds)    -- quality reference
  A2: N04 Knowledge expands (+6 kinds)      -- knowledge base
  A3: N01 Research expands (+6 kinds)       -- research infra
  A4: N05 Operations expands (+7 kinds)     -- ops infra
  A5: N07 Admin expands (+6 kinds)          -- routing infra
  A6: N02 Marketing + N06 Commercial (+12)  -- output layer

Phase B: DEEP (Level 3)
  B1: Research scans real sources
  B2: Knowledge indexes everything
  B3: Engineering rebuilds below 8.0
  B4: Operations tests all workflows
  B5: Repeat until target met
```

## _instances/ Directory

Filled instances live in `_instances/{project_name}/`.
Example: `_instances/organization/` contains organization's 7-nucleus implementation
with specific agent names (research_agent, marketing_agent, builder_agent, etc.) and personality
drives (7 deadly sins). This is ONE possible filling of the CEX mold.
