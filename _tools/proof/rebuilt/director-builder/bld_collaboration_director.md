---
kind: collaboration
id: bld_collaboration_director
pillar: P08
llm_function: COLLABORATE
purpose: How director-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: director-builder
## My Role in Crews
I am a COORDINATOR. I answer ONE question: "which builders run, in what order, with what handoffs, and how do they coordinate?"
I define the full orchestration spec for a multi-builder crew — its mission, DAG topology, handoff contracts between builders, parallelism rules, failure strategies, and entry/exit anchors. I do NOT define individual builder logic (builder-builder), satellite architecture (satellite-spec-builder), or reusable coordination patterns (pattern-builder).
## Crew Compositions
### Crew: "New Crew Design"
```
  1. mission-analyzer      -> "decomposes the goal into builder roles and data flow requirements"
  2. director-builder      -> "produces the full director: DAG, handoff contracts, parallelism, failure handling"
  3. dag-validator         -> "validates the DAG is acyclic and all handoff contracts are satisfiable"
```
### Crew: "Crew Documentation Package"
```
  1. director-builder      -> "produces the director artifact with all 24+ frontmatter fields"
  2. diagram-builder       -> "renders the DAG and crew topology visually from the director spec"
  3. knowledge-card-builder -> "extracts atomic facts from the director for brain indexing"
```
### Crew: "Multi-Crew Orchestration Design"
```
  1. director-builder      -> "specs each sub-crew's mission, DAG, and handoff contracts independently"
  2. pipeline-builder      -> "chains multiple directors into a higher-order pipeline with inter-crew handoffs"
  3. monitoring-builder    -> "defines observability across all directors in the pipeline"
```
## Handoff Protocol
### I Receive
- seeds: mission description, list of builder ids, entry_point, exit_point, known constraints
- optional: parallelism preferences, existing handoff contracts, failure tolerance requirements
### I Produce
- director artifact (YAML frontmatter + Markdown body, 24+ fields, max 300 lines)
- committed to: `cex/P08/examples/p08_dir_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- mission-analyzer: decomposes goal into builder roles and data flow requirements that seed the DAG design
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| dag-validator | needs the director's dag_edges to validate acyclicity and contract satisfiability |
| diagram-builder | uses the director's DAG structure and crew composition to render the visual topology |
| pipeline-builder | chains multiple director specs into a higher-order execution pipeline |
| monitoring-builder | uses the director's entry/exit anchors and signal config to define observability |
