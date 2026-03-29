---
id: p12_sig_admin_task_complete
kind: signal
pillar: P12
---

# Signal Schema

| Field          | Type          | Required/Optional | Allowed Values/Notes                          |
|----------------|---------------|-------------------|------------------------------------------------|
| satellite      | string        | Required          | Lowercase slug representing emitting agent     |
| status         | string        | Required          | "complete", "error", "progress"               |
| quality_score  | float or null | Required          | Fixed null value for outputs                   |
| timestamp      | string        | Required          | ISO 8601 formatted datetime                    |
| task           | string        | Optional          | Short label of task related to signal          |
| artifacts      | array of strings | Optional       | Paths to relevant artifacts                    |
| artifacts_count| integer       | Optional          | Count of artifacts                             |
| commit_hash    | string        | Optional          | Git commit hash if applicable                  |
| error_code     | string        | Optional          | Short string detailing specific error          |
| message        | string        | Optional          | Brief description of signal context            |
| progress_pct   | integer       | Optional          | Progress percentage; used only if status=="progress" |

# Example Payloads

### Complete Signal
```json
{
  "satellite": "central_admin",
  "status": "complete",
  "quality_score": null,
  "timestamp": "2023-10-05T14:48:00Z",
  "task": "update_check",
  "artifacts": ["path/to/artifact1"],
  "artifacts_count": 1,
  "commit_hash": "abc123def"
}
```

### Error Signal
```json
{
  "satellite": "central_admin",
  "status": "error",
  "quality_score": null,
  "timestamp": "2023-10-05T14:50:00Z",
  "error_code": "update_fail",
  "message": "Failed to update configuration",
  "artifacts": ["path/to/logs"]
}
```

### Progress Signal
```json
{
  "satellite": "central_admin",
  "status": "progress",
  "quality_score": null,
  "timestamp": "2023-10-05T14:52:00Z",
  "task": "upgrade_process",
  "progress_pct": 45,
  "message": "Update nearly halfway through"
}
```

# Status Vocabulary

- **complete**: Indicates successful completion of the task.
- **error**: Represents a failure or issue that requires attention.
- **progress**: Conveys ongoing status, a snapshot of the current task stage when relevant.

# Optional Fields

- `task`: Identifies the task associated with the signal.
- `artifacts`: List of related output or log file paths.
- `artifacts_count`: Useful to quickly know how many artifacts were generated.
- `commit_hash`: Provides versioning information for the deployment or task.
- `error_code`: Helps classify errors for quick troubleshooting.
- `message`: Offers concise context or description of the signal.
- `progress_pct`: Specifies the current progress percentage of a task.

# Consumer Contract

- **MUST** handle fields: `satellite`, `status`, `quality_score`, `timestamp`.
- **MAY** process optional fields, ignoring them if not applicable or if data is absent.
- **MUST NOT** assume signal contains routing logic, instructions, or instructions for task completion.