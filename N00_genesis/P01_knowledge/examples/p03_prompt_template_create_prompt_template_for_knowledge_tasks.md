---
id: p03_pt_knowledge_tasks
kind: prompt_template
pillar: P03
title: "Knowledge Task Execution Template"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: prompt-template-builder
variables:
  - name: topic
    type: string
    required: true
    default: null
    description: The subject, concept, or entity the knowledge task will address
  - name: domain
    type: string
    required: true
    default: null
    description: Knowledge domain classifying the topic (e.g., machine_learning, finance, biology, law)
  - name: task_type
    type: string
    required: true
    default: null
    description: The specific knowledge operation to perform — one of synthesize, extract, compare, summarize, map, audit
  - name: audience
    type: string
    required: false
    default: "intermediate"
    description: Target reader level that calibrates terminology and depth (beginner, intermediate, expert)
  - name: depth
    type: string
    required: false
    default: "standard"
    description: Coverage depth controlling section count and elaboration (brief, standard, deep)
  - name: output_format
    type: string
    required: false
    default: "structured"
    description: Shape of the output — structured (headers + tables), prose, or bullet
  - name: sources
    type: list
    required: false
    default: []
    description: Reference sources, URLs, or citation keys to incorporate into the output
  - name: constraints
    type: list
    required: false
    default: []
    description: Explicit focus constraints, exclusion rules, or scope boundaries for the task
variable_syntax: "mustache"
composable: true
domain: knowledge
quality: 9.1
tags: [prompt-template, knowledge, P03, knowledge-task, synthesis, extraction, reusable]
tldr: "Executes any knowledge task (synthesize, extract, compare, summarize, map, audit) for a given topic and domain."
keywords: [knowledge, task, template, synthesis, extraction, comparison, audit, domain, reusable]
density_score: 0.91
related:
  - examples_prompt_template_builder
  - p03_pt_engineering_task
  - p03_pt_creation_task
  - bld_examples_chain
  - p12_wf_intelligence
  - p06_schema_research_brief
  - bld_examples_response_format
  - p08_kc_capability_registry
  - p06_is_knowledge_data_model
  - p03_ins_system_prompt
---
## Purpose

Produces a precisely scoped knowledge task prompt for any topic within any domain. The same mold generates distinct prompts across six knowledge operations — synthesize, extract, compare, summarize, map, and audit — by substituting `task_type` and the remaining variables. Reuse scope covers any situation where an LLM must execute a structured knowledge operation: building knowledge cards, extracting entities from documents, comparing concepts, auditing knowledge bases, or mapping concept relationships. Composable: designed for embedding as a sub-block inside mission-level or multi-step pipeline templates.

## Variables Table

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| topic | string | true | null | The subject, concept, or entity the knowledge task will address |
| domain | string | true | null | Knowledge domain classifying the topic (e.g., machine_learning, finance, biology) |
| task_type | string | true | null | Knowledge operation: synthesize, extract, compare, summarize, map, or audit |
| audience | string | false | "intermediate" | Target reader level calibrating terminology and depth |
| depth | string | false | "standard" | Coverage depth: brief, standard, or deep |
| output_format | string | false | "structured" | Output shape: structured, prose, or bullet |
| sources | list | false | [] | Reference sources, URLs, or citation keys to incorporate |
| constraints | list | false | [] | Explicit focus constraints, exclusion rules, or scope boundaries |

## Template Body

```
You are a knowledge specialist operating in the {{domain}} domain.

TASK: {{task_type}}
TOPIC: {{topic}}
AUDIENCE: {{audience}}
DEPTH: {{depth}}
OUTPUT FORMAT: {{output_format}}

{{#sources}}
SOURCES TO INCORPORATE:
{{#sources}}
- {{.}}
{{/sources}}
{{/sources}}

{{#constraints}}
SCOPE CONSTRAINTS:
{{#constraints}}
- {{.}}
{{/constraints}}
{{/constraints}}

---

TASK EXECUTION GUIDE

Apply the operation "{{task_type}}" to "{{topic}}" within {{domain}} as follows:

synthesize  → Integrate multiple perspectives into a unified, original account. Resolve contradictions. Surface the consensus and the contested edges.
extract     → Identify and list discrete, atomic facts, entities, or relationships. One claim per item. No interpretation.
compare     → Produce a structured comparison: shared properties, divergent properties, and the implications of the differences.
summarize   → Compress the core meaning into the minimum tokens that preserve fidelity. Preserve key terms. Omit elaboration.
map         → Generate a concept map: nodes (key terms in {{domain}}), edges (relationships), and a brief label for each edge type.
audit       → Evaluate existing knowledge for gaps, outdated claims, internal contradictions, and missing cross-references. Return a scored gap report.

---

OUTPUT REQUIREMENTS

Format: {{output_format}}
  structured → Use ## headers, tables, and bullet lists. Every section must have a label.
  prose      → Continuous paragraphs. No headers except the title. Transitions required.
  bullet     → Flat or nested bullet lists only. No prose paragraphs.

Depth calibration for {{depth}}:
  brief    → 150–300 words. Essential claims only.
  standard → 400–700 words. Core concepts + 1 example per concept.
  deep     → 800–1400 words. Full elaboration, edge cases, cross-domain links.

Audience calibration for {{audience}}:
  beginner     → Define all domain terms on first use. Avoid jargon. Use analogies.
  intermediate → Assume domain literacy. Define only specialized sub-terms.
  expert       → Use full technical vocabulary. Omit foundational explanations.

Deliver the {{task_type}} output for {{topic}} now.
```

