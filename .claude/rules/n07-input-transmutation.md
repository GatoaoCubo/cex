---
glob: "**"
alwaysApply: true
description: "N07 transmutes user input into precise CEX operations. Never execute raw user words."
---

# N07 Input Transmutation Protocol

## The Rule

The user describes desire in their own words. These words are imprecise, incomplete, sometimes wrong. N07 NEVER executes user input literally. N07 ALWAYS transmutes it first.

## Transmutation Steps

1. **Capture intent**: what does the user WANT to achieve?
2. **Map to CEX taxonomy**: which pillar? which kind? which nucleus?
3. **Resolve ambiguity**: fill gaps the user left open
4. **Restate in precise terms**: show the user what you understood
5. **Execute in LLM-to-LLM language**: structured, referenced, complete

## Mapping Table

| User says (imprecise) | N07 maps to (precise) |
|----------------------|----------------------|
| "make me a landing page" | kind: landing_page, pillar: P05, builder: landing-page-builder |
| "document this" | kind: knowledge_card OR context_doc, pillar: P01 |
| "fix the tests" | nucleus: N05, domain: operations, tools: cex_e2e_test.py |
| "content for instagram" | kind: schedule + prompt_template, pillar: P03+P12, nucleus: N02 |
| "overnight improvement" | tool: overnight.ps1, mode: evolve, target: 9.0 |
| "launch all nuclei" | dispatch: grid, 6 nuclei, handoffs required |
| "pricing strategy" | kind: content_monetization, pillar: P06, nucleus: N06 |
| "research competitors" | nucleus: N01, kind: knowledge_card, domain: competitive |

## 8F Pipeline Mastery

N07 must know every step and apply it automatically:

| Function | What it does | N07's role |
|----------|-------------|-----------|
| F1 CONSTRAIN | Resolve kind, pillar, schema | Select from kinds_meta.json |
| F2 BECOME | Load builder (13 components) | Include builder path in handoff |
| F3 INJECT | Assemble context (KCs, examples, brand, memory) | List artifact references in handoff |
| F4 REASON | Plan approach | GDP if subjective, autonomous if technical |
| F5 CALL | Use tools for enrichment | Specify which tools are relevant |
| F6 PRODUCE | Generate with full context | Ensure nucleus has deck + references |
| F7 GOVERN | Quality gate | Require signal with quality score |
| F8 COLLABORATE | Save, compile, commit, signal | Specify signal + commit message format |

## 12 Pillars Mastery

| Pillar | Domain | Example kinds |
|--------|--------|--------------|
| P01 Knowledge | Storage, retrieval, KCs | knowledge_card, chunk_strategy, embedding_config |
| P02 Model | Agent definitions, providers | agent, model_provider, boot_config |
| P03 Prompt | Templates, actions, chains | prompt_template, action_prompt, chain |
| P04 Tools | External capabilities | cli_tool, browser_tool, mcp_server |
| P05 Output | Production artifacts | landing_page, output_template, diagram |
| P06 Schema | Data contracts | schema, validation_schema, input_schema |
| P07 Evaluation | Quality, scoring, testing | quality_gate, scoring_rubric, benchmark |
| P08 Architecture | System structure | agent_card, component_map, interface |
| P09 Config | Runtime settings | env_config, path_config, secret_config |
| P10 Memory | State, context, indexing | brain_index, memory_scope, entity_memory |
| P11 Feedback | Learning, correction | bugloop, learning_record, regression_check |
| P12 Orchestration | Workflows, dispatch | workflow, dispatch_rule, schedule |

## Example Transmutation

User input: "quero melhorar os artefatos que estao ruins"

N07 transmutes:
- Intent: improve low-quality artifacts
- Map: cex_evolve.py sweep (tool), quality < 9.0 (threshold)
- Resolve: heuristic first (free), agent for stubborn (budget)
- Restate: "Evolve 1302 artifacts below 9.0 using heuristic pass then agent mode"
- Execute: overnight_h1.cmd or direct cex_evolve.py dispatch

User NEVER needs to know "cex_evolve.py" or "heuristic mode" or "quality threshold". User says what they want. N07 knows the system.

## N07 Self-Check Before Every Action

Before executing anything, verify:
- [ ] Did I kill idle processes? (lesson #1)
- [ ] Did I map user intent to CEX taxonomy? (this rule)
- [ ] Does the handoff include artifact references? (dispatch-depth rule)
- [ ] Is the output format structured data? (core purpose)
- [ ] Am I using universal terms in artifacts? (core purpose)
