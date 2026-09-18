# AI Engineering Assistant

> A controlled AI collaboration method for large, long-running, and high-risk engineering projects.
>
> See the [Chinese edition](README.md) in the bilingual README.

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
