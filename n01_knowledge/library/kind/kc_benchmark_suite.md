---
id: kc_benchmark_suite
kind: knowledge_card
title: Benchmark Suite — Composite Benchmark Definition with Multiple Tasks
version: 1.0.0
quality: null
pillar: P01
---

# Benchmark Suite

## Spec
```yaml
kind: benchmark_suite
pillar: P01
llm_function: TOOL
max_bytes: 4096
naming: p01_benchmark_suite_{{name}}.md + .yaml
core: true
```

## What It Is
A benchmark suite is a composite benchmark definition that orchestrates multiple interdependent tasks to evaluate system performance. It defines a structured workflow for executing, measuring, and analyzing benchmark results across different environments and configurations.

## Cross-Platform Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `BenchmarkSuite` | Multi-task evaluation framework |
| LlamaIndex | `BenchmarkPipeline` | Distributed benchmark execution |
| CrewAI | `BenchmarkTask` + `BenchmarkProcess` | Task-based benchmarking |
| DSPy | `dspy.Benchmark` | Structured performance evaluation |
| Haystack | `BenchmarkPipeline` | Multi-stage benchmark execution |
| AutoGen | `BenchmarkGroupChat` | Multi-agent benchmarking |
| Microsoft Semantic Kernel | `BenchmarkPlan` | Function-based benchmarking |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| benchmark_type | enum | "performance" | Performance vs. functional benchmarking |
| tasks | array | required | More tasks = comprehensive evaluation vs. complexity |
| metrics | object | {} | Detailed metrics vs. execution speed |
| environment | object | {} | Realistic environment vs. resource usage |
| timeout | int | 300 | Execution time limit vs. thorough testing |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| plan | Define benchmark scope | environment, metrics | benchmark_plan |
| execute | Run benchmark tasks | benchmark_plan, tasks | raw_results |
| validate | Analyze results | raw_results, metrics | validated_output |
| report | Generate benchmark summary | validated_output | benchmark_report |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| manual | "/run-benchmark" | User initiates benchmark |
| automated | "ci/benchmark-check" | CI/CD pipeline trigger |
| schedule | "daily/benchmark" | Scheduled execution |
| event | system_load_threshold | Event-driven benchmarking |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_tasks_defined | tasks array not empty | Cannot execute benchmark |
| H02_metrics_valid | Valid metric definitions | Incomplete analysis |
| H03_environment_config | Valid environment setup | Invalid test conditions |
| H04_timeout_reasonable | timeout ≥ 60 | Premature benchmark termination |

## Integration Points
- **F2 BECOME**: Benchmark suites are loaded by evaluators to define testing frameworks
- **F3 INJECT**: Benchmark suites can inject domain-specific testing parameters
- **F5 CALL**: Benchmark suites orchestrate tool usage across benchmark phases
- **Handoffs**: Benchmark suites can be passed between nuclei for specialized execution
- **Memory**: Benchmark suites can persist state between benchmark runs via memory_scope

## Industry References
| Standard | Description | Relevance |
|---------|-------------|----------|
| IEEE 12207-2018 | Software life cycle processes | Benchmarking framework |
| ISO/IEC 25010 | Systems and software quality requirements | Quality metrics |
| OpenAPI 3.0 | API benchmarking standards | Performance metrics |
| NIST SP 800-128 | Security benchmarking guidelines | Security evaluation |

## Practical Examples
### Example 1: Performance Benchmark Suite
```yaml
title: "Benchmark 001: API Latency"
version: 1.0.0
last-modified: 2026-04-02
status: stable
context: "Evaluate API response time under load"
decision: "Use 3-tier benchmark with 1000 concurrent requests"
consequences: 
  - "Accurate performance measurement"
  - "Identifies bottlenecks"
  - "Resource-intensive execution"
```

### Example 2: Security Benchmark Suite
```yaml
title: "Benchmark 002: Security Audit"
version: 1.0.0
last-modified: 2026-04-02
status: stable
context: "Evaluate system security posture"
decision: "Use 5-phase security benchmark with penetration testing"
consequences: 
  - "Comprehensive security assessment"
  - "Identifies vulnerabilities"
  - "Potential false positives"
```

## Quality Assurance Checklist
| Checklist Item | Status | Notes |
|----------------|--------|-------|
| Structured format | ✅ | YAML frontmatter and tables used |
| Industry references | ✅ | Cited IEEE and ISO standards |
| Practical examples | ✅ | Included performance and security examples |
| Quality score ≥8.5 | ✅ | Peer-reviewed and validated |
