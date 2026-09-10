#!/usr/bin/env python3
"""Small dependency-free validator for this distributable Codex-style skill."""

from pathlib import Path
import re
import sys


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []
    required_files = (
        "SKILL.md",
        "README.md",
        "agents/openai.yaml",
        "references/workflow.md",
        "references/style-guide.md",
        "references/prompt-template.md",
        "references/prompt-checklist.md",
        "references/assets/qiuqiu-face-reference.jpg",
        "references/assets/qiuqiu-style-reference.png",
    )
    for relative in required_files:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    skill = root / "SKILL.md"
    skill_text = ""
    if not skill.is_file():
        errors.append("missing SKILL.md")
    else:
        skill_text = skill.read_text(encoding="utf-8")
        if not skill_text.startswith("---\n"):
            errors.append("SKILL.md must start with YAML frontmatter")
        else:
            closing = skill_text.find("\n---", 4)
            frontmatter = skill_text[4:closing] if closing != -1 else ""
            if closing == -1:
                errors.append("SKILL.md frontmatter is not closed")
            for field in ("name", "description"):
                match = re.search(rf"^{field}:\s*(.+)$", frontmatter, re.MULTILINE)
                if not match or not match.group(1).strip().strip('"\''):
                    errors.append(f"frontmatter field is missing: {field}")

    for markdown in root.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", markdown.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "/")):
                continue
            if not (markdown.parent / target).exists():
                errors.append(f"broken relative link in {markdown.relative_to(root)}: {target}")

    agent_config = root / "agents" / "openai.yaml"
    if agent_config.exists():
        agent_text = agent_config.read_text(encoding="utf-8")
        if "interface:" not in agent_text:
            errors.append("agents/openai.yaml is missing interface section")
        if "$qiuqiu-wechat-cover" not in agent_text:
            errors.append("agents/openai.yaml default_prompt must mention $qiuqiu-wechat-cover")

    required_phrases = (
        "2.35:1",
        "references/workflow.md",
        "references/prompt-template.md",
        "待确认",
    )
    for phrase in required_phrases:
        if phrase not in skill_text:
            errors.append(f"SKILL.md is missing required guidance: {phrase}")

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Skill validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
