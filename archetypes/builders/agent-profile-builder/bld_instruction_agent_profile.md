---
kind: instruction
id: bld_instruction_agent_profile
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for agent_profile (persona + identity vectors)
quality: 9.0
title: "Instruction Agent Profile"
version: "1.1.0"
author: n03_builder
tags: [agent_profile, builder, instruction, persona, P02]
keywords: [persona, identity_vector, role_alignment, behavioral_constraint, voice, BECOME]
triggers: ["create agent persona", "define agent identity", "scaffold p02_ap_* profile"]
tldr: "3-phase pipeline (research -> compose -> validate) for producing p02_ap_{slug}.md agent_profile artifacts with 7-trait persona, 3 identity vectors, and role boundaries."
domain: "agent_profile construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Instructions: How to Produce an agent_profile

## Phase 1: RESEARCH
1. Identify the agent's primary role: operator (executes tasks), analyst (interprets data), or automaton (scheduled/reactive). Exactly one.
2. Read `bld_knowledge_card_agent_profile.md` for persona theory (Big Five, FIPA ACL, ISO/IEC 23894 trust attributes).
3. Extract 3 identity vectors: (a) domain of authority, (b) voice register, (c) decision latency (instant/deliberative).
4. Map agent to its consumer: which agent_card or system_prompt will reference this profile? Profile lives upstream of runtime.
5. Scan existing `p02_ap_*.md` artifacts in the repo — avoid trait duplication across sibling profiles.
6. Record 3-5 behavioral constraints (refusals, scope limits) sourced from domain regulation, not invented.

## Phase 2: COMPOSE
1. Read `bld_schema_agent_profile.md` — single source of truth for frontmatter and body structure.
2. Fill frontmatter: id (pattern `p02_ap_[a-z][a-z0-9_]+`), kind=`agent_profile`, pillar=`P02`, agent_type (operator|analyst|automaton), expertise (3-7 items), status=`active`, quality=null.
3. Open `bld_output_template_agent_profile.md` and fill every `{{var}}` — no placeholders leak to output.
4. Write body sections in order: Overview -> Identity Vectors -> Capabilities -> Constraints -> Collaborators -> Compliance.
5. Identity Vectors: write each as `vector: value // rationale` (e.g., `voice: terse_technical // domain requires precision`).
6. Capabilities: 3-7 action verbs in present tense ("diagnoses", "routes", "refuses"). NO implementation detail — that belongs in agent_card (P08).
7. Constraints: use ALWAYS / NEVER / IF-THEN form. At least 3 required. Each cites source (policy, regulation, internal rule).
8. Collaborators: name sibling profiles by id (`p02_ap_triage_nurse`), not by vague role.
9. Keep each bullet <= 100 chars. Body total between 800 and 4096 bytes.
10. NEVER embed system_prompt text, runtime instructions, or code — those are P03 and P04 artifacts.

## Phase 3: VALIDATE
- [ ] HARD: YAML parses; id matches `^p02_ap_[a-z][a-z0-9_]+$`; kind=`agent_profile`; quality=null.
- [ ] HARD: agent_type in {operator, analyst, automaton}; status in {active, inactive, pending}; expertise is non-empty list.
- [ ] HARD: Body has all 6 sections; >= 3 constraints in ALWAYS/NEVER/IF-THEN form; 3 identity vectors present.
- [ ] HARD: No system_prompt content, no code blocks with runtime logic, no internal paths.
- [ ] SOFT: tldr contains concrete role + domain, not generic phrasing; each capability is a single verb phrase.
- [ ] SOFT: Collaborators reference real sibling agent_profile ids; density_score >= 0.85.
- [ ] Boundary: Is this truly persona/identity, or should it be agent (P02), agent_card (P08), or system_prompt (P03)? If ambiguous, reclassify.
- [ ] Run `python _tools/cex_score.py --apply <path>` and verify score >= 8.0 before handoff to peer review.
- [ ] On HARD fail: fix and re-validate. On SOFT < 8.0: replace prose with tables, tighten vectors, cite sources.
