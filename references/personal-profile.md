# Personal Profile

This is the default configuration extracted from the user's long-term working habits. Cases and explicit user feedback may update it.

## Working preferences

- Respond in Chinese; keep code, commands, paths, and proper technical terms unchanged.
- Act and verify first, then report; never present a plan as a result.
- Prefer conclusions grounded in real logs, databases, production state, and image contents.
- Prioritize version baselines, reproducibility, tests, rollback, daily reports, and memory.
- For production changes, state the impact, observation window, rollback method, and responsibility boundary clearly.
- Do not modify business code or expand scope unless the task contract or the user explicitly authorizes it.
- After important work, write the result into a daily report, memory, FAQ, README, or regression test.

## Common work domains

- AI gateways, model routing, account pools, fallback, protocol translation, and Claude Code/Codex integration.
- PTY, containers, proxies, Kubernetes, databases, logs, and production incident response.
- Agent memory, wikis, long-session import, and team knowledge governance.
- Spider AI-Native, crawlers, dynamic-page recognition, and data-quality evaluation.

## Default orchestration

- The Primary Agent keeps the critical path and final decision.
- Explorer investigates read-only; Implementer makes the smallest change; Verifier validates independently; Operator checks release and rollback.
- Codex is often useful for code, logs, data, and regression verification; Claude Code is often useful for long workflows, plans, deployment, and knowledge organization. Choose based on actual task capabilities.

## Known risk patterns

- Memory or daily reports may be stale; verify the current version, live state, and real files first.
- Passing tests does not prove correct production behavior; validate with real data or replay.
- Similar paths, parent-directory Git repositories, old images, and the wrong working copy cause frequent misdiagnosis.
- String slicing, permissive test doubles, and unverified heuristics can introduce silent regressions.
- Production error classification, retries, cooldowns, concurrency, and lease issues require observation before logic changes.