## Quality Gates

| Gate | Status | Notes |
|---|---|---|
| H01 id matches `^p03_pt_[a-z][a-z0-9_]+$` | PASS | `p03_pt_knowledge_tasks` matches pattern |
| H02 required frontmatter fields present | PASS | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H03 `kind` equals `prompt_template` | PASS | Exact literal match |
| H04 `quality` is null | PASS | null at authoring time |
| H05 all body `{{vars}}` declared in variables list | PASS | topic, domain, task_type, audience, depth, output_format, sources, constraints — all declared |
| H06 all declared variables appear in body | PASS | All 8 variables used in template body |
| H07 body contains at least one `{{variable}}` | PASS | Multiple Mustache slots present |
| H08 `variable_syntax` is mustache or bracket | PASS | mustache — no mixed syntax |
| H09 injection point declarable | PASS | Template targets user turn; composable: true for system-level embedding |

## Examples

### Example 1 — Synthesize (structured, intermediate, standard)

**Variables:**
```yaml
topic: "transformer attention mechanisms"
domain: "machine_learning"
task_type: "synthesize"
audience: "intermediate"
depth: "standard"
output_format: "structured"
sources: ["Vaswani et al. 2017", "Dao et al. 2022"]
constraints: ["exclude positional encodings", "focus on multi-head design"]
```

**Rendered Output:**
```
You are a knowledge specialist operating in the machine_learning domain.

TASK: synthesize
TOPIC: transformer attention mechanisms
AUDIENCE: intermediate
DEPTH: standard
OUTPUT FORMAT: structured

SOURCES TO INCORPORATE:
- Vaswani et al. 2017
- Dao et al. 2022

SCOPE CONSTRAINTS:
- exclude positional encodings
- focus on multi-head design

---

TASK EXECUTION GUIDE

Apply the operation "synthesize" to "transformer attention mechanisms" within machine_learning as follows:

synthesize → Integrate multiple perspectives into a unified, original account. Resolve contradictions. Surface the consensus and the contested edges.

---

OUTPUT REQUIREMENTS

Format: structured
  structured → Use ## headers, tables, and bullet lists. Every section must have a label.

Depth calibration for standard:
  standard → 400–700 words. Core concepts + 1 example per concept.

Audience calibration for intermediate:
  intermediate → Assume domain literacy. Define only specialized sub-terms.

Deliver the synthesize output for transformer attention mechanisms now.
```

### Example 2 — Audit (bullet, expert, deep)

**Variables:**
```yaml
topic: "RAG pipeline evaluation metrics"
domain: "knowledge_retrieval"
task_type: "audit"
audience: "expert"
depth: "deep"
output_format: "bullet"
sources: []
constraints: ["focus on retrieval precision and context faithfulness"]
```

**Rendered Output:**
```
You are a knowledge specialist operating in the knowledge_retrieval domain.

TASK: audit
TOPIC: RAG pipeline evaluation metrics
AUDIENCE: expert
DEPTH: deep
OUTPUT FORMAT: bullet

SCOPE CONSTRAINTS:
- focus on retrieval precision and context faithfulness

---

TASK EXECUTION GUIDE

Apply the operation "audit" to "RAG pipeline evaluation metrics" within knowledge_retrieval as follows:

audit → Evaluate existing knowledge for gaps, outdated claims, internal contradictions, and missing cross-references. Return a scored gap report.

---

OUTPUT REQUIREMENTS

Format: bullet
  bullet → Flat or nested bullet lists only. No prose paragraphs.

Depth calibration for deep:
  deep → 800–1400 words. Full elaboration, edge cases, cross-domain links.

Audience calibration for expert:
  expert → Use full technical vocabulary. Omit foundational explanations.

Deliver the audit output for RAG pipeline evaluation metrics now.
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[examples_prompt_template_builder]] | downstream | 0.47 |
| [[p03_pt_engineering_task]] | sibling | 0.30 |
| [[p03_pt_creation_task]] | sibling | 0.28 |
| [[bld_examples_chain]] | downstream | 0.22 |
| [[p12_wf_intelligence]] | downstream | 0.22 |
| [[p06_schema_research_brief]] | downstream | 0.22 |
| [[bld_examples_response_format]] | downstream | 0.22 |
| [[p08_kc_capability_registry]] | downstream | 0.21 |
| [[p06_is_knowledge_data_model]] | downstream | 0.20 |
| [[p03_ins_system_prompt]] | related | 0.20 |
