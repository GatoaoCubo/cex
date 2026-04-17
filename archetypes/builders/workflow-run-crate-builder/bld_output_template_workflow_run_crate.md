---
kind: output_template
id: bld_output_template_workflow_run_crate
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for workflow_run_crate production
quality: 8.9
title: "Output Template Workflow Run Crate"
version: "1.0.0"
author: n04_wave7
tags: [workflow_run_crate, builder, output_template, RO-Crate, CreateAction, provenance-graph, ORCID]
tldr: "Template with vars for workflow_run_crate production"
domain: "workflow_run_crate construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p10_wrc_{{name}}.md
kind: workflow_run_crate
pillar: P10
title: "{{workflow_name}} Run {{run_id}}"
version: "1.0.0"
workflow_language: "{{workflow_language}}"
run_id: "{{run_id}}"
agent_orcid: "{{orcid_url}}"
input_count: {{input_count}}
output_count: {{output_count}}
start_time: "{{start_time}}"
end_time: "{{end_time}}"
domain: "{{scientific_domain}}"
quality: null
tags: [RO-Crate, workflow-run, research-object, provenance-graph, ORCID, {{domain_tag}}]
tldr: "{{workflow_name}} execution provenance for run {{run_id}} by {{researcher_name}}"
author: "{{author}}"
created: "{{date}}"
updated: "{{date}}"
---
```

## RO-Crate Metadata (ro-crate-metadata.json)

```json
{
  "@context": [
    "https://www.researchobject.org/ro-crate/1.2/context",
    "https://w3id.org/ro/terms/workflow-run"
  ],
  "@graph": [
    {
      "@type": "CreativeWork",
      "@id": "ro-crate-metadata.json",
      "about": {"@id": "./"},
      "conformsTo": [
        {"@id": "https://w3id.org/ro/crate/1.2"},
        {"@id": "https://w3id.org/workflowhub/workflow-ro-crate/1.0"}
      ]
    },
    {
      "@type": "Dataset",
      "@id": "./",
      "name": "{{workflow_name}} Run {{run_id}}",
      "description": "{{description}}",
      "datePublished": "{{date}}",
      "license": {"@id": "{{license_url}}"},
      "hasPart": [
        {"@id": "{{workflow_file}}"},
        {"@id": "{{run_id}}-provenance.json"}
      ]
    },
    {
      "@type": ["File", "SoftwareSourceCode", "ComputationalWorkflow"],
      "@id": "{{workflow_file}}",
      "name": "{{workflow_name}}",
      "programmingLanguage": {"@id": "#{{workflow_language_id}}"},
      "url": "{{workflow_url}}",
      "version": "{{workflow_version}}"
    },
    {
      "@type": "CreateAction",
      "@id": "#run-{{run_id}}",
      "name": "Run of {{workflow_name}}",
      "startTime": "{{start_time}}",
      "endTime": "{{end_time}}",
      "instrument": {"@id": "{{workflow_file}}"},
      "object": [{"@id": "{{input_dataset_id}}"}],
      "result": [{"@id": "{{output_dataset_id}}"}],
      "agent": {"@id": "{{orcid_url}}"}
    },
    {
      "@type": "Person",
      "@id": "{{orcid_url}}",
      "name": "{{researcher_name}}",
      "affiliation": {"@id": "#{{institution_id}}"}
    },
    {
      "@type": "Dataset",
      "@id": "{{input_dataset_id}}",
      "name": "{{input_name}}",
      "encodingFormat": "{{input_mime}}",
      "contentSize": "{{input_bytes}}",
      "sha256": "{{input_sha256}}",
      "license": {"@id": "{{input_license}}"}
    },
    {
      "@type": "Dataset",
      "@id": "{{output_dataset_id}}",
      "name": "{{output_name}}",
      "encodingFormat": "{{output_mime}}",
      "contentSize": "{{output_bytes}}",
      "sha256": "{{output_sha256}}",
      "dateCreated": "{{end_time}}"
    }
  ]
}
```

## FAIR Signposting
```
Link: <{{crate_url}}>; rel="cite-as"
Link: <{{metadata_url}}>; rel="describedby"; type="application/ld+json"
Link: <{{license_url}}>; rel="license"
```
