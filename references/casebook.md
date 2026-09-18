# Casebook

Cases contain method information only after redaction. Do not record API keys, cookies, passwords, complete user inputs, or unauthorized production data.

## Seed cases

### `codex-router` production error governance

- **Scenario:** 429, 400, empty responses, SSE errors, and lease problems.
- **Effective practice:** Restore the image baseline, add structured diagnostic logs first, validate assumptions with production data, make one small change at a time, run targeted and full tests, and observe production metrics at the end.
- **Common failures:** Stale memory, the wrong working copy, test doubles that are broader than the real function, relying only on `py_compile`, and treating passing tests as proof of a business fix.
- **Reusable principles:** Verify versions first; observe before diagnosing; make small changes; verify independently; keep deployment reversible.

### `meridian` PTY shim

- **Scenario:** Claude Code runtime, PTY, Bun/Node compatibility, container proxies, and authentication.
- **Effective practice:** Separate runtime differences into sidecar behavior, offline fake-CLI smoke tests, single-turn/multi-turn matrices, and real E2E tests. Distinguish PTY, proxy, authentication, and upstream failures.
- **Reusable principles:** Run deterministic offline validation before real-environment validation; preserve runtime boundaries in error classification.

### Agent memory import

- **Scenario:** Long-session import, vector databases, Panel presentation, and knowledge-base organization.
- **Effective practice:** Reconcile counts and fields first, import in batches, make failures retryable, redact sensitive content, and cross-check import results against Panel and the underlying database.
- **Reusable principles:** Preserve raw data, make imports idempotent, isolate failures, and define permissions and lifecycle explicitly.
