from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAUDE = ROOT / ".claude" / "skills"
ROOT_SKILLS = ROOT / "skills"

a = sorted(p.name for p in CLAUDE.iterdir() if p.is_dir())
b = sorted(p.name for p in ROOT_SKILLS.iterdir() if p.is_dir())

assert a == b, "Root skills mirror differs from .claude/skills"

for name in a:
    assert (CLAUDE/name/"SKILL.md").read_text(encoding="utf-8") == \
           (ROOT_SKILLS/name/"SKILL.md").read_text(encoding="utf-8"), \
           f"Skill mismatch: {name}"

assert len(a) == 85, f"Expected 85 skills, found {len(a)}"
print("PASS: root skills/ exactly mirrors all 85 Claude project skills.")
