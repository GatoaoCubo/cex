---
kind: instruction
id: bld_instruction_memory_type
pillar: P03
llm_function: PRODUCE
---

# Instruction: Build a memory_type artifact

## Phase 1: Classify
1. Identify which of the 4 memory types this artifact defines
2. Determine the correct decay rate (0.0 for corrections, up to 0.05 for context)
3. Decide if this type survives context compression

## Phase 2: Define
4. Write a clear definition of what observations belong to this type
5. Provide the decay formula and rationale
6. Specify storage location and format rules

## Phase 3: Exemplify
7. Provide 3+ concrete examples of observations that match this type
8. Provide 2+ anti-examples (observations that seem like this type but are not)

## Phase 4: Integrate
9. Document how cex_memory_types.py should classify this type
10. Specify interaction with cex_memory_age.py freshness tags
