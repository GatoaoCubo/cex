---  
id: p01_kc_system_testing_patterns  
kind: knowledge_card  
pillar: P01  
title: "System Testing Patterns"  
version: "1.0.0"  
created: "2023-10-15"  
updated: "2023-10-15"  
author: "knowledge-card-builder"  
domain: "Software Testing"  
quality: null  
tags: [system testing, software testing, testing patterns, QA]  
tldr: "Overview of systematic patterns applied in system testing to ensure quality and functionality."  
when_to_use: "Use during system test design or evaluation for improving quality assurance."  
keywords: [testing patterns, system QA, software testing]  
long_tails:  
  - "How to apply functional testing patterns in software QA?"  
  - "Examples of load testing tools in system testing."  
axioms:  
  - ALWAYS define clear system specifications before testing.  
linked_artifacts:  
  primary: null  
  related: []  
density_score: 0.85  
data_source: "https://example.com/system_testing_patterns"  
---  

## Quick Reference  
```yaml  
topic: System Testing Patterns  
scope: System testing for ensuring software quality  
owner: Testing Team  
criticality: medium  
```  

## Key Concepts  
- **Functional Testing**: Validates software against functional requirements.  
- **Load Testing**: Assesses software behavior under expected concurrent user load.  
- **Stress Testing**: Determines limits by pushing beyond normal operational capacity.  

## Strategy Phases  
1. **Identify Requirements**: Gather functional specifications and performance metrics.  
2. **Select Tools**: Choose appropriate testing tools (e.g., JMeter, Selenium).  
3. **Conduct Tests**: Execute tests and analyze results for compliance and performance.  

## Golden Rules  
- ALWAYS document test cases before execution.  
- NEVER ignore test failures; analyze and address them promptly.  
- IF system specifications change, THEN update test cases accordingly.  

## Flow  
```text  
[Input] -> [Identify Requirements] -> [Select Tools] -> [Conduct Tests] -> [Output]  
```  

## Comparativo  
| Aspect               | Functional Testing | Load Testing |  
|----------------------|--------------------|--------------|  
| Purpose              | Validate functionality | Performance under load |  
| Tools                | Selenium, QTP      | JMeter, LoadRunner |  
| Outcomes             | Pass/Fail          | Response times, throughput |  

## References  
- Source: https://example.com/system_testing_patterns