---
kind: instruction
id: bld_instruction_agent_computer_interface
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for agent_computer_interface
quality: 8.9
title: "Instruction Agent Computer Interface"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_computer_interface, builder, instruction]
tldr: "Step-by-step production process for agent_computer_interface"
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH
1. Analyze OS-level accessibility APIs (X11, Wayland, or Windows UI Automation).
2. Map terminal escape sequences and ANSI/Xterm capability sets.
3. Define UI tree traversal logic for DOM and desktop GUI automation.
4. Evaluate latency constraints for real-time screen/input feedback loops.
5. Audit security boundaries for sandboxed agent execution environments.
6. Catalog standard input/output (STDIN/STDOUT) stream protocols.

## Phase 2: COMPOSE
1. Initialize document structure based on bld_output_template_agent_computer_interface.md.
2. Define the CALL function signature for interface invocation.
3. Map input primitives (keystrokes, clicks) to bld_schema_agent_computer_interface.md types.
4. Detail the state machine for terminal and GUI session management.
5. Implement error-handling protocols for unresponsive UI elements.
6. Integrate observation feedback loops (OCR/DOM parsing) per SCHEMA.md.
7. Define the protocol for agent-to-host command serialization.
8. Apply formatting constraints from OUTPUT_TEMPLATE.md.
9. Finalize the interaction handshake logic per bld_quality_gate_agent_computer_interface.md H-gates.

## Phase 3: VALIDATE
- [ ] Verify all CALL primitives map to valid bld_schema_agent_computer_interface.md definitions.
- [ ] Confirm terminal escape sequence compatibility.
- [ ] Validate sandboxing and security constraints for agent execution.
- [ ] Ensure all HARD gates pass per bld_quality_gate_agent_computer_interface.md.
- [ ] Confirm quality: null (never self-score).
- [ ] Run: python _tools/cex_hooks.py validate {path}
