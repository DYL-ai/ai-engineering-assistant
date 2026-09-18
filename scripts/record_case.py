#!/usr/bin/env python3
"""Append a redacted AI-harness case to the skill learning log."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


_SECRET_PATTERNS = (
    (re.compile(r"(?i)(authorization\s*:\s*bearer\s+)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(\bbearer\s+)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(\b(?:api[_-]?key|token|secret|password|passwd)\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"\b(?:sk|fk)[A-Za-z0-9._-]{12,}\b"), "[REDACTED]"),
)


def redact(value: str) -> str:
    for pattern, replacement in _SECRET_PATTERNS:
        value = pattern.sub(replacement, value)
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Record a redacted AI-harness case")
    parser.add_argument("--skill-dir", type=Path, required=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--mode", required=True)
    parser.add_argument("--preference", default="")
    parser.add_argument("--practice", required=True)
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--counterexample", default="")
    parser.add_argument("--candidate-rule", default="")
    parser.add_argument("--status", choices=("否", "候选", "已晋升", "已撤销"), default="否")
    parser.add_argument("--impact", default="")
    parser.add_argument("--review-date", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    log_path = args.skill_dir / "references" / "learning-log.md"
    if not log_path.is_file():
        raise SystemExit(f"learning log not found: {log_path}")
    block = "\n".join(
        [
            "",
            f"日期：{date.today().isoformat()}",
            f"任务：{redact(args.task)}",
            f"触发模式：{redact(args.mode)}",
            f"用户修正/偏好：{redact(args.preference)}",
            f"采用做法：{redact(args.practice)}",
            f"结果证据：{redact(args.evidence)}",
            f"失败或反例：{redact(args.counterexample)}",
            f"候选规则：{redact(args.candidate_rule)}",
            f"是否晋升：{args.status}",
            f"影响文件：{redact(args.impact)}",
            f"复审日期：{redact(args.review_date)}",
        ]
    )
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(block + "\n")
    print(log_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
