---
id: instr_prompt_template_builder
kind: instructions
pillar: P03
llm_function: REASON
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [instructions, prompt-template, P03, execution-protocol]
---

# Instructions — prompt-template-builder

## Execution Protocol

Three phases: DISCOVER → COMPOSE → VALIDATE. Each numbered step is one atomic action.

---

## Phase 1: DISCOVER

**1.** Read the input request and extract the stated purpose in one sentence.

**2.** Ask: "Will this prompt be invoked multiple times with different values?" If NO, route to `user_prompt` and stop.

**3.** Ask: "Does this define an agent's identity?" If YES, route to `system_prompt` and stop.

**4.** Ask: "Does this generate or improve other prompts?" If YES, route to `meta_prompt` and stop.

**5.** List every dynamic slot in the input — any value that changes between invocations.

**6.** Assign a type to each slot: `string`, `list`, `integer`, `boolean`, or `object`.

**7.** Mark each slot as `required: true` or `required: false`.

**8.** Assign a `default` value to every optional slot.

**9.** Write a one-sentence description for each variable.

**10.** Determine the `variable_syntax` tier: `mustache` (default) or `bracket` (only if target system conflicts with Mustache).

**11.** Determine `composable`: true if this template is designed to be embedded inside a larger template.

**12.** Identify the `domain` (e.g., research, marketing, knowledge, code).

---

## Phase 2: COMPOSE

**13.** Generate the `id` using the pattern: `p03_pt_{{topic_slug}}` where topic_slug is lowercase, underscored, and describes the template's purpose.

**14.** Write the frontmatter block using OUTPUT_TEMPLATE.md as the exact structure.

**15.** Write the `## Purpose` section: one paragraph stating what this template produces and its reuse scope.

**16.** Write the `## Variables Table` section: markdown table with columns name, type, required, default, description.

**17.** Write the `## Template Body` section: the parameterized prompt text using declared variables only.

**18.** Verify the template body: every `{{var}}` used in the body MUST appear in the variables list.

**19.** Verify the variables list: every variable declared MUST appear at least once in the template body.

**20.** Write the `## Quality Gates` section: list which H01-H08 gates this template satisfies and how.

**21.** Write the `## Examples` section: one filled example showing a real variable substitution and the rendered output.

---

## Phase 3: VALIDATE

**22.** Check H01: id matches pattern `^p03_pt_[a-z][a-z0-9_]+$`.

**23.** Check H02: all frontmatter required fields present (id, kind, title, variables, quality).

**24.** Check H03: no undeclared variables in template body.

**25.** Check H04: no declared variables missing from template body.

**26.** Check H05: file size does not exceed 8192 bytes.

**27.** Check H06: variable_syntax is either `mustache` or `bracket`.

**28.** Check H07: every variable has name, type, required, description fields.

**29.** Check H08: template body is non-empty and contains at least one `{{variable}}`.

**30.** If any HARD gate fails: fix the violation and re-run the failing gate check.

**31.** Score SOFT gates S01-S10 and record the numeric score in the `quality` field.

**32.** Set `updated` to today's date.

**33.** Deliver the completed artifact.

---

## brain_query [IF MCP]

If the Brain MCP is available, query before Phase 2:
```
brain_query("prompt template examples {{topic}}")
brain_query("P03 prompt_template domain {{domain}}")
```
Use results to inform variable naming conventions and template body patterns.
