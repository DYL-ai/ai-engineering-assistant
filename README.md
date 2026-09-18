# AI 工程助手 / AI Engineering Assistant

> 面向大型、长期和高风险项目的可控 AI 协作方法。
> A controlled AI collaboration method for large, long-running, and high-risk engineering projects.

[中文](#中文) · [English](#english)

## 中文

### 项目简介

**AI 工程助手**将 Codex、Claude Code、subagent、MCP 和其他工程工具组织成一套可复用的工作系统。它把一次任务从“让 Agent 写代码”提升为完整工程闭环：明确目标，装配上下文，划分职责，建立基线，执行最小变更，独立验证，保留人工决策，准备回滚，并将结论沉淀为下一次可以复用的知识。

它适合处理跨会话、跨仓库、跨系统的长期任务，也适合线上排障、部署变更、数据库操作、权限治理和复杂数据工程。Skill 会根据用户偏好和真实案例逐步改进，但不会绕过授权、审计、验证或回滚要求。

### 核心闭环

| 阶段 | 关键问题 | 主要产物 |
| --- | --- | --- |
| 目标 | 要解决什么，什么不在范围内？ | 任务目标与非目标 |
| 上下文 | 当前版本、状态和基线是什么？ | 代码、配置、日志、数据和部署快照 |
| 拆解 | 哪些工作可以独立推进？ | 任务契约与工作包 |
| 分工 | 哪个 Agent 负责调查、实现、验证或运维？ | 角色、边界和停止条件 |
| 执行 | 如何用最小范围改变系统？ | diff、配置变更或操作记录 |
| 证据 | 如何证明结果有效？ | 测试、回放、对账、日志和指标 |
| 决策 | 是否交付、灰度、暂停或回滚？ | 人工决策与审计记录 |
| 沉淀 | 下次如何更快、更准地处理？ | memory、FAQ、案例、规则和回归样本 |

### Agent 角色

- **主 Agent**：维护目标、上下文和关键路径，整合结果并做最终交付判断。
- **Explorer**：只读调查代码、日志、数据库和资料，输出事实、假设与证据。
- **Implementer**：只在契约指定范围内修改，实现最小变更并提供 diff 和测试结果。
- **Verifier**：独立执行测试、回放、对账和反例检查，不修改实现来让测试通过。
- **Operator**：处理权限、镜像、部署、灰度、监控和回滚相关工作。

每个工作包都应明确输入、输出、可读范围、可写范围、禁止动作、验证方式和停止条件。同一文件不由多个 Agent 同时写入。

### 风险分级与人工门禁

- `L0`：只读查询或事实整理。
- `L1`：本地、可逆的代码或文档修改。
- `L2`：批量操作或外部副作用，需要先展示任务契约和基线。
- `L3`：生产、秘密、权限、删除、数据库写入或 rollout，必须记录批准人、批准时间、批准范围、失效条件、观察窗口和回滚路径。

Skill 的存在不代表获得生产或外部系统授权。测试通过也不能替代真实业务验证。

### 自适应机制

AI 工程助手支持受控的案例学习：

1. 每次适用任务结束后记录任务类型、采用模式、用户修正、失败原因、有效做法和结果证据。
2. 用户明确表达的长期偏好可以直接进入个人档案；单次行为只能作为候选规则。
3. 同一模式至少重复三次且没有反例，才升级为适配规则。
4. 每条规则保留来源、适用范围、创建日期、复审日期、证据和反例。
5. 规则过期、被用户否定或出现反例时，可以降级或撤销。
6. 生产授权、权限、秘密处理、数据保留、核心验收和回滚要求不得被静默放宽。

可使用以下脚本追加经过脱敏的案例记录：

```bash
python3 scripts/record_case.py \
  --skill-dir . \
  --task "任务描述" \
  --mode "任务模式" \
  --practice "采用做法" \
  --evidence "结果证据"
```

脚本只写入本地 `references/learning-log.md`，不连接外部服务，也不读取秘密。

### 适用场景

- AI 网关、模型路由、fallback、协议转换和账号池治理。
- Claude Code、Codex、PTY、容器、代理和运行时接入。
- Kubernetes、数据库、日志、监控、部署和线上故障排查。
- 爬虫、动态页面识别、数据质量和长周期数据任务。
- Agent-Memory、Wiki、日报和团队知识管理。
- 任何需要跨会话、跨仓库或跨 Agent 协作的大型工程。

遇到新的领域时，保留任务契约、风险分级、证据验收和知识回灌，替换领域术语、工具和指标，不强行套用原项目实现细节。

### 安装与使用

将仓库目录放入 Codex 的 Skill 目录：

```text
$CODEX_HOME/skills/ai-engineering-assistant
```

未设置 `CODEX_HOME` 时，通常使用：

```text
~/.codex/skills/ai-engineering-assistant
```

在 Codex 中调用：

```text
使用 $ai-engineering-assistant，处理这个长期工程任务。
```

简单问答、只读事实查询和明确的一步修改不需要强行使用完整流程。

### 目录结构

```text
.
├── SKILL.md                         # Skill 入口与核心工作流
├── agents/openai.yaml               # Codex 界面元数据
├── references/
│   ├── task-contract.md             # 通用任务契约
│   ├── agent-orchestration.md       # Agent 编排与边界
│   ├── evidence-acceptance.md       # 证据与验收
│   ├── evolution-policy.md          # 自适应与晋升规则
│   ├── personal-profile.md          # 可选个人偏好
│   ├── adapted-rules.md             # 已验证适配规则
│   ├── casebook.md                  # 案例档案
│   └── learning-log.md              # 学习日志
└── scripts/record_case.py           # 脱敏案例记录脚本
```

## English

### Overview

**AI Engineering Assistant** organizes Codex, Claude Code, subagents, MCP, and engineering tools into a reusable operating system for complex work. It turns a task from “ask an agent to write code” into a complete engineering loop: define the objective, assemble context, assign responsibilities, establish a baseline, make the smallest safe change, verify independently, retain human decision gates, prepare rollback, and feed the result back into reusable knowledge.

It is designed for work that spans sessions, repositories, or systems, including incident response, deployment changes, database operations, access governance, and data engineering. The skill can improve from user preferences and real cases, while preserving authorization, audit, verification, and rollback requirements.

### Core loop

| Stage | Key question | Primary output |
| --- | --- | --- |
| Objective | What must be solved, and what is out of scope? | Goal and non-goals |
| Context | What are the current version, state, and baseline? | Code, config, logs, data, and deployment snapshot |
| Decomposition | Which pieces can proceed independently? | Task contract and work packages |
| Roles | Who investigates, implements, verifies, or operates? | Roles, boundaries, and stop conditions |
| Execution | How can the system change within the smallest scope? | Diff, config change, or operation record |
| Evidence | How will the result be proven? | Tests, replay, reconciliation, logs, and metrics |
| Decision | Should we deliver, canary, pause, or roll back? | Human decision and audit record |
| Learning | How can the next task become faster and more reliable? | Memory, FAQ, cases, rules, and regression samples |

### Agent roles

- **Primary Agent**: owns the objective, context, critical path, integration, and final delivery decision.
- **Explorer**: performs read-only investigation of code, logs, databases, and documentation; reports facts, assumptions, and evidence.
- **Implementer**: changes only the scope defined by the contract; produces the smallest implementation, diff, and tests.
- **Verifier**: independently runs tests, replay, reconciliation, and counterexample checks; it does not alter the implementation to make tests pass.
- **Operator**: handles permissions, images, deployment, canary rollout, monitoring, and rollback.

Every work package should define its inputs, outputs, readable and writable scope, forbidden actions, verification method, and stop condition. Multiple Agents should not write the same file concurrently.

### Risk levels and human gates

- `L0`: read-only queries and fact gathering.
- `L1`: local, reversible code or documentation changes.
- `L2`: batch operations or external side effects; show the task contract and baseline first.
- `L3`: production, secrets, permissions, deletion, database writes, or rollout; record the approver, approval time, approved scope, expiry or stop condition, observation window, and rollback path.

The presence of this skill does not grant authorization to change production or external systems. Passing tests does not prove real business effectiveness.

### Adaptive learning

AI Engineering Assistant supports bounded, traceable learning:

1. Record the task type, selected mode, user corrections, failure causes, effective practices, and evidence after each applicable task.
2. Explicit long-term preferences may enter the personal profile; a one-off behavior remains a candidate rule.
3. Promote a pattern only after it appears at least three times without counterexamples.
4. Keep the source, scope, creation date, review date, evidence, and counterexamples for every rule.
5. Demote or revoke rules when they expire, are rejected by the user, or meet a counterexample.
6. Never silently relax production authorization, access control, secret handling, data retention, acceptance criteria, or rollback requirements.

Use the following helper to append a redacted case record:

```bash
python3 scripts/record_case.py \
  --skill-dir . \
  --task "task description" \
  --mode "task mode" \
  --practice "practice used" \
  --evidence "result evidence"
```

The script writes only to the local `references/learning-log.md`. It does not connect to external services or read secrets.

### Use cases

- AI gateways, model routing, fallback, protocol translation, and account-pool governance.
- Claude Code, Codex, PTY, containers, proxies, and runtime integrations.
- Kubernetes, databases, logs, observability, deployment, and incident response.
- Crawlers, dynamic-page recognition, data quality, and long-running data workflows.
- Agent memory, wikis, daily reports, and team knowledge management.
- Any large engineering effort that spans sessions, repositories, or Agents.

For a new domain, keep the task contract, risk levels, evidence acceptance, and knowledge feedback loop. Replace domain terminology, tools, and metrics instead of forcing the implementation details of an existing project.

### Installation and usage

Place the repository directory in the Codex Skill directory:

```text
$CODEX_HOME/skills/ai-engineering-assistant
```

If `CODEX_HOME` is not set, the usual location is:

```text
~/.codex/skills/ai-engineering-assistant
```

Invoke it in Codex with:

```text
Use $ai-engineering-assistant for this long-running engineering task.
```

Simple questions, read-only fact lookups, and explicit one-step edits do not need the full workflow.

### Repository layout

```text
.
├── SKILL.md                         # Skill entrypoint and core workflow
├── agents/openai.yaml               # Codex UI metadata
├── references/
│   ├── task-contract.md             # Generic task contract
│   ├── agent-orchestration.md       # Agent roles and boundaries
│   ├── evidence-acceptance.md       # Evidence and acceptance
│   ├── evolution-policy.md          # Adaptation and promotion rules
│   ├── personal-profile.md          # Optional personal preferences
│   ├── adapted-rules.md             # Validated adaptation rules
│   ├── casebook.md                  # Case archive
│   └── learning-log.md              # Learning log
└── scripts/record_case.py           # Redacted case recorder
```
