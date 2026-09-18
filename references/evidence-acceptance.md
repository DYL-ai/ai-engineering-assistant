# Evidence and Acceptance

## Evidence types

- **Fact:** Directly checkable in a file, code, version, log, database, or external document.
- **Experiment:** Reproducible under a fixed protocol with inputs, process, and results.
- **Judgment:** An engineering trade-off based on facts and experiments.
- **Assumption:** Not yet verified, but temporarily adopted to move the work forward.
- **Recommendation:** A proposed next action; never present it as a completed result.

## Minimum acceptance

- Objectives, non-goals, version, and risk are explicit.
- A baseline or sample exists before modification.
- Targeted tests cover the goal and at least one failure path.
- Independent validation, data reconciliation, logs, or replay provide evidence.
- Production, secret, permission, deletion, and batch actions have a human gate.
- Stop conditions, an observation window, and a rollback method exist.
- The result is recorded in a daily report, memory, FAQ, Skill, `AGENTS.md`, or regression test.

## Conclusions that must remain separate

- Passing tests ≠ business effectiveness is proven.
- A successful image build ≠ a successful production rollout.
- Existing logs ≠ a complete replay is possible.
- Successful memory write ≠ retrieved content is correct and current.
- A successful demo once ≠ a production SLO is established.
