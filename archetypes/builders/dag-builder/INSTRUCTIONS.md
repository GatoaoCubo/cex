---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for dag
pattern: analyze -> compose -> validate
---

# Instructions: How to Produce a dag

## Phase 1: ANALYZE
1. Identify the pipeline or mission that needs dependency modeling
2. List all tasks (nodes) that make up the pipeline
3. Assign each node a unique id and descriptive label
4. Determine dependencies: which tasks must finish before others can start
5. Check for cycles: if A depends on B and B depends on A, redesign
6. Identify entry points (no incoming edges) and terminal points (no outgoing edges)
7. Check brain_query [IF MCP] for existing DAGs to avoid duplicates

## Phase 2: COMPOSE
1. Read SCHEMA.md first
2. Use OUTPUT_TEMPLATE.md as a direct derivative of SCHEMA.md
3. Set filename as `p12_dag_{pipeline_slug}.yaml`
4. Fill all required fields exactly once
5. Set quality: null (NEVER self-score)
6. Write Nodes section with id, label, satellite for each task
7. Write Edges section with from/to pairs for each dependency
8. Compute execution_order as topologically sorted waves
9. Add optional fields only if they are compact and relevant
10. Omit absent optional fields instead of using placeholders

## Phase 3: VALIDATE
1. Check HARD gates in QUALITY_GATES.md
2. Verify YAML parses correctly
3. Verify the graph is acyclic (no circular dependencies)
4. Verify every edge references existing node ids
5. Cross-check filename matches id pattern `p12_dag_*`
6. Confirm the artifact is static spec and not drifting into workflow scope
7. Confirm the DAG remains under 3072 bytes
8. If validation fails, revise in the same pass before output
