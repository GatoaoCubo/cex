# CEXAI -- Presentation Script (3 min)

## For: AI professionals and enthusiasts
## Tone: Technical-didactic, direct, no fluff

---

CEXAI -- Cognitive Exchange AI -- is a universal typed dictionary for artificial intelligence agents. The X stands for Exchange: intelligence compounds when shared.

Imagine the following problem: you want an LLM to build an agent. You ask, and it generates a markdown or YAML file with fields invented on the spot. Another LLM generates different fields. Another model generates a completely incompatible structure. There is no standard. Each generation is an isolated accident.

CEXAI solves this with a taxonomy of 293 types -- called "kinds". Each kind has a name, a definition, a schema, and a builder with 12 instruction files (one per pillar). When any LLM -- Claude, GPT, Gemini, Llama -- needs to generate an artifact, it consults the builder for that kind and produces something structurally compatible with all other artifacts in the system.

These 293 kinds are organized into 12 pillars. Pillar 1 is knowledge. Pillar 2 is agents. Pillar 3 is prompts. Pillar 4 is tools. And so on, up to pillar 12 which is orchestration. Each artifact belongs to exactly one pillar -- this is an immutable rule called "one kind, one pillar".

The build engine is called the 8F Pipeline -- eight sequential functions that every LLM executes to produce an artifact. F1 Constrain loads the schema. F2 Become loads the builder identity. F3 Inject loads relevant knowledge -- knowledge cards, examples, memory. F4 Reason plans the approach. F5 Call identifies available tools. F6 Produce generates the artifact. F7 Govern validates with a 12-point checklist. F8 Collaborate saves, compiles to YAML, re-indexes, and signals completion.

Validation at F7 uses two methods. 12LP is a 12-point structural checklist -- frontmatter, schema, density, uniqueness, boundary. 5D is a 5-dimension scoring -- structural integrity, content density, actionability, boundary discipline, and composability. The final score is a weighted average. Below 8.0, the artifact is not published.

Above the 293-kind layer, there are 7 nuclei -- each driven by one of the Artificial Sins. Each nucleus is a composition of 12 to 25 kinds forming an operational department. N03, the Builder, is the most important -- it is the factory that builds factories. It accesses all 298 builders and executes the 8F pipeline. N07 is the orchestrator -- it never executes, only dispatches tasks to the other nuclei.

The architecture is multi-LLM by design. N03 uses Claude Opus for complex construction. N05 uses OpenAI Codex for code review. N04 and N01 use Gemini 2.5 Pro with a 1 million token context window for knowledge and research. N02 and N06 use Claude Sonnet for creative writing. And as a free fallback, there is an Ollama provider that runs local models at zero cost.

The orchestration system supports up to 6 builders in parallel via grid dispatch, with continuous batching -- when a slot finishes, the next one in the queue enters automatically. Each builder signals completion via JSON files, and a monitor detects stalls.

What makes CEX unique is self-reference. N03 built itself using its own 8F pipeline. The artifacts that define how to build artifacts were built by the system they define. This is an intentional Strange Loop -- a bootstrap paradox resolved in 3 phases: manual genesis, autopoiesis where the system completes itself, and rewriting where it improves its own originals.

To use CEXAI, you install it, boot with the "cex" command, and describe what you want in natural language. The engine resolves the intent to a kind, loads the builder, and executes the 8F pipeline. The result is a typed, validated, compiled, and indexed knowledge asset -- ready to compose with other artifacts in the system and portable across any CEXAI instance.

CEXAI is not an agent framework. It is an AI brain -- a construction dictionary where every artifact is a typed, portable knowledge asset. Any framework can consume the artifacts it produces. Any LLM can execute its builders. The only thing CEXAI is opinionated about is structure -- and that structure is what makes AI systems scale with quality. Every artifact you produce is an exchange unit: share it across instances, runtimes, and teams. Intelligence compounds when exchanged.
