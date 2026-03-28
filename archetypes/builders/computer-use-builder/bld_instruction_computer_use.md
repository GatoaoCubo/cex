---
kind: instruction
id: bld_instruction_computer_use
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for computer_use
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a computer_use
## Phase 1: RESEARCH
1. Identify the target environment (desktop OS, browser, mobile app, terminal emulator)
2. Define screen resolution and coordinate space
3. List all actions the LLM needs (click, type, scroll, key_press, drag, screenshot)
4. Determine coordinate system (absolute from top-left, relative to element)
5. Define screenshot capture policy (before each action, on demand, continuous)
6. Identify safety constraints (no credential entry, sandbox only, restricted areas)
7. Check for existing computer_use artifacts to avoid duplicates
8. Confirm target slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Overview section: what this controls and the observe-act loop
5. Write Actions section: each action with parameters (coordinates, text, keys)
6. Write Coordinate System section: resolution, origin, format
7. Write Safety section: restrictions, sandboxing, credential policy
8. Verify body <= 2048 bytes
9. Verify id matches `^p04_cu_[a-z][a-z0-9_]+$`
10. Verify resolution is WxH format
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_cu_`
4. Confirm kind == computer_use
5. Confirm actions_supported is non-empty with valid action names
6. Confirm resolution is WxH format
7. Confirm safety_constraints present
8. HARD gates: frontmatter valid, id pattern, actions listed, resolution defined
9. SOFT gates: score against QUALITY_GATES.md
10. Cross-check: is this GUI control (not DOM manipulation)? Not a CLI? Not just vision?
