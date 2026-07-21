#!/usr/bin/env python3
"""Validate the skill structure without third-party packages."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    if not SKILL.is_file():
        fail("SKILL.md is missing")

    text = SKILL.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("frontmatter is invalid")

    frontmatter = match.group(1)
    keys = re.findall(r"^([a-z][a-z0-9-]*):", frontmatter, re.MULTILINE)
    if keys != ["name", "description"]:
        fail("frontmatter must contain only name and description")
    if "name: assignment-writing-workflow" not in frontmatter:
        fail("skill name is wrong")

    links = re.findall(r"\]\((references/[^)]+)\)", text)
    if not links:
        fail("no references are linked")
    for link in links:
        if not (ROOT / link).is_file():
            fail(f"missing linked reference: {link}")

    required = {
        "agents/openai.yaml",
        "references/workflow.md",
        "references/modes-argumentative.md",
        "references/modes-empirical.md",
        "references/modes-applied.md",
        "references/evidence.md",
        "references/revision.md",
    }
    for path in required:
        if not (ROOT / path).is_file():
            fail(f"missing required file: {path}")

    combined = "\n".join(
        path.read_text(encoding="utf-8") for path in ROOT.rglob("*.md")
    )
    for term in (
        "Essay",
        "Literature Review",
        "Research Report",
        "Proposal",
        "Reflection",
        "Case Study",
        "本次任务写作逻辑",
        "no DOI found",
        "文件未说明",
        "文档1",
        "文档2",
    ):
        if term not in combined:
            fail(f"required behavior is missing: {term}")

    if "TODO" in combined:
        fail("placeholder remains")

    print("PASS: skill structure and required behavior markers")


if __name__ == "__main__":
    main()
