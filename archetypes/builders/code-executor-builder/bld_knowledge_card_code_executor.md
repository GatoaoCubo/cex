---
kind: knowledge_card
id: bld_knowledge_card_code_executor
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for code_executor production — sandboxed code execution
sources: Docker security docs, E2B documentation, WASM sandbox specs, OpenAI Code Interpreter docs
---

# Domain Knowledge: code_executor
## Executive Summary
Code executors are sandboxed environments where LLM-generated code runs safely. They isolate untrusted code from the host system using containers, VMs, WASM, or process-level sandboxing. The code_executor artifact specifies which languages can run, how code is isolated, what resources are available, and when execution is killed (timeout).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Sandbox types | docker, e2b, wasm, vm, process |
| Isolation | Code cannot access host filesystem, network, or processes unless explicitly allowed |
| Timeout | Mandatory — prevents infinite loops and resource exhaustion |
| State | Ephemeral by default; persistent_session = true for multi-turn |
## Implementation Mapping
| Implementation | Sandbox | Languages | Session | Network |
|---------------|---------|-----------|---------|---------|
| OpenAI Code Interpreter | container | Python | persistent | blocked |
| E2B Sandbox | cloud VM | Python, Node, Bash + | persistent | allowed |
| AutoGen Docker | docker | any (configurable) | ephemeral | configurable |
| Modal | container/VM | Python | ephemeral | allowed |
| Pyodide/WASM | wasm | Python | ephemeral | blocked |
## Patterns
- **Ephemeral sandbox**: new container per execution — maximum isolation, no state leaks
- **Persistent session**: state carries across calls — useful for multi-step data analysis
- **Resource caps**: always set CPU, memory, disk, timeout — prevent DoS from LLM-generated code
- **Allowlist languages**: explicitly list supported languages — never "any language"
| Pattern | Example | When to use |
|---------|---------|-------------|
| Ephemeral Docker | New container per run, destroyed after | One-shot code execution, max isolation |
| Persistent E2B | Cloud sandbox with session state | Multi-turn data analysis, notebook-style |
| WASM | In-browser execution, no system access | Lightweight, client-side execution |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No timeout | Infinite loop exhausts resources, blocks execution queue |
| Bare-metal execution | No isolation — code can access host, exfiltrate data |
| No resource limits | Code can consume all CPU/memory, crash host |
| Implicit network access | Code can exfiltrate data or make unauthorized API calls |
| No language allowlist | LLM may generate code in unsupported language, fail silently |
| Persistent state without cleanup | State accumulates, disk fills, secrets persist |
## Application
1. Define use case: what kind of code will run here?
2. Choose sandbox type based on isolation needs
3. List supported languages with versions
4. Set timeout (30s default, adjust for use case)
5. Set resource limits: CPU, memory, disk
6. Decide network policy: blocked unless explicitly needed
7. Decide session model: ephemeral (default) or persistent
## References
- Docker: container security best practices
- E2B: cloud sandbox documentation
- OpenAI: Code Interpreter documentation
- WASM: WebAssembly sandboxing specification
- Modal: serverless execution documentation
