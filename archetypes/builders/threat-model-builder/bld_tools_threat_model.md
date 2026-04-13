---
kind: tools
id: bld_tools_threat_model
pillar: P04
llm_function: CALL
purpose: Tools available for threat_model production
quality: null
title: "Tools Threat Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [threat_model, builder, tools]
tldr: "Tools available for threat_model production"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Production Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| cex_compile.py | Compiles threat model components into executable format | During model deployment |  
| cex_score.py | Assigns risk scores based on threat likelihood and impact | Post-attack simulation |  
| cex_retriever.py | Fetches external data (e.g., CVEs, IoCs) for model enrichment | During model training |  
| cex_doctor.py | Diagnoses model inconsistencies or missing dependencies | Pre-deployment validation |  
| cex_exporter.py | Exports models to standard formats (e.g., JSON, XML) | For integration with third-party tools |  
| cex_analyzer.py | Analyzes model performance against real-world scenarios | Post-deployment monitoring |  

## Validation Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| val_checker.py | Validates model compliance with industry standards | Pre-deployment |  
| val_simulator.py | Simulates attack paths to test model accuracy | During testing |  
| val_reporter.py | Generates audit reports for stakeholders | Post-validation |  
| val_comparator.py | Compares model outputs against baseline benchmarks | Continuous improvement |  

## External References  
- MITRE ATT&CK Framework (threat taxonomy)  
- OpenVAS (vulnerability scanning integration)  
- NIST Cybersecurity Framework (compliance alignment)
