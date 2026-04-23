# Glossary

**8F Pipeline** -- The eight-step reasoning process that every task goes through: Constrain, Become, Inject, Reason, Call, Produce, Govern, Collaborate. It is how CEX thinks, whether the task is research, writing, building, or orchestration.

**Artifact** -- Any structured file that CEX produces. Artifacts have YAML frontmatter (id, kind, pillar, version, tags) and a markdown body. They are the atomic units of the knowledge base.

**Builder** -- A set of 12 instruction files (ISOs) that teach an LLM how to produce a specific kind of artifact. Each ISO corresponds to one of the 12 pillars. When you ask CEX to build an agent, it loads the agent-builder's 12 ISOs.

**Crew** -- A multi-role team assembled for work that requires several specialists with handoffs between them. Defined by a crew template (roles and process) and a team charter (mission-specific parameters). Used when a single builder is too shallow and a full grid is too parallel.

**GDP (Guided Decision Protocol)** -- The rule that subjective decisions (tone, audience, style) must be made by the user before autonomous execution begins. Answers are recorded in a decision manifest that all nuclei read.

**Grid** -- A dispatch mode that runs up to 6 nuclei in parallel, each working on its own task. Used for missions that decompose into independent workstreams.

**Handoff** -- A structured file that N07 (the orchestrator) writes to tell a nucleus what to do. Contains the task description, artifact references, decision manifest pointer, and expected output.

**ISO** -- One of the 12 instruction files inside a builder. Each ISO maps 1:1 to a pillar (P01-P12) and provides domain-specific guidance for producing that kind of artifact. ISO stands for the builder's individual instruction set.

**Kind** -- A named artifact type from the CEX taxonomy. There are 300 kinds (e.g., `knowledge_card`, `agent`, `prompt_template`, `workflow`). Each kind has a builder, a schema, and a knowledge card.

**Nucleus** -- A specialized AI agent that acts as a department. CEX has 7 operational nuclei (N01-N07), each with a distinct role (intelligence, marketing, engineering, knowledge, operations, commercial, orchestration) and cultural personality.

**Pillar** -- One of 12 domain categories (P01-P12) that organize artifacts: Knowledge, Model, Prompt, Tools, Output, Schema, Evaluation, Architecture, Config, Memory, Feedback, Orchestration.

**Signal** -- A JSON file that a nucleus writes to `.cex/runtime/signals/` when it finishes a task. Contains the nucleus ID, status, quality score, and kind. The orchestrator polls for these to know when work is done.

**Artificial Sin** -- The personality heuristic (behavioral bias) assigned to each nucleus. Based on one of the seven deadly sins, it determines what a nucleus optimizes for under ambiguity. For example, N01's Analytical Envy drives exhaustive research; N06's Strategic Greed maximizes revenue per artifact.

**CEXAI (Cognitive Exchange AI)** -- The full name of the system. The X stands for Exchange: intelligence compounds when shared. Short form: CEX (used in code, CLIs, variable names).

**Exchange** -- The sharing model that gives CEXAI its name. Typed artifacts (knowledge cards, builders, vertical nuclei) are the exchange units. They are self-describing (.md with YAML frontmatter), quality-scored, and runtime-agnostic. Import into any CEXAI instance; `cex_doctor.py` validates automatically.

**Exchange Protocol** -- The architectural spec for how CEXAI instances share typed cognition. Defines what is exchangeable (N00 artifacts, vertical nuclei, knowledge cards), what is not (brand config, memory, secrets), and how quality gates work on import.

**Vertical Nucleus** -- A domain-specialized nucleus (N08+) contributed by the community. Examples: N08_healthcare, N09_fintech, N10_edtech. Each is a full 12-pillar AI department with its own sin lens, vocabulary, and builders.
