from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
SKILLS=ROOT/".claude"/"skills"
dirs=sorted(p for p in SKILLS.iterdir() if p.is_dir())
assert len(dirs)==85, f"Expected 85 skills, found {len(dirs)}"
nums=[]; names=set()
for d in dirs:
    m=re.match(r"^(\d+)-(.+)$",d.name); assert m, d.name
    nums.append(int(m.group(1)))
    p=d/"SKILL.md"; assert p.exists(), p
    text=p.read_text(encoding="utf-8"); assert text.startswith("---\n"), p
    end=text.find("\n---",4); assert end!=-1, p
    fm={}
    for line in text[4:end].splitlines():
        if ":" in line:
            k,v=line.split(":",1); fm[k.strip()]=v.strip()
    assert fm.get("name"), f"{p}: no name"
    assert fm.get("description"), f"{p}: no description"
    assert len(fm["description"])>=40, f"{p}: weak description"
    assert fm["name"] not in names, f"duplicate {fm['name']}"
    names.add(fm["name"])
assert sorted(nums)==list(range(85)), f"numbering gap: {sorted(nums)}"
c=(ROOT/"CLAUDE.md").read_text()
assert "@.claude/gtm-routing.md" in c
assert "@.claude/gtm-artifacts.md" in c
print("PASS: 85 skills, unique metadata, continuous 00-84 numbering, CLAUDE.md imports present.")
