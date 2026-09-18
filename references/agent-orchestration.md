# Agent Roles and Orchestration

## Roles

- **Primary Agent:** defines the contract, manages context, integrates evidence, and makes the final decision.
- **Explorer:** investigates code, logs, data, and documents in read-only mode; reports facts and assumptions.
- **Implementer:** implements one minimal change within an explicit scope; reports the diff and tests.
- **Verifier:** independently tests, replays, reconciles, and searches for counterexamples; does not modify the implementation.
- **Operator:** checks permissions, deployment, monitoring, canary rollout, and rollback.

## Orchestration rules

1. Define the contract before splitting the work.
2. Give every work package one primary responsibility.
3. Do not write the same file concurrently.
4. Keep work that immediately blocks the main line with the Primary Agent.
5. Read-only roles must not modify files.
6. Verification roles must not modify the implementation to make tests pass.
7. Execute deployment, database writes, approvals, and rollback sequentially.
8. Label every output as fact, experiment, judgment, assumption, or recommendation.

## Recommended graph

```text
Primary Agent: contract and baseline
  ├─ Explorer: code/logs/data
  ├─ Explorer: previous approaches/risks
  ├─ Implementer: minimal change
  └─ Verifier: independent validation/counterexamples
Primary Agent: integration → human review → canary/rollback → knowledge feedback
```
