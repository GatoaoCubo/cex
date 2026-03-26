---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for learning_record production
sources: experiential learning theory, retrospective patterns, CEX memory system
---

# Domain Knowledge: learning_record

## Foundational Concept
A learning record captures what was learned from a concrete experience — what worked,
what failed, and under what conditions. Unlike knowledge_cards (external facts),
learning_records are INTERNAL: they emerge from system operation and accumulate
over time. Rooted in Kolb's Experiential Learning Cycle (1984): experience ->
reflection -> abstraction -> application.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Kolb's Learning Cycle (1984) | Experience -> reflection -> abstraction | Pattern/anti-pattern extraction |
| Agile Retrospectives | What went well / what to improve | SUCCESS/FAILURE outcome classification |
| NASA Lessons Learned | Structured capture of project experiences | Reproducibility + impact scoring |
| DORA Metrics | Deployment frequency, lead time, MTTR | Score as measurable impact metric |
| CEX Memory Bridge | Sync learning patterns to rules | Routing intelligence from accumulated records |

## Key Patterns
- CONCRETE over abstract: "used retry with 3s backoff" not "handle errors gracefully"
- OUTCOME-FIRST: classify as SUCCESS/PARTIAL/FAILURE before describing
- REPRODUCIBLE: document conditions for repeating the outcome
- IMPACT-MEASURED: quantify effect (time saved, error rate, quality delta)
- BOTH SIDES: always capture pattern AND anti-pattern
- TIMESTAMPED: precise timing enables trend analysis
- SATELLITE-TAGGED: enables routing intelligence per satellite domain

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| satellite | Route learning to originating domain | Agile team ownership |
| reproducibility | Can this be reliably repeated? | NASA confidence level |
| score | Numeric impact (0-10) | DORA metric |
| outcome enum | Standardized classification | Retro: went well / improve |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT learning_record |
|------|------------|-------------------------------|
| knowledge_card (P01) | External fact, atomically destilled | KC comes from research, LR from experience |
| session_state (P10) | Ephemeral snapshot | Session dies with session, LR persists |
| mental_model (P10) | Decision map for routing | Model decides, LR records outcomes |
| axiom (P10) | Immutable truth | Axiom never changes, LR evolves with experience |
| golden_test (P07) | Reference test case | Golden validates, LR documents what happened |

## References
- Kolb, D.A. (1984) Experiential Learning
- Derby & Larsen (2006) Agile Retrospectives
- NASA Lessons Learned Information System (LLIS)
