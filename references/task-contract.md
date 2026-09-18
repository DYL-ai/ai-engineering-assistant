# Generic Task Contract

For medium- and high-risk tasks, fill at least these fields before starting:

```yaml
task_id: ""
name: ""
owner: ""
date: ""
project: ""
version_or_baseline: ""
risk: L0  # L0 read-only, L1 local change, L2 batch/external side effect, L3 production/secret/delete/permission
goal: ""
non_goals: []
context: []
allowed_tools: []
forbidden_actions: []
success_criteria: []
failure_thresholds: []
rollback: ""
required_evidence: []
knowledge_sink: []
human_approval:
  required: false
  approver: ""
  approved_at: ""
  approved_scope: ""
  expiry_or_stop_condition: ""
  decision: "pending"  # pending, approved, rejected, revoked
```

## Risk levels

- `L0`: read-only queries, code review, and document organization.
- `L1`: local code, tests, documents, and low-impact configuration.
- `L2`: batch requests, remote writes, bulk database changes, and image pushes.
- `L3`: production rollout, secrets, permissions, data deletion, account state, and irreversible external side effects.

The higher the risk, the more important human gates, independent validation, audit records, and rollback evidence become.

For `L2` and `L3`, set `human_approval.required` to `true`. Enter remote writes, batch changes, or rollout only when `decision: approved` and the approved scope covers the current action.
