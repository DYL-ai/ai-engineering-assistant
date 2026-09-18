---
name: ai-engineering-assistant
description: Organizes Codex, Claude Code, and other Agents into a controlled workflow for long-running, complex, or high-risk engineering work, with task contracts, context, role boundaries, evidence, rollback, knowledge feedback, and traceable adaptation.
metadata:
  short-description: Turn complex engineering work into a controlled, verifiable, reusable AI workflow
---

# AI Engineering Assistant

## When to use

Use this skill when one or more of the following apply:

- The work spans multiple sessions, repositories, or systems.
- Codex, Claude Code, subagents, MCP, or external tools must cooperate.
- The work involves production services, databases, accounts, permissions, secrets, batch operations, or deployment.
- Logs, code, data, and historical records must be used repeatedly for diagnosis or iteration.
- A one-off solution should become a reusable engineering method.

Use a lightweight approach for simple questions, read-only fact lookups, and explicit one-step edits.

## Core objective

Organize work into this loop:

`Objective → Context → Decomposition → Roles → Execution → Evidence → Decision → Rollback/Delivery → Knowledge Feedback`

People own objectives, boundaries, risk, trade-offs, and final approval. Agents investigate, implement, test, and organize evidence. Tools and process provide context, permissions, observability, and memory.

## Before starting

1. Classify the task: lightweight, standard, long-running project, production incident, or high-risk change.
2. Create a minimal task contract: objective, non-goals, version, risk level, allowed tools, success criteria, failure thresholds, and rollback method.
3. Assemble the minimum context package: code/config version, log or data samples, historical conclusions, current baseline, and known limitations.
4. Read personal preferences and approved adaptation rules:
   - [Personal profile](references/personal-profile.md)
   - [Adaptation policy](references/evolution-policy.md)
5. Never present a guess as a fact. When evidence is missing, list the assumption and the validation method.

For `L2` and `L3` tasks, show the contract, baseline, and execution plan first. Record the approver, approval time, approved scope, and expiry or stop condition. Without that record, do not perform production writes, batch changes, secret or permission operations, or rollout.

## Standard execution

### 1. Keep a primary Agent

The Primary Agent owns decomposition, context, conflict resolution, final integration, and the delivery decision. Work that immediately blocks the critical path stays with the Primary Agent; do not delegate merely to create parallelism.

### 2. Assign non-overlapping work packages

- `Explorer`: read-only inspection of code, logs, databases, and documents; reports facts, assumptions, and evidence.
- `Implementer`: changes only the scope defined by the contract; reports the diff, tests, and uncovered areas.
- `Verifier`: independently runs tests, replay, reconciliation, and counterexample checks; does not modify the implementation to make tests pass.
- `Operator`: checks permissions, images, deployment, canary rollout, monitoring, and rollback.

Each work package must define inputs, outputs, readable scope, writable scope, forbidden actions, verification method, and stop condition. Do not let multiple Agents write the same file concurrently.

### 3. Establish baseline and observability before changing behavior

First collect versions, metrics, logs, samples, tests, and deployment state. When the root cause is unclear, add structured observation or replay before changing retries, routing, concurrency, quotas, or similar behavior.

### 4. Make the smallest change and verify independently

Solve one confirmed problem at a time. Verification must cover the target path, failure paths, boundaries, timeouts, empty responses, retries, concurrency, and protocol compatibility. Passing tests does not prove business effectiveness.

### 5. Keep human gates for high-risk actions

Production writes, batch database changes, secrets, permissions, deletion, image pushes, and rollout require a preview, idempotency check, audit record, observation window, and rollback path. The skill never infers authorization from its own presence.

### 6. Feed knowledge back at the end

Write actual results, failed assumptions, boundaries, evidence, and next steps into a daily report, memory, FAQ, Skill, `AGENTS.md`, or regression test. Never put sensitive values into memory, logs, examples, or reports.

## Required output for complex tasks

1. Result: complete, partial, paused, or blocked.
2. Facts and evidence: code, logs, data, tests, versions, and deployment evidence.
3. Changes: actual changes to files, configuration, images, or databases.
4. Risks: unverified items, residual risks, and external dependencies.
5. Rollback: how to stop the new behavior and restore the previous state.
6. Knowledge feedback: new memory, FAQ, Skill, `AGENTS.md`, or regression samples.

## Adaptive mechanism

This skill can update low-risk personal configuration and case records, but every update must remain traceable:

1. Record an anonymized case after each applicable task: task type, selected mode, user correction, failure cause, effective practice, and result metrics.
2. A clearly repeated user preference may be written to the personal profile immediately; a one-off behavior remains a candidate rule.
3. Promote a pattern to an adaptation rule only after it appears at least three times without a counterexample.
4. Every rule must include its source, scope, creation date, review date, evidence, and counterexamples. Downgrade or revoke it when it expires or the user corrects it.
5. Prefer updating `references/personal-profile.md`, `references/casebook.md`, and `references/adapted-rules.md`, and record the change in [the learning log](references/learning-log.md).
6. Never silently relax rules about security, permissions, production release, data retention, secret handling, or core acceptance criteria. Propose such changes explicitly and state them in the result.

Use `scripts/record_case.py` to record a case. It writes only to the selected Skill directory, does not connect to external services, and does not read secrets.

## Personalization and generalization

Personal preferences affect expression, context organization, Agent selection, and knowledge sinks. The current task still determines objectives, authorization, risk gates, and evidence requirements.

The personal profile is especially useful for AI gateways, routing, Kubernetes, log data, crawlers, Agent memory, and long-running projects. For other large projects, keep the loop and risk levels, then replace domain terminology, tools, and acceptance metrics instead of forcing the original implementation details.

## References

- [Personal profile](references/personal-profile.md)
- [Task contract](references/task-contract.md)
- [Agent orchestration](references/agent-orchestration.md)
- [Evidence and acceptance](references/evidence-acceptance.md)
- [Adaptation policy](references/evolution-policy.md)
- [Casebook](references/casebook.md)
- [Learning log](references/learning-log.md)
