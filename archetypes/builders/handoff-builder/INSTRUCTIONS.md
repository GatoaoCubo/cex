---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for handoff
pattern: plan -> compose -> validate
---

# Instructions: How to Produce a handoff

## Phase 1: PLAN
1. Identify the satellite that will execute this work
2. Determine the mission name and scope of delegation
3. List specific tasks the satellite must perform
4. Define the scope fence: allowed paths and forbidden paths
5. Identify dependencies on other handoffs or artifacts
6. Select autonomy level: full, supervised, or assisted
7. Set quality target based on task criticality
8. Run brain_query [IF MCP] for existing handoffs to avoid duplicates

## Phase 2: COMPOSE
1. Read SCHEMA.md first
2. Use OUTPUT_TEMPLATE.md as a direct derivative of SCHEMA.md
3. Set filename as `p12_ho_{task_slug}.md`
4. Fill all required frontmatter fields exactly once
5. Set quality: null (NEVER self-score)
6. Write Context section with background and motivation
7. Write Tasks section with numbered specific actions
8. Write Scope Fence with SOMENTE and NAO TOQUE paths
9. Write Commit section with exact git commands
10. Write Signal section with completion mechanism
11. Add optional fields only if they are compact and relevant

## Phase 3: VALIDATE
1. Check HARD gates in QUALITY_GATES.md
2. Verify YAML frontmatter parses correctly
3. Verify all 5 body sections are present
4. Cross-check filename matches id pattern `p12_ho_*`
5. Confirm scope fence has both SOMENTE and NAO TOQUE
6. Confirm tasks are specific and actionable
7. Confirm the artifact is not drifting into action_prompt or dispatch_rule scope
8. Confirm the handoff remains under 4096 bytes
9. If validation fails, revise in the same pass before output
