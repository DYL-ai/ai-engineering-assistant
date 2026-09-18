# 通用任务契约

中高风险任务开始前，至少填写以下字段：

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

## 风险等级

- `L0`：只读查询、代码审查、资料整理。
- `L1`：本地代码、测试、文档和低影响配置。
- `L2`：批量请求、远程写入、数据库批量变更、镜像推送。
- `L3`：生产 rollout、秘密、权限、删除数据、账号状态和不可逆外部副作用。

风险越高，越需要人工门禁、独立验证、审计和回滚证据。

`L2`/`L3` 任务必须把 `human_approval.required` 设为 `true`。只有 `decision: approved` 且批准范围覆盖当前动作时，才能进入远程写入、批量变更或 rollout。
