# Promoted Adaptation Rules

This file contains rules validated by repeated cases that do not weaken safety boundaries. Candidate rules stay in `casebook.md` or `learning-log.md` until they meet the promotion criteria.

## Current rules

### R-001 Observe before changing production behavior

- **Source:** Repeated `codex-router` issues involving error classification, cooldowns, leases, and empty responses.
- **Scope:** AI gateways and long-running services with real traffic, retries, concurrency, quotas, or account state.
- **Practice:** Add structured diagnostics or replay first, confirm the root cause, and only then change retry, routing, cooldown, or concurrency behavior.
- **Review:** Revisit after every related production incident.

### R-002 Verify versions and working copies in the live environment

- **Source:** Misdiagnoses caused by stale memory, parent-directory Git repositories, abandoned working copies, and mismatched image versions.
- **Scope:** Environments without reliable local version control or with multiple images or project copies.
- **Practice:** Verify paths, versions, image digests, Git roots, and deployment state. Do not rely on verbal memory.
- **Review:** Revisit when the workspace or release process changes.

### R-003 Separate test results from real-world effectiveness

- **Source:** Cases where code tests passed but production data, client protocols, or real browser behavior diverged.
- **Scope:** AI gateways, crawlers, dynamic pages, Agent memory, and production deployment.
- **Practice:** Add real-data, replay, client, browser, or production-observation evidence beyond tests.
- **Review:** Revisit after a production regression that followed passing tests.
