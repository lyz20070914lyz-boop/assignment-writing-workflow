#!/usr/bin/env python3
"""Validate structure, reference routing, metadata, and core behavior markers."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
AGENT = ROOT / "agents/openai.yaml"


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
    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not name_match or not description_match:
        fail("name or description is missing")
    name = name_match.group(1).strip()
    description = description_match.group(1).strip()
    if name != "assignment-writing-workflow":
        fail("skill name is wrong")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        fail("skill name is not valid hyphen-case")
    if len(description) > 1024 or "<" in description or ">" in description:
        fail("skill description is invalid")

    linked = set(re.findall(r"\]\((references/[^)]+)\)", text))
    existing = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "references").glob("*.md")
    }
    for link in linked:
        if not (ROOT / link).is_file():
            fail(f"missing linked reference: {link}")
    unlinked = existing - linked
    if unlinked:
        fail(f"references not routed from SKILL.md: {sorted(unlinked)}")

    required = {
        "agents/openai.yaml",
        "references/workflow.md",
        "references/argument-quality.md",
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
        [text]
        + [
            path.read_text(encoding="utf-8")
            for path in sorted((ROOT / "references").glob("*.md"))
        ]
    )
    for term in (
        "快速检查",
        "标准任务",
        "完整流程",
        "受限辅助模式",
        "Rubric 映射",
        "完整论证链",
        "全文反向审阅",
        "支持强度",
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
        "Apple Translate",
    ):
        if term not in combined:
            fail(f"required behavior is missing: {term}")

    agent = AGENT.read_text(encoding="utf-8")
    agent_keys = re.findall(r"^  ([a-z_]+):", agent, re.MULTILINE)
    if agent_keys != ["display_name", "short_description", "default_prompt"]:
        fail("agents/openai.yaml interface keys are invalid")
    if "$assignment-writing-workflow" not in agent:
        fail("default prompt does not invoke the skill")
    if "流程级别" not in agent:
        fail("agent metadata does not reflect tiered routing")
    short_match = re.search(r'^  short_description:\s*"(.*)"$', agent, re.MULTILINE)
    if not short_match or not 25 <= len(short_match.group(1)) <= 64:
        fail("short_description must contain 25-64 characters")

    for placeholder in ("TODO", "TBD"):
        if placeholder in combined:
            fail(f"placeholder remains: {placeholder}")

    print("PASS: structure, routing, metadata, and behavior markers")


if __name__ == "__main__":
    main()
