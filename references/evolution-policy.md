# Adaptation Policy and Learning Mechanism

## Learning sources

Prioritize these sources:

1. Explicit user corrections, preferences, and long-term constraints.
2. Task contracts and acceptance results.
3. Failures, rollbacks, production incidents, and postmortems.
4. Repeated work patterns and stable metrics.
5. A one-off success without repeated validation; this remains a candidate case only.

## Promotion rules

- When the user explicitly says “do it this way from now on,” update the personal profile and record the source.
- Promote a practice to a general adaptation rule only after it appears at least three times without a counterexample.
- Every rule must include its source, scope, creation date, review date, successful evidence, and counterexamples.
- Lower the priority or revoke a rule when it expires, the user rejects it, or a counterexample appears. Never overwrite the original record.

## Content that may be updated automatically

- Personal expression and delivery preferences.
- Common project paths and knowledge sinks.
- Validated Agent role preferences.
- Investigation order for recurring failures.
- Indexes of reproduced cases and regression samples.

## Content that must never be relaxed silently

- Production, permission, secret, deletion, and batch-change gates.
- User authorization boundaries and project `AGENTS.md` constraints.
- Sensitive-data redaction rules.
- Independent verification and rollback requirements.
- The restriction against presenting assumptions, judgments, or recommendations as facts.

## Post-update review

After every update, record what changed, why it changed, which tasks it affects, how to roll it back, and when it will be reviewed. Prefer updating configuration and case records in `references/`; change `SKILL.md` only when repeated evidence shows that the entry workflow itself needs to change.
