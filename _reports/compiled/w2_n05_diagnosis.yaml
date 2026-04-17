id: w2_n05_structural_diagnosis
kind: audit_log
pillar: P11
title: SELFHEAL W2 -- N05 Structural Diagnosis
version: 1.0.0
created: 2026-04-15
updated: 2026-04-15
author: n05_operations
quality: null
mission: SELFHEAL
wave: 2
nucleus: n05
scope: Full structural audit of previously unscanned zones (N07_admin, P02-P12, P01/library/kind fixes). Based on W1 findings
  from N01 (semantic) and N04 (quality inventory).
remediation_completed: ''
quality_missing_frontmatter_fix_12_files: 'All 12 P01/library/kind files with missing id/kind/pillar/quality keys were repaired.


  | file | old_issue | fix_applied |

  |------|-----------|-------------|

  | kc_agent_name_service_record.md | missing id+pillar+quality | full frontmatter: P04, knowledge_card, quality:null |

  | kc_capability_registry.md | missing id+pillar+quality | full frontmatter: P08, knowledge_card, quality:null |

  | kc_case_study.md | missing id+kind+pillar+quality | full frontmatter: P05, knowledge_card, quality:null |

  | kc_course_module.md | missing id+pillar+quality | full frontmatter: P05, knowledge_card, quality:null |

  | kc_data_residency.md | missing id+pillar+quality | full frontmatter: P09, knowledge_card, quality:null |

  | kc_dataset_card.md | missing id+kind+pillar+quality | full frontmatter: P01, knowledge_card, quality:null |

  | kc_govtech_vertical.md | missing id+kind+pillar+quality | full frontmatter: P01, knowledge_card, quality:null |

  | kc_gpai_technical_doc.md | missing id+kind+pillar+quality | full frontmatter: P11, knowledge_card, quality:null |

  | kc_kubernetes_ai_requirement.md | missing pillar+quality | full frontmatter: P09, knowledge_card, quality:null |

  | kc_mcp_app_extension.md | missing id+pillar+quality | full frontmatter: P04, knowledge_card, quality:null |

  | kc_memory_benchmark.md | missing id+kind+pillar+quality | full frontmatter: P07, knowledge_card, quality:null |

  | kc_prosody_config.md | missing id+kind+pillar+quality | full frontmatter: P09, knowledge_card, quality:null |


  Result: 12/12 fixed. All files now have id, kind, pillar, quality: null.'
zone_scan_results: ''
n07_admin_41_files_first_time_scan:
- 'defects: 1'
- 'N07_admin/README.md: no_frontmatter'
- 'classification: doc_not_artifact (intentional, exemption applies)'
- 'action: skip'
p02_p12_pillars_318_files_unscanned_in_w1:
- 'total: 318'
- 'no_frontmatter: 11'
- 9 README.md files (doc_not_artifact, intentional)
- '2 non-README files: P11_feedback/examples/p11_content_monetization_faz_um_crm_pra_pet_shop.md (missing quality key only),
  P12_orchestration/README.md (doc)'
- 'quality_missing: 0 (all structured files have quality key)'
- 'quality_null: 3'
- P05_output/examples/landing_page_petshop_crm.md
- P09_config/p09_cb_template.md
- P09_config/p09_ec_template.md
p11_feedback_examples_p11_content_monetization_faz_um_crm_pra_pet_shop_md:
- has id/kind/pillar but missing quality key
- 'priority: low (example file, non-blocking)'
- 'recommended_action: add quality: null in W3'
builder_health_cex_doctor: '| metric | value |

  |--------|-------|

  | builders_total | 258 |

  | PASS | 190 |

  | WARN | 63 |

  | FAIL | 5 |

  | avg_density | 0.90 |

  | oversized_files | 47 |'
5_fail_builders_density_size_violations: '| builder | issues |

  |---------|--------|

  | agent-grounding-record-builder | density <0.78 (3 files), size >6144B (2 files) |

  | agent-name-service-record-builder | density <0.78 (3 files), size >6144B (2 files) |

  | conformity-assessment-builder | density <0.78 (3 files), size >6144B (2 files) |

  | contributor-guide-builder | density <0.78 (3 files), size >6144B (1 file) |

  | webinar-script-builder | density <0.78 (3 files), size >6144B (1 file) |


  Pattern: All 5 FAILs share the same issue -- oversized ISOs with low content density.

  Root cause: These builders were scaffolded with verbose boilerplate that inflates byte count

  but adds no structured data value. Density threshold is 0.78; these range 0.67-0.77.


  Recommended W3 action: N03 density-repair pass on these 5 builders.'
63_warn_builders:
- 'Primary issue: size >6144B (47 oversized files) or density 0.78-0.84 borderline'
- Not blocking -- WARN does not prevent 8F pipeline execution
- 'Recommended: periodic compaction pass, lower priority than FAIL'
system_test_results: '| test | result | detail |

  |------|--------|--------|

  | doctor:zero_warn | FAIL | 63 WARN (non-blocking) |

  | doctor:zero_fail | FAIL | 5 FAIL builders (N03 repair needed) |

  | quality:zero_null | FAIL | 22 quality:null (awaiting peer review, expected) |

  | e2e:runs | FAIL | cex_e2e_test.py environment error (not a structural defect) |

  | git:clean | FAIL | 45 dirty files (untracked reports/handoffs, expected during SELFHEAL) |

  | all other | PASS | 53/58 pass |'
coverage_map_post_w1_w2: '| zone | files | W1 scanned | W2 scanned | total_coverage |

  |------|-------|------------|------------|----------------|

  | N01-N06 | ~900 | 500 | 0 | 56% |

  | N07_admin | 41 | 0 | 41 | 100% |

  | P01/library/kind | 131 | 131 | 12 (fixes) | 100% |

  | P01 (rest) | ~518 | ~369 | 0 | ~71% |

  | P02-P12 | 318 | 0 | 318 | 100% |

  | archetypes/builders | 3354 | 0 | 258 (doctor) | builder-level |'
recommended_w3_focus_n03: "1. Density-repair -- 5 FAIL builders (agent-grounding-record, agent-name-service-record,\n   conformity-assessment,\
  \ contributor-guide, webinar-script)\n2. quality_null fill -- 22 remaining quality:null files need peer-review scoring\n\
  3. N01-N06 remainder -- 400 unscanned N01-N06 files (N01 W1 only scanned 500 total)\n4. P01 remainder -- ~518 P01 files\
  \ beyond library/kind not yet covered\n5. P11 example fix -- add quality: null to p11_content_monetization_faz_um_crm_pra_pet_shop.md"
summary: '| category | count | action |

  |----------|-------|--------|

  | quality_missing fixed | 12 | DONE |

  | FAIL builders | 5 | W3 N03 density repair |

  | WARN builders | 63 | low priority compaction |

  | quality_null (expected) | 22 | peer review queue |

  | doc_not_artifact | 10 | exemption applied |

  | P11 example missing quality | 1 | W3 minor fix |

  | coverage gaps remaining | ~900 files | W3 extended scan |'
