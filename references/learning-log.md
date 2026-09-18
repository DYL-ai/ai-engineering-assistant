# Learning Log

Format:

```text
Date: YYYY-MM-DD
Task:
Triggering mode:
User correction/preference:
Practice used:
Result evidence:
Failure or counterexample:
Candidate rule:
Promotion status: no / candidate / promoted / revoked
Affected files:
Review date:
```

## Initial record

Date: 2026-09-18

Task: Extract personal AI steering practices into a reusable Skill.

Triggering mode: A long-running, multi-project engineering method spanning Codex and Claude Code.

User preference: Extract the personal method first, then generalize the reusable capability; the Skill must improve from usage patterns and concrete cases.

Initial decision: Keep personal preferences in the profile, the general workflow in `SKILL.md` and references, cases in the casebook, and rule updates with sources and review dates.

Boundary: Adaptation may update low-risk configuration and case records; it must not silently relax production, permission, secret, deletion, redaction, verification, or rollback gates.

Status: Implemented.

## Case: documentation language and release packaging

Date: 2026-09-18

Task: Publish the reusable Skill to GitHub and organize bilingual and English documentation.

Triggering mode: Public repository packaging and documentation review.

User correction/preference: Keep the previously approved English-first bilingual `README.md`; provide a standalone English `README.en.md`; translate the Skill entrypoint, references, and interface metadata into English.

Practice used: Separate the default bilingual entrypoint from the standalone English edition, add bidirectional links, translate every internal Markdown reference, and validate language coverage before publishing.

Result evidence: `quick_validate.py` passed; `record_case.py` compiled; English-only documentation check passed; GitHub commit `1217a33` published to `DYL-ai/ai-engineering-assistant`.

Failure or counterexample: The first documentation pass changed the README but left the Skill and references in Chinese. The user corrected the scope, so the partial approach is not reusable.

Candidate rule: A published Skill must validate language coverage across the entrypoint, references, examples, and interface metadata, not only the README.

Promotion status: candidate

Affected files: `README.md`, `README.en.md`, `SKILL.md`, `agents/openai.yaml`, `references/*.md`.

Review date: After the next Skill publication or documentation review.
