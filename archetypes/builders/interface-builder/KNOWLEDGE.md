---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for interface production
sources: [API design principles, contract-first design, CEX integration layer]
---

# Domain Knowledge: interface

## Foundational Concept
Interfaces are bilateral contracts: both parties (provider and consumer) agree on
methods, input shapes, and output shapes. Rooted in interface-based programming
(Gamma et al. 1994 "Design Patterns"), API-first design, and contract-first
development. In CEX, interfaces sit in the spec layer of P06 — they define
integration points between agents, not data shapes or validation rules.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| OpenAPI 3.x | REST API contracts (paths, schemas, responses) | methods structure (name, input, output) |
| gRPC/Protobuf | Service definitions with typed RPC methods | Strongly typed method contracts |
| TypeScript interfaces | Structural type contracts between modules | bilateral type agreement |
| GraphQL Schema | Query/mutation contracts with typed fields | Method-level input/output contracts |
| Java Interfaces | Abstract method signatures for implementation | Method signature pattern |

## Key Patterns
- Interfaces are BILATERAL: both provider and consumer agree on the contract
- Interfaces define METHODS: named operations with typed input and output
- Interfaces are VERSIONED: semver, with backward_compatible flag
- Interfaces have DEPRECATION: planned sunset path for old methods
- Interfaces support MOCKING: test doubles derive from the interface
- Methods use TYPED IO: input and output are structured objects, not free text
- Interfaces are STATIC: they define what CAN happen, not what DID happen
- Boundary is CLEAR: interface defines shape, validator checks compliance

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| methods | Named operations with typed IO | OpenAPI paths |
| backward_compatible | Explicit compat flag for evolution | OpenAPI deprecation |
| mock | Test specification embedded in contract | OpenAPI examples |
| deprecation | Planned sunset with timeline | API versioning headers |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT interface |
|------|------------|----------------------|
| input_schema (P06) | Unilateral entry contract for data shape | Interfaces are bilateral — both parties agree |
| signal (P12) | Runtime event notification | Signals report what happened; interfaces define what CAN happen |
| validation_schema (P06) | Post-generation system contract | Applied silently by system; interfaces are explicit agreements |
| connector (P04) | Runtime service adapter | Connectors implement; interfaces specify |
| router (P02) | Routing rule for dispatch | Routers decide WHERE; interfaces define HOW |

## References
- Gamma et al. (1994) "Design Patterns" — interface segregation
- OpenAPI Specification: https://spec.openapis.org/oas/latest.html
- gRPC service definitions: https://grpc.io/docs/what-is-grpc/core-concepts/
- Contract-First API Design: https://swagger.io/resources/articles/adopting-an-api-first-approach/
